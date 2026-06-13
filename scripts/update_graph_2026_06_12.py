#!/usr/bin/env python3
"""Graph update for 2026-06-12 (morning) — the DE-ESCALATION pivot.
Deal track (UNSIGNED), oil -4%, VIX -9%, India +2-3%, gold +3.7% (inflation-unwind, NOT safe-haven).
Discipline: nothing moves watching->active on an unsigned deal; gold bounce is benign, not a regime flip.
Backup at backups/2026-06-12/graph/. Run from repo root."""
import json

DATE = "2026-06-12"
NODES = "graph/nodes"

def load(nid):
    with open(f"{NODES}/{nid}.json") as f:
        return json.load(f)

def save(nid, d):
    with open(f"{NODES}/{nid}.json", "w") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)

def add_signal(d, headline, sources, verification):
    d.setdefault("recent_signals", [])
    d["recent_signals"].insert(0, {"date": DATE, "headline": headline, "sources": sources, "verification": verification})
    d["recent_signals"] = d["recent_signals"][:26]

def bump_edges(d, updates):
    for to, ctx, w in updates:
        for e in d.get("top_edges", []):
            if e.get("to") == to:
                e["last_activated"] = DATE
                if isinstance(e.get("activation_count"), int):
                    e["activation_count"] += 1
                if ctx: e["context"] = ctx
                if w is not None: e["weight"] = w

def trig_note(d, subs, key, text, new_status=None):
    for t in d.get("active_triggers", []):
        c = t.get("condition", "")
        if all(s.lower() in c.lower() for s in subs):
            t[key] = text
            if new_status: t["status"] = new_status
            return True
    return False

def add_trig(d, t):
    d.setdefault("active_triggers", []).append(t)

def set_current(d, u):
    d.setdefault("current", {}); d["current"].update(u)

CH = []

# ===================== GEOPOLITICAL / DEAL TRACK =====================

# ---- iran ----
d = load("iran")
add_signal(d,
  "DE-ESCALATION PIVOT — DEAL 'NEVER CLOSER' BUT UNSIGNED. FM Araghchi told state TV the US-Iran agreement has 'never been closer,' an MoU 'could happen within 1 or 2 days,' describing a TWO-STAGE deal (MoU then negotiations) with a ceasefire 'on all fronts, including Lebanon.' FM spokesman Baqaei hedged: Iran 'has not reached a final conclusion,' citing 'US contradictions.' Crucially Araghchi said Iran will MAINTAIN CONTROL of Hormuz even post-deal ('will not be the same as in the past'). No third US strike round (Trump cancelled it). Rial context stable. This is the 8th 'deal close' claim of the war but the first with on-record Iranian FM optimism + a concrete US de-escalatory act.",
  ["IRNA/state TV (Araghchi)", "Al Jazeera", "India.com", "CBS (Baqaei)"],
  "CONFIRMED (Iranian statements); REPORTED (deal close); CLAIMED (final text)")
d["summary"] = ("Day 106 / 2026-06-12. **THE DE-ESCALATION PIVOT — IRAN AND THE US BOTH SAY A DEAL IS 'NEVER CLOSER,' BUT IT IS UNSIGNED AND THE ENRICHMENT RED LINE IS UNRESOLVED.** "
  "FM Araghchi (state TV) struck the most de-escalatory tone of the war — an MoU 'within 1-2 days,' a two-stage structure (MoU then detailed talks), a ceasefire 'on all fronts, including Lebanon' — while FM spokesman Baqaei kept the hedge alive ('no final conclusion,' 'US contradictions'). "
  "Two leverage-preserving tells: Iran will 'maintain CONTROL of Hormuz' even under a deal (Araghchi) — so a settlement reopens flow but may NOT restore the pre-war freedom-of-navigation regime; and Iran's Atomic Energy Organization has publicly refused enrichment limits, directly contradicting the reported deal term (15-20yr halt + dismantlement). "
  "The deeds matched the words DOWN this time: Trump CANCELLED the threatened third strike round, and the market priced de-escalation hard (oil -4%, VIX -9%). But the structure is unchanged — negotiate-while-leveraging, now with the blockade (not bombing) as the standing pressure. Treat the optimism as CONFIRMED-as-stated and the deal itself as REPORTED/unsigned.")
bump_edges(d, [
  ("united-states", "2026-06-12: Both sides say a deal is 'never closer'; Trump cancelled the third strike round. De-escalation — UNSIGNED, enrichment red line unresolved.", None),
])
add_trig(d, {
  "condition": "US-Iran deal/MoU SIGNED — a published official text reopening Hormuz and/or lifting the US naval blockade (the war-ending resolution event)",
  "status": "watching",
  "cascade": ["brent-crude", "strait-of-hormuz", "nifty-50", "india", "vix", "shipping-tankers", "marine-war-risk-insurance"],
  "added": DATE,
  "note": "As of 12 Jun: Trump claims a 'great settlement,' Pakistan claims a 'final, agreed-upon text,' Araghchi says 'never closer / 1-2 days,' a US official puts signing at 80-85%. But it is UNSIGNED, Iran says 'no final conclusion,' and the US-zero-enrichment vs Iran-no-limits contradiction is unresolved. This is the 8th 'days away' claim of the war. Fires ONLY on a published signed text — not on a claim. Would reopen Hormuz (reportedly 30 days), lift the blockade, and reprice oil/India/VIX. NOTE Araghchi: Iran retains Hormuz 'control' even post-deal — reopening may not restore the pre-war regime."})
d["last_updated"] = DATE; save("iran", d); CH.append("iran")

