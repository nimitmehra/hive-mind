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

## Latest Run — 2026-11-12 (morning), Day 258
- **Pipeline complete.** Ran 10:42–11:28 IST Thursday (true morning edition). Six parallel desks (launched ~10:47 IST; files 10:58–11:03, `date`-checked; DIP's header end time was ahead of the clock and is corrected from the mtime) → CoS header and rulings → consolidated `intel.md` → `markets.md` → graph (backup `backups/2026-11-12/graph_v1`) → brief → independent fact-check → corrections (backup `graph_v2_preverif`) → local commit for the uploader → delivery. India open (intraday); US Treasuries reopened in Asia after Veterans Day.
- **Lead.** Rezaei: "not a single particle" of enriched material will leave Iran (first publication found: Tasnim 14:44 IST Wed — the same minute Brent's first oil-only jump began; Reuters ties the day's rise to it); Ghalibaf: Hormuz will "never return" to its pre-war status, UNCLOS "does not apply" (claims an Oman understanding; Oman silent). Both are restated positions (20 Oct; June). January Brent settled $92.76 (+1.39%); second jump (20:45 IST) unexplained; ~$91.9 Thu. WSJ: Vance weighing direct talks with Rezaei, "no date set"; Iran rejects. Night nine quiet (third). Kan: IDF told to raise readiness for a possible strike in Iran; Israel's security cabinet meets Sun 15 Nov (Ynet: "may now approve action"). NCC Fajr (Bahri-managed) in a "possible attack" (India's minister). Seven Houthi projectiles at Saudi Arabia, Mecca-region debris ~36 km from the Grand Mosque. Nifty's first war-era close above pre-war (25,255.05, our check); FII seventh session; India CPI ~16:00 IST today. Nvidia −8.6% after hours (WSJ board report).
- **Graph.** 46 nodes touched; 17 edge activations, no re-weights. All 133 open triggers reviewed. **None fired.** `brent-crude` >$103.24 watch EXPIRED. Held: `houthis` holy-city (its own 26-Oct reversion and 31-Oct province rule — KIN's lean overruled); `strait-of-hormuz` blacklist (NCC Fajr "possible attack", list names missing). **2 new watches:** `israel` (cabinet approves action against Iran, or a confirmed Israeli strike, by 30 Nov); `qatar` (a second QatarEnergy buyer cancels, or force majeure past 31 Dec, by 31 Jan 2027 — after Orlen). 134 open.
- **Deployment.** Stay defensive; re-test 14 Nov. Cond 1 met ($92.76). Cond 2 met on the last prints (par 4.98% 10 Nov; HY 3.34%); ~4.99% in Asia; next close ~02:30 IST Fri. Cond 3: buying met (7); strict inflation bar ≤5.54% decided today ~16:00 IST, every forecast fails it. Hold rule earliest pass 14 Nov; leg (b)'s earliest run ends 15 Nov. **OPEN FOR THE USER: proposed (not applied) — add "a confirmed Israeli strike on Iranian territory" as a hold-rule reset** (a strike reported as Israel's alone meets none of the current resets).
- **Fact-check.** 20 flags (0 critical, 5 high, 15 low), all applied, plus G1–G3. Highs: the Signal's reset list omitted RESUME legs (c)/(d) (CoS); "not new in substance" missing and "hardened" (CoS); Eisenkot's letter paraphrased as "properly approved"; NCC Fajr called "hit"; Didamar without the Omani denial. Every number matched (copper 10-Nov the only slip).
- **Process notes.**
  - **(1)** CoS framing again drew most HIGHs (sixth run running); desk facts and Page 2 held.
  - **(2)** **Rule restatements:** when restating the hold rule, quote the RESUME trigger's four legs, not the shortened list from earlier briefs (the 10–11 Nov lists had dropped (c)/(d)).
  - **(3)** **Restated vs new:** carry the desk's "not new in substance" into the brief whenever a headline quote repeats a standing position.
  - **(4)** Desks were fast (~11–16 min); the DIP desk timed jump 1 to the minute from page stamps — keep asking desks for first-publication stamps vs 1-minute bars.
  - **(5)** Length: Sections I–III ~4.1k words after corrections (3.8k at draft). Over target again.
  - **(6)** Carried over: 24 duplicate edge pairs; node budgets over 2k tokens.
- **Open at publish.** India CPI (~16:00 IST) and the Indian close; Thursday's first post-holiday Treasury close (~02:30 IST Fri); EIA weekly 22:30 IST; IEA OMR 13 Nov; night ten; Sunday's Israeli cabinet; NCC Fajr damage/UKMTO notice; the 2-Nov list ship names; Al Mayadeen's airtime (jump 2).
- **Dated tells.** 13 Nov IEA, RBI reserves, PPI, VLCC; 14 Nov hold-rule re-test, Ghaani's clock (Orlen's first post-FM Qatari cargo due Świnoujście, per P&GJ); 15 Nov Israeli security cabinet; ~15–16 Nov Syrian forces; ~16 Nov *Roosevelt*; 17 Nov Knesset Speaker, Nvidia, US retail sales; 18–19 Nov APEC; ~20 Nov Kalın; ~24 Nov Fesharaki; 29 Nov OPEC+; ~30 Nov Jan Brent expiry; 2–4 Dec RBI; 9 Dec FOMC; ~11 Dec US funding; 17 Dec ECB; 31 Dec UNIFIL; 3 Jan Congress.

---

## Decisions Made
- 2026-03-23: Project lives in ``
- 2026-03-23: Do deep research backfill BEFORE building anything (user decision — connections must emerge from data, not assumptions)
- 2026-03-23: Embed graph data in viewer.html (no server needed)
- 2026-03-23: Single-pass brief generation (no review step)
