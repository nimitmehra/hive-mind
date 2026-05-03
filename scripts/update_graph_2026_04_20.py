#!/usr/bin/env python3
"""Graph update for 2026-04-20 morning brief.

Inputs: staging/2026-04-20/intel.md + markets.md
Outputs: graph/nodes/*.json (updated), graph/edges.json, graph/meta.json
"""
import json, os, math
from pathlib import Path
from datetime import date, datetime

ROOT = Path('/Users/nimitmehra/Documents/Manus/hive-mind')
NODES = ROOT / 'graph' / 'nodes'
TODAY = '2026-04-20'

# ==== Helpers ===================================================================

def load(node_id):
    return json.loads((NODES / f'{node_id}.json').read_text())

def save(node_id, d):
    (NODES / f'{node_id}.json').write_text(json.dumps(d, indent=2, ensure_ascii=False))

def add_signal(d, content, sources, significance='high', date_str=TODAY):
    d['signals'].append({
        'date': date_str, 'content': content,
        'sources': sources, 'significance': significance
    })

def bump_edge(d, to, activation_inc=1, directness=None):
    """Find edge by `to`, bump activation_count, update last_activated, recompute weight."""
    for e in d.get('edges', []):
        if e['to'] == to:
            e['activation_count'] = e.get('activation_count', 0) + activation_inc
            e['last_activated'] = TODAY
            # Recompute weight per ARCHITECTURE.md formula
            freq = min(e['activation_count'], 20)
            recency = 1.0  # today => 1.0
            d_factor = {1: 3.0, 2: 1.5, 3: 1.0}.get(e.get('directness', directness or 1), 3.0)
            w = min(10, freq * recency * d_factor)
            e['weight'] = w
            return e
    return None

def set_current(d, **fields):
    d.setdefault('current', {}).update(fields)

def set_summary(d, s):
    d['summary'] = s

def touch(d):
    d['last_updated'] = TODAY

# ==== Signals (context-complete, per ARCHITECTURE.md) ===========================

SIG = {}

SIG['touska_us'] = (
    "USS SPRUANCE SEIZED IRANIAN-FLAGGED CARGO SHIP TOUSKA IN GULF OF OMAN — FIRST US-SIDE KINETIC ON AN IRANIAN FLAG UNDER THE BLOCKADE [CONFIRMED ACTION]. "
    "Sunday April 19 evening (post-evening-brief cutoff), USS Spruance (Arleigh-Burke-class DDG) intercepted the Iranian-flagged cargo vessel Touska en route to Bandar Abbas. "
    "After six hours of failed VHF warnings Spruance ordered the engine room evacuated and fired several rounds of its 5-inch Mk 45 main gun into the engine room, disabling propulsion; US Marines subsequently boarded and took custody. "
    "Trump announced the seizure via Truth Social (\"blew a hole\" in engine room); CENTCOM released a short video. Touska was already under US Treasury sanctions. "
    "Analytically load-bearing: this is the first US-side physical-kinetic interception since the blockade came into force, inverting the escalation frame from Iran-kinetic-against-commercial-shipping to US-kinetic-against-Iranian-commercial-shipping. Both sides have now demonstrated kinetic action; neither has crossed the military-on-military line. "
    "Iran's Khatam al-Anbiya joint military command (via spokesperson Ebrahim Zolfaghari on state TV) called the boarding \"armed piracy\" and pre-committed \"the Armed Forces of the Islamic Republic of Iran will soon respond and retaliate.\""
)

SIG['touska_iran'] = (
    "USS SPRUANCE SEIZURE OF IRANIAN-FLAGGED TOUSKA — IRAN'S KHATAM AL-ANBIYA PRE-COMMITS RETALIATION [CONFIRMED action by US; Iran response CONFIRMED rhetorical]. "
    "USS Spruance disabled Touska via Mk 45 naval-gun fire Sunday evening in the Gulf of Oman. Iran's Khatam al-Anbiya joint military command via spokesperson Ebrahim Zolfaghari on state TV labeled the boarding \"armed piracy\" and a \"ceasefire violation\" and declared Iran will \"soon respond and retaliate.\" "
    "IRNA carried the statement as lead Sunday evening item. This is Iran's military (not MFA, not SNSC) making an intent-to-retaliate commitment — the falsification clock for Sadjadpour's 72-hour test now runs from the Touska seizure forward. A Monday or Tuesday IRGC action would read as retaliation for Touska, not continuation of Saturday's escalation ladder."
)

SIG['round2_rejected_iran'] = (
    "IRNA FORMALLY REJECTED TRUMP'S PROPOSED ROUND 2 ISLAMABAD TALKS — CIVILIAN-LINE STATE WIRE CARRIES IRGC-REGISTER FRAMING [CONFIRMED ACTION]. "
    "Sunday afternoon Tehran time, IRNA (civilian-line state wire) formally declined the second round of US–Iran peace talks Trump had floated via Truth Social Sunday morning, citing Washington's \"maximalism and unreasonable and unrealistic demands, frequent changes of positions, constant contradictions, and the continuation of the so-called naval blockade.\" "
    "Structural significance: IRNA had previously maintained distance from Kayhan-Tasnim attack framings; Monday's Round 2 rejection shows IRNA now carrying the anti-Washington attack register, collapsing Iranian state-media toward a single hardline posture. "
    "White House official (to CNBC) confirmed Vance/Witkoff/Kushner still expected to travel to Pakistan Monday despite the rejection — asymmetric status: US delegation in motion, Iranian negotiating team publicly unavailable. Pakistan FM separately confirmed to AP that no date had been set for Round 2. "
    "Diplomatic off-ramp closes ahead of April 26 Lebanon ceasefire expiry without fallback mechanism."
)

SIG['round2_rejected_us'] = (
    "IRNA REJECTED TRUMP'S ROUND 2 PROPOSAL; VANCE/WITKOFF/KUSHNER TRAVEL TO ISLAMABAD MONDAY UNCHANGED [CONFIRMED]. "
    "Trump's Sunday-morning Truth Social proposal (\"we're offering a very fair and reasonable DEAL… if they don't, the United States is going to knock out every single Power Plant, and every single Bridge, in Iran. NO MORE MR. NICE GUY!\") was formally rejected by IRNA Sunday afternoon Tehran time. "
    "A White House official (to CNBC) confirmed Vance/Witkoff/Kushner still expected to travel to Pakistan Monday despite the rejection. Pakistan FM confirmed to AP that no Round 2 date had been set. "
    "Asymmetric posture: US delegation in motion without Iranian counterpart — the US is preserving diplomatic optics while Iran closes the off-ramp. April 26 Lebanon ceasefire expiry arrives without a fallback track."
)

SIG['waiver_iran_elapsed'] = (
    "BESSENT IRANIAN-OIL WAIVER ELAPSED 05:30 IST MONDAY; NO LAST-MINUTE EXTENSION — RUSSIAN-OIL WAIVER RENEWED (ASYMMETRIC DESIGN) [CONFIRMED ACTION]. "
    "Treasury Secretary Scott Bessent's April 15 public non-renewal declaration (\"we will not be renewing the general license on Russian oil, and we will not be renewing the general license on Iranian oil\") executed at 05:30 IST Monday on the Iran side — no extension, carve-out, or wind-down. "
    "Incremental Iranian supply to Indian refiners structurally zero from 05:30 IST onward. NUANCE versus Friday framing: the Russian waiver DID end up being RENEWED (30-day extension for India) despite Bessent's initial \"neither\" statement — The Week, Business Today, The Federal all confirm the Russian-side reversal. "
    "India's ~1.9 mbpd March Russian flow preserved. This asymmetry — Iranian non-renewal executed, Russian renewal executed — is a deliberate US policy design separating energy supply security (Russian oil continues to cushion global balance, particularly for India) from maximum-pressure sanctions on Iran's regime."
)

SIG['mea_summons_absence'] = (
    "INDIA MEA SUMMONS OF IRAN'S AMBASSADOR FATHALI — 40+ HOURS WITHOUT IRANIAN MFA RESPONSE [CONFIRMED ABSENCE]. "
    "Saturday 18:00 IST summons of Ambassador Mohammad Fathali by Foreign Secretary Misri has produced no Iranian Foreign Ministry response in 40+ hours at time of writing Monday AM. "
    "The Wire, Kashmir Reader, Deccan Chronicle, The Week (India), Open The Magazine continue to carry the summons; no Tehran statement has surfaced. Araghchi's personal X account has addressed Trump and the insurance market but has NOT specifically addressed India or the MEA concern. "
    "Fathali \"undertook to convey\" per MEA readout; no public read-back from Tehran. Load-bearing: Iran cannot produce a coherent civilian response because the civilian wing (Araghchi/Pezeshkian/MFA) is institutionally subordinate to the SNSC's Hormuz ratification, and conceding to India would require rolling back the transit-certificate regime. Touska gives Tehran a way to redirect any eventual response inside a broader US-retaliation posture without singling out India."
)

SIG['impeachment_refined_iran'] = (
    "ARAGHCHI IMPEACHMENT THREAT — NAMED MOVER IS MORTEZA MAHMOUDI (NOT AZIZI); MOTION PAUSED 'FOR WARTIME CONSIDERATIONS' [CONFIRMED statement, CLAIMED political weight]. "
    "Refines Friday/Saturday reporting: the named impeachment mover is MP Morteza Mahmoudi (not Ebrahim Azizi), who stated publicly (amplified by Iran International, Open Source Intel on X, NCRI) that Araghchi \"would have been impeached for his Twitter message\" if not for \"the excuse of war,\" accusing the FM of \"ill-timed remarks that calm global oil and energy markets.\" "
    "No motion has been tabled and one is unlikely during active war. But the Mahmoudi statement + continued Kayhan/Tasnim attacks means the parliament-state-media-IRGC triangle is now aligned against the FM. "
    "Pezeshkian has still not publicly defended Araghchi in 72+ hours — civilian-president silence is the key factional signal. Supreme Leader office silent."
)

SIG['trump_stone_age'] = (
    "TRUMP 'STONE AGE' TRUTH SOCIAL POST ON ROUND 2 OFFER + ARAGHCHI COUNTER [CONFIRMED — RHETORIC BOTH SIDES]. "
    "Trump Sunday Truth Social: \"we're offering a very fair and reasonable DEAL… if they don't, the United States is going to knock out every single Power Plant, and every single Bridge, in Iran. NO MORE MR. NICE GUY!\" — echoes his March 20 original power-plant ultimatum (which expired without kinetic follow-through). "
    "Araghchi counter via personal X account referenced \"Stone Age\" by noting \"no oil or gas being pumped back then\" — rhetorical frame positioning Iran as the ancient civilization. Analytically: Trump power-plant rhetoric has now repeated without kinetic follow-through (discount-price signal content). Araghchi engaging Trump personally from a position Kayhan/Tasnim attacked him for 72 hours earlier — factional weakness OR coordinated good-cop/bad-cop; without Pezeshkian defense, former reading has higher prior."
)

