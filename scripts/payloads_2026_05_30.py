# -*- coding: utf-8 -*-
"""Per-node payloads for the 2026-05-30 graph update. See update_graph_2026_05_30.py.
Content authored from staging/2026-05-30-morning/{intel.md,markets.md}.
Market prints = Friday 29 May close (30 May is Saturday). Deltas vs the 28 May brief."""

def s(headline, sources, verification, date="2026-05-30"):
    return {"date": date, "headline": headline, "sources": sources, "verification": verification}

PAYLOADS = []

# ===========================================================================
# LIST A — GEOPOLITICAL
# ===========================================================================

PAYLOADS.append(dict(
    nid="iran",
    summary_prepend=(
        "Day 92 (Saturday May 30; covers 28 May afternoon -> 30 May morning). "
        "**THE POST-MISSILE WORLD DID NOT ESCALATE — IRAN REVERTED TO THE TABLE AND REFRAMED ITS PRICE AS CASH, "
        "NOT NUCLEAR CONCESSIONS. The 28 May calibrated IRGC missile (intercepted over Kuwait, zero casualties) produced NO "
        "further missile exchange and NO new airstrikes through 30 May — confirming the 'calibrated/contained' read. The one new "
        "kinetic development is a US ENFORCEMENT action, not a strike: on 30 May the US military DISABLED the Gambia-flagged bulk "
        "carrier Lian Star in the Gulf of Oman after it tried to enter Iranian ports — the 6th vessel stopped during the blockade "
        "(CONFIRMED — Iran International liveblog citing US military). War Secretary Hegseth: the 'blockade is very much still in "
        "place,' Hormuz must stay 'an open, toll-free strait' (CONFIRMED). The genuinely new intelligence is a MONEY-FIRST "
        "hardening: Iran's semi-official Fars directly contradicted Trump's account of the unsigned 60-day MOU, stating the draft "
        "contains NO HEU-destruction clause and that its 'most important part' is the immediate release of $12bn of Iran's frozen "
        "assets — with Iran refusing further negotiation until paid (REPORTED — Fars; Iran's framing, contested). Trump insists the "
        "~1,000 lbs HEU 'will be destroyed' and 'no sanctions, no money, no nothing' (CLAIMED — US framing). Both the destruction "
        "clause and the $12bn-first demand are CLAIMED by their respective sides until a signed text exists — the one-side-framing "
        "pattern running in BOTH directions. On 29 May Iran publicly claimed 'no negotiations' on the nuclear file are taking place "
        "(CLAIMED Iran), and Araghchi reaffirmed the enriched-material file is 'postponed/deadlocked.' Sadjadpour re-validated: Iran "
        "manages escalation for leverage (frozen-asset relief), not war. TRIGGERS: Mojtaba HEU directive ~Day 9 of 14 (deadline "
        "~June 5), STAYS watching — still no proof-of-life, no state-media confirmation/walk-back. Iran-Oman Hormuz-toll trigger "
        "STAYS watching — the toll question is now LIVE friction (US Treasury reportedly threatened to sanction Oman over tolls, "
        "intel A8) but no permanent toll mechanism has been announced. rial-2M STAYS watching — USD/IRR ~1.34m (TradingEconomics "
        "27 May) to ~1.72m (free-market), well away from the 2,000,000 hyperinflation threshold on either basis. NO trigger moves "
        "to active — the dominant signal of the window is a CONFIRMED NON-EVENT of non-escalation.**"
    ),
    signal=s(
        "**POST-MISSILE NON-ESCALATION CONFIRMED; IRAN REFRAMES ITS PRICE AS $12bn CASH, NOT NUCLEAR CONCESSIONS.** After the 28 "
        "May calibrated IRGC missile, NO further missile exchange or airstrikes through 30 May. New: the US disabled the "
        "Gambia-flagged bulk carrier Lian Star in the Gulf of Oman (6th blockade vessel) after it tried to enter Iranian ports; "
        "Hegseth said the 'blockade is very much still in place' and Hormuz must stay 'open, toll-free.' On the unsigned 60-day MOU, "
        "Fars (semi-official, IRGC-conservative) directly contradicted Trump: the draft has NO HEU-destruction clause and its "
        "'most important part' is the immediate release of $12bn of Iran's frozen assets, with Iran refusing further talks until "
        "paid. Trump's counter-framing ('HEU will be destroyed,' 'no money, no nothing') and Iran's $12bn-first demand are BOTH "
        "CLAIMED by their respective sides — no signed text exists. Iran also publicly claimed (29 May) 'no negotiations' on the "
        "nuclear file are happening; Araghchi reaffirmed the enriched-material file is deadlocked/postponed.",
        ["Iran International liveblog 30 May (Lian Star; US military) — REPORTED-to-CONFIRMED on the enforcement event",
         "Hegseth public statement 30 May — official US — independent",
         "Fars (Iranian semi-official) via wire summaries — Iran's contradicting framing — provides Iran position",
         "CNBC 29 May (Trump ended Situation Room meeting without a final determination)",
         "Tasnim (agreement 'not yet finalized'; warns aggression 'met with force')",
         "Intel dossier 2026-05-30 A1, A2, B2, A11"],
        "Non-escalation (no further strikes through 30 May) = CONFIRMED NON-EVENT; Lian Star interdiction = REPORTED-to-CONFIRMED; "
        "Hegseth 'blockade still in place / toll-free' = CONFIRMED; HEU-destruction clause (US) and $12bn-first demand (Iran) = "
        "CLAIMED by each side (no signed text); Iran 'no negotiations' on nuclear = CLAIMED Iran; deadlock = REPORTED/CONFIRMED."
    ),
    edge_bumps=[
        {"to": "united-states", "new_type": "blockade_enforcement_lian_star_6th_vessel_hegseth_toll_free_strait_plus_unsigned_60day_mou_money_first"},
        {"to": "strait-of-hormuz", "new_type": "active_blockade_continues_lian_star_interdiction_new_mine_alert_toll_friction"},
        {"to": "nuclear-program", "new_type": "deadlock_iran_no_negotiations_fars_no_destruction_clause_mojtaba_day9_of_14"},
    ],
    trigger_notes=[
        {"match": "Mojtaba uranium directive publicly confirmed",
         "note": "Day 9 of 14 (deadline ~June 5). STAYS watching. Still NO state-media confirmation, denial, or walk-back, and no proof-of-life. Fars's $12bn-first reframing (intel A2/B2) reprices Iran's ask as cash-up-front rather than a nuclear concession — orthogonal to, and not a resolution of, the directive. The negative-space signal persists; no upgrade."},
        {"match": "Iran-Oman permanent Hormuz toll mechanism",
         "note": "STAYS watching. The toll question went LIVE this window: the US Treasury reportedly threatened to sanction Oman if it imposes Hormuz tolls (intel A8, REPORTED — single ToI liveblog headline), directly tied to Hegseth's 'toll-free strait' demand and Iran's desired Oman-mediated toll mechanism in the draft MOU. But NO permanent toll mechanism has been publicly announced — Rubio's red line is not breached. No upgrade."},
        {"match": "Iranian rial breaks 2,000,000",
         "note": "STAYS watching. No fresh deterioration print. TradingEconomics USD/IRR ~1,341,554 (27 May, +1.5%); free-market basis ~1.72m. On EITHER basis the rial sits well away from the 2,000,000 hyperinflation threshold; the deal-anticipation / $12bn-frozen-asset-release bid remains the dominant near-term FX driver. No upgrade."},
    ],
))

PAYLOADS.append(dict(
    nid="united-states",
    summary_prepend=(
        "Day 92 (Saturday May 30). **WASHINGTON IS RUNNING THREE SIMULTANEOUS PRESSURE TRACKS AND GENERATING FRICTION WITH ITS OWN "
        "MEDIATORS. (1) ENFORCEMENT: the US military disabled the Gambia-flagged Lian Star in the Gulf of Oman (6th blockade vessel) "
        "after it tried to enter Iranian ports; Hegseth declared the 'blockade is very much still in place,' Hormuz must remain "
        "'an open, toll-free strait,' and Iran can 'deal with the War Department' if diplomacy fails (CONFIRMED). This sits AGAINST "
        "the MOU's own term ('blockade lifted in proportion to restored shipping') — a genuine inconsistency. (2) DEAL: Trump ended "
        "a 29 May White House Situation Room meeting WITHOUT a 'final determination' (CONFIRMED non-signature — CNBC); Rubio blamed "
        "'disagreements over a word, a sentence' and projected 'a few days.' Trump publicly insists Iran's HEU 'will be destroyed' "
        "and 'no sanctions, no money, no nothing' (CLAIMED — US framing, contradicted by Fars). (3) LEBANON: the US hosted the "
        "first-ever Pentagon Israel-Lebanon military talks on 29 May (Under Sec. Colby), called 'productive,' to feed a State-led "
        "political track 'next week' — even as it APPROVED Israel's expanded Lebanon operation while warning only against Beirut "
        "(which Israel then crossed). (4) ACCORDS: Trump told leaders of Saudi/UAE/Qatar/Pakistan/Turkey/Egypt/Jordan/Bahrain it is "
        "'mandatory' to normalize with Israel after the Iran war; capitals were 'stunned' (REPORTED). And the US Treasury reportedly "
        "threatened to sanction OMAN — its own Hormuz mediator — over tolls. Net: maximal pressure on every axis, with new strain "
        "against Oman and Saudi simultaneously.**"
    ),
    signal=s(
        "**US RUNS ENFORCEMENT + UNSIGNED-DEAL + LEBANON + ACCORDS TRACKS AT ONCE; FRICTION WITH ITS OWN MEDIATORS.** The US "
        "military disabled the Lian Star (6th blockade vessel) in the Gulf of Oman; Hegseth: 'blockade very much still in place,' "
        "Hormuz must stay 'open, toll-free' — contradicting the MOU's 'blockade lifted in proportion to restored shipping.' Trump "
        "ended the 29 May Situation Room meeting without signing (CNBC); Rubio: holdup is 'a word, a sentence,' 'a few days.' The "
        "Pentagon hosted the first-ever Israel-Lebanon military talks (29 May, Under Sec. Colby), 'productive,' to feed a State-led "
        "track 'next week,' while the US approved Israel's expanded Lebanon op (warning only vs Beirut). Trump called Abraham "
        "Accords accession 'mandatory' for eight Muslim-nation leaders, who were 'stunned.' Separately the US Treasury reportedly "
        "threatened to sanction Oman — its Hormuz mediator — over tolls.",
        ["Iran International liveblog 30 May (Lian Star); Hegseth on record 30 May",
         "CNBC 29 May (no final determination); Rubio on record",
         "The National / Washington Post / Arab News / ToI (Pentagon Israel-Lebanon talks 29 May)",
         "Axios / Bloomberg / NPR / Time (Accords 'mandatory'; 'stunned' capitals)",
         "Times of Israel liveblog 28 May (US Treasury-Oman tolls — REPORTED, single headline)",
         "Intel dossier 2026-05-30 A1, A2, A4, A8, A9, B1"],
        "Lian Star interdiction + Hegseth statement = CONFIRMED; Trump non-signature = CONFIRMED (CNBC); HEU 'will be destroyed' / "
        "'no money' = CLAIMED (US framing); Pentagon Israel-Lebanon talks 29 May = CONFIRMED; Accords 'mandatory' + 'stunned' = "
        "REPORTED; US Treasury-Oman toll threat = REPORTED (single ToI headline, needs corroboration)."
    ),
    edge_bumps=[
        {"to": "iran"},
        {"to": "strait-of-hormuz"},
        {"to": "israel"},
        {"to": "lebanon"},
    ],
))

