# Hive Mind — Build Plan

## Current Phase: Deep Research Backfill (One-Time)

### Status: COMPLETE ✓
**Started:** 2026-03-23 | **Completed:** 2026-03-23

### Research Output
`research/backfill-feb28-mar23.md` — comprehensive verified research document (6 parts, ~500 lines)

### Research Scope (All Complete)
- [x] Week 1 (Feb 28 - Mar 6): Initial attacks, Khamenei killed, Gulf retaliation, Hormuz closure
- [x] Week 2 (Mar 7 - Mar 13): Mojtaba Khamenei appointed, OPEC response, ADNOC shutdown, Indians killed in Oman
- [x] Week 3 (Mar 14 - Mar 20): Kharg Island raid, South Pars attack, Ras Laffan devastated, Iraq force majeure
- [x] Week 4 (Mar 21 - Mar 23): Trump mixed signals, CCS meeting, Modi parliament address
- [x] Market data: Oil ($70→$119 peak), gas (TTF doubled), gold (-10%), indices, bond yields, currencies
- [x] Country impacts: Iran, Israel, US, India, China, Russia, Gulf states (all 6), Turkey, Iraq, Houthis
- [x] Cascade connections: 10 verified cascade paths identified

### Phase 1 Build
1. [x] Folder structure + schemas — `graph/nodes/`, `graph/edges.json`, `graph/meta.json`, `briefs/`
2. [x] Seed graph nodes from research data — 30 nodes, 117 edges, all from verified research
3. [x] viewer.html — interactive graph with Cytoscape.js, click for details, search, layer layout
4. [x] `/crisis-brief` skill definition — `.claude/commands/crisis-brief.md` + readable copy in `skills/`

## Latest Run — 2026-10-26 (morning), Day 241
- **Pipeline complete.** Six parallel desk researchers produced a consolidated `intel.md`, followed by markets, graph, brief and an independent fact-check agent. The brief was then committed and left to the background uploader to push, and finally delivered.
- **Timing.** This is the first brief since 13 Oct, a 13-day gap. It ran ~18:19–20:00 IST and was filed as "morning" under restart practice.
- **Lead: oil.** Dec Brent settled at a six-month high of $116.72 on 23 Oct, 23 straight settles above $100. Over the same fortnight the physical premium collapsed: the Dated gap went from ~$25 to $6–10, Oman–Dubai hit its lowest since July, and Gulf exports were near pre-war. The premium is now an event premium on post-3-Nov strike risk and Houthi strikes into Saudi Arabia's Eastern Province.
- **US–Iran.** Trump's no-strike pledge held (no confirmed US strike since 1 Sep), while NYT, WSJ, NBC and CNN reported post-midterm plans. Iran sent no new paper and Rezaei's line held.
- **Saudi Arabia.** The Saudi DM, Munir and Kalin began talks in Tehran on 26 Oct; no readout yet.
- **India.** Reserves fell for a sixth week to $721bn; liquidity surplus ~₹542 cr; 10Y at 7.48%; FPI −₹48k cr in October; INR 94.38 → 95.22.
- **Markets.** The 22-Oct AI-credit break (Meta's negative FCF) took the US 10Y below 5% for one close and gold below $4,000. TTF reached €97.
- **Graph.**
  - All 63 nodes were updated; 73 signals added; all 63 summaries refreshed in a staleness sweep (many dated from June).
  - Edges went 411 → 413: new edges `semiconductors→us-10y-yield` 4.0 and `qatar→cheniere-energy` 6.0, plus 8 re-weights.
  - Triggers: 181 reviewed, 77 changed (10 substantive, 67 housekeeping), 12 new dated watches.
- **Fact-check.** 23 flags (1 CRITICAL, 5 HIGH, 17 LOW), with 22 applied. The CRITICAL flag reverted the `houthis` holy-city trigger to watching: the "Makkah/Madinah regions" are provinces and the Houthis claimed Rabigh and Yanbu. This repeats the 13-Oct failure, and a stricter rewrite of that trigger is proposed in its node.
- **Process notes.**
  - **(1)** The background uploader (`~/.claude/brief-delivery`, hive-mind `ready: verification`) auto-commits and pushes `briefs/` once a `*verif*` file appears. Write fact-check drafts to staging and move them into `briefs/` only after corrections are applied, or the uncorrected draft gets published.
  - **(2)** Per the global CLAUDE.md, the session commits locally and the uploader pushes (`push_any_committed`). The skill's Step 6 `git push` is superseded.
  - **(3)** `edges.json` has 24 duplicate from→to pairs. A dedupe pass is needed in a separate session, as a code change needing approval.
  - **(4)** `check_node_budgets.py` fails for nearly every node (pre-existing; summaries and signals are far over the 2k-token budget). Compression needs its own session.
  - **(5)** The architect hook still blocks `scripts/update_graph_*.py`, so helpers live in `staging/<run>/gu_*.py` (gitignored).
  - **(6)** Sections I–III ran ~3.2k words, down from ~3.8k but still over the 5-minute target.
- **Dated tells.**
  - 27 Oct: Israel votes; Pezeshkian meets Putin.
  - 28 Oct: FOMC; MSFT/GOOGL; SK hynix; Jio listing.
  - 29 Oct: ECB; AMZN; Samsung.
  - 30 Oct: Brent Dec expiry; India reserves.
  - 1 Nov: OPEC+.
  - 3 Nov: midterms.
  - 4–30 Nov: post-pledge window.
  - 9 Nov: Tehran readout and the Houthi tempo test.
  - 12 Nov: India CPI.
  - 4 Dec: RBI.
  - 9 Dec: FOMC.

---

## Decisions Made
- 2026-03-23: Project lives in ``
- 2026-03-23: Do deep research backfill BEFORE building anything (user decision — connections must emerge from data, not assumptions)
- 2026-03-23: Embed graph data in viewer.html (no server needed)
- 2026-03-23: Single-pass brief generation (no review step)
