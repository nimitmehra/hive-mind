#!/usr/bin/env python3
"""
Evening graph update for 2026-04-19.
Layered on top of morning changelog. Adds NEW evening developments only:
- Araghchi offensive Sunday X posts
- Sunday Globex Brent ~$98
- Gold +2.0% to $4,879.60 (regime-shift CONFIRMED)
- IDF reservist Kalfon killed by Hezbollah IED (first ceasefire-window fatality)
- Naim Qassem Sunday speech (defiant rhetoric, no rocket order)
- UAE ADNOC Al Jaber "unconditional opening" (UAE public hardening)
- Saudi FM Faisal-Araghchi 3 calls Apr 9-14
- Sunday Houthi quiet Day 54
- US delegation still no travel to Islamabad
- VIX futures 19-20 vs Friday cash 17.48
"""
import json, os
from datetime import datetime

DATE = "2026-04-19"
EVENING_TS = "2026-04-19 evening (~22:00 IST)"
NODES_DIR = "graph/nodes"

def load(name):
    return json.load(open(f"{NODES_DIR}/{name}.json"))

def save(name, data):
    with open(f"{NODES_DIR}/{name}.json", "w") as f:
        json.dump(data, f, indent=2)

def add_signal(node, content):
    node.setdefault("signals", []).append({
        "date": DATE,
        "content": content
    })

def add_snapshot(node, price, trigger, delta_context):
    node.setdefault("price_snapshots", []).append({
        "date": DATE,
        "price": price,
        "trigger": trigger,
        "delta_context": delta_context
    })

def touch_edge(node, to, last_act=DATE, weight_delta=0, count_delta=1, type_rename=None, context_append=None, weight_set=None):
    """Find edge in node and update."""
    for e in node.get("edges", []):
        if e.get("to") == to:
            e["last_activated"] = last_act
            e["activation_count"] = e.get("activation_count", 0) + count_delta
            if weight_set is not None:
                e["weight"] = weight_set
            elif weight_delta:
                e["weight"] = min(10.0, max(0.0, e.get("weight", 5.0) + weight_delta))
            if type_rename:
                e["type"] = type_rename
            if context_append:
                e["context"] = (e.get("context", "") + " | " + context_append).strip(" |")
            return True
    return False

def add_edge(node, to, etype, context, weight, directness=1):
    node.setdefault("edges", []).append({
        "to": to,
        "type": etype,
        "context": context,
        "directness": directness,
        "last_activated": DATE,
        "activation_count": 1,
        "weight": weight
    })

def add_trigger(node, condition, cascade, mechanism, status="watching"):
    node.setdefault("trigger_points", []).append({
        "condition": condition,
        "cascade": cascade,
        "mechanism": mechanism,
        "added": DATE,
        "status": status
    })

def set_last_updated(node, ts=DATE):
    node["last_updated"] = ts

# ---------- IRAN ----------
iran = load("iran")
add_signal(iran,
    "ARAGHCHI PIVOTS DEFENSE TO OFFENSE VIA SUNDAY X POSTS [CONFIRMED via Araghchi's own X account; corroborated The Hill, Fortune, Iran International — RHETORIC]. "
    "Foreign Minister Abbas Araghchi posted Sunday April 19: 'Strait of Hormuz is not closed. Ships hesitate because insurers fear the war of choice you initiated — not Iran'; "
    "'No insurer — and no Iranian — will be swayed by more threats. Try respect'; 'Freedom of Navigation cannot exist without Freedom of Trade. Respect both — or expect neither.' "
    "Material posture shift from morning brief: Araghchi no longer absorbing Kayhan/Tasnim criticism quietly — he is attacking Trump directly ('war of choice') and explicitly redirecting "
    "responsibility for the kinetic chokepoint effect onto the insurance market rather than IRGC kinetic. He has NOT been publicly defended by Pezeshkian; Supreme Leader's office silent second day. "
    "Lawmaker Ebrahim Azizi's Friday impeachment threat has produced no Sunday no-confidence motion. Araghchi's chosen instrument is his personal X account, not institutional backing — "
    "itself a signal of constrained institutional support. The IRNA-Tasnim divergence has matured into IRNA-Tasnim-Araghchi three-way standoff with no resolution path."
)
iran["summary"] = (
    "Day 52 Sunday evening. THREE-WAY FACTIONAL STANDOFF NOT RESOLVED — ARAGHCHI PIVOTS TO OFFENSE. SNSC formal ratification Saturday evening "
    "(civilian apex chaired by Pezeshkian, statutorily outranks IRGC and MFA) operationalised the IRGC framework: transit certificates, $1/bbl loaded-tanker fees, military + hostile vessels denied, "
    "Araghchi Friday framework suspended until US lifts blockade. Sunday April 19 — Araghchi posted three X messages attacking Trump directly ('war of choice you initiated') and naming the insurance market "
    "rather than IRGC as the kinetic-chokepoint vector. Pezeshkian has not publicly defended his Foreign Minister; Supreme Leader's office silent second consecutive day. "
    "Kayhan editor Shariatmadari (Supreme-Leader appointee) named Araghchi again Sunday demanding accountability; Tasnim/Fars unchanged. "
    "Iranian rial 1.527M/USD Saturday print (below 2M trigger; mid-April peak above 1.6M; thin-volume channels). "
    "Three-way IRNA-Tasnim-Araghchi standoff with no resolution channel. Saudi FM Faisal-Araghchi three calls April 9-14 (mediator-adjacent lane). "
    "India MEA summons (Saturday) has not received Iranian MFA response 30+ hours later — Tehran cannot produce coherent civilian reply because IRGC/Araghchi/Pezeshkian triangle is openly fractured."
)
touch_edge(iran, "strait-of-hormuz", count_delta=1)
touch_edge(iran, "united-states", count_delta=1, context_append=f"{DATE} eve: Araghchi X attacks Trump directly ('war of choice'), redirects blame to insurance market.")
touch_edge(iran, "brent-crude", count_delta=1)
set_last_updated(iran)
save("iran", iran)