PAYLOADS.append(dict(
    nid="lebanon",
    summary_prepend=(
        "Day 92 (Saturday May 30). **LEBANON CROSSED WASHINGTON'S RED LINE — IDF CONFIRMED OPERATING INSIDE BEIRUT AND ACROSS THE "
        "LITANI, EVEN AS THE FIRST PENTAGON ISRAEL-LEBANON MILITARY TALKS OPENED THE SAME DAY. On 29 May Netanyahu announced IDF "
        "forces had crossed the Litani and were 'operating in Beirut and the Bekaa Valley' — the first IDF action in Beirut in ~3 "
        "weeks — calling it a 'tactical victory' (CONFIRMED — Netanyahu on record; Times of Israel; Wikipedia Timeline of the 2026 "
        "Lebanon war). The 28 May brief had flagged that WASHINGTON WARNED ISRAEL AGAINST STRIKING THE CAPITAL to protect the Iran "
        "talks — so Beirut operations are a NEW red-line crossing. Israel issued sweeping evacuation orders for ~7 southern "
        "towns/villages ahead of strikes south of the Zahrani River; hundreds of thousands displaced. The Lebanese health ministry "
        "reported 142 killed in the prior 72 hours, raising the cumulative toll to ~3,355 (from ~3,244 at the 28 May brief). IDF "
        "combat deaths reached 24 — RECONCILED UPWARD from the 28 May brief's '22' baseline (a Givati Brigade female soldier killed "
        "+ 2 reservists wounded by a Hezbollah drone on 27 May). Crucially, all of this ran SIMULTANEOUSLY with the first-ever "
        "direct Israel-Lebanon military talks at the Pentagon on 29 May (see A4) — the negotiate-while-bombing pattern, here as a "
        "SINGLE coercive strategy, not two data points. The expanded-operation trigger STAYS ACTIVE (fired May 27); the Beirut "
        "crossing intensifies it. Michael Rubin (defense analyst): any ceasefire is 'illusionary' while Hezbollah keeps heavy "
        "weapons and is excluded from the arrangement — the structural problem behind the Pentagon track.**"
    ),
    signal=s(
        "**BEIRUT RED LINE CROSSED — IDF 'OPERATING IN BEIRUT AND THE BEKAA,' LITANI CROSSED; 142 KILLED/72h, TOLL ~3,355; IDF KIA "
        "RECONCILED TO 24; SAME DAY AS THE FIRST PENTAGON ISRAEL-LEBANON TALKS.** On 29 May Netanyahu announced IDF forces had "
        "crossed the Litani and were operating in Beirut and the Bekaa Valley (first IDF action in Beirut in ~3 weeks), a 'tactical "
        "victory.' Washington had explicitly warned Israel off the capital to protect the Iran talks — so this is a NEW red-line "
        "crossing. Sweeping evacuation orders issued for ~7 southern towns south of the Zahrani; hundreds of thousands displaced. "
        "Lebanese MoPH: 142 killed in 72h, cumulative ~3,355 (vs ~3,244 on 28 May). IDF combat deaths now 24 (reconciled upward "
        "from the 28 May '22' baseline). All simultaneous with the first-ever direct Israel-Lebanon military talks at the Pentagon "
        "(see A4) — negotiate-while-bombing as one strategy.",
        ["Wikipedia Timeline of the 2026 Lebanon war (27-30 May entries; IDF and Lebanese MoPH figures) — independent of ToI",
         "Times of Israel (Netanyahu Litani/Beirut confirmation; evacuation orders) — Israeli centrist",
         "Lebanese Ministry of Public Health (death toll ~3,355; +142/72h) — operational/official",
         "Intel dossier 2026-05-30 A3"],
        "Litani crossing + Beirut/Bekaa operations = CONFIRMED ACTION (Netanyahu on record; ToI; timeline); evacuation orders + "
        "hundreds of thousands displaced = CONFIRMED; 142 killed/72h, cumulative ~3,355 = official (Lebanese MoPH); IDF KIA 24 = "
        "CONFIRMED (reconciled upward from 22). Beirut operation = NEW US red-line crossing."
    ),
    edge_bumps=[
        {"to": "israel", "type_contains": "ground_war",
         "new_type": "beirut_red_line_crossed_may29_idf_operating_in_beirut_bekaa_litani_crossed_142_killed_72h_3355_dead_idf_kia_24"},
        {"to": "hezbollah",
         "new_type": "beirut_bekaa_operations_litani_crossed_evacuation_orders_7_southern_towns_idf_kia_24"},
        {"to": "united-states"},
    ],
    trigger_notes=[
        {"match": "expanded military operation against Hezbollah",
         "note": "STAYS ACTIVE (fired 2026-05-27). INTENSIFIED 2026-05-30: Israel crossed Washington's explicit Beirut red line — Netanyahu confirmed IDF 'operating in Beirut and the Bekaa Valley' and across the Litani on 29 May, the first Beirut action in ~3 weeks (CONFIRMED). 142 killed in 72h (cumulative ~3,355); IDF KIA reconciled to 24. The Beirut crossing directly endangers the Iran-deal precondition ('end the war on all fronts including Lebanon') AND the separate US-brokered Israel-Lebanon ceasefire track — yet it ran simultaneously with the first Pentagon Israel-Lebanon military talks (negotiate-while-bombing as one strategy)."},
    ],
))

PAYLOADS.append(dict(
    nid="israel",
    summary_prepend=(
        "Day 92 (Saturday May 30). **ISRAEL CROSSED THE BEIRUT RED LINE — NETANYAHU CONFIRMED IDF 'OPERATING IN BEIRUT AND THE "
        "BEKAA' AND ACROSS THE LITANI ON 29 MAY ('tactical victory') — THE FIRST BEIRUT ACTION IN ~3 WEEKS AND A NEW CROSSING OF "
        "WASHINGTON'S EXPLICIT WARNING (issued to protect the Iran talks). Israel issued sweeping evacuation orders for ~7 southern "
        "towns south of the Zahrani; the Lebanese MoPH reported 142 killed/72h (cumulative ~3,355). IDF combat deaths reached 24 "
        "(RECONCILED UPWARD from the 28 May '22' baseline; a Givati Brigade soldier killed + 2 reservists wounded by a Hezbollah "
        "drone on 27 May). The Beirut operations ran SIMULTANEOUSLY with the first-ever direct Israel-Lebanon military talks at the "
        "Pentagon on 29 May — Israel's military and political tracks are one coercive strategy. Israeli elite dissent is now public: "
        "Haaretz ran 'Israel's Wars of Deception: Escalation Masquerading as Strategy' (treat as opinion, not intelligence — but a "
        "marker of center-left dissent over the Lebanon expansion as casualties rise). On the IRAN front Israel was NOT the actor "
        "in any new kinetic event this window; its energy stayed in Lebanon, so the Israeli-unilateral-Iran-strike trigger STAYS "
        "watching. The expanded-operation trigger STAYS ACTIVE (fired May 27).**"
    ),
    signal=s(
        "**ISRAEL CROSSED THE BEIRUT RED LINE — IDF 'OPERATING IN BEIRUT AND THE BEKAA,' LITANI CROSSED; 142 KILLED/72h; IDF KIA "
        "RECONCILED TO 24; SAME DAY AS THE FIRST PENTAGON ISRAEL-LEBANON TALKS.** Netanyahu (29 May) confirmed IDF forces crossed "
        "the Litani and were operating in Beirut and the Bekaa Valley — the first Beirut action in ~3 weeks — a 'tactical victory.' "
        "Washington had warned Israel off the capital to protect the Iran talks, making this a NEW red-line crossing. Sweeping "
        "evacuation orders for ~7 southern towns; Lebanese MoPH 142 killed/72h (cumulative ~3,355). IDF combat deaths 24 "
        "(reconciled upward from 22). All ran simultaneously with the first-ever Pentagon Israel-Lebanon military talks. Elite "
        "dissent surfaced publicly (Haaretz 'Wars of Deception' editorial — opinion, not intelligence). Israel was not the actor "
        "in any new Iran-front kinetic event; the unilateral-Iran-strike trigger stays watching.",
        ["Times of Israel (Netanyahu Litani/Beirut confirmation; evacuation orders) — Israeli centrist",
         "Wikipedia Timeline of the 2026 Lebanon war (IDF KIA 24; Lebanese MoPH 142/72h) — operational aggregator",
         "Haaretz editorial 'Israel's Wars of Deception' — opinion marker of elite dissent",
         "Intel dossier 2026-05-30 A3, A4, C (Israeli media tone)"],
        "Beirut/Bekaa + Litani crossing = CONFIRMED ACTION (Netanyahu on record); evacuation orders = CONFIRMED; 142/72h, "
        "~3,355 = official (Lebanese MoPH); IDF KIA 24 = CONFIRMED (reconciled from 22); Haaretz editorial = OPINION (not "
        "intelligence); Israel not the actor in the Iran-front this window = CONFIRMED non-event."
    ),
    edge_bumps=[
        {"to": "lebanon", "type_contains": "ground_war",
         "new_type": "beirut_red_line_crossed_may29_idf_operating_in_beirut_bekaa_litani_crossed_142_killed_72h_idf_kia_24"},
        {"to": "hezbollah",
         "new_type": "beirut_bekaa_operations_litani_crossed_idf_kia_24_givati_soldier_killed_by_drone"},
        {"to": "united-states", "type_contains": "military_alliance"},
    ],
    trigger_notes=[
        {"match": "Israeli unilateral kinetic action on Iran",
         "note": "STAYS watching. Israel was NOT the actor in any new Iran-front kinetic event this window; its kinetic energy stayed fully rotated to the Lebanon front (Beirut/Bekaa operations, Litani crossing). Israeli source-tone remains an open preference for a return to war in Iran (NPR/JPost carried prior), but no operational preparation surfaced. Operational floor intact."},
        {"match": "Second IDF KIA in southern Lebanon",
         "note": "IDF combat-death baseline reconciled UPWARD to 24 (from the 28 May brief's 22) — a Givati Brigade soldier killed + 2 reservists wounded by a Hezbollah drone on 27 May. Multiple ceasefire-window KIAs have now occurred; the ground war is being absorbed as a cost of the operation, not a constraint. Status left as-is (the expanded-operation trigger is the operative active trigger)."},
    ],
))

PAYLOADS.append(dict(
    nid="hezbollah",
    summary_prepend=(
        "Day 92 (Saturday May 30). **HEZBOLLAH ABSORBING THE EXPANDED ISRAELI OPERATION — NOW INSIDE BEIRUT AND THE BEKAA. On 29 "
        "May Netanyahu confirmed the IDF had crossed the Litani and was 'operating in Beirut and the Bekaa Valley' (first Beirut "
        "action in ~3 weeks); 142 Lebanese killed in 72h (cumulative ~3,355), with sweeping evacuation orders for ~7 southern "
        "towns. Hezbollah continued drone strikes on northern Israel — a Hezbollah drone killed a Givati Brigade soldier and "
        "wounded 2 reservists on 27 May, raising the IDF KIA baseline to 24. Hezbollah remains EXCLUDED from the underlying 45-day "
        "ceasefire arrangement and signs nothing — the deal's key vulnerability (analyst Michael Rubin: a ceasefire that doesn't "
        "disarm Hezbollah is 'illusionary'). The first-ever Pentagon Israel-Lebanon military talks (29 May) proceeded WITHOUT "
        "Hezbollah at the table while it was being struck — the negotiate-while-bombing pattern.**"
    ),
    signal=s(
        "**EXPANDED ISRAELI OP REACHES BEIRUT AND THE BEKAA; HEZBOLLAH DRONE KILLED A GIVATI SOLDIER (IDF KIA -> 24); HEZBOLLAH "
        "STILL EXCLUDED FROM THE CEASEFIRE TRACK.** Netanyahu confirmed (29 May) IDF operations inside Beirut and the Bekaa and "
        "across the Litani; 142 Lebanese killed/72h (cumulative ~3,355). Hezbollah continued drone strikes on northern Israel "
        "(Givati soldier killed + 2 reservists wounded, 27 May; IDF KIA -> 24). Hezbollah signs nothing and is excluded from the "
        "45-day ceasefire arrangement; the first-ever Pentagon Israel-Lebanon talks (29 May) proceeded without it. Rubin: ceasefire "
        "'illusionary' while Hezbollah keeps heavy weapons.",
        ["Times of Israel (Netanyahu Beirut/Bekaa/Litani) ; Lebanese MoPH (142/72h, ~3,355)",
         "Wikipedia Timeline of the 2026 Lebanon war (IDF KIA 24; Givati soldier/drone)",
         "The National 29 May (Pentagon talks; Rubin 'illusionary' take)",
         "Intel dossier 2026-05-30 A3, A4, D2"],
        "IDF Beirut/Bekaa operations + Litani crossing = CONFIRMED ACTION; Givati soldier killed by Hezbollah drone + 2 wounded, "
        "IDF KIA 24 = CONFIRMED; Hezbollah exclusion from the ceasefire arrangement = CONFIRMED; Rubin 'illusionary' = analyst take."
    ),
    edge_bumps=[
        {"to": "israel"},
        {"to": "lebanon"},
    ],
))

