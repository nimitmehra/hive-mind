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

## Latest Run — 2026-11-04 (morning), Day 250
- **Pipeline complete.** Six parallel desks (17:18–17:45 IST, `date`-checked; no guessed times this run) → consolidated `intel.md` → `markets.md` (CoS direct pulls) → graph → brief → independent fact-check → corrections → local commit for the uploader → delivery.
- **Timing.** Ran ~17:14–18:35 IST Wednesday. Filed as "morning" under restart practice (no 4-Nov morning baseline).
- **Lead.** Trump confirmed the 2-Nov Qeshm strike on air on 3 Nov ("we watched it get built… we hit it"). Democrats won both chambers (projections) with Iran a voting issue; the new Congress sits 3 Jan. Night one of the 4–30 Nov strike window passed quietly; the NYT reports a CENTCOM plan "as early as Wednesday".
- **Other items.**
  - **Tehran:** the Leader's 13-Aban text rejects hope in US politics or concessions; Rezaei calls the US response "not convincing"; Qatar runs a "real-time exchange" with a 36-hour feedback window.
  - **Oil:** January Brent $103.60, ~$102.3 Wed; February below $100 intraday. Dated premium ~$3.70 (REPORTED). Diesel crack ~$86.7.
  - **India:** FII +₹6,836.81 cr Tue (third straight session); Nifty 23,960.60; rupee touched 94.50, closed 94.58.
  - **Markets:** the vote moved them more than the war; gold +2.9% on the dollar; Fed December odds ~80–85%.
  - **Elsewhere:** VLCC *Grit* hit off Limah; Israel certified (Likud abstained); Trump says Israel aid ends by year-end; Houthis ~80 km from Aden (Reuters, 2 Nov); third Indian death from Houthi fire in Saudi Arabia.
- **Graph.**
  - 58/63 nodes touched; edges 414 (no new edge). Re-weighted: `semiconductors → nifty-50` 5.5 → 7.0, `kospi → nifty-50` 3.0 → 5.0, `houthis → india` 4.5 → 5.0.
  - 129 open triggers reviewed; 5 status changes, 5 new watches.
  - **Broken:** the pledge trigger (on-record).
  - **Fired:** the on-record acknowledgement watch (letter; no campaign declared); `nifty-50` capital substitution; `india` third death (letter; old attack).
  - **Expired:** the `iran` Vance-reply trigger.
  - **New watches:** Congress curbs before 3 Jan; a written Iranian answer to the Qatari draft; formal US action on Israel aid; Houthis reach Aden or the Bab el-Mandeb heights; a Texas data-centre moratorium.
- **Fact-check.** 17 flags (0 critical, 5 high, 12 low), all applied, plus 7 graph corrections (G1–G7). Highs:
  - "~$102 is mostly a bet on the war" (contradicted the desk's fair values; the premium is ~$8–17);
  - "both governments read it as a deadline" (unsourced);
  - "Rezaei never answered" (absence as fact; it repeated a 3-Nov correction);
  - the FT paraphrase "no immediate plans" put inside Trump's quote;
  - "the Leader closed the political door".
- **Process notes.**
  - **(1)** For the second brief running, the fact-checker's highs were CoS analytical overreach in "What it means", the Signal and deployment, not desk errors. Before writing intent or a share of a price, find a source for it (memory: feedback_signal_overreach).
  - **(2)** Sections I–III ran ~3.1k words after corrections, still over the 5-minute target (cut from 3.4k pre-verification).
  - **(3)** `trig_note`/`trig_set` substring matching hit two ambiguities (the resume trigger's leg (a) contains "acknowledges ON THE RECORD"); fixed by exact-prefix match. The completeness sweep must skip triggers added the same day.
  - **(4)** Carried over: 24 duplicate from→to pairs in `edges.json`; node budgets far over 2k tokens; helpers live in `staging/<run>/gu_*.py`.
- **Open at publish.**
  - Herzog's consultations (20:30 IST): the `israel` 61-seat trigger should FIRE next brief if they opened with no 61 path.
  - India's Wednesday FII figure (`fii-flows` 4 of 5?).
  - FRED HY OAS for 3–4 Nov (`us-10y-yield` can fire).
  - Night two of the strike window.
  - The Qatari 36-hour window (~06:30 IST 5 Nov).
- **Dated tells.**
  - ~5–6 Nov: Aramco December OSPs. 6 Nov: India reserves; US payrolls.
  - 9 Nov: Tehran-meeting text. 10 Nov: NSE shut. 10–11 Nov: Russia–Ukraine talks in Abu Dhabi. 11 Nov: Herzog's choice. 12 Nov: India CPI. 13 Nov: rupee 94.50.
  - 17 Nov: Nvidia. Mid–late Nov: Roosevelt. 29 Nov: OPEC+ 2027. ~30 Nov: January Brent expiry (roll trap for the <$100 test).
  - 4 Dec: RBI. 9 Dec: FOMC. ~11 Dec: US funding deadline. 17 Dec: ECB. 3 Jan: new Congress.

---

## Decisions Made
- 2026-03-23: Project lives in ``
- 2026-03-23: Do deep research backfill BEFORE building anything (user decision — connections must emerge from data, not assumptions)
- 2026-03-23: Embed graph data in viewer.html (no server needed)
- 2026-03-23: Single-pass brief generation (no review step)
