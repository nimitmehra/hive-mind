#!/usr/bin/env python3
"""
Backfill for 2026-04-22 morning: 7 nodes that appeared on staging 'Nodes affected'
lists but were not primary-updated in the main update_graph_2026_04_22.py pass.

Top 3 (load-bearing today): irgc, us-10y-yield, india — full signals.
Bottom 4 (steady-state): rbi, qatar, hezbollah, red-sea — brief signals to stop staleness.
"""
import json
from pathlib import Path

TODAY = "2026-04-22"
NODES_DIR = Path("graph/nodes")

def load(p):
    with open(p) as f:
        return json.load(f)

def save(p, obj):
    with open(p, "w") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)

def add_signal(node_id, signal):
    path = NODES_DIR / f"{node_id}.json"
    node = load(path)
    node.setdefault("signals", []).append(signal)
    node["last_updated"] = TODAY
    save(path, node)
    return node.get("last_updated")

# ---------- IRGC (load-bearing) ----------
add_signal("irgc", {
    "date": TODAY,
    "content": ("IRGC-ORBIT OUTLETS CARRIED IRAN'S UNIFIED HARDLINE REJECTION OF TRUMP CEASEFIRE EXTENSION [CONFIRMED, rhetoric "
                "not action]. Tasnim News Agency (IRGC-linked) was the primary vehicle overnight: an adviser to Parliament Speaker "
                "Qalibaf called Trump's extension 'a ploy to buy time for a surprise strike,' framed the continuing US blockade as "
                "'no different from bombardment... must be met with a military response,' and declared 'As long as the blockade "
                "persists, Iran will not reopen the Strait of Hormuz, and, if necessary, it will break the blockade by force.' "
                "Khatam al-Anbiya Central Headquarters commander Ali Abdollahi added: 'ready to give a decisive response to the "
                "enemy's breach of covenant.' An Iranian armed-forces spokesperson claimed '100% ready' for a US surprise attack, "
                "promising 'a harsher lesson than before.' All of this is RHETORIC — zero operational action within the 72-hour "
                "Sadjadpour window that closed at Tuesday 23:59 IST. Tasnim's April 19 single-source claim that 'IRGC forces "
                "launched drone strikes on US military vessels' remains UNCORROBORATED by CENTCOM, Reuters, or AP — tagged CLAIMED "
                "in the intelligence dossier and consistent with information-operations signalling rather than executed action. "
                "Notably, no Kayhan attack on FM Araghchi or President Pezeshkian was amplified overnight; the April 19-20 Kayhan "
                "demand that Araghchi withdraw his Hormuz post has NOT carried into today — tacit IRGC acceptance of the two-track "
                "architecture (public hardline + private Araghchi-Dar channel) holds, narrowly."),
    "sources": ["Tasnim News Agency", "Reuters relay", "NBC News", "ANI/Times of Oman"],
    "significance": "high"
})

# ---------- US-10Y-YIELD (load-bearing) ----------
add_signal("us-10y-yield", {
    "date": TODAY,
    "content": ("US 10Y YIELD 4.29% (+1.0% 1D) — THE MECHANISM BEHIND GOLD'S OVERNIGHT BREAKDOWN [CONFIRMED, yfinance]. The 10-year "
                "Treasury yield rose from 4.25% Tuesday toward 4.29% during the overnight (01:26-01:30 IST) period when the "
                "Vance-cancellation/talks-collapse narrative peaked and Brent spiked to $101.97. The yield rise was the vehicle "
                "through which gold broke down to $4,677.22 at 01:30 IST: oil-inflation fears → bond selloff → higher real yields "
                "competed with gold → gold sold as funding currency while DXY bid absorbed the safe-haven flow. After Trump's "
                "extension announcement, Brent retraced, the inflation fear moderated, 10Y backed off, and gold recovered most "
                "of the overnight loss to $4,780. The 10Y at 4.29% remains within the 4.25-4.35% range that has held since "
                "the Touska seizure; 1M is -2.3% reflecting the broader steady-state of contained-crisis pricing on the long end. "
                "The regime diagnostic is clean: this crisis is being priced as inflation event (10Y sensitive to oil) not "
                "financial-system event (10Y would gap higher on bank stress, which hasn't happened)."),
    "sources": ["yfinance", "Trading Economics", "intel/markets dossiers 2026-04-22"],
    "significance": "medium"
})

