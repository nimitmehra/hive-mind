#!/usr/bin/env python3
"""Graph update for 2026-06-11 (morning). Reads staging dossiers, applies node/edge/trigger
updates respecting verification tags. Deterministic + JSON-validated. Backup already at
backups/2026-06-11/graph/. Run from repo root."""
import json, os

DATE = "2026-06-11"
NODES = "graph/nodes"

def load(nid):
    with open(f"{NODES}/{nid}.json") as f:
        return json.load(f)

def save(nid, d):
    with open(f"{NODES}/{nid}.json", "w") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)

def add_signal(d, headline, sources, verification):
    sig = {"date": DATE, "headline": headline, "sources": sources, "verification": verification}
    d.setdefault("recent_signals", [])
    d["recent_signals"].insert(0, sig)
    d["recent_signals"] = d["recent_signals"][:26]

def bump_edges(d, edge_updates):
    """edge_updates: list of (to, context_or_None, new_weight_or_None)"""
    for to, ctx, w in edge_updates:
        for e in d.get("top_edges", []):
            if e.get("to") == to:
                e["last_activated"] = DATE
                if isinstance(e.get("activation_count"), int):
                    e["activation_count"] += 1
                if ctx:
                    e["context"] = ctx
                if w is not None:
                    e["weight"] = w

def trigger_note(d, match_substrs, note_key, note_text, new_status=None):
    for t in d.get("active_triggers", []):
        cond = t.get("condition", "")
        if all(s.lower() in cond.lower() for s in match_substrs):
            t[note_key] = note_text
            if new_status:
                t["status"] = new_status
            return True
    return False

def add_trigger(d, trig):
    d.setdefault("active_triggers", []).append(trig)

def set_current(d, updates):
    d.setdefault("current", {})
    d["current"].update(updates)

CHANGED = []

# ============================ GEOPOLITICAL / CRITICAL ============================

# ---- united-states ----
d = load("united-states")
add_signal(d,
  "SECOND, LARGER US STRIKE ROUND + FIRST CONFIRMED INDIAN FATALITIES + KHARG SEIZURE THREAT. After Iran's 10 Jun first wave, CENTCOM struck Iran in three waves overnight 10-11 Jun (Trump: 49 Tomahawks, some within 40mi of Tehran) hitting Karaj/Abyek/Qeshm/Kish/Bandar Abbas/Sirik/Jask AND a South Pars-Asalouyeh petrochemical plant -- first widening into energy infrastructure. Hegseth at MacDill: 'CENTCOM will be busy tonight... we will negotiate with bombs.' Third 'bigger/more powerful' round threatened for tonight (RHETORIC until executed). Blockade enforcement (since 13 Apr) now 9 strikes on non-compliant tankers / 135 redirected / 42 humanitarian passages; this week MT Marivex (9 Jun, F-18), MT Settebello (10 Jun -- 3 Indian crew KILLED, first confirmed fatalities of the war at US hands), + a Guinea-Bissau tanker hit by 2 Hellfires (11 Jun). House passed war-powers resolution to end Iran hostilities 215-208 (3 Jun, 4 Republicans crossing) -- symbolic; Senate won't pass, Trump would veto; thin domestic cover.",
  ["CENTCOM/X", "CBS", "Al Jazeera Day 104", "Haaretz live", "WaPo/NPR/PBS"],
  "CONFIRMED (strikes + Settebello deaths + war-powers vote); RHETORIC (third round, Kharg)")
d["summary"] = ("Day 105 / 2026-06-11. **US TEMPO SHIFTED FROM ONE-OFF 'WARNING SHOT' (9 Jun, ~20 sites) TO NIGHTLY MULTI-WAVE STRIKE PACKAGES, NOW WIDENING INTO IRANIAN ENERGY INFRASTRUCTURE.** "
  "Overnight 10-11 Jun CENTCOM ran three waves on Iran (Trump: 49 Tomahawks; targets incl. a South Pars/Asalouyeh petrochemical plant); a third 'bigger' round was threatened for the night of 11 Jun (RHETORIC until executed). "
  "THE INDIA-CONSEQUENTIAL ESCALATION: the US blockade enforcement campaign (running since 13 Apr; 9 strikes on non-compliant tankers, 135 redirected, 42 humanitarian passages) produced the war's FIRST CONFIRMED FATALITIES AT US HANDS -- 3 Indian sailors killed on the disabled MT Settebello off Oman, prompting India to summon the US Charge and lodge a 'strong protest' ('these attacks must cease and end'). "
  "RHETORIC LAYER: Trump's Truth Social post threatening to 'take Kharg Island... and assume total control of their Oil and Gas Markets, much like Venezuela' -- walked back hours later on Fox ('not sure America has the stomach'). The strongest rhetorical signal the Kharg/ground-op trigger family has received, but NO confirmed action, NO force-posture buildup. "
  "DOMESTIC: the 3 Jun House war-powers vote (215-208, 4 GOP crossing) is the constraint baseline against which nightly strikes run -- symbolic but a fraying-cover datum. "
  "MACRO TRANSMISSION: US strikes -> Hormuz blockade -> energy +23.5% YoY -> May CPI 4.2% (3-yr high) -> a December Fed-HIKE now priced as live base-risk. The crisis is now transmitting into US assets through the CPI/Fed channel (slow, sticky), NOT the dead war-premium channel.")
bump_edges(d, [
  ("iran", "2026-06-11: Second, larger US strike round overnight 10-11 Jun (49 Tomahawks per Trump), widening into Iranian energy infrastructure (South Pars/Asalouyeh petrochem); third round threatened. CONFIRMED action.", None),
  ("shipping-tankers", "2026-06-11: Blockade enforcement turned lethal -- MT Settebello disabled off Oman, 3 Indian crew killed (first US-hand fatalities of the war); 9 strikes / 135 redirected / 42 humanitarian passages since 13 Apr.", 6.0),
  ("defense-sector", "2026-06-11: 'US signals more strikes' -> LMT +3.6% / ITA +2.6% on a -1.6% S&P day; first defense bid of this size since the May de-rate -- kinetic-continuation repricing.", None),
])
trigger_note(d, ["strike", "iran"], "note_2026-06-11",
  "RE-FIRES (already active). Second US strike round overnight 10-11 Jun (49 Tomahawks per Trump) widening into energy infrastructure -- another firing of an already-active trigger, NOT a watching->active transition.")
trigger_note(d, ["kharg"], "note_2026-06-11",
  "STAYS WATCHING. Trump's 11 Jun Truth Social post naming Kharg seizure + 'total control of Oil and Gas Markets, much like Venezuela' is the STRONGEST RHETORICAL signal this trigger-family has received -- but he walked it back same-cycle on Fox ('not sure America has the stomach'), and NO force-posture/amphibious buildup was reported. RHETORIC, not confirmed action. Window closes 2026-06-15; watch daily through Sunday.")
add_trigger(d, {
  "condition": "India takes material retaliatory/policy action against the US over the Settebello seafarer deaths beyond diplomatic protest (envoy recall, trade/tariff measure, basing or strategic-autonomy shift) within 30 days",
  "status": "watching",
  "cascade": ["india", "inr-usd", "nifty-50", "united-states"],
  "added": DATE,
  "note": "As of 11 Jun India's response is a summons of the US Charge + 'strong protest' + repatriation order -- diplomatic, not material. 3 weeks to the Section 301 tariff comment deadline; ~8m Indians in the Gulf. Watch for escalation beyond words."})
d["last_updated"] = DATE; save("united-states", d); CHANGED.append("united-states")

