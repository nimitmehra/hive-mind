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

## Latest Run — 2026-11-13 (morning), Day 259
- **Pipeline complete.** Ran 10:59–11:42 IST Friday (true morning edition); committed 11:41, pushed 11:41:51 by the uploader (62 files); Telegram (text + document) and iMessage sent 11:42. Six parallel desks (launched ~11:04 IST; files 11:13–11:16, `date`-checked) → CoS header R1–R14 → consolidated `intel.md` → `markets.md` → graph (backup `backups/2026-11-13/graph_v1`; one partial run crashed on an import and was restored from the backup before the clean run) → brief → independent fact-check → corrections (backup `graph_v2_preverif`) → local commit for the uploader → delivery. India open (intraday).
- **Lead.** Trump on Truth Social, 18:37:34 IST Thu (decoded ID): "We don't need a deal with Iran… we've got their Strait!" — Brent +$2 in six minutes on 611 lots; settle **$95.82** (+3.3%). US 10Y **5.10%** (+12bp; ~two-thirds Fed repricing in US hours). India October CPI **6.09%** (food 8.94%). **All three deployment conditions fail.** Night ten not quiet: IRNA — "the enemy" struck Sirik (unattributed); IRGC claims a US radar on Bahrain destroyed (unconfirmed). UKMTO confirms *NCC Fajr* attacked; we had missed *Dominica Prosperity* (19 Indians, 11 Nov). Houthi claims on Saudi oil sites (unconfirmed). Israel: Ch13 — IDF sees "no immediate urgency"; cabinet Sun 15 Nov. Gold 2026 low close ($3,885.3); Huang resigned (8-K).
- **Graph.** 32 nodes touched; 15 edge activations, no re-weights. All 134 open triggers reviewed (90 explicit, 44 per-node defaults). **Fired: `india` CPI ≥6.0%.** New watch: `bahrain` (confirmed Iranian fire hitting a US/Bahraini military site in Bahrain, by 30 Nov). Held: `strait-of-hormuz` blacklist (NCC Fajr confirmed attacked, list membership unshown); `uae` (14 nm off RAK); `united-states` RESUME no revert (night ten = night one of a possible leg-(b) run → morning of 15 Nov). 134 open.
- **Deployment.** Stay defensive; the 14-Nov re-test cannot pass. Cond 1 fails ($95.82); cond 2 fails (5.10%; credit fine 3.30%); cond 3 buying met (8 sessions), inflation fails both readings and cannot be re-tested before **14 Dec** (November CPI). **OPEN FOR THE USER (proposed, not applied):** (i) a confirmed Israeli strike on Iranian territory as a hold-rule reset (from 12 Nov); (ii) confirmed Iranian fire hitting a Gulf state hosting US forces as a reset; (iii) which bar applies to November's CPI (5.54% strict, or below October's 6.09%).
- **Fact-check.** 16 flags (0 critical, 4 high, 12 low), all applied, plus G1–G4. Highs: the Signal said "only one condition failed because of the war" (now "mainly"; CNBC lists oil among the Fed drivers); Salem's "no hesitation" caption quoted as Trump's words; three different Indian-tanker counts after the correction; Sinokor's ≥29-ship blacklist bloc (already in our graph) left out. Every number matched.
- **Process notes.**
  - **(1)** CoS framing again drew the HIGHs (seventh run running); desk facts and Page 2 held.
  - **(2)** When a correction changes a count ("three tankers, not two"), grep the whole brief for every restatement of that count.
  - **(3)** Before using the desk trigger list script after the update, write to a new file — `gen_open_triggers.py` overwrote the desks' input (restored from the backup).
  - **(4)** Graph helpers: `_EIDX` is private; import `gu_helpers` to reach it.
  - **(5)** Length: Sections I–III ~3.8k words after corrections (3.6k at draft).
- **Open at publish.** Friday prayers (12:30 IST); IEA OMR (14:30); RBI reserves (~17:00); US PPI (19:00); night eleven; Bahrain/US response to the IRGC claim; the 2-Nov list ship names; Sunday's Israeli cabinet.
- **Dated tells.** 14 Nov Ghaani's clock; 15 Nov morning leg-(b) test, Israeli security cabinet; ~15–16 Nov Syrian forces; ~16 Nov *Roosevelt*; 17 Nov Knesset Speaker, Nvidia, US retail sales; 18–19 Nov APEC; ~20 Nov Kalın; ~24 Nov Fesharaki; 29 Nov OPEC+; ~30 Nov Jan Brent expiry; 2–4 Dec RBI; 9 Dec FOMC; ~11 Dec US funding; 14 Dec India CPI; 17 Dec ECB; 31 Dec UNIFIL; 3 Jan Congress.

---

## Decisions Made
- 2026-03-23: Project lives in ``
- 2026-03-23: Do deep research backfill BEFORE building anything (user decision — connections must emerge from data, not assumptions)
- 2026-03-23: Embed graph data in viewer.html (no server needed)
- 2026-03-23: Single-pass brief generation (no review step)
