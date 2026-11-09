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

## Latest Run — 2026-11-09 (filed as "morning"; run Monday evening), Day 255
- **Pipeline complete.** Ran ~20:16–21:10 IST Monday. No brief this morning, so one full edition in the morning slot (same convention as 26 Oct, 31 Oct, 4, 6, 8 Nov); no separate evening delta. Steps: six parallel desks (20:19–20:37 IST, `date`-checked) → CoS alerts (Brent two-leg timing; IND's Trump-CNN lead; MAC's Israel Hayom lead) → consolidated `intel.md` → `markets.md` (CoS pulls 20:19 + refresh 20:45) → graph → brief → independent fact-check → corrections → local commit for the uploader → delivery.
- **Lead.** January Brent fell ~4.3% intraday (open $97.53, high $98.42, ~$94.1 at 20:35 IST, low $92.80) on the first session after the owned Qeshm strike, night six and the Riyadh hit. Outlets tie it to Trump's CNN "highly unlikely" and an Israel Hayom $8bn Hormuz-plan report (16:46–16:51 IST) that Qatari officials denied off the record; oil fell further after the denials. Jan–Dec27 spread ~$15. Pezeshkian restated the Leader's 27-Oct "end neither war nor peace" directive; Kalın claims Vance–Rezaei in Doha "next week". Night six: Iran says a US projectile hit Qeshm (unowned). UKMTO 199-26 (missed 8 Nov) and 200-26. IRGC nav-aid claim (southern strait, maybe Omani; repeats a 23-Oct claim). Houthis claim Abqaiq (unconfirmed). Nifty 25,044.65 (war high close), FII +₹7,212 cr, rupee 93.93; HY OAS 3.42% (6 Nov); Fed Dec ~82%.
- **Graph.** 40/63 nodes touched; edges 415, 6 activated, no weight changed. All 130 open triggers reviewed. **0 fired; 1 expired** (`iran` 26-Oct Tehran meeting — provisional to midnight Tehran); **1 new watch** (`oman`: confirmed damage to nav aids in Omani territory/waters, or other Iranian fire on Oman, by 30 Nov). `united-states` "resume" re-tested, stays fired (no referent clarification).
- **Deployment.** Stay defensive; re-test 14 Nov. Condition 2 met again (HY 3.42% ≤ 3.44% base); condition 1 pending the 9-Nov settle (~01:00 IST Tue); condition 3 buying leg met, CPI 12 Nov. **Hold rule amended 9 Nov:** added a fourth leg (12-Nov CPI consistent with a peak) and a second reset (confirmed Iranian fire on Oman). **Leg (b) note:** "resume" leg (b) (3+ consecutive nights) needs no ownership — Iran-attributed strikes on nights seven and eight would reset the 14-Nov date.
- **Fact-check.** 24 flags (0 critical, 10 high, 14 low), all applied, plus G1–G8. Highs: nav-aid claim is a 23-Oct repeat (Signal recast); Pezeshkian's line restates 27 Oct and the Leader does issue texts; "went unpriced" (Reuters had ship hits supporting the Asian morning); tracker figure presented as an outlet link; leg (b) ownership gap; "all three conditions"; unlabelled hold-rule additions; "Trump turns on Israel" (he described voters); `oman` watch stated a claim as fact.
- **Process notes.**
  - **(1)** CoS framing again drew every HIGH (Signal, lead framing, deployment). Desk facts and all Page 2 numbers held.
  - **(2)** **Check "new" claims against prior weeks before building a Signal on them** — the desk did not search for earlier versions of the nav-aid claim. Same for "the Leader ordered": grep the graph for the directive first.
  - **(3)** Leg (a) and leg (b) of "resume" have different attribution standards; state which leg a ruling rests on.
  - **(4)** Length: Sections I–III ~3.4k words after corrections (3.05k at draft) — still over target.
  - **(5)** A CoS alert was mis-stamped "20:30 IST" (sent ~20:21) — corrected by follow-up message; run `date` before stamping alerts too.
  - **(6)** Carried over: 24 duplicate edge pairs; node budgets over 2k tokens.
- **Open at publish.**
  - The 9-Nov January Brent settle (~01:00 IST Tue): ING's $94.62, deployment condition 1, the $103.24 leg.
  - Qatar's PM in the Oval Office (22:30 IST) — re-test `qatar` and `trump` ceasefire.
  - Night seven; any US ownership of nights five/six; Oman/UKMTO on the nav-aid site.
  - The `iran` expiry becomes final at midnight Tehran.
- **Dated tells.**
  - 10 Nov: NSE shut; US CPI 19:00 IST; Knesset sworn in; CoreWeave; China trade; G7 day two; Abu Dhabi talks (10–11).
  - 11 Nov: India reopens; CIBC's $100 date; Hegseth vote by Wed. 12 Nov: India CPI. 13 Nov: RBI reserves; CFTC. 14 Nov: hold-rule re-test; Ghaani's clock.
  - ~15 Nov AP's Syrian "within a week"; 17 Nov Nvidia; ~20 Nov Kalın's Doha test; mid-Nov *Roosevelt*; 29 Nov OPEC+; ~30 Nov January Brent expiry.
  - 4 Dec RBI; 9 Dec FOMC; ~11 Dec US funding deadline; 17 Dec ECB; 3 Jan new Congress.

---

## Decisions Made
- 2026-03-23: Project lives in ``
- 2026-03-23: Do deep research backfill BEFORE building anything (user decision — connections must emerge from data, not assumptions)
- 2026-03-23: Embed graph data in viewer.html (no server needed)
- 2026-03-23: Single-pass brief generation (no review step)