# ---- iran ----
d = load("iran")
add_signal(d,
  "SECOND RETALIATORY WAVE (12 ballistic missiles: Sheikh Isa/Bahrain, Ali Al Salem & Ahmad Al-Jaber/Kuwait, Al-Azraq/Jordan) -- all intercepted, near-nil damage (Jordan intercepted 20, no casualties). FM called the ceasefire 'MEANINGLESS' (downgrade from Monday's 'reassess'); top joint military command declared Hormuz 'complete closure.' Iran ABSORBED nightly US strikes WITHOUT striking Israel -- axis separation held for a 3rd consecutive iteration. Denied Trump's claim Iranian officials called him (CLAIMED). IRGC claimed 2 transiting tankers hit (CLAIMED, uncorroborated). Rial flat ~1.79m/USD -- did NOT crater on the strike exchange.",
  ["Al Jazeera Day 104", "MS NOW live", "Haaretz live", "Jordanian/Kuwaiti/Bahraini official statements", "Bonbast/Alanchand"],
  "CONFIRMED (second wave, intercepted; FM statements); CLAIMED (tanker hits, the called-Trump claim)")
d["summary"] = ("Day 105 / 2026-06-11. **THE WORDS MOVED TOWARD ESCALATION FASTER THAN THE DEEDS.** Iran's Foreign Ministry called the ceasefire 'meaningless' and the top joint military command declared Hormuz under 'complete closure' (no nationality exceptions) -- maximal in FORM. "
  "But the deeds stayed calibrated: the second retaliatory wave (12 ballistic missiles at US-hosting bases in Bahrain, Kuwait and Jordan) was again intercepted with near-nil damage -- a THIRD consecutive zero-fatality iteration -- and Iran absorbed the nightly US strikes WITHOUT striking Israel, keeping the two axes deliberately separated (ISW's exploit-the-Trump-Netanyahu-seam read). "
  "Two channel-preserving tells persist: NO formal termination of the negotiation track even while calling the ceasefire 'meaningless,' and Iran DENIED Trump's claim that its officials called him (rhetorical positioning, not door-closing). The IRGC's spectacular claims (21 targets, two tankers hit) continue the pattern with no verifiable damage behind them. "
  "The rial held flat ~1.79m/USD through the exchange (below the 2m hyperinflation trigger) -- a market vote that this is still calibrated, not regime-threatening. The structure remains negotiate-while-bombing, mirror-imaging Washington's.")
bump_edges(d, [
  ("bahrain", "2026-06-11: Second wave -- ballistic missiles at Sheikh Isa airbase; intercepted, 11-yr-old injured by intercepted-drone shrapnel.", None),
  ("kuwait", "2026-06-11: Second wave -- Ali Al Salem & Ahmad Al-Jaber airbases targeted; Kuwait closed airspace, suspended Kuwait Airways flights.", None),
  ("jordan", "2026-06-11: Second strike on Jordanian soil (Al-Azraq base); Jordan intercepted 20 missiles, no casualties or material damage. Second consecutive day Jordan hit.", 4.5),
])
trigger_note(d, ["rial"], "note_2026-06-11",
  "STAYS WATCHING. Rial flat ~1.79m/USD (10-11 Jun) -- did NOT crater on the second strike exchange; well below the 2,000,000 hyperinflation trigger.")
d["last_updated"] = DATE; save("iran", d); CHANGED.append("iran")

# ---- strait-of-hormuz ----
d = load("strait-of-hormuz")
add_signal(d,
  "FORMAL 'COMPLETE CLOSURE' DECLARED -- announcement CONFIRMED, operational delta CONTESTED. Iran's top joint military command announced Hormuz 'closed until further notice' for oil tankers AND commercial vessels, 'will be shot at,' NO nationality exceptions -- formally ending the selective/coordinated-passage regime (incl. the permitted Chinese transits the graph tracked). IRGC claimed 2 transiting tankers hit (CLAIMED -- no UKMTO/independent corroboration; UKMTO page 403). CENTCOM countered that commercial ships continue to transit (direct contradiction). Strait already ~5% of normal flow (Day ~104), so the declaration shifts the POLICY perimeter more than observed throughput. Aluminum recovered toward ~$3,600 on the formalization where gold did not move.",
  ["Al Jazeera 10 Jun", "Haaretz live", "NBC", "CENTCOM (contra)", "SeaVantage (vintage unconfirmed)"],
  "CONFIRMED (the declaration); CLAIMED (tanker hits); CONTESTED (actual throughput change)")
d["summary"] = ("Day 105 / 2026-06-11. **IRAN FORMALLY DECLARED 'COMPLETE CLOSURE' OF HORMUZ (no nationality exceptions, 'will be shot at') -- BUT THIS IS A POLICY ACT, NOT A CONFIRMED OPERATIONAL CHANGE, AND CENTCOM PUBLICLY DISPUTES IT.** "
  "(1) THE DECLARATION (CONFIRMED): Iran's top joint military command announced the Strait 'closed until further notice' for oil tankers and commercial vessels, explicitly with NO nationality exceptions -- formally terminating the selective-control / coordinated-passage regime in place since the April framework, including the Iran-permitted Chinese transits. "
  "(2) ENFORCEMENT (CLAIMED/CONTESTED): the IRGC claimed two transiting tankers were hit (no UKMTO or independent corroboration -- treat as CLAIMED); CENTCOM stated commercial ships CONTINUE to transit (a direct factual contradiction, with US incentive to deny Iran leverage). "
  "(3) THE OPERATIONAL READ: the strait was already at ~5% of normal flow (Day ~104, total traffic ~-95%), so 'complete closure' changes the POLICY perimeter (coordinated/Chinese transits now formally targets) more than the observed flow. Treat the ANNOUNCEMENT as fact and the OPERATIONAL DELTA as unverified. "
  "(4) THE MARKET TELL: aluminum recovered toward ~$3,600 on the formalization (the one real physical premium) where Brent moved <1.5% and gold FELL -- the market is pricing the declaration as choreography, not enforcement-at-scale. The structural picture (war-risk cover ~7-10% of hull, VLCC ~$100K/day ~2x YoY, the $40bn DFC reinsurance facility) is unchanged.")
bump_edges(d, [
  ("iran", "2026-06-11: Iran's top joint military command formally declared 'complete closure' of Hormuz (no nationality exceptions) -- ends the selective-control regime as POLICY; enforcement CLAIMED/contested (CENTCOM says transits continue).", None),
  ("brent-crude", "2026-06-11: Formal complete-closure declaration met with a <1.5% Brent move ($93.78) -- the declaration converts an operational reality into a declared one; no enforcement premium priced.", None),
])
trigger_note(d, ["remains under iranian selective control"], "note_2026-06-11",
  "STAYS active. The 10 Jun 'complete closure' declaration supersedes the selective-control framing as POLICY (no nationality exceptions), but enforcement is unconfirmed and CENTCOM says transits continue -- the operative regime on the water is unchanged. Stays active pending operational confirmation of the closure.")
trigger_note(d, ["kharg"], "note_2026-06-11",
  "STAYS WATCHING. Trump's 11 Jun Truth Social Kharg-seizure post is the strongest rhetorical signal yet but was walked back same-cycle ('not sure America has the stomach') with NO force-posture/amphibious-group reporting. Window closes 2026-06-15; watch daily through Sunday.")
add_trigger(d, {
  "condition": "Operationally-confirmed ENFORCEMENT of the 10 Jun complete-closure declaration -- Iran actually fires on / disables a transiting NEUTRAL vessel, verified by UKMTO or an independent maritime tracker (not an IRGC claim) -- converts the declaration from policy to action",
  "status": "watching",
  "cascade": ["brent-crude", "marine-war-risk-insurance", "shipping-tankers", "india", "vix"],
  "added": DATE,
  "note": "As of 11 Jun the closure is a DECLARATION; the only enforcement is the IRGC's uncorroborated 2-tanker claim, which CENTCOM contradicts. This trigger fires only on operationally-verified enforcement against a neutral hull -- the event that would convert the dead war-premium into a violent Brent gap toward $110+ and double AWRP. The market is positioned for choreography; this is the un-priced tail."})