SIG['mbs_sharif_mediation'] = (
    "MBS–SHARIF JEDDAH MEETING ON US–IRAN MEDIATION ARCHITECTURE; SAUDI MOVES FROM OBSERVER TO ACTIVE CONVENER [REPORTED via Arab News; CLAIMED substance]. "
    "Crown Prince Mohammed bin Salman met Pakistan PM Shehbaz Sharif in Jeddah this week to discuss \"regional diplomacy and efforts to advance negotiations between the United States and Iran, underscoring Pakistan's role in facilitating dialogue\" (Arab News). "
    "Separately Middle East Eye reports Saudi \"pushed the US to prioritise securing a ceasefire in Lebanon in order to sustain talks with Iran, as the kingdom shifts to mediation efforts to reopen the Strait of Hormuz,\" with MBS reportedly telling Trump directly that \"a Lebanon ceasefire is critical\" to reopening Hormuz. "
    "Emerging Gulf architecture: Saudi-Pakistan axis (mediator) vs UAE hardening (Al Jaber Apr 9 position) vs Qatar neutral vs Oman silent — a four-way split. If Pakistan and Saudi are coordinated on pushing Iran back to the table, the \"Iran permanently refuses talks\" tail shrinks."
)

SIG['brent_monday_reprice'] = (
    "BRENT MONDAY ASIA CASH ~$95.42 INTRADAY (+7.9% vs FRIDAY $90.38 WIRE / +3.9% vs $91.87 yfinance) — GOLDMAN ONE-OFF CEILING BREACHED; MS FULL-CONVERGENCE NOT YET [CONFIRMED via Bloomberg, Fortune, Axios]. "
    "Sunday Globex printed $98 indicative; Monday Asia cash retraced to ~$95.42. Sits $5 below MS $100 convergence trigger; above Goldman $96-98 interim band ceiling (suggests Globex $98 was emotional overshoot, Touska treated as escalatory-not-supply-disruptive). "
    "Five-catalyst repricing stack: (1) SNSC Saturday ratification (transit cert + $1/bbl fee + civilian apex alignment), (2) Saturday IRGC kinetic broadening across VLCC/container/cruise classes, (3) USS Spruance Touska seizure Sunday, (4) IRNA Round 2 rejection Sunday, (5) Bessent Iranian waiver elapsed 05:30 IST (Russian RENEWED). "
    "Reversibility HIGH on Touska absorption + Islamabad delegation landed = $92-93 within a week; upside tail $103-110 within 3 sessions if IRGC kinetic on US Navy by Tuesday 23:59 IST."
)

SIG['ttf_monday_plus_11'] = (
    "EUROPEAN TTF GAS +11% INTRADAY MONDAY (~€41.59 → ~€46/MWh) — CLEANEST WEEKEND CASCADE SIGNAL [CONFIRMED via Bloomberg, Trading Economics]. "
    "Touska seizure + SNSC ratification + Ras Laffan 3-5yr recovery horizon on Trains 4/6 (12.8 mtpa, ~17% Qatar LNG, ~11% global helium) → LNG tanker risk premium extends on Gulf transit + replacement US Gulf/Australia LNG stretched. "
    "TTF is more crisis-levered than Henry Hub (HH +1% Friday, HH domestic pipeline isolated); TTF must absorb both Qatar loss AND Gulf transit insurance. "
    "Structural floor €45-50 (Ras Laffan partial-restart horizon); spike ceiling €60-70 if cruise-ship repeat or LNG tanker fired on. Propagates to DAX industrial input costs and European nitrogen fertilizer producers (CF Industries Europe exposure, ammonia is gas-heavy)."
)

SIG['vix_dow_futures'] = (
    "DOW FUTURES SUNDAY NIGHT -400 PTS → S&P MONDAY OPEN -0.8 TO -1.0%, NASDAQ 12-DAY WIN STREAK SNAPS [REPORTED via CNBC]. "
    "Friday April 17 close: S&P 500 7,126.06 RECORD (+1.2%); NASDAQ 24,468.48 +1.5% (12-day streak longest since 1992); Dow 49,447.43 +1.8%; VIX 17.48 (-2.6% war-era low). "
    "Monday Globex Dow futures -400 pts Sunday night on Touska + IRNA rejection + SNSC + waiver. VIX futures 19-20 handle Sunday; cash opens ~19-21 Monday. "
    "Vol-short-carry trade vulnerable: if Tuesday IST brings kinetic Iranian retaliation on US assets, VIX spikes into mid-20s on dealer re-marks. Non-crisis AI/earnings momentum (~0.7% S&P / 0.9% NASDAQ of Friday's +1.2/1.5) stickier; intraday rebound plausible absent kinetic."
)

SIG['frontline_monday'] = (
    "FRONTLINE MONDAY +2-4% EXPECTED ON AWRP RE-WIDEN; VLCC TD3C WS 126.5 WITH RATES 'LEFT REALITY BEHIND' PER LLOYD'S LIST [REPORTED]. "
    "Frontline Friday +5.6% vs Brent -9.1% = cleanest divergence of Day 52 tape; physical signal led, paper lagged. "
    "VLCC TD3C Week 4 assessed WS 126.5, daily TCE ~$112,394 standard Baltic VLCC — but Lloyd's List flagged Middle East Gulf indexes \"have left reality behind\" given Hormuz transits ~7/day vs 79/day pre-war baseline (95% reduction). Rate assessments increasingly nominal — pricing risk, not volume. "
    "Structural bid: 100% VLCC+Suezmax Hormuz-exposure-dominant; day-rates multiples of 2-year average even at suppressed volumes. The day-rate premium IS the blockade premium."
)

SIG['awrp_status'] = (
    "LLOYD'S AWRP ~1% HULL — NO SUNDAY REPUBLISH; MONDAY LONDON OPEN IS NEXT HARD TELL [REPORTED]. "
    "Lloyd's AWRP held ~1% hull through Friday despite Saturday IRGC kinetic — insurers did not step UP over the weekend. Evening brief expected Monday step to 1.5%+; morning-side data (Lloyd's List, Reinsurance News, LMA) suggests broader AWRP trend is MODERATION, with certain transits eased to 0.8-1.0% hull. "
    "Expected Monday move +20-80bps (milder than evening's +50-150bps). If Lloyd's republish prints above 1.5%, Goldman severe-tail ($115 Q4) moves to base; if holds at 1.0%, paper-traders pricing a step-up are disappointed. "
    "Crisis peak was 2.5% (60x pre-crisis 0.025-0.04%); current ~32-40x pre-war multiplier — elevated but easing."
)

SIG['cf_monday_bounce'] = (
    "CF INDUSTRIES MONDAY GAP-UP +5-8% EXPECTED; NUTRIEN +3-5% ON SNSC + TTF +11% + UREA RE-BID [REPORTED]. "
    "Friday CF -9.6% / Nutrien -5.2% was pure deal-optimism mispricing. Urea FOB ~$713/T April 16 (+16.8% 1M, +75% YoY); Profercy World Nitrogen Index 352.95 — highest since May 2022. "
    "Monday TTF +11% intraday confirms European nitrogen input-cost re-escalation (ammonia is natural-gas-heavy production → TTF spike propagates to European nitrogen producers via CF European exposure). Structural floor CF ~$105 even in full-resolution case (Ras Laffan damaged trains 3-5 yr recovery). "
    "Middle East granular urea FOB ~$410s/t (Argus post-Qatar-disruption Egypt/Algeria benchmark); global spot $702.25/T +15% 1M."
)

SIG['nifty_monday_revised'] = (
    "NIFTY MONDAY BASE -0.5 TO -1.0% (24,110-24,230) — REVISED MILDER THAN EVENING'S -1.0 TO -1.5% [REPORTED]. "
    "Driver for revision: Russian-oil waiver RENEWED (not in evening framing) preserves ~1.9 mbpd Russian flow to Indian refiners; Brent Monday cash ~$95.42 is $3-4 BELOW Globex $98 that drove evening forecasts; HDFC Bank + ICICI Bank reported Saturday April 18 (read pending). "
    "Triple headwind confirmed (not evaporating): Brent ~$95 imported-inflation tail, MEA summons political-nexus friction (40+ hrs no Iran MFA response), Iranian waiver elapsed 05:30 IST (zero marginal Iranian supply). Supportive crosscurrent: Russian-waiver renewal + potential earnings ballast. "
    "200-DMA 24,050 likely holds intraday. OMCs -1.5 to -2.5% on Brent gap; Reliance neutral (refining-margin-beneficiary vs oil-sourcing-complexity penalty)."
)

SIG['inr_monday'] = (
    "USD/INR MONDAY BASE ₹92.80-93.10 (-0.25 TO -0.55%) — RBI MACRO-PRUDENTIAL TOOLKIT CAPS OFFSHORE-SPECULATIVE TRANSMISSION [REPORTED]. "
    "Friday close ₹92.57 (-0.9% 1D rupee stronger, -0.7% 1M). Monday re-test of ₹93+ expected on Brent spike + MEA summons; break-higher trigger Brent sustains >$97 for 3 sessions → ₹93.50-94.00 intraday. "
    "Context: RBI's March 27 NOP cap ($100M vs 25% Tier-1+2) + April 1 NDF ban (no resident/NRI NDF offers) produced the single-largest 12-year rupee rally (₹95.22 → ₹93.10) without any rate move. Mechanism is macro-prudential, NOT policy-rate. "
    "Rupee more defended than equity market — opposite of 2013 taper tantrum / 2022 Russia-Ukraine. Next RBI escalation tool if ₹93.50 breaks: onshore forward ceiling or special dollar-swap window (neither deployed yet)."
)

SIG['gold_anomaly'] = (
    "GOLD DATA ANOMALY — MORNING PULL $4,819.70 -0.8% 1D vs EVENING PULL $4,879.60 +2.0% 1D; yfinance GC=F BAR REFRESH [DATA ANOMALY — UNDER RECONCILIATION]. "
    "yfinance reprinted: differential -$59.90 on close level, sign reversal on 1D delta. Likely cause: Friday late-tape reversal or Sunday Globex spillover stamped as \"1D.\" "
    "If evening +2.0% stands: regime-shift thesis holds (unexplained ~1.3% = central-bank structural accumulation on a risk-on day). If morning -0.8% stands: classical correlation works, regime-shift thesis weaker. "
    "Kitco/LBMA spot verification required; do NOT adjust `gold ← us-10y-yield` edge weights on this Friday print alone. Monday Globex $4,820-4,880 range Sunday evening per Kitco/Bloomberg; Monday cash $4,860+ re-asserts regime shift, $4,800-4,820 confirms classical view."
)

SIG['houthis_day_55'] = (
    "HOUTHIS DAY 55 OF NON-MIRRORING — NO RED SEA OR BAB-EL-MANDEB KINETIC AFTER IRAN SATURDAY OR TOUSKA SUNDAY [CONFIRMED ABSENCE]. "
    "Deputy information minister Mansour's conditional framing (\"closing Bab al-Mandeb is among our options\" if \"any Gulf state becomes directly involved\") has not fired — no Gulf state directly joined US kinetic action. MARAD 2026-006 advisory remains active as standing posture, not a new advisory. "
    "Soufan coordination thesis WEAKER by elapsed time: the `houthis → shipping-tankers` edge step below 9.0 becomes more defensible with each quiet day. But Touska is a US-side action Houthis could plausibly use as trigger pretext in coming days — test window extends rather than shrinks. "
    "Edge step DEFERRED Monday pending Tuesday IST evaluation."
)