PAYLOADS.append(dict(
    nid="nuclear-program",
    summary_prepend=(
        "Day 92 (Saturday May 30). **THE NUCLEAR LIMB GOT HARDER, NOT CLOSER — IRAN PUBLICLY DENIES NEGOTIATIONS ARE EVEN HAPPENING "
        "AND REPRICES ITS ASK AS CASH. On 29 May Iran publicly claimed 'no negotiations' are taking place on its nuclear program "
        "(CLAIMED Iran), directly countering Trump's 'close to finalizing with strong inspections.' Araghchi reaffirmed a 'deadlock' "
        "on enriched material, with the topic 'postponed' to later stages (REPORTED — at the BRICS FM meeting). The genuinely new "
        "intelligence is Iran's MONEY-FIRST reframing: Fars (semi-official) asserts the unsigned 60-day MOU draft contains NO "
        "reference to dismantling/destroying nuclear material and that the deal's 'most important part' is the immediate $12bn "
        "frozen-asset release (REPORTED — Iran's framing, contested). Trump's counter-claim that the ~1,000 lbs HEU 'will be "
        "destroyed' is CLAIMED — US framing, with no signed text. The Mojtaba Khamenei directive that HEU not leave Iran stands "
        "un-walked-back; no proof-of-life surfaced — the directive watch is ~Day 9 of 14 (deadline ~June 5). Treat both the "
        "destruction clause (US) and the $12bn-first demand (Iran) as CLAIMED until a signed text exists. NO trigger moves.**"
    ),
    signal=s(
        "**IRAN PUBLICLY CLAIMS 'NO NEGOTIATIONS' ON THE NUCLEAR FILE; REPRICES ITS ASK AS $12bn CASH; DESTRUCTION CLAUSE DISPUTED.** "
        "On 29 May Iran countered Trump's 'close to finalizing' by claiming no nuclear negotiations are taking place (CLAIMED Iran); "
        "Araghchi reaffirmed a deadlock on enriched material ('postponed'). Fars says the draft MOU has NO HEU-destruction clause "
        "and that its centerpiece is the immediate $12bn frozen-asset release; Trump insists the HEU 'will be destroyed.' Both are "
        "CLAIMED by their respective sides — no signed text. Mojtaba's HEU-stays-in-Iran directive stands un-walked-back; ~Day 9 of "
        "14 (deadline ~June 5), no proof-of-life.",
        ["Times of Israel liveblog 29 May (Iran 'no negotiations') — reports Iran's claim",
         "The Tribune / Al Jazeera (Araghchi deadlock at BRICS FM meeting)",
         "Fars via wire summaries (no destruction clause; $12bn-first) — Iran framing, contested",
         "Reuters (Mojtaba directive, two senior sources) — single sourcing cluster",
         "Intel dossier 2026-05-30 A11, A2, B2"],
        "Iran 'no negotiations' = CLAIMED Iran (denied-by-implication by US); Araghchi deadlock = REPORTED/CONFIRMED; no-destruction-"
        "clause (Iran) and HEU 'will be destroyed' (US) = CLAIMED by each side; Mojtaba directive ~Day 9 of 14 = REPORTED, un-walked-"
        "back. No weight elevation on CLAIMED inputs."
    ),
    edge_bumps=[
        {"to": "iran"},
        {"to": "united-states"},
    ],
))

PAYLOADS.append(dict(
    nid="trump",
    summary_prepend=(
        "Day 92 (Saturday May 30). **TRUMP ENDED THE 29 MAY SITUATION ROOM MEETING WITHOUT SIGNING — AND HIS PUBLIC ACCOUNT OF THE "
        "DEAL IS NOW DIRECTLY CONTRADICTED BY TEHRAN. Trump made no 'final determination' on the 60-day MOU (CONFIRMED non-signature "
        "— CNBC); Rubio blamed 'disagreements over a word, a sentence' and projected 'a few days.' Trump publicly insists Iran's "
        "~1,000 lbs HEU 'will be destroyed' and that there will be 'no sanctions, no money, no nothing' (CLAIMED — US framing), "
        "which Fars rebutted point-blank (no destruction clause in the text; the centerpiece is a $12bn frozen-asset release). On "
        "the Accords, Trump escalated: he told the leaders of Saudi Arabia, UAE, Qatar, Pakistan, Turkey, Egypt, Jordan and Bahrain "
        "that joining the Abraham Accords is 'mandatory' after the Iran war — and per a US official the leaders, 'especially Saudi "
        "Arabia, Qatar, and Pakistan, appeared stunned… there was silence on the line, and Trump joked and asked if they are still "
        "there' (REPORTED — Axios). Trump's HEU/'no money' claims and the 'mandatory' Accords demand both remain RHETORIC/CLAIMED — "
        "no signed deal, no normalization. NO trigger moves.**"
    ),
    signal=s(
        "**TRUMP ENDS 29 MAY MEETING WITHOUT SIGNING; HIS DEAL ACCOUNT CONTRADICTED BY FARS; CALLS ACCORDS 'MANDATORY,' CAPITALS "
        "'STUNNED.'** No 'final determination' on the MOU (CNBC); Rubio: 'a word, a sentence,' 'a few days.' Trump insists the HEU "
        "'will be destroyed' and 'no money, no nothing' (CLAIMED — US framing), rebutted by Fars (no destruction clause; $12bn "
        "frozen-asset release is the centerpiece). On a call with eight Muslim-nation leaders, Trump said joining the Abraham "
        "Accords is 'mandatory' after the Iran war; per a US official the leaders 'appeared stunned… silence on the line.' Saudi "
        "reaffirmed its Palestinian-state precondition.",
        ["CNBC 29 May (meeting ended without a final determination); Rubio on record",
         "Fars via wire summaries (contradicts Trump's HEU/no-money framing)",
         "Axios / Bloomberg / NPR / Time (Accords 'mandatory'; 'stunned' / 'silence on the line')",
         "Intel dossier 2026-05-30 A2, A9, B2"],
        "Trump non-signature = CONFIRMED (CNBC); HEU 'will be destroyed' / 'no money' = CLAIMED (US framing, contradicted by Fars); "
        "Accords 'mandatory' + 'stunned'/'silence on the line' = REPORTED (Axios). No weight elevation on RHETORIC/CLAIMED."
    ),
    edge_bumps=[
        {"to": "iran"},
    ],
))

PAYLOADS.append(dict(
    nid="strait-of-hormuz",
    summary_prepend=(
        "Day 92 (Saturday May 30). **HORMUZ STILL ACTIVELY CONTESTED INSIDE THE CEASEFIRE — NEW SUSPECTED FLOATING MINE OFF OMAN, "
        "6th BLOCKADE-VESSEL INTERDICTION, AND A TOLL DISPUTE NOW PITTING THE US AGAINST ITS OWN MEDIATOR. Oman's Maritime Security "
        "Centre warned on 30 May of a floating object suspected to be a naval mine, sighted west of the Inshore Traffic Zone within "
        "Omani territorial waters, urging vessels to keep clear (CONFIRMED — Oman MSC advisory). The US military disabled the "
        "Gambia-flagged Lian Star in the Gulf of Oman (6th vessel stopped during the blockade) after it tried to enter Iranian "
        "ports; Hegseth: the 'blockade is very much still in place,' Hormuz must remain 'an open, toll-free strait' (CONFIRMED). "
        "Separately, the US Treasury reportedly threatened to sanction OMAN if it imposes Hormuz transit tolls (REPORTED — single "
        "ToI liveblog headline) — directly tied to Iran's desired Oman-mediated toll mechanism in the draft MOU; the toll question "
        "is now a live point of friction with the mediator itself. This is fresh operational evidence Hormuz remains mined and "
        "contested even as Brent de-prices the tail (~$92, -22% MoM) — the physical floor under oil. The blockade-active reality "
        "sits AGAINST the MOU's term ('blockade lifted in proportion to restored shipping').**"
    ),
    signal=s(
        "**NEW SUSPECTED MINE OFF OMAN (30 MAY); LIAN STAR INTERDICTION (6th VESSEL); US-TREASURY-VS-OMAN TOLL FRICTION.** Oman's "
        "Maritime Security Centre warned (30 May) of a floating object suspected to be a naval mine within Omani territorial waters, "
        "urging vessels to keep clear. The US disabled the Lian Star in the Gulf of Oman (6th blockade vessel); Hegseth said the "
        "blockade is 'very much still in place' and Hormuz must remain 'open, toll-free.' The US Treasury reportedly threatened to "
        "sanction Oman over Hormuz tolls — colliding with Iran's Oman-mediated toll ambition in the draft MOU. Hormuz remains mined "
        "and contested inside the ceasefire — the physical floor under oil even as the tail de-prices.",
        ["Oman Maritime Security Centre advisory 30 May — operational/official",
         "Iran International liveblog 30 May (Lian Star); Hegseth on record 30 May",
         "Times of Israel liveblog 28 May (US Treasury-Oman tolls) — REPORTED, single headline",
         "Intel dossier 2026-05-30 A8, A1"],
        "Suspected-mine advisory = CONFIRMED ACTION (Oman MSC operational/official); Lian Star interdiction = REPORTED-to-CONFIRMED; "
        "Hegseth 'blockade still in place / toll-free' = CONFIRMED; US Treasury-Oman toll threat = REPORTED (single headline)."
    ),
    edge_bumps=[
        {"to": "iran"},
        {"to": "united-states"},
        {"to": "brent-crude"},
    ],
))

PAYLOADS.append(dict(
    nid="mojtaba-khamenei",
    summary_prepend=(
        "Day 92 (Saturday May 30). **MOJTABA HEU-DIRECTIVE WATCH ~DAY 9 OF 14 (DEADLINE ~JUNE 5) — STILL NO PROOF-OF-LIFE, STILL "
        "UN-WALKED-BACK. The directive that Iran's HEU not leave the country (Reuters, two senior sources) stands; no video/audio "
        "appearance surfaced this window. Fars's money-first reframing of the deal (the centerpiece is a $12bn frozen-asset release, "
        "not nuclear concessions; intel A2/B2) reprices Iran's ask in a direction CONSISTENT with the directive's substance — "
        "keep the HEU, take the cash — but does not confirm or walk it back. The negative-space signal persists; no trigger move.**"
    ),
    signal=s(
        "**HEU-DIRECTIVE WATCH ~DAY 9 OF 14 — NO PROOF-OF-LIFE, UN-WALKED-BACK; FARS MONEY-FIRST REFRAME IS DIRECTIONALLY CONSISTENT.** "
        "Mojtaba's directive that HEU stay inside Iran remains un-walked-back with no appearance this window. Iran's new $12bn-first "
        "framing (keep the HEU, take the cash) aligns with the directive's substance without confirming it. Deadline ~June 5.",
        ["Reuters (Mojtaba directive, two senior sources) — single sourcing cluster",
         "Fars via wire summaries ($12bn-first; no destruction clause) — Iran framing",
         "Intel dossier 2026-05-30 A11, A2"],
        "Directive un-walked-back, no proof-of-life = CONFIRMED ABSENCE; $12bn-first reframe = REPORTED (Iran framing); no weight "
        "elevation; trigger ~Day 9 of 14 stays watching."
    ),
))

PAYLOADS.append(dict(
    nid="qatar",
    summary_prepend=(
        "Day 92 (Saturday May 30). **QATAR STAYS MEDIATION-FORWARD — IN THE PENTAGON ISRAEL-LEBANON ECOSYSTEM AND COOL ON THE "
        "ACCORDS. The first-ever Pentagon Israel-Lebanon military talks (29 May, hosted by Under Sec. Colby) were called "
        "'productive,' to feed a State-led political track 'next week' — part of the Gulf mediation ecosystem Qatar sits within. On "
        "the Accords, Trump's 'mandatory' demand left Gulf capitals (Qatar among those 'stunned') slow-walking; Saudi reaffirmed a "
        "Palestinian-state precondition. On the commodity side the Qatar-disruption premium is CRACKING on the fast legs: urea is "
        "-35% MoM and Cheniere -17% MoM as deal-anticipation prices in Gulf LNG/fertilizer export normalization — though TTF gas "
        "(EUR45.96/MWh, ~+30% YoY floor) and the helium read remain elevated, and the Qatar Ras Laffan force majeure persists.**"
    ),
    signal=s(
        "**QATAR IN THE PENTAGON ISRAEL-LEBANON ECOSYSTEM, COOL ON ACCORDS; QATAR-DISRUPTION PREMIUM CRACKS ON FAST LEGS (UREA -35% "
        "MoM, CHENIERE -17%).** The first Pentagon Israel-Lebanon military talks (29 May) were 'productive,' feeding a State track "
        "'next week.' Trump's 'mandatory' Accords demand left Qatar among the 'stunned' Gulf capitals; Saudi reaffirmed a "
        "Palestinian-state condition. Deal-anticipation is unwinding the Qatar LNG/fertilizer premium on the fast legs (urea -35% "
        "MoM, Cheniere -17% MoM), while TTF (~+30% YoY) and helium stay elevated and the Ras Laffan force majeure persists.",
        ["The National / Arab News / WaPo / ToI (Pentagon Israel-Lebanon talks 29 May)",
         "Axios / Bloomberg (Accords 'mandatory'; Gulf 'stunned')",
         "TradingEconomics / Argus (urea -35% MoM); markets dossier C6",
         "Intel dossier 2026-05-30 A4, A9; Market dossier C6"],
        "Pentagon talks 'productive' = CONFIRMED; Accords 'mandatory' / 'stunned' = REPORTED; urea -35% MoM + Cheniere -17% = "
        "CONFIRMED (data); TTF/helium elevated, Ras Laffan FM persists = carried."
    ),
    edge_bumps=[
        {"to": "natural-gas-lng"},
    ],
))