# ---- united-states ----
d = load("united-states")
add_signal(d,
  "TRUMP CANCELLED THE THIRD STRIKE ROUND + ANNOUNCED A 'GREAT SETTLEMENT.' Hours before the threatened 'bigger' round, Trump called the strikes OFF and announced a US-Iran 'great settlement' to be 'signed quickly,' saying terms were approved by the US, Israel, Saudi, UAE, Qatar, Turkey, Pakistan, Bahrain, Kuwait, Jordan, Egypt, and that he believes Supreme Leader Mojtaba Khamenei is ready to sign. A senior official put signing odds at '80-85%... not 100%.' Trump: 'The Naval Blockade will remain in full force until this Transaction is finalized' — so enforcement continues until signing. No third strike round was launched (confirmed non-event).",
  ["RFE/RL", "CNN live 11 Jun", "CBS", "Fox"],
  "CONFIRMED (cancelled strikes; the announcement); REPORTED (settlement terms); CLAIMED (final text)")
d["summary"] = ("Day 106 / 2026-06-12. **THE US PIVOTED FROM NIGHTLY STRIKES TO DEAL-MAKING WITHIN 24 HOURS — TRUMP CANCELLED THE THREATENED THIRD ROUND AND ANNOUNCED A 'GREAT SETTLEMENT.'** "
  "The cancellation is a CONFIRMED de-escalatory action (no third round was launched); the 'great settlement' and the leaked terms (Hormuz reopening within 30 days, blockade lifted, 60-day ceasefire, Iran halts enrichment 15-20yrs + dismantles sites, $24bn assets phased, war-damage compensation) are REPORTED/unsigned. A senior official caps signing at 80-85%. "
  "Critically, **the naval blockade remains 'in full force until this Transaction is finalized'** — the enforcement campaign that killed the three Indian Settebello sailors continues until a signature, so the India-US irritant persists in the interim even as the macro arc turns. "
  "The binding US constraint is unchanged and does NOT reverse on a deal: May CPI 4.2% and the December-hike repricing are domestic and sticky (the 10Y barely moved at 4.49% even as oil fell 4%). De-escalation helps oil-importers (India) far more than it helps US assets.")
bump_edges(d, [
  ("iran", "2026-06-12: Trump cancelled the third strike round and announced a 'great settlement'; de-escalation, UNSIGNED. Blockade stays until finalized.", None),
])
trig_note(d, ["strike", "iran"], "note_2026-06-12",
  "STAYS active but DE-ESCALATING. The threatened third strike round was CANCELLED — no new US strikes on Iran this window. The trigger stays active (the blockade/enforcement campaign continues 'in full force until finalized'), but the kinetic tempo has stopped at two rounds pending the deal.")
trig_note(d, ["kharg"], "note_2026-06-12",
  "STAYS WATCHING — probability FALLEN. Trump cancelled the strikes and pivoted to a settlement; no Kharg force posture. With de-escalation, the near-term Kharg-operation probability has dropped sharply. Window closes 15 Jun.")
trig_note(d, ["settebello"], "note_2026-06-12",
  "STAYS WATCHING. India's response remains a demarche (US Charge Jason Meeks) + 'deepest concern' — diplomatic, not material. The deal track caps the escalation risk; the blockade staying until signing means the irritant persists short-term.")
d["last_updated"] = DATE; save("united-states", d); CH.append("united-states")

# ---- trump ----
d = load("trump")
add_signal(d,
  "FROM 'BOMB THE S—' TO 'GREAT SETTLEMENT' IN 24 HOURS. Trump cancelled the threatened third strike round and announced a US-Iran 'great settlement' to be 'signed quickly,' said he believes Mojtaba Khamenei is ready to sign, and listed ~11 states as approving. Met with skepticism (The Hill) given ~7 prior 'days away' claims and the unresolved enrichment dispute. Running the de-escalation channel personally, as he ran the escalation one.",
  ["RFE/RL", "CBS", "The Hill", "Fox"],
  "CONFIRMED (statements + cancelled strikes); REPORTED/CLAIMED (the settlement)")
d["last_updated"] = DATE; save("trump", d); CH.append("trump")

# ---- nuclear-program ----
d = load("nuclear-program")
add_signal(d,
  "THE DEAL'S CENTRAL UNRESOLVED RISK — ENRICHMENT. Reported deal terms have Iran HALTING enrichment for 15-20 years and DISMANTLING nuclear sites (enriched uranium 'destroyed on site and removed from the country'). But Iran's Atomic Energy Organization has publicly REFUSED any limits on enrichment, and talks have been 'deadlocked' on exactly this (US 'zero enrichment' vs Iran 'no limits'). Either Iran has quietly conceded its core red line (genuine breakthrough) or the 'final text' papers over the gap and risks collapsing like ~7 prior soft deadlines.",
  ["The Hill", "House of Commons Library", "CBS/CNBC (reported terms)"],
  "CONFIRMED (each side's stated position); the contradiction is the open question")
d["last_updated"] = DATE; save("nuclear-program", d); CH.append("nuclear-program")

# ---- strait-of-hormuz ----
d = load("strait-of-hormuz")
add_signal(d,
  "DEAL WOULD REOPEN HORMUZ IN ~30 DAYS — BUT IRAN INTENDS TO RETAIN 'CONTROL' EVEN POST-DEAL, AND THE BLOCKADE STAYS UNTIL SIGNING. Reported terms (CBS/CNBC): reopening to pre-war volumes within 30 days + US lifting the naval blockade. BUT Araghchi: 'Iran will maintain control over the Strait of Hormuz... the future of the Strait will not be the same as in the past.' And Trump: 'The Naval Blockade will remain in full force until this Transaction is finalized.' So a signed deal reopens FLOW but may NOT restore pre-war freedom-of-navigation; until signing, the ~5%-flow blockade persists. Oil priced the reopening hope hard: Brent -4.1% to $86.71.",
  ["Al Jazeera/IRNA (Araghchi)", "RFE/RL (Trump blockade)", "CBS/CNBC (terms)"],
  "REPORTED (reopening term); CONFIRMED (Iran-retains-control + blockade-stays positions)")
