#!/usr/bin/env python3
"""Idempotent patch: add a 2026-05-30 recent_signals entry to market nodes that
got summary/current updates but no structured signal. Safe to re-run (skips if a
2026-05-30 signal already exists)."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NODE_DIR = os.path.join(ROOT, "graph", "nodes")
TODAY = "2026-05-30"

def s(h, src, ver):
    return {"date": TODAY, "headline": h, "sources": src, "verification": ver}

SIGS = {
 "brent-crude": s(
   "**PEACE-DIVIDEND DE-PRICING CONFIRMED — BRENT $92.05, -22% MoM, BIGGEST MONTHLY LOSS SINCE 2020; SUB-$100 TRIGGER RESOLVES.** "
   "Brent closed $92.05 (Fri 29 May; -1.8% 1D, -22.0% MoM, still +26% vs the ~$73 Feb-28 baseline); WTI $87.36. The unsigned 60-day "
   "MOU + Hormuz-reopen hopes dumped the ~$7-8 tail premium; the ~$30 structural premium is intact. Desks (CNBC) see $90-100 'for a "
   "couple of months.' The 'breaks $100 sustained 3+ sessions' trigger resolves on clean multi-session sub-$100 closes — Goldman "
   "$120 Q3 foreclosed, JPM $60 re-enters. Tail-risk de-pricing, NOT structural (Hormuz still contested: new Oman mine, Lian Star). "
   "Asymmetry violent from a low base — a deal collapse / non-calibrated Iranian strike / Lebanon break gaps Brent +$8-15.",
   ["CNBC 29 May (biggest monthly loss since 2020); TradingEconomics; Fortune 29 May",
    "Intel 2026-05-30 A7, D1, A1, A8; Market C1"],
   "Brent $92.05 / -22% MoM = CONFIRMED (data); $90-100 band = analyst (REPORTED); trigger resolution = data-driven; physical floor "
   "(Oman mine, Lian Star) = CONFIRMED/REPORTED-to-CONFIRMED."),
 "gold": s(
   "**REVERSAL — GOLD DID NOT STAY BELOW $4,400; THE 'HEDGE IS DEAD' CALL DID NOT SUSTAIN.** The 28 May break below $4,400 "
   "(two-month low ~$4,380) reversed within a session: +2.56% to $4,524 on 29 May (Fortune), ~$4,560 (CNBC; +1.4% 1D), ~flat MoM, "
   "+36% YoY. Driver: softer April monthly PCE (+0.4% vs +0.5% exp) dialed back rate-HIKE bets + a softer dollar; gold ROSE on "
   "de-escalation headlines (dollar-weakness/inflation-hedge bid reasserted). The 'sub-$4,400 sustained 5+ sessions' watch is "
   "UNTRIPPED/RESET (one-session dip). Regime read HOLDS (real yields/Fed, not crisis); $4,600 still below threshold.",
   ["Fortune 29 May ($4,524, +$113/+2.56%); CNBC/TradingEconomics ($4,539-4,580)",
    "Intel 2026-05-30 A6; Market C4"],
   "Gold +1.4% to +2.56% 1D, ~flat MoM, +36% YoY = CONFIRMED (cross-checked Fortune/CNBC/TE); sub-$4,400 watch UNTRIPPED/RESET = "
   "CONFIRMED (one-session reversal). Do NOT encode the one-day low as a regime change."),
 "nifty-50": s(
   "**INDIA FELL ON A CRISIS-RELIEF DAY — THE CLEANEST NON-CONFIRMATION OF THE CYCLE; DRIVER MECHANICAL, NOT THE WAR.** Nifty "
   "23,547.75 (-1.5%), 3rd straight down session, worst May in six years (-2.8% cal. month); Sensex -1.4%. On a day of Brent -22% "
   "MoM, rupee firming to ~Rs95, 10Y easing to 7.00% and a ceasefire MOU progressing, the relief leg should have lifted Nifty +1-2% "
   "— instead it fell. Driver ~0% crisis: MSCI rebalance ($800m-$1bn passive outflow) + F&O expiry + FII rotation to the Korea/"
   "Taiwan AI-memory supercycle. Held ~23,500; a signed deal could gap toward 24,500, a deal-break opens 23,000.",
   ["TradingEconomics / wire (closes); BusinessUpturn (MSCI $800m-$1bn)",
    "Intel 2026-05-30 A5; Market C2, E1"],
   "Nifty -1.5% / worst May in 6yr = CONFIRMED (data); MSCI $800m-$1bn = REPORTED (wire); FII rotation = CONFIRMED (Goldman + flow "
   "data). Weakness empirically STRUCTURAL+MECHANICAL, not crisis."),
 "india": s(
   "**INDIA'S WEAKNESS NOW EMPIRICALLY STRUCTURAL+MECHANICAL — FELL ON CRISIS RELIEF; RBI RESERVES -$7.5bn/wk.** Nifty -1.5%, "
   "Sensex -1.4%, worst May in six years, even as every crisis variable moved India's way. Proximate cause: MSCI rebalance "
   "($800m-$1bn passive outflow) + F&O expiry + FII rotation to North-Asia AI. RBI forex reserves fell to $681.4bn (wk ending 22 "
   "May, -$7.5bn). Rough rice +19.6% MoM (export-restriction/food-security). A Hormuz deal removes a headwind India already wasn't "
   "trading on; the re-rating needs an FII turn.",
   ["TradingEconomics/wire; RBI weekly supplement ($681.4bn, -$7.5bn)",
    "Intel 2026-05-30 A5; Market C2, C5"],
   "Nifty/Sensex closes + worst May in 6yr = CONFIRMED; RBI reserves -$7.5bn = CONFIRMED (official); MSCI = REPORTED. Crisis was a "
   "TAILWIND on 29 May and India still fell."),
 "inr-usd": s(
   "**RUPEE FIRMED TO ~Rs95.0 — FIRST OIL-RELIEF+DEAL FIRMING TO HOLD INTO THE WEEKEND, BUT PART-INTERVENTION.** USD/INR ~Rs94.99 "
   "(-1.1% 1D, firmer), off the Rs96.96 record (20 May), on Brent sub-$100 + the MOU + a softer dollar (DXY 98.91). But RBI "
   "reserves fell to $681.4bn (-$7.5bn/wk); the $5bn swap drew ~$9.8bn bids (appetite, not stress); FII outflows continue. Rs93-94 "
   "organic path opens only on a SIGNED deal + Brent <$95 + an FII turn; a deal-break + Brent >$110 reopens Rs97-98.",
   ["HDFCSky 29 May (Rs95.05, +53 paise); RBI weekly supplement; TradingEconomics DXY",
    "Intel 2026-05-30 A5; Market C5"],
   "USD/INR Rs94.99 / -1.1% = CONFIRMED; reserves -$7.5bn = CONFIRMED (official); firming part-intervention = assessment. FII turn "
   "is the missing piece."),
 "rbi": s(
   "**INTERVENTION COST MOUNTING — FOREX RESERVES -$7.5bn IN A WEEK TO $681.4bn (~$37bn OFF PEAK).** The week-ending-22-May "
   "drawdown is the price of defending the rupee through the Rs96.96 record episode and into the ~Rs95 firming; the $5bn buy-sell "
   "swap drew ~$9.8bn bids (healthy appetite, not stress). India 10Y eased to ~7.00% on the ceasefire + lower Brent. No new "
   "macroprudential directive this window — the absence of fresh escalation is mildly reassuring; the reserves drawdown is the "
   "binding constraint.",
   ["RBI weekly statistical supplement ($681.4bn, -$7.5bn); Whalesbook; TradingEconomics India 10Y",
    "Intel 2026-05-30 A5; Market C5, D6"],
   "Reserves $681.4bn / -$7.5bn = CONFIRMED (official); $5bn swap ~$9.8bn bids = CONFIRMED; India 10Y ~7.00% = CONFIRMED (web). No "
   "new directive = non-event."),
 "fii-flows": s(
   "**FII/PASSIVE FLOWS THE TRANSMISSION MECHANISM IN EVERY INDIA CHAIN — NEW MECHANICAL LEG (MSCI REBALANCE).** The 29 May Nifty "
   "-1.5% drop on a relief day was driven by the MSCI rebalance ($800m-$1bn one-time passive outflow; Hyundai India -$281m, "
   "Jubilant -$161m steepest) + discretionary selling + structural rotation out of expensive India (~24x P/E) into the Korea/"
   "Taiwan AI supercycle (India -9% YTD vs Korea +90% / Taiwan +42%; Goldman India marketweight / Korea highest-conviction +300% "
   "EPS). War-period cumulative outflows >$22bn; FY26 net FPI ~-$16.7bn. This is why the relief leg fails.",
   ["BusinessUpturn (MSCI $800m-$1bn); Goldman (paired call); wire",
    "Intel 2026-05-30 A5; Market C2, C3, E1"],
   "MSCI $800m-$1bn = REPORTED (wire); rotation + Goldman paired call = CONFIRMED (research + flow data); cumulative outflows = "
   "CONFIRMED. The dominant explanation for India underperformance."),
 "semiconductors": s(
   "**AI-MEMORY SUPERCYCLE FULLY DECOUPLED — SK HYNIX JOINS THE $1T CLUB; SMH +47% 3M; KOSPI/TAIEX RECORDS.** KOSPI +3.6% to a "
   "record (+46% 3M), Taiwan +2.5% (+27.5% 3M), SMH +19.9% MoM / +47.4% 3M. SK Hynix +~11% to a $1T valuation on HBM/AI-memory "
   "demand; Goldman calls Korea 'highest-conviction' (+300% 2026 EPS). Concentration extreme: 82% of Korean stocks fell MoM, "
   "Samsung+SK Hynix = ~50% of KOSPI; the won is weakening (Won1,507, +4.8% 3M) even as KOSPI rips. ~0% crisis — the destination of "
   "capital leaving India (new nifty<->semis capital-substitution edge).",
   ["The Star / Seoul Economic Daily (KOSPI record, SK Hynix $1T, 82% fell); Goldman; SMH yfinance",
    "Intel 2026-05-30 A5; Market C3, E1"],
   "KOSPI/SMH/Taiwan deltas + SK Hynix $1T = CONFIRMED (data); 82%-fell concentration = CONFIRMED (Seoul Economic Daily); ~0% "
   "crisis = assessment. No crack in the thesis visible."),
 "kospi": s(
   "**RECORD ON SK HYNIX'S $1T MILESTONE — BUT THE INDEX IS TWO STOCKS.** KOSPI +3.6% to a record 8,476 (+28% MoM, +46% 3M); SK "
   "Hynix +~11% to join the $1T club, intraday +5% triggering a sidecar halt; Goldman target 9,000, Korea 'highest-conviction.' "
   "82% of Korean stocks fell over the past month; Samsung+SK Hynix = ~50% of the index (narrowest breadth). Won weakening "
   "(Won1,507, +4.8% 3M) even as KOSPI rips. The destination of capital leaving India; reversible only on an AI/memory crack.",
   ["The Star / Seoul Economic Daily; Goldman", "Market C3"],
   "KOSPI +3.6% record / SK Hynix $1T = CONFIRMED; 82%-fell + 2-stock concentration = CONFIRMED (Seoul Economic Daily)."),
 "taiwan": s(
   "**TAIEX +2.5% TO 44,733 (+27.5% 3M) — THE AI/SEMIS BID, TECH >80% OF THE INDEX.** Taiwan tracked the AI-memory supercycle "
   "lifting KOSPI to a record; Goldman sees Taiwan +45% EPS. A structural AI-capex trade (~0% crisis) and a destination of EM "
   "capital leaving expensive India; reversibility idiosyncratic to AI/semis pricing, not the Iran ceasefire.",
   ["TradingEconomics TAIEX; Goldman", "Market C2, C3"],
   "TAIEX +2.5% / +27.5% 3M = CONFIRMED (data); ~0% crisis = assessment."),
 "us-10y-yield": s(
   "**10Y AT 4.45%, CAPPED BY A SOFTER MONTHLY PCE — FED CUTS PRICED OUT.** The 10Y held 4.45% (+0.8% MoM), 2Y 3.59%. April PCE "
   "(28 May) printed headline 3.8% YoY (3-yr high) but monthly +0.4% vs +0.5% expected — a softer read that capped yields and "
   "dialed back the rate-HIKE bets pressuring gold. Cuts remain fully priced out (PPI/Warsh inflation regime, structural through "
   "Q3); does not reverse on a Hormuz deal.",
   ["TradingEconomics US 10Y/2Y; TheStreet (PCE 28 May)", "Market D1, C4"],
   "10Y 4.45% / 2Y 3.59% = CONFIRMED (data); April PCE 3.8% YoY / +0.4% monthly = CONFIRMED; cuts priced out = market-implied."),
 "vix": s(
   "**VIX SANK TO A 15.3 CYCLE LOW — PRICING THE CEASEFIRE AS DONE ON AN UNSIGNED DEAL + A LEBANON RED-LINE CROSSING.** VIX 15.32 "
   "(-2.7% 1D, -28.5% 3M) is the cheapest convexity in the dataset: Trump has NOT signed (Trump-vs-Fars contradiction) and Israel "
   "crossed Washington's Beirut red line. A Situation Room rejection or a Lebanon break of the talks gaps VIX to the low-20s and "
   "the S&P -3-5% in a session. Complacency split: index vol prices de-escalation while defense (ITA +10.5% MoM) bids kinetic "
   "events.",
   ["yfinance VIX; Intel 2026-05-30 A2, A3", "Market C7"],
   "VIX 15.32 / -28.5% 3M = CONFIRMED (data); unsigned deal + Beirut crossing = CONFIRMED (intel). The cheapest convexity in the "
   "dataset."),
 "sp-500": s(
   "**FRESH RECORD ON THE SOFTER PCE + PEACE TAPE — VIX 15.3 ON AN UNSIGNED DEAL IS THE COMPLACENCY TELL.** S&P 7,580.06 (+0.2% 1D, "
   "+6.2% MoM), with NASDAQ and Dow also at records, on the AI/semis bid (SMH +19.9% MoM) + softer April monthly PCE. VIX at a "
   "15.3 cycle low prices the ceasefire as done while the MOU is unsigned and Israel crossed the Beirut red line — a rejection or "
   "Lebanon break snaps the S&P -3-5% from record highs.",
   ["yfinance S&P/NASDAQ/Dow; TheStreet (PCE/records)", "Market A, C7"],
   "S&P 7,580 record / +6.2% MoM = CONFIRMED (data); VIX-complacency convexity = assessment grounded in the unsigned deal + Beirut "
   "crossing (CONFIRMED intel)."),
 "fertilizer-urea": s(
   "**THE FERTILIZER WAR-PREMIUM IS CRACKING — UREA -35% MoM; THE 'PHYSICAL STACK NOT UNWINDING' THESIS IS NO LONGER UNIFORMLY "
   "TRUE.** Urea fell to ~$410-443/t (Argus Mid-East granular high-$410s; TradingEconomics -35% MoM); CF Industries -11% MoM, "
   "Nutrien -7.5% MoM. Chain: deal-anticipation + Modi's import-restraint appeal -> Gulf export-normalization expectation. The "
   "bifurcation is now WITHIN the physical complex — fast legs (fertilizer/oil/LNG equity) de-price first; slow legs (insurance "
   "~8x, VLCC -36%) lag 6-12 weeks and have NOT unwound.",
   ["Argus (Mid-East granular high-$410s); TradingEconomics Urea", "Market C6, E2, Section F"],
   "Urea -35% MoM / ~$410-443/t = CONFIRMED (Argus + TE); CF/Nutrien = CONFIRMED; slow legs not unwound = carried (unverified)."),
 "natural-gas-lng": s(
   "**TWO DIVERGENT STORIES — QATAR-DISRUPTION LNG PREMIUM CRACKS (CHENIERE -17% MoM) WHILE US HENRY HUB RIPS +24% MoM ON "
   "NON-CRISIS SUPPLY/DEMAND.** Cheniere -17.2% MoM de-prices the Hormuz/LNG tail; European TTF eased to EUR45.96/MWh (-2.2% 1D) "
   "but holds a ~+30% YoY floor (Ras Laffan ~17% force majeure persists). Separately, Henry Hub +24.3% MoM to $3.29 is NON-crisis: "
   "storage injections below forecast + an LNG-export ramp (Golden Pass Train 1, Corpus Christi Stage 3 Train 5) + easing "
   "production.",
   ["TradingEconomics TTF/US natgas; Cheniere yfinance", "Market C6, D4, Section F"],
   "Cheniere -17% MoM / Henry Hub +24% MoM / TTF EUR45.96 = CONFIRMED (data); Henry Hub driver NON-crisis = analyst; Ras Laffan FM "
   "persists = carried."),
 "cheniere-energy": s(
   "**CHENIERE -17% MoM — THE HORMUZ/LNG TAIL UNWINDS HARD ON DEAL-ANTICIPATION.** LNG $224.86 (-2.1% 1D, -17.2% MoM, -9.5% 3M) as "
   "the Qatar-disruption/Hormuz-LNG tail premium de-prices — the LNG leg of the same fast-physical unwind cracking fertilizer "
   "(urea -35% MoM). Reversible on a deal collapse / Hormuz re-escalation; the slow legs have not unwound.",
   ["yfinance Cheniere", "Market C6, B"],
   "Cheniere -17.2% MoM = CONFIRMED (data); driver (Hormuz/LNG tail de-pricing) = analyst assessment."),
 "cf-industries": s(
   "**CF -11% MoM AS THE FERTILIZER WAR-PREMIUM CRACKS (UREA -35% MoM).** CF Industries $112.35 (-3.6% 1D, -11.0% MoM, +8.2% 3M) "
   "and Nutrien (-7.5% MoM) de-priced the Qatar-disruption nitrogen premium on deal-anticipation + Modi's import-restraint appeal. "
   "This node was stale (last updated 13 May); the -11% MoM unwind is now encoded. Reversible on a deal collapse / Gulf "
   "re-disruption.",
   ["yfinance CF/Nutrien; Argus urea", "Market C6, B"],
   "CF -11% MoM / -3.6% 1D = CONFIRMED (data); fertilizer-premium-unwind driver = analyst; prior staleness (13 May) reconciled."),
 "aluminum": s(
   "**ALUMINUM +13% MoM / +26% 3M — A DUAL AI/GRID-DEMAND + RESIDUAL GULF-PREMIUM BID, MOSTLY NON-CRISIS.** LME aluminum "
   "$3,917.75/mt (+0.2% 1D, +13.0% MoM). ~75% structural (AI/grid power demand, same as copper +8.2% MoM) + ~25% a residual "
   "EGA/Gulf supply premium that has NOT fully unwound. Demand-led, so not unwinding on deal-anticipation (unlike fertilizer/LNG).",
   ["yfinance/LME aluminum", "Market B, Metals table"],
   "Aluminum +13% MoM / +26% 3M = CONFIRMED (data); ~75/25 demand/premium split = analyst assessment."),
 "defense-sector": s(
   "**DEFENSE BID THE DISCRETE KINETIC EVENTS (ITA +10.5% MoM) EVEN AS THE BROAD TAPE PRICED PEACE — THE COMPLACENCY SPLIT.** ITA "
   "$235.44 (-0.1% 1D, +10.5% MoM, still -6.0% 3M). The monthly bid tracks May's discrete kinetic events (28 May missile "
   "exchange, Lebanon/Beirut escalation) while VIX sank to a 15.3 cycle low pricing the ceasefire as done. Defense votes the "
   "kinetic risk is real while index vol prices de-escalation — both can't be right for long. Lockheed +4.0% MoM but -21.6% 3M "
   "(deeply de-rated by the peace-track).",
   ["yfinance ITA/LMT", "Market B, C7"],
   "ITA +10.5% MoM / LMT +4.0% MoM = CONFIRMED (data); complacency-split read = assessment grounded in VIX 15.3 + kinetic events."),
}

n=0
for nid, signal in SIGS.items():
    fp = os.path.join(NODE_DIR, nid + ".json")
    with open(fp) as f: node = json.load(f)
    rs = node.setdefault("recent_signals", [])
    if rs and rs[0].get("date") == TODAY:
        print(f"skip {nid} (already has {TODAY} signal)"); continue
    rs.insert(0, signal)
    node["last_updated"] = TODAY
    with open(fp, "w") as f: json.dump(node, f, ensure_ascii=False, indent=2)
    n += 1
    print(f"signal added -> {nid}")
print("Total market signals added:", n)