PAYLOADS.append(dict(
    nid="saudi-arabia",
    summary_prepend=(
        "Day 92 (Saturday May 30). **SAUDI SLOW-WALKS TRUMP'S 'MANDATORY' ACCORDS DEMAND, REAFFIRMS THE PALESTINIAN-STATE "
        "CONDITION. Trump told eight Muslim-nation leaders it is 'mandatory' to normalize with Israel after the Iran war; a US "
        "official said the leaders — 'especially Saudi Arabia, Qatar, and Pakistan — appeared stunned… silence on the line' "
        "(REPORTED — Axios). Saudi Arabia reaffirmed it will only normalize on a 'credible, irreversible' path to a Palestinian "
        "state, which Israel's government opposes (REPORTED — Bloomberg, Time). The Tadawul was steady (11,027, +0.4% 1D). The "
        "coordinated Gulf slow-walk continues; the Accords-Iran-deal linkage is now explicit and contested. No normalization "
        "signed — RHETORIC/DIPLOMATIC PRESSURE, no trigger move.**"
    ),
    signal=s(
        "**SAUDI REAFFIRMS PALESTINIAN-STATE PRECONDITION, SLOW-WALKS TRUMP'S 'MANDATORY' ACCORDS DEMAND.** Trump called Accords "
        "accession 'mandatory' for eight Muslim-nation leaders; per a US official Saudi/Qatar/Pakistan 'appeared stunned… silence "
        "on the line.' Saudi reaffirmed it will normalize only on a 'credible, irreversible' path to a Palestinian state, which "
        "Israel opposes. Tadawul steady (11,027, +0.4%). No normalization signed.",
        ["Axios (24/28 May, 'stunned/silence on the line')",
         "Bloomberg (Trump pushes Saudis to recognize Israel) / Time",
         "Intel dossier 2026-05-30 A9"],
        "Accords 'mandatory' / Gulf 'stunned' = REPORTED; Saudi Palestinian-state precondition = REPORTED (Bloomberg/Time); no "
        "normalization signed = RHETORIC/DIPLOMATIC PRESSURE. No weight elevation."
    ),
    edge_bumps=[
        {"to": "israel"},
        {"to": "united-states"},
    ],
))

PAYLOADS.append(dict(
    nid="uae",
    summary_prepend=(
        "Day 92 (Saturday May 30). **UAE AMONG GULF CAPITALS SLOW-WALKING THE 'MANDATORY' ACCORDS DEMAND. Trump told the leaders "
        "of Saudi/UAE/Qatar/Pakistan/Turkey/Egypt/Jordan/Bahrain that joining the Abraham Accords is 'mandatory' after the Iran war "
        "(REPORTED — Axios, ToI, Bloomberg, NPR). The UAE (already an Accords member) sits inside the coordinated Gulf resistance to "
        "the linkage of normalization to the Iran deal; no new UAE commitment. RHETORIC/DIPLOMATIC PRESSURE — no trigger move.**"
    ),
    signal=s(
        "**UAE INSIDE THE GULF SLOW-WALK ON TRUMP'S 'MANDATORY' ACCORDS PUSH.** Trump told eight Muslim-nation leaders (UAE among "
        "them) that Accords accession is 'mandatory' after the Iran war; Gulf capitals were 'stunned.' No new UAE commitment; the "
        "Accords-Iran-deal linkage is explicit and contested.",
        ["Axios / ToI / Bloomberg / NPR (Accords 'mandatory')",
         "Intel dossier 2026-05-30 A9"],
        "Accords 'mandatory' = REPORTED; no new normalization = RHETORIC/DIPLOMATIC PRESSURE. No weight elevation."
    ),
))

PAYLOADS.append(dict(
    nid="pakistan",
    summary_prepend=(
        "Day 92 (Saturday May 30). **PAKISTAN AMONG THE CAPITALS 'STUNNED' BY TRUMP'S 'MANDATORY' ACCORDS DEMAND — BUILDING ON ITS "
        "26 MAY REJECTION. Trump told eight Muslim-nation leaders that joining the Abraham Accords is 'mandatory' after the Iran "
        "war; a US official singled out Saudi Arabia, Qatar, and Pakistan as the leaders who 'appeared stunned… there was silence "
        "on the line' (REPORTED — Axios). Pakistan, which rejected the demand on 26 May, remains a non-normalizer; the coordinated "
        "Gulf/Muslim slow-walk continues. RHETORIC/DIPLOMATIC PRESSURE — no trigger move.**"
    ),
    signal=s(
        "**PAKISTAN 'STUNNED' BY 'MANDATORY' ACCORDS DEMAND, CONTINUES TO RESIST.** Trump's 'mandatory' Accords push singled out "
        "Pakistan (with Saudi/Qatar) among the 'stunned' leaders; Pakistan had already rejected the demand on 26 May. No "
        "normalization; coordinated slow-walk intact.",
        ["Axios (Accords 'mandatory'; Pakistan among 'stunned')",
         "Intel dossier 2026-05-30 A9"],
        "Accords 'mandatory' + Pakistan 'stunned' = REPORTED; Pakistan non-normalizer = continuation. No weight elevation."
    ),
))

PAYLOADS.append(dict(
    nid="shipping-tankers",
    summary_prepend=(
        "Day 92 (Saturday May 30). **THE BLOCKADE IS STILL INTERDICTING IRAN-BOUND TRAFFIC — 6th VESSEL STOPPED — AND HORMUZ "
        "REMAINS MINED, BUT THE PAPER FREIGHT TAPE IS FADING THE DEAL. The US disabled the Gambia-flagged Lian Star in the Gulf of "
        "Oman (6th vessel stopped during the blockade); a new suspected floating mine was sighted off Oman (30 May). The slow "
        "physical legs have NOT unwound: VLCC volumes -36% (longer voyages), war-risk insurance still 3-8% of hull (~8x pre-war) — "
        "but no fresh late-May VLCC/AWRP print this window (freshest hard VLCC data ~Week 16, late April; carried, not reconfirmed). "
        "Equity proxy faded: BOAT -0.5% 1D / -1.4% MoM, Frontline +0.4% 1D / -4.4% MoM (paper deal-fade vs physical book still "
        "locked). The paper-vs-physical bifurcation persists; the fast legs (oil, fertilizer, LNG) de-priced first, the slow legs "
        "(insurance, freight) lag 6-12 weeks even on a clean deal.**"
    ),
    signal=s(
        "**BLOCKADE INTERDICTS 6th VESSEL (LIAN STAR); NEW OMAN MINE ALERT; PAPER FREIGHT FADES, PHYSICAL STILL LOCKED.** The US "
        "disabled the Lian Star in the Gulf of Oman (6th blockade vessel); Oman warned of a new suspected mine (30 May). VLCC "
        "volumes -36% (longer voyages) and war-risk insurance ~8x pre-war have NOT unwound (carried — no fresh late-May print). "
        "Equity proxies faded on deal-anticipation: BOAT -1.4% MoM, Frontline -4.4% MoM. Paper-vs-physical bifurcation intact.",
        ["Iran International liveblog 30 May (Lian Star); Oman MSC advisory 30 May",
         "Market dossier Section F (VLCC/AWRP — no fresh print, carried) ; BOAT/Frontline yfinance",
         "Intel dossier 2026-05-30 A1, A8; Market dossier C1, C6"],
        "Lian Star interdiction = REPORTED-to-CONFIRMED; Oman mine alert = CONFIRMED; VLCC -36% / AWRP 8x = carried (last hard "
        "print ~Week 16, NOT reconfirmed this window); BOAT/Frontline deltas = CONFIRMED (yfinance)."
    ),
    edge_bumps=[
        {"to": "strait-of-hormuz"},
        {"to": "united-states"},
    ],
))

PAYLOADS.append(dict(
    nid="marine-war-risk-insurance",
    summary_prepend=(
        "Day 92 (Saturday May 30). **THE SLOW PHYSICAL FLOOR — WAR-RISK INSURANCE STILL ~8x PRE-WAR, NOT UNWINDING, BUT UNVERIFIED "
        "THIS WINDOW. No fresh late-May Gulf war-risk-insurance print (Lloyd's/Marsh) was retrieved; the carried read is 3-8% of "
        "hull vs ~0.25% pre-war (8x+), NOT unwinding. The operational case for the floor strengthened: a new suspected mine off "
        "Oman (30 May), the Lian Star interdiction (6th vessel), and an active blockade keep Hormuz contested even as Brent "
        "de-prices the tail (-22% MoM). The bifurcation is the signal: the fast legs (oil futures, fertilizer, LNG equity) "
        "de-priced; insurance and freight lag 6-12 weeks even on a clean deal (Khaleej Times: 'Hormuz reopening won't mean cheaper "
        "shipping'). Do NOT state the physical stack is 'intact' — only that the slow legs are unverified-but-presumed-elevated.**"
    ),
    signal=s(
        "**WAR-RISK INSURANCE ~8x PRE-WAR (CARRIED, UNVERIFIED THIS WINDOW); OPERATIONAL FLOOR REINFORCED BY NEW OMAN MINE + LIAN "
        "STAR.** No fresh Lloyd's/Marsh print this window — the 3-8%-of-hull (8x+) read is carried, not reconfirmed. New suspected "
        "mine off Oman (30 May) + the 6th-vessel interdiction + active blockade keep the floor under freight while the fast legs "
        "de-price. Insurance/freight lag 6-12 weeks even on a clean deal.",
        ["Market dossier Section F (war-risk insurance — no fresh print, carried)",
         "Oman MSC advisory 30 May; Iran International (Lian Star) 30 May",
         "Intel dossier 2026-05-30 A8, A1; Market dossier C1, C6"],
        "Insurance ~8x pre-war = carried/unverified this window (no fresh Lloyd's/Marsh print); mine alert + interdiction = "
        "CONFIRMED operational reinforcement of the floor. No price encoded; honest-coverage flag respected."
    ),
))

PAYLOADS.append(dict(
    nid="opec-plus",
    summary_prepend=(
        "Day 92 (Saturday May 30). **BRENT'S BIGGEST MONTHLY LOSS SINCE 2020 (-22% MoM TO ~$92) REMOVES THE WINDFALL THE GROUP HAD "
        "BEEN BANKING ON A SHUT HORMUZ. The peace-dividend de-pricing of the Hormuz tail premium pushed Brent decisively sub-$100 "
        "on the unsigned 60-day MOU; analysts now see $90-100 'for the next couple of months' until a lasting peace is clear "
        "(CNBC). The structural ~$30 premium above the ~$73 pre-crisis baseline is intact (Brent still +18-26% vs Feb 28), but the "
        "~$7-8 tail premium has de-priced. Asymmetry is now extreme from a low-premium base: a deal collapse or a non-calibrated "
        "Iranian strike gaps Brent +$8-15 in a session. No new OPEC+ policy action this window; the cartel's spare-capacity "
        "arithmetic remains the structural backdrop.**"
    ),
    signal=s(
        "**PEACE-DIVIDEND DE-PRICING: BRENT -22% MoM TO ~$92, BIGGEST MONTHLY LOSS SINCE 2020; $90-100 SEEN 'FOR A COUPLE MONTHS.'** "
        "The unsigned 60-day MOU + Hormuz-reopen hopes dumped the tail premium; structural ~$30 premium above $73 intact. Analysts "
        "(CNBC) see $90-100 until a lasting peace is clear. Asymmetry extreme from a low base — a deal collapse or non-calibrated "
        "Iranian act gaps Brent +$8-15. No new OPEC+ policy this window.",
        ["CNBC 29 May (Brent biggest monthly loss since 2020); TradingEconomics Brent",
         "Intel dossier 2026-05-30 A7, D1; Market dossier C1"],
        "Brent -22% MoM to ~$92 = CONFIRMED (data); $90-100 analyst band = analyst take (REPORTED); structural premium intact = "
        "carried. No new OPEC+ action = non-event."
    ),
    edge_bumps=[
        {"to": "brent-crude"},
    ],
))

PAYLOADS.append(dict(
    nid="houthis",
    summary_prepend=(
        "Day 92 (Saturday May 30). **RED SEA THREAT-ACTIVE, NOT ACTION-ACTIVE — NO CONFIRMED LATE-MAY VESSEL ATTACK (CONFIRMED "
        "NON-EVENT). Searches surfaced threats and 'signals' of renewed Houthi Red Sea attacks (gCaptain: 'Red Sea Corridor Slips "
        "Back Into Crisis as Houthi Threats Resurface') but NO confirmed new merchant-vessel strike in late May 2026. The "
        "widely-circulated 'Scarlet Ray' tanker attack traces to September 2025, not now — a stale-source trap avoided. The "
        "double-chokepoint wildcard stays at watching. RHETORIC/THREAT only — no weight change.**"
    ),
    signal=s(
        "**RED SEA THREAT-ACTIVE, NOT ACTION-ACTIVE — NO CONFIRMED LATE-MAY VESSEL STRIKE (CONFIRMED NON-EVENT).** Houthi threats "
        "resurfaced (gCaptain) but no confirmed new merchant-vessel attack in late May; the circulating 'Scarlet Ray' attack dates "
        "to Sept 2025 (stale-source trap avoided). Double-chokepoint wildcard stays at watching; no weight change.",
        ["gCaptain / Global Security Review (threat framing)",
         "Date-check: 'Scarlet Ray' = Sept 2025 (stale-source rejected)",
         "Intel dossier 2026-05-30 A10"],
        "No confirmed late-May vessel strike = CONFIRMED NON-EVENT; threats = RHETORIC/THREAT only; 'Scarlet Ray' = stale (Sept "
        "2025). No weight change."
    ),
))