d["summary"] = ("Day 106 / 2026-06-12. **THE STRAIT BECAME THE CENTRAL BARGAINING CHIP — A DEAL WOULD REOPEN IT IN ~30 DAYS, BUT IRAN INTENDS TO KEEP 'CONTROL' AND THE BLOCKADE STAYS UNTIL SIGNING.** "
  "Reported deal terms have Hormuz reopening to pre-war volumes within 30 days and the US lifting its naval blockade. Two caveats define the trade: (1) Araghchi says Iran will 'maintain control' of the Strait even under a deal — reopening restores FLOW but not necessarily the pre-war freedom-of-navigation regime, so the structural floor under oil may be higher than a clean reopening implies; (2) Trump says the blockade stays 'in full force until finalized,' so the ~5%-of-normal-flow paralysis and the lethal enforcement campaign continue until a signature. "
  "The market priced the reopening hope hard: Brent -4.1% to $86.71 (WTI below $85), the war premium finally deflating DOWN on de-escalation after refusing to bid UP through the kinetic escalation. Physical (VLCC rates, war-risk cover ~7-10% of hull) has NOT unwound — paper-oil drops on hope, physical waits for the signature. Tanker equities (Frontline +9.8%) priced reopening as VOLUME-bullish (idled-fleet re-employment).")
bump_edges(d, [
  ("brent-crude", "2026-06-12: Deal-driven reopening hope priced Brent -4.1% to $86.71 — the war premium deflating DOWN; but Iran intends to retain Hormuz 'control' even post-deal.", None),
  ("shipping-tankers", "2026-06-12: Reopening read as VOLUME-bullish for tankers (Frontline +9.8%) — idled-fleet re-employment; physical rates still elevated until signing.", None),
])
trig_note(d, ["reopens to all traffic"], "note_2026-06-12",
  "STAYS WATCHING — but for the first time the vector points TOWARD reopening (deal terms: pre-war volumes within 30 days). NOT fired: unsigned, and Araghchi says Iran retains 'control' even post-deal, so a clean reopening is not assured. Fires only on operationally-confirmed restored transit.")
trig_note(d, ["kharg"], "note_2026-06-12",
  "STAYS WATCHING — probability fallen with the cancelled strikes and the deal track. Window closes 15 Jun.")
trig_note(d, ["enforcement of the 10 jun complete-closure"], "note_2026-06-12",
  "STAYS WATCHING. No new operationally-confirmed strike on a neutral hull this window; the blockade stays 'in full force until finalized' but the deal track lowers near-term enforcement-escalation risk.")
d["last_updated"] = DATE; save("strait-of-hormuz", d); CH.append("strait-of-hormuz")

# ---- pakistan ----
d = load("pakistan")
add_signal(d,
  "PAKISTAN DECLARES A 'FINAL, AGREED-UPON TEXT.' PM Shehbaz Sharif said a 'final, agreed-upon text' of the US-Iran peace deal has been reached, Pakistan is 'working closely with both sides to finalize next steps,' and 'peace has never been this close' — the most forward-leaning mediator claim, consistent with the Naqvi/Munir channel tracked all week. Iran has NOT formally confirmed the text (Baqaei: 'no final conclusion'). Pakistan as mediator has a stake in the optimistic framing.",
  ["CBS", "NBC", "Al Jazeera"],
  "REPORTED (mediator claim; Iran not formally confirming)")
d["last_updated"] = DATE; save("pakistan", d); CH.append("pakistan")

# ---- mojtaba-khamenei ----
d = load("mojtaba-khamenei")
add_signal(d,
  "TRUMP SAYS KHAMENEI 'READY TO SIGN.' Trump stated he believes Supreme Leader Mojtaba Khamenei is ready to sign off on the settlement, and that discussions were 'brought to the highest level of Iranian leadership and approved.' This is a US CLAIM about the Supreme Leader's position; no direct statement from Khamenei's office was published, and Iran's FM spokesman simultaneously said 'no final conclusion.'",
  ["RFE/RL", "CBS"],
  "CLAIMED (Trump's characterization; no direct Khamenei statement)")
d["last_updated"] = DATE; save("mojtaba-khamenei", d); CH.append("mojtaba-khamenei")

# ===================== MARKETS — THE DE-ESCALATION TRADE =====================

# ---- brent-crude ----
d = load("brent-crude")
add_signal(d,
  "BRENT -4.1% TO $86.71 (WTI -3.9% to $84.29; WTI fell ~4% in 15 min on the cancelled-strikes headline). THE PREMIUM FINALLY DEFLATED DOWN. The risk-premium that REFUSED to bid up through state-on-state strikes, the Hormuz closure and US attacks collapsed on the first credible de-escalation signal (deal hopes + cancelled third round) — confirming the market was positioned for choreography, with oil's convexity on the DOWNSIDE. Down ~6% on the week, -17.9% 1M. WTI now below $85; Brent approaching the 'sub-$85 sustained' watch (not crossed). $100-sustained trigger deeply resolved.",
  ["CNBC", "TradingEconomics", "Bloomberg", "markets.md C2"],
  "CONFIRMED (market data)")
