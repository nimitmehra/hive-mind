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

## Latest Run — 2026-11-11 (morning), Day 257
- **Pipeline complete.** Ran 11:22–~12:15 IST Wednesday (true morning edition). Steps: six parallel desks (launched 11:26–11:27 IST; files 11:38–11:45, `date`-checked; MAC's header end time was ahead of the clock and corrected from the mtime) → CoS alerts (the 21:45 IST Brent jump; ISR's Netanyahu timing lead) → consolidated `intel.md` → `markets.md` → graph (backup `backups/2026-11-11/graph_v1`) → brief → independent fact-check → corrections (backup `graph_v2_preverif`) → local commit for the uploader → delivery. India reopened (intraday only); US bond market shut (Veterans Day).
- **Lead.** At least two tankers hit Tue 10 Nov: ADNOC L&S confirms a vessel damaged in UAE territorial waters (WAM; probably MT *Fujairah Energy*, India's minister: four crew hurt, one Indian); UKMTO 201-26 off Lima; 202-26 suspicious activity; IRGC claims a third mined tanker. Night eight quiet (second running). Rubio on the record: "for the time being… no need for major combat operations"; Hegseth: "We control the Strait of Hormuz". January Brent settled $91.49 (Brew's $90 held); a 9-minute oil-only jump at 21:45 IST that Reuters ties to Rezaei's "no talks" (first publication found 21:52 IST — timing not established); ~$92.4 Wed. Rezaei: "pure lie"; Hormuz shut until the conditions are "fully implemented". Egypt's FM: forces in the kingdom "for defensive purposes", being reinforced. Houthis disowned the Medina pipeline hit. 2Y +17bp, 10Y 4.98% par (5.02% intraday). Nifty above its pre-war close intraday.
- **Graph.** 44/63 nodes touched; 9 edge activations/changes; **`brent-crude → fed` 10 → 9.0** (CPI composition; Fed talk on core). All 131 open triggers reviewed. **None fired** (the CoS fired `saudi-arabia` Egypt air-defence units; fact-check C1 reverted it to watching, closest). **2 new watches:** `uae` (attribution or a further hit in UAE waters after 10 Nov, by 30 Nov); `china` (Chinese or joint APEC readout naming Iran/Hormuz, by 20 Nov). 133 open.
- **Deployment.** Stay defensive; re-test 14 Nov. Condition 1 met ($91.49; physical leg one source; FRED spot sits above futures — sign conflicts with Morgan Stanley). Condition 2 met by 2bp (par 4.98%; HY 3.34% on 9 Nov); next test 12 Nov. Condition 3: buying met; strict inflation bar ≤5.54% fails on every forecast we found (5.9–6.11%); decided Thu 12 Nov. Hold rule: earliest pass 14 Nov (leg (b)'s earliest new run would complete the morning of 14 Nov).
- **Fact-check.** 18 flags (1 critical, 6 high, 11 low), all applied, plus G1–G9. Critical: the Egypt trigger fire (air-defence wording attaches to the reinforcement). Highs: Egypt headline; Logan's quote was FXStreet's summary; Bahri's "US military coordination" was a headline paraphrase; EIA $100 scored against futures although EIA forecasts spot; January fed funds cannot test a late-January hike; Rezaei's "at the present moment" dropped. Every number matched.
- **Process notes.**
  - **(1)** CoS framing/rulings again drew every CRITICAL and HIGH; desk facts and Page 2 numbers held (fifth run running).
  - **(2)** **A trigger fire on a fragment.** I fired a leg on an AFP Arabic fragment with no verb while noting the ambiguity myself. When the CoS ruling says "natural but not certain", hold — do not fire.
  - **(3)** **Quote marks on summaries:** FXStreet highlights and Bloomberg headlines are not the speaker's words. Check the desk's "paraphrase" caveats before quoting.
  - **(4)** **Forecast series:** score an analyst's forecast on the series it forecasts (EIA = spot), and check contract-averaging before using a fed-funds month as a test.
  - **(5)** Length: Sections I–III ~3.8k words after corrections (3.5k at draft after one trim). Still over target.
  - **(6)** Carried over: 24 duplicate edge pairs; node budgets over 2k tokens.
- **Open at publish.**
  - The Indian close (15:30 IST): is the Nifty's first close above its pre-war 25,178.65? Wednesday FII/DII.
  - Tadawul and Europe (opened after the brief); Qassem 21:30 IST; night nine; the 11-Nov Brent settle (~01:00 IST Thu) ends CIBC's $100 call and the >$103.24 leg.
  - Any UAE attribution; the 2-Nov blacklist ship names; Al-Mayadeen's airtime.
- **Dated tells.**
  - 12 Nov: India CPI (strict 5.54%; `india` ≥6.0%); US Treasuries reopen (condition 2); EIA weekly. 13 Nov: RBI reserves; CFTC; VLCC. 14 Nov: hold-rule re-test; Ghaani's clock.
  - ~15–16 Nov Syrian forces; ~16 Nov *Roosevelt*; 17 Nov Knesset Speaker vote, Nvidia; 18–19 Nov APEC Shenzhen (`china` watch); ~20 Nov Kalın; ~24 Nov Fesharaki; 29 Nov OPEC+; ~30 Nov January Brent expiry.
  - 2–4 Dec RBI; 9 Dec FOMC (`fed` 50bp); ~11 Dec US funding deadline; 17 Dec ECB; 31 Dec UNIFIL ends; 3 Jan new Congress.

---

## Decisions Made
- 2026-03-23: Project lives in ``
- 2026-03-23: Do deep research backfill BEFORE building anything (user decision — connections must emerge from data, not assumptions)
- 2026-03-23: Embed graph data in viewer.html (no server needed)
- 2026-03-23: Single-pass brief generation (no review step)
