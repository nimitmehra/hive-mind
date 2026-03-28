# The Hive Mind Crisis — Full Context Document

> **Purpose:** This document is the complete context for any AI session working on this project. It captures the problem, the user's thinking, every design decision, the reasoning behind each choice, the architecture, and the build plan. Read this fully before doing anything.

> **Last updated:** 2026-03-23
> **Working directory:** `/Users/nimitmehra/Documents/Manus/the-hive-mind-crisis/`
> **Adjacent projects:** NSE-Tracker, US-Stock-Tracker, MF-Tracker (all under `/Users/nimitmehra/Documents/Manus/`)

---

## 1. What We Are Trying to Achieve

### The Problem
The West Asia crisis (Israel-Iran-US conflict) creates cascading effects across global energy markets, commodities, financial markets, interest rates, inflation, and ultimately Indian and US equity markets. There is far more noise than signal. Reading 10 newspapers and following X accounts still leaves gaps — each source pushes one narrative and misses the interconnections.

### The User
Nimit is sitting on cash. He invests in Indian and US equities/ETFs (commodities and bonds via mutual funds). His holding period for direct equity is 3-5 years. He does NOT do tactical trades. He deploys capital with deep conviction after understanding sectoral tailwinds and, critically, after inverting — mapping all risks and seeing them clear.

He needs a system that:
1. **Separates signal from noise** in the West Asia crisis and its global ripple effects
2. **Builds accumulated memory** of what has happened, how things connect, and what trigger points exist
3. **Generates daily intelligence** — a 5-minute read, like The Economist's World in Brief
4. **Produces AI analysis** that gets smarter over time as the knowledge graph gets denser
5. **Helps him see when risks are clearing** so he can build conviction to deploy capital

### The End Goal
This is NOT a news aggregator. It is an **intelligence system** — a context engine with a living knowledge graph that accumulates understanding over time and can trace how a change in one node (e.g., helium shortage) cascades through 50 connected nodes to affect something seemingly unrelated (e.g., US interest rates via AI infrastructure collapse).

---

## 2. What the User Told Us — Key Requirements

### Daily Brief Requirements
- Run manually via `/crisis-brief` command in Claude Code
- Generates a file (markdown) the user reads — saved in `briefs/YYYY-MM-DD.md`
- **5-minute read, one page.** If too long, user will skip it. Brevity is critical.
- Styled like The Economist's World in Brief: headline + context paragraph per item
- Three sections:
  1. **What Happened** — sourced, cross-referenced, bias-assessed facts from last 24 hours
  2. **What Analysts Say** — expert takes with credibility context
  3. **My Analysis** — AI's own forward-looking analysis, informed by the knowledge graph
- Market snapshot: oil, gas, key indices (US, UK, India, China, Japan), bond yields, with 1d/1m/3m deltas
- Morning read, around 9-10am IST, triggered manually

### Source Requirements
- Every fact cross-referenced across 3-4 sources before reporting
- Assess publication bias (Bloomberg/Reuters may have China/US bias on India reporting)
- Use local media: Iranian (IRNA, Tasnim), Israeli (Haaretz, Times of Israel), Gulf (Al Jazeera, The National)
- Local media value: access to ground-level mood, unreported signals, tone of one side not verified by the other
- Identify quality geopolitical analysts on X — multi-order thinkers, not sensationalists
- Verify claims by checking if sources close to the OTHER side corroborate
- No paid data subscriptions. Use free sources only.

### What the Brief Must Cover
- Any attacks on infrastructure: what was attacked, why significant, what munitions, impact assessment
- Statements by key leaders on all sides
- Impact on energy markets: oil, gas, natural gas, helium, fertilizer
- All parties being drawn in: Gulf states attacked by Iran, Russia/China supplying one side, EU, others
- Sanctions, mediation efforts, diplomatic developments
- Tone from sources on either side: is conflict escalating or de-escalating?
- Impact on global financial markets, bond yields, central bank policy
- Any key fact or commodity insight that others may have missed

