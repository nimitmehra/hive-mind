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

## Latest Run — 2026-11-16 (morning), Day 262
- **Pipeline complete.** Ran 12:10–13:02 IST Monday (`date`-checked); committed 13:00, pushed 13:01:45 by the uploader (62 files); Telegram (text + document) and iMessage sent 13:02. Six parallel desks (launched ~12:13 IST; files 12:24–12:30) → CoS header R1–R14 → consolidated `intel.md` → `markets.md` → graph (backup `backups/2026-11-16/graph_v1`) → brief → independent fact-check → corrections (backup `graph_v2_preverif`) → local commit for the uploader → delivery. Window 15 Nov ~10:15 IST → 16 Nov ~12:30 IST (~26 h). Asian closes final; Brent/gold/US futures and India live at publish.
- **Lead.** No strike on Iran reported on night thirteen (third night running; OSINT only) → hold rule not reset; earliest new leg-(b) completion Thu 19 Nov. No US response to Sunday's Bahrain/Riyadh salvos and no "provocations" label; Bessent "We are squeezing them"; USS *Roosevelt* entered CENTCOM (three carriers; US officials). NYT (unnamed, relays): plans for renewed strikes incl. "energy infrastructure" — NOT new in substance (24-Oct story). Israel's security cabinet met Sunday evening (reported); no decision reported (Kan/Haaretz/Israel Hayom unreadable). Yemen: government Southern Armed Forces withdrew from Dhubab/Bab el-Mandeb (CONFIRMED); Reuters: Houthis "in control"; AFP: Kharaz camp 60 km from Aden. Bahrain to the UNSC; Saudi MOFA and GCC condemned Iran. UKMTO logged a tanker attack inside the Gulf (15 Nov; reported by Indian shipping authorities; unnamed). Iran claims "six tankers" mined (unnamed). Brent soft reopen $95.29, low $94.46, then +$1.20 from 11:17 IST (cause not found; gold fell in the same minutes); $96.40 at 12:35. Asian chip rout (TAIEX −6.0%, KOSPI −3.6%) on Nvidia/AI. WPI 12.29% (fuel & power 32.84%). Nifty above pre-war intraday (25,257 at 12:35).
- **Graph.** 29 nodes touched; 14 edge activations at unchanged weights + **new edge `brent-crude → indian-oil-marketing` (6.0)**; summaries rewritten: houthis, israel, fii-flows, indian-oil-marketing. All 134 open triggers reviewed (110 explicit, 24 defaults). **No status changes; no new watches.** Closest: `houthis` Aden watch (withdrawal confirmed, "heights" not named), `gold` 80:1 (~81 live; scored on settles — re-test the 16-Nov settles), `kospi` 5,000 (5,100.50).
- **Deployment.** Stay defensive. Cond 1 fails ($95.84 last settle; $96.4 live); cond 2 fails (5.15%); cond 3 buying met (ten sessions), inflation fails until 14 Dec. **OPEN FOR THE USER (proposed, not applied):** (i) confirmed Israeli strike on Iranian territory as a reset; (ii) confirmed Iranian fire on a Gulf state hosting US forces as a reset — "hitting" (not met) or "fired at" (met 13 and 15 Nov); (iii) the bar for November's CPI (5.54% strict or below 6.09%).
- **Fact-check.** 17 flags (1 critical, 4 high, 12 low), all applied, plus G1–G6. Critical: KOSPI/Samsung were pre-auction prints (5,082.39 → 5,100.50; Samsung −5.0% → −4.5%). Highs: NYT energy targets "new" (our 26-Oct brief had them); Dhubab retake "missed" (graph had it 13 Oct); "only oil moved" (gold −$27 same minutes; crisis share → unknown); Bahrain heading recycled Sunday's fire. **Correction published:** FII run was TEN regular sessions to 13 Nov, not nine (11-Nov brief dropped 30 Oct).
- **Process notes.**
  - **(1)** Asian closes pulled within ~30 min of the KRX close can be pre-auction on yfinance — re-pull Korea after ~16:00 KST (12:30 IST) before printing a "close".
  - **(2)** CoS "new/missed in our record" claims drew two HIGHs (NYT targets; Dhubab): grep `graph/nodes/*.json` notes AND October intel, not just recent signals, before writing "new" or "missed".
  - **(3)** "Only X moved" needs the 1-minute cross-asset check at the exact minutes, not the 30-minute bars.
  - **(4)** A follow-up on an event already in the last brief must lead with what is new (reaction), not the event.
  - **(5)** Length: Sections I–III ~3.8k words.
  - **(6)** Stale/pending: 62/63 nodes over the token budget (pre-existing).
- **Open at publish.** Late cabinet leak; CENTCOM on Sunday's Bahrain wave; the UKMTO tanker's name/crew; Houthi position on the Bab el-Mandeb heights; night fourteen; Warsh (22:30 IST); the 16-Nov settles (gold/silver ratio); Monday FII flows; CFTC (02:00 IST Tue); the 2-Nov blacklist names.
- **Dated tells.** 17 Nov Araghchi in Muscat, US retail sales, Knesset Speaker, Nvidia; 19 Nov Shenzhen and earliest leg-(b); ~20 Nov Kalın, India reserves; ~24 Nov Fesharaki; 29 Nov OPEC+; ~30 Nov Jan Brent expiry; 2–4 Dec RBI; 6 Dec Kan's "coming weeks"; 9 Dec FOMC; ~11 Dec US funding; 14 Dec India CPI; 17 Dec ECB; 31 Dec UNIFIL; 3 Jan Congress.

---

## Decisions Made
- 2026-03-23: Project lives in ``
- 2026-03-23: Do deep research backfill BEFORE building anything (user decision — connections must emerge from data, not assumptions)
- 2026-03-23: Embed graph data in viewer.html (no server needed)
- 2026-03-23: Single-pass brief generation (no review step)