set_current(d, {
  "price": "Brent $86.71 (12 Jun, -4.1%); WTI $84.29 (-3.9%, below $85); DXY 99.81 (soft); European TTF ~EUR48-49/MWh (easing, sub-50).",
  "delta_1d": "-4.1% (Brent) -- the war premium FINALLY deflated DOWN on US-Iran deal hopes + Trump cancelling the third strike round (WTI -4% in 15 min on the headline). The asymmetry resolved on the downside.",
  "delta_1m": "-17.9% MoM.",
  "regime": "DE-ESCALATION PRICED. Brent trades the deal probability (~80-85% per a US official) + the Fed path + China demand, now ~$87 and falling. The premium that wouldn't bid UP collapsed DOWN -- but the move is HIGH-reversibility two-way: an unsigned deal that breaks on the enrichment red line reverses it violently. Floor caveat: Araghchi says Iran retains Hormuz 'control' even post-deal, so a reopening may not fully normalize the structural premium.",
  "trigger_status": "'Brent $100 sustained' DEEPLY RESOLVED. 'Brent sub-$85 sustained' APPROACHING -- WTI below $85, Brent $86.71, but NOT crossed and NOT sustained. Do NOT fire on one day."})
trig_note(d, ["below $85"], "note_2026-06-12",
  "APPROACHING but STAYS WATCHING. WTI below $85, Brent $86.71 on deal-driven de-escalation -- the closest of the war, but not crossed (Brent >$85) and not 'sustained.' Watch if the deal signs and reopening prices in further.")
d["last_updated"] = DATE; save("brent-crude", d); CH.append("brent-crude")

# ---- vix ----
d = load("vix")
add_signal(d,
  "VIX -9.1% TO 17.68 — FEAR COLLAPSE ON DEAL HOPES. From a 22.22 close (10 Jun, the first >22 close of the war) to sub-18 in two sessions as Trump cancelled the strikes and the deal advanced. The >22-sustained trigger is now firmly MOOT (~4.5pts below the line); the 10 Jun straddle was a one-print near-miss, correctly never fired. Equity vol back to a low-18 handle confirms the market reads the deal as high-probability.",
  ["yfinance", "markets.md C1"],
  "CONFIRMED")
set_current(d, {
  "price": "17.68 (12 Jun, -9.1%)",
  "delta_1d": "-9.1% -- fear collapse on US-Iran deal hopes + cancelled strikes; from 22.22 (10 Jun) to sub-18 in two sessions",
  "read": "VIX 17.68 -- the >22 trigger is now firmly MOOT (~4.5pts below). The 10 Jun 22.22 close (first >22 of the war, on CPI+escalation) was a one-print near-miss that correctly never fired the 'sustained 2 sessions' trigger; vol has since collapsed on de-escalation. The convexity is cheap again: an UNCALIBRATED re-escalation (deal collapses on enrichment) would re-gap vol, but the base case is now priced as de-escalation."})
trig_note(d, ["vix", ">22"], "note_2026-06-12",
  "STAYS WATCHING — now firmly MOOT at 17.68 (~4.5pts below the line). The 10 Jun straddle never sustained; de-escalation collapsed vol.")
d["last_updated"] = DATE; save("vix", d); CH.append("vix")

# ---- gold ----
d = load("gold")
add_signal(d,
  "GOLD +3.7% TO $4,239.90 — NOT A SAFE-HAVEN BID; THE INFLATION-REGIME HEADWIND UNWINDING. On a RISK-ON day (stocks up, VIX -9%), gold bounced off its ~23-March low alongside silver +6.6%, copper +3.4%, platinum +3.5%. Mechanism = mirror image of the cycle's drag: oil -4% -> inflation/December-hike fears EASE -> real yields/DXY soften -> the headwind on zero-yield gold releases -> gold bounces. THE TELL it is NOT a flight to safety: copper +3.4% on the same day (industrial metals don't rally in a risk-off). This is a risk-ON metals bid + oversold short-covering, the SAME inflation regime relaxing -- NOT the financial-system-risk mutation the $4,600 trigger watches for.",
  ["yfinance", "markets.md C3", "BullionVault (context)"],
  "CONFIRMED (price)")
set_current(d, {
  "price": "$4,239.90 (12 Jun, +3.7%) -- bounce off the ~23-Mar low; Silver $68.12 (+6.6%); Copper $6.47/lb (+3.4%, the tell); Platinum $1,720.60 (+3.5%); DXY 99.81 (soft).",
  "delta_1d": "+3.7% -- rose on a RISK-ON day because oil -4% eased the inflation/real-yields headwind that had crushed it; NOT a safe-haven bid (copper +3.4% confirms risk-on).",
  "delta_1m": "-9.7% MoM (still the cycle underperformer, but bouncing).",
  "regime": "INFLATION / REAL-YIELDS regime, now RELAXING (not flipped). Gold fell all cycle because oil->CPI->hike-repricing lifted real yields/DXY; today oil -4% reversed that mechanism and gold bounced. This is the SAME regime easing, NOT a mutation to financial-system risk. Copper +3.4% on the same day is the disambiguation: a risk-ON metals bid, not a haven flight.",
  "watching_threshold": "Gold sustains above $4,600 for 3+ sessions = regime-shift confirmed -- still ~$360 below at $4,239.90. The bounce moves TOWARD the trigger but on a BENIGN mechanism (inflation-unwind), not the crisis-mutation the trigger requires. Do NOT read the bounce as a regime flip."})
trig_note(d, ["$4,600"], "note_2026-06-12",
  "STAYS WATCHING. Gold bounced +3.7% to $4,239 but on a BENIGN inflation-unwind mechanism (oil down -> real yields ease), NOT the financial-system-risk mutation the trigger requires. Copper +3.4% same day confirms risk-ON, not haven. ~$360 below; do not misread the bounce as a regime flip.")
