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

## Latest Run — 2026-11-10 (filed as "morning"; run Tuesday evening), Day 256
- **Pipeline complete.** Ran ~18:36–20:30 IST Tuesday. No brief this morning, so one full edition in the morning slot (same convention as 26 Oct, 31 Oct, 4, 6, 8, 9 Nov); no separate evening delta. Steps: six parallel desks (launched 18:39 IST; files 18:48–19:27, `date`-checked; MAC stayed on for the 19:00 IST US CPI) → CoS alerts (Brent settle-window bars; Trump's "effectively over" to verify) → consolidated `intel.md` → `markets.md` → graph → brief → independent fact-check → corrections → local commit for the uploader → delivery. India was shut (Diwali-Balipratipada).
- **Lead.** January Brent settled $92.57 on 9 Nov (−5.85%, lowest front-month settle since 31 Aug) and traded below $90 Tuesday for the first time since 31 Aug ($89.54 at 19:15 IST; low $89.15 post-CPI). Trump after Qatar's PM: Truth Social "quite unlikely… positive momentum" (02:59 IST, ID-decoded) and "Iran militarily is effectively over" (~04:02 IST). The sharpest settle-window minutes (00:53–01:12 IST) came before the first publication we found of any post-meeting statement; cause not established. Tehran denied the Doha talks on the record (Rezaei "imaginary talks… SURRENDER"; Araghchi "baseless"); Qatar: "positive responses from both sides", no terms. Saudi Energy Ministry confirmed an East-West pipeline hit (Madinah region, "limited fire", operations unaffected, attacker unnamed). Iranian state-aligned media (Fars/Hamshahri) named Didamar, "in the Omani section", as the IRGC nav-aid target; Oman, US, UKMTO silent. US October CPI hot (+0.4%/core +0.3%); Waller floated 50bp; December hike fully priced (26.8bp at 19:15 IST, our ZQZ26 math). Rubio: Israel aid to end "as soon as possible". Mildenhall KC-135s moved over a reported Iranian drone threat (WSJ).
- **Graph.** 43/63 nodes touched; edges 415, 11 activated, no weight changed. All 130 open triggers reviewed. **1 fired:** `saudi-arabia` "second confirmed hit on Aramco processing/export capacity (… East-West line)" — LOW IMPACT, on the leg's 8-Nov note. **2 new watches:** `saudi-arabia` capacity loss (lost throughput, or imagery of damage at Abqaiq/any East-West pumping station, by 31 Dec); `fed` 9-Dec 50bp. `iran` Tehran-meeting expiry final. `oman` NOT fired (closest yet). No `irgc → oman` edge until confirmation. 131 open.
- **Deployment.** Stay defensive; re-test 14 Nov. Condition 1 MET on the 9-Nov settle (physical leg one source). Condition 2 met (10Y 4.88% par; HY 3.42% vs 3.44% base). Condition 3: buying met; **inflation bar set 10 Nov before the print: strict reading — October CPI at or below September's 5.54%** (looser "below 6.0%" shown as the alternative). Both polls (BS 6.05%, Reuters 5.93%) fail the strict bar. Hold-rule reset: a US-owned strike, three straight nights of reported strikes, a declared campaign, or confirmed Iranian fire on Oman.
- **Fact-check.** 18 flags (0 critical, 7 high, 11 low), all applied, plus G1–G4 and Flag 17. Highs: absolute timing claim in the lead; "war did not de-escalate"; Fed headline "services, not oil" (components unknown — broke the CoS header's own rule); Signal headline "market priced the war as over" vs "half the premium gone"; Oman singled out over a pipeline hit no Gulf state condemned; hold-rule reset omitted a single owned strike; the 6.0% bar looser than "peaking". Every number matched.
- **Process notes.**
  - **(1)** CoS framing again drew every HIGH; desk facts and all Page 2 numbers held (fourth run in a row).
  - **(2)** **The CoS broke its own header rule** (components unknown → don't say energy did/didn't drive it) in a headline. Re-read the header's "wording rules" against every H3 before the fact-check.
  - **(3)** Absence claims ("every statement we could time") need "first publication we found"; relay times are not statement times. The Truth Social post ID decodes to UTC — use it.
  - **(4)** A deployment leg without a number ("consistent with a peak") had to be set under pressure; set numeric bars when a leg is added.
  - **(5)** Length: Sections I–III ~3.5k words after corrections (3.3k at draft, cut from 3.66k) — still over target.
  - **(6)** Carried over: 24 duplicate edge pairs; node budgets over 2k tokens.
- **Open at publish.**
  - The 10-Nov Brent settle (~01:00 IST Wed): Eurasia's "$90" test; the $85 leg (~$4.5 away).
  - Night eight; any US ownership; any Omani/US/UKMTO word on Didamar.
  - CoreWeave after the US close; the US cash session after CPI.
- **Dated tells.**
  - 11 Nov: India reopens (two settles + CPI + "effectively over" at once); CIBC's $100 date and the `brent-crude` $103.24 leg end at the 11-Nov settle (~01:00 IST Thu); Hegseth vote possible; Knesset Speaker vote this week.
  - 12 Nov: India CPI (strict bar 5.54%; `india` ≥6.0% trigger). 13 Nov: RBI reserves; CFTC; VLCC print. 14 Nov: hold-rule re-test; Ghaani's clock.
  - ~15–16 Nov AP's Syrian "within a week"; 17 Nov Nvidia; ~20 Nov Kalın's Doha test; ~24 Nov Fesharaki's "two weeks"; 29 Nov OPEC+; ~30 Nov January Brent expiry.
  - 2–4 Dec RBI; 9 Dec FOMC (`fed` 50bp watch); ~11 Dec US funding deadline; 17 Dec ECB; 3 Jan new Congress.

---

## Decisions Made
- 2026-03-23: Project lives in ``
- 2026-03-23: Do deep research backfill BEFORE building anything (user decision — connections must emerge from data, not assumptions)
- 2026-03-23: Embed graph data in viewer.html (no server needed)
- 2026-03-23: Single-pass brief generation (no review step)
