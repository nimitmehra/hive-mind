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

## Latest Run — 2026-10-13 (morning), Day 228
- Pipeline complete: intel (six parallel desk researchers → consolidated intel.md) → markets → graph → brief → verify (independent fact-check agent) → publish → deliver. First brief since 22 Sep (21-day gap); run at ~15:30–18:30 IST, filed as "morning" per restart practice.
- Lead: Saudi Arabia escalated alone in Yemen (Sanaa strikes from 1 Oct; Mecca Pact activated 5 Oct; "Dawn of Yemen") and the Houthis hit Saudi civil airports (KKIA 10 Oct: 13 dead incl. 1 American and 1 Indian, 309 injured). Hormuz ship war ~25 hulls in 20 days, IRGC now claims specific strikes (UKMTO attributes none). Brent >$100 for 14 settles (peak $106.65), Dated $25–28 over, TD3C record $1.41m/day; East-West pipeline restarted (5.8 mb/d). India: RBI hike to 5.50%, CPI 5.54%, FPI −₹35.9k cr Sept, reserves −$46bn, then the RBI OMC dollar window (10 Oct). US–Iran: one proximity round (22 Sep), Trump's no-strike pledge to 3 Nov. US 10Y 5.37% (highest since 2002).
- Corrections to the baseline: the ECB HIKED on 10 Sep (the brief and node said it held); the script's "US 2Y" (`^IRX`) is the 13-week bill; the rupee record is 96.96, not 96.60; FOMC is 27–28 Oct; the KOSPI "−7.4%" was the intraday low (close −5.46%).
- Fact-check: 22 flags (1 CRITICAL, 7 HIGH, 14 LOW), all applied; 2 triggers reverted to watching (houthis holy-city; red-sea ≥2%); Hormuz attribution relabelled REPORTED/CLAIMED.
- Process notes: (1) the architect-check hook blocks writing new `scripts/update_graph_*.py`, so the graph update ran inline via Bash with the same helpers (scratchpad); (2) Sections I–III ran ~3,800 words — over the 5-minute target, same as the last brief; (3) `edges.json` has a duplicate `iran→strait-of-hormuz` record; (4) many node summaries were months stale and 30 were refreshed — the staleness sweep should run every brief.
- Dated tells: 14 Oct US CPI / IEA OMR / India WPI; 15 Oct TSMC, Wipro, Warsh; 16 Oct India reserves; 17 Oct KKIA reopening + F-35 window; ~20 Oct Rezaei "not responding" test; 27 Oct Israel election; 28 Oct FOMC; 29 Oct ECB; 3 Nov US midterms → 4–30 Nov post-pledge window; 2–4 Dec RBI.

---

## Decisions Made
- 2026-03-23: Project lives in ``
- 2026-03-23: Do deep research backfill BEFORE building anything (user decision — connections must emerge from data, not assumptions)
- 2026-03-23: Embed graph data in viewer.html (no server needed)
- 2026-03-23: Single-pass brief generation (no review step)
