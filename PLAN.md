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

## Latest Run — 2026-11-05 (morning), Day 251
- **Pipeline complete.** Ran ~10:55–12:00 IST Thursday: a genuine morning edition, before 13:00. Six parallel desks (10:57–11:24 IST, `date`-checked) → consolidated `intel.md` → `markets.md` (CoS direct pulls) → graph → brief → independent fact-check → corrections → local commit for the uploader → delivery.
- **Mid-sweep alert.** At ~11:00 the CoS's own contract pull showed January Brent had settled at $94.62 (−8.7%). All six desks were alerted, since their brief still said ~$102, and each was asked to find the cause in its own area. This worked: every desk independently ruled out a Gulf, Hormuz or diplomatic cause.
- **Lead.** Oil broke $100 on Washington's politics. Vance's X post ("The reason we lost is the war", 21:08 IST, decoded from the post ID) preceded a $101.2 → $93.40 fall in two hours. Nothing physical changed. Markets traded the war as ending (Dow +3%, VIX −20%, Lockheed −6.9%). The paper trail did not move: the Qatari 36-hour window closed with no answer, Axios reports the military "finishing preparations", and night two was quiet.
- **Other items.**
  - **India:** FII +₹7,284.03 cr (fourth session); Nifty ~24,370 Thursday. PTI's final rupee close was 94.46, a correction to the 4-Nov brief, then re-capped at 94.50. 10Y ~7.19% → ~7.06%.
  - **Israel:** consultations opened with no 61 path (stated positions: Eisenkot 56, Netanyahu 46). Lebanon had its first death from Israeli fire since September, a correction to 4 Nov.
  - **Saudi front:** Houthi claim on Riyadh's airport met with Saudi silence; a Saudi–Syria defence agreement.
  - **Chips:** the AI "permission" sell-off (SOX −3.1%, KOSPI −5%), which is non-war.
- **Graph.**
  - 59/63 nodes touched; edges 414 → 415 (new `vance → brent-crude`, 5.0 provisional).
  - All 129 open triggers reviewed (completeness check 0 missing).
  - **Fired:** `brent-crude` sub-$100 unwind (cause logged: US political signal); `inr-usd` PTI <94.50 (on its letter; limits noted); `israel` 61-seat.
  - **New watches (4):** Brent back above $100 or below $85; two PTI closes below 94.50 by 20 Nov or one above 95.50; a Vance or Witkoff on-record meeting with an Iranian official; Syrian units in Saudi Arabia, or Syria joining the Mecca pact.
  - `us-10y-yield` is a NEAR-FIRE, awaiting FRED's 4-Nov HY OAS (fires at ≤3.44%).
- **Fact-check.** 22 flags (0 critical, 7 high, 15 low), all applied, plus graph corrections G1–G9. The highs:
  - An unsourced "RBI reserve-refilling" attribution;
  - "No Iranian fire" (the desk had said not to write it);
  - Stated positions written as recommendations made;
  - The premium against one bank's fair value only (a repeat of 4-Nov H1);
  - "Nifty +4% in five sessions" (it was 6%);
  - The Wednesday bond rally put under oil relief, though it came before the fall;
  - "Weakened, not disproved" reinterpreting a falsification trigger after it fired.
- **Process notes.**
  - **(1)** CoS overreach again drew most of the highs, this time in the trimming pass: when cutting for length, I dropped Goldman's number and kept a causal parenthesis. Re-check fair values, timing and causation after every edit pass, not only the first draft.
  - **(2)** Timing traps: India's Wednesday close and bond rally both came before the 21:08 IST oil break. Before attributing any move to an event, check which session it closed in.
  - **(3)** Sections I–III ran ~2.9k words after corrections, still over the 5-minute target (3.1k → 2.66k at draft, then +250 from corrections).
  - **(4)** The improved `_find` (open triggers only; exact → prefix → substring) gave zero ambiguities.
  - **(5)** Carried over: 24 duplicate edge pairs; node budgets over 2k tokens.
- **Open at publish.**
  - India's Thursday FII figure (~18:00 IST; a fifth session fires `fii-flows`).
  - FRED's 4-Nov HY OAS (`us-10y-yield`).
  - Aramco December OSPs (`saudi-arabia` OSP trigger).
  - Likud at Herzog (~00:00 IST).
  - Night three of the strike window.
- **Dated tells.**
  - 6 Nov: India reserves; US payrolls.
  - 9 Nov: Tehran-meeting text; a Hegseth impeachment vote that week. 10 Nov: NSE shut. 10–11 Nov: Russia–Ukraine talks in Abu Dhabi. 11 Nov: Herzog's choice; the window one week old (the hold-rule date). 12 Nov: India CPI.
  - 17 Nov: Nvidia. 20 Nov: the rupee two-close test. 29 Nov: OPEC+. ~30 Nov: January Brent expiry.
  - 4 Dec: RBI. 9 Dec: FOMC. ~11 Dec: US funding deadline. 17 Dec: ECB. 3 Jan: new Congress.

---

## Decisions Made
- 2026-03-23: Project lives in ``
- 2026-03-23: Do deep research backfill BEFORE building anything (user decision — connections must emerge from data, not assumptions)
- 2026-03-23: Embed graph data in viewer.html (no server needed)
- 2026-03-23: Single-pass brief generation (no review step)