PAYLOADS.append(dict(
    nid="red-sea",
    summary_prepend=(
        "Day 92 (Saturday May 30). **RED SEA QUIET-BUT-THREATENED — NO CONFIRMED NEW ATTACK IN LATE MAY (CONFIRMED NON-EVENT). "
        "Houthi threats of renewed Red Sea attacks resurfaced in the press, but no confirmed new merchant-vessel strike materialized; "
        "the circulating 'Scarlet Ray' incident traces to September 2025. The corridor remains threat-active, not action-active; the "
        "double-chokepoint (Red Sea + Hormuz) wildcard stays at watching. No weight change.**"
    ),
    signal=s(
        "**NO CONFIRMED NEW RED SEA ATTACK IN LATE MAY (CONFIRMED NON-EVENT).** Houthi threats resurfaced but no confirmed strike; "
        "'Scarlet Ray' = Sept 2025. Corridor threat-active, not action-active.",
        ["gCaptain / Global Security Review; date-check 'Scarlet Ray' Sept 2025",
         "Intel dossier 2026-05-30 A10"],
        "No confirmed strike = CONFIRMED NON-EVENT; threats = RHETORIC. No weight change."
    ),
))

PAYLOADS.append(dict(
    nid="kuwait",
    summary_prepend=(
        "Day 92 (Saturday May 30). **NO NEW KUWAIT-DIRECTED KINETIC EVENT THIS WINDOW — THE 28 MAY IRGC MISSILE (INTERCEPTED OVER "
        "KUWAIT, ZERO CASUALTIES) WAS NOT FOLLOWED BY ANY FURTHER STRIKE THROUGH 30 MAY. The new Gulf enforcement event is the US "
        "disabling of the Lian Star in the Gulf of Oman (not Kuwaiti airspace). Kuwait remains the site of the last calibrated "
        "Iranian missile, now confirmed as a face-saving one-off, not the start of an escalation. No trigger move.**"
    ),
    signal=s(
        "**NO NEW KUWAIT-DIRECTED EVENT — 28 MAY INTERCEPTED MISSILE WAS A ONE-OFF (CONFIRMED NON-ESCALATION).** No further strike "
        "near Kuwait through 30 May; the new Gulf enforcement action (Lian Star) was in the Gulf of Oman. Kuwait's role this window "
        "is the site of the last calibrated, intercepted, zero-casualty Iranian missile.",
        ["Iran International liveblog 30 May; Intel dossier 2026-05-30 A1"],
        "No new Kuwait-directed kinetic event = CONFIRMED NON-EVENT; 28 May missile confirmed face-saving one-off. No weight change."
    ),
))

PAYLOADS.append(dict(
    nid="irgc",
    summary_prepend=(
        "Day 92 (Saturday May 30). **IRGC HELD FIRE AFTER THE 28 MAY CALIBRATED MISSILE — NON-ESCALATION CONFIRMED. No further IRGC "
        "kinetic action through 30 May following the single intercepted, zero-casualty ballistic missile at the US airbase in "
        "Kuwait (the 2020 Ain al-Assad template). The window's Gulf story is US enforcement (the Lian Star interdiction, 6th "
        "vessel) and a new suspected mine off Oman, not an IRGC offensive. Consistent with escalation MANAGEMENT (Sadjadpour), not "
        "escalation to war; Iran reverted to the table with a money-first ($12bn) ask. No trigger move.**"
    ),
    signal=s(
        "**IRGC HELD FIRE AFTER THE 28 MAY CALIBRATED MISSILE — NON-ESCALATION CONFIRMED.** No further IRGC kinetic action through "
        "30 May; the Gulf story is US enforcement (Lian Star, 6th vessel) and a new Oman mine alert, not an IRGC offensive. "
        "Escalation management, not escalation to war.",
        ["Iran International liveblog 30 May; Intel dossier 2026-05-30 A1, D3"],
        "No further IRGC kinetic action = CONFIRMED NON-EVENT; consistent with calibrated/face-saving 28 May missile. No weight "
        "change."
    ),
))

# ===========================================================================
# LIST B — MARKET / COMMODITY
# ===========================================================================

PAYLOADS.append(dict(
    nid="brent-crude",
    summary_prepend=(
        "Day 92 (Saturday May 30; Friday 29 May close). **THE PEACE-DIVIDEND DE-PRICING IS NOW CONFIRMED — BRENT $92.05, -22% MoM, "
        "ITS BIGGEST MONTHLY LOSS SINCE 2020; THE SUB-$100 TRIGGER RESOLVES. Brent closed ~$92.05 (-1.8% 1D, -22.0% MoM, +18.4% 3M, "
        "still +26% vs the ~$73 Feb-28 baseline); WTI $87.36 (-18.3% MoM). The unsigned 60-day MOU + Hormuz-reopen hopes dumped the "
        "~$7-8 tail premium over the month; the ~$30 structural premium above $73 is intact. Sell-side desks (CNBC) see $90-100 "
        "'for at least the next couple of months' — a real war-risk premium persists even sub-$100 because Iran retains "
        "Hormuz-disruption capacity and the blockade is still active (Lian Star interdiction; new Oman mine alert, intel A1/A8). "
        "**The 'Brent breaks $100 sustained 3+ sessions' trigger (firing-day1 straddle on May 27) now RESOLVES: Brent printed "
        "sub-$100 cleanly across multiple sessions (sub-$100 May 25, ~$94 May 27, ~$93 May 28, $92.05 May 29) — Goldman's $120 Q3 "
        "base case is mathematically foreclosed; JPM's $60 2026-average case re-enters the band. This is TAIL-RISK de-pricing on "
        "deal-anticipation, NOT structural normalization — Hormuz is physically still contested.** Asymmetry is now violent from a "
        "low-premium base: a deal collapse (the Trump-vs-Fars HEU-destruction contradiction + the $12bn frozen-asset demand, intel "
        "A2) OR a NON-calibrated Iranian strike OR a Lebanon-driven break of the talks gaps Brent +$8-15 toward $105-115 in a "
        "session; a Trump SIGNATURE grinds Brent toward the high-$80s. The physical stack's fast legs de-priced (urea -35% MoM, "
        "Cheniere -17% MoM) but the slow legs lag: war-risk insurance ~8x, VLCC volumes -36% (carried, unverified this window). "
        "DATA NOTE: yfinance/web prints now agree (Brent low-$90s) — the late-May roll/sign artifacts have cleared.**"
    ),
    current={
        "price": "Brent $92.05 (Friday 29 May close); WTI $87.36; Heating Oil $3.54/gal; RBOB $3.13/gal; European TTF Gas EUR45.96/MWh (-2.2% 1D, ~+30% YoY floor intact).",
        "delta_1d": "-1.8% (29 May; data prints now agree — the late-May roll/sign artifacts have cleared).",
        "delta_1m": "-22.0% MoM — biggest monthly loss since 2020; net DE-pricing of the Hormuz tail premium on the unsigned 60-day MOU.",
        "delta_3m": "+18.4% 3M; still +26% vs the ~$73 Feb-28 pre-crisis baseline — the ~$30 structural premium intact, only the ~$7-8 tail premium compressed.",
        "trigger_status": "'Brent breaks $100 sustained 3+ sessions' RESOLVED (confirmed sub-$100): sub-$100 May 25, ~$94 May 27, ~$93 May 28, $92.05 May 29 = clean multi-session sub-$100. Goldman $120 Q3 base case mathematically foreclosed; JPM $60 2026-average re-enters the band.",
        "asymmetry": "EXTREME from a low-premium base. Upside-shock conditional on an IRANIAN act or a deal break: a deal collapse (Trump-vs-Fars HEU contradiction + $12bn frozen-asset demand), a NON-calibrated Iranian strike, or a Lebanon-driven break of the talks gaps Brent +$8-15 toward $105-115 in a session. A Trump signature grinds Brent toward the high-$80s.",
        "paper_physical_bifurcation": "Fast legs de-priced (urea -35% MoM, Cheniere -17% MoM, LNG/fertilizer equity). Slow legs lag 6-12 weeks: war-risk insurance ~8x pre-war, VLCC volumes -36% (longer voyages) — CARRIED, not reconfirmed this window (freshest hard VLCC ~Week 16). Hormuz physically contested (new Oman mine alert 30 May; Lian Star interdiction)."
    },
    snapshot={
        "date": "2026-05-29",
        "price": "Brent $92.05 (-1.8% 1D, -22.0% MoM); WTI $87.36",
        "trigger": "PEACE-DIVIDEND DE-PRICING CONFIRMED. Unsigned 60-day MOU + Hormuz-reopen hopes drove Brent's biggest monthly loss since 2020. The 'Brent breaks $100 sustained 3+ sessions' trigger resolves on clean multi-session sub-$100 closes — Goldman $120 Q3 foreclosed; JPM $60 re-enters the band.",
        "delta_context": "Tail-risk de-pricing, NOT structural normalization — Hormuz physically still contested (new Oman mine alert; Lian Star interdiction). Asymmetry violent from a low base: deal collapse / non-calibrated Iranian strike / Lebanon break gaps Brent +$8-15 toward $105-115; a signature grinds toward high-$80s."
    },
    edge_bumps=[
        {"to": "strait-of-hormuz"},
        {"to": "india"},
    ],
    trigger_status=[
        {"match": "Brent breaks $100 sustained 3+ sessions", "status": "resolved", "resolved": True,
         "note": "RESOLVED 2026-05-30 (confirmed). Brent printed sub-$100 cleanly across multiple sessions: sub-$100 May 25, ~$94 May 27, ~$93 May 28, $92.05 May 29 close (-22% MoM, biggest monthly loss since 2020). Goldman's $120 Q3 base case is mathematically foreclosed; JPM's $60 2026-average re-enters the band. The de-pricing is TAIL-RISK on deal-anticipation, not structural (Hormuz physically still contested — new Oman mine alert, Lian Star interdiction). Convexity now skewed violently to the upside-shock side from a low-premium base, conditional on an Iranian act / deal break."},
    ],
))

PAYLOADS.append(dict(
    nid="gold",
    summary_prepend=(
        "Day 92 (Saturday May 30; Friday 29 May close). **REVERSAL — GOLD DID NOT STAY BELOW $4,400; THE 'HEDGE IS DEAD / SUB-$4,400 "
        "WATCH' CALL FROM 28 MAY DID NOT SUSTAIN. Gold's 28 May break below $4,400 (two-month low ~$4,380) REVERSED WITHIN A "
        "SESSION: +2.56% to $4,524 on 29 May (Fortune; +$113 from the prior $4,411), and ~$4,560 (CNBC/markets, +1.4% 1D); it is "
        "~flat-to-slightly-negative on the month (~-0.7% to +0.3%) and +36% YoY. The sub-$4,400 dip lasted ONE session — so the 28 "
        "May 'gold below $4,400 sustained 5+ sessions = second-leg premium unwind (Day 1)' watch is marked UNTRIPPED/RESET, not "
        "activating. The driver was the SOFTER monthly PCE (April monthly +0.4% vs +0.5% expected, released 28 May) dialing back "
        "the Fed rate-HIKE bets that had crushed gold, plus a softer dollar (DXY 98.91) — note gold ROSE on de-escalation headlines "
        "(counter to the simple 'ceasefire = sell gold' read), so the dollar-weakness/inflation-hedge bid reasserted. **The "
        "cycle-long regime read HOLDS: gold trades on REAL YIELDS and the FED, not on the crisis.** The $4,600 regime-shift trigger "
        "remains BELOW threshold. Do NOT encode a one-day low as a regime change in either direction.**"
    ),
    current={
        "price": "$4,560.50 (Friday 29 May close; +1.4% 1D). 29 May intraday/alt prints $4,524-$4,580 (Fortune $4,524 +$113/+2.56%; CNBC ~$4,539-4,580). Reversed off the 28 May two-month low ~$4,380. Silver $75.62 (-0.0% 1D, +5.7% MoM); Copper $6.36/lb (-0.6% 1D, +8.2% MoM — AI/China bid); Platinum $1,922; Palladium $1,361.",
        "delta_1d": "+1.4% (29 May) — climbing for a second straight session; the 28 May sub-$4,400 break reversed within a session (+2.56% to $4,524).",
        "delta_1m": "~+0.3% (roughly flat on the month; the sub-$4,400 dip was a one-session event).",
        "delta_3m": "-13.9% (the cycle underperformer, but no regime change — trades on real yields/Fed, not the crisis).",
        "regime": "INFLATION + REAL-YIELDS regime CONFIRMED — softer April monthly PCE (+0.4% vs +0.5% exp) dialed back rate-HIKE bets and a softer dollar (DXY 98.91) drove the rebound. Gold rose on de-escalation headlines (dollar-weakness/inflation-hedge bid reasserted), so the mechanism is muddier than risk-on/off. The regime flips only on a FINANCIAL-SYSTEM-risk mutation (Gulf-exposed bank distress, sovereign wobble), not on oil/inflation.",
        "watching_threshold": "Gold sustains above $4,600 for 3+ sessions = regime-shift confirmed — remains BELOW threshold at ~$4,560. The 28 May 'gold below $4,400 sustained 5+ sessions = second-leg premium unwind' watch is UNTRIPPED/RESET — the sub-$4,400 dip lasted ONE session and reversed +2.56%. Do NOT encode a one-day low as a regime change in either direction."
    },
    snapshot={
        "date": "2026-05-29",
        "price": "$4,524-4,560 (+1.4% to +2.56% 1D)",
        "trigger": "REVERSAL — gold reclaimed $4,500+ within a session after the 28 May break below $4,400 (two-month low ~$4,380). Driver: softer April monthly PCE (+0.4% vs +0.5% exp) dialed back Fed rate-HIKE bets + softer dollar; gold rose on de-escalation headlines (dollar-weakness/inflation-hedge bid reasserted).",
        "delta_context": "The 'sub-$4,400 sustained 5+ sessions' watch is UNTRIPPED/RESET — the dip lasted one session. Regime read HOLDS (real yields/Fed, not crisis). $4,600 regime-shift trigger still below threshold. ~flat MoM, +36% YoY."
    },
    edge_bumps=[
        {"to": "us-10y-yield"},
        {"to": "fed"},
    ],
    trigger_notes=[
        {"match": "Gold sustains above $4,600",
         "note": "STAYS WATCHING, BELOW THRESHOLD at ~$4,560. CORRECTION TO THE 28 MAY READ: the OPPOSITE watch level ('gold below $4,400 sustained 5+ sessions = second-leg premium unwind') that was marked ACTIVATING (Day 1) on 28 May is now UNTRIPPED/RESET — the sub-$4,400 break was a ONE-SESSION event that reversed +2.56% to $4,524 on 29 May (then ~$4,560). Gold rose on a softer April monthly PCE (+0.4% vs +0.5% exp) dialing back rate-HIKE bets + a softer dollar; it ROSE on de-escalation headlines, so the dollar-weakness/inflation-hedge bid reasserted. Regime read HOLDS (real yields/Fed, not crisis); $4,600 still below threshold. Do NOT encode the one-day low as a regime change in either direction."},
    ],
))