d["last_updated"] = DATE; save("strait-of-hormuz", d); CHANGED.append("strait-of-hormuz")

# ---- trump ----
d = load("trump")
add_signal(d,
  "DEAL WHIPLASH + KHARG THREAT + WALKBACK. 9 Jun: deal 'two or three days away,' Hormuz to reopen 'immediately.' 10 Jun (post-strikes): Iran 'playing us for suckers,' 'taken too long,' 'pay the price' -> the 49-Tomahawk round. 11 Jun: Truth Social post -- US 'will be taking Kharg Island... and assume total control of their Oil and Gas Markets, much like Venezuela' + 'VERY HARD TONIGHT'; hours later on Fox walked it back ('not sure America has the stomach') while confirming talks continue. Claimed Iranian officials called him asking for a halt -- Iran DENIED (CLAIMED). Running both the escalation and de-escalation channels personally; the Fox venue for the walkback suggests base-appetite testing.",
  ["CNBC 9 Jun", "CBS/NPR/NewsNation", "Truth Social (via CNBC/Euronews/The Hill)", "Fox News", "Al Jazeera Day 104"],
  "CONFIRMED (the statements); RHETORIC/THREAT (Kharg seizure); CLAIMED (Iranian-call claim)")
d["last_updated"] = DATE; save("trump", d); CHANGED.append("trump")

# ---- india ----
d = load("india")
add_signal(d,
  "FIRST INDIAN WAR FATALITIES, AT US HANDS -- SOVEREIGNTY PIVOT. 3 Indian sailors (Aditya Sharma, Shivanand Chaurasiya, Patnala Suresh) killed on the disabled MT Settebello off Oman (US strike, 10 Jun; confirmed dead 11 Jun; 21 of 24 crew rescued). MEA summoned the US Charge d'Affaires, lodged a 'strong protest'; Jaiswal: 'These attacks must cease and end'; Sonowal ordered repatriation. Indian media pivoted markets->sovereignty (India vs America); Zee ran the summons prominently, Business Standard stayed transactional. Markets held: Nifty -0.23% (23,162), FII -Rs2,125cr Wed, rupee 95.79 (re-approaching Rs96). ~3 weeks to the Section 301 tariff comment deadline.",
  ["CBS", "Zee News", "BusinessToday", "MEA (Jaiswal)", "Business Standard"],
  "CONFIRMED (deaths, summons, market data)")
d["summary"] = ("Day 105 / 2026-06-11. **A NEW, NON-MARKET CHANNEL OF INDIA EXPOSURE OPENED: THE WAR'S FIRST INDIAN FATALITIES, KILLED BY THE US NAVY.** "
  "Three Indian sailors died on the disabled MT Settebello off Oman (US blockade-enforcement strike); India summoned the US Charge and lodged an unusually sharp 'strong protest' ('these attacks must cease and end') -- imperative language for Delhi's US lane. Indian media pivoted from market-mechanics to sovereignty/anti-US grievance (the sharpest tone shift in weeks), with the government-adjacent and mass-market outlets running the story and the business press staying transactional. "
  "The market channel held but thinned: Nifty -0.23% to 23,162 (IT the drag, Infosys -2.25%), FIIs sold Rs2,125cr Wednesday, and the rupee slid to 95.79 -- re-approaching Rs96 and ERODING the one ticked deployment box from yesterday. "
  "Deployment scorecard: Brent <$95 [met, barely], FII net-positive 3+ sessions [NOT met -- May was a record Rs55,963cr outflow month], organic Rs93-94 [NOT met -- 95.79 and weakening]. ONE of three met; NO deployment signal. The new variable: domestic political pressure on India's strategic-autonomy posture now comes from the AMERICAN direction, three weeks before the Section 301 comment deadline, with ~8m Indians in the Gulf.")
d["last_updated"] = DATE; save("india", d); CHANGED.append("india")

# ---- fed ----
d = load("fed")
add_signal(d,
  "MAY CPI 4.2% YoY (0.5% m/m) -- 3-YEAR HIGH, highest since Apr 2023. Energy +23.5% YoY = ~60% of the monthly increase (the oil->CPI->Fed chain is now the PRIMARY crisis-transmission channel into US assets); core 2.9% with its own momentum. Fed-cut hopes dead; ~98% hold priced for 17 Jun, but the market now prices a December HIKE as live base-risk (odds disputed across sources: CME FedWatch, Yahoo ~30% rising, Polymarket >50%). This print does NOT un-print on Gulf de-escalation -- energy base effects take 2+ quarters to flush.",
  ["BLS (via TechTimes/Yahoo)", "CME FedWatch", "CBS/CNBC", "Polymarket"],
  "CONFIRMED (published data)")
d["summary"] = ("**MAY CPI 4.2% (3-YR HIGH) LOCKS IN THE 'RATES-NOT-WAR' ENGINE.** The Fed's problem is no longer separable from the war: energy (war-derived via the Hormuz blockade) drove ~60% of the May monthly CPI increase to a 4.2% YoY headline, but core at 2.9% has its own momentum. "
  "Market pricing: a near-certain hold at the 17 Jun meeting, but a December HIKE is now priced as live base-risk (odds disputed 30->70%+ across CME FedWatch / Yahoo / Polymarket -- the graph's prior '~70%' read now looks like the top of the range). "
  "THE STRUCTURAL EDGE FOR THE INVESTOR: the crisis now transmits into US assets through the CPI/Fed channel (slow, sticky) rather than the war-premium channel (fast, reversible -- dead since late May). Even a signed Iran deal does NOT buy back this drawdown on a short horizon; the December-hike repricing is the regime fact under gold's collapse, the dollar's firmness, and the equity selloff.")
d["last_updated"] = DATE; save("fed", d); CHANGED.append("fed")

# ---- sp-500 ----
d = load("sp-500")
add_signal(d,
  "CPI-SHOCK SELLOFF (operative 10 Jun close): S&P -1.62% to 7,266.99, Dow -1.87% to 49,918.78 (-953pts; industrials -3%), Nasdaq -1.98% to 25,169.50; VIX closed 22.22 (+11.8%, first >22 close of the war). yfinance shows +0.5-0.8% rebound prints -- those are overnight/11-Jun-early levels ABOVE the CPI-shock closes (data-vintage artifact, corrected). NOT a war risk-off: gold FELL, oil moved <1.5%, the overnight tape REBOUNDED with no de-escalation news. The drawdown migrated from the war-premium channel into the sticky CPI/Fed channel.",
  ["TheStreet 10 Jun", "TechTimes", "Yahoo Finance", "Investing.com (VIX)"],
  "CONFIRMED (web-verified closes; yfinance artifact corrected)")