# ---------- STRAIT-OF-HORMUZ ----------
soh = load("strait-of-hormuz")
add_signal(soh,
    "ARAGHCHI SUNDAY X POSTS REFRAME CHOKEPOINT EFFECT AS INSURANCE-MARKET PROBLEM [CONFIRMED — RHETORIC]. "
    "FM Araghchi Sunday April 19: 'Strait of Hormuz is not closed. Ships hesitate because insurers fear the war of choice you initiated — not Iran.' "
    "Significance: Iran's civilian wing now explicitly naming the insurance market — not the IRGC kinetic — as the operational chokepoint mechanism. Operationally, this is correct "
    "(Lloyd's AWRP ~1% Friday, expected step to 1.2-1.8% Monday; VLCC TD3C WS 513 with $130-150K/day earnings vs ~WS 50 nominal) but it sets up a separate Iranian framing where "
    "Tehran can claim 'open in principle' while harvesting fee revenue under SNSC's $1/bbl regime. The civilian-IRGC factional gap is narrative-only, not operational."
)
add_signal(soh,
    "NO FURTHER IRGC KINETIC SUNDAY — SATURDAY'S BURST IS ONE EVENT, NOT A CADENCE [CONFIRMED non-event via UKMTO, CENTCOM, Reuters, CNN, Times of Israel]. "
    "Through ~20:00 IST Sunday April 19, no additional ship fired on, no new UKMTO advisory beyond Saturday's 038-26 on container-ship projectile, CENTCOM's Sunday posture update repeats "
    "the 23-vessel blockade figure without new kinetic claim, no IMO-level cruise-ship incident corroborated beyond master-report on Mein Schiff 4. MarineTraffic AIS shows handful of vessels "
    "still transiting (Iranian-flag skewed, AIS spoofing per USNI). Sadjadpour's 72-hour falsifiable test (fresh fire through Tuesday IST = ladder stepped up; quiet = warning-shot-for-leverage thesis holds) "
    "tracking toward 'thesis holds' branch at the ~36-hour mark. CEILING signal for Monday Brent: $100+ would have required Sunday-kinetic repeat."
)
add_signal(soh,
    "UAE ADNOC CHAIRMAN AL JABER — 'STRAIT OF HORMUZ IS NOT OPEN AND NEEDS TO BE OPEN UNCONDITIONALLY' [REPORTED single-chain pending Monday corroboration — DIPLOMATIC SIGNAL]. "
    "Sultan Al Jaber, ADNOC chairman and former COP28 president, declared Sunday April 19 that the Strait is 'not open' and must be opened 'unconditionally.' Material hardening from "
    "morning brief's 'conspicuously quiet' UAE posture. Gulf diplomatic matrix Sunday evening: Saudi FM Faisal mediator-adjacent (3 calls with Araghchi Apr 9-14), Qatar neutral broker, "
    "Oman silent, UAE now publicly hardening on the chokepoint issue. Timing — Sunday before waiver expiry and before any Islamabad Round 2 — suggests UAE pre-positioning a public tough line "
    "rather than playing quiet convenor. The National (Abu Dhabi) carries Al Jaber's framing with editorial support; UAE information space aligned against Iran on chokepoint rights. "
    "Single-chain as of Sunday evening; await Al Monitor / The National corroboration Monday."
)
soh["summary"] = (
    "Day 52 Sunday evening. INSTITUTIONAL CODIFICATION INTACT, KINETIC IN PAUSE, GULF MATRIX HARDENING ON UAE LEG. "
    "Saturday SNSC ratification of IRGC framework remains operative (transit certificates, $1/bbl loaded-tanker fees, military + hostile vessels denied). "
    "No further IRGC kinetic Sunday — Saturday's burst (Jag Arnav VLCC, Sanmar Herald, container-ship projectile, Mein Schiff 4 cruise threat) is one event so far, not a cadence. "
    "CENTCOM's Sunday posture update repeats the 23-vessel blockade figure with no new kinetic claim. Sadjadpour 72-hour test tracking toward 'warning-shot-for-leverage thesis holds' at 36-hour mark. "
    "Sunday evening NEW: (1) UAE ADNOC chairman Al Jaber publicly: 'Strait not open, needs to be open unconditionally' — first UAE public hardening (single-chain pending Monday corroboration); "
    "(2) Iranian FM Araghchi Sunday X posts reframe chokepoint effect as insurance-market problem rather than IRGC action ('insurers fear the war of choice you initiated — not Iran') — "
    "operationally correct given Lloyd's AWRP ~1% Friday and VLCC TD3C WS 513 day-rates, but it sets up Tehran's civilian wing to claim 'open in principle' while harvesting SNSC fee revenue. "
    "Sunday Globex Brent indicatively ~$98 (+8.4% over Friday wire-ICE $90.38) confirms paper-physical convergence by paper rising to physical (Dated ~$132 Thursday). "
    "Kpler tape ~2 tankers since April 8 ceasefire; ~1-2% pre-war baseline. Gulf media: UAE hardening, Saudi mediating, Qatar neutral, Oman silent — four-way Gulf posture favours diplomatic optionality."
)
add_snapshot(soh,
    "Sunday Globex Brent ~$98 indicative; Lloyd's AWRP no Sunday republish",
    "Sunday non-event ceiling on Brent + UAE Al Jaber Sunday hardening + Araghchi insurance-market reframing",
    "+8.4% Brent over Friday wire close. AWRP republish Monday London open is next hard tell; expected 1.2-1.8%. UAE single-chain hardening pending Monday corroboration."
)
touch_edge(soh, "iran", count_delta=1)
touch_edge(soh, "shipping-tankers", count_delta=1)
touch_edge(soh, "irgc", count_delta=1)
add_trigger(soh,
    "Sustained kinetic absence Sunday-Tuesday IST + Lloyd's AWRP step UP — paper Brent tops $100 on insurance, not on kinetic",
    ["brent-crude", "marine-war-risk-insurance", "shipping-tankers"],
    "Sunday confirmed no fresh fire; if AWRP republishes >=1.5% Monday at London open and Brent prints $100+ without renewed kinetic, the chokepoint instrument becomes a pure financial-sector mechanism. "
    "Tests Brew/Eurasia 'effective control' thesis distinct from kinetic ladder. Resolution window: Tuesday IST.",
    status="watching"
)
set_last_updated(soh)
save("strait-of-hormuz", soh)

# ---------- IRGC ----------
irgc = load("irgc")
add_signal(irgc,
    "NO FRESH IRGC KINETIC SUNDAY — SATURDAY'S BURST UNREPEATED IN ~36 HOURS [CONFIRMED non-event via 4+ liveblog chains: UKMTO, CENTCOM, Reuters, CNN, Times of Israel]. "
    "No new UKMTO advisory beyond Saturday's 038-26 on container-ship projectile. Iranian lawmaker Ebrahim Azizi: 'whether the Strait is open or closed will be determined by the field, not by social media' — "
    "fresh RHETORIC aimed at Araghchi but not matched by new operational event. CENTCOM Sunday update repeats 23-vessel blockade figure without claiming additional interdictions. "
    "Tracks toward Sadjadpour 'warning-shot-for-leverage' branch at 36-hour mark. NB: ceiling signal for Monday Brent — $100+ would have required Sunday-kinetic repeat."
)
irgc["summary"] = (
    "Day 52 Sunday evening. KINETIC PAUSE AFTER SATURDAY BURST; CIVILIAN-APEX ENDORSEMENT INTACT. "
    "Saturday's multi-vessel sweep (Jag Arnav VLCC fast-boat fire, Sanmar Herald bridge-window damage, container-ship 'unknown projectile' = standoff munition not small-arms, Mein Schiff 4 cruise VHF threat) "
    "remains the operative kinetic event. SNSC's Saturday-evening ratification of IRGC's permission regime + $1/bbl fees + military/hostile-vessel denial gives the IRGC civilian-apex political cover. "
    "Sunday: no new ship fired on, no new UKMTO advisory beyond 038-26, CENTCOM repeats 23-vessel blockade figure without naming additional interdictions. "
    "Iranian lawmaker Azizi's 'field, not social media' Sunday line is rhetoric pointed at Araghchi rather than operational signal. Sadjadpour 72-hour test tracking 'thesis holds.'"
)
touch_edge(irgc, "strait-of-hormuz", count_delta=1)
set_last_updated(irgc)
save("irgc", irgc)