# ---------- INDIA (load-bearing) ----------
add_signal("india", {
    "date": TODAY,
    "content": ("INDIA IS ABSORBING THE CEASEFIRE EXTENSION AS 'NOT A DEAL' RATHER THAN 'PEACE' — CAPITAL-ACCOUNT STRESS DOMINATING "
                "TRADE-ACCOUNT RELIEF [CONFIRMED, multi-source]. Wednesday 11:51 IST: Nifty 50 at 24,411 (-0.7% from Tuesday's "
                "24,576.60 rally close); Sensex 78,706 (-0.7%); Bank Nifty flat; USD/INR ₹93.81 (0.3% weaker vs Tuesday NSE close "
                "of ₹93.50). Mechanical transmission says Brent -$6/bbl from the overnight spike and -$2.40/bbl from Monday should "
                "have STRENGTHENED the rupee 0.6-1.0%; rupee has done the opposite, now two consecutive sessions. FII outflow "
                "total now Rs 48,213 crore through April 10 per NSDL, Rs 1.8 lakh crore FY26 per Livemint — updated number "
                "supersedes yesterday's Rs 1.61 lakh crore. Four simultaneous forces: (1) Indian oil marketers' sticky contracted "
                "dollar demand for OPEC May/June lifting; (2) FII continuation; (3) RBI tolerating managed depreciation via NDF "
                "ban; (4) broadly weaker Asian FX complex (KRW ₩1,477.68 +0.6%). REGIME READ: rupee has shifted from oil-correlated "
                "to capital-flow-correlated. The 21,500 Nifty 200-day EMA trigger now requires compounding events from the capital "
                "side, not any single oil shock. Indian IT weakness on US-recession transmission adds second-order indirect-crisis "
                "pressure (Infosys/HCL/Wipro). India 10Y G-Sec at 6.90% range-bound with FII debt outflow persisting. (Sources: "
                "NSE/yfinance, Livemint, NSDL, Business Today, Mumbai Port reference rate)"),
    "sources": ["NSE/yfinance", "Livemint", "NSDL", "Business Today", "Mumbai Port"],
    "significance": "high"
})

# ---------- RBI (steady-state) ----------
add_signal("rbi", {
    "date": TODAY,
    "content": ("RBI MANAGED-DEPRECIATION POSTURE CONTINUES; NO WEDNESDAY ANNOUNCEMENT [OBSERVATION, no new action]. NDF position "
                "ban remains the active visible-hand tool; $3.6 billion April intervention figure from earlier in the week is the "
                "operative scale. RBI did not defend ₹93 Tuesday as USD/INR moved ₹93.05→₹93.50 or Wednesday as it pushed to "
                "₹93.81 — consistent with the tolerate-orderly-depreciation posture. RBI weekly statistical supplement due Friday "
                "will give the next intervention-scale data point. No policy rate decision scheduled near-term; the next MPC is "
                "early-June. Steady state."),
    "sources": ["Observation — no Wednesday RBI output", "prior RBI intervention data"],
    "significance": "low"
})

# ---------- QATAR (steady-state) ----------
add_signal("qatar", {
    "date": TODAY,
    "content": ("QATAR STRUCTURAL DISRUPTION CONTINUES AS CF INDUSTRIES DIVERGENCE SIGNAL [OBSERVATION, structural-chain update]. "
                "No Qatar-specific news Wednesday (Foreign Ministry silent; Oman similarly quiet on back-channel posture). However, "
                "the Qatar-linked fertilizer-urea node showed structural re-assertion via CF Industries +4.6% and Nutrien +2.1% "
                "Tuesday — the market continues to price Ras Laffan disruption and Qatari nitrogen shortfall into the fertilizer "
                "complex independent of the crude-complex crash. Spot urea FOB ME $702/mt (April 17 print, no Wednesday update). "
                "Qatar's dual posture (Al Udeid US base + Iran relations + mediator role) gives it the quietest most-significant "
                "role in the crisis; its silence Wednesday is consistent with Round 2 cancellation routing mediation back through "
                "Pakistan rather than Gulf states. Steady state at the node; active at the commodity-chain level."),
    "sources": ["Inferential from CF/Nutrien market action; Qatar Foreign Ministry silence"],
    "significance": "low"
})

# ---------- HEZBOLLAH (steady-state) ----------
add_signal("hezbollah", {
    "date": TODAY,
    "content": ("HEZBOLLAH REGISTER UNCHANGED — FADLALLAH 'YELLOW LINE' FRAMING HOLDS, NO KINETIC [OBSERVATION]. No new Hezbollah "
                "statements Wednesday morning IST. Lawmaker Hassan Fadlallah's earlier position — the group would 'work to break "
                "the yellow line that Israel established' and 'no one in the country or abroad can disarm' Hezbollah — remains the "
                "operative public framing. No rocket fire since Lebanon ceasefire inception April 16-17 (Day 7 of 10). Katz "
                "restating IDF holds positions in southern Lebanon provides the accumulating quiet-cost casus belli without active "
                "engagement. Structural point reinforced: the April 26 ceasefire expiry arrives with permanent buffer zone + Yellow "
                "Line erosion regardless of rocket absence."),
    "sources": ["Observation — no new Hezbollah output", "earlier statements via Al Jazeera"],
    "significance": "low"
})

# ---------- RED-SEA (steady-state) ----------
add_signal("red-sea", {
    "date": TODAY,
    "content": ("RED SEA MARITIME CORRIDOR STEADY — UKMTO MODERATE THREAT LEVEL HOLDS DAY 58 [CONFIRMED, UKMTO JMIC Advisory 031]. "
                "No Houthi-attributed commercial shipping attacks; UKMTO advisory 031 (April 12, latest available) maintains "
                "MODERATE threat level for Bab el-Mandeb Strait and Gulf of Aden with explicit statement: 'no verified evidence "
                "that Houthi forces have resumed attacks on commercial shipping.' Container freight (FBX) remains mid-range with "
                "Red Sea diversions persisting; IEA April flagged Hormuz disruption is adding ~2x March Red Sea impact to global "
                "freight rerouting. Steady state."),
    "sources": ["UKMTO JMIC Advisory 031", "IEA April report"],
    "significance": "low"
})

print(f"Backfill complete. 7 nodes updated to {TODAY}.")