set_current(d, {
  "price": "S&P 7,266.99 (-1.62%, 10 Jun operative close); Dow 49,918.78 (-1.87%, -953pts); Nasdaq 25,169.50 (-1.98%); VIX 22.22 (+11.8%, first >22 close of the war, eased to 21.37 latest). yfinance 'prices' (+0.5-0.8%) are overnight/11-Jun rebound prints ABOVE the CPI-shock closes.",
  "delta_1d": "-1.62% (S&P, 10 Jun close) on the May CPI 4.2% shock + 'US signals more strikes' -- a discount-rate selloff, NOT a war risk-off",
  "driver": "MAY CPI 4.2% (3-yr high) cratered Fed-cut hopes -> December-hike repricing -> discount-rate compression across duration assets -> broad selloff, industrials -3%. Secondary: the 'more strikes in Iran' headline + the live AI/chip correction (IDC -13% 2026 smartphones). The cross-check confirms it was NOT a war risk-off: gold fell, oil rose <1.5%, the overnight tape rebounded +0.5-0.8% with no de-escalation news.",
  "data_flag": "Mixed-vintage yfinance run (^GSPC/^IXIC/^DJI): the POSITIVE 1D deltas are overnight rebound prints vs the 10 Jun CPI-shock closes. Operative move is the 10 Jun DOWN close, web-confirmed."})
d["last_updated"] = DATE; save("sp-500", d); CHANGED.append("sp-500")

# ---- vix ----
d = load("vix")
add_signal(d,
  "VIX CLOSED 22.22 (10 Jun, +11.8%) -- the FIRST close above the >22 trigger of the entire kinetic war -- but on the CPI 4.2% print PLUS strike escalation COMBINED, not kinetics alone, and it EASED to 21.37 on the latest print. One close above 22 then back below != the 'sustained 2 sessions' threshold. The convexity remains the cheapest in the dataset: an uncalibrated act (confirmed US deaths, operational Hormuz closure, a Tehran-scale strike) is NOT in this print.",
  ["Investing.com (22.22 close)", "TheStreet", "markets.md"],
  "CONFIRMED (close); trigger discipline applied")
set_current(d, {
  "price": "22.22 close (10 Jun, +11.8%) -> eased to 21.37 (latest print)",
  "delta_1d": "+11.8% to a 22.22 close -- first >22 close of the war, on CPI 4.2% + strike escalation COMBINED; eased back to 21.37",
  "read": "VIX briefly CLOSED above the >22 trigger (22.22, 10 Jun) for the first time -- but on the inflation print plus escalation TOGETHER, not on kinetics alone, and it eased to 21.37 the next print. This is a near-miss on 'VIX >22 sustained 2 sessions,' NOT a fire. The market still absorbed state-on-state missile exchanges, a downed US aircraft, US strikes on Iran, and Iranian strikes on three US-allied capitals with vol in a low-20s handle. The convexity stays the cheapest in the dataset; an UNCALIBRATED act would gap VIX to the mid-20s. The >25 kinetic marker stays uncrossed."})
trigger_note(d, ["vix", ">22"], "note_2026-06-11",
  "STAYS WATCHING. VIX CLOSED 22.22 on 10 Jun (first >22 close of the war) but eased to 21.37 the next print -- one close above the line then back below is NOT 'sustained 2 sessions,' and the close arrived on CPI+escalation combined, not kinetics alone. markets.md explicitly warns against firing on the straddle. Closest this trigger has come; does NOT fire.")
trigger_note(d, ["vix", ">25"], "note_2026-06-11",
  "STAYS WATCHING. Not crossed (peak ~22.22 close).")
d["last_updated"] = DATE; save("vix", d); CHANGED.append("vix")

# ---- gold ----
d = load("gold")
add_signal(d,
  "GOLD FELL TO ~$4,109.50 (~-1.4%) THROUGH A 4.2%-CPI + US-IRAN STRIKE DAY -- a fresh ~23-March low, now -12.1% 1M, ~$490 below the $4,600 regime trigger and moving AWAY. TERMINAL CONFIRMATION of the inflation/real-yields regime: the CPI print FEEDS the December-hike repricing -> real yields + DXY 100.26 up -> zero-yield gold repriced down. Copper +0.6% the same day (control variable) = precious/positioning unwind, not a growth collapse. Regime flips ONLY on a mutation from inflation-risk to FINANCIAL-SYSTEM risk.",
  ["yfinance", "markets.md C5", "TradingEconomics"],
  "CONFIRMED (price)")
set_current(d, {
  "price": "$4,109.50 (10 Jun; ~-1.4% 1D) -- fresh ~23-March low; Copper $6.30/lb (+0.6%, the control variable); DXY 100.26 (+0.3%, back above 100, the metals-killer).",
  "delta_1d": "~-1.4% -- FELL through a May CPI 4.2% (3-yr high) print AND renewed US-Iran strikes; the war-risk bid is dead and the inflation-regime call is confirmed, not contradicted.",
  "delta_1m": "-12.1% MoM (the cycle underperformer).",
  "watching_threshold": "Gold sustains above $4,600 for 3+ sessions = regime-shift confirmed -- now ~$490 BELOW threshold at $4,109.50 and moving AWAY (wrong direction) through the war's maximum kinetic escalation AND a 3-yr-high CPI. The 'sub-$4,400 sustained' watch is well tripped but rates/inflation-driven, not a crisis-regime change. No regime change."})
trigger_note(d, ["$4,600"], "note_2026-06-11",
  "STAYS WATCHING. Gold $4,109.50 -- ~$490 below the $4,600 regime trigger and moving AWAY through a 4.2% CPI + US-Iran strike day. The non-bid is terminal confirmation of the inflation/real-yields regime; only a mutation to financial-system risk re-bids gold.")
d["last_updated"] = DATE; save("gold", d); CHANGED.append("gold")

# ---- us-10y-yield ----
d = load("us-10y-yield")
add_signal(d,
  "10Y ~4.53% -- BARELY MOVED on the 4.2% CPI print: the bond market had PRE-PRICED the inflation/hike path; equities had not (hence the -1.6% S&P vs a pinned 10Y). DXY 100.26 (+0.3%, back above 100). India 10Y G-Sec fell to ~6.90% (4-week low) on the G-sec FII tax-exemption ordinance -- a clean policy win on the DEBT channel despite oil up and the US CPI shock abroad.",
  ["markets.md", "TradingEconomics", "CME FedWatch"],
  "CONFIRMED")
set_current(d, {
  "price": "4.53% (10Y -- pinned by the Dec-hike repricing; barely moved on CPI, bond market pre-priced); 3.63% (2Y); DXY 100.26 (firm, back above 100). India 10Y G-Sec ~6.90% (4-week low, on the G-sec FII tax exemption).",
  "delta_1d": "~flat (10Y) -- the bond market had pre-priced the CPI; the equity selloff did the repricing the 10Y already carried",
  "driver": "The December Fed-HIKE repricing is the engine under the whole window. May CPI 4.2% confirmed it but barely moved the 10Y (4.53%) -- the curve had front-run the inflation path; equities had not, hence the -1.6% S&P on a pinned yield. Firm DXY (100.26) crushed the metals complex and is why gold could not bid the strike exchange. India 10Y diverges LOWER (~6.90%) on the domestic G-sec tax-exemption policy offset. Does NOT reverse on a Hormuz deal."})
d["last_updated"] = DATE; save("us-10y-yield", d); CHANGED.append("us-10y-yield")

# ---- brent-crude ----
d = load("brent-crude")
add_signal(d,
  "BRENT ~$93.78 (+0.7%) / WTI ~$91.21 (+1.3%) -- a sub-1.5% move on renewed US strikes on Iran AND Iran's formal 'complete closure' declaration AND a US strike on a South Pars petrochemical plant. THE NON-BID, AGAIN: the marginal barrel was already priced for a near-shut strait, so the formal closure mostly converts an operational reality into a declared one. TTF EUR50.26 (+0.5%). $100-sustained trigger stays resolved; sub-$85 watch uncrossed (low ~$91). The un-priced tail is enforcement-at-scale or a Kharg move.",
  ["TradingEconomics", "markets.md C2", "MS NOW"],
  "CONFIRMED (market data)")
