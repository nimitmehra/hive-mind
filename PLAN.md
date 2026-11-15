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

## Latest Run — 2026-11-15 (morning), Day 261
- **Pipeline complete.** Ran 09:57–10:49 IST Sunday; committed 10:46, pushed 10:48:18 by the uploader (62 files); Telegram (text + document) and iMessage sent 10:49 (true morning edition; no 14-Nov brief, so a ~47-hour window). Six parallel desks (launched ~10:01 IST; files 10:11–10:17, `date`-checked) → CoS header R1–R14 → consolidated `intel.md` → `markets.md` → graph (backup `backups/2026-11-15/graph_v1`) → brief → independent fact-check → corrections (backup `graph_v2_preverif`) → local commit for the uploader → delivery. All prices are Friday 13 Nov closes (weekend).
- **Lead.** The hold-rule leg-(b) test FAILED to reset: no strike on Iran reported on nights eleven (IRNA: Jask "explosion sound… no impact"; Hormozgan governorate: no impact) or twelve (one OSINT feed only). CENTCOM confirmed two IRGC drones at Bahrain on 13 Nov, "no injuries or damage" (rebutting the radar claim); Bahrain TV: one Iranian drone intercepted 15 Nov; IRGC claims six drones hit a radar at Al-Rifa'a (unconfirmed). Coalition: two Houthi ballistic missiles at Riyadh intercepted 15 Nov. Washington repeated restraint (Rubio "no need for military action"; Reuters: Trump "may hold off" absent new provocations). Brent $95.84 flat (IEA: first Q4 surplus since the war); 10Y 5.15% (highest since 19 Oct, though Fed bets eased); Nifty 25,144.30, back below pre-war; FII ninth session; Oct trade deficit $39.88bn. IAEA "not able to conclude… no diversion". Israel's cabinet meets Sunday evening (after the brief).
- **Graph.** 36 nodes touched; 15 edge activations at unchanged weights; 8 stale summaries rewritten (bahrain, fii-flows, us-10y-yield, nifty-50, brent-crude, israel, united-states, nuclear-program). All 134 open triggers reviewed (113 explicit, 21 per-node defaults). **No status changes; no new watches.** `united-states` RESUME stays fired, no revert. Closer: `bahrain` (fire AT confirmed, hit not), `gold` 80:1 (79.1), `china` APEC (19 Nov). Pending tonight: `israel` cabinet watch.
- **Deployment.** Stay defensive. Cond 1 fails ($95.84, by $0.84); cond 2 fails (5.15%; credit fine 3.20%); cond 3 buying met (9 sessions), inflation fails until 14 Dec. Hold rule: no reset; earliest new leg-(b) completion Wed 18 Nov. **OPEN FOR THE USER (proposed, not applied):** (i) confirmed Israeli strike on Iranian territory as a reset; (ii) confirmed Iranian fire on a Gulf state hosting US forces as a reset — and whether the bar is "hitting" (would not fire today) or "fired at" (would have fired on CENTCOM's 13-Nov statement); (iii) the bar for November's CPI (5.54% strict or below 6.09%).
- **Fact-check.** 19 flags (1 critical, 9 high, 9 low), all applied, plus G1–G5. Critical: the evening Brent slide was ~$1.00 from 21:05 IST, not $1.60 (that was from the $97.12 high). Highs: lead headline counted Friday's (pre-window) Bahrain drones as an "instead" event; "Washington's line moved" (it restated Trump's own Saudi-request hold); the Signal said Reuters "named what would end the hold" (it gave a condition for holding) and contradicted itself ("whatever Washington does"); "your proposed reset (ii)" (we proposed it); "yields mostly the Fed" (futures eased; curve steepened); "clearest direct cost of the war" (deficit below Oct 2025's $42.58bn); FII "three days" (two); OMC "third day" (BPCL fourth, HPCL/IOC second). Every settle/close matched.
- **Process notes.**
  - **(1)** CoS framing drew the HIGHs again (eighth run running); desk facts and numbers held except two desk-level streak counts (FII, OMC) — re-derive any "N days running" from the prior briefs' tables.
  - **(2)** Sequence words ("instead", "then", "after") need both timestamps checked against the WINDOW start, not just against each other: Friday's Bahrain drones predated the window.
  - **(3)** "Moved/shifted" for a government line: check the previous brief for the same stance before calling it a shift.
  - **(4)** Self-caught before the fact-check: three titles from memory (Kalın, Ghaani, Leiter), a "will" inside quote marks, "not a first" for Bahrain (July strikes in the graph) and Riyadh (5 Nov claims).
  - **(5)** The "dusk in Tehran ~18:25 IST" line carried from 13 Nov was wrong (~19:00 IST): use IST − 2:00.
  - **(6)** Length: Sections I–III ~3.9k words.
  - **(7)** Stale for next run: the `indian-oil-marketing` summary (Day 241); 62/63 nodes over the token budget (pre-existing).
- **Open at publish.** Israel's security cabinet (Sunday evening); CENTCOM on Sunday's Bahrain wave; Tadawul (12:30 IST); night thirteen; a Houthi claim for the Riyadh missiles; Friday's Trump posts (unchecked); the 2-Nov list ship names.
- **Dated tells.** 16 Nov Brent reopen, India WPI 12:00 IST, CFTC (delayed); ~16 Nov *Roosevelt*; 17 Nov Knesset Speaker, Nvidia, US retail sales; 18 Nov earliest leg-(b); 19 Nov Trump–Xi–Putin Shenzhen; ~20 Nov Kalın; ~24 Nov Fesharaki; 29 Nov OPEC+; ~30 Nov Jan Brent expiry; 2–4 Dec RBI; 6 Dec Kan's "coming weeks"; 9 Dec FOMC; ~11 Dec US funding; 14 Dec India CPI; 17 Dec ECB; 31 Dec UNIFIL; 3 Jan Congress.

---

## Decisions Made
- 2026-03-23: Project lives in ``
- 2026-03-23: Do deep research backfill BEFORE building anything (user decision — connections must emerge from data, not assumptions)
- 2026-03-23: Embed graph data in viewer.html (no server needed)
- 2026-03-23: Single-pass brief generation (no review step)