# ---------- ISRAEL ----------
israel = load("israel")
add_signal(israel,
    "WO (RES) BARAK KALFON KILLED BY HEZBOLLAH IED IN SOUTHERN LEBANON — FIRST IDF FATALITY UNDER 10-DAY CEASEFIRE [REPORTED multi-source: Times of Israel, JNS, Jerusalem Post, Ynet, The Media Line; "
    "sourcing tension on incident date — disclosure date Sunday is hard anchor]. Warrant Officer (res.) Barak Kalfon, 48, of 226th Reserve Paratroopers Brigade's 7056th Battalion (Adi, northern Israel), "
    "was killed in Jebbayn, southern Lebanon, when an IED detonated during a building-search operation. Three to nine other soldiers wounded (sourcing inconsistent — IDF spokesperson statement to be cross-checked). "
    "Kalfon was an engineer at Rafael. Times of Israel dates incident Friday April 17; The Media Line dates it Saturday April 18 ('one day after ceasefire'); public disclosure Sunday April 19. "
    "Kiryat Shmona on Israeli side: municipal protests against the ceasefire ran Sunday with a convoy to Jerusalem — domestic political pressure on Netanyahu from the north building. "
    "Defense ETF (ITA) Friday +1.3%; if a second incident this week surfaces, defense-budget pressure on Netanyahu re-engages and ITA likely +3-5% 1W."
)
israel["summary"] = (
    "Day 52 Sunday evening. CEASEFIRE FRAGILITY SHARPENS — FIRST IDF FATALITY UNDER 10-DAY WINDOW. "
    "WO (res.) Barak Kalfon, 48, killed by Hezbollah-attributed IED during building-search in Jebbayn, southern Lebanon. Disclosure Sunday April 19; incident date contested (Friday or Saturday). "
    "Three to nine soldiers wounded (sourcing inconsistent). PM Netanyahu condolence post Sunday. Kiryat Shmona protests + convoy to Jerusalem = domestic political pressure on Netanyahu from the north. "
    "Hezbollah SecGen Naim Qassem Sunday speech called the ceasefire 'an insult to Lebanon' but did NOT order rocket retaliation, did NOT name a kinetic timeline, did NOT invoke axis-of-resistance coordination. "
    "Israeli press (TOI, Haaretz, Ynet) clinical on Kalfon — public not in crisis mode on Lebanon yet (function of one death; second would change framing). "
    "Hormuz framing in Israeli press remains 'Iran's showdown with US' — Trump's problem, not Israel's. Smotrich/Ben-Gvir have not walked out of coalition through Day 3. ITA Friday +1.3%; "
    "second IDF fatality this week would re-engage defense-budget pressure and push ITA toward +3-5% 1W."
)
touch_edge(israel, "hezbollah", count_delta=1, context_append=f"{DATE} eve: Kalfon IED — first IDF fatality under 10-day ceasefire window; Hezbollah operational attribution.")
touch_edge(israel, "lebanon", count_delta=1)
set_last_updated(israel)
save("israel", israel)

# ---------- HEZBOLLAH ----------
hez = load("hezbollah")
add_signal(hez,
    "KALFON IED — HEZBOLLAH OPERATIONAL ATTRIBUTION; LOW-SIGNATURE KINETIC PERMITTED, ROCKET WAR NOT [CONFIRMED IDF probe attribution; reported non-remote detonation]. "
    "Pre-placed IED detonated during IDF building-search in Jebbayn, southern Lebanon. WO Barak Kalfon (res.) killed; multiple wounded. Sunday public disclosure. "
    "Hezbollah's operational posture under the 10-day ceasefire is now visible: low-signature kinetic permitted (pre-placed IEDs on building scans) + escalatory rhetoric permitted "
    "(Qassem Sunday speech) + open rocket war NOT permitted (zero rockets since ceasefire onset per IDF Homefront Command). Consistent with a ceasefire the organization publicly disavows but operationally accepts."
)
add_signal(hez,
    "NAIM QASSEM SUNDAY SPEECH — DEFIANT RHETORIC WITHOUT KINETIC ESCALATION ORDER [REPORTED via al-Manar primary; Times of Israel cross-reference]. "
    "Hezbollah SecGen Naim Qassem delivered Sunday April 19 speech calling the ceasefire arrangement 'an insult to Lebanon' and warning Hezbollah 'will not tolerate continued Israeli attacks while diplomatic efforts ongoing.' "
    "What Qassem did NOT do is the analytically load-bearing fact: he did NOT order rocket retaliation, did NOT name a kinetic-response timeline, did NOT invoke the Iran-nexus axis for coordinated action. "
    "Read alongside the Kalfon IED (Hezbollah operational attribution, low-signature) and continued zero-rocket count, posture is calibrated: visible defiance for the domestic Lebanese audience, "
    "operational acceptance of the ceasefire envelope."
)
hez["summary"] = (
    "Day 3 of 10-day ceasefire (Sunday evening). LOW-SIGNATURE KINETIC + DEFIANT RHETORIC + NO ROCKET WAR — POSTURE CALIBRATED. "
    "Hezbollah-attributed IED killed WO (res.) Barak Kalfon in Jebbayn during IDF building-search; first IDF fatality under the ceasefire window. SecGen Naim Qassem Sunday speech "
    "called the ceasefire 'an insult to Lebanon' but did NOT order rocket retaliation, did NOT name a kinetic timeline, did NOT invoke axis-of-resistance coordination. "
    "Zero Hezbollah rockets into Israeli territory since ceasefire onset (IDF Homefront Command logs per TOI liveblog). Hezbollah's rule-set under the ceasefire: pre-placed IEDs on building scans permitted, "
    "rhetoric permitted, open rocket war not permitted. The organisation publicly disavows the ceasefire while operationally accepting its core constraint. "
    "CSIS 'fragile ceasefire' near-term Hezbollah terrorism risk call is now inside the prediction window — Kalfon is one confirmed lethal action; a second would compound CSIS's fragility framing."
)
touch_edge(hez, "israel", count_delta=1, context_append=f"{DATE} eve: Kalfon IED — first IDF fatality under ceasefire; Qassem 'insult to Lebanon' speech without rocket order.")
touch_edge(hez, "lebanon", count_delta=1)
set_last_updated(hez)
save("hezbollah", hez)

# ---------- LEBANON ----------
lbn = load("lebanon")
add_signal(lbn,
    "FIRST IDF FATALITY UNDER 10-DAY CEASEFIRE — KALFON IED + QASSEM 'INSULT' SPEECH + KIRYAT SHMONA PROTESTS [REPORTED multi-source]. "
    "WO (res.) Barak Kalfon killed by Hezbollah-attributed IED in Jebbayn during IDF building-search; disclosure Sunday April 19. Three to nine wounded (sourcing inconsistent). "
    "Hezbollah SecGen Naim Qassem Sunday speech: ceasefire is 'an insult to Lebanon' but no rocket retaliation order, no kinetic timeline, no axis-of-resistance call. "
    "Israeli side: Kiryat Shmona municipal protests + convoy to Jerusalem Sunday = symmetric domestic dissatisfaction. Lebanese government statement not yet surfaced. "
    "Ceasefire's structural fragility (Hezbollah non-signatory, IDF in-country, non-withdrawal) is now testing under live conditions: ceasefire HOLDING in aggregate but with first lethal IDF event inside the window."
)
lbn["summary"] = (
    "Day 3 of 10-day ceasefire (Sunday evening). FRAGILITY SHARPENS — FIRST IDF FATALITY INSIDE WINDOW; CEASEFIRE HOLDS IN AGGREGATE. "
    "WO (res.) Barak Kalfon killed by Hezbollah-attributed IED during IDF building-search in Jebbayn; disclosure Sunday. SecGen Qassem Sunday: ceasefire 'an insult to Lebanon' "
    "without ordering rocket retaliation. Zero Hezbollah rockets into Israeli territory since ceasefire onset. Kiryat Shmona civilian protests + convoy to Jerusalem = symmetric domestic dissatisfaction. "
    "Friday April 17 IDF drone strike on motorcycle near Kounine remains separately tracked (1 dead). State Department's April 17 clarification — Trump's 'Israel PROHIBITED' framing applies only to "
    "offensive action and preserves Israel's self-defence lane — still defines the operational envelope. CSIS 'fragile ceasefire' Hezbollah terrorism risk call now activated by Kalfon (one lethal action); "
    "a second would compound CSIS framing and likely break the 10-day clock."
)
touch_edge(lbn, "israel", count_delta=1)
touch_edge(lbn, "hezbollah", count_delta=1)
set_last_updated(lbn)
save("lebanon", lbn)