SIG['lebanon_day_4'] = (
    "LEBANON CEASEFIRE DAY 4 — KALFON IED FATALITY DETAILS UNCHANGED; NO IDF RETALIATION; HEZBOLLAH KINETIC RESTRAINT HOLDS [CONFIRMED]. "
    "Kalfon (Warrant Officer Barak Kalfon, 226th Reserve Paratroopers Brigade, killed in Jebbayn) remains the only Israeli fatality under the 10-day ceasefire. Defense Minister Katz's Sunday tribute (\"brave and dedicated fighter… devoted family man… engineer at Rafael\") surfaced with no IDF retaliatory strike. "
    "Hezbollah SG Qassem Sunday speech called the ceasefire \"an insult to Lebanon\" — RHETORIC only, no rockets. Structural reading holds at Day 4: low-signature kinetic permitted + escalatory rhetoric permitted + open rocket war withheld. "
    "Ceasefire fragility unchanged (Hezbollah non-signatory, IDF in-country, no withdrawal). April 26 expiry in 6 days."
)

SIG['ras_laffan_unchanged'] = (
    "RAS LAFFAN PARTIAL-RESTART TIMELINE UNCHANGED MONDAY — NORTH SITE WITHIN A MONTH, SOUTH BY LATE SUMMER [CONFIRMED]. "
    "QatarEnergy CEO Al-Kaabi's April 9 framework (via The National, OilPrice.com) has no Monday update. Trains 4 & 6 ~12.8 mtpa (~17% Qatar LNG exports) offline 3-5 years. Helium impact: ~11% of global supply at risk (AGBI; Fortune reports 35% of market), ~30% of Qatar volumes. "
    "No Intel/TSMC/Samsung allocation notice Sunday/Monday AM; helium → semiconductor cascade stays at watching. TTF likely absorbs partial-restart horizon as structural floor €45-50."
)

SIG['uae_correction'] = (
    "CORRECTION TO EVENING BRIEF: AL JABER HORMUZ DECLARATION IS APRIL 9 ADNOC POSITION, NOT A NEW SUNDAY STATEMENT [CONFIRMED via Gulf Business, The National, Al Arabiya, ADNOC press release]. "
    "The evening brief framed Al Jaber's \"not open and needs to be open unconditionally\" language as \"new Sunday declaration\" and bumped `uae → strait-of-hormuz` edge 7.0 → 8.0 on \"first UAE on-record public hardening.\" "
    "Verification shows the language traces to April 9 ADNOC interviews (Gulf Business, Al Arabiya, CNBC, The National, AGBI, CGTN on that date). The UAE posture going into Monday is the same April 9 position — 10-day continuity, not a fresh step-up. "
    "Edge weight stands on consistently hardened position, but the proximate phantom-Sunday reason does not survive verification. Graph history should reflect continuity, not step-up."
)

SIG['shipping_us_kinetic'] = (
    "USS SPRUANCE KINETIC ON COMMERCIAL-FLAGGED VESSEL — FIRST US-SIDE KINETIC-ON-IRANIAN-FLAG UNDER BLOCKADE [CONFIRMED ACTION]. "
    "USS Spruance disabled Iranian-flagged cargo vessel Touska in Gulf of Oman Sunday evening via Mk 45 naval-gun fire after 6 hours of failed VHF warnings. First use of live ordnance on an Iranian-flagged vessel in international waters by US under the blockade. "
    "Commercial-shipping threat surface now includes both IRGC-side kinetic (VLCC / container / cruise-ship targeting Saturday) AND US-side kinetic (Touska) — bi-directional risk. Insurance implications: AWRP models previously assumed Iran-side risk premium; now require US-side kinetic risk premium on Iranian-flagged commercial vessels. "
    "VLCC/Suezmax rate assessments remain elevated against 95% transit reduction."
)

# ==== Node updates ==============================================================

updates_log = {}  # for changelog later

# ---------------------------------------------------------------------- IRAN
n = load('iran')
add_signal(n, SIG['touska_iran'], ['Trump Truth Social', 'CNBC (Jeff Cox)', 'Naval News', 'CNN live blog', 'Al Jazeera', 'IRNA'], 'high')
add_signal(n, SIG['round2_rejected_iran'], ['IRNA (via CNBC translation)', 'Al Jazeera live blog', 'Irish Times', 'CBS News live', 'CNBC (White House official)'], 'high')
add_signal(n, SIG['waiver_iran_elapsed'], ['Business Today', 'The Week', 'The Federal', 'Atlantic Council dispatch', 'Bloomberg (Apr 15)'], 'high')
add_signal(n, SIG['mea_summons_absence'], ['The Wire', 'Kashmir Reader', 'Deccan Chronicle', 'The Week (India)', 'Open The Magazine', 'IRNA (silence CONFIRMED)'], 'high')
add_signal(n, SIG['impeachment_refined_iran'], ['Iran International', 'Caliber.Az', 'Open Source Intel (@Osint613)', 'NCRI'], 'medium')
add_signal(n, SIG['trump_stone_age'], ['Trump Truth Social', 'The Hill', 'Al Jazeera', 'CBS Face the Nation (Araghchi)'], 'medium')
add_signal(n, (
    "IRANIAN MEDIA TONE — COORDINATED-ESCALATORY (UP FROM 'DECISIVELY ESCALATORY') [SOURCE TONE ASSESSMENT]. "
    "Monday AM state-media set more coordinated than any point in 10 days: IRNA leading with Round 2 rejection — the civilian-line wire now carrying anti-Washington \"maximalism/contradictions\" framing previously a Tasnim/Fars register. "
    "State-media map a week ago was IRNA (moderate) vs Tasnim/Fars/Kayhan (attack); today the entire map has moved toward IRNA carrying IRGC-register language. Zolfaghari's \"armed piracy… will respond and retaliate\" amplified uniformly. "
    "Araghchi's personal X remains the ONE heterodox voice. If Pezeshkian stays silent through Monday evening, factional collapse confirmed as new baseline."
), ['Iranian state-media corpus: IRNA, Tasnim, Fars, Kayhan'], 'high')
bump_edge(n, 'united-states')
bump_edge(n, 'strait-of-hormuz')
bump_edge(n, 'brent-crude')
bump_edge(n, 'russia')
bump_edge(n, 'pakistan')
n.setdefault('trigger_points', []).append({
    'condition': 'Iran executes kinetic action on US Navy vessel, US-flagged commercial vessel, or US base by Tuesday 23:59 IST 2026-04-21 (Sadjadpour post-Touska falsifiable)',
    'cascade': ['united-states', 'brent-crude', 'strait-of-hormuz', 'marine-war-risk-insurance', 'sp-500'],
    'mechanism': "Iran's Khatam al-Anbiya via Zolfaghari pre-committed retaliation for the Touska seizure. Falsification window ends Tuesday 23:59 IST — absence = absorption branch (escalation stabilizes at new step); presence = ceasefire breaks formally before April 26 expiry. Iranian kinetic on US asset would trigger Brent $103-110 within 3 sessions, AWRP step to 2.5%+, dated Brent $140+.",
    'added': TODAY,
    'status': 'watching'
})
set_summary(n, (
    "Day 53 Monday morning. TOUSKA SEIZURE INVERTS ESCALATION FRAME — US NOW KINETIC ON IRANIAN-FLAGGED COMMERCIAL VESSEL; IRAN'S KHATAM AL-ANBIYA PRE-COMMITS RETALIATION. "
    "USS Spruance disabled Iranian cargo vessel Touska in Gulf of Oman Sunday evening via Mk 45 fire after 6 hrs of failed VHF warnings — first US-side physical-kinetic interception under the blockade. "
    "IRNA (civilian-line wire, now carrying IRGC-register framing) formally rejected Trump's proposed Round 2 Islamabad talks Sunday citing Washington's \"maximalism and unreasonable demands.\" "
    "Bessent Iranian-oil waiver elapsed 05:30 IST Monday (confirmed non-renewal); Russian-oil waiver RENEWED (30-day India extension) — asymmetric US policy design. "
    "India MEA summons of Ambassador Fathali has produced no Iranian MFA response 40+ hrs — Tehran cannot produce a coherent civilian reply because civilian wing subordinate to SNSC's Hormuz ratification. "
    "Mahmoudi named as impeachment mover for Araghchi (not Azizi); motion paused \"for wartime.\" Pezeshkian silent 72+ hrs; Supreme Leader office silent. Iranian state-media tone COORDINATED-ESCALATORY — IRNA now carrying anti-Washington register. "
    "Sadjadpour 72-hr falsifiable test re-framed around Touska: window runs Monday→Tuesday 23:59 IST; absence = absorption branch, presence = ceasefire breaks formally before April 26."
))
touch(n)
save('iran', n)
updates_log['iran'] = {'signals': 7, 'edges_bumped': ['united-states', 'strait-of-hormuz', 'brent-crude', 'russia', 'pakistan'], 'new_trigger': 'Iran kinetic on US asset by Tue 23:59 IST (Sadjadpour post-Touska)', 'summary_refreshed': True}

# ---------------------------------------------------------------------- UNITED STATES
n = load('united-states')
add_signal(n, SIG['touska_us'], ['Trump Truth Social', 'CNBC (Jeff Cox)', 'Naval News', 'CNN live blog', 'Al Jazeera', 'NPR', 'Daily Caller (CENTCOM video)'], 'high')
add_signal(n, SIG['round2_rejected_us'], ['IRNA (via CNBC)', 'CNBC (White House official)', 'AP (Pakistan FM)', 'CBS News live', 'Al Jazeera'], 'high')
add_signal(n, SIG['waiver_iran_elapsed'], ['Business Today', 'The Week', 'The Federal', 'Atlantic Council dispatch', 'Bloomberg'], 'high')
add_signal(n, SIG['trump_stone_age'], ['Trump Truth Social', 'The Hill', 'Al Jazeera', 'CBS Face the Nation'], 'medium')
add_signal(n, SIG['mbs_sharif_mediation'], ['Arab News', 'Middle East Eye', 'Al Jazeera'], 'medium')
add_signal(n, (
    "US MEDIA BIFURCATED WITH RIGHT-MEDIA FIRST ACCESS ON TOUSKA [SOURCE TONE ASSESSMENT]. "
    "Trump's Touska announcement ran FIRST through Daily Caller with CENTCOM video, then Fox, before mainstream wires (CNN, NBC, NPR, Al Jazeera) picked it up — clear Fox-first administration briefing pattern on kinetic action. "
    "Framing split: Daily Caller/Fox emphasize Trump strength (\"Blowing A Hole In Engine Room\") vs CNN/NBC/NPR framing as escalation that \"throws a fragile ceasefire into question\" — NPR emphasizing Iran piracy accusation + Round 2 collapse. "
    "Matters for Monday tape: right-media = blockade-vindication; mainstream = ceasefire-endangerment. For Indian FIIs and European institutional flows, mainstream framing controls (more negative for risk)."
), ['Daily Caller', 'Fox News', 'CNN', 'NBC', 'NPR', 'Al Jazeera', 'WSJ', 'Bloomberg', 'Axios'], 'medium')
bump_edge(n, 'iran')
bump_edge(n, 'brent-crude')
bump_edge(n, 'pakistan')
bump_edge(n, 'trump')
set_summary(n, (
    "Day 53 Monday morning. US EXECUTES FIRST KINETIC ON IRANIAN-FLAGGED VESSEL UNDER BLOCKADE; RUSSIAN WAIVER RENEWED (ASYMMETRIC POLICY) WHILE IRANIAN WAIVER ELAPSED. "
    "USS Spruance intercepted Iranian-flagged cargo Touska in Gulf of Oman Sunday evening; disabled via Mk 45 naval-gun fire after 6 hrs of failed VHF warnings; Marines boarded and took custody. Trump announced via Truth Social. First US-side physical-kinetic interception under blockade; symmetric threshold crossed from US side (Iran-kinetic-on-commercial vs US-kinetic-on-commercial), neither yet military-on-military. "
    "Trump Sunday Truth Social \"Stone Age\" threat on power plants + bridges (echoes March 20 ultimatum that expired) + \"NO MORE MR. NICE GUY!\" framing. IRNA rejected Round 2 Sunday; Vance/Witkoff/Kushner still expected to travel to Pakistan Monday per WH official. "
    "Bessent Iranian-oil waiver executed non-renewal 05:30 IST Monday; Russian-oil waiver RENEWED (30-day India extension) — deliberate asymmetric policy separating energy supply security (Russia) from maximum-pressure on Iran. "
    "Right-media first access to administration on Touska (Daily Caller/Fox before CNN/NBC/NPR); bifurcated framing. MBS-Sharif Jeddah meeting moves Saudi to active convener-mediator on US-Iran track."
))
touch(n)
save('united-states', n)
updates_log['united-states'] = {'signals': 6, 'edges_bumped': ['iran', 'brent-crude', 'pakistan', 'trump'], 'summary_refreshed': True}

