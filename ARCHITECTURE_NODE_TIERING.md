# Architecture Decision: Bounded Node Files with Git as Audit Trail

**Status:** Proposed (2026-05-03) — pending migration
**Decision-makers:** Nimit Mehra (PO), Claude (architect)
**Supersedes:** Implicit "append-only signals" pattern in current node schema

---

## Context

The hive-mind graph holds 49 node JSON files under `graph/nodes/`. Each daily brief appends signals to the affected nodes. After 65 days of operation, several nodes exceed 60K tokens — `iran.json` alone is 62K tokens, larger than the Read tool's 89K-token per-call cap.

### Measured token state (2026-05-03)

| Statistic | Value |
|---|---|
| Total nodes | 49 |
| Total tokens (all node files) | ~643,000 |
| Average per node | ~13,100 |
| Largest node (iran) | 61,607 |
| Top 10 nodes combined | ~289,000 |
| Days of operation | 65 |
| Daily growth rate | ~10,000 tokens/day across graph |

At current rate, total tokens would exceed 1M context window by Day ~120. The system is already broken on read budget — `iran.json` cannot be read in a single call.

### Token consumers

- **`rebuild-viewer.py`** — globs all node JSONs, embeds them in `viewer.html` as `const GRAPH_DATA = {...}`. Result: `viewer.html` is 2.7MB.
- **Daily update scripts** (`scripts/update_graph_*.py`) — load each affected node, mutate, save.
- **Skills run by Claude** — `gather-intel`, `update-graph`, `write-brief`, `verify-brief` all read node JSONs through the Read tool.
- **Browser viewer** — loads the embedded `GRAPH_DATA` blob.

---

## Problem

The current schema conflates three different things into one append-only `signals[]` array:

1. **Institutional memory** — what the node *means* now (belongs in `summary`)
2. **Live state tracking** — what's active right now (belongs in `current`, `active_triggers`)
3. **Audit trail** — what was claimed when, with what evidence (currently in `signals[]`)

Append never trims. Files grow unboundedly. Read budget breaks. Synthesis quality degrades because the summary becomes commentary on top of accumulating signals rather than the actual institutional memory.

---

## Decision

**Bound each node file at ~1,500 tokens. Use git history as the audit trail.**

No new files. No subdirectories. No parallel `.jsonl` audit logs. One file per node, capped, with rolling rolloff.

### Why git is sufficient

The project already commits daily with the brief. Every state of every node at every date is preserved in git. To audit a claim from Day 15:

```bash
git log -p graph/nodes/iran.json          # Every change to this node
git show HEAD~50:graph/nodes/iran.json    # State on any past commit
git log --all -S "rial 1.8M"              # Find when we first claimed this
```

Adding a parallel `signals.jsonl` would duplicate what git already provides.

---

## Schema (target ~1,500 tokens per node)

```jsonc
{
  "id": "iran",
  "name": "Iran",
  "type": "country",
  "created": "2026-03-23",
  "last_updated": "2026-05-03",

  // ~500 tokens — institutional memory; does real synthesis work
  "summary": "Day 65. Iran delivered 14-point counter-proposal via Pakistan...",

  // ~100 tokens — live state snapshot
  "current": {
    "rial_freemarket": "1.83M/USD (May 2)",
    "oil_exports_bpd": 567000,
    "blockade_day": 65
  },

  // max 5; resolved triggers are absorbed into summary, not retained here
  "active_triggers": [
    {"condition": "...", "status": "watching", "added": "2026-04-23"}
  ],

  // max 10 by weight; full edge graph still lives in edges.json
  "top_edges": [
    {"to": "trump", "weight": 8.0, "type": "..."}
  ],

  // last 7 days, max ~7 entries; older drop from file (preserved in git)
  "recent_signals": [
    {"date": "2026-05-03", "headline": "...", "verification": "CONFIRMED"}
  ],

  // rolling 6 months, 1 bullet per month
  "historical_summaries": [
    {"period": "2026-03", "summary": "War begins Feb 28..."}
  ]
}
```

### Hard rules

1. Hot-tier file MUST be ≤ 1,500 tokens. Enforced at write time.
2. `recent_signals` keeps last 7 days max, hard cap of 10 entries.
3. `active_triggers` keeps only `watching` and `active` status. Resolved triggers move into `summary`.
4. `top_edges` keeps top 10 by weight. Full edge graph is in `graph/edges.json`.
5. `historical_summaries` keeps rolling 6 months. Older bullets drop.
6. When file exceeds 1,500 tokens after a write: drop oldest signal, then oldest historical bullet, then force summary refresh.

---

## Migration plan

One commit, ~1 hour total.

1. **`scripts/migrate_nodes_compress.py`** (one-time):
   - For each node, read full JSON
   - Group signals by month → write one compressed bullet per month into `historical_summaries`
   - Keep last 7 days of signals as `recent_signals` (full content)
   - Keep top 5 watching/active triggers; drop resolved
   - Keep top 10 edges by weight (full set still in `edges.json`)
   - Validate file ≤ 1,500 tokens; if over, force summary compression
   - Save back to same path
2. **`scripts/check_node_budgets.py`**: validates every node ≤ 1,500 tokens. Run pre-commit.
3. **Update `update-graph` skill** with cap-enforcement paragraph and the rolloff rule.
4. **One commit**: `"Migrate node files to bounded hot-tier structure (~643K → ~73K tokens; git retains full history)"`.
5. **Validate**: run `rebuild-viewer.py`, confirm viewer works, confirm next daily brief runs.

