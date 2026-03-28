# Hive Mind — System Architecture

> **What this is:** The definitive reference for any AI session working on this project. Captures the system design, data schemas, design decisions, and how everything connects.
> **Last updated:** 2026-03-25
> **Working directory:** ``

---

## 1. What This System Does

An **intelligence system** — not a news aggregator — that tracks the 2026 West Asia crisis (US-Israel war on Iran) and its cascading effects on global energy, commodities, currencies, and equity markets.

**For whom:** Nimit — growth investor sitting on cash, deploying with deep conviction after mapping and seeing risks clear. Indian + US equities/ETFs, 3-5yr horizon.

**Core outputs:**
1. **Daily brief** (via 5-step pipeline — see Section 9) — 5-minute read, Economist World in Brief style
2. **Living knowledge graph** — accumulates signals, strengthens connections, tracks cascade paths
3. **Interactive viewer** — `viewer.html`, open in browser, click to explore

**Brief generation pipeline:** `/gather-intel` → `/gather-markets` → `/update-graph` → `/write-brief` → `/verify-brief`. Each step has a single job and produces a staging file. See Section 9 for full details.

**The system gets smarter each day.** Day 30's analysis is materially better than Day 1 because the graph has 30 days of signals, refined edge weights, and tested trigger points.

---

## 2. Design Principles (Non-Negotiable)

1. **Information first, architecture second.** If the brief takes 10 minutes, it failed. Intelligence delivery beats elegant graphs.
2. **Signal over noise.** Every node, edge, signal must earn its place. 2-source minimum. Context-complete.
3. **The graph gets smarter, not bigger.** Growth = edge weight accuracy + trigger point quality, not raw node count.
4. **Simplicity, modularity, incremental.** Start discrete, grow organically.
5. **No external APIs.** Everything runs through Claude Code's WebSearch/WebFetch + yfinance for market data.
6. **Accumulated intelligence.** The knowledge graph IS the memory. The brief IS the daily changelog.

---

## 3. Project Structure

```
hive-mind/
├── .claude/commands/                 ← Pipeline sub-skills (Claude Code runs these)
│   ├── crisis-brief.md              ← Orchestrator — tells you the order
│   ├── gather-intel.md              ← Step 1: Crisis news + media tone
│   ├── gather-markets.md            ← Step 2: Market data + causal chains
│   ├── update-graph.md              ← Step 3: Graph updates + changelog
│   ├── write-brief.md               ← Step 4: Compose the brief
│   └── verify-brief.md              ← Step 5: Adversarial fact-check
├── briefs/YYYY-MM-DD.md             ← Daily intelligence briefs (final output)
├── staging/YYYY-MM-DD/              ← Pipeline intermediate files (per-day)
│   ├── intel.md                     ← Output of /gather-intel
│   ├── markets.md                   ← Output of /gather-markets
│   └── graph-changelog.md           ← Output of /update-graph
├── graph/
│   ├── nodes/{id}.json              ← One JSON file per persistent entity
│   ├── edges.json                   ← Master wiring diagram (all connections)
│   └── meta.json                    ← Graph stats, last updated, counts
├── research/                        ← Deep research documents
│   └── backfill-feb28-mar23.md      ← Initial 24-day crisis research
├── scripts/rebuild-viewer.py        ← Regenerates viewer.html with latest data
├── skills/crisis-brief.md           ← Readable copy of the skill
├── viewer.html                      ← Self-contained HTML graph viewer
├── ARCHITECTURE.md                  ← This file
├── CONTEXT.md                       ← Original design discussion (historical)
└── PLAN.md                          ← Work tracker
```

---

## 4. Data Schemas