# ---------------------------------------------------------------------- IRGC
n = load('irgc')
add_signal(n, (
    "KHATAM AL-ANBIYA JOINT MILITARY COMMAND (ZOLFAGHARI) PRE-COMMITS RETALIATION FOR TOUSKA SEIZURE [CONFIRMED STATEMENT, RHETORIC]. "
    "Iran's Khatam al-Anbiya joint military command via spokesperson Ebrahim Zolfaghari on state TV labeled USS Spruance's disabling of Touska \"armed piracy\" and a \"ceasefire violation,\" declaring \"the Armed Forces of the Islamic Republic of Iran will soon respond and retaliate.\" "
    "IRNA carried as Sunday evening lead. First pre-committed retaliation intent from Iran's military (NOT MFA, NOT SNSC) since crisis start. Sadjadpour 72-hr falsifiable test re-anchored: window runs from Touska forward, clock at ~60 hrs Monday AM; Tuesday 23:59 IST is the evaluation point."
), ['IRNA', 'Al Jazeera', 'ANI', 'BNO News', 'Naval News'], 'high')
add_signal(n, (
    "NO NEW IRGC KINETIC IN 36+ HRS SINCE TOUSKA; NO NEW UKMTO ADVISORY SINCE SATURDAY 038-26 [CONFIRMED ABSENCE]. "
    "Sadjadpour 72-hr test at ~60-hr mark with no new IRGC commercial-vessel fire. UKMTO no new advisory since 038-26 on container projectile Saturday. JMIC Sunday feed empty for Gulf-waters incidents. "
    "On narrow falsifiable terms, \"warning-shot-for-leverage\" branch still winning at 60-hr mark. Frame inverted: research question now is \"will Iran retaliate against US-side escalation\" not \"will Iran escalate further.\""
), ['UKMTO advisory log', 'JMIC feed', 'Hormuz Strait Monitor'], 'high')
bump_edge(n, 'united-states')
bump_edge(n, 'strait-of-hormuz')
bump_edge(n, 'shipping-tankers')
set_summary(n, (
    "Day 53 Monday AM. KHATAM AL-ANBIYA JOINT MIL COMMAND PRE-COMMITS RETALIATION FOR TOUSKA. "
    "Iran's military (Zolfaghari via state TV) declared \"will respond and retaliate\" for USS Spruance's disabling of Touska Sunday evening — first military pre-commitment since crisis start. "
    "IRGC commercial-vessel kinetic at ~60-hr absence since Saturday's gunboat burst (Sadjadpour 72-hr test re-anchored around Touska: clock runs forward to Tuesday 23:59 IST). "
    "SNSC transit-certificate regime ($1/bbl loaded-tanker fee, military + hostile vessels denied, Oman partnered on collection) executed since Saturday. Factional collapse into hardline SNSC posture holds — Araghchi remains sole heterodox voice. "
    "Soufan coordination thesis weaker: Houthis Day 55 non-mirroring despite Touska."
))
touch(n)
save('irgc', n)
updates_log['irgc'] = {'signals': 2, 'edges_bumped': ['united-states', 'strait-of-hormuz', 'shipping-tankers'], 'summary_refreshed': True}

# ---------------------------------------------------------------------- STRAIT OF HORMUZ
n = load('strait-of-hormuz')
add_signal(n, (
    "USS SPRUANCE KINETIC INTERCEPTION OF IRANIAN-FLAGGED TOUSKA IN GULF OF OMAN — FIRST US-SIDE KINETIC UNDER BLOCKADE [CONFIRMED]. "
    "USS Spruance disabled Iranian-flagged cargo Touska in the Gulf of Oman Sunday evening via Mk 45 main-gun fire. Crosses symmetric kinetic threshold from US side. "
    "Both sides have now demonstrated kinetic action on commercial-flagged vessels; neither has crossed military-on-military line. Transit data: AIS shipping continues at ~1-2% pre-war baseline (95% reduction); 3 diversions out of ~30 daily = 10% diversion, not closure. Physical closure trigger UNCHANGED — transits are suppressed but NOT zero."
), ['Naval News', 'CENTCOM video', 'Hormuz Strait Monitor', 'UKMTO'], 'high')
add_signal(n, SIG['brent_monday_reprice'], ['Bloomberg', 'Fortune', 'Axios', 'Investing.com'], 'high')
add_signal(n, SIG['uae_correction'], ['Gulf Business', 'The National (Abu Dhabi)', 'Al Arabiya', 'ADNOC press release'], 'medium')
add_signal(n, SIG['mbs_sharif_mediation'], ['Arab News', 'Middle East Eye', 'Al Jazeera'], 'medium')
bump_edge(n, 'brent-crude')
bump_edge(n, 'iran')
bump_edge(n, 'united-states')
touch(n)
save('strait-of-hormuz', n)
updates_log['strait-of-hormuz'] = {'signals': 4, 'edges_bumped': ['brent-crude', 'iran', 'united-states']}

# ---------------------------------------------------------------------- SHIPPING TANKERS
n = load('shipping-tankers')
add_signal(n, SIG['shipping_us_kinetic'], ['Naval News', 'CENTCOM', 'CNN', 'Al Jazeera'], 'high')
add_signal(n, SIG['frontline_monday'], ['Baltic Exchange Week 4', "Lloyd's List"], 'high')
add_signal(n, SIG['houthis_day_55'], ['MARAD 2026-006', 'Reuters', 'TWZ'], 'medium')
add_signal(n, (
    "BRENT MONDAY +7.9% INTRADAY ON TOUSKA STACK; FRONTLINE MONDAY EXPECTED +2-4% ON AWRP RE-WIDEN [REPORTED]. "
    "Frontline Friday +5.6% vs Brent -9.1% = cleanest divergence of Day 52 — physical signal LED paper. Monday reverse confirms physical as leading indicator. "
    "Propose shipping-tankers → brent-crude as LEADING edge (not lagging) per markets.md F1."
), ['Bloomberg', 'Fortune', 'Axios', 'Baltic Exchange'], 'high')
bump_edge(n, 'brent-crude')
bump_edge(n, 'marine-war-risk-insurance')
bump_edge(n, 'strait-of-hormuz')
set_current(n,
    price='VLCC TD3C WS 126.5, TCE ~$112,394/day; Frontline $37.13 (Fri); BOAT ETF $41.33 (Fri)',
    delta_1d='Frontline +5.6% Fri; Monday +2-4% expected',
    delta_1m='Frontline +15.5%; BOAT +3.1%',
    delta_3m='Frontline +47.8%; BOAT +25.5%'
)
set_summary(n, (
    "Day 53 Monday AM. US KINETIC NOW BI-DIRECTIONAL ON COMMERCIAL-FLAGGED VESSELS: USS SPRUANCE DISABLED IRANIAN-FLAGGED TOUSKA VIA MK 45 FIRE SUNDAY, FIRST US-SIDE KINETIC UNDER BLOCKADE. "
    "Commercial-shipping threat surface now includes IRGC-side kinetic (VLCC/container/cruise Saturday) AND US-side kinetic (Touska Sunday). Insurance implications: AWRP models must now include US-side kinetic risk premium on Iranian-flagged vessels. "
    "VLCC TD3C Week 4 WS 126.5 / TCE ~$112,394 — rates \"left reality behind\" per Lloyd's List given Hormuz transits 95% below pre-war (7/day vs 79/day). Frontline +5.6% Fri vs Brent -9.1% = physical leading paper; Monday expected +2-4% on AWRP re-widen. "
    "Houthis Day 55 quiet despite Touska — Mansour conditional doctrine not triggered; edge step below 9.0 DEFERRED pending Tuesday IST."
))
touch(n)
save('shipping-tankers', n)
updates_log['shipping-tankers'] = {'signals': 4, 'edges_bumped': ['brent-crude', 'marine-war-risk-insurance', 'strait-of-hormuz'], 'summary_refreshed': True}

# ---------------------------------------------------------------------- BRENT CRUDE
n = load('brent-crude')
add_signal(n, SIG['brent_monday_reprice'], ['Bloomberg', 'Fortune', 'Axios', 'Investing.com', 'Trading Economics'], 'high')
add_signal(n, SIG['waiver_iran_elapsed'], ['Business Today', 'The Week', 'The Federal', 'Atlantic Council', 'Bloomberg'], 'high')
add_signal(n, SIG['awrp_status'], ["Lloyd's List", 'Reinsurance News', 'LMA', 'IBTimes'], 'medium')
add_signal(n, (
    "$20B FROZEN-FUNDS-FOR-URANIUM WIRE CLAIM — TREAT AS CLAIMED, POTENTIAL SEED-AND-AMPLIFY PATTERN [REPORTED wire-chain, anonymous sources]. "
    "Multiple oil-market wires reported Fri/Sat that \"the US may release $20 billion in frozen Iranian funds in exchange for enriched uranium stockpiles\" (cited by TradingEconomics, specialist aggregators). "
    "First specific number attached to frozen-funds concession in current round — prior framework was $6B from 2023 Biden-era hostage deal plus South Korean/Iraqi holdings. "
    "Single-chain reporting with respect to the specific $20B, attributed to \"sources\" without named US/Iran official. Classic seed-and-amplify risk pattern. Treat CLAIMED pending named-sourced confirmation. "
    "Either Washington is offering more than prior rounds (so IRNA rejection inconsistent) or the $20B figure was leaked by US to make Iran refusal look unreasonable (information operation)."
), ['TradingEconomics Brent commentary', 'specialist market aggregators'], 'low')
bump_edge(n, 'strait-of-hormuz')
bump_edge(n, 'iran')
n.setdefault('price_snapshots', []).append({
    'date': TODAY,
    'price': '~$95.42 Monday Asia intraday; Sunday Globex $98 indicative',
    'trigger': 'Touska seizure + SNSC ratification + IRNA Round 2 rejection + Bessent Iranian waiver elapsed + Saturday IRGC kinetic broadening',
    'delta_context': '+7.9% vs Friday wire $90.38 (+3.9% vs yfinance $91.87). Breaches Goldman one-off ceiling; below MS $100 full-convergence trigger. Interim mixed-conviction settle.'
})
set_current(n,
    price='~$95.42 Monday Asia intraday (wire); Sunday Globex $98 indicative; Friday close $91.87 yfinance / $90.38 wire-ICE',
    delta_1d='+7.9% vs Friday wire (Monday intraday); +3.9% vs yfinance Fri',
    delta_1m='-15.8% (Friday settle basis)',
    delta_3m='+41.5%'
)
set_summary(n, (
    "Day 53 Monday AM. MONDAY ASIA CASH ~$95.42 (+7.9% vs FRIDAY WIRE $90.38) — GOLDMAN ONE-OFF CEILING BREACHED; MS FULL-CONVERGENCE NOT YET. "
    "Sunday Globex printed $98 indicative (MS thesis at upper edge); Monday Asia cash retraced to ~$95.42 — below Goldman $96-98 interim band, suggests Globex overshoot was emotional and Touska treated as escalatory-not-supply-disruptive. "
    "Five-catalyst repricing stack: (1) SNSC Saturday ratification (transit cert + $1/bbl fee + civilian apex alignment); (2) Saturday IRGC kinetic across VLCC/container/cruise; (3) USS Spruance Touska seizure Sunday; (4) IRNA Round 2 rejection Sunday; (5) Bessent Iranian waiver elapsed 05:30 IST (Russian RENEWED — asymmetric). "
    "Reversibility HIGH on Touska absorption + Islamabad delegation landed → $92-93 within a week; upside tail $103-110 within 3 sessions if IRGC kinetic on US Navy by Tuesday 23:59 IST. Pre-crisis floor $80-82. "
    "$20B frozen-funds-for-uranium wire claim CLAIMED pending named sourcing — potential info-op."
))
touch(n)
save('brent-crude', n)
updates_log['brent-crude'] = {'signals': 4, 'edges_bumped': ['strait-of-hormuz', 'iran'], 'price_snapshot_added': True, 'summary_refreshed': True}

