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

## Latest Run — 2026-09-22 (morning), Day 207
- Pipeline complete: intel → markets → graph → brief → verify → publish → deliver (deliver-brief.py run manually per memory).
- Lead: Brent −7.7% in four sessions to $100.34 (Nov) on rhetoric + Saudi rerouting through Hormuz, no Yanbu restart; Europe Oct Saudi allocations zero; five UKMTO tanker strikes (unattributed); Trump ordered then cancelled Houthi strikes (REPORTED); Riyadh hit by Houthi missile 19 Sep; Iran's seven conditions via Qatar (REPORTED); VIX <16 ×3 trigger FIRED (complacency caveat); ECB Sept trigger resolved unfired.
- Data catches: yfinance front-month ROLL (BZ=F/CL=F/RB=F/HO=F) — market-data.py 1D figures were artefacts; used Nov contracts. India reserves baseline was stale ($675bn → $780.8bn; FCNR(B)/swap ~$133–144bn + ₹1trn OMO drain — now in `rbi`/`india`).
- Fact-check: 11 corrections (3 HIGH: "first attack on the capital" over-claim; "six houses" → five; Krieg day-count drift 10 → 11).
- Structural flag: market-data.py should print contract month / detect rolls; consider pinning explicit contract tickers around expiry.
- Open gaps: war-risk premium print (4th brief); fresh TD3C (last 15 Sep); JMIC Sept PDF (403); Qatar confirmation of the seven conditions; Trump–GCC outcome (today) — evening/next brief.
- Dated tells: 22 Sep Trump–GCC + Trump UNGA speech + Brent settle vs $100; 23 Sep Pezeshkian speech + Yanbu "days" clock + Iranian airline cliff; 25 Sep Trump–Xi readout + Krieg test expiry; 28 Sep RBI last OMO tranche; 7 Oct RBI; 28 Oct FOMC.

---

## Decisions Made
- 2026-03-23: Project lives in ``
- 2026-03-23: Do deep research backfill BEFORE building anything (user decision — connections must emerge from data, not assumptions)
- 2026-03-23: Embed graph data in viewer.html (no server needed)
- 2026-03-23: Single-pass brief generation (no review step)