d["last_updated"] = DATE; save("gold", d); CH.append("gold")

# ---- nifty-50 ----
d = load("nifty-50")
add_signal(d,
  "NIFTY +2.0% TO 23,622.90, SENSEX +2.3% (+1,695), BANK NIFTY +3.0% — THE DEAL+OIL RELIEF RALLY. Reversed the 11 Jun 'resilience thinned' read: US-Iran deal hopes + oil -4% -> India's ~85%-imported oil bill eases -> fiscal/inflation/CAD relief -> broad rally, financials leading. The cleanest India-POSITIVE transmission of the war (the war finally HELPING India via the de-escalation/oil-down channel). But it is a one-day rally on deal HOPE, not a SIGNED deal or an FII-flow turn.",
  ["Business Standard 12 Jun", "TradingEconomics", "markets.md C5"],
  "CONFIRMED (market data)")
set_current(d, {
  "price": "Nifty 23,622.90 (+2.0%, 12 Jun); Sensex 75,527.95 (+2.3%, +1,695); Bank Nifty 56,814.80 (+3.0%).",
  "delta_1d": "+2.0% (Nifty) -- deal hopes + oil -4% relief rally; financials/Bank Nifty led on the rate-relief read",
  "driver": "DEAL+OIL RELIEF. US-Iran de-escalation + Brent -4% eased India's import-cost/fiscal/inflation pressure -> Nifty +2.0%, Sensex +2.3%, Bank Nifty +3.0%. Reverses the 11 Jun thinning. The cleanest India-POSITIVE war transmission yet -- but on HOPE (deal unsigned, ~80-85% odds) and not yet an FII-flow turn.",
  "note": "Deployment scorecard IMPROVING: Brent <$95 [✓ $86.71], rupee toward ₹93-94 [closer, ₹95.10], FII net-positive 3+ sessions [STILL the unconfirmed leg]. Improving on hope, not signature -- no deployment signal yet."})
d["last_updated"] = DATE; save("nifty-50", d); CH.append("nifty-50")

# ---- india ----
d = load("india")
add_signal(d,
  "RELIEF RALLY + SOVEREIGNTY ANGER FADING. The deal+oil-down drove a broad India rally (Nifty +2.0%, Sensex +2.3%, rupee firmer to ₹95.10); Indian media pivoted from the 11 Jun 'India vs America' Settebello grievance back to the upside (cheaper oil helps the importer). The Settebello protest advanced procedurally (demarche to US Charge Jason Meeks, 'deepest concern,' three Indian-crewed ships hit in four days) but is now the secondary frame. Deployment conditions improving (Brent $86.71, rupee ₹95.10) but on deal HOPE, not a signature or an FII turn.",
  ["Business Standard 12 Jun", "SCMP", "Al Jazeera", "markets.md C5"],
  "CONFIRMED")
d["summary"] = ("Day 106 / 2026-06-12. **THE WAR FINALLY HELPED INDIA — A DEAL+OIL RELIEF RALLY (NIFTY +2.0%, SENSEX +2.3%, RUPEE FIRMER) AS THE DE-ESCALATION/OIL-DOWN CHANNEL FIRED POSITIVE FOR THE FIRST TIME.** "
  "US-Iran deal hopes plus Brent -4% eased India's import-cost, fiscal and inflation pressure; financials led (Bank Nifty +3.0%) and the rupee firmed to ₹95.10, AWAY from the ₹96 line that was un-ticking yesterday. The Indian press swung from the Settebello sovereignty-grievance back to the upside within a day. "
  "The Settebello fallout advanced only procedurally (demarche to US Charge Jason Meeks; 'deepest concern over the ongoing incidents'); with the blockade staying until a deal signs, the irritant persists short-term but the deal track caps the rupture risk. "
  "Deployment scorecard, IMPROVING for the first time: Brent <$95 [✓ $86.71], organic rupee toward ₹93-94 [closer, ₹95.10], FII net-positive 3+ sessions [STILL UNCONFIRMED]. The conditions are improving — but on a ~80-85% deal HOPE, not a signature, and not yet an FII-flow turn. No deployment signal yet.")
d["last_updated"] = DATE; save("india", d); CH.append("india")

# ---- inr-usd ----
d = load("inr-usd")
add_signal(d,
  "RUPEE FIRMED TO ~₹95.10 (from ~95.79) — AWAY FROM ₹96 on deal hopes + oil -4%. DXY soft (99.81), EM-FX risk-on (USD/BRL -2.5%), and the India import-cost relief eased rupee pressure. The ₹96 RBI-intervention trigger STAYS WATCHING, pressure now EASING (was pressed at 95.79 yesterday). The ₹93-94 organic-retracement path needs Brent sustained-low + an FII turn + a signed deal; two of three improving.",
  ["market-data.py", "markets.md C5"],
  "CONFIRMED")
set_current(d, {
  "price": "USD/INR ~₹95.10 (12 Jun, firmer from 95.79) -- moving AWAY from ₹96; ₹94.50 broken, ₹96 not breached.",
  "delta_1d": "stronger to ~₹95.10 -- deal hopes + oil -4% + soft DXY eased EM-FX pressure",
  "driver": "DE-ESCALATION RELIEF. US-Iran deal hopes + Brent -4% + DXY soft (99.81) -> rupee firmed to ₹95.10, away from the ₹96 line. The RBI June 5 package plus the oil-down channel are both working now. ₹93-94 organic retracement needs the deal to sign + an FII turn (still unconfirmed).",
  "trigger_status": "₹96 RBI-direct-intervention trigger STAYS WATCHING -- pressure EASING (₹95.10, away from the line). ₹94.50 resolved (structurally weaker). The deal-driven oil-down is the rupee's first clear tailwind in weeks."})