# ---------------------------------------------------------------------- MARINE WAR RISK INSURANCE
n = load('marine-war-risk-insurance')
add_signal(n, SIG['awrp_status'], ["Lloyd's List", 'Reinsurance News', 'LMA', 'IBTimes', 'Insurance Journal'], 'high')
add_signal(n, SIG['shipping_us_kinetic'], ['Naval News', 'CENTCOM', 'CNN'], 'medium')
bump_edge(n, 'brent-crude')
bump_edge(n, 'shipping-tankers')
set_summary(n, (
    "Day 53 Monday AM. AWRP ~1% HULL THROUGH FRIDAY; NO SUNDAY REPUBLISH; MONDAY LONDON OPEN IS NEXT HARD TELL. "
    "Lloyd's AWRP held ~1% through Friday despite Saturday IRGC kinetic broadening — insurers did NOT step up over the weekend. Broader Lloyd's List/LMA trend is MODERATION, with certain transits at 0.8-1.0% hull. "
    "Monday expected +20-80bps (milder than evening brief's +50-150bps). If Monday republish >1.5%, Goldman severe-tail ($115 Q4) moves to base; if ≤1.0%, paper-traders pricing step-up disappointed. "
    "Crisis peak 2.5% (60x pre-crisis 0.025-0.04%); current ~32-40x — elevated but easing. USS Spruance Touska kinetic introduces US-side risk premium on Iranian-flagged commercial vessels (bi-directional AWRP modeling required)."
))
touch(n)
save('marine-war-risk-insurance', n)
updates_log['marine-war-risk-insurance'] = {'signals': 2, 'edges_bumped': ['brent-crude', 'shipping-tankers'], 'summary_refreshed': True}

# ---------------------------------------------------------------------- TRUMP
n = load('trump')
add_signal(n, (
    "TRUMP TRUTH SOCIAL SUNDAY MORNING 'STONE AGE' POST ON ROUND 2 OFFER [CONFIRMED — RHETORIC]. "
    "\"we're offering a very fair and reasonable DEAL… if they don't, the United States is going to knock out every single Power Plant, and every single Bridge, in Iran. NO MORE MR. NICE GUY!\" — echoes March 20 original power-plant ultimatum (which expired without kinetic follow-through). "
    "IRNA formally rejected Round 2 Sunday afternoon citing \"maximalism\"; Araghchi countered via personal X account noting \"no oil or gas being pumped back then\" (Stone Age reference). "
    "Rhetorical pattern: Trump power-plant threats have now repeated without kinetic follow-through = discount-price signal content."
), ['Trump Truth Social', 'The Hill', 'Al Jazeera', 'CBS Face the Nation'], 'medium')
add_signal(n, (
    "TRUMP ANNOUNCED USS SPRUANCE SEIZURE OF TOUSKA VIA TRUTH SOCIAL (\"BLEW A HOLE\" IN ENGINE ROOM) [CONFIRMED ACTION + RHETORIC]. "
    "Sunday evening post followed CENTCOM video release of Mk 45 firing sequence. Right-media first access (Daily Caller before Fox before mainstream wires) — administration briefed right-media channels ahead of CNN/NBC/NPR on kinetic action. "
    "First live-ordnance US action against an Iranian-flagged commercial vessel under the blockade; Trump owns the escalation on the public record."
), ['Trump Truth Social', 'Daily Caller', 'Fox News', 'CNN', 'NPR'], 'high')
bump_edge(n, 'iran')
set_summary(n, (
    "Day 53 Monday AM. TRUMP OWNS TOUSKA KINETIC + 'STONE AGE' RHETORIC; RIGHT-MEDIA FIRST ACCESS. "
    "Sunday Truth Social sequence: morning \"Stone Age\" threat on power plants + bridges (echoes March 20 ultimatum); afternoon IRNA rejected Round 2; evening Trump announced Touska seizure (\"blew a hole\"). "
    "USS Spruance disabled Iranian-flagged cargo Touska in Gulf of Oman via Mk 45 fire after 6 hrs failed VHF warnings. Right-media first access (Daily Caller with CENTCOM video before Fox before mainstream). "
    "Bessent Iranian-oil waiver executed non-renewal 05:30 IST Monday; Russian-oil waiver RENEWED — asymmetric US policy. Vance/Witkoff/Kushner still expected to travel to Pakistan Monday per WH despite IRNA rejection."
))
touch(n)
save('trump', n)
updates_log['trump'] = {'signals': 2, 'edges_bumped': ['iran'], 'summary_refreshed': True}

# ---------------------------------------------------------------------- PAKISTAN
n = load('pakistan')
add_signal(n, (
    "PAKISTAN FM CONFIRMED TO AP NO DATE SET FOR US-IRAN ROUND 2 AFTER IRNA REJECTION [CONFIRMED]. "
    "Pakistan's Foreign Ministry confirmed to AP that no date had been set for Round 2, following IRNA's Sunday afternoon formal rejection of Trump's proposed Islamabad talks. "
    "White House official (to CNBC) confirmed Vance/Witkoff/Kushner still expected to travel to Pakistan Monday despite rejection — asymmetric posture: US delegation in motion without Iranian counterpart."
), ['AP', 'CNBC', 'IRNA'], 'high')
add_signal(n, SIG['mbs_sharif_mediation'], ['Arab News', 'Middle East Eye', 'Al Jazeera'], 'high')
bump_edge(n, 'iran')
bump_edge(n, 'united-states')
bump_edge(n, 'saudi-arabia')
set_summary(n, (
    "Day 53 Monday AM. PAKISTAN HOLDS MEDIATOR ROLE DESPITE IRNA REJECTION OF ROUND 2; SAUDI ARCHITECTURE NOW OVERLAYS. "
    "IRNA formally rejected Trump's proposed Monday Islamabad Round 2 Sunday; Pakistan FM confirmed to AP no date set. Vance/Witkoff/Kushner still travel to Pakistan Monday per WH official (asymmetric — US delegation in motion, Iranian team publicly unavailable). "
    "MBS-Sharif Jeddah meeting this week on US-Iran mediation architecture; Saudi moves from observer to active convener-mediator — emerging Saudi-Pakistan axis alongside Pakistan's host-mediator role. "
    "Four-way Gulf split: Saudi-Pakistan mediator / UAE hardening (Al Jaber Apr 9 position) / Qatar neutral / Oman silent."
))
touch(n)
save('pakistan', n)
updates_log['pakistan'] = {'signals': 2, 'edges_bumped': ['iran', 'united-states', 'saudi-arabia'], 'summary_refreshed': True}

# ---------------------------------------------------------------------- VANCE
n = load('vance')
add_signal(n, (
    "VANCE/WITKOFF/KUSHNER STILL EXPECTED TO TRAVEL TO PAKISTAN MONDAY DESPITE IRNA REJECTION [CONFIRMED via WH official to CNBC]. "
    "White House official confirmed to CNBC that VP Vance, Witkoff, and Kushner remain on the Monday travel manifest despite IRNA's Sunday afternoon formal rejection of Round 2. "
    "Asymmetric status: US delegation in motion, Iranian negotiating team publicly unavailable. No public flight manifest released — Vance-led team travel is WH-official-on-background rather than public departure."
), ['CNBC (White House official)', 'AP', 'CBS News live'], 'high')
bump_edge(n, 'pakistan')
touch(n)
save('vance', n)
updates_log['vance'] = {'signals': 1, 'edges_bumped': ['pakistan']}

# ---------------------------------------------------------------------- INDIA
n = load('india')
add_signal(n, SIG['mea_summons_absence'], ['The Wire', 'Kashmir Reader', 'Deccan Chronicle', 'The Week (India)', 'Open The Magazine'], 'high')
add_signal(n, SIG['waiver_iran_elapsed'], ['Business Today', 'The Week', 'The Federal', 'Atlantic Council', 'Bloomberg'], 'high')
add_signal(n, SIG['nifty_monday_revised'], ['Business Standard', 'Livemint', 'Economic Times', 'Moneycontrol'], 'high')
bump_edge(n, 'iran')
bump_edge(n, 'russia')
bump_edge(n, 'united-states')
bump_edge(n, 'brent-crude')
set_summary(n, (
    "Day 53 Monday AM. INDIA POSITION — MEA SUMMONS ABSENCE (40+ HRS NO IRAN MFA RESPONSE) + RUSSIAN WAIVER RENEWED + IRANIAN WAIVER ELAPSED (ASYMMETRIC US POLICY). "
    "MEA summons of Iran's Ambassador Fathali Saturday produced no Iranian MFA response 40+ hrs — Tehran cannot produce coherent civilian reply because civilian wing subordinate to SNSC Hormuz ratification; Touska gives Iran pretext to redirect. "
    "Bessent Iranian-oil waiver elapsed 05:30 IST Monday (zero marginal Iranian supply to Indian refiners); Russian-oil waiver RENEWED (30-day extension) preserves ~1.9 mbpd Russian flow — material positive vs evening framing. "
    "Nifty Monday revised base -0.5 to -1.0% (24,110-24,230) from evening's -1.0 to -1.5% on (a) Russian-waiver renewal, (b) Brent ~$95 (not $100+), (c) HDFC/ICICI Bank April 18 earnings pending read. 200-DMA 24,050 likely holds intraday. "
    "Triple-headwind confirmed (not evaporating): Brent $95 imported-inflation mild-tail, MEA summons friction, Iranian waiver elapsed. Rupee more defended than equity (RBI macro-prudential toolkit already deployed)."
))
touch(n)
save('india', n)
updates_log['india'] = {'signals': 3, 'edges_bumped': ['iran', 'russia', 'united-states', 'brent-crude'], 'summary_refreshed': True}

