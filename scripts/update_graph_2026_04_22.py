#!/usr/bin/env python3
"""
Graph update for 2026-04-22 morning edition.
Reads staging/2026-04-22-morning/{intel.md, markets.md} conceptually
and applies updates to graph nodes, edges, and meta.

Changes follow verification-tag discipline:
- CONFIRMED findings → full signal + weight adjustment
- REPORTED → signal with attribution + modest adjustment
- CLAIMED / single-source → signal only, no weight change
"""
import json
from pathlib import Path

TODAY = "2026-04-22"
NODES_DIR = Path("graph/nodes")
EDGES_FILE = Path("graph/edges.json")
META_FILE = Path("graph/meta.json")

def load(p):
    with open(p) as f:
        return json.load(f)

def save(p, obj):
    with open(p, "w") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)

def update_node(node_id, new_signals=None, current=None, summary_update=None,
                trigger_updates=None, trigger_adds=None):
    path = NODES_DIR / f"{node_id}.json"
    if not path.exists():
        return None, f"MISSING: {node_id}"
    node = load(path)
    actions = []
    old_last = node.get("last_updated")

    if new_signals:
        node.setdefault("signals", []).extend(new_signals)
        actions.append(f"+{len(new_signals)} signals")
    if current is not None:
        node["current"] = current
        actions.append("price updated")
    if summary_update:
        node["summary"] = summary_update
        actions.append("summary refreshed")
    if trigger_updates:
        for idx, updates in trigger_updates:
            for k, v in updates.items():
                node["trigger_points"][idx][k] = v
        actions.append(f"{len(trigger_updates)} triggers updated")
    if trigger_adds:
        node.setdefault("trigger_points", []).extend(trigger_adds)
        actions.append(f"+{len(trigger_adds)} new triggers")

    node["last_updated"] = TODAY
    save(path, node)
    return old_last, ", ".join(actions)


updates_log = []

# ---------- IRAN ----------
iran = load(NODES_DIR / "iran.json")
iran_trigger_updates = []
iran_trigger_adds = []
for idx, t in enumerate(iran.get("trigger_points", [])):
    cond = t.get("condition", "")
    if "Sadjadpour post-Touska falsifiable" in cond or ("kinetic action on US" in cond and "Tuesday 23:59 IST 2026-04-21" in cond):
        iran_trigger_updates.append((idx, {
            "status": "resolved",
            "mechanism": (t.get("mechanism", "") +
                " | RESOLVED 2026-04-22: Clock expired Tuesday 23:59 IST without confirmed Iranian kinetic. "
                "Only rhetoric through 72-hour window — Khatam al-Anbiya crew-family deferral, Ghalibaf 'new cards', "
                "Tasnim single-source drone-strike claim UNCORROBORATED by CENTCOM/Reuters/AP. "
                "Absorption branch fully vindicated. 2019 Aramco analogue confirmed.")
        }))
    elif "Iran-US ceasefire lapses Wednesday April 22" in cond:
        iran_trigger_updates.append((idx, {
            "status": "resolved",
            "mechanism": (t.get("mechanism", "") +
                " | RESOLVED 2026-04-22: Trump Truth Social Tuesday evening Washington EXTENDED ceasefire indefinitely "
                "'until Iran's leaders... come up with a unified proposal.' Pakistan PM Sharif + Army Chief Munir "
                "formally requested extension. Blockade continues. Vance/Witkoff Round 2 CANCELLED. "
                "Lapse branch did not fire. Next forcing function: Mojtaba Khamenei expected Wednesday response.")
        }))
    elif "Iranian delegation CONFIRMED in Islamabad by Tuesday 23:59 IST" in cond:
        iran_trigger_updates.append((idx, {
            "status": "resolved",
            "mechanism": (t.get("mechanism", "") +
                " | RESOLVED 2026-04-22: NOT MET. Iranian state TV publicly denied delegation Tuesday. "
                "FM spokesperson Baghaei confirmed no attendance. Vance/Witkoff trip cancelled after Trump extension. "
                "Round 2 Islamabad format indefinitely postponed pending Iranian 'unified proposal' submission.")
        }))

iran_trigger_adds.append({
    "condition": "Mojtaba Khamenei issues substantive Wednesday statement on US unified-proposal requirement (IRNA-carried or video/audio)",
    "cascade": ["iran", "united-states", "trump", "brent-crude", "strait-of-hormuz", "mojtaba-khamenei"],
    "mechanism": "Axios/Fortune reporting Tuesday: US and Pakistani mediators have been awaiting Mojtaba's response specifically; "
                 "civilian wing favours continued engagement while IRGC-adjacent hardliners publicly more skeptical. "
                 "Mojtaba is the deciding vote. Falsifiable: Wed 23:59 IST substantive statement OR "
                 "Thursday silence deepens the 'fractured' framing.",
    "added": TODAY,
    "status": "watching"
})
iran_trigger_adds.append({
    "condition": "Iranian unified proposal submitted to US/Pakistani mediators within 14 days",
    "cascade": ["iran", "united-states", "trump", "brent-crude", "sp-500"],
    "mechanism": "Trump's extension conditions US restraint on Iran submitting unified proposal. Signable proposal → Brent $85-88 "
                 "within 5 sessions; ceasefire could convert to permanent framework. Absence past 14 days → 'fractured' "
                 "framing deepens → US strike-plan probability rises.",
    "added": TODAY,
    "status": "watching"
})