trig_note(d, ["96"], "note_2026-06-12",
  "STAYS WATCHING — pressure EASING. Rupee firmed to ₹95.10 (from 95.79) on deal hopes + oil -4%; moving away from the line.")
d["last_updated"] = DATE; save("inr-usd", d); CH.append("inr-usd")

# ---- fii-flows ----
d = load("fii-flows")
add_signal(d,
  "THE UNCONFIRMED DEPLOYMENT LEG. The 12 Jun deal+oil relief rally (Nifty +2.0%) is equity-price action, NOT yet a confirmed FII-flow turn -- the net-positive-3-sessions deployment condition remains the open question and the 12-Jun FII print was not yet available. A one-day rally on deal HOPE is not the institutional-money turn the deployment thesis requires; watch whether FIIs actually buy into the de-escalation or whether DIIs again do the lifting.",
  ["markets.md F", "Business Standard"],
  "REPORTED (rally confirmed; FII-flow turn unconfirmed)")
d["last_updated"] = DATE; save("fii-flows", d); CH.append("fii-flows")

# ---- defense-sector ----
d = load("defense-sector")
add_signal(d,
  "DEFENSE GAVE BACK THE KINETIC BID — ITA -1.0%, LMT -1.5% — as the strikes were cancelled and the deal advanced. The 11 Jun 'more strikes' bid (LMT +3.6%) reversed on de-escalation; pure positioning, high reversibility. The kinetic-continuation trade fades when the kinetics stop.",
  ["market-data.py", "markets.md C7"],
  "CONFIRMED (price)")
bump_edges(d, [("united-states", "2026-06-12: Strikes cancelled / deal track -> defense gave back the kinetic bid (ITA -1.0%, LMT -1.5%). De-escalation fades the trade.", None)])
d["last_updated"] = DATE; save("defense-sector", d); CH.append("defense-sector")

# ---- shipping-tankers ----
d = load("shipping-tankers")
add_signal(d,
  "FRONTLINE +9.8% — DE-ESCALATION READ AS VOLUME-BULLISH FOR TANKERS. The market priced a Hormuz reopening as NET BULLISH tanker equities: the idled/diverted fleet (Hormuz ran ~5% of normal) gets RE-EMPLOYED, ton-mile demand normalizes upward -> FRO +9.8%, BOAT +1.2%. Two-sided (bullish volume, bearish war-risk premium); today volume-recovery dominated. MODERATE confidence (no single confirmed catalyst; 3M feed nan). Physical VLCC rates + war-risk cover stay ELEVATED -- not unwinding until the deal signs.",
  ["market-data.py", "Lloyd's List", "markets.md C4"],
  "CONFIRMED (price); moderate-confidence attribution")
d["last_updated"] = DATE; save("shipping-tankers", d); CH.append("shipping-tankers")

# ---- marine-war-risk-insurance ----
d = load("marine-war-risk-insurance")
add_signal(d,
  "PHYSICAL HASN'T UNWOUND — cover still ~7-10% of hull per transit, ~340% above pre-Feb-28, VLCC spot rates elevated (a recent ~24% session spike). Paper-oil dropped 4% on deal HOPE while physical shipping risk stays firm because the deal is UNSIGNED and the blockade remains 'in full force until finalized.' The paper-physical bifurcation persists, now with paper falling; it resolves only when a signature actually reopens flow.",
  ["Lloyd's List", "Gulf News", "markets.md F"],
  "REPORTED (market structure)")
d["last_updated"] = DATE; save("marine-war-risk-insurance", d); CH.append("marine-war-risk-insurance")

# ---- aluminum ----
d = load("aluminum")
add_signal(d,
  "ALUMINUM -5.8% (±artifact) TO ~$3,575 — THE REAL WAR PREMIUM DE-PRICING ON DEAL HOPES, the 'most reversible move' tested in the DOWN direction. De-escalation -> the genuine Gulf-supply premium (EGA/ALBA offline) deflates. Copper +3.4% on the same day (control) confirms this is aluminium's war-premium unwind, NOT an industrial-demand collapse. Magnitude carries the usual thin-ALI=F artifact caveat; direction reliable.",
  ["market-data.py", "markets.md C7"],
  "CONFIRMED (direction; ±2pt magnitude caveat)")
set_current(d, {
  "price": "~$3,575/mt (12 Jun, -5.8% ±artifact) -- war premium de-pricing on deal hopes; Copper +3.4% control confirms premium-unwind not demand collapse.",
  "delta_1d": "-5.8% (±thin-ALI=F artifact; direction reliable) -- the real Gulf war premium deflating on de-escalation, the 'most reversible move' in the DOWN direction",
  "driver": "WAR-PREMIUM UNWIND on de-escalation. Aluminium carried the one genuine physical Gulf premium (EGA flagship ~1-yr restart, ALBA partially suspended, WoodMac up-to-3.5Mt 2026 loss); deal hopes deflate it. Copper resilient (+3.4%) confirms premium dynamics, not demand collapse. The structural supply floor remains -- a deal that does NOT actually restart Gulf smelters leaves the physical shortage intact even as the premium de-prices."})
d["last_updated"] = DATE; save("aluminum", d); CH.append("aluminum")

# ---- us-10y-yield ----
d = load("us-10y-yield")
add_signal(d,
  "10Y ~4.49% — BARELY MOVED even as oil fell 4%: the 'deal helps oil-importers, not the Fed' split. De-escalation eases oil but does NOT un-print May CPI 4.2% or reverse the December-hike repricing -- the US's binding constraint is domestic and sticky. DXY soft (99.81) on risk-on. India 10Y eased to ~6.85-6.90% on the oil-down + G-sec tax exemption.",
  ["market-data.py", "markets.md C6"],
  "CONFIRMED")