# ---------- INDIA ----------
india = load("india")
add_signal(india,
    "INDIA MEA SUMMONS — IRAN HAS NOT REPLIED PUBLICLY 30+ HOURS LATER [CONFIRMED absence of Iranian MFA statement Sunday]. "
    "Iran's Foreign Ministry (Spokesperson Baghaei) has not published an official response to Saturday evening's Misri-Fathali demarche (Sanmar Herald + Jag Arnav). "
    "Tehran cannot produce a coherent civilian reply because the IRGC/Araghchi/Pezeshkian triangle is openly fractured. Jerusalem Post citing Iranian state TV reports IRGC-aligned commentators "
    "characterising Araghchi as 'idiot' (single-chain framing). The morning brief's india->iran weight-5.0 demarche edge holds with no downgrade justification; the absence of Iranian apology or "
    "commitment to resume facilitation IS the update."
)
add_signal(india,
    "INDIAN-DIASPORA GULF EVACUATION POSTURE — NO MEA ADVISORY UPGRADE SUNDAY [CONFIRMED non-event]. "
    "No Indian Ministry of External Affairs advisory upgrade from 'caution' to 'avoid non-essential travel' has been published Sunday for Gulf destinations; no Air India wide-body diversion notices; "
    "no Indian embassy (Tehran, Abu Dhabi, Doha, Riyadh, Muscat) has announced contact-registration campaigns. Reference point: ~8 million Indians in the Gulf; any evacuation planning would equal "
    "severe escalation assessment. The non-arrival of evacuation planning signals India's security establishment is not yet reading Saturday's kinetic as requiring civilian-protection posture. "
    "Confirmed by absence across MEA Twitter, Air India route-change notices, embassy websites."
)
india["summary"] = (
    "Day 52 Sunday evening. WAIVER T-0 IN ~9 HOURS (MONDAY 05:30 IST) + MEA SUMMONS UNANSWERED + NO EVACUATION POSTURE. "
    "MEA summons of Iranian Ambassador Fathali (Foreign Secretary Misri, 'deep concern' on Jag Arnav + Sanmar Herald, Saturday evening IST) — Iran has not publicly replied 30+ hours later; "
    "Tehran's IRGC/Araghchi/Pezeshkian fracture means no coherent civilian reply channel. India has not upgraded MEA travel advisory or initiated embassy contact-registration for the ~8M Gulf diaspora — "
    "security establishment is NOT reading Saturday's kinetic as civilian-protection level. "
    "Bessent's Iranian-oil waiver non-renewal effective 05:30 IST Monday; Russian 30-day side-waiver protects Russian supply lane. Reliance compliance rejections of Derya and Lenore (loaded post-Mar 20 OFAC cut-off) "
    "set the benchmark; ~4M bbl waiver-window total discharged via Jaya (IOC) and Felicity (RIL); IOC reportedly indicated 'no further Iranian purchases.' Yuan-settlement via ICICI Shanghai is the payments channel. "
    "GIFT Nifty last reading 24,186 (April 16 close); morning's triple-headwind setup (SNSC + MEA + Brent reversal) intact. Sunday Globex Brent ~$98 = imported-inflation tail re-engages within 18 hours of Monday open. "
    "Adani Ports (Mundra/Krishnapatnam Iran-Gulf exposure) at risk -1.5 to -2.5% Monday if Brent holds $98; Bank Nifty downside if 10Y G-Sec gaps through 7.00%."
)
touch_edge(india, "iran", count_delta=1)
touch_edge(india, "brent-crude", count_delta=1)
set_last_updated(india)
save("india", india)

# ---------- UNITED STATES ----------
us = load("united-states")
add_signal(us,
    "CENTCOM SUNDAY POSTURE UPDATE REPEATS 23-VESSEL BLOCKADE FIGURE — NO NEW KINETIC CLAIM [CONFIRMED non-event]. "
    "CENTCOM Sunday April 19 statements repeat the standing 23-vessel turned/inspected blockade figure without naming additional interdictions or specifically responding to Saturday's "
    "Jag Arnav/Sanmar Herald/container-projectile/Mein Schiff 4 incidents. The 'Iran executes reciprocal measures' trigger CENTCOM-corroboration bar remains uncleared at ~36 hours. "
    "White House has not chosen an outlet to brief first on Sunday's developments — quiet strategy continues, letting physical blockade and 'productive conversations' rhetoric do the work. "
    "Witkoff/Vance/Kushner have not publicly travelled, tweeted travel, or been tracked via flight manifests through Sunday evening — Islamabad Round 2 deployment-signal condition unmet."
)
add_signal(us,
    "WSJ EDITORIAL BOARD: 'US PLAN HAS FAILED' + PUSH FOR ADDITIONAL STRIKES [REPORTED — hawkish-right editorial position distinct from WSJ news desk]. "
    "WSJ editorial board declared Sunday April 19 that 'the US plan has failed' and pushed for additional strikes. Notable because WSJ news desk continues factual reporting (Iannotta team) — "
    "the editorial split widens. Combined with Fox/Keane segment ('Iran overplayed hand') and Hannity framing, US conservative media is calling for escalation while CNN/WaPo are in 'far from final agreement' mode. "
    "AP/Reuters/Bloomberg wire copy neutral. Administration's preferred messaging channel has not been activated for the Sunday cycle — interpret as wanting kinetic and rhetoric to run on their own momentum "
    "rather than be claimed by any specific White House line."
)
us["summary"] = (
    "Day 52 Sunday evening. CENTCOM SILENT ON SATURDAY-SPECIFIC KINETIC; WHITE HOUSE QUIET; ISLAMABAD DELEGATION UNMOVED; WSJ EDITORIAL BOARD CALLS FOR MORE STRIKES. "
    "CENTCOM Sunday posture update repeats 23-vessel blockade figure without naming additional interdictions or responding to Saturday's UKMTO chain (Jag Arnav VLCC, Sanmar Herald, "
    "container-projectile, Mein Schiff 4 cruise threat). The 'Iran executes reciprocal measures' trigger 2+ operational-source bar remains uncleared 36+ hours after UKMTO. "
    "Witkoff, Vance, Kushner have not publicly travelled or been tracked via flight manifests through Sunday — Islamabad Round 2 deployment-signal condition unmet. "
    "Bessent confirmation (Apr 15 'we will not be renewing' on Iranian oil) holds; Russian 30-day side-waiver protects India's Russian supply lane. "
    "Trump's Saturday-dated 'Iran got a little cute … they can't blackmail us' + 'talks working out really well' has not updated Sunday. "
    "WSJ editorial board Sunday declared 'US plan has failed' and pushed for additional strikes — hawkish-right editorial split from WSJ news desk's factual reporting; "
    "Fox/Keane/Hannity calling for escalation; CNN/WaPo in 'far from final agreement' mode. Administration messaging channel not chosen — strategy is to let blockade and 'productive conversations' rhetoric run on their own."
)
touch_edge(us, "iran", count_delta=1)
set_last_updated(us)
save("united-states", us)

