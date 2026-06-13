#!/usr/bin/env python3
"""
Payloads for the 2026-06-07 (Sunday morning) graph update.
Inputs: staging/2026-06-07-morning/intel.md + markets.md

CONTEXT: Sunday — global cash & futures markets CLOSED. Friday 5 June closes were
already encoded in the 2026-06-06 run; they are NOT re-encoded here. Genuinely new
material this window:
  B1  Treasury (Bessent) to spend Iran's demanded $24bn frozen assets on Gulf-ally
      reconstruction — INVERTS Iran's precondition; HARDENS the deal-deadlock (CONFIRMED policy action)
  A1  Trump's promised "weekend deal" did NOT materialise (>=6th lapsed deadline);
      ISW: IRGC/Vahidi inner circle suspended talks 1 June, prefers the status quo (CONFIRMED non-event)
  A2  Lebanon ESCALATED — 3 Israeli soldiers killed since the week-old truce; Sat 6 Jun
      strikes killed 9 incl 3 Lebanese ARMY; Beirut NOT struck (Iran red-line held) (CONFIRMED action)
  A3  US downed 2 more Iranian drones near Hormuz eve of 6 Jun; UAE joined GCC condemnation;
      ZERO casualties (CONFIRMED action) — no trigger to active
  A4  GIFT/NSE-IX Nifty futures -1.52% -> ~1.5% gap-DOWN indicated Monday 8 Jun (forward
      indicator, not cash verdict); FII ownership ~14.7% (Apr) = two-decade low, BELOW DII
      ~18.9% for the first time ever; YTD FII net-sell ~Rs2.5-3.0L cr; DII absorbing ~90% (CONFIRMED)
  A5  Mojtaba HEU-directive window (by 06-05) EXPIRED un-resolved; Iran-Oman Hormuz-toll
      trigger (iran node, by 06-05) EXPIRED un-resolved; deadlock is now MONEY not nuclear
  B2  Pakistan's Naqvi visited Iran Sat 6 Jun for talks with Araghchi — mediation channel
      alive (REPORTED, single-source Tasnim)

NO trigger moved to active: Gulf round zero-casualty; Beirut red-line held; markets closed
(no fresh VIX); gold below $4,600; Brent no >=$100 close; rupee offshore ~Rs95.6 below Rs96.
"""

# ---- shared signal sources ----
S_B1 = ["CBS News (6 Jun)", "Jewish Insider (6 Jun)", "ABC News live (6 Jun)", "Business Standard/Arab News/Reuters (7 Jun)"]
S_A1 = ["ISW/Critical Threats Iran Update (1 & 3 Jun)", "CNN exclusive (5 Jun)", "Al Jazeera liveblog (6 Jun)", "CNBC (29 May)"]
S_A2 = ["NPR (6 Jun)", "Washington Post (6 Jun)", "Times of Israel", "Al Jazeera/Time (4-6 Jun)"]
S_A3 = ["ABC News (6 Jun, CENTCOM)", "The National/Al Jazeera/UPI (6 Jun)"]
S_A4_gift = ["Business Today (6 Jun)"]
S_A4_fii = ["Outlook Business/Maxiom/Republic World (Jun)"]
S_A5 = ["Reuters/JPost/Haaretz (21 May, carry)", "The National (2 Jun, Rubio)", "PBS NewsHour (Grossi, carry)"]
S_B2 = ["Tasnim (6-7 Jun)"]