set_current(d, {
  "price": "4.49% (10Y -- barely moved on the oil drop); 3.62% (2Y); DXY 99.81 (soft). India 10Y ~6.85-6.90% (easing on oil-down).",
  "delta_1d": "~flat (10Y) -- the de-escalation/oil-down does NOT reverse the May CPI print or the Dec-hike repricing; the US rates channel is sticky",
  "driver": "THE STICKY CHANNEL. Oil -4% on deal hopes but the 10Y held 4.49% -- May CPI 4.2% and the December-hike repricing are domestic and do not un-print on a Hormuz deal. This is why US equities only rose +0.5% while oil-importers (India +2-3%, Europe +1.8%) rallied hard. India 10Y eases on the oil-down (importer benefit)."})
d["last_updated"] = DATE; save("us-10y-yield", d); CH.append("us-10y-yield")

# ---- fed ----
d = load("fed")
add_signal(d,
  "THE DEAL DOESN'T FIX THE FED. Oil fell 4% on de-escalation but the December-hike repricing held (10Y 4.49% flat) -- May CPI 4.2% does not un-print, energy base effects take 2+ quarters to flush. The crisis transmits to US assets via the sticky CPI/rates channel, so a Hormuz deal helps oil-IMPORTERS (India) far more than US assets. A SUSTAINED oil-down (if the deal holds) would, over quarters, ease the energy-CPI impulse -- but not on a headline.",
  ["market-data.py", "markets.md C6/D"],
  "CONFIRMED")
d["last_updated"] = DATE; save("fed", d); CH.append("fed")

# ---- sp-500 ----
d = load("sp-500")
add_signal(d,
  "S&P +0.5% TO 7,431 — MUTED vs the global rally (India +2-3%, Europe +1.8%, KOSPI +4.6%). The deal eases OIL, which helps oil-importers directly, but the US's binding constraint is the CPI/Fed overhang, which a Hormuz deal does not reverse (10Y flat 4.49%). The S&P recovered the CPI-shock losses over 11-12 Jun (7,266 -> 7,431) but the de-escalation upside is capped by the rates channel. NASDAQ +0.3%, Dow +0.7%.",
  ["market-data.py", "markets.md C6", "Bloomberg"],
  "CONFIRMED")
set_current(d, {
  "price": "S&P 7,431.46 (+0.5%, 12 Jun); NASDAQ 25,888.84 (+0.3%); Dow 51,202.26 (+0.7%); VIX 17.68 (-9.1%).",
  "delta_1d": "+0.5% (S&P) -- recovered the CPI-shock losses but MUTED vs oil-importers; the Fed/CPI overhang caps the de-escalation upside",
  "driver": "DEAL HELPS OIL-IMPORTERS MORE THAN THE US. The de-escalation eased oil and collapsed VIX (-9.1% to 17.68), recovering the S&P to 7,431 -- but the gain is capped at +0.5% vs India/Europe/Asia's +2-4% because the US's binding constraint (CPI 4.2%, Dec-hike repricing) does not reverse on a Hormuz deal. Chip/AI rebound (SMH +1.7%) did much of the lifting."})
d["last_updated"] = DATE; save("sp-500", d); CH.append("sp-500")

# ---- kospi / samsung / sk-hynix / semiconductors ----
d = load("kospi")
add_signal(d,
  "KOSPI +4.6% (TAIEX +2.4%, Nikkei +2.8%) — RISK-ON RELIEF + AI/CHIP REBOUND, a sharp two-way whipsaw from the 10 Jun circuit-breaker DOWN week. ~40% de-escalation relief, ~60% the AI/memory bounce (SMH +1.7%, +8.3% 1M). The North-Asia tape is high-vol and headline-driven; the structural helium overhang persists underneath.",
  ["market-data.py", "markets.md C-context/D"],
  "CONFIRMED (price)")
set_current(d, {
  "price": "KOSPI 8,123.62 (+4.6%); TAIEX 44,169 (+2.4%); Nikkei 66,020 (+2.8%); SMH $619.96 (+1.7%, +8.3% 1M).",
  "delta_1d": "+4.6% -- risk-on relief + AI/memory rebound; a whipsaw from the 10 Jun circuit-breaker down week",
  "driver": "TWO LEGS: ~40% US-Iran de-escalation relief, ~60% the AI/memory valuation bounce (post the 10 Jun unwind). High-vol two-way tape; the helium overhang and the IDC -13% smartphone demand cut remain the structural bears underneath."})
d["last_updated"] = DATE; save("kospi", d); CH.append("kospi")

for nid, mv in [("samsung", "+ in the KOSPI risk-on/AI rebound"), ("sk-hynix", "+ in the KOSPI risk-on/AI rebound")]:
    d = load(nid)
    add_signal(d,
      f"Bounced {mv} (12 Jun) as North-Asia tech rallied on US-Iran de-escalation relief + the AI/memory valuation rebound (SMH +1.7%) — a whipsaw from the 10 Jun circuit-breaker week. Structural overhang (IDC -13% 2026 smartphones, helium ~6-mo inventories) persists underneath the bounce.",
      ["market-data.py", "markets.md D"], "CONFIRMED (price)")
    d["last_updated"] = DATE; save(nid, d); CH.append(nid)

d = load("semiconductors")
add_signal(d,
  "SMH +1.7% (+8.3% 1M) — the AI/memory complex rebounding, doing much of the lifting in the US/North-Asia rally. Partly de-escalation relief, mostly the post-10-Jun valuation bounce. The IDC -13% 2026 smartphone demand cut and the helium overhang remain the structural bears; Micron-Bechtel NY fab proceeds.",
  ["market-data.py", "markets.md D"], "CONFIRMED (price)")