### Technical Constraints
- **No external APIs.** No Tavily, OpenAI, Gemini, or any API key usage. Everything runs through Claude Code's built-in web search and web fetch capabilities.
- **Manually triggered.** User runs the command. No cron jobs, no automation.
- **Local storage only.** All files in the project directory. May be open-sourced on GitHub later.
- **Design principles (non-negotiable):**
  1. Simplicity over complexity
  2. Modularity — separate concerns into reusable components
  3. Incremental code — small, testable changes
  4. Do not break what is working
  5. Information first, architecture supports information (NOT the other way around)

---

## 3. The Discussion — How We Got to the Architecture

### Socratic Dialogue Summary

**Round 1 — Understanding the User:**
- Confirmed: Indian + US markets only, equities/ETFs, 3-5yr horizon
- Confirmed: No tactical trades, conviction-based deployment
- Confirmed: Inversion thinker — maps risks, deploys when they clear
- Key insight: The system's ultimate purpose is helping him decide WHEN to deploy cash

**Round 2 — Layering Model:**
- User initially described "layers" (geopolitical → macro → markets → sectors → companies)
- We proposed: layers organized by CONNECTION STRENGTH, not by category
- User agreed strongly: "I do not want to hard-code it on the basis of show geopolitics first, then companies. It should be of how strong and how many number of nodes are coming to that particular point."
- This is essentially **PageRank for the crisis graph** — most-connected nodes surface to Layer 1 regardless of whether they're a country, commodity, or company

**Round 3 — Zoomable vs. Discrete Graph:**
- Zoomable graph (one canvas, semantic zoom) = ~3x more complex to build
- Discrete 3-layer graph (three linked views by connection strength) = simpler, modular
- **Decision: Start discrete, migrate to zoomable when enough data justifies it.** The data layer is identical for both — it's purely a rendering decision.
- This satisfies: simplicity, modularity, incremental, don't break what works

**Round 4 — The Memory Problem:**
- User's critical insight: "If you are just reporting what happened yesterday, you will not have any sort of shared memory of what has happened."
- Memory cannot live in a flat .md file — it must be a network with tags, linkages, connections
- **Decision: The knowledge graph IS the memory.** Every daily brief simultaneously updates the graph. The brief is the graph's daily changelog.
- User clarified: the AI analysis section should USE the graph memory to make connections, trace cascades, and provide forward-looking intelligence that gets smarter over time

**Round 5 — Risk Visualization:**
- We proposed red/amber/green risk flags on nodes
- User rejected: "I just don't want risk flags. They don't give a lot to me."
- We proposed alternative: edge thickness based on momentum (strengthening connections = thicker lines)
- **Decision: Edge weight determines visual thickness. No subjective traffic-light system.** The graph visually shows which connections are intensifying and which are fading. User reads the landscape himself.

**Round 6 — Node Granularity:**
- **Decision: Nodes are persistent entities** (countries, commodities, companies, trade routes, institutions, sectors)
- **Events and statements are data points ON nodes, not nodes themselves**
- "Khamenei died in Israeli strike" → Khamenei is a node, Israel is a node, the strike is information flowing between them
- This keeps the graph clean — prevents 500 event-nodes in a month

**Round 7 — Data Storage Depth:**
- Each node stores only **first-order (direct) edges**
- Cascade traversal happens at query time via `edges.json` master index
- **Why not store 2-3 levels deep?**
  - Duplication: same data in multiple files → sync nightmares
  - Staleness: when Iran's connections change, every file caching Iran's edges must update
  - Modularity violation: one change requires touching many files
  - Traversal is cheap: read `edges.json` (lightweight), walk the graph, read specific node files along the path
- **Exception: Trigger points** — curated cascade hypotheses stored per node. These are pre-identified "if X happens here, watch Y and Z" paths. Not exhaustive, but the known important ones.

