#!/usr/bin/env python3
"""Graph update for 2026-05-03 morning brief (covers May 1-3 weekend gap).

Inputs:  staging/2026-05-03-morning/intel.md + markets.md
Outputs: graph/nodes/*.json (updated), graph/edges.json, graph/meta.json

Operates on the bounded hot-tier schema (post-2026-05-04 migration).
Each signal added is a HEADLINE only (full text preserved in git via this commit).
Cap and rolloff enforced per ARCHITECTURE_NODE_TIERING.md.
"""
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NODES = ROOT / "graph" / "nodes"
TODAY = "2026-05-03"
TOKEN_BUDGET = 1500
SOFT_LIMIT = 2000
BYTES_PER_TOKEN = 3.5
RECENT_SIGNALS_MAX = 5


def load(node_id):
    return json.loads((NODES / f"{node_id}.json").read_text())


def save(node_id, d):
    (NODES / f"{node_id}.json").write_text(
        json.dumps(d, indent=2, ensure_ascii=False)
    )


def estimate_tokens(obj):
    return int(len(json.dumps(obj, ensure_ascii=False)) / BYTES_PER_TOKEN)


def add_signal(d, headline, sources, verification="CONFIRMED"):
    """Append a signal headline with rolloff enforcement."""
    sig = {
        "date": TODAY,
        "headline": headline[:120],
        "sources": sources[:2],
        "verification": verification[:50],
    }
    if "recent_signals" not in d:
        d["recent_signals"] = []
    d["recent_signals"].insert(0, sig)
    # Cap at RECENT_SIGNALS_MAX
    d["recent_signals"] = d["recent_signals"][:RECENT_SIGNALS_MAX]
    return sig


def bump_edge(d, to, activation_inc=1):
    """Find edge by `to`, bump activation_count, update last_activated."""
    for e in d.get("top_edges", []):
        if e.get("to") == to:
            e["activation_count"] = e.get("activation_count", 0) + activation_inc
            e["last_activated"] = TODAY
            # Recompute weight per ARCHITECTURE.md
            freq = min(e["activation_count"], 20)
            d_factor = {1: 3.0, 2: 1.5, 3: 1.0}.get(e.get("directness", 1), 3.0)
            e["weight"] = min(10, freq * 1.0 * d_factor)
            return e
    return None


def update_summary(d, new_summary):
    d["summary"] = new_summary[:1700]


def touch(d):
    d["last_updated"] = TODAY


def update_node(node_id, signal_headline, sources, verification="CONFIRMED",
                summary=None, edges_to_bump=None):
    """Atomic update: load, mutate, save."""
    d = load(node_id)
    if summary is not None:
        update_summary(d, summary)
    add_signal(d, signal_headline, sources, verification)
    for to in (edges_to_bump or []):
        bump_edge(d, to)
    touch(d)
    tokens = estimate_tokens(d)
    save(node_id, d)
    return tokens


# ============================================================================
# Per-node updates for May 1-3 developments
# ============================================================================