PAYLOADS.append(dict(
    nid="nifty-50",
    summary_prepend=(
        "Day 92 (Saturday May 30; Friday 29 May close). **INDIA FELL ON A DAY OF UNAMBIGUOUS CRISIS RELIEF — THE CLEANEST "
        "NON-CONFIRMATION OF THE CYCLE; THE DRIVER WAS MECHANICAL, NOT THE WAR. Nifty 50 closed 23,547.75 (-1.5% 1D), a THIRD "
        "straight down session and the WORST MAY IN SIX YEARS (-2.8% calendar month); Sensex -1.4% to 74,775.7. On a day when every "
        "crisis variable moved India's way (Brent -22% MoM import-bill relief, rupee firming to ~Rs95.0, India 10Y easing to 7.00%, "
        "a ceasefire MOU progressing), the textbook relief leg should have lifted Nifty +1-2%. Instead it FELL. The driver was "
        "MECHANICAL + STRUCTURAL, ~0% crisis-linked: (1) MSCI Global Standard Index rebalance took effect at the 29 May close -> an "
        "estimated $800m-$1bn of foreign PASSIVE outflows (one-time, does not recur); (2) F&O monthly expiry volatility + "
        "profit-booking in oil&gas/metals/autos/financials (Bank Nifty -1.1%, financials led down; tech the lone strength); (3) "
        "structural FII rotation OUT of expensive India (~24x P/E vs ~22x 10-yr avg) INTO the Korea/Taiwan AI-memory supercycle. "
        "**India's weakness is now empirically proven STRUCTURAL + MECHANICAL, not crisis-linked: the brent->nifty relief leg is "
        "necessary but INSUFFICIENT.** For the investor: a Hormuz deal will NOT re-rate India — it removes a headwind India already "
        "wasn't trading on; the re-rating requires FII flows to turn, which requires winning capital back from the North-Asia AI "
        "trade (or that trade cracking). Key levels: held ~23,500 (relief-rally floor); a SIGNED deal could gap toward 24,500, a "
        "deal-break opens 23,000. NEW EDGE formalized: nifty-50 <-> semiconductors (capital_substitution), the mechanism that "
        "explains why the relief leg fails (markets E1).**"
    ),
    current={
        "price": "23,547.75 (Friday 29 May close)",
        "delta_1d": "-1.5% — 3rd straight down session; worst May in six years",
        "delta_1m": "-1.9% (calendar May -2.8%)",
        "delta_3m": "-5.3%",
        "driver": "MECHANICAL + STRUCTURAL, ~0% crisis (crisis was a TAILWIND on 29 May and India still fell): MSCI rebalance $800m-$1bn one-time passive outflow + F&O expiry + structural FII rotation into the Korea/Taiwan AI-memory supercycle. The relief leg (oil-down + rupee-up + deal-progress) is necessary but INSUFFICIENT.",
        "key_levels": "Held ~23,500 (relief-rally floor). A SIGNED deal could gap toward 24,500; a deal-break opens 23,000. Re-rating requires an FII turn, not a Hormuz deal."
    },
    edge_bumps=[
        {"to": "india"},
        {"to": "inr-usd"},
    ],
    new_edges=[
        {"to": "semiconductors", "type": "capital_substitution_em_portfolio_reallocation_india_to_korea_taiwan_ai_memory",
         "directness": 2, "activation_count": 3, "weight": 4.5},
    ],
))

PAYLOADS.append(dict(
    nid="india",
    summary_prepend=(
        "Day 92 (Saturday May 30; Friday 29 May close). **INDIA'S WEAKNESS IS NOW EMPIRICALLY STRUCTURAL + MECHANICAL, NOT "
        "CRISIS-LINKED — IT FELL ON A DAY OF CRISIS RELIEF. Nifty -1.5% (23,547.75), Sensex -1.4% (74,775.7), a 3rd straight down "
        "session and the worst May in six years — even as Brent fell -22% MoM, the rupee firmed to ~Rs95.0, India 10Y eased to "
        "7.00% and a ceasefire MOU progressed. The proximate cause was a MECHANICAL MSCI rebalance ($800m-$1bn passive outflow) + "
        "F&O expiry + structural FII rotation into the Korea/Taiwan AI-memory supercycle. The macro hardened: RBI forex reserves "
        "fell to $681.4bn (week ending 22 May, -$7.5bn w/w, ~$37bn off peak) on rupee-defence intervention; cumulative war-period "
        "outflows exceed $22bn (stocks+bonds), FY26 net FPI ~-$16.7bn. Rough rice +19.6% MoM signals India export-restriction / "
        "food-security pressure. **The investment read: a Hormuz deal removes a headwind India already wasn't trading on; the "
        "re-rating requires an FII turn (winning capital back from North-Asia AI), not a ceasefire.**"
    ),
    current={
        "price": "Nifty 23,547.75 / Sensex 74,775.74 (Friday 29 May close)",
        "delta_1d": "Nifty -1.5% / Sensex -1.4% — 3rd straight down session, worst May in six years",
        "delta_1m": "Nifty cal. May -2.8%; Sensex -2.7%",
        "rupee": "USD/INR ~Rs94.99 (firmer; -1.1% 1D), off the Rs96.96 record low of 20 May",
        "reserves": "RBI forex reserves $681.4bn (week ending 22 May, -$7.5bn w/w, ~$37bn off peak)",
        "read": "Weakness STRUCTURAL + MECHANICAL, not crisis: MSCI rebalance + F&O expiry + FII rotation to North-Asia AI. The brent->nifty relief leg is necessary but INSUFFICIENT; re-rating requires an FII turn, not a Hormuz deal."
    },
    edge_bumps=[
        {"to": "inr-usd"},
        {"to": "brent-crude"},
    ],
))

PAYLOADS.append(dict(
    nid="inr-usd",
    summary_prepend=(
        "Day 92 (Saturday May 30; Friday 29 May close). **RUPEE FIRMED TO ~Rs95.0 — THE FIRST OIL-RELIEF + DEAL-FIRMING TO HOLD "
        "INTO THE WEEKEND, BUT THE STRUCTURAL BEAR IS INTACT AND THE FIRMING IS PART-INTERVENTION. USD/INR ~Rs94.99 (-1.1% 1D, "
        "rupee firmer), off the Rs96.96 all-time low of 20 May — driven by Brent sub-$100 (import-bill/CAD relief) + the ceasefire "
        "MOU + a softer dollar (DXY 98.91, soft PCE). BUT: RBI forex reserves fell to $681.4bn (week ending 22 May, -$7.5bn w/w, "
        "~$37bn off peak) — the firming is still part-intervention; the RBI's $5bn buy-sell swap drew ~$9.8bn in bids (healthy bank "
        "appetite, not stress). FII outflows continue (FY26 net FPI ~-$16.7bn; war-period cumulative >$22bn). No new RBI "
        "macroprudential directive this window — the absence of fresh escalation is itself mildly reassuring. **The Rs93-94 ORGANIC "
        "retracement path is open only on a SIGNED deal + Brent <$95 sustained + an FII turn — and the FII turn is the missing "
        "piece. A deal-break + Brent re-spike toward $110+ reopens the Rs97-98 path despite intervention.**"
    ),
    current={
        "price": "Rs94.99 (Friday 29 May close)",
        "delta_1d": "-1.1% (rupee firmer)",
        "delta_1m": "+0.1%",
        "delta_3m": "+5.1%",
        "driver": "Brent sub-$100 + ceasefire MOU + softer dollar (DXY 98.91, soft PCE) firmed the rupee off the Rs96.96 record (20 May). Still part-intervention: RBI reserves $681.4bn (-$7.5bn w/w); $5bn swap drew ~$9.8bn bids.",
        "path": "Rs93-94 organic retracement open only on a SIGNED deal + Brent <$95 sustained + an FII turn (the missing piece). A deal-break + Brent >$110 reopens Rs97-98 despite intervention."
    },
    edge_bumps=[
        {"to": "brent-crude"},
        {"to": "rbi"},
    ],
))

PAYLOADS.append(dict(
    nid="rbi",
    summary_prepend=(
        "Day 92 (Saturday May 30; week ending 22 May data). **THE INTERVENTION COST IS MOUNTING — FOREX RESERVES FELL $7.5bn IN A "
        "WEEK TO $681.4bn (~$37bn OFF PEAK). The sharp weekly drawdown (RBI weekly statistical supplement, week ending 22 May) is "
        "the price of defending the rupee through the Rs96.96 record-low episode (20 May) and into the ~Rs95.0 firming. The RBI's "
        "$5bn dollar-rupee buy-sell swap drew ~$9.8bn in bids (healthy bank appetite, NOT stress). India 10Y G-Sec eased to ~7.00% "
        "on the ceasefire + lower Brent, capped by an upcoming debt auction + RBI policy. No NEW macroprudential directive this "
        "window — the toolkit ($5bn swap + ~$1bn/day spot sales + NDF controls + NOP cap) is unchanged; the ABSENCE of fresh "
        "escalation is mildly reassuring. The reserves drawdown is the constraint: continued intervention at this pace is not "
        "indefinitely sustainable, which is why an organic FII turn (not a Hormuz deal) is the real rupee-stabilizer.**"
    ),
    current={
        "forex_reserves": "$681.4bn (week ending 22 May; -$7.5bn w/w, ~$37bn off peak)",
        "india_10y": "~7.00% (eased on ceasefire + lower Brent; capped by upcoming auction + policy)",
        "swap": "$5bn dollar-rupee buy-sell swap drew ~$9.8bn bids (healthy bank appetite, not stress)",
        "directive": "No new macroprudential directive this window; toolkit unchanged ($5bn swap + ~$1bn/day spot + NDF controls + NOP cap)."
    },
    edge_bumps=[
        {"to": "inr-usd"},
    ],
))

PAYLOADS.append(dict(
    nid="fii-flows",
    summary_prepend=(
        "Day 92 (Saturday May 30; Friday 29 May close). **FII/PASSIVE FLOWS WERE THE TRANSMISSION MECHANISM IN EVERY INDIA CHAIN "
        "AGAIN — NOW WITH A NEW MECHANICAL LEG. The 29 May Nifty -1.5% drop on a crisis-RELIEF day was driven by (1) the MSCI "
        "Global Standard Index rebalance taking effect at the close -> an estimated $800m-$1bn of foreign PASSIVE outflows "
        "(Nuvama via wire; Hyundai India -$281m, Jubilant -$161m the steepest) — one-time, mechanical, calendar-driven, "
        "non-recurring; (2) discretionary FII selling; (3) structural rotation OUT of expensive India (~24x P/E) INTO the "
        "Korea/Taiwan AI-memory supercycle (India -9% YTD vs Korea +90% / Taiwan +42%; Goldman's paired call: India marketweight / "
        "Korea highest-conviction +300% EPS). Cumulative war-period outflows >$22bn (stocks+bonds); FY26 net FPI ~-$16.7bn. **This "
        "is the node that explains why India's relief leg fails: even with every crisis variable moving India's way, global capital "
        "reallocation to AI overwhelmed it.** The new nifty-50 <-> semiconductors capital-substitution edge formalizes the channel "
        "(markets E1).**"
    ),
    current={
        "fy26_fii_outflow": "~-$16.7bn (FY26 net FPI)",
        "ytd_cy26_fii_outflow": "war-period cumulative >$22bn (stocks+bonds since late Feb)",
        "capital_rotation": "OUT of expensive India (~24x P/E vs ~22x 10-yr avg) INTO the Korea/Taiwan AI-memory supercycle (India -9% YTD vs Korea +90% / Taiwan +42%); Goldman India marketweight / Korea highest-conviction +300% EPS.",
        "new_mechanical_leg": "MSCI Global Standard Index rebalance (29 May close) = $800m-$1bn one-time passive outflow (Hyundai India -$281m, Jubilant -$161m steepest); does not recur."
    },
    edge_bumps=[
        {"to": "nifty-50"},
        {"to": "semiconductors"},
    ],
))