**Round 8 — Price Storage:**
- Do NOT store price daily — wasteful and noisy
- **Current price: always overwritten** (latest + 1d/1m/3m deltas)
- **Snapshots: only at inflection points** (>3% daily move OR trigger threshold crossed)
- Each snapshot includes date, price, and WHY it moved (context-complete)

**Round 9 — Signal Granularity (How to Store News):**
- NOT original headlines (too terse, loses context)
- NOT two-word summaries
- **Context-complete sentences** that a reader (human or AI) can understand 3 months later without clicking anything
- Bad: `"Iran threatens Hormuz closure"`
- Good: `"Iran's IRGC Navy chief threatened to close Strait of Hormuz if US/Israel strikes continue on Iranian oil infrastructure, following the March 21 Kharg Island attack (source: IRNA, corroborated by Reuters)"`
- Each signal: date, what happened, why, who, sourced by whom

**Round 10 — Edge Schema:**
- Not two-word types like `"supply_route"`
- Includes a `context` field explaining WHY this edge exists and WHAT the mechanism is
- This is what enables intelligent cascade traversal — each hop has an explanation

---

## 4. Architecture — What We Decided

### Folder Structure
```
/Users/nimitmehra/Documents/Manus/the-hive-mind-crisis/
├── briefs/                     # Daily intelligence briefs
│   └── 2026-03-24.md
├── graph/
│   ├── nodes/                  # One JSON file per entity
│   │   ├── brent-crude.json
│   │   ├── iran.json
│   │   ├── israel.json
│   │   ├── strait-of-hormuz.json
│   │   └── ...
│   ├── edges.json              # Master wiring diagram (all connections)
│   └── meta.json               # Graph stats, last updated, node count
├── viewer.html                 # Self-contained HTML — open in browser to see graph
├── CONTEXT.md                  # This file
└── README.md                   # For open-source (how the system works)
```

### Node Schema (JSON)
```json
{
  "id": "brent-crude",
  "name": "Brent Crude",
  "type": "commodity | country | company | institution | trade_route | sector | person | index",
  "created": "2026-03-24",
  "last_updated": "2026-03-24",
  "summary": "One-line description of what this node represents and why it matters in the crisis context",
  "current": {
    "price": "$92.40",
    "delta_1d": "+2.1%",
    "delta_1m": "+14%",
    "delta_3m": "+31%",
    "snapshot_note": "Only present when price data applies to this node type"
  },
  "price_snapshots": [
    {
      "date": "2026-03-22",
      "price": "$88.10",
      "trigger": "Pre-Kharg Island attack baseline",
      "delta_context": "Jumped to $92.40 in 2 days post-attack"
    }
  ],
  "signals": [
    {
      "date": "2026-03-24",
      "content": "Iran's IRGC Navy chief threatened to close Strait of Hormuz if US/Israel strikes continue on Iranian oil infrastructure, following the March 21 Kharg Island attack (source: IRNA, corroborated by Reuters)",
      "sources": ["IRNA", "Reuters"],
      "significance": "high | medium | low"
    }
  ],
  "edges": [
    {
      "to": "strait-of-hormuz",
      "type": "supply_dependency",
      "context": "~20% of global oil (~17-20M bpd) transits Hormuz; closure would immediately remove this from market, causing supply shock",
      "directness": 1,
      "last_activated": "2026-03-22",
      "activation_count": 5,
      "weight": 8.4
    }
  ],
  "trigger_points": [
    {
      "condition": "Brent crosses $100/barrel sustained for 2+ weeks",
      "cascade": ["india-current-account", "inr-usd", "rbi-policy", "indian-equity-valuations"],
      "mechanism": "India imports ~85% of crude; $100 oil adds ~$25B to annual import bill, widening CAD to ~3.5% GDP, pressuring INR, forcing RBI to choose between defending currency and cutting rates",
      "added": "2026-03-24",
      "status": "watching"
    }
  ]
}
```