# ---------------------------------------------------------------------- RUSSIA
n = load('russia')
add_signal(n, (
    "US TREASURY RENEWED RUSSIAN-OIL WAIVER (30-DAY EXTENSION FOR INDIA) DESPITE BESSENT 'NEITHER' LANGUAGE; ~1.9 MBPD INDIAN REFINER FLOW PRESERVED [CONFIRMED]. "
    "Bessent April 15 public statement: \"we will not be renewing the general license on Russian oil, and we will not be renewing the general license on Iranian oil.\" Iranian side executed non-renewal 05:30 IST Monday; Russian side DID end up being RENEWED (30-day extension specific to India). "
    "The Week, Business Today, The Federal all confirm Russian-side reversal. ~1.9 mbpd Russian flow to Indian refiners preserved (March baseline). "
    "Asymmetric US policy design: Iranian non-renewal = maximum pressure on regime; Russian renewal = preserving energy supply security for global balance + Indian strategic partner. Russia has shown no appetite to publicly broker on Iran's behalf despite position."
), ['The Week', 'Business Today', 'The Federal', 'Atlantic Council dispatch'], 'high')
bump_edge(n, 'india')
bump_edge(n, 'united-states')
bump_edge(n, 'iran')
set_summary(n, (
    "Day 53 Monday AM. RUSSIAN-OIL WAIVER RENEWED (30-DAY INDIA EXTENSION) DESPITE BESSENT 'NEITHER' LANGUAGE — ASYMMETRIC US POLICY PRESERVES ~1.9 MBPD RUSSIAN FLOW TO INDIA. "
    "Iranian side executed non-renewal 05:30 IST Monday; Russian side RENEWED by Treasury (30-day extension specific to India). Deliberate asymmetry: maximum pressure on Iran's regime + energy supply security for global balance + Indian strategic partner preserved. "
    "Russia has not publicly brokered on Iran's behalf; no Moscow framing on Touska seizure as of Monday AM (Xinhua/TASS/Global Times also silent — not framing as multilateral escalation yet). "
    "Pakistan-Russia track (if it exists) has not publicly surfaced this week."
))
touch(n)
save('russia', n)
updates_log['russia'] = {'signals': 1, 'edges_bumped': ['india', 'united-states', 'iran'], 'summary_refreshed': True}

# ---------------------------------------------------------------------- INDIAN-OIL-MARKETING
n = load('indian-oil-marketing')
add_signal(n, (
    "BESSENT IRANIAN-OIL WAIVER ELAPSED 05:30 IST MONDAY — STRUCTURAL ZERO MARGINAL IRANIAN SUPPLY; RUSSIAN WAIVER RENEWED (30-DAY) PRESERVES ~1.9 MBPD [CONFIRMED]. "
    "Incremental Iranian supply to Indian OMCs structurally zero from 05:30 IST Monday onward — Bessent's non-renewal executed without extension, carve-out, or wind-down. "
    "Russian-oil waiver RENEWED (30-day India-specific extension) despite Bessent's April 15 \"neither\" statement — preserves March baseline ~1.9 mbpd Russian flow to Indian refiners. "
    "Reliance pre-positioned earlier by rejecting Derya and Lenore. IOC/BPCL/HPCL Monday -1.5 to -2.5% on Brent gap. Reliance Q4 earnings this week — crisis-beneficiary through refining margins, oil-sourcing complexity penalized."
), ['Business Today', 'The Week', 'The Federal', 'Bloomberg'], 'high')
bump_edge(n, 'brent-crude')
bump_edge(n, 'iran')
touch(n)
save('indian-oil-marketing', n)
updates_log['indian-oil-marketing'] = {'signals': 1, 'edges_bumped': ['brent-crude', 'iran']}

# ---------------------------------------------------------------------- PEZESHKIAN
n = load('pezeshkian')
add_signal(n, (
    "PEZESHKIAN SILENT 72+ HRS — NO PUBLIC DEFENSE OF ARAGHCHI; NO STATEMENT ON MEA SUMMONS OR TOUSKA SEIZURE [CONFIRMED ABSENCE]. "
    "Through Monday AM, President Pezeshkian has not publicly defended FM Araghchi against Mahmoudi impeachment threat + Kayhan/Tasnim attacks; has not addressed India MEA summons of Ambassador Fathali (40+ hrs Iran MFA silence); has not framed Touska seizure. "
    "Civilian-president silence is the key factional signal — if absence continues through Monday evening, factional collapse (parliament + state media + IRGC + Supreme Leader office aligned against FM) confirmed as new baseline, not temporary."
), ['Iran International', 'NCRI', 'Araghchi X (indirect)'], 'high')
touch(n)
save('pezeshkian', n)
updates_log['pezeshkian'] = {'signals': 1}

# ---------------------------------------------------------------------- UAE
n = load('uae')
add_signal(n, SIG['uae_correction'], ['Gulf Business (Apr 9)', 'The National (Abu Dhabi) Apr 9', 'Al Arabiya Apr 9', 'ADNOC press release', 'CNBC', 'AGBI', 'CGTN'], 'medium')
touch(n)
save('uae', n)
updates_log['uae'] = {'signals': 1, 'note': "No edge bump — CORRECTION logged for yesterday's phantom-Sunday weight increase (7.0 to 8.0). Underlying April 9 position confirmed; edge stands but history reflects continuity not step-up."}

# ---------------------------------------------------------------------- MOJTABA KHAMENEI
n = load('mojtaba-khamenei')
add_signal(n, (
    "SUPREME LEADER OFFICE SILENT ON ARAGHCHI IMPEACHMENT MATTER SECOND DAY; MAHMOUDI NAMED AS MOVER (NOT AZIZI) [CONFIRMED absences; CORRECTION on naming]. "
    "Mojtaba Khamenei's office silent Monday AM on Mahmoudi's impeachment statement, Kayhan/Tasnim FM attacks, and Touska seizure. Parliament-state-media-IRGC triangle now aligned against Araghchi with only civilian executive (Pezeshkian) remaining ambiguously positioned — also silent. "
    "Refines Friday reporting: the named impeachment mover is MP Morteza Mahmoudi, not Ebrahim Azizi; motion paused \"for wartime considerations.\""
), ['Iran International', 'Caliber.Az', 'NCRI', 'Open Source Intel (@Osint613)'], 'medium')
touch(n)
save('mojtaba-khamenei', n)
updates_log['mojtaba-khamenei'] = {'signals': 1}

# ---------------------------------------------------------------------- ISRAEL
n = load('israel')
add_signal(n, SIG['lebanon_day_4'], ['JNS', 'Ynet', 'Times of Israel', 'Terrorism-info.org.il (ITIC)'], 'medium')
add_signal(n, (
    "ISRAELI MEDIA TONE: QUIET → GRIEF-FOCUSED ON KALFON FUNERAL [SOURCE TONE]. "
    "Monday Israeli outlets (Times of Israel, Ynet, Jerusalem Post, Haaretz) dominated by Kalfon funeral coverage — Katz tribute, Kiryat Shmona municipal convoy, 226th Reserve Paratroopers unit — displacing Hormuz framing to interior pages. "
    "Haaretz military correspondents have published nothing Sun night-Mon AM specifically challenging the government's Lebanon-ceasefire-holds framing (absence-as-intelligence: if IDF senior officers had private disagreement, would typically leak via Haaretz). "
    "Hegemonic Israeli frame for Hormuz/Touska: \"Trump problem, Iran problem, Israel watches.\""
), ['Times of Israel', 'Ynet', 'Jerusalem Post', 'Haaretz'], 'low')
bump_edge(n, 'lebanon')
touch(n)
save('israel', n)
updates_log['israel'] = {'signals': 2, 'edges_bumped': ['lebanon']}

# ---------------------------------------------------------------------- LEBANON
n = load('lebanon')
add_signal(n, SIG['lebanon_day_4'], ['JNS', 'Ynet', 'Times of Israel', 'Terrorism-info.org.il'], 'medium')
bump_edge(n, 'israel')
bump_edge(n, 'hezbollah')
touch(n)
save('lebanon', n)
updates_log['lebanon'] = {'signals': 1, 'edges_bumped': ['israel', 'hezbollah']}

# ---------------------------------------------------------------------- HEZBOLLAH
n = load('hezbollah')
add_signal(n, (
    "QASSEM SUNDAY SPEECH CALLED LEBANON CEASEFIRE 'INSULT TO LEBANON' — RHETORIC ONLY; NO ROCKETS DAY 4 [CONFIRMED RHETORIC, CONFIRMED KINETIC ABSENCE]. "
    "Hezbollah SG Qassem's Sunday speech labeled the 10-day ceasefire \"an insult to Lebanon\" but has not produced rocket fire. Day 4 posture: low-signature kinetic permitted (Kalfon IED) + escalatory rhetoric permitted + open rocket war withheld. "
    "Structural fragility unchanged: Hezbollah non-signatory, IDF in-country, no withdrawal. April 26 ceasefire expiry in 6 days."
), ['JNS', 'Times of Israel', 'Ynet'], 'medium')
touch(n)
save('hezbollah', n)
updates_log['hezbollah'] = {'signals': 1}

# ---------------------------------------------------------------------- HOUTHIS
n = load('houthis')
add_signal(n, SIG['houthis_day_55'], ['MARAD 2026-006', 'Reuters (Apr 7 backgrounder)', 'TWZ'], 'medium')
touch(n)
save('houthis', n)
updates_log['houthis'] = {'signals': 1, 'note': 'shipping-tankers edge step below 9.0 DEFERRED pending Tuesday IST — Touska extends test window.'}

# ---------------------------------------------------------------------- RED SEA
n = load('red-sea')
add_signal(n, (
    "RED SEA DAY 55 OF NON-MIRRORING — NO HOUTHI KINETIC AFTER IRAN SATURDAY OR TOUSKA SUNDAY [CONFIRMED ABSENCE]. "
    "No Houthi kinetic in Red Sea or Bab-el-Mandeb has followed Iran's Saturday kinetic, the Touska seizure, or Iran's Round 2 rejection. MARAD 2026-006 advisory active as standing posture. Soufan coordination thesis weaker with elapsed time."
), ['MARAD 2026-006', 'TWZ'], 'low')
touch(n)
save('red-sea', n)
updates_log['red-sea'] = {'signals': 1}

# ---------------------------------------------------------------------- QATAR
n = load('qatar')
add_signal(n, SIG['ras_laffan_unchanged'], ['The National (Abu Dhabi)', 'AGBI', 'Oil & Gas Middle East'], 'medium')
add_signal(n, SIG['ttf_monday_plus_11'], ['Bloomberg', 'Trading Economics'], 'high')
bump_edge(n, 'helium')
bump_edge(n, 'natural-gas-lng')
touch(n)
save('qatar', n)
updates_log['qatar'] = {'signals': 2, 'edges_bumped': ['helium', 'natural-gas-lng']}

# ---------------------------------------------------------------------- NATURAL GAS LNG
n = load('natural-gas-lng')
add_signal(n, SIG['ttf_monday_plus_11'], ['Bloomberg', 'Trading Economics'], 'high')
add_signal(n, SIG['ras_laffan_unchanged'], ['The National', 'AGBI'], 'medium')
bump_edge(n, 'european-ttf-gas')
bump_edge(n, 'qatar')
touch(n)
save('natural-gas-lng', n)
updates_log['natural-gas-lng'] = {'signals': 2, 'edges_bumped': ['european-ttf-gas', 'qatar']}