set_current(d, {
  "price": "Brent ~$93.78 (10 Jun, +0.7%); WTI ~$91.21 (+1.3%); DXY 100.26 (firm). European TTF ~EUR50.26/MWh (+0.5%, 3-wk high, +7.65% 1M).",
  "delta_1d": "+0.7% (Brent) -- UNDER a 1.5% 'war bid' through renewed US strikes + Iran's FORMAL complete-closure declaration + a US strike on a South Pars petrochem plant. The non-bid IS the signal: no war premium left to re-price on calibrated escalation.",
  "regime": "NO war premium left to unwind. Brent trades the FED PATH (December hike repriced live on the May CPI 4.2% print) + China demand softness, genuinely two-sided ~$93-94. The convexity is in the tail: an UNCALIBRATED event (operationally-confirmed Hormuz enforcement, confirmed US personnel deaths, a Kharg ground move) hits a market positioned for choreography and gaps Brent toward $110+.",
  "trigger_status": "'Brent breaks $100 sustained 3+ sessions' STAYS RESOLVED -- no clean >=$100 close (peak ~$94). 'Brent drops below $85 sustained' STAYS watching -- not crossed (low ~$91). NEITHER moves."})
d["last_updated"] = DATE; save("brent-crude", d); CHANGED.append("brent-crude")

# ---- aluminum ----
d = load("aluminum")
add_signal(d,
  "TWO-SIDED PRINT, THESIS INTACT. 10 Jun LME 3-month fell -2.9% to ~$3,480.5 ($3,585->$3,480.5, AlCircle) on an oil->inflation->tighter-policy->industrial-demand-fear day -- NOT the -6.6% yfinance artifact (3rd aluminum data artifact of the cycle). Then 11 Jun it recovered toward ~$3,600 (TradingEconomics) as Iran formalized 'complete closure' -- the de-pricing thesis being contested by exactly the mechanism predicted: the underlying Gulf shortage is REAL, so closure-formalization re-prices aluminum UP where gold won't move. WoodMac (Charvi Trivedi): the Middle East could lose up to 3.5M tonnes of 2026 output; EGA flagship smelter ~1-yr restart, ALBA partially suspended.",
  ["AlCircle", "TradingEconomics", "Wood Mackenzie (via Discovery Alert)", "markets.md C7"],
  "CONFIRMED (price, +/-2pt contract caveat); REPORTED (3.5Mt projection)")
set_current(d, {
  "price": "~$3,480-3,600/mt -- 10 Jun LME 3-mo -2.9% to ~$3,480.5 (AlCircle); 11 Jun recovering toward ~$3,600 (TradingEconomics) on the Hormuz closure formalization. Contract/timestamp spread; direction = partial reversal of the -9.4% war-premium unwind.",
  "delta_1d": "-2.9% (10 Jun LME 3-mo close; the -6.6% yfinance print is the 3rd aluminum data artifact of the cycle -- do NOT encode) then recovering 11 Jun on the closure declaration",
  "driver": "MOST REVERSIBLE MOVE ON THE BOARD, being tested exactly as flagged. The 10 Jun -2.9% was a demand-fear day inside a supply-constrained market (oil->inflation->policy->industrial-demand worry, ~60% crisis-derived macro). The 11 Jun recovery toward ~$3,600 on Iran's complete-closure declaration is the predicted mechanism: because the premium is REAL (genuine removed Gulf capacity -- EGA ~1-yr restart, ALBA partially suspended, WoodMac up to 3.5Mt 2026 loss), closure-formalization re-prices it UP where gold (no real premium) cannot bid. Copper resilient confirms premium dynamics, not demand collapse.",
  "data_confidence": "+/-2pt on the precise figure (thin yfinance ALI=F vs AlCircle LME vs TradingEconomics). Direction (partial reversal) and driver (real Gulf-supply floor meeting closure formalization) corroborated."})
trigger_note(d, ["alba"], "note_2026-06-11",
  "STAYS WATCHING. No new smelter strike or non-restart event; but the closure formalization re-priced aluminum toward ~$3,600, validating the 'real premium' thesis. A confirmed re-hit or ALBA/EGA non-restart re-prices violently up.")
d["last_updated"] = DATE; save("aluminum", d); CHANGED.append("aluminum")

# ---- nifty-50 ----
d = load("nifty-50")
add_signal(d,
  "Nifty closed 23,161.60 (-0.23%, 11 Jun), Sensex 73,832.55 (-0.20%) -- a shallow drift, NOT a break, through the US-Iran exchange + Hormuz closure declaration; IT the main drag (Infosys -2.25%) on US-recession/CPI worry, mid/small-caps harder (-0.83%/-0.72%). The watch items moved the WRONG way at the margin: FIIs sold Rs2,125cr Wednesday (net-positive-3-sessions deployment leg unmet, not close) and the rupee weakened to ~95.79, eroding the Rs96 cushion. New non-market channel: domestic political pressure over the Settebello seafarer deaths.",
  ["Business Standard 11 Jun", "HDFC Sky"],
  "CONFIRMED (market data)")
set_current(d, {
  "price": "Nifty 23,161.60 (-0.23%, 11 Jun close); Sensex 73,832.55 (-0.20%); mid-caps -0.83%, small-caps -0.72%; Infosys -2.25% (IT the drag).",
  "delta_1d": "-0.23% -- a shallow drift through the second US-Iran strike exchange + Iran's formal Hormuz closure declaration; the 23,000 floor held",
  "driver": "RESILIENCE THINNED BUT HELD. The market drifted -0.23% through maximum kinetic escalation, with IT (US-recession/CPI exposure) the drag and FMCG/domestic names resilient. But the deployment math worsened at the margin: FIIs sold Rs2,125cr Wednesday and the rupee re-approached Rs96, un-ticking the one box yesterday counted.",
  "note": "Deployment scorecard: Brent <$95 [met barely, $93.78], FII net-positive 3+ sessions [NOT met], organic Rs93-94 [NOT met, 95.79]. ONE of three met -- no deployment signal. The crisis is still arriving in India as global risk-off, not as rotation INTO India (Kotak 'dragged-in' read still winning)."})
d["last_updated"] = DATE; save("nifty-50", d); CHANGED.append("nifty-50")

# ---- inr-usd ----
d = load("inr-usd")
add_signal(d,
  "USD/INR ~95.79 (from 95.25) -- re-approaching the Rs96 line, ERODING the cushion that yesterday's brief counted as the one ticked deployment box. Driven by DXY >100 (post-CPI) + the $94 oil import bill + FII equity selling (May a record Rs55,963cr outflow). The Rs96 RBI-direct-intervention trigger STAYS WATCHING (pressed, not breached). India 10Y diverged LOWER to ~6.90% on the G-sec tax exemption -- the package working on the DEBT channel it targets, not the equity-flow channel it can't.",
  ["Business Standard 11 Jun", "markets.md C6"],
  "CONFIRMED")
set_current(d, {
  "price": "USD/INR ~95.79 (11 Jun, weaker from 95.25) -- re-approaching Rs96; Rs94.50 decisively broken; Rs96 pressed but NOT breached onshore.",
  "delta_1d": "weaker to ~95.79 -- the rupee gave back the early-week firmness as DXY pushed back above 100 post-CPI and FIIs kept selling equities",
  "driver": "US CPI 4.2% -> DXY >100 -> EM-FX pressure + $94 oil import bill + FII equity selling (May was a RECORD Rs55,963cr outflow, absorbed by DIIs) -> rupee back toward Rs96. The RBI June 5 package is being stress-tested. CONTRAST: India 10Y eased to ~6.90% (4-wk low) on the FII G-sec tax exemption -- the policy works on the debt channel, not the equity-flow channel.",
  "trigger_status": "Rs96 RBI-direct-intervention trigger STAYS WATCHING -- pressed (95.79) but NOT breached. [Correction applied: intel A9's 'Rs96 trigger ACTIVE_FIRED' is not the graph state -- 95.79 is below 96; trigger remains watching.] Rs94.50 trigger resolved (rupee structurally weaker). Rs93-94 organic retracement still needs Brent <$95 + an FII turn (unmet) + a signed deal."})