UPDATES = [
    # Major: Iran 14-point proposal
    ("iran",
     "IRAN DELIVERS 14-POINT COUNTER-PROPOSAL VIA PAKISTAN; TRUMP 'NOT SATISFIED' BUT REVIEWING; IRGC OUTLETS VALIDATE",
     ["NPR", "Al Jazeera"],
     "CONFIRMED multi-source",
     "Day 65 Sunday. IRAN DELIVERS 14-POINT COUNTER-PROPOSAL VIA PAKISTAN MAY 1-2 — IRNA/Tasnim/Fars/Press TV all carry; Pakistani officials confirmed receipt to MS NOW. Trump 'not satisfied' but reviewing; 'leadership disjointed... two, three, maybe four groups.' Markets adjudicated as substantive: Brent -5.1% to $108.17, VIX -10% to 16.88, S&P record close 7,230. Rial decelerated 1.80M -> 1.83M (only +1.7% in 3D vs +36% prior 6D). Oil exports collapsed 73% to 567K bpd vs 2.1M pre-blockade (Kpler); $500M/day revenue loss; storage runway 26-76 days (Columbia CGEP). Tasnim/Fars (IRGC-linked) carrying proposal validates IRGC nominal alignment — meaningful shift from Apr 30 'operational paralysis.' 14-point asks: 30-day resolution, lift blockade, withdraw US forces from Iran's surroundings, free assets, compensation, full sanctions removal, end fighting on all fronts incl Lebanon, NEW Hormuz governance mechanism. Mojtaba Day 56 absence (Mashhad-mural-refutation window EXPIRED Day 8 of 7). Hezbollah-Lebanon 80+ killed 48hr May 1-2 in IDF strikes despite Apr 17 ceasefire. UAE OPEC exit effective May 1; Saudi MBS conspicuous-quiet Day 5 of 14. Chabahar US sanctions waiver expired Apr 26. Branches: kinetic ~25%, extended-economic-warfare ~50%, negotiated-resolution ~25% (re-priced UP from 10%).",
     ["trump", "united-states", "strait-of-hormuz"]),

    # Trump
    ("trump",
     "TRUMP 'NOT SATISFIED' WITH IRAN 14-POINT BUT REVIEWING; QUOTES 'LEADERSHIP DISJOINTED... TWO, THREE, MAYBE FOUR GROUPS'",
     ["Breitbart", "Al Jazeera"],
     "CONFIRMED multi-source",
     "Day 65. TRUMP 'NOT SATISFIED' WITH IRAN 14-POINT PROPOSAL BUT REVIEWING — first public acknowledgment of multiple Iranian factions seeking exit. May 1-2 quotes departing White House: 'they want to make a deal, but I'm not satisfied with it'; Iran is seeking terms 'I can't agree to'; 'the leadership is very disjointed... two, three, maybe four groups... they all want to make a deal but they're all messed up'; 'Iran has not yet paid a big enough price'; 'may never be a deal'; warned 'blast them away' if talks fail. Vowed maintain blockade. Markets adjudicated as opening of diplomatic window: Brent -5.1% Apr 29 -> May 1 to $108.17; VIX -10% to 16.88; S&P record close 7,230.12; AAPL +3.24%. Apr 30 brief's 'extended-economic-warfare-at-elevated-Brent base case' partially undercut by Brent collapse. New watching trigger: 'US substantively engages on Iran proposal within 14 days.'",
     ["iran", "strait-of-hormuz"]),

    # Brent
    ("brent-crude",
     "BRENT -5.1% TO $108.17 ON IRAN 14-POINT PROPOSAL; $115-SUSTAINED-2-SESSION TRIGGER RESOLVED-NO",
     ["CNBC", "TradingEconomics"],
     "CONFIRMED price tape",
     "Day 65. BRENT $108.17 (-5.1% 1D, +6.9% 1M, +60.7% 3M) — DOWN $9-12/BBL FROM APR 29 HIGHS IN 2 SESSIONS ON IRAN 14-POINT PROPOSAL. The $115-sustained-2-session trigger RESOLVED-NO (Apr 29 $118-120, Apr 30 ~$110.40, May 1 $108.17). Proximate driver: Iran 14-point proposal delivered via Pakistan May 1 (CNBC primary attribution). Cross-asset: WTI $101.94 -3%, RBOB -4.7%, Heating Oil -4.6%, Urea -14.23%, Iran rial decelerated, VIX -10%, S&P record. Operational reality unchanged: blockade in place, Iran exports 567K bpd (-73%), $500M/day revenue loss, 26-76 day storage runway. DIPLOMATIC RE-PRICING move, not SUPPLY DISRUPTION REVERSAL. If Trump publicly engages within 7 days, Brent likely tests $100-105; if rejects, rebounds to $112-118 within 5 sessions. UAE OPEC exit effective May 1 was calendar-priced through April. Deployment-signal counter-trigger 'Brent <$115 sustained 5+ sessions' Day 2 confirmed.",
     ["iran", "strait-of-hormuz"]),

    # INR
    ("inr-usd",
     "INR ₹95 TRIGGER ACTIVATED APR 30 — RECORD LOW ₹95.20 INTRADAY; CLOSE HELD ₹94.88 ON RBI DEFENSE",
     ["Sunday Guardian", "Business Standard"],
     "CONFIRMED multi-source",
     "Day 65. INR ₹95 TRIGGER ACTIVATED APR 30 — record low ₹95.20 intraday; close held at ₹94.88 on RBI defense. The Apr 30 morning brief was composed before the IST close and logged ₹94.82; this dossier corrects: actual session opened ₹95.01 and slipped to ₹95.20 record-low intraday driven by Brent above $120 spillover from Apr 29 US, FII outflows ₹8,047.86 Cr Apr 30 alone (NSDL), and FOMC hawkish-dissent DXY-firming. RBI conducted intermittent dollar-selling defending ₹95 round number — Bloomberg confirmed Governor framing FX curbs 'won't remain forever.' India closed May 1 (Maharashtra Day). Brent's collapse to $108.17 May 1 reduces oil-import-CAD pressure materially. Business Standard analysts now flag ₹96-97 as next levels if relief fades. The ₹95 trigger ACTIVATED on Apr 30; sustaining TBD Monday May 4 IST open.",
     ["india", "fed"]),

    # India
    ("india",
     "CHABAHAR WAIVER EXPIRED APR 26 + INR ₹95 ACTIVATED + OPERATION SINDHU 2,490 EVACUATED",
     ["Al Jazeera", "ORF"],
     "CONFIRMED multi-source",
     "Day 65. INR ₹95 TRIGGER ACTIVATED APR 30 (intraday low ₹95.20, close ₹94.88 on RBI defense). NIFTY 23,997.55 (-0.74%) / SENSEX 76,913.50 (-0.75%) Apr 30 close; FII outflows ₹8,047.86 Cr Apr 30 alone. NSE/BSE closed May 1 (Maharashtra Day); first post-INR-breach session is Monday May 4. CHABAHAR US SANCTIONS WAIVER EXPIRED APR 26 — India transferred ~$120M to Iran before sanctions reimposition (ET via Channel I Am, Al Jazeera, ORF). India now negotiating local-Iranian-management mechanism. INSTC 7,200km India-Europe corridor loses India-managed Iranian endpoint. India MEA Operation Sindhu: 2,490 nationals evacuated from Iran via land routes (May 2). India 10Y GOI ~7.0-7.1% (3-week high). Domestic Indian framing through Apr 30 close was bearish; recalibration expected Monday May 4 if Brent stays sub-$110, INR opens stronger, US S&P record + Apple beat price into Asian carry.",
     ["iran", "inr-usd"]),

    # Pakistan
    ("pakistan",
     "PAKISTAN CONFIRMED AS PRIMARY US-IRAN MEDIATOR ON 14-POINT PROPOSAL DELIVERY",
     ["NPR", "Al Jazeera"],
     "CONFIRMED",
     None,
     ["iran", "united-states"]),

    # UAE
    ("uae",
     "UAE OPEC EXIT EFFECTIVE MAY 1 — DAY 2-3 OF POST-OPEC ARCHITECTURE",
     ["Enerdata", "Khaleej Times"],
     "CONFIRMED",
     None,
     ["saudi-arabia", "opec-plus"]),

    # Saudi
    ("saudi-arabia",
     "SAUDI CONSPICUOUS-QUIET DAY 5 OF 14 — NO MBS STATEMENT POST-UAE-OPEC EFFECTIVE DATE",
     ["Chatham House", "Atlantic Council"],
     "REPORTED",
     None,
     ["uae", "opec-plus"]),

    # OPEC+
    ("opec-plus",
     "POST-UAE OPEC+ ARCHITECTURE — JUNE 7 MINISTERIAL FIRST STRUCTURAL TEST",
     ["Enerdata", "Atlantic Council"],
     "CONFIRMED",
     None,
     ["saudi-arabia", "uae", "brent-crude"]),

    # Fed
    ("fed",
     "CME FEDWATCH JUNE CUT 28% / HOLD 70%; POLYMARKET 56.4% PROBABILITY ZERO 2026 CUTS",
     ["CME FedWatch", "Polymarket"],
     "CONFIRMED",
     None,
     ["sp-500", "inr-usd"]),

    # S&P
    ("sp-500",
     "S&P 500 RECORD CLOSE 7,230.12 + AAPL +3.24% + VIX -10% + BRENT -2% — RISK-ON COORDINATION",
     ["TheStreet", "CNBC"],
     "CONFIRMED",
     None,
     ["semiconductors"]),

    # Gold
    ("gold",
     "GOLD $4,644.50 — HOLDS ABOVE $4,600 ON RISK-ON DAY (NOT REGIME-SHIFT ACTIVATION)",
     ["TradingEconomics", "Fortune"],
     "CONFIRMED",
     None,
     ["us-10y-yield"]),

    # Semiconductors
    ("semiconductors",
     "APPLE Q2 BEAT CLOSES LAST MAG 7 BINARY BULLISH — $111.2B REV, $20.5B GREATER CHINA, $100B BUYBACK",
     ["Apple IR", "CNBC"],
     "CONFIRMED",
     None,
     ["sp-500", "south-korea", "taiwan"]),

    # South Korea
    ("south-korea",
     "KOSPI -1.4% PROFIT-TAKING AFTER 1M +20.4%; KRW ₩1,471 EASED FROM APR 29 RECORD-NEAR",
     ["yfinance", "MacRumors"],
     "CONFIRMED",
     None,
     ["semiconductors"]),

    # Taiwan
    ("taiwan",
     "TAIWAN TAIEX -1.0% PROFIT-TAKING AFTER 1M +19.7%; APPLE BEAT REINFORCES TSMC THESIS",
     ["yfinance", "CNBC"],
     "CONFIRMED",
     None,
     ["semiconductors"]),

    # Hezbollah
    ("hezbollah",
     "HEZBOLLAH-LEBANON 80+ KILLED IN 48 HOURS BY IDF STRIKES — ONE-SIDED ESCALATION DESPITE APR 17 CEASEFIRE",
     ["Al Jazeera", "NBC News"],
     "CONFIRMED",
     None,
     ["israel", "lebanon"]),

    # Israel
    ("israel",
     "ISRAEL POSTURE BIFURCATES — HAWKISH ON LEBANON 80+ KILLED 48HR, RESTRAINED ON IRAN DIPLOMACY",
     ["Times of Israel", "Haaretz"],
     "CONFIRMED",
     None,
     ["hezbollah", "lebanon"]),

    # Lebanon
    ("lebanon",
     "LEBANON 80+ KILLED 48 HOURS BY IDF STRIKES — CEASEFIRE OPERATIONALLY DEAD MAY 1-2",
     ["Al Jazeera", "Washington Post"],
     "CONFIRMED",
     None,
     ["israel", "hezbollah"]),

    # Mojtaba
    ("mojtaba-khamenei",
     "MOJTABA WINDOW EXPIRED DAY 8 OF 7 — NO APPEARANCE; PROPOSAL VALIDATED VIA IRGC OUTLETS WITHOUT SUPREME-LEADER COVER",
     ["CNN", "Wikipedia"],
     "REPORTED via observation",
     None,
     ["iran", "irgc"]),

    # Russia
    ("russia",
     "RUSSIA NUCLEAR-CUSTODIAN TRACK STRUCTURALLY SIDELINED BY PAKISTAN-ROUTE PROPOSAL",
     ["Moscow Times", "INSS"],
     "REPORTED",
     None,
     ["iran"]),

    # Helium
    ("helium",
     "HELIUM FALSIFICATION HOLDS WEEK 2 — CAPE REROUTING WORKING; LINDE +1.4% INSUFFICIENT TO CONFIRM ROTATION",
     ["Tom's Hardware", "Foreign Policy"],
     "CONFIRMED",
     None,
     ["semiconductors", "qatar"]),

    # Urea
    ("fertilizer-urea",
     "UREA -14.23% TO $585/T MAY 1 — LARGEST SINGLE-DAY MOVE IN DOSSIER (3X BRENT'S MOVE)",
     ["TradingEconomics", "CME Group"],
     "CONFIRMED",
     None,
     ["india", "qatar"]),

    # Defense
    ("defense-sector",
     "LOCKHEED -1.0% (1M -17%) — DEFENSE UNDERPERFORMANCE HARDENS POST-IRAN-PROPOSAL",
     ["yfinance", "Lockheed Q1"],
     "CONFIRMED",
     None,
     []),

    # TTF
    ("european-ttf-gas",
     "TTF GAS €45.41/MWh -1.26% MAY 1 — DECOUPLED FROM BRENT MONTHLY (-3% 1M VS BRENT +6.9%)",
     ["TradingEconomics", "Reuters"],
     "CONFIRMED",
     None,
     ["natural-gas-lng"]),

    # Tankers
    ("shipping-tankers",
     "FRONTLINE +1.4% MAY 1 DESPITE BRENT COLLAPSE — IRAN SHADOW FLEET 31 SHIPS RETURNING ADDS 50M BBL",
     ["yfinance", "Columbia CGEP"],
     "CONFIRMED",
     None,
     ["iran", "strait-of-hormuz"]),

    # War risk
    ("marine-war-risk-insurance",
     "AWRP STABILIZING AT 1-5% HULL VALUE — DIPLOMATIC WINDOW EXTENDS PAUSE",
     ["Lloyd's List", "Strauss Center"],
     "REPORTED",
     None,
     ["strait-of-hormuz"]),

    # 10Y
    ("us-10y-yield",
     "US 10Y 4.38% -3BPS — REVERSED APR 29 SPIKE ON BRENT COLLAPSE",
     ["yfinance", "CME FedWatch"],
     "CONFIRMED",
     None,
     ["fed"]),

    # SOH
    ("strait-of-hormuz",
     "IRAN 14-POINT PROPOSAL INCLUDES 'NEW HORMUZ GOVERNANCE MECHANISM' — DAY 65 DUAL BLOCKADE PERSISTS",
     ["NPR", "Al Jazeera"],
     "CONFIRMED",
     None,
     ["iran", "trump"]),

    # Nifty
    ("nifty-50",
     "NIFTY 23,997.55 / SENSEX 76,913.50 APR 30 CLOSE; FII -₹8,047 CR; SETUP FOR MONDAY MAY 4 RECALIBRATION",
     ["yfinance", "Udaipur Times"],
     "CONFIRMED",
     None,
     ["india", "inr-usd"]),

    # IRGC
    ("irgc",
     "IRGC NOMINAL ENDORSEMENT VIA TASNIM/FARS PROPOSAL CARRY",
     ["Tasnim", "Fars"],
     "CONFIRMED",
     None,
     ["iran"]),

    # United States
    ("united-states",
     "TRUMP REVIEWING IRAN 14-POINT; S&P RECORD CLOSE 7,230; BRENT $108; CME ZERO-CUT 56%",
     ["TheStreet", "CNBC"],
     "CONFIRMED",
     None,
     ["iran", "trump"]),

    # Qatar
    ("qatar",
     "QATAR SUPPORTING-MEDIATOR ROLE HOLDS POST-IRAN-PROPOSAL; PAKISTAN PRIMARY",
     ["Al Jazeera", "Voice of Emirates"],
     "REPORTED",
     None,
     ["iran"]),
]


