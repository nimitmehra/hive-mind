#!/usr/bin/env python3
"""One-time migration: compress every node JSON to bounded hot-tier structure.

Per ARCHITECTURE_NODE_TIERING.md:
- Hot tier per node: ~1,500 tokens hard cap
- Last 7 days of signals -> recent_signals (full content)
- Older signals grouped by month -> 1 bullet per month in historical_summaries
- Top 5 watching/active triggers (resolved dropped)
- Top 10 edges by weight (full set still in edges.json)
- Validate token budget; warn on outliers

Git history retains every prior state of every node, so dropped signal text
is recoverable via `git show <commit>:graph/nodes/<id>.json`.

Usage:
    python3 scripts/migrate_nodes_compress.py            # run on all nodes
    python3 scripts/migrate_nodes_compress.py --dry-run  # report only, no writes
    python3 scripts/migrate_nodes_compress.py iran       # specific node(s)
"""
import argparse
import json
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NODES_DIR = ROOT / "graph" / "nodes"

TODAY = date(2026, 5, 4)
RECENT_WINDOW_DAYS = 7
HISTORICAL_MAX_MONTHS = 3
ACTIVE_TRIGGERS_MAX = 5
TOP_EDGES_MAX = 8
RECENT_SIGNALS_MAX = 5
TOKEN_BUDGET = 1500
BYTES_PER_TOKEN = 3.5  # JSON-density estimate, calibrated from observed sizes


def estimate_tokens(obj):
    """Estimate token count by serialized byte length / chars-per-token."""
    s = json.dumps(obj, ensure_ascii=False)
    return int(len(s) / BYTES_PER_TOKEN)


def parse_date(s):
    """Parse YYYY-MM-DD; return None on failure."""
    try:
        parts = s.split("-")
        return date(int(parts[0]), int(parts[1]), int(parts[2]))
    except (ValueError, IndexError, AttributeError):
        return None


def signal_to_headline(sig):
    """Compress a full-content signal into a headline entry.

    Full content stays in git history. Headline + 2 top sources + verification
    tag are enough for daily pipeline reads. Fact-checker uses git for full text.
    """
    content = sig.get("content", "")
    headline = content.split("[")[0]
    if ". " in headline:
        headline = headline.split(". ")[0]
    headline = headline.strip()[:120]  # tighter than before

    verif = sig.get("verification", sig.get("significance", ""))
    if verif and len(verif) > 50:
        verif = verif.split(".")[0][:50]

    return {
        "date": sig.get("date", ""),
        "headline": headline,
        "sources": sig.get("sources", [])[:2],  # top 2 sources only; rest in git
        "verification": verif,
    }


def group_signals(signals):
    """Split signals into recent (last 7 days) and historical (older, grouped by month)."""
    cutoff = TODAY - timedelta(days=RECENT_WINDOW_DAYS)
    recent = []
    by_month = {}  # "YYYY-MM" -> list of signals

    for sig in signals or []:
        d = parse_date(sig.get("date", ""))
        if d is None:
            # Skip signals without parseable dates; preserved in git
            continue
        if d >= cutoff:
            recent.append(sig)
        else:
            month_key = f"{d.year:04d}-{d.month:02d}"
            by_month.setdefault(month_key, []).append(sig)

    # Sort recent newest-first; convert to headline form for size
    recent.sort(key=lambda s: s.get("date", ""), reverse=True)
    recent = [signal_to_headline(s) for s in recent[:RECENT_SIGNALS_MAX]]
    return recent, by_month


def summarize_month(month_key, signals):
    """Produce a one-line auto-summary for a month group.

    Mechanical synthesis (count + first-line of top signals). The /update-graph
    skill should re-synthesize these into proper prose on the next material
    activity. Marked auto:true so the skill knows to refresh.
    """
    if not signals:
        return None
    high_sig = [s for s in signals if s.get("significance") == "high"]
    target = high_sig[:3] if high_sig else signals[:3]

    snippets = []
    for s in target:
        c = s.get("content", "")
        first = c.split("[")[0]  # strip "[CONFIRMED]" tags
        first = first.split(".")[0][:140].strip()
        if first:
            snippets.append(first)

    summary = f"{len(signals)} signals. " + " | ".join(snippets)
    if len(summary) > 600:
        summary = summary[:597] + "..."

    return {
        "period": month_key,
        "summary": summary,
        "signal_count": len(signals),
        "auto": True,
    }