trigger_note(d, ["96"], "note_2026-06-11",
  "STAYS WATCHING. Rupee 95.79 (11 Jun) -- pressed toward Rs96 again but NOT breached onshore. Correction: intel A9 characterized this trigger as 'ACTIVE_FIRED'; the operative rupee (95.79 < 96) keeps it WATCHING. RBI June 5 package being stress-tested.")
d["last_updated"] = DATE; save("inr-usd", d); CHANGED.append("inr-usd")

# ---- fii-flows ----
d = load("fii-flows")
add_signal(d,
  "FIIs sold ~Rs2,124.98cr Wednesday (10 Jun) -- the net-positive-for-3-sessions deployment condition remains UNMET and not close. May was a RECORD Rs55,963cr FII outflow month, absorbed by DIIs. Leg one of the capital-substitution thesis (North-Asia AI correction >10% -- KOSPI circuit-breaker week, VKOSPI record) is now unambiguously met, but leg two (India FII net-positive) is not: the global AI-trade unwind is hitting India as risk-off, not rotating INTO it.",
  ["Business Standard 11 Jun", "Republic World (May outflow)", "markets.md C4/C6"],
  "CONFIRMED")
d["last_updated"] = DATE; save("fii-flows", d); CHANGED.append("fii-flows")

# ============================ MARKET / NORTH ASIA ============================

# ---- kospi ----
d = load("kospi")
add_signal(d,
  "KOSPI -4.5% (Samsung -6.1%, SK Hynix -7.5%), TAIEX -3.3%, Nikkei -1.9% -- a circuit-breaker week with VKOSPI at a RECORD high. Two braided drivers: ~60% the post-Broadcom AI/memory valuation unwind (leg 3; IDC's record -13% 2026 smartphone forecast hits memory directly) + ~40% crisis-derived (US CPI 4.2% -> Fed-hike repricing -> duration-tech compression + USD/KRW W1,530 leveraged-Korea unwind). Leg one of the India capital-substitution trigger (North-Asia AI correction >10% from peak) is now UNAMBIGUOUSLY met.",
  ["markets.md C4", "IDC", "Tom's Hardware/Fortune (helium)"],
  "CONFIRMED (price); REPORTED (IDC forecast)")
set_current(d, {
  "price": "KOSPI ~ -4.5% (Samsung -6.1%, SK Hynix -7.5%); VKOSPI at a RECORD high; TAIEX -3.3%; Nikkei -1.9%; USD/KRW ~W1,530 (+2.5% 1M).",
  "delta_1d": "-4.5% -- a circuit-breaker week; ~60% AI/memory valuation unwind (IDC -13% smartphones), ~40% crisis-derived (CPI->Fed-hike + USD/KRW)",
  "driver": "TWO BRAIDED DRIVERS. (1) NON-CRISIS ~60%: post-Broadcom AI/memory unwind leg 3 -- IDC's record -13% 2026 smartphone forecast is a demand-side negative for the memory complex; VKOSPI at a record; foreign outflows continue. (2) CRISIS-DERIVED ~40%: US CPI 4.2% -> Fed-hike repricing -> global duration-tech compression + USD/KRW W1,530 leveraged-Korea unwind; plus the structural helium overhang (Korean fabs rationing, ~6-mo inventories). Leg one of the India capital-substitution trigger (North-Asia AI correction >10%) is now unambiguously met; leg two (India FII net-positive 3 sessions) is still UNMET."})
d["last_updated"] = DATE; save("kospi", d); CHANGED.append("kospi")

# ---- samsung ----
d = load("samsung")
add_signal(d,
  "Samsung -6.1% in the KOSPI circuit-breaker week -- the memory complex hit by IDC's record -13% 2026 smartphone-volume forecast (demand-side, non-war) layered on the post-Broadcom AI unwind and the structural helium overhang (Korean fabs rationing ultra-pure helium, ~6-mo inventories). VKOSPI at a record.",
  ["markets.md C4", "IDC"],
  "CONFIRMED (price); REPORTED (IDC)")
d["last_updated"] = DATE; save("samsung", d); CHANGED.append("samsung")

# ---- sk-hynix ----
d = load("sk-hynix")
add_signal(d,
  "SK Hynix -7.5% in the KOSPI circuit-breaker week -- the HBM/memory leader leading the AI-valuation unwind (IDC -13% 2026 smartphones, demand-side) plus the helium-inventory clock (~6-mo cover, ultra-pure helium prices doubled). VKOSPI at a record.",
  ["markets.md C4", "IDC", "Tom's Hardware"],
  "CONFIRMED (price); REPORTED (IDC)")
d["last_updated"] = DATE; save("sk-hynix", d); CHANGED.append("sk-hynix")

# ---- semiconductors ----
d = load("semiconductors")
add_signal(d,
  "IDC: 2026 global smartphone volumes forecast -13% -- the LARGEST YoY decline on record. A pure demand-side negative for memory/semis (Samsung, SK Hynix, Micron), non-war, layered on the post-Broadcom AI unwind; the war (helium) is only the third factor. Counter: Micron-Bechtel broke ground on the New York fab (10 Jun) -- US memory capex proceeding, marginal positive for US-domiciled semis vs Korea.",
  ["IDC (via markets.md D)", "Micron/Bechtel"],
  "REPORTED (IDC forecast); CONFIRMED (Micron fab)")
d["last_updated"] = DATE; save("semiconductors", d); CHANGED.append("semiconductors")

# ---- defense-sector ----
d = load("defense-sector")
add_signal(d,
  "LMT +3.6%, ITA +2.6% on a -1.6% S&P day -- the first defense bid of this size since the May de-rate, the cleanest within-tape rotation signature of the window. Driver: the US signaling continued/nightly strikes -> kinetic-continuation + munitions-replenishment repricing. This is positioning (HIGH reversibility), not earnings -- fades on any de-escalation headline.",
  ["markets.md C3/E2"],
  "CONFIRMED (price)")
bump_edges(d, [("united-states", "2026-06-11: 'US signals more strikes' -> LMT +3.6% / ITA +2.6% on a down tape; kinetic-continuation + munitions-replenishment repricing. Activation, not new edge.", None)])
d["last_updated"] = DATE; save("defense-sector", d); CHANGED.append("defense-sector")

# ---- shipping-tankers ----
d = load("shipping-tankers")
add_signal(d,
  "FRO +4.5%, BOAT +1.9% on a down tape (extended-blockade duration repriced); plus the blockade enforcement turned LETHAL -- MT Settebello disabled off Oman, 3 Indian crew killed (first US-hand fatalities of the war), 9 strikes / 135 redirected / 42 humanitarian passages since 13 Apr. Physical: VLCC ~$100K/day (~2x YoY), Hormuz volumes -36%, 'no quick recovery' consensus. The equity bid is positioning (HIGH reversibility); the physical rates are structural.",
  ["markets.md C2/C3", "Lloyd's List/Fearnleys", "CBS (Settebello)"],
  "CONFIRMED")
bump_edges(d, [("united-states", "2026-06-11: US blockade enforcement turned lethal (Settebello, 3 Indian crew killed) + 'more strikes' signal -> FRO +4.5%, BOAT +1.9%; extended-blockade-duration repricing.", None)])
d["last_updated"] = DATE; save("shipping-tankers", d); CHANGED.append("shipping-tankers")

