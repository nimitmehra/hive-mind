# Hive Mind — Crisis Intelligence System

A knowledge-graph-driven intelligence system that tracks the 2026 West Asia crisis (US-Israel war on Iran) and its cascading effects on global energy, commodities, currencies, and equity markets. Built entirely with Claude Code.

**[Explore the Live Knowledge Graph](https://nimitmehra.github.io/hive-mind/viewer.html)**

---

## What This Is

An **intelligence system** — not a news aggregator — that produces daily briefs giving complete situational awareness. The crisis is the epicenter, but the shockwaves hit markets worldwide and THOSE markets create secondary effects and new connections.

**For whom:** An investor sitting on significant cash, waiting for deep conviction to deploy into Indian and US equities with a 3-5 year horizon. The system tracks when conditions are right — and more importantly, when they're not.

**The system must understand:** What happened in the war → What happened in global markets → WHY each market moved → Whether the move is crisis-linked or driven by something else → What new connections emerged → What trigger points are approaching.

### Core Outputs

1. **Daily Intelligence Brief** — 5-minute read, Economist World in Brief style. Verified, both-sides-checked, graph-driven analysis.
2. **Living Knowledge Graph** — Accumulates signals, strengthens connections, tracks cascade paths. Gets smarter each day.
3. **Interactive Viewer** — Click any node to see its signals, connections, trigger points, and price data.

---

## The Knowledge Graph

The graph currently tracks **46 nodes** across 7 types and **184 weighted edges** representing causal connections.

### Node Types
- **Countries** (16): Bahrain, China, India, Iran, Iraq, Israel, Kuwait, Lebanon, Pakistan, Qatar, Russia, Saudi Arabia, South Korea, Taiwan (TSMC), United Arab Emirates, United States
- **Commodities** (7): Aluminum, Brent Crude, European TTF Natural Gas, Fertilizer / Urea, Gold, Helium, Natural Gas / LNG
- **Institutions** (8): European Central Bank (ECB), Federal Reserve, Hezbollah, Houthis (Yemen), Islamic Revolutionary Guard Corps (IRGC), Marine War Risk Insurance, OPEC+, Reserve Bank of India
- **Indices** (4): INR/USD Exchange Rate, Nifty 50, S&P 500, US 10-Year Treasury Yield
- **Trade Routes** (2): Red Sea / Suez Canal, Strait of Hormuz
- **Sectors** (5): Defense & Aerospace Sector, Energy Sector (Global), Indian IT Sector (TCS/Infosys/Wipro), Indian Oil Marketing (IOC/BPCL/HPCL), Shipping / Tanker Rates
- **Persons** (4): Donald Trump, JD Vance, Masoud Pezeshkian, Mojtaba Khamenei

### How the Graph Works

Every node has **signals** (context-complete, sourced observations), **edges** (weighted causal connections to other nodes), and **trigger points** (thresholds that change the game if crossed).

Edge weights are calculated using: `weight = min(10, frequency x recency_factor x directness_multiplier)`

The graph doesn't just grow — it gets **smarter**. Day 30's analysis is materially better than Day 1 because the graph has 30 days of refined edge weights and tested trigger points.

### Cascade Paths (Verified)

These are the documented cascade paths the system tracks:

1. **Hormuz → Oil → India CAD → Rupee → RBI dilemma → Nifty**
2. **South Pars attack → Iran retaliates on Qatar → LNG crisis → European gas → Fertilizer → India food security**
3. **Ras Laffan damage → Helium shortage → Semiconductor fabs → HBM memory → NVIDIA GPUs → Magnificent 7 → S&P 500**
4. **Oil → Inflation → Fed/ECB/RBI can't cut → Bond yields rise → Equity pressure everywhere**
5. **Houthi Red Sea threat → Carrier voluntary withdrawal → Effective Bab al-Mandeb closure → Double chokepoint risk**
6. **Fertilizer disruption → Kharif 2026 sowing risk → India food inflation (Oct-Nov) → RBI rate cycle reversal**
7. **ALBA/EGA attacks → Aluminum $3,500 → Auto/construction/aerospace cost pressure**
8. **Hormuz decoupling → Oil stays $90-100+ even with ceasefire → Structural floor, not crisis premium**
9. **Defense sector decline during war → Political sustainability eroding → Market pricing stalemate**

---

## The Pipeline

The daily brief is produced by a 5-step pipeline. Each step is a separate Claude Code skill with a single job. The pipeline enforces structural separation — the researcher and the fact-checker are different "people" with different mindsets, preventing the kind of verification shortcut that caused the March 24 Houthi error.

```
/gather-intel    → staging/YYYY-MM-DD/intel.md         (The Researcher)
/gather-markets  → staging/YYYY-MM-DD/markets.md       (The Market Analyst)
/update-graph    → staging/YYYY-MM-DD/graph-changelog.md (The Graph Engineer)
/write-brief     → briefs/YYYY-MM-DD.md                (The Editor)
/verify-brief    → corrections applied                  (The Fact-Checker)
```

### The Team

Each pipeline step is designed as a **full job description** for a senior professional — not a checklist, but a persona with psychology, thinking process, media literacy, and examples of good and bad work.

| Role | Skill | Persona | Key Responsibility |
|---|---|---|---|
| **Senior Intel Analyst** | `/gather-intel` | 15-year RAW/MI6 veteran | Gather, verify, tag every finding. Separate rhetoric from action. Check both sides. |
| **Senior Market Analyst** | `/gather-markets` | 12-year macro hedge fund | Trace causal chains. Separate crisis-linked from non-crisis drivers. Every move needs a WHY. |
| **Graph Engineer** | `/update-graph` | Intelligence database specialist | Update the living knowledge graph. Respect verification tags. Triggers require confirmed actions. |
| **Senior Editor** | `/write-brief` | 20-year Economist writer | Compose the brief from dossiers. Verification status drives language. Page 1 = 5 minutes. |
| **Chief Fact-Checker** | `/verify-brief` | Der Spiegel verification dept | Adversarially challenge every claim. Default to skepticism. Better to under-report. |
| **Chief of Station** | `/crisis-brief` | 25-year intelligence manager | Orchestrate the pipeline. Gate checks after each step. Quality control. |

### Why a Pipeline (Not a Monolith)

On March 24, 2026, when this was a single monolithic skill, an aggressive IntelliNews headline ("Houthi join the fight") was elevated to a factual claim. Deep verification found ZERO confirmed Houthi attacks in 25 days — only escalating rhetoric. The researcher and fact-checker were the same cognitive flow, so verification was skipped in the excitement of a big finding.

The pipeline fixes this by structural separation. Each sub-skill has one job, one mindset, and cannot shortcut the others.

---

## Verification Architecture

The system enforces a verification chain from research to publication:

### Verification Tags
- **CONFIRMED** — 2+ independent sources, both sides checked, operational data supports
- **REPORTED** — 1 credible source, plausible but not independently verified
- **CLAIMED** — One side's assertion only, other side denies or hasn't responded

### Tag Flow Through Pipeline
1. `/gather-intel` tags each finding with verification status
2. `/update-graph` respects tags: CONFIRMED = full weight. RHETORIC = modest increase. CLAIMED = no weight change
3. `/write-brief` maps tags to language: CONFIRMED = stated as fact. REPORTED = "reports suggest." CLAIMED = "[party] claims; [other party] denies"
4. `/verify-brief` cross-checks: Was anything elevated from its original tag?

### Trigger Point Rules
Trigger points move to "active" ONLY on confirmed actions verified by 2+ independent operational sources (maritime trackers, military channels, shipping insurers, published data). Threats, rhetoric, and preparations keep it at "watching" — no matter how aggressive the language.

---

## Media Literacy Guide

The system includes a comprehensive media bias guide covering 50+ outlets across 6 regions, with political alignment, editorial context, and what-to-watch-for for each:

- **Iranian media** — IRNA (state), Tasnim (IRGC-linked), Press TV (propaganda), Iran International (diaspora)
- **Israeli media** — Haaretz (left, military sources), Times of Israel (centrist), Jerusalem Post (right/government)
- **US media** — Political map: CNN/WaPo/NYT (Democrat-aligned), Fox (Republican-aligned), NPR (most careful), AP/Reuters (neutral wire), WSJ (split: news centrist, editorial conservative)
- **Indian media** — BS/Livemint (centrist business), The Hindu (centre-left), HT (centre-right/government access), Republic/Times Now/Zee (propaganda)
- **Gulf media** — State-controlled (editorials ARE intelligence here). Al Jazeera (Qatar), The National (UAE), Arab News (Saudi)
- **European/Global** — FT (gold standard), Economist (pro-Western lens), BBC (careful), Reuters (foundation)

**Critical rule:** Editorials from independent media are NOT intelligence. Only state-controlled media editorials (IRNA, The National, TASS) reflect government positions.

---

## Project Structure

```
hive-mind/
├── .claude/commands/           ← 6 pipeline skills (Claude Code runs these)
│   ├── crisis-brief.md         ← Orchestrator
│   ├── gather-intel.md         ← Step 1: Crisis news + media tone
│   ├── gather-markets.md       ← Step 2: Market data + causal chains
│   ├── update-graph.md         ← Step 3: Graph updates
│   ├── write-brief.md          ← Step 4: Compose the brief
│   └── verify-brief.md         ← Step 5: Adversarial fact-check
├── briefs/                     ← Daily intelligence briefs (final output)
│   ├── 2026-03-23.md through 2026-04-01-morning.md (10 briefs)
├── graph/
│   ├── nodes/*.json            ← 43 entity files with signals, edges, triggers
│   ├── edges.json              ← Master edge index (171 weighted connections)
│   └── meta.json               ← Graph statistics
├── scripts/
│   ├── market-data.py          ← Pulls 62 assets via yfinance, flags significant moves
│   └── rebuild-viewer.py       ← Regenerates viewer.html with latest graph data
├── skills/                     ← Readable copies of the skills
├── research/                   ← Deep research documents
│   └── backfill-feb28-mar23.md ← Initial 24-day crisis research
├── viewer.html                 ← Self-contained interactive graph viewer
├── ARCHITECTURE.md             ← System design, schemas, verification rules
├── OPERATIONS.md               ← Full team handbook with personas, examples, media guide
└── README.md                   ← This file
```

---

## How to Use

### Prerequisites
- [Claude Code](https://claude.ai/claude-code) CLI installed
- Python 3.8+ with `yfinance` package (`pip3 install yfinance`)

### Running the Daily Brief

```bash
# Run the full pipeline (orchestrator guides you through all 5 steps)
/crisis-brief

# Or run individual steps
/gather-intel       # Gather and verify today's crisis developments
/gather-markets     # Pull market data and trace causal chains
/update-graph       # Update the knowledge graph from staging files
/write-brief        # Compose the brief from all dossiers
/verify-brief       # Adversarially fact-check before publishing
```

### Viewing the Knowledge Graph

Open `viewer.html` in any browser. Click nodes to see their signals, connections, trigger points, and price data. No server needed — fully self-contained.

Or view the live version: **[nimitmehra.github.io/hive-mind/viewer.html](https://nimitmehra.github.io/hive-mind/viewer.html)**

### Market Data

```bash
python3 scripts/market-data.py           # Full report with alerts
python3 scripts/market-data.py --alerts  # Only significant moves
python3 scripts/market-data.py --json    # Structured JSON for graph updates
```

Tracks 62 assets across 8 categories: Energy, Metals (incl. Aluminum), Agriculture/Food (incl. Rice, Sugar, Soybean Oil), Equity Indices (incl. Bank Nifty, Saudi Tadawul), Sector ETFs, Bellwether Stocks (incl. CF Industries, Linde, Nutrien, BASF), Bonds/Volatility, Currencies.

---

## Design Principles

1. **Information first, architecture second.** If the brief takes 10 minutes, it failed.
2. **Signal over noise.** Every node, edge, signal must earn its place. 2-source minimum.
3. **The graph gets smarter, not bigger.** Growth = edge weight accuracy + trigger point quality, not raw node count.
4. **No external APIs.** Everything runs through Claude Code's WebSearch + yfinance.
5. **Accumulated intelligence.** The knowledge graph IS the memory. The brief IS the daily changelog.
6. **Structural verification.** The researcher and fact-checker are structurally separated — different prompts, different mindsets, different pipeline stages.

---

## The March 24 Lesson

The entire pipeline architecture exists because of one error. On March 24, 2026, the monolithic skill elevated an aggressive IntelliNews headline ("Houthi join the fight") into a factual claim. Deep verification found ZERO confirmed Houthi attacks in 25 days — only escalating rhetoric that one outlet inflated to "entering the war."

The verification protocol existed within the skill but was skipped because the researcher and fact-checker were the same cognitive flow. The pipeline fixes this by structural separation — each sub-skill has one role and cannot shortcut the others.

Ironically, on March 28 (4 days later), the Houthis DID enter the war with a confirmed missile strike on Israel. The system correctly identified this as CONFIRMED ACTION — verified by IDF (interception), Houthi claim (Al-Masirah TV), and 4+ independent media sources. The lesson isn't that the Houthis weren't a threat — it's that 28 days of threats without action should not have been reported as action.

---

## Built With

- **[Claude Code](https://claude.ai/claude-code)** — AI-powered CLI for the entire pipeline
- **[Claude Opus 4.6](https://anthropic.com)** — Powers all 6 pipeline skills
- **[yfinance](https://pypi.org/project/yfinance/)** — Market data for 62 assets
- **[Cytoscape.js](https://js.cytoscape.org/)** — Interactive graph visualization (embedded in viewer.html)

---

## License

This project is open source. The intelligence analysis, graph data, and daily briefs reflect real-world events as of the 2026 West Asia crisis (February-April 2026) and are provided for educational and research purposes.

---

*Built by [Nimit Mehra](https://github.com/nimitmehra) with Claude Code*