iran_signals = [
    {
        "date": TODAY,
        "content": ("SADJADPOUR 72-HOUR ABSORPTION BRANCH FULLY VINDICATED [CONFIRMED ABSENCE of Iranian kinetic]. "
                    "Clock expired Tuesday 23:59 IST; Iran produced only rhetoric through the 72-hour window post-Touska seizure. "
                    "Outputs: Khatam al-Anbiya crew-family deferral (doctrinal posture), Ghalibaf 'new cards' framing, Pezeshkian "
                    "'Iranians do not submit to force' X post, Tasnim single-source claim of 'IRGC drones striking US vessels' "
                    "UNCORROBORATED by CENTCOM, Reuters, AP, or any Western navy tracker (tagged CLAIMED in intel.md). "
                    "2019 Aramco analogue confirmed: capability-demo without crossing military-on-military."),
        "sources": ["CENTCOM operational silence", "Reuters", "AP", "Intel dossier 2026-04-22"],
        "significance": "high"
    },
    {
        "date": TODAY,
        "content": ("IRAN UNIFIED HARDLINE DISMISSAL OF TRUMP EXTENSION [CONFIRMED, rhetoric not action]. Senior adviser "
                    "Mahdi Mohammadi: extension 'means nothing.' Tasnim (IRGC-linked) via advisor-to-Qalibaf: 'a ploy to buy time "
                    "for a surprise strike,' blockade 'no different from bombardment, must be met with military response.' "
                    "Tasnim further: 'As long as the blockade persists, Iran will not reopen the Strait of Hormuz, and, if "
                    "necessary, it will break the blockade by force.' Armed-forces spokesperson: '100% ready,' will give "
                    "'a harsher lesson than before.' Khatam al-Anbiya commander Ali Abdollahi: 'ready to give a decisive response.' "
                    "ALL RHETORIC — zero operational actions. IRNA silent; Tasnim said official position 'announced later.' "
                    "Civilian wing (Pezeshkian/Araghchi/Baghaei) tactically silent — narrower register than Tuesday's "
                    "enumerated-reasons mode. No Kayhan attack on Araghchi overnight — tacit factional acceptance of two-track "
                    "holds, narrowly."),
        "sources": ["Tasnim News Agency", "Reuters", "NBC News", "Al Jazeera", "ANI", "Fortune"],
        "significance": "high"
    },
    {
        "date": TODAY,
        "content": ("IRANIAN RIAL PARALLEL RATE 1,531,500 IRR/USD TUESDAY (Alanchand) — mild ~1% rial strengthening vs Monday's "
                    "1,546,500. 2,000,000 hyperinflation trigger unbreached; trajectory to 2M slightly flattened from earlier "
                    "'early-May' framing."),
        "sources": ["Alanchand.com"],
        "significance": "medium"
    },
    {
        "date": TODAY,
        "content": ("MOJTABA KHAMENEI RESPONSE EXPECTED WEDNESDAY [REPORTED, Axios exclusive sourcing]. Axios/Fortune Tuesday: "
                    "US and Pakistani mediators specifically waiting for Mojtaba's response; Iranian negotiators waiting 'for a "
                    "green light from the supreme leader.' CNN April 21 analysis and Time both note public absence is structural "
                    "feature. A substantive Wednesday statement (IRNA-carried written or video/audio) is the next forcing function."),
        "sources": ["Axios", "Fortune", "CNN", "Time"],
        "significance": "high"
    }
]

old, act = update_node("iran",
    new_signals=iran_signals,
    trigger_updates=iran_trigger_updates,
    trigger_adds=iran_trigger_adds)
updates_log.append(("iran", old, act))

# ---------- UNITED-STATES ----------
us_trigger_updates = []
us_trigger_adds = []
us_node = load(NODES_DIR / "united-states.json")
for idx, t in enumerate(us_node.get("trigger_points", [])):
    cond = t.get("condition", "")
    if "Treasury announces lift or modification of naval blockade before Wednesday April 22" in cond:
        us_trigger_updates.append((idx, {
            "status": "resolved",
            "mechanism": (t.get("mechanism", "") +
                " | RESOLVED 2026-04-22: NOT MET — blockade EXPLICITLY CONTINUES per Trump Truth Social ('directed our Military "
                "to continue the Blockade'). Ceasefire extended indefinitely instead. Structural: blockade-lifting conditioned "
                "on Iranian unified proposal.")
        }))

us_trigger_adds.append({
    "condition": "US Truth Social or Pentagon-channel statement converting strike plan from 'held' to 'active' OR executing strike",
    "cascade": ["united-states", "iran", "brent-crude", "strait-of-hormuz", "sp-500", "defense-sector", "gold"],
    "mechanism": "Trump's extension explicitly said 'hold our Attack on the Country of Iran' — confirming imminent US strike plan "
                 "existed pre-extension. TIO April 21: Israel 'coordinating potential attack plans with US.' A revert to 'active' "
                 "status → Brent $105-115, VIX 25+, ITA +10-15%, gold breaking $5,000. Falsifiable: any US strike post on "
                 "Truth Social within 30 days.",
    "added": TODAY,
    "status": "watching"
})