PAYLOADS = [

# ============================ IRAN ============================
{
  "nid": "iran",
  "summary_prepend": (
    "Day 100 (Sunday June 7; covers 6 June US day -> overnight -> 7 June IST-morning; "
    "GLOBAL CASH MARKETS CLOSED). **THE DEADLOCK HARDENED ON A QUIET-CALENDAR SUNDAY — "
    "WASHINGTON MOVED TO SPEND THE VERY $24bn IRAN DEMANDS ON THE GULF STATES IRAN BOMBED, "
    "TRUMP'S 'WEEKEND DEAL' LAPSED EMPTY, AND ISW NOW READS THE IRGC INNER CIRCLE AS "
    "DELIBERATELY CHOOSING DRIFT.** (1) THE $24bn DEMAND INVERTED (intel B1, CONFIRMED POLICY "
    "ACTION): Treasury Secretary Bessent directed his department (6 Jun) to use 'all tools "
    "available' to channel FROZEN IRANIAN ASSETS into rebuilding the Gulf allies Iran has bombed "
    "since 28 Feb — i.e. Washington intends to spend on Kuwait/Bahrain the same $24bn that Rezaei "
    "(Mojtaba's military adviser) made Iran's non-negotiable 'test of trust' the day before. This "
    "does not split the difference; it INVERTS the precondition and raises deal-failure probability. "
    "Iran's formal response not yet captured (expect a sharp rejection). (2) THE 'WEEKEND DEAL' "
    "LAPSED (intel A1, CONFIRMED NON-EVENT): Trump's repeated 'deal could happen as soon as this "
    "weekend' passed without any announcement — at least the 6th such deadline to lapse since "
    "mid-March, a documented pattern of unfulfilled optimism, a signal of constraint not progress. "
    "ISW assesses the regime — which it characterises as dominated by IRGC commander Maj. Gen. "
    "Ahmad Vahidi and his inner circle — SUSPENDED US-Iran negotiations on 1 June and 'likely "
    "calculates that the status quo... is a favorable situation,' i.e. the side that benefits from "
    "drift is choosing drift. (3) GULF STAYED KINETICALLY LIVE BUT ZERO-CASUALTY (intel A3, CONFIRMED "
    "ACTION): US forces shot down two MORE Iranian one-way attack drones near the Strait of Hormuz on "
    "the evening of 6 June; the UAE joined Kuwait/Bahrain in condemning the Friday barrage 'in the "
    "strongest terms'; ZERO casualties again — the recalibration to zero-casualty after the 3-June "
    "Kuwait death held across the weekend. The IRGC 'Fifth Fleet hit' stays CENTCOM-DENIED (not "
    "elevated). (4) NUCLEAR -> MONEY (intel A5): the reported Mojtaba HEU directive (~440kg 60%-HEU "
    "not to leave Iran) stayed un-walked-back, and the iran-node trigger demanding state-media "
    "confirmation OR a walk-back within 14 days (by 2026-06-05) EXPIRED WITH NEITHER — the directive "
    "held its 'reported, never owned, never denied' posture for the full window; the companion Iran-Oman "
    "Hormuz-toll trigger (by 2026-06-05) also EXPIRED (only Rezaei's repeated rhetorical toll framing, "
    "no announced mechanism). Rubio reframed HEU disposal as a later 'phase two.' (5) PAKISTAN CHANNEL "
    "ALIVE (intel B2, REPORTED): Tasnim said Pakistan's interior minister Naqvi visited Iran Saturday "
    "for talks with Araghchi — the back-channel being worked even as the formal US table is suspended "
    "(single-source, no published framework). **TRIGGER DECISIONS (June 7)**: NO trigger moves to "
    "active — the Bessent move is a negotiation-state HARDENING (no kinetic threshold), the Gulf round "
    "was zero-casualty, the Beirut red-line held, and Rezaei's toll/wider-war lines stay rhetoric. TWO "
    "triggers EXPIRE UNRESOLVED: Mojtaba-HEU (by 06-05) and iran-node Iran-Oman-toll (by 06-05). "
  ),
  "signal": {"date": "2026-06-07",
    "headline": ("**THE DEADLOCK HARDENED: US TO SPEND IRAN'S DEMANDED $24bn ON THE GULF STATES IT BOMBED; "
      "TRUMP'S 'WEEKEND DEAL' LAPSED EMPTY; ISW SAYS THE IRGC INNER CIRCLE PREFERS THE STATUS QUO.** "
      "On 6 June Treasury Secretary Bessent directed his department to use 'all tools available' to "
      "fund Gulf-ally reconstruction from FROZEN IRANIAN ASSETS — inverting the $24bn that Rezaei "
      "(Mojtaba's adviser, 5 Jun) made Tehran's non-negotiable 'test of trust.' The two sides now "
      "price the same money in opposite directions (CONFIRMED policy action; disbursement not yet "
      "executed; Iran's response pending). Separately Trump's promised 'deal this weekend' passed "
      "without announcement — at least the 6th lapsed deadline since mid-March (CONFIRMED non-event) — "
      "while ISW assessed the IRGC/Vahidi inner circle suspended talks on 1 June and prefers the "
      "favorable status quo. Gulf stayed live but ZERO-casualty (2 more drones downed near Hormuz "
      "6 Jun eve; UAE joined GCC condemnation). The Mojtaba-HEU and Iran-Oman-toll trigger windows "
      "(both by 2026-06-05) EXPIRED un-resolved; Naqvi (Pakistan) visited Tehran Saturday (REPORTED)."),
    "sources": S_B1 + S_A1 + S_A3, "verification": "CONFIRMED (B1 policy action / A1 non-event / A3 action); REPORTED (B2 Naqvi); A5 trigger expiries"},
  "edge_bumps": [
    {"to": "united-states", "new_type": "negotiation_hardening_jun7_bessent_inverts_24bn_demand"},
    {"to": "strait-of-hormuz", "new_type": "jun7_2_more_drones_downed_near_hormuz_blockade_day100_ongoing"},
    {"to": "pakistan", "new_type": "jun7_naqvi_araghchi_meeting_back_channel_alive_reported"},
  ],
  "trigger_status": [
    {"match": "mojtaba uranium directive publicly confirmed", "status": "expired_unresolved",
     "note": "EXPIRED 2026-06-05 with NEITHER limb fired — no state-media confirmation, no walk-back. The directive held its 'reported by anonymous Iranian sources, never officially owned, never officially denied' posture for the full 14-day window. Window closed quietly = a weak signal the directive is internal posture, not an operational act (intel A5)."},
    {"match": "iran-oman permanent hormuz toll mechanism publicly announced within 14 days (by 2026-06-05)", "status": "expired_unresolved",
     "note": "EXPIRED 2026-06-05 un-met — only Rezaei's repeated rhetorical 'joint-management-with-Oman + transit-toll' framing, no announced mechanism. (Companion oman-node toll trigger, by 2026-06-13, remains watching.) (intel A5)."},
  ],
  "trigger_notes": [
    {"match": "pakistan-naqvi mediation produces published framework",
     "note": "2026-06-07: Naqvi REAPPEARED in Tehran (Tasnim, 6 Jun) for talks with Araghchi during the deadlock + fresh Gulf exchanges — the back-channel is being worked even as the formal US table is suspended. Still NO published framework draft (the original by-05-30 window lapsed un-met). Process signal, not a substantive breakthrough. REPORTED, single-source."},
    {"match": "iran accepts direct talks with us",
     "note": "2026-06-07: still watching — ISW assesses the IRGC/Vahidi inner circle SUSPENDED negotiations on 1 June and prefers the status quo; Trump's >=6th 'weekend deal' deadline lapsed empty; Bessent's $24bn asset move cuts AGAINST de-escalation. The drift is a choice (intel A1/B1)."},
  ],
},

# ============================ UNITED STATES ============================
{
  "nid": "united-states",
  "summary_prepend": (
    "Day 100 (Sunday June 7; covers 6 June US day -> 7 June IST-morning; MARKETS CLOSED). "
    "**TREASURY MOVED TO SPEND IRAN'S DEMANDED $24bn ON THE GULF STATES IRAN BOMBED — A HARD-LINE "
    "ACTION THAT CUTS AGAINST TRUMP'S OWN 'WEEKEND DEAL' OPTIMISM (THE SPLIT IS NOW INTRA-"
    "ADMINISTRATION).** (1) THE BESSENT ASSET MOVE (intel B1, CONFIRMED POLICY ACTION): Treasury "
    "Secretary Scott Bessent directed his department (6 Jun) to use 'all tools available to allow "
    "Iranian assets to be made available to our Gulf allies to support rebuilding,' tasking a team "
    "to assess war-damage costs (since Iran's first strikes 28 Feb) to be funded from Iranian assets "
    "(frozen cash vs seized tankers 'unclear'). This collides with Iran's precondition — Rezaei made "
    "the release of $24bn TO IRAN the deal's 'test of trust'; Washington signals it will spend those "
    "same assets ON Kuwait/Bahrain. It gives the GCC a concrete material stake in the US hard line "
    "and is strong evidence the money-deadlock is widening, not closing. (2) THE OPTIMISM-vs-REALITY "
    "GAP, NOW INTRA-ADMINISTRATION (intel A1/C): Trump again forecast a 'deal this weekend' that "
    "LAPSED EMPTY (>=6th such lapse) — while Treasury publicly moved to weaponise the exact $24bn "
    "Tehran demands. Treat the president's framing as the optimistic bound; the Bessent action is "
    "the harder signal. (3) GULF (intel A3, CONFIRMED ACTION): CENTCOM downed two MORE Iranian "
    "drones near the Strait of Hormuz on the evening of 6 June — ZERO US casualties, the US-personnel "
    "calibration intact; the IRGC 'Fifth Fleet hit' stays CENTCOM-DENIED. The markets desk continues "
    "to lead US coverage (the AI/rates selloff outweighs the Gulf). **TRIGGER DECISIONS (June 7)**: no "
    "trigger moves to active — the Bessent move is a negotiation-state hardening (no kinetic threshold); "
    "the Gulf round was zero-casualty; the 'deal this weekend' is a CLAIM falsified by the lapsed "
    "deadline. The 'executing strike' trigger STAYS ACTIVE (no new strike on Iran this window — the "
    "6-June evening was drone intercepts, not a fresh strike). "
  ),
  "signal": {"date": "2026-06-07",
    "headline": ("**TREASURY (BESSENT) MOVED TO SPEND IRAN'S DEMANDED $24bn ON GULF-ALLY RECONSTRUCTION — "
      "INVERTING TEHRAN'S PRECONDITION AND HARDENING THE DEADLOCK, EVEN AS TRUMP FORECAST A 'WEEKEND "
      "DEAL.'** On 6 June Secretary Bessent directed Treasury to use 'all tools available' to fund "
      "rebuilding of the Gulf allies Iran bombed (since 28 Feb) FROM IRANIAN ASSETS, tasking a "
      "war-damage costing team. The day before, Rezaei made the release of $24bn TO IRAN the deal's "
      "non-negotiable test of trust — so the two sides now price the same money in opposite directions "
      "(CONFIRMED policy action; disbursement not executed; Iran's response pending). The optimism gap "
      "is now intra-administration: Trump's 'deal this weekend' lapsed empty (>=6th lapse) while "
      "Treasury acted against it. CENTCOM downed 2 more Iranian drones near Hormuz 6 Jun eve — ZERO US "
      "casualties. The move gives the GCC a material stake in the US hard line."),
    "sources": S_B1 + S_A1, "verification": "CONFIRMED (B1 on-record Treasury action; A1 lapsed-deadline non-event; A3 CENTCOM)"},
  "edge_bumps": [
    {"to": "iran", "new_type": "negotiation_hardening_jun7_bessent_inverts_iran_24bn_precondition"},
  ],
  "new_edges": [
    {"to": "kuwait", "type": "reconstruction_funding_jun7_bessent_iranian_assets_to_rebuild_kuwait", "directness": 1, "activation_count": 1},
    {"to": "bahrain", "type": "reconstruction_funding_jun7_bessent_iranian_assets_to_rebuild_bahrain", "directness": 1, "activation_count": 1},
  ],
  "trigger_notes": [
    {"match": "us truth social or pentagon-channel statement converting strike plan",
     "note": "2026-06-07: STAYS ACTIVE but no new strike on Iran this window — the 6-June evening event was CENTCOM drone intercepts near Hormuz (zero US casualties), not a fresh self-defence strike. Limited, not a full-scale resumption (intel A3)."},
  ],
},

# ============================ MOJTABA KHAMENEI ============================
{
  "nid": "mojtaba-khamenei",
  "summary_prepend": (
    "2026-06-07 (Sunday): **THE $24bn DEMAND VOICED BY MOJTABA'S ADVISER REZAEI WAS DIRECTLY "
    "ATTACKED BY WASHINGTON, AND THE HEU-DIRECTIVE WINDOW EXPIRED QUIETLY — WHILE ISW RE-CENTRED "
    "THE POWER MAP ON THE IRGC/VAHIDI INNER CIRCLE.** (1) BESSENT INVERTS REZAEI'S DEMAND (intel B1): "
    "Treasury moved (6 Jun) to spend the $24bn in frozen Iranian assets — the very sum Rezaei "
    "(military adviser to Mojtaba) made the deal's 'test of trust' — on rebuilding the Gulf states "
    "Iran bombed; the regime's central precondition is being weaponised against it (deal-failure "
    "probability up). (2) HEU DIRECTIVE WINDOW EXPIRED (intel A5): the reported Mojtaba directive "
    "(~440kg 60%-HEU not to leave Iran) stayed un-walked-back, and the 14-day window for state-media "
    "confirmation OR a walk-back (by 2026-06-05) PASSED WITH NEITHER — consistent with the directive "
    "being internal posture, not an operational act. (3) ISW POWER-MAP (intel A1/D): ISW now "
    "characterises the regime as dominated by IRGC commander Maj. Gen. Ahmad Vahidi and his inner "
    "circle, which it says suspended talks on 1 June and prefers the status quo — a sharper "
    "power-center claim to track against the Mojtaba/Rezaei surface. No proof-of-life of Mojtaba "
    "himself this window. "
  ),
  "signal": {"date": "2026-06-07",
    "headline": ("**WASHINGTON MOVED TO SPEND THE $24bn MOJTABA'S ADVISER DEMANDED ON IRAN'S VICTIMS; "
      "THE HEU-DIRECTIVE WINDOW EXPIRED UN-RESOLVED; ISW RE-CENTRED POWER ON THE IRGC/VAHIDI INNER "
      "CIRCLE.** Treasury's 6-June move to fund Gulf reconstruction from frozen Iranian assets "
      "directly inverts the $24bn release that Rezaei (Mojtaba's military adviser) set as the deal's "
      "non-negotiable 'test of trust' (intel B1). Separately the reported Mojtaba HEU directive "
      "(~440kg 60%-HEU not to leave Iran) held un-walked-back through its 14-day window (by 06-05), "
      "which expired with no state-media confirmation and no denial — a weak signal it is internal "
      "posture, not an operational act (intel A5). ISW assesses the regime as dominated by IRGC "
      "commander Vahidi and his inner circle, said to have suspended talks 1 June and to prefer the "
      "status quo (intel A1/D)."),
    "sources": S_B1 + S_A5 + ["ISW/Critical Threats (1 & 3 Jun)"],
    "verification": "CONFIRMED (B1 policy action); REPORTED (A5 directive single-lineage, window expiry); analyst assessment (ISW)"},
  "edge_bumps": [
    {"to": "trump", "new_type": "jun7_bessent_inverts_rezaei_24bn_test_of_trust_demand"},
    {"to": "nuclear-program", "new_type": "jun7_heu_directive_window_expired_unresolved_internal_posture"},
    {"to": "vahidi", "new_type": "jun7_isw_vahidi_inner_circle_dominant_suspended_talks_1jun"},
  ],
},

# ============================ NUCLEAR PROGRAM ============================
{
  "nid": "nuclear-program",
  "summary_prepend": (
    "2026-06-07 (Sunday): **THE NUCLEAR FILE STAYED DEFERRED WHILE THE HEU-DIRECTIVE WINDOW EXPIRED "
    "AND THE IMPASSE MOVED FULLY ONTO MONEY.** The reported Mojtaba directive that Iran's ~440kg of "
    "60%-enriched uranium not leave the country remains un-walked-back, but the iran/mojtaba-node "
    "trigger demanding state-media confirmation OR a walk-back within 14 days (by 2026-06-05) EXPIRED "
    "WITH NEITHER — the thread went dark exactly on schedule, a weak signal the directive is internal "
    "posture not an operational act (intel A5). Substantively the deadlock has shifted from the "
    "nuclear file to MONEY (the $24bn — see iran/united-states B1); Secretary Rubio reframed HEU "
    "disposal as a later 'phase two' of negotiations. The IAEA continues to report a complete LOSS OF "
    "CONTINUITY on the stockpile (access terminated 28 Feb), with Grossi's standing line that Iran "
    "'isn't actively enriching' but that 'movement [was] detected near the stockpile.' Iran's "
    "non-response is the operative reality. (Russia-HEU-custodian trigger, by 2026-06-11, still "
    "watching.) "
  ),
  "signal": {"date": "2026-06-07",
    "headline": ("**HEU-DIRECTIVE WINDOW EXPIRED UN-RESOLVED; NUCLEAR FILE DEFERRED TO RUBIO'S 'PHASE "
      "TWO' AS THE IMPASSE MOVES ONTO MONEY.** The reported Mojtaba directive (~440kg 60%-HEU not to "
      "leave Iran) held un-walked-back through its 14-day window (by 2026-06-05), which expired with "
      "no state-media confirmation and no denial — the thread went dark on schedule. Rubio reframed "
      "HEU disposal as a later 'phase two,' consistent with the nuclear-deferred pivot; the core of "
      "the impasse is now the $24bn frozen-assets question, not enrichment. IAEA reports a continued "
      "complete loss of continuity since 28 Feb (Grossi: not actively enriching, but 'movement "
      "detected near the stockpile'). (intel A5)"),
    "sources": S_A5, "verification": "REPORTED (directive single-lineage, window expiry); CONFIRMED (IAEA continued blackout)"},
  "edge_bumps": [
    {"to": "iran", "new_type": "jun7_heu_window_expired_deadlock_is_money_24bn_not_nuclear"},
    {"to": "mojtaba-khamenei", "new_type": "jun7_directive_window_expired_unresolved_internal_posture"},
  ],
},

# ============================ LEBANON ============================
{
  "nid": "lebanon",
  "summary_prepend": (
    "Day 100 / 2026-06-07 (Sunday): **LEBANON ESCALATED — THREE ISRAELI SOLDIERS HAVE NOW BEEN "
    "KILLED IN THE SOUTH SINCE THE WEEK-OLD TRUCE, AND SATURDAY'S ISRAELI STRIKES KILLED NINE "
    "INCLUDING THREE LEBANESE *ARMY* PERSONNEL — BUT BEIRUT WAS AGAIN NOT STRUCK (IRAN'S RED-LINE "
    "INTACT).** (intel A2, CONFIRMED ACTION) Hezbollah, having flatly rejected the 3-June "
    "Washington-brokered truce, kept up fire on Israeli forces over the weekend, killing three "
    "Israeli soldiers since the ceasefire was signed (Capt. Lemberg Thu, Sgt. Yaari Fri, Capt. Galma "
    "Sat). Israel continued striking the south: Saturday 6 June airstrikes killed nine, including "
    "three Lebanese ARMY members (a strike on Saksakiyah killed six civilians). Defence Minister Katz "
    "reiterated the army 'will continue operations in southern Lebanon,' demanded a demilitarised "
    "zone, and said Israel 'would not be withdrawing.' Two second-order signals: (i) Israel killing "
    "Lebanese ARMY personnel undercuts the Beirut government it signed the truce with; (ii) Israeli "
    "MILITARY casualties (three in four days) raise domestic pressure and make the 'no ceasefire in "
    "Lebanon' posture costlier. The single most important detail is unchanged and geographic: the "
    "strikes hit the SOUTH (Tyre/Sidon/Saksakiyah/Nabatieh), NOT Beirut — the specific trigger "
    "Araghchi has tied to 'full-scale resumption.' **TRIGGER (June 7): the 'US greenlights OR Israel "
    "launches an expanded military operation against Hezbollah' trigger (ACTIVE, window by 2026-06-08) "
    "is INTENSIFYING-WITHIN-ACTIVE — Israeli soldier deaths + Katz's no-withdrawal + Lebanese-army "
    "casualties are an intensifying expanded operation, though still sub-Beirut. NOT a new activation; "
    "Beirut red-line NOT crossed, so no Iran-resumption trigger moves.** "
  ),
  "signal": {"date": "2026-06-07",
    "headline": ("**LEBANON ESCALATED: 3 ISRAELI SOLDIERS KILLED SINCE THE WEEK-OLD TRUCE; SATURDAY'S "
      "ISRAELI STRIKES KILLED 9 INCLUDING 3 LEBANESE *ARMY* PERSONNEL — BUT BEIRUT WAS NOT STRUCK.** "
      "Hezbollah, having rejected the 3-June truce, kept up fire killing three Israeli soldiers (Capt. "
      "Lemberg Thu, Sgt. Yaari Fri, Capt. Galma Sat). Israel's Saturday 6 June airstrikes killed nine, "
      "incl three Lebanese ARMY members (six civilians died in Saksakiyah). Katz vowed continued "
      "operations and 'no withdrawal.' Israel killing the Lebanese army undercuts the Beirut "
      "government it signed the truce with; Israeli military casualties raise domestic pressure. "
      "Critically, the strikes stayed in the SOUTH — Beirut, the specific Araghchi 'full-scale "
      "resumption' red-line, was NOT struck. (CONFIRMED — multi-sourced; named soldiers)"),
    "sources": S_A2, "verification": "CONFIRMED ACTION (named soldier deaths; multi-sourced Saturday toll)"},
  "edge_bumps": [
    {"to": "israel", "type_contains": "renewed_ceasefire", "new_type": "jun7_israel_killed_9_incl_3_lebanese_army_strikes_south_not_beirut"},
    {"to": "hezbollah", "new_type": "jun7_hezbollah_killed_3_idf_soldiers_since_truce_ongoing_fire"},
  ],
  "trigger_notes": [
    {"match": "expanded military operation against hezbollah",
     "note": "2026-06-07: STAYS ACTIVE — INTENSIFYING-WITHIN-ACTIVE (not a new activation). Three Israeli soldiers killed in four days (Lemberg/Yaari/Galma), Saturday strikes killed 9 incl 3 Lebanese ARMY, Katz vows no withdrawal — an intensifying expanded operation, but still SUB-BEIRUT. Beirut red-line NOT crossed; window by 2026-06-08 (intel A2)."},
  ],
},

# ============================ HEZBOLLAH ============================
{
  "nid": "hezbollah",
  "summary_prepend": (
    "Day 100 / 2026-06-07 (Sunday): **HEZBOLLAH'S REJECTION OF THE 3-JUNE TRUCE HAS NOW COST ISRAEL "
    "THREE SOLDIERS IN FOUR DAYS — IT KEPT UP FIRE FROM THE SOUTH WHILE ISRAEL STRUCK BACK, KILLING "
    "NINE INCLUDING THREE LEBANESE ARMY.** (intel A2, CONFIRMED ACTION) Having flatly rejected the "
    "Washington-brokered truce (Qassem: 'a roadmap to annihilate part of the Lebanese people'), "
    "Hezbollah killed three Israeli soldiers since the ceasefire was signed — Capt. Eitan Shmuel "
    "Lemberg (21) Thursday, Sgt. Ohad Yaari Friday, Capt. Shahar Galma (23) Saturday. The Israeli "
    "military casualties (three in four days) are the new register — historically a tightener on "
    "domestic appetite for an open-ended Lebanon operation. Beirut was NOT struck; the conflict "
    "remains geographically contained to the south. **TRIGGER (June 7): the Litani-ground-crossing "
    "Israeli-KIA trigger (active_fired) now stands at THREE confirmed IDF KIA since the week-old "
    "truce — the drone-attrition-to-ground-engagement transition is sustained, not a one-off.** "
  ),
  "signal": {"date": "2026-06-07",
    "headline": ("**HEZBOLLAH KEPT UP FIRE AND HAS NOW KILLED THREE ISRAELI SOLDIERS SINCE THE WEEK-OLD "
      "TRUCE — LEMBERG (THU), YAARI (FRI), GALMA (SAT).** After flatly rejecting the 3-June truce, "
      "Hezbollah sustained attacks on Israeli forces in the south; Israel struck back, killing nine "
      "Saturday including three Lebanese ARMY members. Israeli military casualties (three in four days) "
      "raise the domestic cost of Israel's open-ended Lebanon posture. The fighting stayed in the "
      "south; Beirut was NOT struck. (CONFIRMED — Times of Israel named soldiers; NPR/WaPo on the "
      "Saturday toll) (intel A2)"),
    "sources": S_A2, "verification": "CONFIRMED ACTION (named Israeli soldier deaths; multi-sourced)"},
  "edge_bumps": [
    {"to": "israel", "new_type": "jun7_hezbollah_killed_3_idf_lemberg_yaari_galma_since_truce"},
    {"to": "lebanon", "new_type": "jun7_ongoing_fire_from_south_3_idf_killed_beirut_not_struck"},
  ],
  "trigger_notes": [
    {"match": "litani-ground-crossing-induced israeli soldier kia",
     "note": "2026-06-07: active_fired and SUSTAINED — now THREE confirmed IDF KIA since the week-old truce (Lemberg Thu, Yaari Fri, Galma Sat). The ground-engagement register is recurring, not a single event (intel A2)."},
  ],
},

# ============================ ISRAEL ============================
{
  "nid": "israel",
  "summary_prepend": (
    "Day 100 / 2026-06-07 (Sunday): **ISRAEL KEPT STRIKING SOUTHERN LEBANON UNDER THE FRAYING TRUCE — "
    "SATURDAY STRIKES KILLED NINE INCLUDING THREE LEBANESE *ARMY* PERSONNEL — WHILE ABSORBING ITS "
    "OWN CASUALTIES: THREE SOLDIERS KILLED IN FOUR DAYS. BEIRUT WAS NOT STRUCK.** (intel A2, "
    "CONFIRMED ACTION) Saturday 6 June IDF airstrikes killed nine (a strike on Saksakiyah killed six "
    "civilians), including three Lebanese ARMY members — undercutting the Beirut government Israel "
    "signed the truce with. Defence Minister Katz reiterated operations 'will continue,' demanded a "
    "demilitarised zone, and said Israel 'would not be withdrawing.' Against that, Hezbollah killed "
    "three Israeli soldiers since the truce (Capt. Lemberg Thu, Sgt. Yaari Fri, Capt. Galma Sat) — "
    "the Israeli press is now covering a war that is COSTING the army, historically a tightener on "
    "an open-ended Lebanon operation even as the government stays publicly defiant. The strikes "
    "stayed in the SOUTH (Tyre/Sidon/Saksakiyah/Nabatieh); BEIRUT WAS NOT STRUCK. **TRIGGER (June 7): "
    "the 'Second IDF KIA in southern Lebanon during the 45-day ceasefire window' trigger (active_fired) "
    "now stands at THREE IDF KIA in four days; the 'expanded operation against Hezbollah' trigger "
    "(active) is intensifying-within-active — both SUB-BEIRUT, no new activation.** "
  ),
  "signal": {"date": "2026-06-07",
    "headline": ("**ISRAEL KEPT STRIKING SOUTHERN LEBANON — SATURDAY STRIKES KILLED 9 INCLUDING 3 "
      "LEBANESE *ARMY* — AND LOST A THIRD SOLDIER IN FOUR DAYS; BEIRUT WAS NOT STRUCK.** IDF airstrikes "
      "Saturday 6 June killed nine (six civilians in Saksakiyah), incl three Lebanese ARMY members, "
      "undercutting the Beirut government Israel signed the truce with. Katz vowed continued operations "
      "and 'no withdrawal.' Hezbollah killed three Israeli soldiers since the truce (Lemberg/Yaari/"
      "Galma) — Israeli casualties now tighten domestic constraints on the open-ended Lebanon posture. "
      "Strikes stayed in the SOUTH; Beirut, the Iran-tied red-line, was NOT struck. (CONFIRMED — NPR/"
      "WaPo on the toll; Times of Israel on the named soldiers) (intel A2)"),
    "sources": S_A2, "verification": "CONFIRMED ACTION (multi-sourced strike toll; named IDF casualties)"},
  "edge_bumps": [
    {"to": "lebanon", "new_type": "jun7_idf_killed_9_incl_3_lebanese_army_saksakiyah_strikes_south"},
    {"to": "hezbollah", "new_type": "jun7_3_idf_killed_katz_no_withdrawal_ops_continue"},
  ],
  "trigger_notes": [
    {"match": "second idf kia in southern lebanon during the 45-day ceasefire",
     "note": "2026-06-07: active_fired and ESCALATING — now THREE IDF KIA in four days (Lemberg Thu, Yaari Fri, Galma Sat). Israeli military casualties are mounting under the fraying truce, raising domestic pressure (intel A2)."},
    {"match": "expanded military operation against hezbollah",
     "note": "2026-06-07: STAYS ACTIVE, intensifying-within-active — Saturday strikes killed 9 incl 3 Lebanese army; Katz 'no withdrawal.' Still SUB-BEIRUT (intel A2)."},
  ],
},

# ============================ KUWAIT ============================
{
  "nid": "kuwait",
  "summary_prepend": (
    "2026-06-07 (Sunday): **KUWAIT IS NOW SET TO BE REBUILT WITH IRAN'S MONEY — TREASURY MOVED TO "
    "FUND GULF-ALLY RECONSTRUCTION FROM FROZEN IRANIAN ASSETS, GIVING KUWAIT A CONCRETE MATERIAL "
    "STAKE IN THE US HARD LINE.** (intel B1, CONFIRMED POLICY ACTION) Secretary Bessent directed "
    "Treasury (6 Jun) to assess war-damage costs inflicted on Gulf allies since 28 Feb — Kuwait "
    "among them, after the 3-June Kuwait-airport death and the 5-6 June missile barrage — to be "
    "funded from Iranian assets. This aligns Kuwait materially with Washington's refusal to return "
    "the $24bn to Tehran. On the kinetic front the weekend was quiet for Kuwait: the 6-June evening "
    "exchange was drones near Hormuz, not a fresh Kuwait barrage, and ZERO casualties this round. "
  ),
  "signal": {"date": "2026-06-07",
    "headline": ("**KUWAIT TO BE REBUILT WITH IRANIAN MONEY: TREASURY MOVED TO FUND GULF-ALLY "
      "RECONSTRUCTION FROM FROZEN IRANIAN ASSETS.** Secretary Bessent directed Treasury (6 Jun) to "
      "use 'all tools available' to channel frozen Iranian assets into rebuilding Gulf allies — "
      "Kuwait among the bombed states (3-June airport death; 5-6 June barrage). This gives Kuwait a "
      "concrete material stake in Washington's refusal to return the $24bn to Tehran, reinforcing the "
      "GCC's tilt against Iran. No fresh Kuwait barrage over the weekend (the 6-Jun evening event was "
      "drones near Hormuz; zero casualties). (CONFIRMED policy action; disbursement not executed) "
      "(intel B1)"),
    "sources": S_B1, "verification": "CONFIRMED (on-record Treasury action; disbursement not yet executed)"},
  "edge_bumps": [
    {"to": "united-states", "new_type": "jun7_bessent_iranian_assets_to_rebuild_kuwait_material_stake"},
  ],
},

# ============================ BAHRAIN ============================
{
  "nid": "bahrain",
  "summary_prepend": (
    "2026-06-07 (Sunday): **BAHRAIN IS NOW SET TO BE REBUILT WITH IRAN'S MONEY — AND THE UAE JOINED "
    "BAHRAIN/KUWAIT IN CONDEMNING IRAN'S BARRAGE.** (intel B1/A3) Treasury Secretary Bessent directed "
    "his department (6 Jun) to fund Gulf-ally reconstruction from FROZEN IRANIAN ASSETS, assessing "
    "war-damage costs since 28 Feb — Bahrain among the targeted states (it intercepted missiles and "
    "drones on 5-6 June and activated air-raid sirens) — giving Bahrain a concrete material stake in "
    "the US refusal to return the $24bn to Tehran (CONFIRMED policy action). Diplomatically the GCC "
    "condemnation WIDENED: the UAE denounced the targeting of Kuwait and Bahrain 'in the strongest "
    "terms.' The weekend was quiet for Bahrain kinetically (6-Jun evening was drones near Hormuz; "
    "zero casualties). "
  ),
  "signal": {"date": "2026-06-07",
    "headline": ("**BAHRAIN TO BE REBUILT WITH IRANIAN MONEY; UAE JOINS THE GCC CONDEMNATION.** "
      "Treasury's 6-June move to fund Gulf-ally reconstruction from frozen Iranian assets covers "
      "Bahrain (which intercepted the 5-6 June barrage and sounded air-raid sirens), giving it a "
      "material stake in Washington's refusal to return the $24bn to Tehran (CONFIRMED policy action; "
      "intel B1). The GCC condemnation widened — the UAE denounced the targeting of Kuwait and "
      "Bahrain 'in the strongest terms' (intel A3). No fresh Bahrain hit over the weekend; the 6-Jun "
      "evening event was drones near Hormuz, zero casualties."),
    "sources": S_B1 + S_A3, "verification": "CONFIRMED (Treasury action; UAE condemnation multi-sourced)"},
  "edge_bumps": [
    {"to": "united-states", "new_type": "jun7_bessent_iranian_assets_to_rebuild_bahrain_material_stake"},
  ],
},

# ============================ SAUDI ARABIA ============================
{
  "nid": "saudi-arabia",
  "summary_prepend": (
    "2026-06-07 (Sunday): **THE GCC'S TILT AGAINST TEHRAN WAS MATERIALLY REWARDED AND WIDENED.** "
    "(intel B1/A3) Treasury's move (6 Jun) to rebuild the bombed Gulf allies (Kuwait/Bahrain) from "
    "FROZEN IRANIAN ASSETS gives the GCC bloc — Saudi Arabia included — a concrete material incentive "
    "aligned with the US hard line, after the Kuwait-airport death and the 5-6 June barrages. The "
    "condemnation of Iran's strikes widened from Kuwait/Bahrain to the UAE ('strongest terms'), with "
    "no new expulsions (the bloc reserving hard diplomatic action for lethal events). No Saudi-"
    "specific kinetic development this window. "
  ),
  "signal": {"date": "2026-06-07",
    "headline": ("**GCC TILT AGAINST IRAN MATERIALLY REWARDED AS WASHINGTON MOVES TO REBUILD GULF "
      "ALLIES WITH IRANIAN MONEY; UAE JOINS THE CONDEMNATION.** Treasury's 6-June move to fund "
      "Kuwait/Bahrain reconstruction from frozen Iranian assets gives the GCC bloc — Saudi Arabia "
      "included — a material incentive aligned with the US hard line against returning the $24bn to "
      "Tehran (intel B1). The condemnation of Iran's barrage widened to the UAE 'in the strongest "
      "terms,' with no new expulsions (intel A3). (CONFIRMED policy action / multi-sourced "
      "condemnation; no Saudi-specific kinetic event)"),
    "sources": S_B1 + S_A3, "verification": "CONFIRMED (Treasury action; condemnation multi-sourced)"},
},

# ============================ OMAN ============================
{
  "nid": "oman",
  "summary_prepend": (
    "2026-06-07 (Sunday): **REZAEI REASSERTED THE 'JOINT-MANAGEMENT-WITH-OMAN + TRANSIT-TOLL' "
    "PROPOSAL ATOP A STILL-THROTTLED STRAIT — RHETORIC, NO MECHANISM — WHILE THE PAKISTAN MEDIATION "
    "CHANNEL REACTIVATED IN THE BROADER ECOSYSTEM.** (intel A5/A6/B2) The iran-node companion "
    "trigger ('Iran-Oman permanent Hormuz toll mechanism publicly announced by 2026-06-05') EXPIRED "
    "un-met — only Rezaei's repeated rhetorical toll framing, no announced mechanism. The oman-node "
    "trigger (toll mechanism by 2026-06-13 OR US sanctions Oman) REMAINS WATCHING. Separately, "
    "Pakistan's interior minister Naqvi visited Iran Saturday for talks with Araghchi (REPORTED, "
    "Tasnim) — the mediation ecosystem (Pakistan formal + Oman/Qatar Gulf channels) is being worked "
    "even as the formal US-Iran table is suspended. "
  ),
  "signal": {"date": "2026-06-07",
    "headline": ("**REZAEI REASSERTED THE HORMUZ OMAN-JOINT-MANAGEMENT + TOLL PROPOSAL (RHETORIC, NO "
      "MECHANISM); PAKISTAN'S NAQVI VISITED IRAN, MEDIATION ECOSYSTEM ALIVE.** Iran's Rezaei renewed "
      "the 'sovereignty + Oman joint-management + transit-toll' line atop an already-throttled strait "
      "(~10 ships/day vs ~95) — no new physical act and no announced toll mechanism; the iran-node "
      "06-05 toll trigger EXPIRED un-met (intel A5/A6). The oman-node toll trigger (by 06-13 or US "
      "sanctions Oman) stays watching. Separately, Pakistan's Naqvi visited Iran Saturday for talks "
      "with Araghchi (REPORTED, Tasnim) — the back-channel ecosystem is being worked during the "
      "deadlock (intel B2)."),
    "sources": S_A5 + S_B2 + ["CNN Business (2 Jun, Hormuz)"],
    "verification": "RHETORIC (toll proposal); REPORTED (Naqvi visit, single-source); CONFIRMED (Hormuz throttle ongoing)"},
  "edge_bumps": [
    {"to": "iran", "new_type": "jun7_rezaei_reasserts_oman_joint_mgmt_toll_rhetoric_no_mechanism"},
  ],
  "trigger_notes": [
    {"match": "iran-oman permanent hormuz toll mechanism publicly announced within 14 days (by 2026-06-13)",
     "note": "2026-06-07: STAYS WATCHING — Rezaei reasserted the Oman-joint-management/toll proposal but NO mechanism announced; the companion iran-node trigger (by 06-05) EXPIRED un-met. US-Treasury-sanctions-Oman limb also not fired (intel A5/A6)."},
  ],
},

# ============================ NIFTY 50 ============================
{
  "nid": "nifty-50",
  "summary_prepend": (
    "2026-06-07 (Sunday; CASH MARKET CLOSED — forward indicator only): **GIFT/NSE-IX NIFTY FUTURES "
    "FELL ~356 POINTS (-1.52%) TO ~23,091, SIGNALLING A SHARP ~1.5% GAP-DOWN AT MONDAY'S (8 JUNE) "
    "OPEN — THE FIRST CONCRETE SIGN INDIA IMPORTS THE US AI/RATES RISK-OFF RATHER THAN ROTATING "
    "AWAY FROM IT.** (intel A4 / markets B1, CONFIRMED futures datum) Indian cash closed Friday at "
    "23,366.70 (-0.21%) BEFORE Wall Street's AI rout (Nasdaq -4.2%, S&P -2.6%, VIX +40% to ~21.5) — "
    "so Monday is India's FIRST reaction to the shock. The futures lean toward the Kotak 'India gets "
    "dragged, doesn't benefit' read at the open, against the bullish 'AI crack rotates FII into "
    "India' thesis. Key Monday levels: support ~23,150 then the 23,000 floor; resistance "
    "23,500-23,550. A break of 23,000 opens the contagion downside; a hold + intraday recovery keeps "
    "the DII-buffer floor intact. The Market Analyst's split: ~10-15% of the move is crisis-linked, "
    "~85% imported US AI/rates risk-off. **This is a forward indicator of the OPEN, NOT the cash "
    "session's verdict — the real reaction and the FII print that adjudicates the deployment thesis "
    "land Monday 8 June and after.** "
  ),
  "signal": {"date": "2026-06-07",
    "headline": ("**GIFT/NSE-IX NIFTY FUTURES -1.52% TO ~23,091 — A ~1.5% GAP-DOWN INDICATED FOR "
      "MONDAY 8 JUNE, INDIA'S FIRST REACTION TO FRIDAY'S US AI ROUT.** With cash markets closed since "
      "Friday's calm -0.21% close (23,366.70), GIFT Nifty fell ~356 pts over the weekend, signalling "
      "India imports the US AI/rates risk-off at the open rather than rotating away from it — leaning "
      "toward the Kotak 'dragged, doesn't benefit' read over the bullish FII-rotation thesis. Monday "
      "support ~23,150 then 23,000 floor; resistance 23,500-23,550. ~10-15% crisis-linked, ~85% "
      "imported macro. A forward indicator of the OPEN, not the cash verdict (which, with the FII "
      "print, lands Monday and after). (CONFIRMED futures datum) (intel A4 / markets B1)"),
    "sources": S_A4_gift + ["NSE-IX/GIFT"], "verification": "CONFIRMED (observable futures datum; indicates Monday's OPEN not the cash verdict)"},
  "current_merge": {"price": "Nifty cash 23,366.70 (5 June Asia close, pre-US-rout) | GIFT/NSE-IX futures ~23,091 (-1.52%, weekend) -> ~1.5% gap-down indicated for Monday 8 June open",
                    "delta_1d": "GIFT futures -1.52% (Monday-open indicator; cash closed)",
                    "note": "Sunday — cash market closed; GIFT futures are the only live India signal. Monday support 23,150/23,000; resistance 23,500-23,550."},
  "edge_bumps": [
    {"to": "india", "new_type": "jun7_gift_nifty_minus1.52pct_gapdown_indicated_monday8jun"},
  ],
  "trigger_notes": [
    {"match": "north-asia ai complex",
     "note": "2026-06-07: STAYS WATCHING — leg-one (North-Asia/AI >10% correction) is confirmed (SMH -9.2% Fri), but GIFT Nifty's -1.52% gap-down indication leans AGAINST leg-two (India FII net-positive 3+ sessions) at the open. Do NOT flip the capital_substitution edge sign; leg-two is untested and resolves only on Monday's cash session + the FII print (markets E1)."},
  ],
},

# ============================ INDIA ============================
{
  "nid": "india",
  "summary_prepend": (
    "2026-06-07 (Sunday; markets closed): **INDIA IS SET TO OPEN MONDAY 8 JUNE BY IMPORTING THE US "
    "AI/RATES RISK-OFF — GIFT/NSE-IX NIFTY FUTURES -1.52% INDICATE A ~1.5% GAP-DOWN, THE FIRST "
    "CONCRETE SIGN INDIA GETS DRAGGED IN RATHER THAN ROTATED INTO.** (intel A4) Cash closed Friday "
    "(23,366.70) BEFORE Wall Street's Friday plunge, so Monday is India's first reaction. The "
    "structural backdrop hardened: FII ownership of Indian equities at a ~two-decade low (~14.7%, "
    "April) and BELOW DII (~18.9%) for the first time ever; YTD CY26 FII net selling ~Rs2.5-3.0 lakh "
    "crore (already exceeding 2025's full-year record), with DIIs absorbing ~90% (see fii-flows). A "
    "countervailing analyst camp argues FII selling is nearing EXHAUSTION (H2 reversal). The crisis "
    "itself is a marginal driver here (~10-15%); the dominant force is imported US macro (hot May "
    "jobs -> Fed higher-for-longer; Broadcom AI re-rating). The verdict resolves on Monday's cash "
    "session and the FII print that follows. "
  ),
  "signal": {"date": "2026-06-07",
    "headline": ("**INDIA TO OPEN MONDAY IMPORTING THE US AI/RATES RISK-OFF — GIFT NIFTY -1.52% "
      "INDICATES A ~1.5% GAP-DOWN.** India's cash market closed Friday (23,366.70) before Wall "
      "Street's Friday AI rout, so Monday 8 June is its first reaction; the futures lean toward the "
      "'dragged-down' read over the bullish FII-rotation thesis. The crisis is a marginal driver "
      "(~10-15%); the dominant force is imported US macro (Fed higher-for-longer + AI re-rating). FII "
      "ownership is at a two-decade low below DII for the first time, with DIIs absorbing ~90% of "
      "outflows — India's proximate floor. (CONFIRMED futures datum; forward indicator of the open) "
      "(intel A4)"),
    "sources": S_A4_gift + S_A4_fii, "verification": "CONFIRMED (futures/flow data; indicates Monday's open)"},
},

# ============================ FII FLOWS ============================
{
  "nid": "fii-flows",
  "summary_prepend": (
    "2026-06-07 (Sunday): **FII OWNERSHIP OF INDIAN EQUITIES HAS FALLEN TO A ~TWO-DECADE LOW (~14.7%, "
    "APRIL) AND NOW SITS *BELOW* DII OWNERSHIP (~18.9%) FOR THE FIRST TIME IN THE MODERN HISTORY OF "
    "INDIAN CAPITAL MARKETS — A STRUCTURAL MILESTONE.** (intel A4, CONFIRMED/REPORTED) 2026 YTD FII "
    "net selling is in the ~Rs2.5-3.0 lakh crore range (sources vary: ~Rs2.3L cr Jan-May, ~Rs2.54L "
    "cr cited 5 Jun, up to ~Rs2.99L cr on one tally — all already exceeding 2025's full-year "
    "~Rs1.7-2.4L cr record), with DIIs absorbing ~90% (May DII net buying ~Rs82,600 cr). A NEW "
    "analyst camp has emerged arguing FII selling is NEARING EXHAUSTION (ownership below DII; ~90% "
    "DII absorption; 'experts see an H2 2026 reversal') — the bullish counter to the Kotak "
    "'India-stays-muted' read: the marginal foreign seller is running out of stock, so further FII "
    "downside is structurally limited. FII was STILL net-selling through Friday's Asia session; "
    "Monday 8 June (India's first reaction to the US rout) is the real flow test. **The "
    "deployment-thesis sufficient condition — FII net-positive 3+ sessions — remains UNMET and "
    "untested.** "
  ),
  "signal": {"date": "2026-06-07",
    "headline": ("**FII OWNERSHIP AT A ~TWO-DECADE LOW (~14.7%) — NOW *BELOW* DII (~18.9%) FOR THE "
      "FIRST TIME EVER; YTD NET-SELLING ~Rs2.5-3.0L cr, DIIs ABSORBING ~90%; AN 'EXHAUSTION' CAMP "
      "EMERGES.** FII ownership of Indian equities has fallen below domestic institutions for the "
      "first time in the modern history of Indian capital markets — a structural milestone. YTD CY26 "
      "FII net selling (~Rs2.54-2.99L cr on most tallies) already exceeds 2025's full-year record, "
      "with DIIs absorbing ~90% (May ~Rs82,600 cr). A new analyst camp argues the selling is nearing "
      "EXHAUSTION (H2 reversal) — the marginal foreign seller running low — the bullish counter to "
      "Kotak. FII still net-selling through Friday; the deployment-thesis condition (FII net-positive "
      "3+ sessions) is UNMET. Monday 8 June is the real flow test. (CONFIRMED ownership data; "
      "REPORTED YTD tallies) (intel A4)"),
    "sources": S_A4_fii, "verification": "CONFIRMED (ownership-below-DII milestone); REPORTED (YTD tallies vary by source)"},
  "current_merge": {"fii_ownership": "~14.7% (April) — ~two-decade low, BELOW DII (~18.9%) for the first time ever",
                    "ytd_cy26_fii_outflow": "~Rs2.5-3.0 lakh cr (sources vary: ~Rs2.54L cr cited 5 Jun, up to ~Rs2.99L cr) — already exceeds 2025 full-year record",
                    "dii_absorption": "~90% (May DII net buying ~Rs82,600 cr)",
                    "latest_day": "FII STILL net-selling through 5-June Asia session; Monday 8 June is the real flow test (India closed before the US rout). No confirmed flow turn."},
  "trigger_notes": [
    {"match": "fii ytd cy26 outflow exceeds",
     "note": "2026-06-07: the Rs2.5L cr OUTFLOW threshold is now REACHED on most tallies (~Rs2.54-2.99L cr) — BUT the trigger's actual cascade ('DII channel cracks') has NOT occurred: DIIs are absorbing ~90% and the Nifty floor held. Outflow limb met; consequence not fired. Stays watching the DII-crack consequence, not the headline number (intel A4)."},
    {"match": "fii flow turn positive for 5 consecutive sessions",
     "note": "2026-06-07: STILL UNMET — FII net-selling through Friday; an 'exhaustion/H2-reversal' camp has emerged (ownership below DII; ~90% DII absorption) but no actual flow turn yet. Monday 8 June is the test (intel A4)."},
  ],
},

# ============================ INR / USD ============================
{
  "nid": "inr-usd",
  "summary_prepend": (
    "2026-06-07 (Sunday; onshore market closed — offshore NDF only): **THE RUPEE IS PRESSING-BUT-NOT-"
    "BREAKING Rs96 INTO MONDAY, WITH A DXY +0.7% (FRIDAY) HEADWIND.** (intel A4 / markets A) The "
    "only live weekend FX signal is the offshore INR-NDF at ~Rs95.1-95.6, consistent with Friday's "
    "onshore ~Rs95.63 close — still Asia's worst-performing currency in 2026 and still pressing, but "
    "NOT breaking, the Rs96 RBI-direct-intervention trigger. Friday's DXY +0.7% (on the hot-jobs -> "
    "Fed-higher-for-longer repricing) is the headwind into Monday's open. (The recurring yfinance "
    "Rs94.95 print remains an offshore/Saturday-vintage artifact — NOT operative; treat ~Rs95.6 as "
    "the operative level.) No fresh onshore print until Monday 8 June. "
  ),
  "signal": {"date": "2026-06-07",
    "headline": ("**RUPEE PRESSING-NOT-BREAKING Rs96 INTO MONDAY; DXY +0.7% (FRIDAY) IS THE HEADWIND.** "
      "On a Sunday the only live FX signal is the offshore INR-NDF at ~Rs95.1-95.6, consistent with "
      "Friday's onshore ~Rs95.63 close — still pressing, but not breaking, the Rs96 RBI-direct-"
      "intervention trigger. Friday's dollar strength (DXY +0.7% on the Fed-higher-for-longer "
      "repricing) is the headwind into Monday's open. The yfinance Rs94.95 'firming' print is an "
      "offshore/Saturday-vintage artifact, NOT encoded. No fresh onshore print until Monday 8 June. "
      "(offshore/forward signal — not a fresh onshore datum) (intel A4)"),
    "sources": ["intel A4 (onshore ~Rs95.63, 5 Jun)", "markets A (offshore NDF ~Rs95.1-95.6)"],
    "verification": "REPORTED (offshore NDF / forward; not a fresh onshore close)"},
  "trigger_notes": [
    {"match": "usd/inr breaks ₹96 within 5-7 sessions",
     "note": "2026-06-07: active_fired and STILL PRESSING-NOT-BREAKING — offshore NDF ~Rs95.1-95.6 (Sunday), Friday onshore ~Rs95.63; DXY +0.7% headwind into Monday. Rs96 not cleanly breached; the verdict resolves on Monday's onshore session (intel A4)."},
  ],
},

]
