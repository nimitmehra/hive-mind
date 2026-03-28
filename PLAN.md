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

---

## Decisions Made
- 2026-03-23: Project lives in `/Users/nimitmehra/Documents/Manus/hive-mind/`
- 2026-03-23: Do deep research backfill BEFORE building anything (user decision — connections must emerge from data, not assumptions)
- 2026-03-23: Embed graph data in viewer.html (no server needed)
- 2026-03-23: Single-pass brief generation (no review step)
