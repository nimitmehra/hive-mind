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

## Latest Run — 2026-11-20 (evening, FULL edition), Day 266
- **Pipeline complete.** Ran 20:12–~23:10 IST Friday (`date`-checked). Window 19 Nov ~13:15 IST → 20 Nov ~20:40 IST (~31 h). No 20-Nov morning edition, so this was a FULL brief labelled "Evening — Full Edition" (precedent: 19/21/22 Jul evening briefs run after 1 PM without a morning baseline). Six parallel desks (20:17–20:37 IST) → CoS header R1–R15 → `intel.md` (~36k words) → `markets.md` (agent) → graph (agent; backup `backups/2026-11-20/graph_v1`) → brief (agent) → fact-check (agent; 0 critical, 6 high, 11 low, G1–G5) → corrections (backups `graph_v2_preverif`, brief `2026-11-20-evening_v1.md`) → held for Trump's 22:30 IST news conference → local commit for the uploader → delivery.
- **Lead.** Trump (three interviews, Thu 19 Nov): Iran decision "after the beginning of the year" (CONFIRMED words; rhetoric). CBS (Fri, one outlet): US–Israeli assault considered "in the short term", "within two to four days, if such an order were given" (REPORTED); IDF: "no change to the current instructions" (public guidance). Senate rejected war powers 48–51. Night seventeen quiet → **no reset; earliest new leg (b) Mon 23 Nov**. No Iranian fire at Gulf hosts since 18 Nov. Yemen: PIF Tower, Riyadh, damaged (Thu; missile REPORTED); coalition says it struck Hodeidah port (Fri) — the Houthis' stated condition for hitting "all Saudi ports along the Red Sea coast"; no port strike found. AI/chip crash (US −2% Thu; TAIEX −6.23%, KOSPI −5.21% to 4,869.96, Nikkei −5.06% Fri) — war share ~0–5%; metals rout. India up 1.1% twice (Nifty 25,800.60, highest close since 18 Feb; Bank Nifty records); FII 15 straight sessions; rupee 92.67 PTI (first close stronger than 93 since 10 Apr); reserves −$14.205bn to $705.342bn (cause not split). Brent $91.98 Thu settle, ~$90.9 live (oil-only drop on Gulf "export flows"); TTF +8% on Norway/cold.
- **Graph.** 55 nodes; 59 signals; 34 summaries; 28 edge activations; raised `saudi-arabia → houthis` 10, `fii-flows → nifty-50` 10, `fii-flows → inr-usd` 10, `semiconductors → fii-flows` 3 → 4; **new edge `gold → rbi` 4.3**. **Status changes: `strait-of-hormuz` 2-Nov blacklist → FIRED (dated 17 Nov, on its letter: NAVIG8 MESSI, an ADNOC tanker on the PGSA list — attacker unnamed; list may follow strikes); `china` APEC → expired.** New watch: `saudi-arabia` Houthi strike on a Saudi Red Sea port or Shuqaiq, by 15 Dec. 133 open triggers.
- **Deployment.** Stay defensive. Cond 1 MET (four settles <$95); cond 2 FAILS (10Y par 5.04% Thu; HY OAS widening 3.43 → 3.52%); cond 3 buying met, inflation fails to 14 Dec. **OPEN FOR THE USER (proposed, not applied), unchanged:** (i) Israeli strike as a reset; (ii) Iranian fire on a Gulf host as a reset ("fired at" met at Bahrain 13/15/17/18 Nov, Kuwait 18 Nov; nothing since); (iii) November CPI bar (5.54% or <6.09%); (iv) whether an on-record admission of a single "self-defense" launcher strike meets leg (a).
- **Process notes.**
  - **(1)** The verifier caught a calendar error: **Tue 24 Nov is an NSE holiday (Guru Nanak Jayanti)** — trigger "earliest fire" dates must skip market holidays (graph `india.json` lists them). `inr-usd` earliest Wed 25 Nov; `fii-flows` Thu 26 Nov.
  - **(2)** Quote provenance: a Gulf News sentence was relayed as JMIC's words, and a Maritime Executive paraphrase of Martin Kelly was put in quotation marks by the CoS header — the CoS's own rulings need the same "summaries are not quotes" check as desk text.
  - **(3)** Graph "first" claims: the Graph Engineer wrote "first time he has put a date on the hold" — false (8 Oct Truth Social). Grep the node's own history before any "first".
  - **(4)** A chained string replacement in the changelog (Wed 25 → Thu 26) double-applied; apply date fixes per file/context, not globally in sequence.
  - **(5)** The CoS checked the blacklist evidence itself (Eagle PGSA mirror row 17; Maritime Executive 18 Nov) before ruling FIRED — keep doing this for any status change.
- **Open at publish.** What Trump said at the 22:30 IST news conference (indexed coverage thin at publish); night eighteen; Friday's Brent settle and Treasury/HY prints; whether the Houthis hit a Saudi port; NAVIG8 MESSI named by ADNOC; *Tara Gas*'s and the Jordanian seafarers; reserves split (intervention vs valuation).
- **Dated tells.** Mon 23 Nov earliest leg (b); Tue 24 Nov NSE holiday, ~Fesharaki; Wed 25 Nov earliest `inr-usd`; 27 Nov reserves (<$700bn watch); 29 Nov OPEC+; ~30 Nov Jan Brent expiry and strike-window end; 2–4 Dec RBI; 6 Dec Kan; 9 Dec FOMC; ~11 Dec US funding; 14 Dec India CPI; 15 Dec Houthi-ports watch; 17 Dec ECB; 31 Dec UNIFIL/joint-campaign watch; after 1 Jan Trump's own date; 3 Jan Congress.
- **Hygiene (not done):** `edges.json` holds 24 pre-existing duplicate from→to pairs (e.g. two `saudi-arabia → iran`) — needs a separate clean-up run.

---

## Decisions Made
- 2026-03-23: Project lives in ``
- 2026-03-23: Do deep research backfill BEFORE building anything (user decision — connections must emerge from data, not assumptions)
- 2026-03-23: Embed graph data in viewer.html (no server needed)
- 2026-03-23: Single-pass brief generation (no review step)