us_signals = [
    {
        "date": TODAY,
        "content": ("TRUMP EXTENDS IRAN CEASEFIRE INDEFINITELY TUESDAY POST-MARKET [CONFIRMED, 7-source]. Truth Social: "
                    "'Based on the fact that the Government of Iran is seriously fractured, not unexpectedly so and, upon the "
                    "request of Field Marshal Asim Munir, and Prime Minister Shehbaz Sharif, of Pakistan, we have been asked to "
                    "hold our Attack on the Country of Iran until such time as their leaders and representatives can come up with "
                    "a unified proposal. I have therefore directed our Military to continue the Blockade and... extend the Ceasefire "
                    "until such time as their proposal is submitted.' Three loaded elements: (1) reverses Monday's 'highly unlikely' "
                    "framing inside 36 hours; (2) first public presidential confirmation an imminent US strike plan existed ('hold "
                    "our Attack'); (3) first US public acceptance of Iranian factional paralysis as binding constraint ('seriously "
                    "fractured'). Vance/Witkoff/Kushner Round 2 CANCELLED. Blockade continues. No deadline for Iranian submission."),
        "sources": ["Trump Truth Social", "CNBC", "CNN", "Axios", "NBC News", "Al Jazeera", "Nikkei Asia"],
        "significance": "high"
    },
    {
        "date": TODAY,
        "content": ("FORTUNE ADMINISTRATION-DISCONTENT LEAK [REPORTED]. Fortune Tuesday: 'Trump officials whisper that his Truth "
                    "Social posts about Iran risk killing peace talks.' CNN Collinson analysis: 'Trump's craving for the spotlight "
                    "risks Iran deal hopes.' Pentagon channels silent — Jennifer Griffin, NBC Kube/Lee — consistent with "
                    "force-projection-silent de-escalation signal."),
        "sources": ["Fortune", "CNN"],
        "significance": "medium"
    },
    {
        "date": TODAY,
        "content": ("US EQUITIES TUESDAY CLOSE: S&P 500 7,064.01 (-0.63%), NASDAQ 24,259.96 (-0.59%), DOW 49,149.38 (-0.59%) "
                    "[CONFIRMED]. First Iran-sensitive down session since April 16. VIX 19.50 (+3.3%). Post-Trump-extension: "
                    "S&P 500 and Nasdaq 100 futures +0.4%, Dow futures +190 pts — partial retracement only. Tape now pricing "
                    "'extension without deal, blockade stays' as mildly risk-off."),
        "sources": ["CNBC", "TheStreet", "Yahoo Finance"],
        "significance": "medium"
    }
]
old, act = update_node("united-states",
    new_signals=us_signals,
    trigger_updates=us_trigger_updates,
    trigger_adds=us_trigger_adds)
updates_log.append(("united-states", old, act))

# ---------- TRUMP ----------
trump_signals = [
    {
        "date": TODAY,
        "content": ("TRUMP TRUTH SOCIAL EXTENDS IRAN CEASEFIRE INDEFINITELY; 'HOLD OUR ATTACK' LANGUAGE [CONFIRMED, primary + "
                    "multi-source relay]. Reversed Monday's 'highly unlikely' framing inside 36 hours. Three presidential-"
                    "messaging analytical loads: (1) attribute personally to Pakistan's Munir + Sharif — elevating Pakistan to "
                    "strike-suspension broker; (2) accepted publicly Iran is 'seriously fractured'; (3) held strike plan explicitly "
                    "rather than disavowed it. Iranian response: Mahdi Mohammadi 'means nothing,' Tasnim 'ploy to buy time for a "
                    "surprise strike.' The post moved Brent from overnight $101.97 spike to $92.48 Wed 11:51 IST — a $9.49 "
                    "presidential-messaging move, second confirmed Trump-post→Brent move of the crisis. Defense ITA -3.8%, "
                    "Frontline -4.3% — pure strike-plan premium deflation."),
        "sources": ["Trump Truth Social", "CNBC", "CNN", "Axios", "Nikkei Asia", "Fortune"],
        "significance": "high"
    }
]
old, act = update_node("trump", new_signals=trump_signals)
updates_log.append(("trump", old, act))