def filter_triggers(triggers):
    """Keep only watching/active triggers, max ACTIVE_TRIGGERS_MAX, compressed.

    Drops verbose `mechanism` field (preserved in git). Keeps condition,
    status, cascade list, and added date — enough for the daily pipeline
    to understand what's being watched.
    """
    if not triggers:
        return []
    keep = [
        t for t in triggers
        if t.get("status", "").lower() in {"watching", "active", "partially-activated"}
    ]
    compressed = []
    for t in keep[:ACTIVE_TRIGGERS_MAX]:
        compressed.append({
            "condition": t.get("condition", "")[:200],
            "status": t.get("status", "watching"),
            "cascade": t.get("cascade", [])[:5],
            "added": t.get("added", ""),
        })
    return compressed


def select_top_edges(edges):
    """Keep top TOP_EDGES_MAX edges by weight, descending. Drops verbose context.

    Edge `context` field can be multi-paragraph in old nodes. Keep only to,
    type, weight, directness, last_activated, activation_count. Full edge
    set is preserved separately in graph/edges.json and in git.
    """
    if not edges:
        return []
    sorted_edges = sorted(edges, key=lambda e: e.get("weight", 0), reverse=True)
    compressed = []
    for e in sorted_edges[:TOP_EDGES_MAX]:
        compressed.append({
            "to": e.get("to", ""),
            "type": e.get("type", "")[:80],
            "weight": e.get("weight", 0),
            "directness": e.get("directness", 1),
            "last_activated": e.get("last_activated", ""),
            "activation_count": e.get("activation_count", 0),
        })
    return compressed


def compress_current(current):
    """Truncate any long string values in current dict.

    Some nodes have current fields with multi-sentence prose that should
    be one-line. Cap each value at 200 chars.
    """
    if not isinstance(current, dict):
        return current
    out = {}
    for k, v in current.items():
        if isinstance(v, str) and len(v) > 200:
            out[k] = v[:197] + "..."
        else:
            out[k] = v
    return out


SUMMARY_TARGET_CHARS = 1700  # ~485 tokens; leaves room for triggers/edges/signals/historical


def truncate_summary(summary, target_chars=SUMMARY_TARGET_CHARS):
    """Truncate summary to target_chars at sentence boundary.

    Keeps the FIRST portion (which is usually the most current state in this
    codebase's writing pattern - newer summaries appended PRIOR SUMMARY at end).
    Marked [TRUNCATED] so /update-graph knows to re-synthesize.
    """
    if len(summary) <= target_chars:
        return summary
    chunk = summary[:target_chars]
    # Cut at last sentence boundary
    if ". " in chunk:
        chunk = chunk.rsplit(". ", 1)[0] + "."
    return chunk + " [TRUNCATED — needs re-synthesis]"