### Edge Master Index Schema (edges.json)
```json
{
  "last_updated": "2026-03-24",
  "edges": [
    {
      "from": "brent-crude",
      "to": "strait-of-hormuz",
      "weight": 8.4,
      "directness": 1,
      "last_activated": "2026-03-22"
    },
    {
      "from": "strait-of-hormuz",
      "to": "iran",
      "weight": 9.1,
      "directness": 1,
      "last_activated": "2026-03-22"
    }
  ]
}
```

### Edge Weight Formula
```
weight = frequency × recency_factor × directness_multiplier

Where:
- frequency = number of times this connection appeared in news in last 30 days
- recency_factor = exponential decay (yesterday = 1.0, 7 days ago = 0.7, 30 days ago = 0.3)
- directness_multiplier = {1st order: 3.0, 2nd order: 1.5, 3rd order: 1.0}

Weight is recalculated when the edge is activated (new signal references both nodes).
Weight range: 0-10 (normalized).
```

### Graph Meta Schema (meta.json)
```json
{
  "last_updated": "2026-03-24",
  "total_nodes": 25,
  "total_edges": 48,
  "briefs_generated": 1,
  "node_types": {
    "country": 8,
    "commodity": 5,
    "institution": 4,
    "trade_route": 2,
    "sector": 3,
    "company": 2,
    "index": 1
  },
  "layer_thresholds": {
    "layer_1_min_connections": 8,
    "layer_2_min_connections": 4,
    "layer_3_min_connections": 1
  }
}
```

### Layer Determination (PageRank-like)
- **Layer 1 (center):** Nodes with ≥8 connections (total incoming + outgoing edges). These are the crisis backbone.
- **Layer 2 (middle):** Nodes with 4-7 connections. Significantly involved but not central.
- **Layer 3 (periphery):** Nodes with 1-3 connections. Affected but not driving.
- Thresholds adjust as graph grows (stored in meta.json, recalculated periodically).
- Layer placement is NEVER hard-coded by category. A company with 15 connections sits at Layer 1. A country with 2 connections sits at Layer 3.

### Viewer (viewer.html)
- Single self-contained HTML file, no server needed (open in browser)
- Uses a JS graph library (Cytoscape.js or D3-force) bundled inline or via CDN
- Reads graph data from `graph/` folder (loaded via fetch or embedded)
- Discrete 3-layer layout initially (Layer 1 center, Layer 2 ring, Layer 3 outer)
- Edge thickness = weight (thicker = stronger connection)
- Click a node → panel/modal shows: summary, current data, recent signals, trigger points, direct connections
- Future: "Generate Analysis" button per node (triggers AI analysis for that node)
- Future: migrate from discrete to zoomable layout

### Node Creation Rules
A new node gets created when:
1. A new entity appears in the daily brief
2. It is mentioned across **2+ independent sources** (prevents noise)
3. It has a **causal connection to at least one existing node** (prevents orphans)
4. It is a **persistent entity** (country, commodity, company, institution, trade route, sector, person, index) — NOT an event or statement

When NOT to create a node:
- One-off mentions in a single source
- Events (these are signals on existing nodes)
- Statements (these are signals on the person/institution node)
- Speculative entities with no established connection