# ---------- BRENT-CRUDE ----------
brent_signals = [
    {
        "date": TODAY,
        "content": ("BRENT OVERNIGHT ROUND-TRIP: $95.48 TUE SETTLE → $101.97 (01:26 IST WED SPIKE, +7%) → $92.48 (11:51 IST WED) "
                    "[CONFIRMED, multi-source]. Arc: Tuesday European close $90.38 → Tuesday NYMEX US settle ~$95.48-95.75 "
                    "(US session recovered on Vance-Pakistan-trip-paused fear) → 01:26 IST Wed spike to $101.97 (+7.03%) → "
                    "Trump extension → Tokyo morning $98.48 → 11:51 IST Wed $92.48. Morgan Stanley $100 convergence trigger fired "
                    "briefly; extension unfired it. CRITICAL GRAPH STATE: Brent $92.48 is now BELOW pre-Touska-seizure Monday "
                    "($94.88) WHILE Hormuz physical transit remains at virtual standstill (Tasnim: 'Iran will not reopen the "
                    "Strait' while blockade persists). The paper-physical divergence yesterday flagged has REVERSED DIRECTION — "
                    "paper now UNDERPRICES physical disruption by ~$5-7/bbl. Reversibility VERY high — Mojtaba rejection would "
                    "drive Brent back to $97-100 within 48 hours."),
        "sources": ["ICE front-month", "CNBC", "Detroit News/Reuters", "Gulf News", "Trading Economics"],
        "significance": "high"
    }
]
brent_current = {
    "price": "$92.48 (Wed 11:51 IST); overnight arc $95.48 Tue settle → $101.97 spike → $92.48",
    "delta_1d": "-6.1%",
    "delta_1m": "-7.5%",
    "delta_3m": "+44.4%"
}
brent_trigger_adds = [{
    "condition": "Brent-Hormuz paper-physical divergence >$10/bbl in EITHER direction sustained 3 sessions",
    "cascade": ["brent-crude", "strait-of-hormuz", "marine-war-risk-insurance"],
    "mechanism": "Paper Brent (futures settle) vs dated Brent or physical-disruption-implied fair value. Direction reversed "
                 "Wednesday morning: paper $92.48, physical-implied value given Hormuz standstill ~$98-100. Either direction "
                 "sustained 3 sessions = trigger. Replaces previous one-sided divergence framing.",
    "added": TODAY,
    "status": "watching"
}]
old, act = update_node("brent-crude",
    new_signals=brent_signals,
    current=brent_current,
    trigger_adds=brent_trigger_adds)
updates_log.append(("brent-crude", old, act))

# ---------- GOLD ----------
gold_signals = [
    {
        "date": TODAY,
        "content": ("GOLD OVERNIGHT BREAKDOWN AND RECOVERY — $4,808.50 TUE → $4,677.22 (01:30 IST WED, -2.7%) → $4,780 (11:51 IST) "
                    "[CONFIRMED, Comex]. Largest intraday gold move of crisis. Overnight mechanism: Vance-cancellation + "
                    "talks-collapse → Brent spike → DXY bid → safe-haven INTO USD not gold → 10Y yields rose → gold sold as "
                    "funding currency. After Trump extension: Brent retraced, DXY softened, gold recovered almost all overnight "
                    "loss. CRITICAL REGIME-DIAGNOSTIC: yesterday's 'gold trades as inflation-regime not crisis-beta' thesis FULLY "
                    "VINDICATED by the overnight round-trip. $5,000 financial-event trigger further away; $4,900 peace-capitulation "
                    "trigger distant. Structural underperformance continues: 1M +8.5%, 3M -2.6%."),
        "sources": ["Comex front-month", "BusinessUpturn", "Trading Economics", "FX Leaders"],
        "significance": "high"
    }
]
gold_current = {
    "price": "$4,780.10 (Wed 11:51 IST); overnight low $4,677.22",
    "delta_1d": "+1.7% (settle-reference); -0.6% vs Tue spot $4,808.50",
    "delta_1m": "+8.5%",
    "delta_3m": "-2.6%"
}
old, act = update_node("gold", new_signals=gold_signals, current=gold_current)
updates_log.append(("gold", old, act))

# ---------- STRAIT-OF-HORMUZ ----------
soh_signals = [
    {
        "date": TODAY,
        "content": ("HORMUZ VIRTUAL STANDSTILL HOLDS; IRAN FORMALLY BINDS REOPENING TO BLOCKADE LIFT [CONFIRMED via Tasnim]. "
                    "Tasnim Wed morning IST: 'As long as the blockade persists, Iran will not reopen the Strait of Hormuz, and, "
                    "if necessary, it will break the blockade by force.' Codifies the IRGC-selective-control regime already "
                    "encoded as ACTIVE trigger. Trump's extension continues the blockade. Result: binary Wednesday risk on Hormuz "
                    "closure REMOVED (ceasefire extended) but ongoing physical suppression LOCKED IN for duration of extension. "
                    "Bloomberg/Windward/Daily Sabah data remains operative baseline: virtual standstill, ~3 crossings/12hr, 35 "
                    "vessel reversals (April 19 Windward). No fresh Wed AIS print. Paper Brent $92.48 now trading as if Hormuz "
                    "RESOLVED — paper-physical divergence reversed direction by $5-7/bbl."),
        "sources": ["Tasnim April 22", "Bloomberg", "Windward Maritime AI", "Daily Sabah"],
        "significance": "high"
    }
]
old, act = update_node("strait-of-hormuz", new_signals=soh_signals)
updates_log.append(("strait-of-hormuz", old, act))