def main():
    print(f"Updating graph for {TODAY} (May 1-3 weekend gap coverage)...")
    print(f"Bounded hot-tier schema; cap {TOKEN_BUDGET} tokens, soft limit {SOFT_LIMIT}")
    print("=" * 90)

    total_warnings = []
    for entry in UPDATES:
        node_id, headline, sources, verification, summary, edges = entry
        try:
            tokens = update_node(node_id, headline, sources, verification, summary, edges)
            status = "OK" if tokens <= SOFT_LIMIT else "WARN"
            print(f"  [{status:4}] {node_id:30} {tokens:>5} tokens")
            if tokens > SOFT_LIMIT:
                total_warnings.append((node_id, tokens))
        except FileNotFoundError:
            print(f"  [MISS] {node_id:30} (file not found)")
        except Exception as e:
            print(f"  [FAIL] {node_id:30} {type(e).__name__}: {e}")

    # Update meta.json
    meta_path = ROOT / "graph" / "meta.json"
    meta = json.loads(meta_path.read_text())
    meta["last_updated"] = TODAY
    meta["briefs_generated"] = meta.get("briefs_generated", 0) + 1
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False))

    print("=" * 90)
    print(f"Updated meta.json: briefs_generated -> {meta['briefs_generated']}")
    if total_warnings:
        print(f"\nWARN ({len(total_warnings)} nodes over soft limit):")
        for n, t in total_warnings:
            print(f"  {n}: {t}")
    else:
        print("\nAll updated nodes within soft limit.")


if __name__ == "__main__":
    main()
