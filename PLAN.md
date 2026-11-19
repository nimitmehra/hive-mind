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

## Latest Run — 2026-11-19 (morning), Day 265
- **Pipeline complete.** Ran 12:54–~14:20 IST Thursday (`date`-checked). Window 16 Nov ~12:30 IST → 19 Nov ~13:15 IST (~72 h): **no brief was published 17–18 Nov** (the 17-Nov run was abandoned after its India desk; its staging dir is partial). Six parallel desks (12:58–13:16 IST) → CoS header R1–R15 → `intel.md` (46k words) → `markets.md` (Market Analyst agent) → graph (Graph Engineer agent; backup `backups/2026-11-19/graph_v1`) → brief (Editor agent) → independent fact-check → corrections (backup `graph_v2_preverif`, brief `2026-11-19-morning_v1.md`) → local commit for the uploader → delivery.
- **Lead.** US jets struck an IRGC missile-launch site on Qeshm Tue 17 Nov (strike CONFIRMED: Hormozgan deputy governor + unnamed US officials, "self-defense"; ownership anonymous). Iran then fired at Bahrain (17, 18 Nov) and Kuwait (Ali Al Salem; first since September) — all intercepted on the record. Nights fourteen and sixteen quiet → **hold rule: no reset**; earliest new leg (b) **Sun 22 Nov**. NYT (relays): Trump weighing "another round of extensive military strikes"; Netanyahu pressing a 4–7-day joint campaign; Channel 13: joint plans "approved… waiting for Trump's decision". *George Washington* left (two carriers). Ship war turned lethal off Musandam (≥4 projectile hits; *Tara Gas* — one Indian missing; ADNOC L&S ship 11 injured, 1 missing; attacker unnamed; MEA "must end"). Brent settles $92.44 / $93.14 / $91.95 (below $95; EFP ~0). AI/chip + metals rout fired `kospi` (4,968.48 close 17 Nov) and `gold` (ratio 82.2/81.6/83.0 on settles). India: 13 straight FII buying sessions, record month ("highest-ever", not "since 2002"); rupee 93.41 (seven-month high); IT −4%. Saudi: new Yemen commander; Reuters: campaign "up to six months". Araghchi's "initiative" in Muscat with Qatar; IAEA Board opened 18 Nov; Shenzhen — Trump's Hormuz words, no Chinese readout (`china` watch to 20 Nov).
- **Graph.** 57 nodes touched; 63 signals; 29 summaries rewritten; 32 edge activations, 5 raised (us→irgc 9.0; houthis→saudi 10; brent→fed 10; semis→kospi 10; semis→taiwan 10); **new edge `semiconductors → fii-flows` (3.0, inverse)**. 137 triggers considered; **fired: `kospi`, `gold`** (data thresholds, not war). **New watches: `kuwait` (confirmed hit on a military site by 30 Nov); `israel` joint US–Israeli campaign (2+ consecutive nights, both roles confirmed, by 31 Dec).** Closest: `strait-of-hormuz` blacklist (*Al Dhannah* — listing not read at source), `houthis` Aden, `vix`, `european-ttf-gas` <€80.
- **Deployment.** Stay defensive. Cond 1 MET (three settles <$95; EFP ~0); cond 2 FAILS on both legs (10Y 5.07%; HY OAS 3.43%, wider); cond 3 buying met, inflation fails until 14 Dec. **OPEN FOR THE USER (proposed, not applied):** (i) Israeli strike as a reset; (ii) Iranian fire on a Gulf host as a reset — "fired at" now met at Bahrain (13/15/17/18 Nov) and Kuwait (18 Nov); (iii) November CPI bar (5.54% or <6.09%); **(iv) NEW: does an on-record US admission of a single "self-defense" launcher strike meet leg (a), or is it "logged, not fired" (the RESUME text's last sentence vs the 7/8-Nov precedent)?**
- **Fact-check.** 11 flags (1 critical, 4 high, 6 low), all applied, plus G1–G4. Critical: KOSPI Thursday close 5,137.89, not 5,112.97 (pre-final pulls). Highs: Fed minutes quote needed its subject ("a couple of participants"); leg (a) contested by the rule's own last sentence → decision (iv); Qeshm "one site" is the US account (Iran: "locations"); NAVIG8 MESSI name vs ADNOC casualties conflict (Sonowal: "entire crew" safe).
- **Process notes.**
  - **(1)** KOSPI was wrong AGAIN after the 16-Nov lesson — yfinance kept updating until ~14:00 IST. Re-pull Korea (and HK after 13:30 IST) immediately before publish, or use Naver/KRX.
  - **(2)** The CoS ruled leg (a) without re-reading the RESUME condition's last sentence. Before ruling on any trigger, read the FULL condition text in the node file, not the `_open_triggers.md` truncation (it cuts at ~230 chars).
  - **(3)** Quote fragments: desk quotes of documents (Fed minutes) dropped the subject. When a quote starts mid-sentence, check who is speaking in the source.
  - **(4)** Delegating markets/graph/brief to agents kept the CoS context small; the ~72-h window ran ~85 minutes end to end.
  - **(5)** Length: Sections I–III ~3.8k words after corrections (cap was 3.6k).
- **Open at publish.** On-record US ownership of Qeshm; who is firing at ships off Musandam; *Tara Gas*'s missing seafarer; NAVIG8 MESSI identity/casualties; the Shenzhen trilateral readout; night seventeen; Thursday's FII flows; Fri reserves; the *Al Dhannah* listing at source.
- **Dated tells.** 19 Nov night seventeen, Shenzhen readout; 20 Nov reserves, Vijayakumar 25,144.30, Kalın; 22 Nov earliest leg-(b); ~24 Nov Fesharaki; 29 Nov OPEC+; ~30 Nov Jan Brent expiry and the strike window's end; 2–4 Dec RBI; 6 Dec Kan; 9 Dec FOMC; ~11 Dec US funding; 14 Dec India CPI; 17 Dec ECB; 31 Dec UNIFIL; 3 Jan Congress.

---

## Decisions Made
- 2026-03-23: Project lives in ``
- 2026-03-23: Do deep research backfill BEFORE building anything (user decision — connections must emerge from data, not assumptions)
- 2026-03-23: Embed graph data in viewer.html (no server needed)
- 2026-03-23: Single-pass brief generation (no review step)
