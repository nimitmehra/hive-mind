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

## Latest Run — 2026-11-06 (filed as "morning"; run Friday afternoon), Day 252
- **Pipeline complete.** Ran ~16:33–17:40 IST Friday. No morning brief existed, so the run went out as one full edition in the morning slot (same convention as 26 Oct, 31 Oct and 4 Nov). Steps: six parallel desks (16:36–~17:09 IST, `date`-checked) → consolidated `intel.md` → `markets.md` (CoS direct pulls) → graph → brief → independent fact-check → corrections → local commit for the uploader → delivery.
- **Mid-sweep alert.** The CoS pull at 16:37 showed a US crash (S&P −4.36%, SOX −12.25%, VIX 28.18), Brent +3.9% and India +2.4%/+2.0%. All six desks were alerted. They agreed the crash was AI/data-centre driven (non-war); Reuters attributed the Brent rebound to ship attacks and Iran's terms; India ran on oil Thursday and on the "reverse AI" rotation Friday.
- **Lead.** Wall Street's worst day since April 2025 came from AI, not Iran; oil went the other way, mainly on the ship war. India closed near its pre-war level (Nifty 25,030.35, highest since 27 Feb) on the largest FII day in nearly six years. Trump: "Now we will make a decision… You'll know soon enough." Unnamed officials noted the 9-Nov new moon to Fox. Night three was quiet.
- **Other items.**
  - **Iran:** a nuclear proposal via Qatar, reported by one anonymous Iranian and unacknowledged; Rezaei's seven conditions stated on the record.
  - **Ship war:** UKMTO 196-26 (*Velos Sapphire*, one seafarer killed or missing), a correction to 5 Nov.
  - **Israel:** Eisenkot 67 / Netanyahu 46; Herzog decides 8 Nov.
  - **Saudi Arabia:** Aramco cut its Asian OSP $2 to ~−$7; WSJ reports an approach to the Houthis (demands denied).
  - **Europe:** the BoE hiked to 4%.
  - **India:** reserves $717.06bn (−$2.69bn).
- **Graph.**
  - 62/63 nodes touched; edges 415 (none new). `kospi → nifty-50` 5 → 6; `semiconductors → vix` 5 → 6.
  - All 130 open triggers reviewed (completeness check: 0 missing).
  - **Fired:** `us-10y-yield` (4-Nov HY OAS 3.32%); `fii-flows` (fifth session); `inr-usd` two PTI closes <94.50 (cause: mainly flows); `saudi-arabia` OSP cut.
  - **Amended:** `vix` ">25 = kinetic marker" now needs a coincident kinetic event, after a non-war false positive.
  - **New watches (4):** HY OAS >3.75% with 10Y <5%; FII net sellers ×3; PTI weaker than 95.00; Saudi–Houthi talks on the record.
- **Fact-check.** 23 flags (0 critical, 6 high, 17 low), all applied, plus G1–G10. The highs:
  - "Record" FII (it was the largest in nearly six years);
  - "Flows, not oil" for the rupee (wrong comparator, a clipped Parmar quote);
  - Signal overreach (India "priced the war out"; an unmeasured AI share; "oil rose too" at rupee closes);
  - "Officials point at 9 Nov" (unnamed officials only noted a new moon);
  - Akraminia's conditional dropped;
  - Saxo's test pinned on Yardeni.
- **Process notes.**
  - **(1)** CoS overreach again drew all six highs. Every one sat in the CoS's own causal or Signal lines, not in desk facts. Before drafting, line up each causal claim against the session clock: the rupee closes at 15:30 IST, Brent settles ~01:00 IST.
  - **(2)** Superlatives: check "record" against the source's own wording ("nearly six years").
  - **(3)** Length: Sections I–III ran ~3.2k words after corrections (2.83k at draft), still over the 5-minute target.
  - **(4)** The desk sweep took ~33 min. The IND desk waited for the 17:00 RBI print; a 17:20 cutoff kept it bounded.
  - **(5)** Carried over: 24 duplicate edge pairs; node budgets over 2k tokens.
- **Open at publish.**
  - Friday's FII figure.
  - PTI's final Friday rupee close (~20:45 IST).
  - FRED's 5-Nov HY OAS.
  - US payrolls (19:00 IST).
  - Tonight's Brent settle (the above-$100 watch).
  - Night four.
- **Dated tells.**
  - 8 Nov: Herzog.
  - 9 Nov: new moon; Tehran-meeting text; the Hegseth vote that week. 7–11 Nov: Iraqi airspace report (unconfirmed). 10 Nov: NSE shut. 10–11 Nov: Abu Dhabi talks. 11 Nov: the hold-rule date; CIBC's $100 test.
  - 12 Nov: India CPI. 13 Nov: RBI reserves. 17 Nov: Nvidia. Mid-Nov: *Roosevelt*. 29 Nov: OPEC+. ~30 Nov: January Brent expiry.
  - 4 Dec: RBI. 9 Dec: FOMC. ~11 Dec: US funding deadline. 17 Dec: ECB. 3 Jan: new Congress.

---

## Decisions Made
- 2026-03-23: Project lives in ``
- 2026-03-23: Do deep research backfill BEFORE building anything (user decision — connections must emerge from data, not assumptions)
- 2026-03-23: Embed graph data in viewer.html (no server needed)
- 2026-03-23: Single-pass brief generation (no review step)