# ---------- UAE ----------
uae = load("uae")
add_signal(uae,
    "ADNOC CHAIRMAN AL JABER PUBLIC HARDENING — 'STRAIT OF HORMUZ NOT OPEN, NEEDS TO BE OPEN UNCONDITIONALLY' [REPORTED single-chain Sunday; pending Monday Al Monitor / The National corroboration]. "
    "Sultan Al Jaber, ADNOC chairman and former COP28 president, publicly declared Sunday April 19 that the Strait is 'not open' and must be opened 'unconditionally.' "
    "Material hardening from morning brief's 'conspicuously quiet' UAE posture — UAE moves from two-track (hawkish-on-blockade Al Jaber + diplomatic Mansour-Ghalibaf parliamentary channel) "
    "to publicly hawkish through ADNOC chairman channel. Timing — Sunday before waiver expiry and before any Islamabad Round 2 — suggests UAE pre-positioning a public tough line "
    "rather than playing quiet convenor. The National (Abu Dhabi) carries Al Jaber's framing with editorial support; UAE information space aligned against Iran on chokepoint rights. "
    "Note: UAE was previously reported (via Times of Israel UAE sourcing) as internally 'pushing for military op to reopen Hormuz, willing to take part' — Sunday Al Jaber moves part of that posture into public record."
)
uae["summary"] = (
    "Day 52 Sunday evening. ADNOC AL JABER SUNDAY HARDENING — UAE MOVES FROM TWO-TRACK TO PUBLICLY HAWKISH ON HORMUZ. "
    "ADNOC chairman Sultan Al Jaber publicly: 'Strait of Hormuz not open, needs to be open unconditionally' (single-chain Sunday, pending Monday corroboration). "
    "Material hardening from prior 'conspicuously quiet' posture — UAE now combines the parliamentary diplomatic channel (Mansour-Ghalibaf x2 Apr 15+17) with on-record public hawkishness via ADNOC. "
    "The National (Abu Dhabi) editorial-supports Al Jaber framing; UAE information space aligned against Iran on chokepoint rights. "
    "Gulf diplomatic matrix Sunday evening: Saudi mediator-adjacent (Faisal-Araghchi 3 calls Apr 9-14), Qatar neutral broker, Oman silent, UAE now publicly hardening — four-way Gulf posture favours diplomatic optionality "
    "while removing UAE's 'quiet convener' optionality. Domestic fuel inflation ongoing (+31% petrol, +72% diesel from earlier crisis peak); IMF MENA 1.1% growth projection still operative. "
    "ADNOC refinery Ruwais shutdown (922K bpd) status unchanged Sunday."
)
touch_edge(uae, "strait-of-hormuz",
    count_delta=1,
    weight_delta=+1.0,
    type_rename="public_hardening_chokepoint_rights",
    context_append=f"{DATE} eve: Al Jaber Sunday 'not open, needs to be open unconditionally' — first UAE on-record public hardening; pending Monday corroboration."
)
touch_edge(uae, "iran", count_delta=1, context_append=f"{DATE} eve: ADNOC Al Jaber public hardening cuts against Mansour-Ghalibaf parliamentary track.")
set_last_updated(uae)
save("uae", uae)

# ---------- SAUDI ARABIA ----------
ksa = load("saudi-arabia")
add_signal(ksa,
    "SAUDI FM FAISAL-ARAGHCHI THREE CALLS APR 9-14 — SAUDI MEDIATOR-ADJACENT BUT NOT ISLAMABAD PARTY [REPORTED via ACLED Gulf-posture tracker; Saudi MFA readouts]. "
    "Per ACLED's Gulf mediation tracker (April 2026), Saudi Foreign Minister Prince Faisal bin Farhan and Iranian FM Araghchi had three phone calls between April 9 and April 14: Apr 9, Apr 11, Apr 14. "
    "This corrects the morning brief's earlier 'two confirmed calls' framing — public record now stands at three. Saudi Arabia is positioning as mediator-adjacent — not a party to the US-Iran Islamabad track — "
    "but is demonstrably open to Iran on the ministerial channel while welcoming the ceasefire framework. This establishes a separate Gulf diplomatic lane that can either support Islamabad Round 2 (if it happens) "
    "or substitute for it (if Araghchi's institutional authority further erodes after Sunday's open factional standoff with hardline state media). Does not alter Saturday's kinetic calculus."
)
ksa["summary"] = (
    "Day 52 Sunday evening. THREE FAISAL-ARAGHCHI CALLS APR 9-14 (NOT TWO) — SAUDI MEDIATOR-ADJACENT LANE EXPANDS. "
    "Public-record evidence: three confirmed Saudi FM Prince Faisal bin Farhan - Iranian FM Araghchi calls (Apr 9, Apr 11, Apr 14) per ACLED's Gulf mediation tracker — corrects prior 'two-call' framing. "
    "Saudi Arabia is positioning as mediator-adjacent — not a party to the US-Iran Islamabad track — but demonstrably open to Iran on the ministerial channel while welcoming the ceasefire framework. "
    "Establishes a separate Gulf diplomatic lane that can either support Islamabad Round 2 (if it happens) or substitute for it (if Araghchi's institutional authority further erodes after Sunday's "
    "open factional standoff with Kayhan/Tasnim/Fars). Saudi Arabia positioning for POST-CEASEFIRE convener role opened by US absence from Macron-Starmer summit (April 17). "
    "Arab News maintained 'urged US to end blockade' framing through Sunday — break-from-Washington posture preserved. East-West pipeline fully restored (700K bpd recovered post-April 9 drone strike); "
    "Yanbu port bottleneck binding constraint (4-4.5M bpd vs 7M pipeline). Physical-futures gap $40 (Dated $132 vs futures $91) continues to price port as binding. "
    "TASI 11,554.16 (-0.3% 1D, +5.6% 1M). Pakistan 13,000 troops + fighter jets security intact. Sadara $20B JV at zero; $3.7B debt grace period expires June 15."
)
existing_iran = any(e.get("to") == "iran" for e in ksa.get("edges", []))
if not existing_iran:
    add_edge(ksa, "iran", "diplomatic_mediation_adjacent",
        "Three Faisal-Araghchi calls Apr 9-14 (Apr 9, Apr 11, Apr 14) per ACLED Gulf mediation tracker. Saudi mediator-adjacent — open to Iran ministerial channel while welcoming ceasefire framework; "
        "separate Gulf diplomatic lane that can support or substitute Islamabad Round 2.",
        weight=5.0)
else:
    touch_edge(ksa, "iran", count_delta=1, context_append=f"{DATE} eve: Faisal-Araghchi 3 calls Apr 9-14 confirmed (corrects prior 2-call framing).")
set_last_updated(ksa)
save("saudi-arabia", ksa)

# ---------- PAKISTAN ----------
pak = load("pakistan")
add_signal(pak,
    "ISLAMABAD ROUND 2 — STILL NO NAMED US DELEGATION TRAVEL THROUGH SUNDAY EVENING [CONFIRMED absence]. "
    "White House (Apr 14) said 'future talks under discussion but nothing scheduled.' Pakistani sources and aggregator coverage say Round 2 'within days' and 'very likely,' with PM Shehbaz Sharif's Apr 14-16 "
    "Gulf tour (Saudi, Qatar, Türkiye) reportedly shoring up regional support and Dar + Munir running Pakistani mediation. Witkoff, Vance, Kushner have NOT publicly travelled, tweeted travel, or been tracked "
    "via flight manifests through Sunday evening. Load-bearing forcing function: April 21-22 ceasefire expiry. The IRGC-Araghchi rift (Saturday kinetic + Sunday state-media attack + no Pezeshkian defense + Sunday Araghchi offensive X posts) "
    "means Iran cannot present a unified negotiating mandate to any Round 2 convened before that rift resolves."
)
set_last_updated(pak)
save("pakistan", pak)

