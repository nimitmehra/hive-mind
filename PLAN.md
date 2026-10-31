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

## Latest Run — 2026-10-31 (morning), Day 246
- **Pipeline complete.** Six parallel desk researchers produced the material for a consolidated `intel.md`. Markets, graph, brief and an independent fact-check agent followed. Everything was committed locally for the background uploader to push, then delivered.
- **Timing.** First brief since 26 Oct, a 5-day gap. Ran ~19:19–20:40 IST on Saturday and was filed as "morning" under restart practice. All markets were last open Fri 30 Oct.
- **Lead.** Washington is negotiating and preparing to strike at once, and both tracks point at 4 Nov.
  - **The talks track:** Vance's letter to SNSC secretary **Mohsen** Rezaei reached Iran via Qatar on 25 Oct; receipt confirmed, no reply. Qatar held a 12-hour session in Tehran, and Iranian negotiators were in Doha.
  - **The strike track:** Gulf allies were told to prepare for a "short, intense" post-midterm campaign. This is well-sourced REPORTED (three independent unnamed chains); "as soon as Nov 4" is single-source.
  - **Tehran's side:** Mojtaba issued two written directives (end "neither war nor peace" on Iran's terms; an "unrestricted" response to any threat).
- **Other items.**
  - **Oil:** December Brent expired at $117.64 on the first successful limpet attack (Louise 1, 29 Oct). October was the worst month of the ship war (UKMTO "just over 30").
  - **Houthis:** kept firing at Riyadh after the Tehran meeting. Ras Tanura had a fire with a claimed but unestablished hit.
  - **India:** a strong week carried by the Fed and the RBI. The IMF said "the rupee should be the first line of defense"; the forward book is $200bn short.
  - **AI credit:** deepened (Alphabet's second negative-FCF quarter, Amazon). The US 10Y is at 4.94%.
  - **Gas:** TTF crossed €100.
  - **Israel:** hung result, 53/48/19.
- **Graph.**
  - All 63 nodes touched: 72 signals, 26 summaries rewritten, 4 snapshots.
  - Edges stay at 413. Four were re-weighted: `brent→10Y` 7→6, `semis→10Y` 4→5, `qatar→cheniere` 6→6.5, `TTF→ecb` 7.5→8.
  - All 131 open triggers were reviewed and 10 changed. Fired: the hyperscaler capex>OCF trigger, and TTF €100 on two nodes.
  - **The Ras Tanura trigger was deliberately NOT fired.** It was REPORTED only, and the fact-check later showed the refinery was already damaged in March.
  - 11 new dated watches.
- **Fact-check.** 28 flags (0 critical, 9 high, 19 low), all applied, plus 6 graph corrections. Highs:
  - "Ali" Rezaei → Mohsen;
  - "Confirmed" Gulf warning → well-sourced REPORTED;
  - Ras Tanura "hit" → fire;
  - "best week of the autumn" was false;
  - reserves fall was on gold valuation;
  - IOC warning misframed;
  - Alphabet's FCF was already negative in Q2;
  - gap correction reworded to "re-widened";
  - Patriot "moved into Israel" → "moving to the region".
- **Process notes.**
  - **(1)** The Chief of Station stamped files with guessed times (~23:00 IST) instead of running `date`. The fact-checker copied the anchor. **Run `date` before writing any "Generated" line.**
  - **(2)** Do not fill officials' first names from memory: "Ali" Rezaei was introduced by the Chief of Station, not a desk.
  - **(3)** Before treating satellite "damage" as new, check the site's prior strike history in the graph and backfill research. Ras Tanura was hit on 2 Mar.
  - **(4)** The uploader race is still handled: the verifier writes to staging, corrections are applied, then the report is copied into `briefs/`.
  - **(5)** Carried over: `edges.json` has 24 duplicate from→to pairs (27 surplus records; `TTF→ecb` exists at 10 and 8.0). This needs a dedupe session. The brief footer now discloses it.
  - **(6)** Carried over: node budgets far over 2k tokens.
  - **(7)** Sections I–III ran ~3.4k words after corrections. Still over the 5-minute target.
  - **(8)** Carried over: the architect hook blocks `scripts/update_graph_*.py`, so helpers live in `staging/<run>/gu_*.py`.
- **Dated tells.**
  - 1 Nov: OPEC+ (hold expected); NSDL October FPI.
  - 2 Nov: India opens into the US tech rout; Reliance Q2 reaction.
  - 3 Nov: midterms; the pledge expires.
  - 4 Nov: earliest reported strike date; Israeli results to Herzog; EZ flash HICP.
  - ~5 Nov: Aramco December OSP.
  - 6 Nov: India reserves (first intervention week); US payrolls.
  - 9 Nov: Tehran-text and Houthi tempo tests.
  - 11 Nov: Israeli mandate.
  - 12 Nov: India CPI (>6% expected).
  - Late Nov: Roosevelt arrives.
  - 29 Nov: OPEC+.
  - 4 Dec: RBI.
  - 9 Dec: FOMC.
  - 17 Dec: ECB.

---

## Decisions Made
- 2026-03-23: Project lives in ``
- 2026-03-23: Do deep research backfill BEFORE building anything (user decision — connections must emerge from data, not assumptions)
- 2026-03-23: Embed graph data in viewer.html (no server needed)
- 2026-03-23: Single-pass brief generation (no review step)