# ---------------------------------------------------------------------- HELIUM
n = load('helium')
add_signal(n, (
    "MONDAY NO INTEL/TSMC/SAMSUNG Q2 ALLOCATION NOTICE — HELIUM→SEMICONDUCTOR CASCADE STAYS WATCHING; ALLOCATION-IMPACT SEAM TUE-THU [CONFIRMED ABSENCE]. "
    "No allocation-notice filing Sunday/Monday morning from Intel/TSMC/Samsung. Ras Laffan damage = ~11% of global helium supply at risk (AGBI; Fortune reports 35% of market); Seagate/WD already allocated + price-increased. Asian fab transit schedules covered \"through approximately early April 2026\" per Smith Helium Shortage Update April 9 — we are AT the allocation-impact seam. "
    "SMH Friday +2.1% on risk-on + earnings momentum; Monday expected mild DOWN on Dow futures -400pts. Any Q2 allocation notice re-prices SMH -3 to -5% and activates `helium → semiconductors → tech-valuations` cascade."
), ['AGBI', 'Fortune', 'Smith Helium Shortage Update'], 'medium')
touch(n)
save('helium', n)
updates_log['helium'] = {'signals': 1, 'note': 'Allocation-impact seam Tue-Thu — most time-sensitive trigger in graph'}

# ---------------------------------------------------------------------- EUROPEAN TTF GAS
n = load('european-ttf-gas')
add_signal(n, SIG['ttf_monday_plus_11'], ['Bloomberg', 'Trading Economics'], 'high')
add_signal(n, (
    "TTF → FERTILIZER-UREA EDGE CONFIRMED MECHANISM MONDAY — NITROGEN INPUT COST RE-ESCALATION VIA EUROPEAN PRODUCERS [REPORTED]. "
    "TTF +11% intraday Monday propagates to European industrial input costs for nitrogen fertilizers. CF Industries European exposure + ammonia is gas-heavy production — gas price → urea floor. "
    "Supports markets.md F3 new-edge proposal: european-ttf-gas → fertilizer-urea (1st order, initial weight 4.5)."
), ['Bloomberg', 'Trading Economics', 'Profercy World Nitrogen Index'], 'medium')
bump_edge(n, 'fertilizer-urea')
set_current(n,
    price='~€46/MWh Monday intraday (+11%); Friday close €41.59/MWh',
    delta_1d='+11% intraday Mon (vs Fri)',
    delta_1m='Off April 13 €56 peak but Mon reclaims upside on Touska/SNSC',
    delta_3m='structural floor €45-50 per Ras Laffan partial-restart horizon'
)
n.setdefault('price_snapshots', []).append({
    'date': TODAY,
    'price': '~€46/MWh intraday (+11% vs €41.59 Fri)',
    'trigger': 'Touska seizure + SNSC ratification + Ras Laffan 3-5yr partial-restart horizon = cleanest weekend cascade signal',
    'delta_context': 'European gas more crisis-levered than HH (US pipeline isolated); TTF must absorb Qatar LNG loss AND Gulf transit insurance. Floor €45-50, ceiling €60-70 on cruise-ship repeat / LNG-tanker kinetic.'
})
set_summary(n, (
    "Day 53 Monday AM. TTF +11% INTRADAY (~€41.59 → ~€46/MWh) — CLEANEST WEEKEND CASCADE SIGNAL. "
    "Touska seizure + SNSC ratification + Ras Laffan 3-5yr on Trains 4/6 (12.8 mtpa, ~17% Qatar LNG) = LNG tanker risk premium extends on Gulf transit + replacement US Gulf/Australia LNG stretched. "
    "More crisis-levered than Henry Hub (HH +1% Fri, domestic pipeline isolated); TTF absorbs both Qatar loss AND Gulf transit insurance. Structural floor €45-50 (partial-restart horizon); spike ceiling €60-70 on cruise-ship repeat or LNG-tanker kinetic. "
    "Propagates to DAX industrial input costs (DAX Mon -1 to -1.5% base) and European nitrogen fertilizer producers (CF European exposure — markets.md F3 proposes european-ttf-gas → fertilizer-urea new edge weight 4.5)."
))
touch(n)
save('european-ttf-gas', n)
updates_log['european-ttf-gas'] = {'signals': 2, 'edges_bumped': ['fertilizer-urea'], 'price_snapshot_added': True, 'summary_refreshed': True}

# ---------------------------------------------------------------------- SAUDI ARABIA
n = load('saudi-arabia')
add_signal(n, SIG['mbs_sharif_mediation'], ['Arab News', 'Middle East Eye', 'Al Jazeera'], 'high')
bump_edge(n, 'iran')
bump_edge(n, 'strait-of-hormuz')
set_summary(n, (
    "Day 53 Monday AM. SAUDI MOVES FROM OBSERVER TO ACTIVE CONVENER-MEDIATOR ON US-IRAN TRACK. "
    "MBS-Sharif Jeddah meeting this week on US-Iran mediation architecture and Pakistan's host-mediator role (Arab News). Middle East Eye: MBS reportedly told Trump directly \"a Lebanon ceasefire is critical\" to reopening Hormuz — Saudi shifts to mediation efforts to reopen the Strait. "
    "Emerging Gulf architecture: Saudi-Pakistan mediator axis / UAE hardening (Al Jaber Apr 9 position continuity) / Qatar neutral / Oman silent — four-way split. If Saudi-Pakistan coordinate on pushing Iran back to table, \"Iran permanently refuses talks\" tail shrinks. "
    "Arab News Monday lead = MBS-Sharif meeting; Saudi is public about mediator positioning."
))
touch(n)
save('saudi-arabia', n)
updates_log['saudi-arabia'] = {'signals': 1, 'edges_bumped': ['iran', 'strait-of-hormuz'], 'summary_refreshed': True}

# ---------------------------------------------------------------------- NIFTY 50
n = load('nifty-50')
add_signal(n, SIG['nifty_monday_revised'], ['Business Standard', 'Livemint', 'Economic Times', 'Moneycontrol'], 'high')
bump_edge(n, 'brent-crude')
bump_edge(n, 'inr-usd')
set_current(n,
    price='24,353.55 (Friday April 17 close)',
    delta_1d='+0.65% Friday; Monday open expected -0.5 to -1.0% (24,110-24,230)',
    delta_1m='+5.2%',
    delta_3m='-4.8%'
)
set_summary(n, (
    "Day 53 Monday AM. NIFTY MONDAY BASE -0.5 TO -1.0% (24,110-24,230) — REVISED MILDER THAN EVENING'S -1.0 TO -1.5%. "
    "Revision drivers: Russian-oil waiver RENEWED (preserves ~1.9 mbpd to Indian refiners — material positive not in evening framing); Brent Monday ~$95.42 is $3-4 BELOW Globex $98 that drove evening forecast; HDFC Bank + ICICI Bank reported Apr 18 (earnings read pending). "
    "200-DMA 24,050 likely holds intraday. OMCs (IOC/BPCL/HPCL) -1.5 to -2.5% on Brent gap; Reliance neutral (refining-margin beneficiary vs oil-sourcing complexity penalty); Adani Ports (Mundra/Krishnapatnam Gulf exposure) -1 to -2%. "
    "Bank Nifty direction depends on yield — India 10Y 6.90% avg; if gaps through 7.00%, banks -1 to -2%. "
    "Recovery to Friday's 24,353.55 by Wednesday plausible if Monday cash settles Brent $94-95 and no IRGC kinetic on US assets by Tuesday close."
))
touch(n)
save('nifty-50', n)
updates_log['nifty-50'] = {'signals': 1, 'edges_bumped': ['brent-crude', 'inr-usd'], 'summary_refreshed': True}

# ---------------------------------------------------------------------- INR USD
n = load('inr-usd')
add_signal(n, SIG['inr_monday'], ['Business Standard', 'Livemint', 'Trading Economics', 'Moneycontrol'], 'high')
bump_edge(n, 'brent-crude')
bump_edge(n, 'rbi')
set_summary(n, (
    "Day 53 Monday AM. USD/INR MONDAY BASE ₹92.80-93.10 (-0.25 TO -0.55%) — RBI MACRO-PRUDENTIAL TOOLKIT CAPS OFFSHORE-SPECULATIVE TRANSMISSION. "
    "Friday ₹92.57 (-0.9% rupee stronger 1D, -0.7% 1M) mechanical on Brent crash + RBI ~$800M intervention. Monday re-test ₹93+ expected on Brent spike + MEA summons; break-higher trigger Brent >$97 sustained 3 sessions → ₹93.50-94.00 intraday. "
    "RBI's March 27 NOP cap ($100M/bank) + April 1 NDF ban produced single-largest 12-year rupee rally (₹95.22 → ₹93.10) without any rate move — mechanism is macro-prudential, NOT policy-rate. Rupee more defended than equity market (opposite of 2013 / 2022). "
    "Next RBI escalation tool if ₹93.50 breaks: onshore forward ceiling or special dollar-swap window (neither deployed yet; deployment itself would signal escalated concern)."
))
touch(n)
save('inr-usd', n)
updates_log['inr-usd'] = {'signals': 1, 'edges_bumped': ['brent-crude', 'rbi'], 'summary_refreshed': True}

# ---------------------------------------------------------------------- RBI
n = load('rbi')
add_signal(n, (
    "RBI MACRO-PRUDENTIAL TOOLKIT DEPLOYED; NO NEW POLICY MONDAY — NEXT ESCALATION TOOL IS ONSHORE FORWARD CEILING OR SPECIAL DOLLAR-SWAP WINDOW [REPORTED]. "
    "March 27 NOP cap ($100M/bank vs prior 25% Tier-1+2) + April 1 NDF ban (barring authorized dealers from offering rupee NDF to resident Indians and NRIs) are already in effect; rupee rallied ₹95.22 → ₹93.10 on the mechanism alone — single-largest 12-year single-day rupee gain April 2 attributable to NDF-ban/NOP-cap combination. "
    "Monday: no new RBI policy expected. Rupee ₹92.57 Friday continuation of stabilization trend. Next escalation tool if USD/INR breaks ₹93.50: onshore forward ceiling or special dollar-swap window (deployment itself signals escalated concern). "
    "Propose edge refinement (markets.md F5): distinguish `rbi → inr-usd` policy-rate channel (weight ~4.0) vs macro-prudential channel (weight ~7.0 post-Apr-1 demonstration). Single-edge retained for simplicity, context field updated."
), ['Trading Economics', 'Business Standard', 'Livemint'], 'high')
bump_edge(n, 'inr-usd')
touch(n)
save('rbi', n)
updates_log['rbi'] = {'signals': 1, 'edges_bumped': ['inr-usd']}

# ---------------------------------------------------------------------- GOLD
n = load('gold')
add_signal(n, SIG['gold_anomaly'], ['yfinance GC=F', 'markets.md 2026-04-20 Section D5', 'Kitco (pending)', 'LBMA (pending)'], 'high')
touch(n)
save('gold', n)
updates_log['gold'] = {'signals': 1, 'note': 'NO edge weight changes — regime-shift thesis UNDER RECONCILIATION pending yfinance print vs Kitco/LBMA spot verification.'}