# ---------- HOUTHIS ----------
hou = load("houthis")
add_signal(hou,
    "DAY 54 NON-MIRROR — NO HOUTHI KINETIC AFTER IRAN'S SATURDAY KINETIC + SUNDAY SNSC + SUNDAY KALFON IED [CONFIRMED non-event]. "
    "Through Sunday evening April 19, no Houthi kinetic in Red Sea or Bab-el-Mandeb. MARAD advisory 2026-006 remains the governing notice. Mansour's 'Bab al-Mandeb is among our options' "
    "remains conditional on 'any Gulf state directly involved' — Saturday IRGC kinetic did not meet that condition. The 54-day silence now exceeds any prior Iran-nexus conflict cycle. "
    "Soufan coordination-decay thesis strengthens by another day. The 'most important non-event of Sunday was the one in Bab-el-Mandeb' (Soufan IntelBrief framing). "
    "houthis -> shipping-tankers edge stepped to 9.5 in morning update; further step below 9.0 deferred per intel guidance until Tuesday IST-or-later if quiet persists."
)
hou["summary"] = (
    "Day 54 of non-mirroring (Sunday evening). NON-EVENT HARDENS — SOUFAN COORDINATION-DECAY THESIS STRENGTHENS. "
    "No Houthi kinetic in Red Sea or Bab-el-Mandeb through Sunday April 19. MARAD advisory 2026-006 is the governing notice. Iran's Saturday IRGC kinetic + SNSC ratification + Sunday Kalfon Hezbollah IED = "
    "axis-of-resistance is acting SEQUENTIALLY (Hezbollah Sunday, IRGC Saturday, Houthis quiet) NOT SIMULTANEOUSLY. Mansour's 'Bab al-Mandeb among our options' conditional on 'any Gulf state directly involved' "
    "has not been met by Saturday's IRGC vs commercial-shipping action. 54-day silence exceeds any prior Iran-nexus conflict cycle. "
    "Last confirmed Houthi maritime kinetic: April 12 skiff approach near Hodeidah, deterred by crew flare. Soufan IntelBrief framing: 'most important non-event of Sunday was in Bab-el-Mandeb.' "
    "Edge weight to shipping-tankers stepped 10.0 -> 9.5 in morning update; further step below 9.0 defensible if Tuesday IST still has no kinetic."
)
touch_edge(hou, "red-sea", count_delta=1)
set_last_updated(hou)
save("houthis", hou)

# ---------- RED SEA ----------
rs = load("red-sea")
add_signal(rs,
    "DAY 54 QUIET — NO HOUTHI KINETIC AFTER SATURDAY IRGC FIRE + SUNDAY KALFON IED [CONFIRMED non-event]. "
    "MARAD 2026-006 active; UKMTO regional threat-level MODERATE; no confirmed shift in maritime threat environment. Soufan coordination-decay thesis strengthens by another day. "
    "Axis-of-resistance acting sequentially (Hezbollah Sunday IED + Qassem speech, IRGC Saturday kinetic, Houthis quiet) — not simultaneously. "
    "Editor cascade implication: Red Sea risk premium decoupling from Hormuz risk premium — for the first time in 54 days, the two chokepoints can be priced independently."
)
touch_edge(rs, "houthis", count_delta=1)
set_last_updated(rs)
save("red-sea", rs)

# ---------- SHIPPING TANKERS ----------
ships = load("shipping-tankers")
add_signal(ships,
    "FRONTLINE +5.6% FRIDAY VALIDATED AS LEADING SIGNAL — TANKERS DIVERGED FROM PAPER OIL ON SAME SESSION [CONFIRMED tradeable divergence]. "
    "Frontline +5.6% Friday on a day Brent crashed -9.1% — paper-oil priced an Iranian-declaration thesis that physical-tanker-rate strength invalidated within the same session. "
    "VLCC TD3C spot rates held WS 513 Friday (~$130-150K/day earnings — moderated from WS 600+ peak but multiples of the 2-year average ~WS 50). Frontline fleet is 100% VLCC + Suezmax, "
    "Hormuz-transit-dominant. Sunday SNSC ratification + container-ship projectile + cruise-liner VHF threat = war-risk premium re-widens Monday, not deflates. "
    "Expected Monday: Frontline +2-4% as AWRP reprices; VLCC TD3C spot toward WS 550-600. If a second cruise-class incident corroborates (Mein Schiff 4 was 1 event), tanker rates double on insurance-denial premium. "
    "Tradeable signal: the day Frontline diverges from Brent is a day to trust tankers and fade Brent."
)
add_signal(ships,
    "SUNDAY GLOBEX BRENT ~$98 + LLOYD'S AWRP NO SUNDAY REPUBLISH = MONDAY AWRP STEP-UP 1.2-1.8% LIKELY [REPORTED]. "
    "AWRP held ~1% hull through Friday despite Saturday kinetic — insurers had not yet repriced Sunday. Monday London open (07:00 IST) is the next hard tell. "
    "AWRP step to 1.5%+ likely; passenger-vessel-scope expansion via Mein Schiff 4 master report creates IMO-level emergency potential if a second cruise incident corroborates."
)
touch_edge(ships, "marine-war-risk-insurance", count_delta=1, context_append=f"{DATE} eve: AWRP no Sunday republish; Monday step expected 1.2-1.8% on Saturday kinetic + SNSC.")
touch_edge(ships, "strait-of-hormuz", count_delta=1)
existing_brent = any(e.get("to") == "brent-crude" for e in ships.get("edges", []))
if not existing_brent:
    add_edge(ships, "brent-crude", "leading_signal_physical_tanker_rates",
        "Frontline +5.6% Friday on Brent -9.1% same session is the tradeable divergence: physical-tanker-rate strength leads paper-oil reversal by 24-48 hours. "
        "VLCC TD3C WS 513 with $130-150K/day earnings vs ~WS 50 nominal 2-year average. The day Frontline diverges from Brent is a day to trust tankers and fade Brent.",
        weight=5.5)
else:
    touch_edge(ships, "brent-crude", count_delta=1, context_append=f"{DATE} eve: Frontline +5.6% Friday vs Brent -9.1% validated as leading signal; Sunday Globex $98 confirms paper catching tankers.")
set_last_updated(ships)
save("shipping-tankers", ships)

# ---------- MARINE WAR RISK INSURANCE ----------
mwri = load("marine-war-risk-insurance")
add_signal(mwri,
    "AWRP NO SUNDAY REPUBLISH — MONDAY LONDON OPEN IS NEXT HARD TELL [REPORTED]. "
    "Lloyd's AWRP held ~1% hull through Friday; insurers did NOT step UP on Saturday's IRGC kinetic during weekend. Monday London open (07:00 IST) republish expected at 1.2-1.8%; "
    "2%+ if cruise-class incident corroborates (Mein Schiff 4 master-report only as of Sunday). Araghchi Sunday X posts explicitly named the insurance market — not the IRGC kinetic — "
    "as the operational chokepoint mechanism: 'Ships hesitate because insurers fear the war of choice you initiated — not Iran.' Iran's civilian wing now sees insurance as the leverage point."
)
mwri["summary"] = (
    "Day 52 Sunday evening. AWRP ~1% HULL FRIDAY UNCHANGED; MONDAY LONDON OPEN IS NEXT REPRICE. "
    "Lloyd's AWRP held ~1% hull through Friday despite Saturday IRGC kinetic — insurers did NOT step UP over the weekend. Morning brief expected Monday step to 1.2-1.8%; "
    "evening sharpens — Sunday Globex Brent ~$98 + Saturday container-projectile + Mein Schiff 4 cruise-VHF threat = passenger-class scope expansion creates IMO-level emergency potential. "
    "AWRP is the binding economic chokepoint mechanism Iran's civilian wing has now publicly named (Araghchi Sunday X posts: 'Ships hesitate because insurers fear the war of choice you initiated — not Iran'). "
    "Translation: even if Iran officially says 'open,' insurers don't underwrite + ship-owners don't transit + paper-physical gap stays open. "
    "The chokepoint instrument has become a financial-sector mechanism distinct from the kinetic ladder. Watch: 1.5% AWRP republish + Brent $100+ = pure insurance-driven price action."
)
touch_edge(mwri, "shipping-tankers", count_delta=1)
touch_edge(mwri, "strait-of-hormuz", count_delta=1)
set_last_updated(mwri)
save("marine-war-risk-insurance", mwri)