### How Connections Are Identified
When processing daily news, for each signal:
1. Identify which existing nodes are referenced (entity extraction)
2. If two nodes are referenced in the same causal context → create/strengthen edge between them
3. The edge `context` field captures the mechanism (WHY they're connected)
4. If the connection already exists → increment `activation_count`, update `last_activated`, recalculate weight
5. If the connection is new → create edge with `directness` assessment, initial weight

---

## 5. The Daily Brief Format

```markdown
# West Asia Crisis Brief — [Date]
*Generated at [time] IST | Graph: [X] nodes, [Y] edges*

---

## I. What Happened (Last 24 Hours)

### [Headline 1]
[Context-complete paragraph. What happened, who was involved, why it matters,
what triggered it. Sources noted inline. ~3-5 sentences.]

### [Headline 2]
[Same format. Each item is self-contained.]

### Market Snapshot
| Asset | Price | 1D | 1M | 3M |
|-------|-------|-----|------|------|
| Brent Crude | $92.40 | +2.1% | +14% | +31% |
| WTI | $88.60 | +1.9% | +12% | +28% |
| Natural Gas (Henry Hub) | ... | ... | ... | ... |
| Gold | ... | ... | ... | ... |
| Nifty 50 | ... | ... | ... | ... |
| S&P 500 | ... | ... | ... | ... |
| US 10Y Yield | ... | ... | ... | ... |
| India 10Y Yield | ... | ... | ... | ... |
| USD/INR | ... | ... | ... | ... |

---

## II. What Analysts Say

### [Analyst/Source Name] — [Affiliation/Credibility Context]
[Their take. What they said, what they predict, how reliable they've been.]

### [Another Analyst]
[Same format. 2-4 analysts per brief.]

### Source Tone Assessment
[Which side's media is escalating rhetoric? Which is quieting? What does the
tone shift suggest about intent?]

---

## III. Analysis — What the Graph Tells Me

### Cascade Watch
[Based on accumulated graph data: which edges are strengthening? Which trigger
points are approaching? What cascade paths should we monitor?]

### Forward View (1 month / 3 month)
[Based on current trajectory and historical patterns in the graph: where does
this go? What are the scenarios?]

### The Signal You Might Miss
[One non-obvious connection or development that mainstream coverage is not
highlighting but the graph data suggests is significant.]

### Risk Landscape
[For the investor: which risks are intensifying, which are fading? NOT traffic
lights — descriptive assessment of the risk environment for deploying capital
into Indian and US equities.]

---

*Graph updated: [N] nodes modified, [M] new edges, [K] new signals added*
*Open viewer.html to explore the knowledge graph*
```

---

## 6. Build Plan — Phases

### Phase 1 (Immediate — First Build)
1. **Folder structure** — create all directories
2. **Data schemas** — create empty `edges.json`, `meta.json` with initial structure
3. **Seed nodes** — create initial ~15-20 nodes for the current crisis (Iran, Israel, US, Brent, Hormuz, India, China, Russia, etc.) with known structural connections
4. **`/crisis-brief` skill** — Claude Code skill definition that:
   - Fetches news via Claude Code's web search/fetch
   - Cross-references sources
   - Generates the brief in the format above
   - Updates graph nodes with new signals
   - Updates edges.json with new/strengthened connections
   - Saves brief to `briefs/YYYY-MM-DD.md`
5. **viewer.html** — basic version showing nodes and connections, click for detail

### Phase 2 (After 1-2 Weeks of Data)
1. **Enhanced viewer** — thicker edges for stronger connections, layer layout by connection count
2. **Trend indicators** — show how edge weights have changed over time
3. **Node detail panel** — full signal history, trigger points, cascade paths
4. **Per-node analysis button** — click to get AI analysis of one specific node

### Phase 3 (After 1 Month of Data)
1. **Zoomable graph** — migrate from discrete 3-layer to continuous zoom
2. **Pattern detection** — AI identifies emerging patterns across the graph
3. **Scenario modeling** — "What if Hormuz closes?" trace all cascades
4. **India sub-graph** — deeper layer showing Indian sectors and stocks affected

---

## 7. Existing Data Stack (Reusable)

From adjacent projects in `/Users/nimitmehra/Documents/Manus/`:

| Data Type | Source | Cost | Used In |
|-----------|--------|------|---------|
| Indian stock prices | yfinance | Free | NSE-Tracker |
| Indian fundamentals | Screener.in (scraper) | Free | NSE-Tracker |
| US stock prices | yfinance | Free | US-Stock-Tracker |
| US SEC filings | edgartools (EDGAR) | Free | US-Stock-Tracker |
| Earnings transcripts | Motley Fool (scraper) | Free | US-Stock-Tracker |
| NSE announcements | NSE website (Playwright) | Free | NSE-Tracker |

**For the crisis system:** yfinance can provide commodity prices (Brent, WTI, Natural Gas, Gold) and index data (Nifty, S&P 500). No new data sources needed for market data.

**Existing sector stock lists in US-Stock-Tracker:**
- Energy: 31 stocks (XOM, CVX, COP, etc.)
- Defense: 18+ stocks (RTX, LMT, BA, etc.)
- Shipping: 26+ stocks (FRO, STNG, ZIM, etc.)
- Fertilizer: 4 stocks (CF, NTR, MOS, IPI)
- Gold: 5 stocks (NEM, GOLD, AEM, etc.)
- LNG: 5 stocks (LNG, TELL, GLNG, etc.)

These sector lists are directly relevant to the crisis analysis.

---

## 8. Key Design Principles — Never Violate These

1. **Information first, architecture second.** If a beautiful graph means the brief takes 10 minutes instead of 5, the brief wins. The system exists to deliver intelligence, not to be an elegant graph.

2. **Signal over noise.** Every node, every edge, every signal must earn its place. Two-source minimum for node creation. Context-complete signals only.

3. **The graph gets smarter, not bigger.** Growth should be in edge weight accuracy and trigger point quality, not in raw node count. 30 well-connected nodes beat 300 sparse ones.

4. **Simplicity, modularity, incremental.** Start discrete, migrate to zoomable. Start with 15 seed nodes, grow organically. Don't pre-build for hypothetical future needs.

5. **No external API dependencies.** Everything runs through Claude Code. User triggers manually. Self-contained.

6. **Accumulated intelligence.** The daily brief on Day 30 must be materially better than Day 1 because the graph has 30 days of signals, refined weights, and tested trigger points.

---

## 9. Example Cascade — How the System Thinks

**Starting event:** Iran's IRGC threatens Hormuz closure.

**Graph traversal:**
```
Iran [threat signal added]
  → Strait of Hormuz [disruption risk elevated]
    → Brent Crude [supply shock: 17-20M bpd at risk → price spike]
      → India Current Account [85% crude import dependency → CAD widens]
        → INR/USD [current account pressure → currency depreciation]
          → RBI Policy [defend rupee vs. support growth dilemma]
            → Indian Equity Valuations [FII outflow risk if INR weakens]
      → US Shale [benefits from price spike → energy sector gains]
        → S&P 500 Energy Sector [outperforms]
      → Natural Gas [linked pricing → LNG spot prices spike]
        → Fertilizer [gas-based fertilizer costs rise]
          → India Food Inflation [fertilizer subsidy burden]
            → RBI Policy [inflation mandate conflicts with growth]
    → Shipping/Tanker Rates [rerouting around Hormuz → longer voyages]
      → Global Trade Costs [container shipping inflation]
    → Helium Supply [Qatar is top producer, Gulf instability]
      → Semiconductor Manufacturing [helium needed for chip fab]
        → AI Infrastructure [chip supply constraints]
          → US Tech Valuations [growth rate uncertainty]
            → S&P 500 [tech-heavy index correction risk]
              → Fed Policy [market instability vs. inflation]
```

This cascade — from a single Iranian threat to Fed policy implications — is what the graph enables. No single newspaper reports this chain. The system sees it because the nodes and edges exist with mechanisms documented.

---

## 10. Open Questions (To Resolve During Build)

1. **Viewer technology:** Cytoscape.js (graph-native, good for networks) vs. D3-force (more flexible, steeper learning curve). Leaning Cytoscape.js for simplicity.
2. **Brief generation time:** How long will web fetching take within Claude Code? May need to optimize source list.
3. **Node merge/split:** What happens if two nodes should be merged (realized they're the same thing) or split (too broad)?
4. **Historical backfill:** Do we seed the graph with pre-existing crisis data, or start fresh from Day 1?
5. **India sub-graph depth:** When do we start adding individual Indian stocks as nodes? After Phase 1? Only when a crisis connection is directly identified?

---

*This document should be given to any new Claude session working on this project. It contains the full context of why, what, and how.*