# ---------------------------------------------------------------------- US 10Y YIELD
n = load('us-10y-yield')
add_signal(n, (
    "US 10Y 4.25% FRIDAY (-1.5% 1D) — FED APRIL 28-29 FOMC IN 8 DAYS; STATEMENT FRAMING 'TEMPORARY ENERGY SHOCK' VS 'INFLATION PERSISTENCE' IS LIVE [REPORTED]. "
    "CME FedWatch 99.3% probability no rate change at April 28-29 FOMC. Front-month oil futures +50% over period with longer-dated futures much smaller rise → expectations of temporary-shock (per Fed minutes). Brent $95 Monday tests whether \"temporary\" framing survives March CPI +0.9% m/m (core +0.2%). "
    "Tape risk: If any Fed speaker (Waller, Williams, Daly) walks back June-cut probability Monday-Tuesday, yields spike across curve independent of crisis."
), ['CME FedWatch', 'Trading Economics', 'Fed minutes'], 'medium')
touch(n)
save('us-10y-yield', n)
updates_log['us-10y-yield'] = {'signals': 1}

# ---------------------------------------------------------------------- FERTILIZER UREA
n = load('fertilizer-urea')
add_signal(n, SIG['cf_monday_bounce'], ['Argus Media', 'Profercy World Nitrogen Index', 'Trading Economics'], 'high')
bump_edge(n, 'european-ttf-gas')
bump_edge(n, 'qatar')
set_summary(n, (
    "Day 53 Monday AM. CF INDUSTRIES MONDAY GAP-UP +5-8% EXPECTED; NUTRIEN +3-5% ON SNSC + TTF +11% + UREA RE-BID. "
    "Friday CF -9.6% / Nutrien -5.2% was pure deal-optimism mispricing. Urea FOB ~$713/T Apr 16 (+16.8% 1M, +75% YoY); Profercy World Nitrogen Index 352.95 — highest since May 2022. "
    "ME granular urea FOB ~$410s/t (Argus Egypt/Algeria post-Qatar benchmark); global spot $702.25/T +15% 1M. TTF Monday +11% confirms European nitrogen input-cost re-escalation — ammonia gas-heavy production → TTF → CF European exposure. "
    "Structural floor CF ~$105 even in full-resolution case (Ras Laffan damaged trains 3-5 yr recovery). markets.md F3 proposes new european-ttf-gas → fertilizer-urea edge (weight 4.5)."
))
touch(n)
save('fertilizer-urea', n)
updates_log['fertilizer-urea'] = {'signals': 1, 'edges_bumped': ['european-ttf-gas', 'qatar'], 'summary_refreshed': True}

# ---------------------------------------------------------------------- SP 500
n = load('sp-500')
add_signal(n, SIG['vix_dow_futures'], ['CNBC', 'Dow futures Globex', 'CME VX front-month'], 'high')
bump_edge(n, 'us-10y-yield')
set_current(n,
    price='7,126.06 Friday April 17 RECORD close; Monday open expected -0.8 to -1.0%',
    delta_1d='+1.2% Fri; Mon -0.8 to -1.0% base',
    delta_1m='+7.6%',
    delta_3m='+4.8%',
    vix='17.48 Fri cash; 19-20 VIX futures Sunday; expected 19-21 cash re-mark Monday'
)
set_summary(n, (
    "Day 53 Monday AM. DOW FUTURES SUNDAY NIGHT -400 PTS → S&P MONDAY OPEN -0.8 TO -1.0%; NASDAQ 12-DAY STREAK SNAPS; VIX CASH 19-21 MONDAY. "
    "Friday: S&P 500 7,126.06 RECORD (+1.2%); NASDAQ 24,468.48 +1.5% (12-day streak longest since 1992); VIX 17.48 (-2.6% war-era low). Monday Globex Dow -400 pts on Touska + IRNA rejection + SNSC + waiver. "
    "Vol-short-carry trade vulnerable: Tuesday IST kinetic Iranian retaliation on US assets → VIX mid-20s dealer re-marks. Non-crisis AI/earnings momentum ~0.7% S&P / 0.9% NASDAQ of Friday's gains stickier — intraday rebound plausible absent kinetic. "
    "Tail scenario: VIX cash 22+ Monday AND Brent $97+ sustained 3 sessions AND macro compounding (hawkish Fed speaker / regional bank stress) = S&P -2-3% first week. Base-resolution: Witkoff/Vance/Kushner on-ground Tuesday + IRGC absorbs Touska → fresh records within days."
))
touch(n)
save('sp-500', n)
updates_log['sp-500'] = {'signals': 1, 'edges_bumped': ['us-10y-yield'], 'summary_refreshed': True}

# ---------------------------------------------------------------------- FED
n = load('fed')
add_signal(n, (
    "FED APRIL 28-29 FOMC 8 DAYS OUT — 99.3% NO CHANGE; STATEMENT FRAMING ON BRENT $95 IS LIVE RISK [REPORTED]. "
    "CME FedWatch 99.3% probability no rate change. Live issue: statement framing — \"temporary energy shock\" vs \"inflation persistence\" vs \"reason to delay cuts deeper into H2.\" Brent $95 Monday tests whether \"temporary\" framing survives March CPI +0.9% m/m (core +0.2%). "
    "Front-month oil +50% vs. smaller longer-dated rise = market still pricing temporary-shock; Fed minutes align. Tape risk: Fed speaker (Waller, Williams, Daly) walking back June-cut Monday-Tuesday → yield spike across curve independent of crisis."
), ['CME FedWatch', 'Trading Economics', 'Fed minutes'], 'medium')
touch(n)
save('fed', n)
updates_log['fed'] = {'signals': 1}

# ==== Edges.json updates ========================================================

edges_path = ROOT / 'graph' / 'edges.json'
edata = json.loads(edges_path.read_text())

def get_edge(from_, to_):
    for e in edata['edges']:
        if e['from'] == from_ and e['to'] == to_:
            return e
    return None

# Bump existing edges activated today — sync weights from the node edges
activated_today = [
    ('iran', 'united-states'), ('iran', 'strait-of-hormuz'), ('iran', 'brent-crude'),
    ('iran', 'russia'), ('iran', 'pakistan'),
    ('united-states', 'iran'), ('united-states', 'brent-crude'), ('united-states', 'pakistan'),
    ('united-states', 'trump'),
    ('irgc', 'united-states'), ('irgc', 'strait-of-hormuz'), ('irgc', 'shipping-tankers'),
    ('strait-of-hormuz', 'brent-crude'), ('strait-of-hormuz', 'iran'), ('strait-of-hormuz', 'united-states'),
    ('shipping-tankers', 'brent-crude'), ('shipping-tankers', 'marine-war-risk-insurance'),
    ('shipping-tankers', 'strait-of-hormuz'),
    ('brent-crude', 'strait-of-hormuz'), ('brent-crude', 'iran'),
    ('marine-war-risk-insurance', 'brent-crude'), ('marine-war-risk-insurance', 'shipping-tankers'),
    ('trump', 'iran'),
    ('pakistan', 'iran'), ('pakistan', 'united-states'), ('pakistan', 'saudi-arabia'),
    ('vance', 'pakistan'),
    ('india', 'iran'), ('india', 'united-states'), ('india', 'brent-crude'),
    ('indian-oil-marketing', 'brent-crude'), ('indian-oil-marketing', 'iran'),
    ('israel', 'lebanon'),
    ('lebanon', 'israel'), ('lebanon', 'hezbollah'),
    ('qatar', 'helium'), ('qatar', 'natural-gas-lng'),
    ('natural-gas-lng', 'european-ttf-gas'), ('natural-gas-lng', 'qatar'),
    ('european-ttf-gas', 'fertilizer-urea'),
    ('saudi-arabia', 'iran'), ('saudi-arabia', 'strait-of-hormuz'),
    ('nifty-50', 'brent-crude'), ('nifty-50', 'inr-usd'),
    ('inr-usd', 'brent-crude'), ('inr-usd', 'rbi'),
    ('rbi', 'inr-usd'),
    ('fertilizer-urea', 'european-ttf-gas'), ('fertilizer-urea', 'qatar'),
    ('sp-500', 'us-10y-yield'),
]

edges_bumped_count = 0
for (f, t) in activated_today:
    e = get_edge(f, t)
    if e:
        # sync weight from node
        try:
            nd = load(f)
            for ne in nd.get('edges', []):
                if ne['to'] == t:
                    e['weight'] = ne.get('weight', e['weight'])
                    break
        except Exception:
            pass
        e['last_activated'] = TODAY
        edges_bumped_count += 1

# NEW edges
new_edges_added = []

def add_new_edge(from_, to_, weight, directness, ctx):
    if not get_edge(from_, to_):
        edata['edges'].append({
            'from': from_, 'to': to_, 'weight': weight,
            'directness': directness, 'last_activated': TODAY
        })
        new_edges_added.append((from_, to_, weight, ctx))

add_new_edge('qatar', 'european-ttf-gas', 7.0, 1,
    'Ras Laffan 12.8 mtpa offline 3-5yr on Trains 4/6 (~17% Qatar LNG) → structural TTF floor. Transmission confirmed in crisis; markets.md F4.')
add_new_edge('saudi-arabia', 'pakistan', 4.5, 1,
    'MBS-Sharif Jeddah meeting on US-Iran mediation architecture; Saudi-Pakistan mediation axis coordinated vs UAE hardening. Arab News, MEE.')
add_new_edge('saudi-arabia', 'united-states', 4.5, 1,
    'MBS-Trump direct line per MEE: "a Lebanon ceasefire is critical" to reopening Hormuz; Saudi moves to active convener.')
add_new_edge('russia', 'united-states', 4.5, 1,
    'US Treasury renewed Russian-oil waiver (30-day India extension) despite Bessent "neither" language — asymmetric sanctions policy preserves global supply balance.')
add_new_edge('russia', 'india', 4.5, 1,
    'Russian-oil waiver renewed for 30-day India-specific extension; ~1.9 mbpd March Russian flow to Indian refiners preserved.')
add_new_edge('india', 'russia', 4.5, 1,
    'Russian-oil waiver renewal preserves ~1.9 mbpd flow to Indian refiners — material positive for Indian OMC supply security while Iranian waiver elapsed.')
add_new_edge('indian-oil-marketing', 'russia', 4.5, 1,
    'Russian-oil waiver renewal — Indian OMCs preserve ~1.9 mbpd Russian supply vs zero Iranian incremental post-waiver elapse.')
add_new_edge('united-states', 'shipping-tankers', 4.5, 1,
    'USS Spruance Mk 45 kinetic on Iranian-flagged Touska introduces US-side risk premium on commercial shipping; AWRP modeling now requires bi-directional US + Iran kinetic risk.')
add_new_edge('fertilizer-urea', 'european-ttf-gas', 4.5, 1,
    'European nitrogen producers re-price input costs on TTF moves; ammonia gas-heavy production. markets.md F3 symmetric mechanism.')

edata['last_updated'] = TODAY

edges_path.write_text(json.dumps(edata, indent=2, ensure_ascii=False))

# ==== meta.json =================================================================

meta_path = ROOT / 'graph' / 'meta.json'
meta = json.loads(meta_path.read_text())
meta['last_updated'] = TODAY
meta['briefs_generated'] = meta.get('briefs_generated', 30) + 1
meta['total_nodes'] = len(list(NODES.glob('*.json')))
meta['total_edges'] = len(edata['edges'])
meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False))

# Print summary
print('=== Updates applied ===')
for k, v in updates_log.items():
    print(k, ':', v)
print()
print(f'=== New edges added: {len(new_edges_added)} ===')
for f, t, w, ctx in new_edges_added:
    print(f'{f} -> {t} w={w}')
print()
print(f'Existing edges activated: {edges_bumped_count}')
print(f'Total nodes: {meta["total_nodes"]}')
print(f'Total edges: {meta["total_edges"]}')
print(f'Briefs generated: {meta["briefs_generated"]}')