# ---------- BRENT CRUDE ----------
brent = load("brent-crude")
add_signal(brent,
    "SUNDAY GLOBEX BRENT INDICATIVELY ~$98 — MORNING +5-8% RE-OPEN THESIS VINDICATED AT UPPER EDGE [REPORTED via Investing.com Sunday quote + specialist aggregator]. "
    "Sunday Globex (CME ICE) indicatively ~$98 for June Brent = +8.4% over Friday wire-ICE $90.38 / +6.7% over yfinance $91.87. Morning brief base case: +5-8% -> $93-97.50; severe tail: $100+. "
    "Sunday print sits ON THE SEAM between base and severe cases — i.e., escalation pricing at upper edge of 'standard brinkmanship' band but not at the tail. "
    "The 'Sunday quiet' non-event (no fresh IRGC fire) provides a CEILING — $100+ would have required Sunday-kinetic repeat. Paper-physical gap closing BY PAPER RISING toward physical (Dated ~$132 Thursday), "
    "not physical falling — direction the morning brief argued. WTI Globex indicatively ~$89-90 (consistent +8%). Lloyd's AWRP no Sunday republish; Monday London open is next hard-money tell. "
    "If AWRP steps to 1.5%+ hull at London open, Brent prints $100+; if AWRP holds 1.0-1.2%, Brent consolidates $96-98. "
    "Goldman ($90 Q2 base / $115 Q4 severe Apr 15 note): paper already converging upward to physical at Sunday Globex; Goldman base case visibly under pressure within 4 days. "
    "Morgan Stanley ($110 Q2): vindicated on direction — confirmed if Brent above $100 within 10 sessions."
)
add_snapshot(brent,
    "Sunday Globex indicatively ~$98 (June Brent) — +8.4% over Friday wire $90.38",
    "Morning +5-8% re-open thesis vindicated at upper edge by Sunday Globex; Sunday quiet provides CEILING (no new kinetic needed for tail $100+)",
    "Paper-physical convergence direction confirmed — paper rising to physical (Dated ~$132). Lloyd's AWRP republish Monday London open is next discriminator: >=1.5% -> $100+; 1.0-1.2% -> $96-98 consolidation."
)
brent["current"]["price"] = "$91.87/bbl (yfinance Fri); $90.38 wire-ICE Fri; ~$98 Sunday Globex indicative"
brent["current"]["delta_1d"] = "-9.1% (wire Fri) / -7.6% (yfinance Fri); +8.4% Sunday Globex over wire close"
touch_edge(brent, "strait-of-hormuz", count_delta=1)
touch_edge(brent, "iran", count_delta=1)
set_last_updated(brent)
save("brent-crude", brent)

# ---------- GOLD ----------
gold = load("gold")
add_signal(gold,
    "GOLD +2.0% TO $4,879.60 FRIDAY — REGIME SHIFT CONFIRMED ON RISK-ON DAY [CONFIRMED via fresh yfinance pull 17:12 IST Sunday]. "
    "Friday April 17 settle: gold $4,879.60 (+2.0% 1D, -0.2% 1M, +2.5% 3M). On a day where S&P hit a record close (+1.2%), VIX fell -2.6% to a war-era low, and Brent crashed -9.1%, "
    "the traditional gold playbook says gold should have been flat to negative (risk-on sheds hedge bids; real yields competitive). Instead gold went UP 2.0% to a fresh post-crisis high. "
    "Causal decomposition: DXY -0.1% explains ~0.3%; US 10Y -1.5% to 4.25% explains ~0.3-0.4%; ~1.3% UNEXPLAINED by conventional drivers. "
    "Consistent with central-bank (PBOC, RBI, CBR, TCMB, CBN) structural accumulation that is price-insensitive — flagged since April 9. "
    "Araghchi's offensive Sunday posture sharpens the regime-shift read: a sanctions-isolated nation's ability to mobilize non-USD clearing (Yuan via ICICI Shanghai for Indian Iran-crude payments) "
    "during crisis is LIVE — accelerates structural gold bid on the reserve-diversification channel. The crisis-resolution scenario that would SELL gold in the old regime is now AMBIGUOUS for gold. "
    "The crisis-escalation scenario is unambiguously gold-positive (path to $5,100 by mid-May). Gold is no longer the classic 'crisis goes away = gold goes down' trade — it is the 'dollar-hegemony-contestation continues = gold accumulates' trade."
)
gold["current"] = {
    "price": "$4,879.60/oz (Friday April 17 settle, fresh evening yfinance pull 17:12 IST)",
    "delta_1d": "+2.0%",
    "delta_1m": "-0.2%",
    "delta_3m": "+2.5%"
}
add_snapshot(gold,
    "$4,879.60/oz Friday close (+2.0% on a risk-on session)",
    "REGIME SHIFT CONFIRMED — gold UP on risk-on day (S&P record, VIX war-era low, Brent crash) is structurally INCOMPATIBLE with safe-haven framework; central-bank accumulation dominant",
    "DXY -0.1% explains 0.3%; 10Y -1.5% explains 0.3-0.4%; ~1.3% unexplained by conventional drivers. PBOC/RBI/CBR structural accumulation thesis confirmed. Path to $5,100 mid-May on escalation; $4,800+ holds even on crisis resolution."
)
gold["summary"] = (
    "Day 52 Sunday evening. REGIME SHIFT CONFIRMED — gold +2.0% to $4,879.60 Friday on a risk-on day. "
    "S&P hit record (+1.2%), VIX war-era low (17.48 -2.6%), Brent crashed (-9.1%) — traditional safe-haven playbook says gold should have been flat to negative. Instead gold went UP 2.0% to a fresh post-crisis high. "
    "Causal decomposition leaves ~1.3% unexplained by conventional drivers (DXY, 10Y) — consistent with PBOC/RBI/CBR/TCMB/CBN structural central-bank accumulation that is price-insensitive. "
    "Sunday's Araghchi-vs-Trump-vs-IRGC-vs-insurance-market standoff sharpens the read: a sanctions-isolated nation's ability to mobilize non-USD clearing (Yuan via ICICI Shanghai) during crisis is LIVE — "
    "accelerates structural gold bid on the reserve-diversification channel. Gold is no longer the classic 'crisis resolves = gold sells' trade — it is the 'dollar-hegemony-contestation continues = gold accumulates' trade. "
    "The crisis-resolution scenario is now AMBIGUOUS for gold (resolution reduces tail-risk but does not reverse central-bank accumulation; gold can hold $4,800+ through resolution). "
    "Crisis-escalation scenario is unambiguously gold-positive — path to $5,100 by mid-May. Fed April 30 FOMC 11 days out; soft April CPI (May 13) reinforces real-yield-down narrative independent of crisis."
)
set_last_updated(gold)
save("gold", gold)