# ---- marine-war-risk-insurance ----
d = load("marine-war-risk-insurance")
add_signal(d,
  "Gulf war-risk cover holding at ~$10-14M per VLCC transit (~7-10% of hull value), ~340% above pre-Feb-28; capacity has SHRUNK ($2-3B -> $0.5-1.5B per transit, Lloyd's List/LMA). NOT unwinding through the de-escalation talk -- the clearest paper-vs-physical divergence: paper-Brent refuses to bid, physical insurance refuses to normalize. Iran's formal complete-closure declaration adds latent re-rating risk if enforcement is operationally confirmed.",
  ["Lloyd's List", "LMA", "markets.md F"],
  "REPORTED (market structure)")
d["last_updated"] = DATE; save("marine-war-risk-insurance", d); CHANGED.append("marine-war-risk-insurance")

# ---- cf-industries ----
d = load("cf-industries")
add_signal(d,
  "CF +2.0% (Nutrien +2.2%) -- equity crisis-rotation flow on Gulf fertilizer supply-risk repricing, NOT a physical-price signal: physical urea fell -1.1% to $397.50/t (-27.4% 1M) the same day. Paper-physical divergence, same caution as tankers in May -- do NOT read the equity move as physical disruption.",
  ["markets.md C3/E3", "TradingEconomics (urea)"],
  "CONFIRMED (price)")
d["last_updated"] = DATE; save("cf-industries", d); CHANGED.append("cf-industries")

# ---- fertilizer-urea ----
d = load("fertilizer-urea")
add_signal(d,
  "Physical urea -1.1% to $397.50/t (-27.4% 1M); FOB Middle East ~$500 vs $512.50 prior. Physical DE-PRICING continues even as CF/NTR equity rallied +2% on crisis-rotation -- the physical-disruption edge should NOT be strengthened on the equity move. The Hormuz exposure (~40-49% of urea exports transit) is latent, not yet in the physical price.",
  ["TradingEconomics", "markets.md E3"],
  "CONFIRMED (price)")
d["last_updated"] = DATE; save("fertilizer-urea", d); CHANGED.append("fertilizer-urea")

# ---- european-ttf-gas ----
d = load("european-ttf-gas")
add_signal(d,
  "TTF EUR50.26/MWh (+0.53%, a 3-week high; +7.65% 1M) -- rose just half a percent through Iran's FORMAL complete-closure declaration of the strait that carries a fifth of global LNG. Europe's framing remains winter storage-refill COMPETITION, not crisis/panic; bid on escalation threatening conflict-resolution, not on supply fear. The ~+33% YoY floor is intact. No new European emergency measures or ECB language surfaced.",
  ["TradingEconomics", "gmk.center", "markets.md F"],
  "CONFIRMED (price)")
set_current(d, {
  "price": "EUR50.26/MWh (10-11 Jun, +0.53%, 3-week high)",
  "delta_1d": "+0.53% -- a half-percent move through a formal Hormuz closure declaration; storage-refill framing, not panic",
  "delta_1m": "+7.65% MoM; ~+33% YoY floor intact"})
d["last_updated"] = DATE; save("european-ttf-gas", d); CHANGED.append("european-ttf-gas")

# ============================ LOCATION / SECONDARY ACTORS ============================

# ---- bahrain ----
d = load("bahrain")
add_signal(d,
  "Hit in Iran's SECOND wave -- ballistic missiles at the Sheikh Isa airbase; an 11-year-old girl injured and property damage in Hamad City/Manama from intercepted-drone shrapnel. Response stayed in the established pattern: absorb, intercept, condemn, mediate -- no expulsion, no downgrade. Saudi Arabia and Qatar signaled 'diplomacy still possible' after the wave.",
  ["Al Jazeera Day 104", "Bahraini official statements", "Jerusalem Post (Saudi-Qatar)"],
  "CONFIRMED")
bump_edges(d, [("iran", "2026-06-11: Second-wave ballistic missiles at Sheikh Isa airbase; 11-yr-old injured by intercepted-drone shrapnel. Absorb-intercept-condemn-mediate pattern holds.", None)])
d["last_updated"] = DATE; save("bahrain", d); CHANGED.append("bahrain")

# ---- kuwait ----
d = load("kuwait")
add_signal(d,
  "Hit in Iran's SECOND wave -- ballistic missiles at the Ali Al Salem and Ahmad Al-Jaber airbases. Kuwait temporarily CLOSED its airspace and Kuwait Airways suspended all flights -- practical, not political; no expulsion or downgrade, consistent with every prior round.",
  ["Al Jazeera Day 104", "Kuwaiti official statements"],
  "CONFIRMED")
bump_edges(d, [("iran", "2026-06-11: Second-wave ballistic missiles at Ali Al Salem & Ahmad Al-Jaber airbases; airspace closed, Kuwait Airways flights suspended.", None)])
d["last_updated"] = DATE; save("kuwait", d); CHANGED.append("kuwait")

# ---- jordan ----
d = load("jordan")
add_signal(d,
  "Hit for a SECOND consecutive day -- ballistic missiles at the Al-Azraq base; Jordan said it intercepted 20 missiles with 'no casualties or material damage.' Confined itself to interception statements -- no expulsion, no escalation. The iran->jordan edge bumped on the second confirmed strike.",
  ["Al Jazeera Day 104", "Jordanian military statement"],
  "CONFIRMED")
d["last_updated"] = DATE; save("jordan", d); CHANGED.append("jordan")

# ---- lebanon ----
d = load("lebanon")
add_signal(d,
  "Tyre death toll revised UP to 11 (from 'at least 8') for the 9 Jun Israeli strikes amid the whole-city evacuation; IDF killed a gunman who infiltrated from Lebanon and opened fire on troops; raids continued at 12+ southern locations. Cumulative Lebanese figures: 3,666 killed since March, 1m+ displaced (single-side official data, REPORTED). No new Hezbollah rocket fire found this window. Lebanon remains the theatre where Israel retains freedom of action inside the wider stand-down.",
  ["BSS/AFP", "Times of Israel", "Lebanese NNA (via AJ)"],
  "CONFIRMED (toll, IDF ops); REPORTED (cumulative figures)")
d["last_updated"] = DATE; save("lebanon", d); CHANGED.append("lebanon")

# ---- israel ----
d = load("israel")
add_signal(d,
  "THE AXIS HELD: no Israel-Iran strikes in either direction since the 8 Jun stand-down, through the entire US-Iran exchange. Trump explicitly said Israel was NOT involved in the latest US strikes. The decoupling is now openly chafing -- an Israeli official complained Washington demands Israeli restraint 'noting Trump didn't hold back' himself (ToI). Editorial tell: ToI's 11 Jun live blog LED with Haredi draft protests, not the US-Iran war -- for Israeli audiences this is now someone else's war.",
  ["Haaretz live", "Times of Israel live blog 10-11 Jun"],
  "CONFIRMED (non-action, Trump statement); REPORTED (official irritation)")
bump_edges(d, [("iran", "2026-06-11: Axis stayed quiet through maximum US-Iran kinetics -- no strikes since 8 Jun stand-down; Trump confirmed Israel not involved. Iran exploiting the Trump-Netanyahu seam (ISW).", None)])
d["last_updated"] = DATE; save("israel", d); CHANGED.append("israel")