d["last_updated"] = DATE; save("semiconductors", d); CH.append("semiconductors")

# ---- european-ttf-gas ----
d = load("european-ttf-gas")
add_signal(d,
  "TTF held ~EUR48-49/MWh, sub-50 (10 Jun high EUR49.9), EASING as the deal lowers the Hormuz-LNG disruption premium (the strait carries ~19% of global LNG). Storage-refill-competition framing relaxes if the deal holds; ~+33% YoY floor intact. No new European emergency measures.",
  ["gmk.center", "TradingEconomics", "markets.md F"],
  "CONFIRMED (price)")
set_current(d, {
  "price": "~EUR48-49/MWh (12 Jun, sub-50, easing)",
  "delta_1d": "~flat/easing -- deal hopes lower the Hormuz-LNG disruption premium",
  "delta_1m": "held sub-50; ~+33% YoY floor intact"})
d["last_updated"] = DATE; save("european-ttf-gas", d); CH.append("european-ttf-gas")

# ---- cf-industries / fertilizer-urea ----
d = load("cf-industries")
add_signal(d,
  "CF +2.7% (Nutrien +3.1%) — broad risk-on equity flow on the de-escalation day, NOT a physical-price signal: physical urea stays soft (~$397/t, -27% 1M). Same paper-physical caution as before; the equity bounce is risk-on rotation, not fertilizer-disruption pricing.",
  ["market-data.py", "markets.md D"], "CONFIRMED (price)")
d["last_updated"] = DATE; save("cf-industries", d); CH.append("cf-industries")

d = load("fertilizer-urea")
add_signal(d,
  "Physical urea remains SOFT (~$397/t, -27% 1M) even as CF/NTR equity rose +2-3% on the risk-on day — the physical-disruption edge should NOT be strengthened on the equity move. A signed deal reopening Hormuz would further relieve the latent urea-export-transit risk (~40-49% of urea exports transit the strait).",
  ["market-data.py", "markets.md D/F"], "CONFIRMED (price)")
d["last_updated"] = DATE; save("fertilizer-urea", d); CH.append("fertilizer-urea")

# ---- natural-gas-lng ----
d = load("natural-gas-lng")
add_signal(d,
  "Henry Hub +1.7% on US weather/storage (~zero crisis). The crisis-linked gauge is European TTF (~EUR48-49, easing on the deal), not Henry Hub. A signed deal reopening Hormuz would relieve the ~19%-of-global-LNG transit risk the strait carries.",
  ["market-data.py", "markets.md F"], "CONFIRMED (price)")
d["last_updated"] = DATE; save("natural-gas-lng", d); CH.append("natural-gas-lng")

# ---- lebanon / hezbollah / houthis / red-sea / israel (folding into all-fronts ceasefire) ----
d = load("lebanon")
add_signal(d,
  "Lebanon is folding into the deal — Araghchi said the agreement includes 'a ceasefire on all fronts, including in Lebanon.' No specific new major Lebanon strike was confirmed this window (coverage gap, not a confirmed absence). The theatre that kept escalating inside the stand-down may now be subsumed by the wider settlement if it signs.",
  ["Al Jazeera/IRNA"], "REPORTED (deal term; no new kinetic action confirmed)")
d["last_updated"] = DATE; save("lebanon", d); CH.append("lebanon")

d = load("hezbollah")
add_signal(d,
  "Subsumed into the reported 'ceasefire on all fronts, including Lebanon' (Araghchi). No new Hezbollah rocket fire confirmed this window. Whether Hezbollah/Israel honor an all-fronts ceasefire is an open question (Israeli/Hezbollah positions on it not found this window — gap).",
  ["Al Jazeera/IRNA"], "REPORTED (deal term)")
d["last_updated"] = DATE; save("hezbollah", d); CH.append("hezbollah")

d = load("houthis")
add_signal(d,
  "Folding into the deal's all-fronts ceasefire framing; STILL zero confirmed Houthi attacks on neutral commercial shipping (Day ~105) — the oil-market wildcard trigger stays UNFIRED. No new Houthi action confirmed this window.",
  ["Al Jazeera/IRNA", "UKMTO (no new incident found)"], "no new action; trigger stays unfired")
trig_note(d, ["neutral"], "note_2026-06-12",
  "STAYS UNFIRED. Day ~105, still zero confirmed Houthi attacks on neutral shipping; folding into the reported all-fronts ceasefire.")
d["last_updated"] = DATE; save("houthis", d); CH.append("houthis")

d = load("red-sea")
add_signal(d,
  "No new neutral-vessel incident confirmed (Day ~105); the Red Sea wildcard trigger stays unfired, now potentially subsumed by the deal's all-fronts ceasefire if it signs.",
  ["UKMTO (no new incident found)"], "no new incident")
d["last_updated"] = DATE; save("red-sea", d); CH.append("red-sea")

d = load("israel")
add_signal(d,
  "Netanyahu CAUTIOUSLY SUPPORTIVE from outside the room: 'expressed appreciation' for Trump's commitment to include nuclear-material removal and an end to Iran's proxy support (CBS). Israel remains OUTSIDE the formal negotiations (benched through the US strikes) but did not reject the framework; the Israeli concern is enforcement (does Iran actually ship out the uranium), not opposition.",
  ["CBS"], "REPORTED (Netanyahu position)")
d["last_updated"] = DATE; save("israel", d); CH.append("israel")

print("NODES UPDATED:", len(CH))
print(", ".join(CH))