# ---------- PAKISTAN ----------
pak_trigger_adds = [{
    "condition": "Pakistan-brokered Iranian unified proposal delivered to US within 21 days (Munir-Sharif channel)",
    "cascade": ["pakistan", "iran", "united-states", "trump", "brent-crude"],
    "mechanism": "Trump Truth Social Tuesday explicitly attributed US strike-plan suspension to Field Marshal Asim Munir and PM "
                 "Shehbaz Sharif's formal request. Elevates Pakistan from facilitator to strike-suspension broker. A successful "
                 "Pakistan-brokered Iranian unified proposal within 21 days converts ceasefire extension to durable framework; "
                 "failure returns strike plan to active status. Falsifiable: substantive Iranian proposal through Pakistani "
                 "channel by Tuesday 2026-05-13 IST.",
    "added": TODAY,
    "status": "watching"
}]
pak_signals = [
    {
        "date": TODAY,
        "content": ("PAKISTAN ELEVATED TO STRIKE-SUSPENSION BROKER BY US PRESIDENTIAL ATTRIBUTION [CONFIRMED]. Trump Truth Social "
                    "named Field Marshal Asim Munir and PM Shehbaz Sharif as the specific parties whose appeal caused US to "
                    "'hold our Attack on the Country of Iran.' First public attribution of Pakistani intervention as operative "
                    "reason for US military restraint — significant elevation from Round 1 Islamabad facilitator role to 'broker "
                    "who can pause US military action.' Pakistan FM Dar continues phoning Araghchi; China-Egypt-Pakistan mediator "
                    "architecture is now Pakistan-led with explicit US endorsement. Round 2 cancelled but Pakistan channel remains "
                    "highest-probability de-escalation path."),
        "sources": ["Trump Truth Social", "CNBC", "Axios", "Sahara Reporters"],
        "significance": "high"
    }
]
old, act = update_node("pakistan", new_signals=pak_signals, trigger_adds=pak_trigger_adds)
updates_log.append(("pakistan", old, act))

# ---------- NIFTY-50 ----------
nifty_current = {
    "price": "24,411.20 (Wed 11:51 IST intraday)",
    "delta_1d": "-0.7% (vs Tuesday close 24,576.60)",
    "delta_1m": "+2.7%",
    "delta_3m": "-3.5%"
}
nifty_signals = [
    {
        "date": TODAY,
        "content": ("NIFTY SOFT OPEN 24,413 → INTRADAY LOW 24,241 → 24,411 BY 11:51 IST [CONFIRMED, NSE live]. Despite Trump "
                    "ceasefire extension and Brent -$2.40/bbl vs Monday, Indian equities opened soft. Sensex -0.7% at 78,706. "
                    "Bank Nifty flat. IT sector 'tumble' (Infosys/HCL/Wipro) on US recession-risk transmission. Tested 50-day EMA "
                    "support at 24,240 zone; held. Breakdown vectors: profit-booking after Tuesday's +0.87% rally; FII continuation "
                    "(Rs 48,213 crore through April 10 NSDL, Rs 1.8 lakh crore FY26 Livemint); IT weakness on US macro fear; "
                    "rupee decoupling from oil relief. Key levels: support 24,240 (50-day EMA, BEING TESTED); resistance 24,576 "
                    "(Tue close, rejected once); structural watch 21,500 (200-day EMA trigger)."),
        "sources": ["NSE live", "5paisa", "Business Today", "Livemint", "NSDL"],
        "significance": "medium"
    }
]
old, act = update_node("nifty-50", new_signals=nifty_signals, current=nifty_current)
updates_log.append(("nifty-50", old, act))

# ---------- INR-USD ----------
inr_current = {
    "price": "₹93.81/USD (Wed 11:51 IST)",
    "delta_1d": "+0.7% rupee weaker (vs Tue close ₹93.50)",
    "delta_1m": "+0.6%",
    "delta_3m": "+2.5%"
}
inr_signals = [
    {
        "date": TODAY,
        "content": ("RUPEE ₹93.81 — TWO-SESSION DECOUPLING FROM OIL RELIEF [CONFIRMED]. Second consecutive session of rupee "
                    "weakening despite Brent dropping significantly. Tue ₹93.50 (Brent intraday retrace to $90.38); Wed 11:51 "
                    "₹93.81 (Brent $92.48). Mechanical oil-import transmission fully broken. Mechanisms: (1) Indian oil marketers' "
                    "sticky dollar demand for OPEC May/June lifting; (2) FII continuation at Rs 1.8 lakh crore FY26; (3) RBI "
                    "tolerating managed depreciation via NDF ban; (4) EM FX broadly weaker (KRW ₩1,477.68 +0.6%) — dollar-strength "
                    "dominating. REGIME CHANGE: rupee shifted from oil-correlated to capital-flow-correlated. The trigger "
                    "'USD/INR ₹95' remains watching but structurally threatened from the capital account side, not trade account."),
        "sources": ["yfinance", "Mumbai Port reference", "Livemint", "Business Standard"],
        "significance": "high"
    }
]
inr_trigger_adds = [{
    "condition": "USD/INR strengthens below ₹93 AND Brent above $95 sustained 5 sessions (capital-flow stabilisation signal)",
    "cascade": ["inr-usd", "india", "nifty-50", "rbi"],
    "mechanism": "Current 2-session decoupling (rupee weaker while Brent drops) shows capital-account dominating trade-account. "
                 "The REVERSE pattern — rupee strengthening with oil expensive — would signal capital flow returning. Falsifiable: "
                 "5 consecutive NSE closing prints with USD/INR <93 while Brent >$95.",
    "added": TODAY,
    "status": "watching"
}]
old, act = update_node("inr-usd", new_signals=inr_signals, current=inr_current, trigger_adds=inr_trigger_adds)
updates_log.append(("inr-usd", old, act))