# ---------- SP-500 ----------
sp = load("sp-500")
add_signal(sp,
    "VIX FUTURES 19-20 SUNDAY VS FRIDAY CASH 17.48 — DIRECTIONALLY UP, MILD MAGNITUDE; CASH RE-MARK MONDAY EXPECTED 20-22 [REPORTED CME VX front-month screen]. "
    "VIX futures front-month 19-20 handle Sunday evening vs Friday cash 17.48 = +~15% directional. Mild for an oil move of Sunday Globex's magnitude — "
    "in a 2019-Saudi-Aramco-analogue frame, this oil move would push VIX futures into 22-25 handle. Two readings: (a) vol market treating Saturday's kinetic as still contained by Sunday-quiet (no further IRGC fire); "
    "(b) vol-sellers underhedged and Monday cash VIX gaps higher when dealers re-mark. Lean (b) — 17.48 Friday cash was war-era low, structurally mis-priced for kinetic-resumption weekend. "
    "ES (S&P 500 fut) Sunday Globex indicatively -0.5 to -0.8% pre-open. Crisis-linked component of Friday's +1.2% (~0.5%) is structurally fastest to unwind on Monday gap-down; "
    "non-crisis 0.7% (Q1 earnings momentum, AI/Gemini, semis) is stickier. Expect S&P -0.5 to -1.0% Monday open but rebuild intra-week on earnings."
)
sp["summary"] = (
    "Day 52 Sunday evening. VIX FUTURES 19-20 (+~15% over Friday cash 17.48) — DIRECTIONALLY UP, MILD MAGNITUDE; CASH RE-MARK MONDAY 20-22 EXPECTED. "
    "Friday April 17 close: S&P 500 7,126.06 record (+1.2%); NASDAQ 24,468.48 +1.5% (12-day win streak longest since 1992); Dow 49,447.43 +1.8%. VIX 17.48 (-2.6% war-era low). "
    "Sunday Globex: ES indicatively -0.5 to -0.8% pre-open; VIX futures 19-20 directionally consistent with oil move but mild for the magnitude (a 2019-Aramco-analogue would push 22-25). "
    "Reading: vol-sellers underhedged over the weekend; Monday cash VIX likely re-marks 20-22. Crisis-linked ~0.5% S&P / ~0.6% NASDAQ component fastest to unwind; "
    "non-crisis 0.7%/0.9% (Q1 earnings momentum, AI/Gemini refresh, SMH +2.1% on Taiwan/Samsung capacity) is stickier. Expected Monday open: S&P -0.5 to -1.0%, NASDAQ -0.8 to -1.3%. "
    "What breaks the thesis: VIX cash 22+ AND oil $98+ for 3 sessions = crisis component re-prices beyond 0.5% allocation, S&P could lose 2-3% in first week; "
    "Islamabad delegation named + ceasefire framework = S&P fresh records within days on earnings momentum carry."
)
sp["current"]["vix"] = "17.48 Fri cash; 19-20 VIX futures Sunday; expected 20-22 cash re-mark Monday"
set_last_updated(sp)
save("sp-500", sp)

# ---------- NIFTY 50 ----------
nifty = load("nifty-50")
add_signal(nifty,
    "EVENING DOWNSIDE-SKEW WIDENING ON ARAGHCHI SUNDAY OFFENSIVE POSTURE [REPORTED]. "
    "Morning brief base case: -0.6 to -1.2% Monday open -> 24,060-24,210. Evening upgrade: Araghchi's offensive Sunday X posts (not silent, not deposed, not defended by Pezeshkian — directly attacking Trump) = "
    "Iran has no single negotiating voice. Downside skew widens slightly: -1.0 to -1.5% -> 23,988-24,109. Key technical: 24,050 (200-DMA) — break below intraday triggers algo selling. "
    "Sunday Globex Brent ~$98 holds -> imported-inflation tail re-engages within 18 hours of Monday open. OMCs (IOC, BPCL, HPCL): expect -2 to -3.5% on Brent gap + Reliance Derya/Lenore compliance benchmark. "
    "Adani Ports: Mundra/Krishnapatnam Iran-Gulf exposure = -1.5 to -2.5% if Brent holds $98. Bank Nifty: direction depends on yield curve — India 10Y G-Sec gapping through 7.00% = banks -1 to -2%. "
    "Reversibility: US delegation named in Islamabad + no further IRGC kinetic by Tuesday close = Nifty recovers Friday's +0.6% by end of week."
)
set_last_updated(nifty)
save("nifty-50", nifty)

# ---------- INR USD ----------
inr = load("inr-usd")
add_signal(inr,
    "MONDAY RE-TEST RS93+ EXPECTED; INTRADAY RS93.50+ IF BRENT $100+ [REPORTED]. "
    "Brent Globex $98 -> INR imported-inflation tail re-engages within 18 hours of Monday open. MEA summons = political-nexus signal, not FX-mechanical (marginally INR-negative within noise). "
    "Waiver T-0 + $1/bbl Iranian fee + Russian 30-day side-waiver = mixed: Russian supply protected = INR-supportive; Iranian flows frozen = INR-negative on marginal-barrel price. "
    "Expected Monday: USD/INR 92.80-93.10 open (INR -0.25 to -0.6%); Rs93.50+ intraday if Brent prints $100+. "
    "RBI intervention lane: NDF position caps ($100M/bank) effective April 10 = macro-prudential tool already deployed. A second tool (special dollar-swap window, or onshore forward ceiling) would signal escalated concern."
)
set_last_updated(inr)
save("inr-usd", inr)

# ---------- US 10Y YIELD ----------
us10y = load("us-10y-yield")
add_signal(us10y,
    "MONDAY GAP UP 5-8BPS EXPECTED ON BRENT REVERSAL [REPORTED]. "
    "Friday's -1.5% (to 4.25%): Brent crash re-priced oil-inflation tails; Fed cut probability at June FOMC moved from ~35% to ~48% (CME FedWatch); 10Y rallied from 4.31% intraday to 4.25% close on dovish re-read. "
    "Monday gap: Brent Globex $98 = oil-inflation tail re-engages -> Fed cut probability back down to ~35% -> 10Y sells off. Expected: 4.30-4.33%; gap UP ~5-8bps. "
    "Bond market is fastest-mover — Monday open is the first tradeable re-price. Pairs with gold's regime-shift read: if 10Y gaps UP and gold ALSO gaps UP, the central-bank accumulation thesis is the dominant marginal driver."
)
set_last_updated(us10y)
save("us-10y-yield", us10y)

# ---------- EUROPEAN TTF GAS ----------
ttf = load("european-ttf-gas")
add_signal(ttf,
    "MONDAY OPEN AGAINST SNSC + RAS LAFFAN 3-5YR + AL JABER HARDENING; STRUCTURAL FLOOR EUR45-50 LIKELY [REPORTED]. "
    "TTF Friday close EUR41.25/MWh (-1.96% 1D; -26% 1M; peaked EUR56 April 13). No Sunday cash print (closed). Monday opens against three Sunday-evening structural pressures: "
    "(1) SNSC ratification re-imposes $1/bbl Iranian fee + 'transit certificates' regime; (2) Ras Laffan partial restart North <1 month, South late summer, Trains 4/6 3-5 years (QatarEnergy CEO Al-Kaabi); "
    "(3) UAE ADNOC Al Jaber Sunday public hardening on chokepoint rights. Structural floor likely re-establishes EUR45-50 Monday. If cruise/container incidents continue (Mein Schiff 4 was 1; second triggers IMO-level), EUR55+. "
    "Cheniere LNG -4.4% Friday on TTF-JKM compression on ceasefire optimism = mispriced; TTF re-widening Monday lifts Cheniere. German industrial press most alarmist European voice; DAX gap-down Monday partly on TTF, not just crisis."
)
set_last_updated(ttf)
save("european-ttf-gas", ttf)

# ---------- FERTILIZER UREA ----------
urea = load("fertilizer-urea")
add_signal(urea,
    "EVENING CONFIRMATION: CF MONDAY GAP-UP SETUP — ARAGHCHI SUNDAY POSTS DO NOT REBOOT NITROGEN [CONFIRMED]. "
    "CF Industries Friday -9.6% on pure deal-optimism error. Urea (Yuzhny FOB) $713/T (+16.8% 1M, +75% YoY); Profercy World Nitrogen Index 352.95 (highest since May 2022). "
    "20% of seaborne ammonia + one-third of seaborne urea via Hormuz remain priced-in as risk. Sunday SNSC ratification + Araghchi's Sunday X posts framing chokepoint as insurance-market problem "
    "do NOT reboot frozen Qatar/UAE/Saudi/Bahrain nitrogen exports — those require 6-18 months even post-resolution. "
    "Expected Monday: CF +5-8% gap-up base ($118-122); +8-12% upside if Brent $100+ ($122-126); structural floor on CF $105 even in full-resolution case (Ras Laffan recovery 3-5 years). "
    "Nutrien +3-5% Monday on nitrogen-complex sympathy. If TTF >EUR45/MWh Monday, European industrial gas cost = key nitrogen input cost re-rates further."
)
set_last_updated(urea)
save("fertilizer-urea", urea)

print("Evening graph node update complete.")