def compress_node(node):
    """Apply bounded hot-tier transformation. Returns (new_node, warnings, tokens)."""
    warnings = []

    # Pre-truncate summary upfront (was the dominant token consumer)
    summary = node.get("summary", "")
    if len(summary) > SUMMARY_TARGET_CHARS:
        summary = truncate_summary(summary)

    new_node = {
        "id": node["id"],
        "name": node.get("name", node["id"]),
        "type": node.get("type", "other"),
        "created": node.get("created", ""),
        "last_updated": node.get("last_updated", ""),
        "summary": summary,
        "current": compress_current(node.get("current", {})),
    }

    new_node["active_triggers"] = filter_triggers(node.get("trigger_points", []))
    new_node["top_edges"] = select_top_edges(node.get("edges", []))

    recent, by_month = group_signals(node.get("signals", []))
    new_node["recent_signals"] = recent

    historical = []
    for month_key in sorted(by_month.keys()):
        bullet = summarize_month(month_key, by_month[month_key])
        if bullet:
            historical.append(bullet)
    historical = historical[-HISTORICAL_MAX_MONTHS:]
    new_node["historical_summaries"] = historical

    tokens = estimate_tokens(new_node)

    # Layered enforcement if over budget
    if tokens > TOKEN_BUDGET:
        # Step 1: shrink recent_signals to 5 if currently more
        if len(new_node["recent_signals"]) > 5:
            new_node["recent_signals"] = new_node["recent_signals"][:5]
            tokens = estimate_tokens(new_node)

    if tokens > TOKEN_BUDGET:
        # Step 2: shrink historical to 4 months
        if len(new_node["historical_summaries"]) > 4:
            new_node["historical_summaries"] = new_node["historical_summaries"][-4:]
            tokens = estimate_tokens(new_node)

    if tokens > TOKEN_BUDGET:
        # Step 3: truncate summary
        # Calculate budget for summary: total target minus other components
        other_tokens = tokens - estimate_tokens({"summary": new_node["summary"]})
        summary_budget = TOKEN_BUDGET - other_tokens - 50  # safety margin
        if summary_budget > 100:
            new_node["summary"] = truncate_summary(new_node["summary"], summary_budget)
            tokens = estimate_tokens(new_node)

    if tokens > TOKEN_BUDGET:
        warnings.append(
            f"OVER_BUDGET: {tokens} tokens (cap {TOKEN_BUDGET}) after enforcement; "
            f"summary={len(new_node['summary'])} chars, "
            f"recent_signals={len(new_node['recent_signals'])}, "
            f"historical={len(new_node['historical_summaries'])}"
        )

    return new_node, warnings, tokens


def measure_original(node):
    return estimate_tokens(node)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Report only; do not write")
    parser.add_argument("nodes", nargs="*", help="Specific node IDs (default: all)")
    args = parser.parse_args()

    if args.nodes:
        targets = [NODES_DIR / f"{n}.json" for n in args.nodes]
    else:
        targets = sorted(NODES_DIR.glob("*.json"))

    print(f"Migrating {len(targets)} nodes (dry-run={args.dry_run})...")
    print(f"Target: {TOKEN_BUDGET} tokens/node, recent={RECENT_WINDOW_DAYS}d, history={HISTORICAL_MAX_MONTHS}mo")
    print("=" * 100)

    total_before = 0
    total_after = 0
    over_budget = []

    for path in targets:
        if not path.exists():
            print(f"  MISS: {path.name}")
            continue

        with open(path) as f:
            node = json.load(f)

        before_tokens = measure_original(node)
        new_node, warnings, after_tokens = compress_node(node)

        total_before += before_tokens
        total_after += after_tokens

        status = "OK" if after_tokens <= TOKEN_BUDGET else "WARN"
        delta = before_tokens - after_tokens
        print(
            f"  [{status:4}] {path.stem:35} "
            f"{before_tokens:>6} -> {after_tokens:>5} tokens  "
            f"(saved {delta:>6}, "
            f"signals: {len(node.get('signals', []))} -> "
            f"{len(new_node['recent_signals'])} recent + "
            f"{len(new_node['historical_summaries'])} mo bullets)"
        )

        for w in warnings:
            print(f"        {w}")
            over_budget.append((path.stem, after_tokens))

        if not args.dry_run:
            with open(path, "w") as f:
                json.dump(new_node, f, indent=2, ensure_ascii=False)

    print("=" * 100)
    print(f"TOTAL: {total_before:,} -> {total_after:,} tokens (saved {total_before - total_after:,})")
    if total_before > 0:
        print(f"Reduction: {total_after / total_before * 100:.1f}% of original")
    if over_budget:
        print(f"\nOVER BUDGET ({len(over_budget)} nodes):")
        for name, t in over_budget:
            print(f"  {name}: {t} tokens")
    else:
        print("\nAll nodes within budget.")


if __name__ == "__main__":
    main()