# ---------- DEFENSE-SECTOR ----------
defense_signals = [
    {
        "date": TODAY,
        "content": ("DEFENSE ETF ITA -3.8% TUE CLOSE [CONFIRMED]. Lockheed -1.6% ($571.95), Northrop -0.66%. Strike-plan premium "
                    "deflation after Trump's ceasefire extension explicitly held the Iran strike plan. ITA's larger drop reflects "
                    "second-tier names having less $45bn congressional backlog protection. Northrop Q1 earnings posted Tuesday "
                    "(higher revenue on B-21 Raider demand) couldn't offset de-escalation headwind. Single cleanest 'ceasefire-works' "
                    "trade on US tape. Reversibility: Mojtaba rejection reverses drop within 48 hours; signable proposal continues "
                    "lower another 3-5%."),
        "sources": ["yfinance", "Investing.com", "Defense News"],
        "significance": "medium"
    }
]
defense_current = {
    "price": "ITA $223.09 (Tue close); Lockheed $571.95; Northrop ~$685.92",
    "delta_1d": "ITA -3.8%",
    "delta_1m": "+0.2%",
    "delta_3m": "-5.3%"
}
old, act = update_node("defense-sector", new_signals=defense_signals, current=defense_current)
updates_log.append(("defense-sector", old, act))

# ---------- ISRAEL ----------
israel_signals = [
    {
        "date": TODAY,
        "content": ("ISRAEL 'COORDINATING POTENTIAL ATTACK PLANS WITH US' ON IRAN TRACK [REPORTED, Times of Israel single-source]. "
                    "TIO April 21 live blog: 'Israel doubts prospects of Iran deal, is coordinating potential attack plans with US.' "
                    "Inverts Haaretz April 21 analytical pattern (dovish on Iran, pessimistic on Lebanon) — Israel is moving from "
                    "'decoupled-from-US-Iran-dovishness' to 'hedging-for-kinetic-if-talks-fail.' No Channel 12/13 or Haaretz "
                    "IDF imminent-strike leak as of 11:30 IST Wed. Add watching trigger."),
        "sources": ["Times of Israel"],
        "significance": "medium"
    }
]
israel_trigger_adds = [{
    "condition": "Channel 12/13 or Haaretz publishes IDF imminent-strike preparation on Iran track within 72 hours",
    "cascade": ["israel", "iran", "united-states", "brent-crude", "gold", "sp-500", "defense-sector"],
    "mechanism": "TIO reported Israel coordinating attack plans with US — single-source REPORTED. A follow-on Israeli-military-"
                 "source leak (Channel 12/13 are typical IDF leak channels; Haaretz military correspondents carry credible senior-"
                 "officer sourcing) would pre-indicate actual strike at 7-14 day horizon: Brent +$8-12, defense +5-8%.",
    "added": TODAY,
    "status": "watching"
}]
old, act = update_node("israel", new_signals=israel_signals, trigger_adds=israel_trigger_adds)
updates_log.append(("israel", old, act))

# ---------- MOJTABA-KHAMENEI ----------
mojtaba_signals = [
    {
        "date": TODAY,
        "content": ("MOJTABA RESPONSE EXPECTED WEDNESDAY — FORCING FUNCTION ELEVATED [REPORTED]. Axios/Fortune Tuesday: US and "
                    "Pakistani mediators awaiting Mojtaba's response; Iranian negotiators waiting 'for a green light from the "
                    "supreme leader.' CNN April 21 'Iran's new supreme leader is nowhere to be seen.' Time 'Iran's Supreme Leader "
                    "No Longer Reigns Supreme.' Public absence since April 10 Al Jazeera statement. 'Seriously fractured' framing "
                    "Trump adopted Tuesday leans directly on this uncertainty. A substantive Wednesday statement is now THE "
                    "forcing function of the crisis calendar."),
        "sources": ["Axios", "Fortune", "CNN", "Time"],
        "significance": "high"
    }
]
old, act = update_node("mojtaba-khamenei", new_signals=mojtaba_signals)
updates_log.append(("mojtaba-khamenei", old, act))

# ---------- SP-500 ----------
sp_current = {
    "price": "7,064.01 (Tue close)",
    "delta_1d": "-0.6%",
    "delta_1m": "+8.6%",
    "delta_3m": "+2.2%"
}
sp_signals = [
    {
        "date": TODAY,
        "content": ("S&P 500 7,064.01 TUE CLOSE (-0.63%), NASDAQ 24,259.96 (-0.59%), DOW 49,149.38 (-0.59%) [CONFIRMED]. "
                    "VIX 19.50 (+3.3%). First Iran-sensitive down session since April 16. Post-Trump-extension: S&P 500 and "
                    "Nasdaq 100 futures +0.4%. The VIX >22 trigger on Wednesday ceasefire lapse did NOT fire — ceasefire extended. "
                    "Asian Wednesday: KOSPI -0.14%, TAIEX +0.7%, Nikkei +0.3%, Hang Seng -1.3%, Nifty -0.7%."),
        "sources": ["CNBC", "yfinance", "TheStreet"],
        "significance": "medium"
    }
]
old, act = update_node("sp-500", new_signals=sp_signals, current=sp_current)
updates_log.append(("sp-500", old, act))

