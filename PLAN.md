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

## Latest Run — 2026-11-03 (morning), Day 249
- **Pipeline complete.** Six parallel desks (~13:16–13:39 IST) → consolidated `intel.md` → `markets.md` (CoS direct pulls) → graph → brief → independent fact-check → corrections → local commit for the uploader → delivery.
- **Timing.** Ran ~13:11–14:20 IST on Tuesday (US Election Day). Filed as "morning" under restart practice (3-day gap; no morning baseline). Last full session everywhere: Mon 2 Nov.
- **Lead.** Oil fell 7.6% on deal talk (Jan Brent $113.43 → $104.77), and that night, per US officials, a US jet struck an IRGC launcher on Qeshm. The WSJ says it was one of a weeks-long quiet series. The strike is REPORTED (7+ outlets, own officials; IRNA blasts); there is no on-record confirmation.
- **Other items.**
  - **Ship war:** an Indian was killed on the India-flagged dhow *Al Jusufi* off Limah (2 Nov; MEA names no attacker); UKMTO logged 3 attacks on 1 Nov (Kuwait-origin tanker, UAE tug).
  - **Iran's blacklist:** +114 ships (~240), incl. KOTC, Bahri and ADNOC (REPORTED).
  - **Physical oil:** Bloomberg has Gulf exports at 15.53 mb/d and Dubai in contango (REPORTED).
  - **India:** Nifty 23,440.80 (highest close since 23 Sep); the rupee barely moved (RBI/SBI dollar buying; forward book a record $239.2bn).
  - **AI funding scare:** Nasdaq-100 in correction; KOSPI/TAIEX −3.6%.
  - **Houthi test:** failed on unattributed Riyadh-region drones.
  - **Israel:** no 61-seat path.
  - **Gas:** TTF ~€95.
- **Graph.**
  - 61/63 nodes touched. Edges 413 → 414 (new `china → saudi-arabia` 4.0); `united-states → irgc` 6.5 → 7.5.
  - 132 open triggers reviewed; 11 status changes, 2 amended, 7 new.
  - **Fired:** Indian seafarer/India-flagged hull (CONFIRMED).
  - **Breach reported:** the pledge trigger. Resolve next brief: broken if confirmed on the record, else expired.
  - **Failed:** Houthi tempo. **Resolved:** OPEC+ (pause). **Expired:** 6 dated watches, provisional to end-3 Nov ET.
  - **Redefined:** `united-states` "strikes resume 4–30 Nov" — on-record (not a single response to fire), 3+ nights, multi-site/beyond-launcher targets, or nuclear/energy/leadership — and the matching `brent-crude` <$100 test.
- **Fact-check.** 24 flags (0 critical, 9 high, 15 low), all applied, plus 11 graph corrections (G1–G11). Highs:
  - the strike stated as fact in two sentences;
  - "March first below $100" was false;
  - "no written reply" stated as fact;
  - the "ball in America's court" line misattributed to Aref;
  - India/Korea flows on different days;
  - the Signal's "largely on state fleets" claim was unsupported;
  - the Pusztai test scored wrongly;
  - the pledge trigger set "broken" below its own 31-Oct threshold;
  - the redefined strike trigger turned on Washington's "self-defence" label.
- **Process notes.**
  - **(1)** Two desks again wrote guessed sweep times (SAU, IND); corrected from file mtimes. **Add "run `date` before writing any time" to `_brief_for_agents.md` next run.**
  - **(2)** Before resolving a trigger, read its prior dated notes for the threshold it set itself (the 31-Oct note on the pledge required on-record confirmation).
  - **(3)** Before writing "first"/"record" about a contract or index, check the whole curve and history (June Brent was already below $100).
  - **(4)** Sections I–III ran ~3.3k words after corrections. Still over the 5-minute target.
  - **(5)** Carried over: 24 duplicate from→to pairs in `edges.json`; node budgets far over 2k tokens; the architect hook blocks `scripts/update_graph_*.py`, so helpers live in `staging/<run>/gu_*.py`.
- **Open at publish.**
  - Tuesday's India FII figure (~18:00 IST): if positive, the `nifty-50` capital-substitution trigger fires next brief.
  - The Vance-reply trigger on its final day.
  - US election results.
- **Dated tells.**
  - 4 Nov: strike window opens (redefined); Israel certification and Herzog consultations; EZ flash HICP (3.9%).
  - ~4–5 Nov: Aramco December OSP.
  - 6 Nov: India reserves (first FCA >$3bn test); US payrolls.
  - 9 Nov: Tehran-meeting text deadline.
  - 11 Nov: Herzog's choice.
  - 12 Nov: India CPI.
  - 13 Nov: rupee 94.50 test.
  - 17 Nov: Nvidia.
  - Mid–late Nov: Roosevelt.
  - 29 Nov: OPEC+ 2027.
  - 30 Nov: most new watches.
  - 4 Dec: RBI. 9 Dec: FOMC. 17 Dec: ECB.

---

## Decisions Made
- 2026-03-23: Project lives in ``
- 2026-03-23: Do deep research backfill BEFORE building anything (user decision — connections must emerge from data, not assumptions)
- 2026-03-23: Embed graph data in viewer.html (no server needed)
- 2026-03-23: Single-pass brief generation (no review step)