PAYLOADS.append(dict(
    nid="semiconductors",
    summary_prepend=(
        "Day 92 (Saturday May 30; Friday 29 May close). **THE AI-MEMORY SUPERCYCLE, FULLY DECOUPLED FROM THE CRISIS — AND THE "
        "DESTINATION OF THE CAPITAL LEAVING INDIA. KOSPI +3.6% to a record 8,476 (+28.1% MoM, +46.3% 3M); Taiwan TAIEX +2.5% "
        "(+27.5% 3M); SMH +19.9% MoM / +47.4% 3M. SK Hynix jumped ~11% to join the $1 trillion club (after Samsung and Micron) on "
        "HBM/high-end AI-memory demand; Goldman calls Korea its 'highest-conviction' market (KOSPI target 9,000; 2026 EPS growth "
        "+300%), Taiwan +45% EPS. **Critical concentration risk: 82% of Korean listed stocks FELL over the past month — Samsung + "
        "SK Hynix alone = ~50% of the KOSPI by market cap; this is the narrowest possible breadth, the index is two stocks. The won "
        "is WEAKENING (USD/KRW Won1,507, +4.8% 3M) even as KOSPI rips — FX outflow alongside equity inflow.** This is a structural "
        "AI-capex trade, ~0% crisis — it would run with or without the war. The node's standing flag that 'KOSPI is the most "
        "reversible position in the world if the AI/helium thesis cracks' stands, but NO crack is visible. New edge: nifty-50 <-> "
        "semiconductors (capital_substitution) formalizes that this is where EM capital leaving India goes (markets E1/C3).**"
    ),
    current={
        "price": "SMH $598.93; KOSPI 8,476.15 (record); Taiwan TAIEX 44,732.94 (Friday 29 May close)",
        "delta_1d": "SMH -0.2%; KOSPI +3.6%; TAIEX +2.5%",
        "delta_1m": "SMH +19.9%; KOSPI +28.1%; TAIEX +13.8%",
        "delta_3m": "SMH +47.4%; KOSPI +46.3%; TAIEX +27.5%",
        "driver": "Global AI/HBM capex supercycle, ~0% crisis. SK Hynix joined the $1T club (~+11%). Goldman: Korea highest-conviction (KOSPI target 9,000, +300% 2026 EPS).",
        "concentration_risk": "82% of Korean listed stocks FELL over the past month; Samsung + SK Hynix = ~50% of KOSPI by market cap (the index is two stocks). Won weakening (USD/KRW Won1,507, +4.8% 3M) even as KOSPI rips. Most-reversible position if the AI/helium thesis cracks — no crack visible."
    },
    edge_bumps=[
        {"to": "india"},
        {"to": "helium"},
    ],
    new_edges=[
        {"to": "nifty-50", "type": "capital_substitution_em_reallocation_destination_north_asia_ai_memory_vs_india",
         "directness": 2, "activation_count": 3, "weight": 4.5},
    ],
))

PAYLOADS.append(dict(
    nid="kospi",
    summary_prepend=(
        "Day 92 (Saturday May 30; Friday 29 May close). **RECORD HIGH ON SK HYNIX'S $1T MILESTONE — BUT THE INDEX IS TWO STOCKS. "
        "KOSPI +3.6% to a record 8,476.15 (+28.1% MoM, +46.3% 3M); SK Hynix jumped ~11% to join the $1 trillion club, rising as "
        "much as 5% intraday and triggering a 'sidecar' algo-halt. Goldman raised its KOSPI target to 9,000 and calls Korea its "
        "'highest-conviction' market (+300% 2026 EPS growth). **Concentration is extreme: 82% of Korean listed stocks FELL over "
        "the past month; Samsung + SK Hynix alone are ~50% of the index by market cap — the narrowest possible breadth. The won is "
        "WEAKENING (USD/KRW Won1,507, +4.8% 3M) even as KOSPI rips — FX outflow alongside equity inflow.** This is the destination "
        "of capital leaving India (markets C3) — a structural AI-memory trade, ~0% crisis, reversible only on an idiosyncratic "
        "AI/memory-pricing crack, none visible.**"
    ),
    current={
        "price": "8,476.15 (record, Friday 29 May close)",
        "delta_1d": "+3.6%",
        "delta_1m": "+28.1%",
        "delta_3m": "+46.3%",
        "driver": "SK Hynix joined the $1T club (~+11%, intraday +5% triggered a sidecar halt); HBM/AI-memory supercycle. Goldman target 9,000, Korea 'highest-conviction.'",
        "concentration_risk": "82% of Korean listed stocks fell over the past month; Samsung + SK Hynix = ~50% of the index. Won weakening (Won1,507, +4.8% 3M) even as KOSPI rips."
    },
    snapshot={
        "date": "2026-05-29",
        "price": "8,476.15 (+3.6%, record)",
        "trigger": "SK Hynix joined the $1 trillion club (~+11%), intraday +5% triggered a sidecar algo-halt; HBM/AI-memory supercycle + Goldman 'highest-conviction' / target 9,000.",
        "delta_context": "+46.3% 3M but the narrowest breadth (82% of stocks fell MoM; 2 stocks = ~50% of the index). Won weakening (Won1,507, +4.8% 3M). The destination of capital leaving India; reversible only on an AI/memory crack."
    },
    edge_bumps=[
        {"to": "semiconductors"},
    ],
))

PAYLOADS.append(dict(
    nid="taiwan",
    summary_prepend=(
        "Day 92 (Saturday May 30; Friday 29 May close). **TAIEX +2.5% TO 44,732.94 (+27.5% 3M) — THE AI/SEMIS BID, TECH >80% OF "
        "THE INDEX. Taiwan tracked the same AI-memory supercycle lifting KOSPI to a record; Goldman sees Taiwan +45% EPS. Like "
        "Korea, this is a structural AI-capex trade (~0% crisis) and a destination of EM capital rotating out of expensive India "
        "(markets C2/C3). No crisis linkage; reversibility is idiosyncratic to AI/semis pricing, not the Iran ceasefire.**"
    ),
    current={
        "price": "44,732.94 (Friday 29 May close)",
        "delta_1d": "+2.5%",
        "delta_1m": "+13.8%",
        "delta_3m": "+27.5%",
        "driver": "AI/semis supercycle (tech >80% of the index); Goldman Taiwan +45% EPS. ~0% crisis; a destination of capital leaving India."
    },
    edge_bumps=[
        {"to": "semiconductors"},
    ],
))

PAYLOADS.append(dict(
    nid="us-10y-yield",
    summary_prepend=(
        "Day 92 (Saturday May 30; Friday 29 May close). **10Y AT 4.45%, CAPPED BY A SOFTER MONTHLY PCE — FED CUTS PRICED OUT. The "
        "US 10Y held 4.45% (+0.8% MoM, +10.0% 3M); the 2Y at 3.59%. April PCE (released 28 May) printed headline 3.8% YoY (a "
        "3-year high) but monthly +0.4% vs +0.5% expected — a softer-than-feared monthly read that capped yields and dialed back "
        "the rate-HIKE bets that had been pressuring gold. Fed cuts remain fully priced OUT (the PPI/Warsh inflation regime, "
        "structural through Q3) — this does NOT reverse on a Hormuz deal. The softer monthly print, not the war, drove the gold "
        "rebound and the fresh US equity records.**"
    ),
    current={
        "price": "4.45% (10Y); 3.59% (2Y) — Friday 29 May close",
        "delta_1d": "~flat",
        "delta_1m": "+0.8%",
        "delta_3m": "+10.0%",
        "driver": "Soft April monthly PCE (+0.4% vs +0.5% exp) capped the 10Y; Fed cuts fully priced out (PPI/Warsh inflation regime, structural through Q3). Does not reverse on a Hormuz deal."
    },
    edge_bumps=[
        {"to": "fed"},
    ],
))

PAYLOADS.append(dict(
    nid="fed",
    summary_prepend=(
        "Day 92 (Saturday May 30). **SOFTER APRIL MONTHLY PCE, BUT CUTS STILL PRICED OUT — THE INFLATION REGIME IS STRUCTURAL "
        "THROUGH Q3. April PCE (28 May) printed headline 3.8% YoY (a 3-year high) with core 3.3% in-line, but the monthly +0.4% "
        "came in BELOW the +0.5% expected — a softer-than-feared monthly read that drove the gold rebound and fresh equity records "
        "(not the war). Fed rate cuts remain fully priced out; this is the PPI/Warsh inflation regime, structural through Q3, and "
        "does NOT reverse on a Hormuz deal. The crisis is being priced as an inflation/oil event, which keeps the Fed on hold and "
        "real yields competitive with gold.**"
    ),
    signal=s(
        "**SOFTER APRIL MONTHLY PCE (+0.4% vs +0.5% EXP) DROVE THE GOLD REBOUND AND EQUITY RECORDS — BUT CUTS STILL PRICED OUT.** "
        "April PCE headline 3.8% YoY (3-yr high), core 3.3% in-line, monthly +0.4% below the +0.5% expected. The softer monthly "
        "read dialed back rate-HIKE bets (lifting gold) and lifted equities; Fed cuts remain fully priced out (PPI/Warsh inflation "
        "regime, structural through Q3). Does not reverse on a Hormuz deal.",
        ["TheStreet 28 May (S&P/Nasdaq records despite highest PCE in ~3yr); markets dossier D1, C4",
         "Intel/Market dossier 2026-05-30 (April PCE released 28 May)"],
        "April PCE 3.8% YoY headline / 3.3% core / +0.4% monthly (vs +0.5% exp) = CONFIRMED (data); cuts priced out = market-implied; "
        "structural-through-Q3 regime = analyst assessment. No weight elevation beyond the data linkage."
    ),
    edge_bumps=[
        {"to": "gold"},
    ],
))

PAYLOADS.append(dict(
    nid="vix",
    summary_prepend=(
        "Day 92 (Saturday May 30; Friday 29 May close). **VIX SANK TO A 15.3 CYCLE LOW — PRICING THE CEASEFIRE AS DONE ON AN "
        "UNSIGNED DEAL + A LEBANON RED-LINE CROSSING. VIX 15.32 (-2.7% 1D, -28.5% 3M) is the cheapest convexity in the dataset: "
        "(a) Trump has NOT signed and the two sides describe the text incompatibly (Trump: HEU 'will be destroyed'; Fars: no "
        "destruction clause, $12bn-first), and (b) Israel CROSSED Washington's Beirut red line — the explicit binding constraint "
        "on the deal. If the next Situation Room produces a rejection, or Lebanon breaks the talks, VIX gaps to the low-20s and the "
        "S&P snaps -3-5% in a session. The complacency split persists: broad-index vol prices de-escalation while defense (ITA "
        "+10.5% MoM) bids the discrete kinetic events — both can't be right for long.**"
    ),
    current={
        "price": "15.32 (Friday 29 May close)",
        "delta_1d": "-2.7%",
        "delta_1m": "-9.3%",
        "delta_3m": "-28.5% — cycle low",
        "read": "Prices the ceasefire as DONE despite an UNSIGNED deal (Trump-vs-Fars contradiction) + a Lebanon red-line crossing. Cheapest convexity in the dataset: a Situation Room rejection or a Lebanon break of the talks gaps VIX to the low-20s, S&P -3-5% in a session. Complacency split: index vol prices de-escalation while defense (ITA +10.5% MoM) bids kinetic events."
    },
    edge_bumps=[
        {"to": "sp-500"},
    ],
))