# ---------- SHIPPING-TANKERS ----------
tank_signals = [
    {
        "date": TODAY,
        "content": ("FRONTLINE -4.3% TO $35.38; BOAT -2.5%; PUREST DE-ESCALATION TRADE [CONFIRMED]. Ceasefire extension → "
                    "war-risk premium expectations decline → VLCC spot rates (TD3C) expected to soften from ~$423k/day late-March "
                    "peak → NAV accretion slows. Frontline 1M still +10% (Monday was full war premium); 3M +44% captures war "
                    "premium accumulation. Reversibility: very high — Mojtaba rejection reverses within 48 hours; signable deal "
                    "another 10-15% lower."),
        "sources": ["yfinance", "Lloyd's List"],
        "significance": "medium"
    }
]
old, act = update_node("shipping-tankers", new_signals=tank_signals)
updates_log.append(("shipping-tankers", old, act))

# ---------- MARINE-WAR-RISK-INSURANCE ----------
mwri_signals = [
    {
        "date": TODAY,
        "content": ("AWRP HOLDING ~1.0% POST-EXTENSION; MODERATION THESIS VINDICATED [CONFIRMED]. Gulf AWRP ~1.0% certain transits; "
                    "0.8% with NCB residency; 2.5-5% US/UK/Israeli nexus. LMA March 23 statement 'safety concerns, not insurance "
                    "availability, driving reduced vessel traffic' remains structural London market position. ≥1.5% step-up "
                    "trigger requires kinetic event; extension removes imminent-kinetic risk. Thursday London republish expected "
                    "1.0-1.2% band (not ≥1.5%)."),
        "sources": ["Lloyd's List", "LMA"],
        "significance": "medium"
    }
]
old, act = update_node("marine-war-risk-insurance", new_signals=mwri_signals)
updates_log.append(("marine-war-risk-insurance", old, act))

# ---------- VANCE ----------
vance_signals = [
    {
        "date": TODAY,
        "content": ("VANCE/WITKOFF/KUSHNER ROUND 2 ISLAMABAD TRIP CANCELLED [CONFIRMED]. After Trump Truth Social extension "
                    "announcement, US delegation will NOT travel to Islamabad for second round. First floated Tue afternoon "
                    "Washington as 'Vance trip paused' per NYT/Axios; finalised post-extension. Round 2 indefinitely postponed "
                    "pending Iranian unified proposal. Vance reported at White House Tue per Fox News live blog."),
        "sources": ["CNBC", "Al Jazeera", "NYT", "Axios"],
        "significance": "medium"
    }
]
old, act = update_node("vance", new_signals=vance_signals)
updates_log.append(("vance", old, act))

# ---------- PEZESHKIAN ----------
pez_signals = [
    {
        "date": TODAY,
        "content": ("PEZESHKIAN TACTICALLY SILENT WEDNESDAY — CIVILIAN-WING NARROWER PUBLIC CORRIDOR [OBSERVATION]. Tue evening "
                    "X post ('Iranians do not submit to force') hardened the public register; Wed morning IST no new statement. "
                    "Civilian wing silent while IRGC-orbit (Tasnim, Khatam al-Anbiya, armed-forces spokesperson) carries rejection "
                    "message. Narrow factional corridor — can't soften without losing IRGC support; can't harden without "
                    "preempting Mojtaba. Waiting-for-Mojtaba posture."),
        "sources": ["Observational — no new Pezeshkian output"],
        "significance": "low"
    }
]
old, act = update_node("pezeshkian", new_signals=pez_signals)
updates_log.append(("pezeshkian", old, act))

# ---------- LEBANON ----------
leb_signals = [
    {
        "date": TODAY,
        "content": ("LEBANON CEASEFIRE DAY 7 OF 10 — HOLDING WITH VIOLATIONS [CONFIRMED]. Lebanese military reports continued "
                    "Israeli shelling in Khiam, Bint Jbeil, Dibbin. Katz: IDF holds positions. TIO April 20: US reportedly plans "
                    "ask Lebanon repeal law forbidding contact with Israeli citizens. Washington Round 2 State Dept-hosted "
                    "Thursday April 23. TIO April 21 Israel 'coordinating attack plans with US' on Iran track — suggests hedging "
                    "against Iran-track failure while Lebanon deteriorates toward April 26 expiry."),
        "sources": ["Lebanese military", "Times of Israel", "Al Jazeera"],
        "significance": "medium"
    }
]
old, act = update_node("lebanon", new_signals=leb_signals)
updates_log.append(("lebanon", old, act))