# ---- hezbollah ----
d = load("hezbollah")
add_signal(d,
  "The Lebanon theatre grinds on inside the stand-down -- Israeli raids at 12+ southern locations, Tyre toll to 11 -- but NO new Hezbollah rocket fire at Israel was found this window (gap noted). Iran's stated tripwire (further Israeli strikes in Lebanon -> 'much harsher' retaliation) is being tested daily without re-fusing the axes.",
  ["Times of Israel", "Lebanese NNA (via AJ)"],
  "CONFIRMED (Israeli ops); absence-of-Hezbollah-fire noted as gap")
d["last_updated"] = DATE; save("hezbollah", d); CHANGED.append("hezbollah")

# ---- houthis ----
d = load("houthis")
add_signal(d,
  "Missile fire at Israel during the 7-8 Jun window (single missile intercepted, Tel Aviv sirens, no injuries) + a declared 'complete and total ban on Israeli maritime navigation in the Red Sea.' But STILL ZERO confirmed Houthi attacks on neutral commercial shipping on Day ~104 -- the oil-market wildcard trigger stays UNFIRED. The 'attack on Israel' trigger (already active) re-fires; the navigation ban is a DECLARATION until a vessel is actually struck.",
  ["Times of Israel", "IDF statement", "Jerusalem Post"],
  "CONFIRMED (missile at Israel, intercepted); RHETORIC/DECLARATION (navigation ban)")
trigger_note(d, ["neutral"], "note_2026-06-11",
  "STAYS UNFIRED. Day ~104, still zero confirmed Houthi attacks on neutral commercial shipping despite the declared Israeli-navigation ban. UKMTO page inaccessible (flagged). The declaration is rhetoric until a hull is struck.")
d["last_updated"] = DATE; save("houthis", d); CHANGED.append("houthis")

# ---- red-sea ----
d = load("red-sea")
add_signal(d,
  "Houthis declared a 'complete and total ban on Israeli maritime navigation,' designating 'all enemy movements' legitimate targets -- but no neutral-vessel incident was confirmed (UKMTO recent-incidents page inaccessible/403, flagged). The Red Sea neutral-shipping trigger -- the oil-market wildcard -- stays unfired on Day ~104.",
  ["Jerusalem Post", "UKMTO (inaccessible)"],
  "DECLARATION; no operational incident confirmed")
d["last_updated"] = DATE; save("red-sea", d); CHANGED.append("red-sea")

# ---- pakistan ----
d = load("pakistan")
add_signal(d,
  "The 7 Jun Naqvi-to-Tehran message is now sourced to BOTH PM Shehbaz Sharif AND Field Marshal Asim Munir jointly -- the military co-signature signals the army's direct stake in the mediation. Contents undisclosed; no Iranian readout published. GlobalSecurity's 'most consequential variable for the next 48 hours' call was overtaken by the US-Iran strike exchange, with no visible channel output.",
  ["Geo TV", "Pakistan Today", "Arab News", "CGTN"],
  "REPORTED")
d["last_updated"] = DATE; save("pakistan", d); CHANGED.append("pakistan")

# ---- mojtaba-khamenei ----
d = load("mojtaba-khamenei")
add_signal(d,
  "Received the written Pakistani message (from Sharif + Field Marshal Munir) delivered by Interior Minister Naqvi during his Tehran visit -- the channel operates at Supreme-Leader level. No published Iranian response; the silence is itself noted. The channel has not visibly arrested the escalation.",
  ["Geo TV", "Arab News"],
  "REPORTED")
d["last_updated"] = DATE; save("mojtaba-khamenei", d); CHANGED.append("mojtaba-khamenei")

# ---- oman ----
d = load("oman")
add_signal(d,
  "The Omani navy is physically RESCUING crews from US-struck tankers in its waters (Settebello survivors; a Guinea-Bissau-flagged tanker hit by 2 Hellfires, 20 crew evacuated). The quiet mediator is now in direct OPERATIONAL contact with the blockade's consequences off its coast -- a node to watch as the enforcement campaign turns lethal near Omani waters.",
  ["Al Jazeera Day 104", "ONA", "CBS"],
  "CONFIRMED")
d["last_updated"] = DATE; save("oman", d); CHANGED.append("oman")

# ---- qatar ----
d = load("qatar")
add_signal(d,
  "Qatar (with Saudi Arabia) signaled 'diplomacy still possible' via a foreign-minister call after Iran's second strike wave on Gulf soil -- the load-bearing Gulf de-escalation signal. Fertilizer/helium supply-risk context persists (Ras Laffan). The revealed Gulf preference remains absorb-intercept-condemn-mediate.",
  ["Jerusalem Post", "markets.md C3"],
  "REPORTED")
d["last_updated"] = DATE; save("qatar", d); CHANGED.append("qatar")

# ---- china ----
d = load("china")
add_signal(d,
  "Iran's formal 'complete closure' declaration (no nationality exceptions) ends the Iran-PERMITTED Chinese transits as policy -- the coordinated-passage instrument the graph tracked. Operationally unconfirmed (CENTCOM says transits continue). China is also the ~40% non-crisis leg of the aluminum demand-fear move (industrial softness) and the marginal-demand swing for Brent.",
  ["Haaretz live", "markets.md C2/C7"],
  "CONFIRMED (declaration); CONTESTED (operational effect on Chinese transits)")
d["last_updated"] = DATE; save("china", d); CHANGED.append("china")

# ---- saudi-arabia ----
d = load("saudi-arabia")
add_signal(d,
  "Saudi Tadawul +0.3% -- the Gulf's own market STILL not pricing the escalation, a consistent regional-calibration data point. Saudi Arabia (with Qatar) signaled 'diplomacy still possible' after Iran's second strike wave. The Gulf revealed preference: absorb, intercept, condemn, mediate.",
  ["markets.md C8", "Jerusalem Post"],
  "CONFIRMED (market); REPORTED (diplomacy signal)")
d["last_updated"] = DATE; save("saudi-arabia", d); CHANGED.append("saudi-arabia")

# ---- natural-gas-lng ----
d = load("natural-gas-lng")
add_signal(d,
  "Henry Hub -3.0% on US weather/storage -- ~zero crisis content (do NOT encode as crisis). The crisis-linked gas gauge is European TTF (EUR50.26, +0.5%, +7.65% 1M), NOT Henry Hub. Iran's formal Hormuz closure (the strait carries ~a fifth of global LNG) drew only a half-percent TTF move -- storage-refill framing, not panic.",
  ["markets.md C8/F", "TradingEconomics"],
  "CONFIRMED (price)")
d["last_updated"] = DATE; save("natural-gas-lng", d); CHANGED.append("natural-gas-lng")

# ---- rbi ----
d = load("rbi")
add_signal(d,
  "The June 5 stabilization package is being stress-tested as the rupee re-approaches Rs96 (95.79). It is WORKING on the channel it targets -- the G-sec FII tax-exemption ordinance eased India 10Y to ~6.90% (4-week low) despite oil up and the US CPI shock -- and NOT working on the one it can't (equity-flow appeal: FIIs still selling, May a record outflow). A clean debt-channel win; the FX/equity legs remain pressured.",
  ["markets.md C6", "Business Standard"],
  "CONFIRMED")
d["last_updated"] = DATE; save("rbi", d); CHANGED.append("rbi")

# ---- indian-it ----
d = load("indian-it")
add_signal(d,
  "Indian IT the main Nifty drag on 11 Jun (Infosys -2.25%) on US-recession/CPI worry -- the sector most exposed to the US macro deterioration (CPI 4.2%, December-hike repricing, recession framing) rather than to the Gulf kinetics. The transmission to India is via the US demand/rates channel, not the war.",
  ["Business Standard 11 Jun"],
  "CONFIRMED (price)")
d["last_updated"] = DATE; save("indian-it", d); CHANGED.append("indian-it")

print("NODES UPDATED:", len(CHANGED))
print(", ".join(CHANGED))
