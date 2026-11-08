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

## Latest Run — 2026-11-08 (filed as "morning"; run Sunday afternoon), Day 254
- **Pipeline complete.** Ran ~14:50–15:55 IST Sunday. No brief since 6 Nov, so one full edition in the morning slot (same convention as 26 Oct, 31 Oct, 4 Nov, 6 Nov); no evening delta (no Sunday market session after the brief). Steps: six parallel desks (14:53–15:43 IST, `date`-checked) → CoS cross-desk alert at 15:05 (ISR's ToI/Naharnet leads sent to KIN/DIP/SAU) → consolidated `intel.md` → `markets.md` (CoS direct pulls) → graph → brief → independent fact-check → corrections → local commit for the uploader → delivery.
- **Lead.** The first owned US strike inside the 4–30 Nov window: two projectiles hit the Suza area of Qeshm (first reported ~01:08 Tehran Sat 7 Nov); Trump, Friday evening ET: "We do minor strikes… They built a little bit of an anti-aircraft device, and we knocked it out". Night five: unattributed blasts in four Hormozgan counties. CENTCOM disabled the *Huda*; Task Force Iron Gate (land/Caspian). A Houthi barrage damaged Aramco's KAFD tower in Riyadh (Energy Ministry: "limited damage"). Herzog picked Eisenkot (Sat night). Payrolls +165k; Fed Dec odds ~65% → ~76%. Brent Jan settled $98.32 Friday — every war event came after the settle. India: FII sixth buying day (+₹13,750 cr), futures hedge 1.00 lakh; IANS: RBI buying near 93.88; Muhurat Nifty 24,986.40 (−0.18%).
- **Graph.** 55/63 nodes touched (43 with new signals); edges 415 (none new), 5 activated, `houthis → saudi-arabia` 9.0 → 9.5. All 130 open triggers reviewed (0 missing).
  - **Fired:** `united-states` "resume 4–30 Nov" on leg (a) only (CoS ruling against KIN/DIP "log, not fire"; fact-checker AGREED, moderate) — **REVERT if the White House says Trump meant the 2-Nov strike** (referent risk); `israel` Herzog–Eisenkot.
  - **New watches (2):** owned strikes 3 nights running or 2+ sites in a night by 30 Nov; Brent Monday open >$100 or a 9–11 Nov settle >$103.24.
  - **Hold rule amended:** leg 1 ("window a week old with no qualifying strike") failed 7 Nov; amended to seven straight days with no further qualifying strike — earliest re-test 14 Nov. Do not stage on 11 Nov.
- **Fact-check.** 14 flags (0 critical, 8 high, 6 low), all applied, plus G1–G5. Highs: drone-claim timing (~6h, not ~3h — wrong timestamp pair in KIN/CoS); a paraphrase in quotation marks and two trigger notes merged; the missing referent caveat; header said no Indian price had traded (Muhurat had); Signal superlative beyond the data (FII futures data only 4–6 Nov) and RBI reserve effect stated as fact; McNally/ING row inconsistent with the strike ruling; hold-rule amendment unlabelled; *Huda* = UKMTO 198-26 was an inference.
- **Process notes.**
  - **(1)** CoS framing again drew every HIGH (lead's "why it counts", Signal, scorecard, hold rule). Desk facts held; all ~110 Page 2 numbers matched.
  - **(2)** Timestamps: when pairing two events, name both clocks (Tehran vs UTC) — the "~2.7h" came from 18:56 Tehran read against 18:58 UTC.
  - **(3)** A scorecard must apply the day's trigger ruling consistently to every row.
  - **(4)** Length: Sections I–III ~3.3k words after corrections (2.9k at draft) — still over the 5-minute target.
  - **(5)** The IND desk ran to 15:43 waiting for the Muhurat close; the other five finished by ~15:09.
  - **(6)** Carried over: 24 duplicate edge pairs; node budgets over 2k tokens (`united-states` ~51k).
- **Open at publish.**
  - Monday's Brent open (~04:30 IST) — the first price after the strike and the Riyadh hit.
  - Night six (new moon 9 Nov); any US ownership of night five.
  - A White House clarification of Trump's referent (would revert the fire).
  - Muhurat FII figure; PTI's final Friday rupee close; FRED 6-Nov HY OAS.
  - Eisenkot's mandate ceremony (20:30 IST tonight).
- **Dated tells.**
  - 9 Nov: Brent open; India trades; Miller starts; Iran MFA briefing; Korea margin waiver; Hegseth vote week. 10 Nov: NSE shut; US CPI; Knesset sworn in; CoreWeave. 10–11 Nov: Abu Dhabi talks. 11 Nov: CIBC's $100 date.
  - 12 Nov: India CPI. 13 Nov: RBI reserves; CFTC. 14 Nov: amended hold-rule re-test; Ghaani's Bab el-Mandeb clock. 17 Nov: Nvidia. Late next week: *Roosevelt* in the Arabian Sea. 29 Nov: OPEC+. ~30 Nov: January Brent expiry.
  - 4 Dec RBI; 9 Dec FOMC; ~11 Dec US funding deadline; 17 Dec ECB; 3 Jan new Congress.

---

## Decisions Made
- 2026-03-23: Project lives in ``
- 2026-03-23: Do deep research backfill BEFORE building anything (user decision — connections must emerge from data, not assumptions)
- 2026-03-23: Embed graph data in viewer.html (no server needed)
- 2026-03-23: Single-pass brief generation (no review step)