# ---------- HOUTHIS ----------
hou_signals = [
    {
        "date": TODAY,
        "content": ("HOUTHI DAY 58 QUIET [CONFIRMED ABSENCE]. UKMTO JMIC Advisory Note Update 031 (April 12) maintains MODERATE "
                    "threat level for Bab el-Mandeb/Gulf of Aden. 'No verified evidence Houthi forces have resumed attacks on "
                    "commercial shipping.' Saree Feb 28 'fingers on trigger' unfired 54 days later. Steady state."),
        "sources": ["UKMTO JMIC Advisory Note 031"],
        "significance": "low"
    }
]
old, act = update_node("houthis", new_signals=hou_signals)
updates_log.append(("houthis", old, act))

# ---------- INDIAN-IT ----------
it_signals = [
    {
        "date": TODAY,
        "content": ("INDIAN IT SECTOR WEAK WED OPEN [REPORTED, Business Today intraday]. Infosys, HCL, Wipro, Tech Mahindra "
                    "drifting on US recession-risk concerns (indirect crisis transmission: oil-inflation → Fed cannot cut → US "
                    "growth pressure → Indian IT client budget cuts). Not directly crisis-linked. Contributes ~30% of Nifty -0.7%."),
        "sources": ["Business Today", "5paisa"],
        "significance": "low"
    }
]
old, act = update_node("indian-it", new_signals=it_signals)
updates_log.append(("indian-it", old, act))

# ---------- FERTILIZER-UREA ----------
urea_signals = [
    {
        "date": TODAY,
        "content": ("CF INDUSTRIES +4.6% TO $121.31 DESPITE CRUDE CRASH — STRUCTURAL NITROGEN SCARCITY DIVERGING FROM CRUDE "
                    "[CONFIRMED]. Nutrien +2.1% at $72.67 confirms sector bid. CF is clearest example of structural crisis "
                    "exposure without daily crisis correlation — function of Qatar's base-rate disruption (Ras Laffan unresolved) "
                    "+ spring planting demand + UBS PT $140. Urea FOB ME still at $702/mt (April 17 print, no Wed update). "
                    "If this were new crisis signal, spot urea would spike too — it isn't. Move is US-domestic fertilizer supply/"
                    "demand balance. Structural thesis intact."),
        "sources": ["yfinance", "UBS", "Argus", "Trading Economics"],
        "significance": "medium"
    }
]
old, act = update_node("fertilizer-urea", new_signals=urea_signals)
updates_log.append(("fertilizer-urea", old, act))

# === EDGES UPDATE ===
edges_data = load(EDGES_FILE)
edges = edges_data["edges"]

new_edges = []

if not any(e["from"] == "trump" and e["to"] == "brent-crude" for e in edges):
    new_edges.append({
        "from": "trump", "to": "brent-crude",
        "weight": 6.0, "directness": 1, "last_activated": TODAY
    })

if not any(e["from"] == "pakistan" and e["to"] == "united-states" for e in edges):
    new_edges.append({
        "from": "pakistan", "to": "united-states",
        "weight": 5.0, "directness": 1, "last_activated": TODAY
    })

isr_iran_found = False
for e in edges:
    if e["from"] == "israel" and e["to"] == "iran":
        e["weight"] = min(10.0, e.get("weight", 5.0) + 1.0)
        e["last_activated"] = TODAY
        isr_iran_found = True
        break
if not isr_iran_found:
    new_edges.append({
        "from": "israel", "to": "iran",
        "weight": 5.0, "directness": 1, "last_activated": TODAY
    })

edges.extend(new_edges)

edges_activated_today = [
    ("trump", "iran"), ("trump", "united-states"),
    ("iran", "united-states"), ("iran", "brent-crude"),
    ("strait-of-hormuz", "brent-crude"), ("pakistan", "iran"),
    ("united-states", "brent-crude"), ("brent-crude", "nifty-50"),
    ("brent-crude", "gold"), ("brent-crude", "inr-usd"),
    ("inr-usd", "nifty-50"), ("iran", "irgc"),
    ("iran", "strait-of-hormuz"), ("mojtaba-khamenei", "iran"),
]
for from_n, to_n in edges_activated_today:
    for e in edges:
        if e["from"] == from_n and e["to"] == to_n:
            e["last_activated"] = TODAY
            old_w = e.get("weight", 0)
            e["weight"] = min(10.0, old_w + 0.3)
            break

edges_data["edges"] = edges
edges_data["last_updated"] = TODAY
save(EDGES_FILE, edges_data)

# === META UPDATE ===
meta = load(META_FILE)
meta["last_updated"] = TODAY
meta["briefs_generated"] = meta.get("briefs_generated", 32) + 1
meta["total_edges"] = len(edges)
save(META_FILE, meta)

# === SUMMARY ===
print(f"\n=== Graph Update Summary 2026-04-22 ===")
print(f"Nodes updated: {len(updates_log)}")
for nid, old, act in updates_log:
    print(f"  {nid:30s} was {old}  →  {TODAY}  |  {act}")
print(f"\nNew edges: {len(new_edges)}")
for e in new_edges:
    print(f"  {e['from']} → {e['to']}  weight={e['weight']}")
print(f"\nEdges activated (weight bumped): {len(edges_activated_today)}")
print(f"\nMeta: {meta['total_nodes']} nodes, {meta['total_edges']} edges, brief #{meta['briefs_generated']}")