### Node Schema (`graph/nodes/{id}.json`)
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
    "delta_3m": "+31%"
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
      "cascade": ["india-current-account", "inr-usd", "rbi-policy"],
      "mechanism": "India imports ~85% of crude; $100 oil adds ~$25B to annual import bill...",
      "added": "2026-03-24",
      "status": "watching | active | resolved"
    }
  ]
}
```

### Signal Writing Rules
Signals are NOT headlines. NOT one-liners. They are **context-complete sentences** that a reader can understand 3 months later without clicking anything.

**Bad:** `"Iran threatens Hormuz closure"`
**Good:** `"Iran's IRGC Navy chief threatened to close Strait of Hormuz if US/Israel strikes continue on Iranian oil infrastructure, following the March 21 Kharg Island attack (source: IRNA, corroborated by Reuters)"`

### Edge Weight Formula
```
weight = min(10, frequency × recency_factor × directness_multiplier)

frequency = activation_count (capped at 20 for normalization)
recency_factor = exponential decay (today = 1.0, 7 days = 0.7, 30 days = 0.3)
directness_multiplier = {1st order: 3.0, 2nd order: 1.5, 3rd order: 1.0}
```

### Edge Master Index (`edges.json`)
Flat list of all edges with `from`, `to`, `weight`, `directness`, `last_activated`. Enables graph traversal without loading every node file.

### Layer Determination (PageRank-like)
- **Layer 1 (center):** Nodes with ≥8 connections. Crisis backbone.
- **Layer 2 (middle):** 4-7 connections. Significantly involved.
- **Layer 3 (periphery):** 1-3 connections. Affected but not driving.
- Layer placement is NEVER hard-coded by category. A commodity with 26 connections sits at Layer 1 center.

---

## 5. Node Creation Rules

Create a new node ONLY when ALL conditions are met:
1. Entity appears across **2+ independent sources**
2. Has **causal connection to at least one existing node**
3. Is a **persistent entity** (country, commodity, company, institution, trade route, sector, person, index)
4. Is NOT an event or statement (those are signals on existing nodes)

**When NOT to create:** One-off mentions, events (→ signals), statements (→ signals on person/institution), speculative entities.

---

## 6. Connection Identification

When processing daily news, for each signal:
1. Identify which existing nodes are referenced
2. If two nodes appear in the same causal context → create/strengthen edge
3. Edge `context` field captures the mechanism (WHY they're connected)
4. Existing connection → increment `activation_count`, update `last_activated`, recalculate weight
5. New connection → create edge with `directness` assessment, initial weight

---

## 7. Brief Format — The Economist World in Brief Style

Each item in "What Happened" is written as **one paragraph (4-6 sentences)** that gives complete context. Not a full article. Not a one-liner. Like this:

> **Trump threatened to strike Iran's power plants, then backed down within 48 hours.** On Saturday, President Trump issued a 48-hour ultimatum demanding Iran reopen the Strait of Hormuz or face strikes on its power grid — an escalation that would have crippled civilian infrastructure across the country (source: NBC News, Al Jazeera, confirmed by White House press briefing). By Monday morning, Trump posted on Truth Social that the US was in "productive back-channel discussions" with Iranian intermediaries and that strikes were "on pause." Iran's Foreign Ministry immediately denied any talks were taking place, calling it "psychological warfare" (source: IRNA, corroborated by Iran International). The contradiction leaves the situation ambiguous — but the 48-hour deadline passed without action, which is itself a signal of constraint.

This format:
- Leads with the headline as a bold sentence
- Gives the full arc (what happened → what it means → what the other side says)
- Cites sources inline
- Ends with a forward-looking observation
- Is self-contained — understandable without yesterday's brief

---

## 8. Verification Architecture

### Two-pass verification (structural separation)
The crisis-brief skill uses a **two-pass verification architecture**:
- **Pass 1 (inline):** During Phase 4, apply the verification checklist below to each finding as it's gathered.
- **Pass 2 (separate skill):** After the brief is drafted (Phase 6), run `/verify-brief` — a separate adversarial fact-check gate that challenges every claim before publishing.

**Why two passes:** Pass 1 often fails because the researcher and fact-checker are the same cognitive flow — exciting findings bypass verification. Pass 2 is structurally separated: a different prompt, a different mindset (skeptic vs researcher), run AFTER the brief is written. This is the same principle as code review — you don't review your own code in the same sitting.

**Key rule for trigger points:** Trigger points move to "active" ONLY on confirmed actions verified by 2+ independent operational sources (maritime trackers, military channels, shipping insurers, published data). Threats, rhetoric, and preparations keep it at "watching" — no matter how aggressive the language.

### Verification Checklist (Pass 1)

Apply to EVERY geopolitical claim before including in the brief:
1. How many **independent** sources confirm? (Not citing each other)
2. **Date** of each source? (>48hrs old on active event = suspect)
3. Has the **subject** confirmed or denied?
4. Does only **one side** claim this?
5. Is the **headline supported** by the article body?
6. Is this being **amplified by adversarial media**?
7. What does actual **data** show? (shipping data, trade data > narrative claims)

**Known disinformation patterns (from March 2026):**
- "Seed and amplify" — one wire service report gets amplified into a stronger claim by downstream outlets
- "One side's framing as fact" — only one party to a deal announces what the other "committed to"
- "Stale source, active event" — articles >48hrs old not updated with corrections/denials

---

## 9. Brief Generation Pipeline

The daily brief is produced by a 5-step pipeline. Each step is a separate Claude Code command (`/skill`) with a single job. Each produces a staging file that the next step reads.

### Why a pipeline (not a monolith)
On March 24, 2026, the monolithic `/crisis-brief` skill elevated an aggressive IntelliNews headline into a factual claim. The verification protocol existed within the skill but was skipped because the researcher and fact-checker were the same cognitive flow. The pipeline fixes this by structural separation — each sub-skill has one role and cannot shortcut the others.

### Pipeline steps

```
/gather-intel    → staging/YYYY-MM-DD/intel.md         (Researcher)
/gather-markets  → staging/YYYY-MM-DD/markets.md       (Market Analyst)
/update-graph    → staging/YYYY-MM-DD/graph-changelog.md (Graph Engineer)
/write-brief     → briefs/YYYY-MM-DD.md                (Editor)
/verify-brief    → corrections applied                  (Fact-Checker)
```

| Step | Role | Input | Output | Key rule |
|------|------|-------|--------|----------|
| `/gather-intel` | Researcher | Graph state, web searches | `intel.md` with CONFIRMED/REPORTED/CLAIMED tags | Tag everything. Rhetoric ≠ Action. |
| `/gather-markets` | Market Analyst | `market-data.py`, web searches | `markets.md` with causal chains | Every significant move needs a WHY. |
| `/update-graph` | Graph Engineer | `intel.md` + `markets.md` | Updated `graph/` + `graph-changelog.md` | Respect verification tags. Trigger points need confirmed actions. |
| `/write-brief` | Editor | All staging files + graph | `briefs/YYYY-MM-DD.md` | CONFIRMED leads. RHETORIC goes last, gets proportional space. |
| `/verify-brief` | Fact-Checker | Brief + staging files | Corrections applied | Default to skepticism. Better to under-report. |

### Staging files
- Location: `staging/YYYY-MM-DD/` (date-partitioned, one directory per day)
- Format: Structured markdown with required section headers (see each sub-skill for format)
- Lifecycle: Persist for at least 7 days for auditability
- Gate checks: Each step verifies required staging files exist before proceeding

### Verification tag flow
The pipeline enforces a verification chain from research to publication:

1. `/gather-intel` tags each finding: **CONFIRMED** (2+ independent sources, both sides checked, operational data supports) | **REPORTED** (1 credible source, plausible) | **CLAIMED** (one side only)
2. `/update-graph` respects tags: CONFIRMED → full weight adjustment. RHETORIC → modest increase (0.5-1.0). CLAIMED → no weight change. Trigger points move to "active" ONLY on CONFIRMED ACTIONS.
3. `/write-brief` maps tags to language: CONFIRMED → state as fact. REPORTED → "reports suggest." CLAIMED → "[party] claims; [other party] denies."
4. `/verify-brief` cross-checks: Was anything elevated from its original tag?

### Running the pipeline
Type `/crisis-brief` to see the full pipeline order and gate checks. Then run each sub-skill in order. Or run them individually: `/gather-intel`, then `/gather-markets`, etc.

---

## 10. Cascade Paths (Verified from Research)

These are the documented cascade paths in the graph as of initial build:

1. **Hormuz → Oil → India CAD → Rupee → RBI dilemma → Nifty**
2. **South Pars attack → Iran retaliates on Qatar → LNG crisis → European gas → Fertilizer → India food security**
3. **Ras Laffan damage → Helium shortage → Semiconductor supply → AI infrastructure → Tech valuations**
4. **Saudi Yanbu bypass → But Yanbu attacked too → No safe Gulf export route**
5. **Iraq force majeure → Additional supply shock → Oil spike → Global stagflation**
6. **Oil → Inflation → Fed can't cut → Bond yields rise → Equity pressure everywhere**
7. **Defense/Energy rotation ← War → Tech selloff**
8. **Houthi wildcard — if they enter, Red Sea + Hormuz = double chokepoint**

---

## 10. Market Data Infrastructure

### Automated pull: `scripts/market-data.py`
Pulls **39 assets** across 8 categories via yfinance. Auto-flags significant moves (>2% daily, >10% monthly).

```bash
python3 scripts/market-data.py           # Full report with alerts
python3 scripts/market-data.py --alerts  # Only significant moves
python3 scripts/market-data.py --json    # Structured JSON for graph updates
```

**Categories covered:**
| Category | Assets | Examples |
|----------|--------|---------|
| Energy | 5 | Brent, WTI, Natural Gas, Heating Oil, Gasoline |
| Metals | 5 | Gold, Silver, Copper, Platinum, Palladium |
| Agriculture | 3 | Wheat, Corn, Soybeans |
| Equity Indices | 9 | S&P 500, NASDAQ, Nifty 50, Sensex, FTSE, DAX, Nikkei, Shanghai, Dow |
| Sector ETFs | 4 | Energy (XLE), Defense (ITA), Semiconductors (SMH), Shipping (BOAT) |
| Bellwether Stocks | 4 | Exxon, Lockheed Martin, Cheniere, Frontline |
| Bonds & Vol | 3 | US 10Y, US 2Y, VIX |
| Currencies | 5 | USD/INR, DXY, EUR/USD, USD/CNY, GBP/USD |

**NOT on yfinance (must web-search):**
- European TTF gas, VLCC tanker rates, urea/fertilizer, helium, container freight, war risk insurance, India 10Y yield

### Adjacent project data
| Data | Source | Cost | Project |
|------|--------|------|---------|
| Indian stocks | yfinance + Screener.in | Free | NSE-Tracker |
| US stocks | yfinance + EDGAR | Free | US-Stock-Tracker |
| US sector lists (Energy 31, Defense 18+, Shipping 26+, Fertilizer 4, Gold 5, LNG 5) | Pre-built | Free | US-Stock-Tracker |

---

## 11. Current Graph State (as of 2026-03-23)

- **30 nodes** across 7 types (13 countries, 5 commodities, 5 institutions, 4 indices, 1 person, 1 sector, 1 trade route)
- **117 edges** with weighted connections
- **Layer 1 (13 nodes):** Brent Crude (26 connections), Iran (24), Strait of Hormuz (18), India (15), US (10), Fed (10), Natural Gas/LNG (10), S&P 500 (9), INR/USD (8), RBI (8), Qatar (8), Israel (8), Nifty 50 (8)
- **Layer 2 (13 nodes):** Fertilizer, Hezbollah, Shipping, Saudi Arabia, OPEC+, China, Russia, US 10Y, Helium, Lebanon, Houthis, UAE, Iraq
- **Layer 3 (4 nodes):** Gold, Bahrain, Kuwait, Mojtaba Khamenei
- **Briefs generated:** 0 (backfill research done, daily briefs start tomorrow)