PAYLOADS.append(dict(
    nid="sp-500",
    summary_prepend=(
        "Day 92 (Saturday May 30; Friday 29 May close). **FRESH RECORD ON THE SOFTER PCE + PEACE-DIVIDEND TAPE — BUT VIX 15.3 ON AN "
        "UNSIGNED DEAL IS THE COMPLACENCY TELL. S&P 500 7,580.06 (+0.2% 1D, +6.2% MoM, +10.1% 3M), with NASDAQ (26,972.62) and Dow "
        "(51,032.46) also at fresh records, led by the AI/semis bid (SMH +19.9% MoM) and a softer April monthly PCE (+0.4% vs +0.5% "
        "exp). The risk: VIX at a 15.3 cycle low prices the ceasefire as DONE while the 60-day MOU is UNSIGNED (Trump-vs-Fars "
        "contradiction) and Israel crossed Washington's Beirut red line. If the Situation Room rejects or Lebanon breaks the talks, "
        "the S&P snaps -3-5% in a session from record highs — the cheapest convexity in the dataset.**"
    ),
    current={
        "price": "7,580.06 (record); NASDAQ 26,972.62 (record); Dow 51,032.46 (record) — Friday 29 May close",
        "delta_1d": "+0.2%",
        "delta_1m": "+6.2%",
        "delta_3m": "+10.1%",
        "driver": "AI/semis bid (SMH +19.9% MoM) + softer April monthly PCE + peace-dividend de-pricing. Risk: VIX 15.3 cycle low prices the ceasefire as done on an UNSIGNED deal + a Lebanon red-line crossing — a rejection or Lebanon break snaps the S&P -3-5%."
    },
    edge_bumps=[
        {"to": "vix"},
    ],
))

PAYLOADS.append(dict(
    nid="fertilizer-urea",
    summary_prepend=(
        "Day 92 (Saturday May 30; Friday 29 May data). **THE FERTILIZER WAR-PREMIUM IS CRACKING — UREA -35% MoM; THE 'PHYSICAL "
        "STACK NOT UNWINDING' THESIS IS NO LONGER UNIFORMLY TRUE. Urea fell to ~$410-443/t (Argus Mid-East granular high-$410s; "
        "TradingEconomics generic -35% MoM), and the nitrogen complex de-priced the Qatar-disruption premium hard: CF Industries "
        "-11% MoM (-3.6% 1D), Nutrien -7.5% MoM. The chain: deal-anticipation + Modi's fertilizer-cut/import-restraint appeal -> "
        "Gulf urea export-normalization expectation -> the fertilizer premium unwinds. **But the bifurcation is now WITHIN the "
        "physical complex, not just paper-vs-physical: the FAST legs (fertilizer, oil, LNG equity) de-price first; the SLOW legs "
        "(war-risk insurance ~8x, VLCC volumes -36%) lag 6-12 weeks even on a clean deal and have NOT unwound.** Whether shipping/"
        "insurance follow is the key tell for the next dossier.**"
    ),
    current={
        "price": "Urea ~$410-443/t (Argus Mid-East granular high-$410s; TradingEconomics generic)",
        "delta_1m": "-35% MoM — the war-premium cracking on deal-anticipation + Modi import-restraint",
        "complex": "CF Industries $112.35 (-3.6% 1D, -11% MoM); Nutrien $68.55 (-1.6% 1D, -7.5% MoM) — nitrogen complex de-pricing the Qatar premium.",
        "bifurcation": "Now WITHIN the physical complex: fast legs (fertilizer/oil/LNG equity) de-priced; slow legs (insurance ~8x, VLCC -36%) lag 6-12 weeks and have NOT unwound."
    },
    edge_bumps=[
        {"to": "qatar"},
        {"to": "natural-gas-lng"},
    ],
))

PAYLOADS.append(dict(
    nid="natural-gas-lng",
    summary_prepend=(
        "Day 92 (Saturday May 30; Friday 29 May close). **TWO DIVERGENT STORIES: THE QATAR-DISRUPTION LNG PREMIUM IS CRACKING "
        "(CHENIERE -17% MoM) WHILE US HENRY HUB RIPS +24% MoM ON NON-CRISIS DOMESTIC SUPPLY/DEMAND. Cheniere -17.2% MoM (-2.1% 1D) "
        "as deal-anticipation de-prices the Hormuz/LNG tail; European TTF gas eased to EUR45.96/MWh (-2.2% 1D) but holds a ~+30% YoY "
        "floor (Qatar Ras Laffan ~17% force majeure persists). Separately and NON-crisis: US Henry Hub +24.3% MoM to $3.29 on "
        "storage injections below forecast (92 bcf vs 95-96 exp) + an LNG-export ramp (Golden Pass Train 1, Corpus Christi Stage 3 "
        "Train 5) + easing production — a domestic supply/demand story, NOT the war. The Qatar-premium crack is on the FAST legs "
        "(equity, TTF); the SLOW legs (insurance/freight) and helium remain elevated/unverified.**"
    ),
    current={
        "price": "Henry Hub $3.29 (+0.2% 1D, +24.3% MoM — NON-crisis); European TTF EUR45.96/MWh (-2.2% 1D, ~+30% YoY floor); Cheniere $224.86 (-2.1% 1D, -17.2% MoM)",
        "henry_hub_driver": "+24% MoM is NON-crisis: storage injections below forecast (92 bcf vs 95-96 exp) + LNG-export ramp (Golden Pass Train 1, Corpus Christi Stage 3 Train 5) + easing production.",
        "lng_premium": "Cheniere -17% MoM = Hormuz/LNG tail-risk de-pricing on deal-anticipation. TTF eased but holds ~+30% YoY (Ras Laffan ~17% force majeure persists)."
    },
    edge_bumps=[
        {"to": "qatar"},
    ],
))

PAYLOADS.append(dict(
    nid="cheniere-energy",
    summary_prepend=(
        "Day 92 (Saturday May 30; Friday 29 May close). **CHENIERE -17% MoM — THE HORMUZ/LNG TAIL UNWINDS HARD ON DEAL-"
        "ANTICIPATION. LNG $224.86 (-2.1% 1D, -17.2% MoM, -9.5% 3M) as the market de-prices the Qatar-disruption / Hormuz-LNG tail "
        "premium that had bid the name through the crisis. This is the LNG leg of the same fast-physical de-pricing cracking "
        "fertilizer (urea -35% MoM, CF -11% MoM). Reversible on a deal collapse / Hormuz re-escalation; the slow legs (insurance, "
        "freight) have not unwound.**"
    ),
    current={
        "price": "$224.86 (Friday 29 May close)",
        "delta_1d": "-2.1%",
        "delta_1m": "-17.2%",
        "delta_3m": "-9.5%",
        "driver": "Hormuz/LNG tail-risk de-pricing on deal-anticipation — the LNG leg of the fast-physical premium unwind (alongside fertilizer)."
    },
    edge_bumps=[
        {"to": "natural-gas-lng"},
    ],
))

PAYLOADS.append(dict(
    nid="cf-industries",
    summary_prepend=(
        "Day 92 (Saturday May 30; Friday 29 May close). **CF -11% MoM AS THE FERTILIZER WAR-PREMIUM CRACKS (UREA -35% MoM). CF "
        "Industries $112.35 (-3.6% 1D, -11.0% MoM, +8.2% 3M) and Nutrien (-7.5% MoM) de-priced the Qatar-disruption nitrogen "
        "premium hard on deal-anticipation + Modi's fertilizer-cut/import-restraint appeal -> Gulf urea export-normalization "
        "expectation. This node had gone stale (last updated 13 May); the -11% MoM unwind is now encoded. Reversible on a deal "
        "collapse / Gulf re-disruption; the slow physical legs (insurance, freight) have not unwound.**"
    ),
    current={
        "price": "$112.35 (Friday 29 May close)",
        "delta_1d": "-3.6%",
        "delta_1m": "-11.0%",
        "delta_3m": "+8.2%",
        "driver": "Fertilizer war-premium unwind: urea -35% MoM + Modi fertilizer-cut/import-restraint appeal -> Gulf export-normalization expectation. Nutrien -7.5% MoM alongside."
    },
    edge_bumps=[
        {"to": "fertilizer-urea", "create": True, "directness": 1,
         "new_type": "fertilizer_premium_unwind_urea_minus35_mom_cf_minus11_mom"},
    ],
))

PAYLOADS.append(dict(
    nid="aluminum",
    summary_prepend=(
        "Day 92 (Saturday May 30; Friday 29 May close). **ALUMINUM +13% MoM / +26% 3M — A DUAL AI/GRID-DEMAND + RESIDUAL GULF-"
        "PREMIUM BID, MOSTLY NON-CRISIS. LME aluminum $3,917.75/mt (+0.2% 1D, +13.0% MoM, +26.0% 3M). The move is ~75% structural "
        "(AI/grid power demand, the same capex story lifting copper +8.2% MoM) and ~25% a residual EGA/Gulf supply premium that has "
        "NOT fully unwound even as oil de-prices. Unlike the fertilizer/LNG fast legs, aluminum's premium is demand-led, so it is "
        "not unwinding on deal-anticipation.**"
    ),
    current={
        "price": "$3,917.75/mt (Friday 29 May close)",
        "delta_1d": "+0.2%",
        "delta_1m": "+13.0%",
        "delta_3m": "+26.0%",
        "driver": "~75% AI/grid demand (structural, same as copper +8.2% MoM) + ~25% residual EGA/Gulf supply premium. Demand-led, not unwinding on deal-anticipation."
    },
    edge_bumps=[
        {"to": "uae"},
    ],
))

PAYLOADS.append(dict(
    nid="defense-sector",
    summary_prepend=(
        "Day 92 (Saturday May 30; Friday 29 May close). **DEFENSE BID THE DISCRETE KINETIC EVENTS (ITA +10.5% MoM) EVEN AS THE "
        "BROAD TAPE PRICED PEACE — THE COMPLACENCY SPLIT. ITA (defense & aero) $235.44 (-0.1% 1D, +10.5% MoM, but still -6.0% 3M, "
        "de-rated by the peace-track). The monthly bid tracks the discrete kinetic events of May — the 28 May US-Iran missile "
        "exchange, the Lebanon/Beirut escalation — while VIX sank to a 15.3 cycle low pricing the ceasefire as done. Defense is "
        "voting that the kinetic risk is real while broad-index vol prices de-escalation; both can't be right for long. Lockheed "
        "(+4.0% MoM but -21.6% 3M) remains deeply de-rated from the peace-track.**"
    ),
    current={
        "price": "ITA $235.44; Lockheed $530.45 (Friday 29 May close)",
        "delta_1d": "ITA -0.1%; LMT -1.3%",
        "delta_1m": "ITA +10.5%; LMT +4.0%",
        "delta_3m": "ITA -6.0%; LMT -21.6% — deeply de-rated by the peace-track",
        "read": "Monthly kinetic-event bid (28 May missile exchange, Lebanon/Beirut escalation) vs VIX 15.3 cycle low — the complacency split. Defense prices kinetic risk as real while index vol prices de-escalation."
    },
    edge_bumps=[
        {"to": "vix", "create": True, "directness": 2,
         "new_type": "complacency_split_defense_bids_kinetic_events_while_index_vol_prices_peace"},
    ],
))

PAYLOADS.append(dict(
    nid="helium",
    summary_prepend=(
        "Day 92 (Saturday May 30). **NO FRESH HELIUM PRINT THIS WINDOW — THE READ IS CARRIED, AND THE SEMICONDUCTOR TAPE SHOWS NO "
        "ACUTE-SHORTAGE PRICING. No new gasworld/industry helium price was retrieved; the carried read is ~25-30% of global supply "
        "(Qatar) disrupted. Crucially, the semiconductor complex is pricing THROUGH any helium constraint, not into a crisis: SMH "
        "+47.4% 3M, KOSPI +46% 3M, SK Hynix joining the $1T club, Korean fabs running the AI-memory supercycle at full tilt — there "
        "is NO visible supply-crisis pricing in the chips that would consume the helium. This is consistent with helium NOT being "
        "an acute binding constraint right now (the cascade path war -> Qatar -> helium -> semis is latent, not firing). HONEST "
        "FLAG: the helium price itself is unverified this window — do not state the shortage has eased OR worsened; only that the "
        "downstream (semis) shows no acute-shortage signal.**"
    ),
    signal=s(
        "**NO FRESH HELIUM PRINT (CARRIED); SEMICONDUCTOR TAPE SHOWS NO ACUTE-SHORTAGE PRICING.** No new helium price retrieved; "
        "carried read ~25-30% of global supply (Qatar) disrupted. The downstream is pricing through, not into a crisis: SMH +47% "
        "3M, KOSPI +46% 3M, SK Hynix joined the $1T club — Korean fabs running the AI-memory supercycle at full tilt with no "
        "visible supply-crisis pricing. Consistent with helium NOT being an acute binding constraint right now; the war->Qatar->"
        "helium->semis cascade is latent, not firing. Helium price itself unverified this window.",
        ["Market dossier Section F (helium — no fresh print, carried)",
         "Market dossier C3 (SMH +47% 3M, KOSPI +46% 3M, SK Hynix $1T — semis pricing through)",
         "Intel/Market dossier 2026-05-30"],
        "Helium price = carried/UNVERIFIED this window (no fresh print); semis pricing-through = CONFIRMED (data, SMH/KOSPI). Do "
        "NOT state the shortage eased or worsened — only the downstream shows no acute-shortage signal."
    ),
    edge_bumps=[
        {"to": "semiconductors"},
    ],
))

# ===========================================================================
# NEW NODE — OMAN (created separately in the runner via create_oman.py)
# ===========================================================================