### Expected outcome

| Metric | Before | After | Reduction |
|---|---|---|---|
| Total node tokens | ~643,000 | ~73,000 | **8.8×** |
| Largest node | 61,607 | ≤1,500 | **41×** |
| `viewer.html` size | 2.7 MB | ~0.4 MB | **6×** |
| Daily pipeline context load | ~250–450K | ~30–45K | **~10×** |

---

## Alternatives considered

### A. Tiered subdirectories (originally proposed)
```
graph/nodes/iran.json              # hot
graph/nodes/iran/signals.jsonl     # warm
graph/nodes/iran/snapshots/*.json  # cold
```
**Rejected:** Adds 49 subdirectories + ~150 archive files. Requires `rebuild-viewer.py` modifications. Dual-write complexity in update scripts. Duplicates what git already provides.

### B. Sibling `.jsonl` audit log
```
graph/nodes/iran.json
graph/nodes/iran.signals.jsonl
```
**Rejected for same reason as A:** parallel audit log duplicates git. Doubles file count without benefit.

### C. Top-level signals/ directory
```
graph/nodes/iran.json     # pure schema, no signals
graph/signals/iran.jsonl  # full audit trail
```
**Rejected:** cleanest separation conceptually but still duplicates git.

### D. Single bounded file, git as archive — **CHOSEN**
See above.

### E. Markdown nodes
```
graph/nodes/iran.md  # YAML frontmatter + markdown body
```
**Rejected:** breaks `rebuild-viewer.py` (would need markdown→JSON parsing). Loses programmatic schema. Major migration cost. Not warranted by the problem.

### F. SQLite database
```
graph/graph.db  # tables: nodes, signals, edges, triggers
```
**Rejected:** breaks every existing script. Loses git diffability of state changes. Massive migration cost. Solving a different problem (querying) than the actual problem (token budget).

---

## Operational rules going forward

### When to update the summary (the most important rule)
The summary IS the institutional memory. It should be rewritten when any of:
- A material event materially changed the situation
- A trigger resolved (resolution context absorbs into summary)
- A signal in `recent_signals` is about to roll off (capture its essence in summary first)

### When to drop a resolved trigger
When status moves to `resolved`, capture one sentence about how it resolved into the `summary`, then remove the trigger entry. The git commit for that day preserves the full trigger text.

### Auditing a past claim
1. Find the brief that made the claim (`briefs/YYYY-MM-DD-*.md`)
2. Look at the git commit for that brief: `git show <sha>:graph/nodes/<id>.json`
3. The node state at that commit was the basis for the brief

### When the file would exceed 1,500 tokens after a write
The update helper enforces in this order:
1. Drop oldest signal from `recent_signals`
2. If still over, drop oldest entry from `historical_summaries`
3. If still over, force a summary refresh (collapse older content into denser prose)
4. If still over after summary refresh, the input signal is too verbose — compress it

---

## Blast radius / non-impacts

| Component | Impact |
|---|---|
| `rebuild-viewer.py` | **None** — still globs `graph/nodes/*.json`. Receives smaller blobs; outputs smaller `viewer.html`. |
| Daily `update_graph_*.py` scripts | **One helper added** — `cap_and_rolloff(d)`. Existing scripts continue working without it. |
| Browser `viewer.html` | **None** — JSON shape compatible. Loads faster. |
| Skills (`gather-intel`, `update-graph`, `write-brief`, `verify-brief`) | **One new instruction** — "for older signal text, use `git log -p graph/nodes/<id>.json`". |
| `graph/edges.json` | **None** — parallel structure unchanged. |
| `graph/meta.json` | **None** — parallel stats unchanged. |
| `briefs/*.md` | **None** — not programmatically dependent on node schema. |
| Existing daily backfill scripts | **None** — they ran once, already in git. |

---

## Risk and mitigation

| Risk | Mitigation |
|---|---|
| Migration script over-compresses summary, loses signal | Run on copy first; validate every node by hand before committing |
| Cap forces summary degradation over time | Periodic review (e.g., end of each month) — if summary quality drops, raise cap selectively |
| Fact-checker workflow slower (git lookup vs file read) | One-time skill update documents the new workflow; affects rare operation |
| Some node has structurally more state than 1,500 tokens fits | Per-node cap override allowed, but must be justified in node frontmatter |

---

## Open questions

1. **Cap value: 1,500 vs 2,000 tokens?** Conservative 1,500 forces tighter synthesis. Looser 2,000 gives breathing room. Recommendation: **1,500** with allowance for explicit overrides per node.
2. **Resolved trigger retention: how many in summary?** Recommendation: **last 3 resolved** mentioned as one-liners in summary; older absorbed into prose.
3. **Pre-commit budget check: hard fail or warn?** Recommendation: **warn for first 30 days, hard fail after**.
4. **`edges.json` redundancy:** node files embed top edges; `edges.json` has the full graph. Should they be derived from one source? **Out of scope for this decision; revisit separately.**

---

## Implementation status

- [ ] `scripts/migrate_nodes_compress.py` written
- [ ] Migration validated on top 3 nodes (iran, united-states, strait-of-hormuz) before full sweep
- [ ] All 49 nodes migrated
- [ ] `scripts/check_node_budgets.py` written
- [ ] `update-graph` skill updated with cap-enforcement rule
- [ ] One commit landed
- [ ] `rebuild-viewer.py` validated post-migration
- [ ] Next daily brief runs cleanly
