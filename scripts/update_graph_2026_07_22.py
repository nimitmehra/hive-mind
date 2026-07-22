#!/usr/bin/env python3
"""Graph update for the 2026-07-22 evening brief.
Backup: backups/2026-07-22/graph_v1
Sources: staging/2026-07-22-evening/{intel,markets}.md
Run ONCE and capture output to a file — do NOT pipe to grep (that re-executes and duplicates).
"""
import json, os

D = "2026-07-22"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NODES = os.path.join(ROOT, "graph", "nodes")
log = []


def _load(nid):
    p = os.path.join(NODES, nid + ".json")
    if not os.path.exists(p):
        log.append(("MISSING", nid)); return None, None
    return json.load(open(p)), p


def _save(d, p):
    json.dump(d, open(p, "w"), indent=1, ensure_ascii=False)


def sig(nid, headline):
    d, p = _load(nid)
    if d is None: return
    d.setdefault("recent_signals", []).append({"date": D, "headline": headline})
    d["last_updated"] = D; _save(d, p); log.append(("SIG", nid))


def current(nid, **kw):
    d, p = _load(nid)
    if d is None: return
    d.setdefault("current", {}).update(kw); d["last_updated"] = D
    _save(d, p); log.append(("CUR", nid))


def snapshot(nid, price, trigger):
    d, p = _load(nid)
    if d is None: return
    d.setdefault("price_snapshots", []).append({"date": D, "price": price, "trigger": trigger})
    d["last_updated"] = D; _save(d, p); log.append(("SNAP", nid))


def trig_set(nid, match, status, note):
    d, p = _load(nid)
    if d is None: return
    hits = [t for t in d.get("active_triggers", []) if match.lower() in str(t.get("condition", "")).lower()]
    if len(hits) != 1:
        log.append(("TRIG-AMBIG", nid, match, len(hits))); return
    hits[0]["status"] = status; hits[0]["status_changed"] = D; hits[0]["notes"] = note
    d["last_updated"] = D; _save(d, p); log.append(("TRIG", nid, status))


def trig_add(nid, condition, status, cascade, note):
    d, p = _load(nid)
    if d is None: return
    if any(str(t.get("condition","")).lower()[:55] == condition.lower()[:55] for t in d.get("active_triggers", [])):
        log.append(("TRIG-DUP", nid)); return
    d.setdefault("active_triggers", []).append(
        {"condition": condition, "status": status, "cascade": cascade, "added": D, "notes": note})
    d["last_updated"] = D; _save(d, p); log.append(("TRIG-NEW", nid))


# ============================== GEOPOLITICAL ==============================

sig("united-states",
    "**Strike night 11 hit Bushehr province + Ilam — the nearest US ordnance has come to a live safeguarded reactor. The tripwire HELD.** Reuters (22 Jul 00:57 GMT): the US completed its 11th successive night of strikes; CENTCOM confirmed. Targets: three sites in Bushehr province plus Ilam. NO strike on Fordow, Natanz, Esfahan or Pickaxe Mountain. Bushehr province hosts Iran's OPERATIONAL, IAEA-safeguarded Bushehr Nuclear Power Plant; the struck sites read as military targets and are NOT confirmed to be the reactor, but this is the closest approach yet — air defences were 'activated near Bushehr nuclear plant' (20 Jul) and an Iranian official alleged 'an airstrike near Bushehr' (US unacknowledged). No IAEA statement yet. Haaretz's analytical framing adds a second escalation vector: 'As Ground Invasion Looms, U.S. and Iran Want Wild-card Israel Out of the Fight.' Night 12 not yet announced. **CENTCOM's framing remains the shipping-protection rationale, not 'swiftly punish.'** CONFIRMED.")

sig("united-states",
    "**Trump has still NOT chosen between the 10-day ceasefire and the joint US-Israeli campaign — and his rhetoric hardened toward escalation.** He said 'We're not done in Iran,' 'not finished at all,' and renewed the threat to hit the underground nuclear site 'probably pretty soon' (Hindustan Times, Times of Israel, 21-22 Jul); Axios frames him 'approaching a decisive point' / 'eyes all-out war.' **This escalation tilt is what re-armed oil to a war-restart high (Brent $93.84) — the single most consequential open binary in the brief.** Decision still 'within days.' The COUNTER-voice is Rubio, not Trump: 'US still willing to negotiate,' 'open to talks but Tehran not serious,' 'there will be consequences,' the Hormuz toll a 'dangerous precedent' — a door held open with blame pre-assigned to Tehran. The Rubio-vs-Trump gap is the live Pentagon-vs-White-House split. CONFIRMED (decision not made).")

sig("united-states",
    "**US deaths hold at 17; the House defence-bill floor vote had NOT happened; Hegseth put the war's cost at $37.5bn.** No new US deaths in-window; the Al-Azraq MIA is NOT resolved (no update, no Iranian POW claim). The House cleared a PROCEDURAL hurdle on the $1.1 trillion defence bill (21 Jul) and passed a personal-guns-on-bases measure and a Continuing Appropriations Act 2027 overnight — but the final defence-appropriations/war-funding floor vote and any war-powers vote had NOT occurred as of ~14:12 IST. The money fight is JAMMED, not resolved. The dominant Hill story is **Hegseth's Senate testimony: the Iran war has cost $37.5 billion so far**, as he asked for more supplemental funds at a 'fiery hearing.' (FT's earlier '$95bn/$60bn munitions' package could not be re-confirmed this cycle.) CONFIRMED.")

sig("nuclear-program",
    "**THE TRIPWIRE HELD FOR A THIRD CONSECUTIVE WINDOW — Fordow, Natanz, Esfahan and Pickaxe Mountain all UNTOUCHED — but strike night 11 hit BUSHEHR PROVINCE, the nearest US ordnance has come to a live safeguarded reactor.** The three struck sites read as military targets in the province and are NOT confirmed to be the operational Bushehr Nuclear Power Plant, but the proximity is the new escalation caveat; no IAEA statement yet. Trump renewed the threat to hit the underground enrichment site 'probably pretty soon' — RHETORIC, not action. The Pickaxe centrifuge-relocation claim remains an ISRAELI ASSESSMENT (WSJ), with construction/concealment confirmed by imagery. Iran's posture is UNCHANGED and remains the strongest non-weaponization indicator: it took the Darkhovin strike to the UNSC invoking IAEA safeguards in its own favour, has made NO NPT withdrawal threat and NO enrichment escalation. CONFIRMED (the absences) / RHETORIC (Trump's threat).")

sig("iran",
    "**Diplomacy stalled to contact-without-process, and the ceasefire's AUTHORSHIP is now disputed.** Iran has neither formally accepted nor rejected the 10-day proposal. Two new complications: (1) **Iraqi PM al-Zaidi offered to host US-Iran talks and carry a US message — and Trump reportedly DECLINED** (Al-Hurra); either way, no meeting, venue or named negotiator exists. (2) **The Jerusalem Post reports Iran SECRETLY SUBMITTED the 10-day proposal itself while under strikes** — which INVERTS the baseline that Qatar/Pakistan conveyed it TO Tehran. Treat authorship as UNRESOLVED (single-source). Mediators still 'racing to salvage' it. **No on-record Baghaei/Araghchi statement surfaced — and Iranian STATE MEDIA IS HIDING THE PROPOSAL** (see tone). Day 10+ since the 11 July Muscat trip with no round of talks. CONFIRMED (no process) / REPORTED (authorship inversion).")

sig("iran",
    "**The rial did NOT break 2,000,000 — soft, sideways, ~1,915,000 (22 Jul, alanchand)**, up from 1,903,500 the prior day (+0.6%), still below the 19 July peak of 1,953,500 and 5.8% from the threshold. **The 3% reversal-off-peak has STALLED and the rial is weakening again slightly** — direction sideways-to-soft, no capitulation. The stall coincides precisely with the ceasefire stalling and Trump's escalation rhetoric, reinforcing the rial's role as the cleanest high-frequency proxy for the market's diplomacy read. Inflation 88.6% (no new print). Single-source caveat: alanchand only (bonbast USD renders client-side). CONFIRMED.")

sig("iran",
    "**Iran claims a fresh wave — 'Operation Nasr-2' — on US bases in Kuwait, Bahrain and Jordan (~19-21 Jul), including disabling Kuwaiti radar, hitting 'the digital eye of CENTCOM,' and (again) 'Amazon data infrastructure in Bahrain.'** CLAIMED (IRGC/IranWire/Anadolu/Press TV) — **NO confirmation from CENTCOM, Bahrain, Kuwait or Jordan**, and consistent with the established pattern of Iranian damage claims being denied or ignored by host nations (the Aqaba/Al-Azraq contradictions of the prior window). Treat as rhetoric/unverified. Crucially, Gulf states acknowledged incoming attacks, responded defensively only, and did NOT restrict US operations. CLAIMED.")

sig("strait-of-hormuz",
    "**A FOURTH ship was struck (21 Jul), and the IRGC shifted from deniable 'accidents' to CLAIMING it 'stopped two oil tankers.'** After the 20 July three-ship cluster (Kavomaleas, Acheloos, Kaifan), a fresh strike hit a tanker off UAE/Oman on 21 July — crew abandoned ship (Seatrade, SAMAA, Reuters logged the projectile strike). No casualties in-window; attacker attribution not independently confirmed (REPORTED). **The framing shift is the intelligence: the IRGC now CLAIMS it 'stopped two oil tankers in Hormuz' — moving from 'accidents on an unsafe route' toward OWNING the interdictions.** Iran is converting a plausibly-deniable campaign into an asserted enforcement regime. No newer transit count than the ~4/day (20 Jul) / 12/day 5-day-average baseline surfaced. CONFIRMED (strike) / CLAIMED (IRGC ownership).")

sig("marine-war-risk-insurance",
    "**THE 21 JULY CORRECTION HELD ANOTHER CYCLE — Hormuz reopening is gated by CREW AND OWNER APPETITE, not underwriting capacity.** No war-risk premium print newer than the 9 July Marsh figure of 2-6% of vessel value has been published despite three-to-four ships struck since; all signals are qualitative ('surge again,' 'braces for prolonged elevated premiums'). NO new JWC listing change. NO ITF/IBF Warlike-Operations-Area declaration (STILL OVERDUE). The load-bearing datum remains labour: **Sinokor's six-months'-salary offer for one ~30-day Hormuz round trip was reconfirmed 21 July** and The National ran it as 'Danger money.' The market clears on seafarer refusal, not cover withdrawal — which is why transits collapsed to a trickle even though cover is available and priced. CONFIRMED (the absence of any print above 2-6%).")

sig("shipping-tankers",
    "A fourth tanker struck 21 Jul off UAE/Oman (crew abandoned; REPORTED). Tanker equities finally caught the war-risk bid — Frontline +4.1%, BOAT +2.0% (22 Jul) — on the day the Houthi Saudi-crude embargo turned three tankers back and TTF hit a new high, though the move is pricing a SECOND-chokepoint premium on a declaration, not a closure. The crew-supply constraint is reconfirmed (Sinokor six-months'-salary offer). No newer Hormuz transit count than ~4/day (20 Jul). CONFIRMED (equity) / REPORTED (4th strike).")

sig("houthis",
    "**THE FRONT CRACKED TO 'DECLARATION WITH EFFECT' — but NO kinetic strike (Day ~15).** The Saudi-shipping embargo (declared 20 Jul) is enforced by WARNING EMAIL AND RADIO ONLY — 'Houthis warn shipping companies to avoid Saudi ports, email shows' (Reuters). **Effect is real but non-kinetic: THREE tankers carrying Saudi crude made U-turns in the Red Sea, AIS-confirmed** (Reuters, WaPo). NO confirmed missile/drone hit on any ship — checked specifically. **Bab el-Mandeb is NOT closed**, and the 16 July Reuters 'close the strait if the US hits Iranian power' order STILL has not fired its predicted kinetic response (~15 days). Counter-signal: a sanctioned Iranian rocket-fuel vessel entered the Red Sea FREELY post-blockade (TradeWinds) — Iranian shipping transits while Saudi cargo turns back, i.e. the embargo is TARGETED COERCION of Riyadh, not a general closure. Saudi Arabia rejected the blockade and 'vows to protect shipping'; Trump threatened to strike the Houthis; Saudi loadings -36%. CONFIRMED (declaration + AIS turn-backs) / RHETORIC (no kinetic).")

sig("saudi-arabia",
    "**Saudi Arabia rejected the Houthi maritime embargo and 'vows to protect shipping' — but has taken no offensive military action.** The embargo turned three Saudi-crude tankers back in the Red Sea (AIS-confirmed) and Saudi loadings are -36% on the threat; the Saudi Crown Prince also telephoned Aoun to voice support for Lebanon. Riyadh is escalating rhetorically and holding operationally — no strikes reported. The commercial stakes are unchanged and precise: the East-West Petroline to Yanbu is the Hormuz workaround the Houthi declaration targets. MEE's 'Saudi mulling military escalation' from the prior window has NOT converted to action. CONFIRMED (rhetoric) / no offensive action.")

sig("red-sea",
    "The Houthi Saudi-crude embargo produced its first measurable effect — three tankers U-turned (AIS) — but Bab el-Mandeb is OPEN and no vessel has been struck. A sanctioned Iranian rocket-fuel vessel transited the Red Sea freely, underlining that this is targeted coercion of Saudi cargo, not a closure. Tanker equities (Frontline +4.1%) and TTF (+2.8% to a new high) priced a second-chokepoint premium on the declaration. Suez traffic/revenue could not be refreshed this cycle. CONFIRMED (turn-backs) / RHETORIC (closure).")

sig("lebanon",
    "**The Aoun-Trump meeting produced pledges and one flight route — no dated deliverable.** Trump 'vows to help Lebanon but offers no timeline for Israeli withdrawal' (Al Jazeera). Aoun presented a WRITTEN Hezbollah-disarmament plan but conditioned it on Israeli withdrawal first — no published text, no deadline. The single tangible outcome: **Trump authorised resumption of direct US-Lebanon commercial flights (first since ~1985)** — symbolic. Trump offered to 'speak with Hezbollah if asked' and pledged LAF support (no dollar figure). No joint statement. Separately, the LAF DEPLOYED into a pilot zone after a (partial) Israeli withdrawal WITH VILLAGERS RETURNING (BBC, Al Jazeera) — extending the 21 Jul first-withdrawal finding, though the caveat stands (part of one village, packaged as three) and FDD frames the pilot zones as designed to pit Beirut against Hezbollah. A de-escalatory diplomatic event dressed as a settlement, with the disarm-vs-withdraw sequencing unresolved. CONFIRMED.")

sig("hezbollah",
    "**~Day 15 of complete silence toward Israel** — no rocket, missile or drone found across Israeli, Lebanese and pan-Arab sources. The silence has now survived the first US combat deaths, the Darkhovin strike, eleven nights of US bombing, and the start of an Israeli withdrawal Hezbollah publicly rejects. The LAF deployed into a pilot zone as villagers returned — the firewall is holding-to-strengthening, but via a CONFRONTATIONAL mechanism (FDD: the pilot zones are designed to force the Beirut-vs-Hezbollah disarmament confrontation), and Israeli demolitions/artillery inside Lebanon continue. No new Naim Qassem statement. CONFIRMED (negative).")

sig("israel",
    "**Israel STILL has not struck Iran (11th American night) — and now FEARS entrapment on Pickaxe rather than seeking it.** The posture note reverses slightly from 21 July's 'openly waiting to join': the Israeli press now frames Trump naming Pickaxe Mountain as a RISK of being drawn into escalation (Times of Israel: 'Israel reportedly concerned about being drawn into escalation'). Haaretz's convergence claim is the striking one: **'As Ground Invasion Looms, U.S. and Iran Want Wild-card Israel Out of the Fight'** — i.e. BOTH belligerents want Israel sidelined, and Israel itself may now prefer it. Times of Israel: 'Israel remains on the sidelines… which for Jerusalem is just fine for now.' No Iran-war polling anywhere (not a domestic mobilising story); Haaretz's military desk does not contradict the IDF. No Netanyahu-Trump contact confirmed in-window. **The firewall's integrity still rests on the US decision, but Israeli enthusiasm has cooled.** CONFIRMED (negative) / REPORTED (posture).")

sig("iraq",
    "**No confirmed militia attack on US forces (firewall holds) — and Baghdad's mediation offer was reportedly REBUFFED.** PM al-Zaidi offered to host US-Iran talks and carry a US message to Tehran; Trump reportedly DECLINED (Al-Hurra), though a competing account has him carrying a message — UNRESOLVED. The National frames Iraq's US economic talks as the 'base to mediate with Iran.' Al-Zaidi's Tehran trip is pending (~23 Jul). No new militia kinetic activity; the September US withdrawal timetable remains without update. CONFIRMED (non-attack) / REPORTED (mediation rebuff).")

sig("oman",
    "**Public silence holds (Day 6+) — but Oman is quietly active.** No ONA war statement reached any desk (site cert-failed; nothing in RSS). BUT 'Qatar, Oman discuss regional security amid US-Iran tensions' (22 Jul) and opinion coverage quotes Oman's FM telling Washington 'you've been containing the wrong country.' Read: Oman is mediating privately and declining to speak publicly — the silence is the METHOD, not absence. Axios places the current 10-day proposal as building on the 11 July Muscat plan. Any ONA statement remains a first-order signal. CONFIRMED (the silence).")

sig("mojtaba-khamenei",
    "**Day 145 — still no appearance, no audio, no verified photograph.** No pre-memorial appearance materialised; the 23/24 July memorial for his father is the next test. The exile-media 'coup' narrative persists — Iran International: 'Hardliner accuses Ghalibaf of paving way for coup through US deal' and 'Araghchi interview draws fire from Iran hardliners' — confirming the diplomatic track is being cast internally as treason and the elite fight is suppressed, not resolved. The 18 July written statement (which rebuked the hardliners and backed Pezeshkian/the MoU) remains his last output; he has issued text and only text for ~4.5 months. No new protest or execution news in-window. CONFIRMED (absence).")

# ============================== INDIA ==============================

sig("india",
    "**India's insulation CRACKED AT THE MARGIN — the first session this cycle where the war clearly led the tape lower, though the DII wall bent rather than broke.** Nifty -0.9% to 23,973 (broke below 24,000 intraday, ~700-800 Sensex points at the low), Bank Nifty -1.4%. Read it precisely: a -0.9% controlled decline is the DII wall bending — it absorbed -2% war gap-downs earlier in July — NOT a crash, despite ET's '₹4 lakh crore wealth wipeout' framing. **TWO drivers, and the second is NEW: (1) oil at $94 into a June import bill already +48%; (2) Trump's phased generic-pharma tariff — 0% for ~2 years from ~1 Aug, then 100% (~2028), up to 200% (~2029) — targeting India's ~$9.7bn US generic exports.** The 2-year grace means near-term cash impact is nil; it is a medium-term relocation-pressure instrument (analysts note Indian generics may still undercut US rivals even at tariff), so the pharma selloff (Aurobindo, Sun, Cipla, Lupin, Glenmark, Biocon) is a re-rating, not an earnings event. **The tape is under-weighting the offset: Jaishankar met Rubio in Manila (22 Jul), both sides 'pushing' an interim deal — the channel is open two days before the cliff.** CONFIRMED.")

sig("india",
    "**The rupee gave up its hold intraday — the borrowed-dollar defence is being tested AT the record.** USD/INR touched ₹96.53 late session after opening ~96.34-96.36 ('record not breached' early); it gave up the hold as the oil rally intensified (CNBC-TV18). So the record low of 96.52/96.60 (~14 July) is being REACHED in real time, not cleanly broken — the RBI is holding the line AT the record. The mechanism matters: that line is held with $20.72bn of BORROWED dollars via the swap/FCNR(B) facility, and ET reports the RBI is using the dollar-deposit surge to CUT its FX forward book (unwinding forwards rather than spending spot reserves) while briefing Reuters it is debating LIMITING intervention. **The 24 July weekly reserves release — the same day as the tariff cliff — will show the 13-17 July intervention and likely flatter the underlying spot defence.** CONFIRMED.")

sig("india",
    "**India-US trade deal UNSIGNED at T-2; a NEW 200% phased pharma tariff opens a non-crisis structural front, partly offset by Jaishankar-Rubio in Manila.** No signature, no extension text; Parliament told 'engaged with the US, studying all developments' (holding language). Trump's phased generic-drug tariff (0% for 2 years, then 100%/200%) is a medium-term relocation-pressure instrument that does NOT reverse on a Hormuz ceasefire — analogous to the Section 301 track. Jaishankar-Rubio (Manila, 22 Jul) 'pushing' an interim deal is the first minister-level US-India contact of the window and a de-escalatory signal against the deadlock narrative. Farmer protests continued (21 Jul Mahapanchayat, Shambhu border) but did not escalate further. Baseline snap-back mechanics unchanged (10% Section 122 lapse; Section 301 successor). CONFIRMED (unsigned) / CONFIRMED (pharma announcement).")

sig("india",
    "**Four Indian seafarers dead off Odesa — the Kremlin says it is 'in touch'; India still has not named Washington.** NEW: the Kremlin acknowledged contact with India following the 21 July summons of the Russian Chargé (Outlook India/PTI) — contact, not apology or admission. The figure is FOUR dead, one critical (corroborated across The Hindu, Indian Express, HT, FE; guarding against the false '9'). No evacuation, no further casualties, no Russian reply beyond 'in touch.' India has now named Tehran (14 Jul) and Moscow but STILL NOT Washington — the asymmetry holds. Notable media gap: the story has DROPPED off the Indian front page, displaced by the market selloff and the domestic protest thread. Q1 earnings that printed were strong and domestic (Nestlé +48%, TVS +67%, M&M Finance +70%) with no visible war-cost signal. CONFIRMED (summons) / REPORTED (Kremlin contact).")

sig("nifty-50",
    "**Nifty broke below 24,000 (-0.9% to 23,973), the war finally leading the Indian tape lower — but a controlled decline, not a crash.** Drivers: oil at $94 + Trump's phased 200% pharma tariff (pharma names down), against a still-supportive DII bid. Sensex -1.0% to 76,698; Bank Nifty -1.4% to 57,022, still weighed by the Monday NIM re-rating. The '₹4 lakh crore wipeout / -800 points' is the INTRADAY LOW; the ~close was -0.9%/-1.0%. Q1 prints strong and domestic (Nestlé +48%, TVS +67%). India VIX and exact Bank Nifty close could not be pinned (portals blocked) — flagged. The war premium is now transmitting to Indian equity via oil AND a new tariff vector, where for weeks it lived only in the rupee. CONFIRMED (directional; intraday levels late-session, not confirmed close).")

sig("inr-usd",
    "**The record is being TOUCHED in real time — ₹96.53 late session (22 Jul), after opening 96.34-96.36.** The 96.52/96.60 record of ~14 July is being REACHED, not cleanly breached; the rupee gave up early gains as the oil rally to $94 intensified. The RBI is holding the line AT the record with $20.72bn of borrowed dollars (swap/FCNR(B)) and is reportedly CUTTING its FX forward book rather than spending spot reserves, while briefing Reuters it is debating LIMITING intervention. **The defence is being tested precisely at the level it was designed to hold, on a day oil made a war-restart high. Watch the 24 July reserves release (same day as the cliff) — it will flatter the underlying spot defence.** CONFIRMED.")

sig("rbi",
    "The RBI is holding the rupee AT its 96.52 record with borrowed dollars, not spot reserves: ET reports it is using the $20.72bn dollar-deposit/FCNR(B) surge to CUT its FX forward book (unwinding forwards), while briefing Reuters it is debating LIMITING intervention. No new on-record RBI statement in-window. The tactic preserves headline reserves at the cost of a larger forward liability that reverses on maturity — so the 24 July weekly reserves release (same day as the tariff cliff) will look better than the underlying spot defence warrants. Repo 5.25%; next MPC 3-5 August. CONFIRMED (ET-reported).")

# ============================== MARKET / COMMODITY ==============================

sig("brent-crude",
    "**CRUDE FINALLY COUPLED — the flat price, not just cracks, did the work.** Brent +3.1% to $93.84, the war-restart high, +20.5% over 30 days; WTI +2.8% to $87.28. For the whole cycle Brent held -8% over three months despite the war; that decoupling broke on the month. **Chain: the ceasefire optimism that suppressed volatility Monday REVERSED — Trump 'We're not done in Iran,' declined the Iraqi channel, Axios 'eyes all-out war'; strike night 11 hit Bushehr province; a FOURTH tanker was struck; and the Houthi Saudi-crude embargo turned three tankers back. Risk premium was ADDED, not released.** The discipline check now cuts the OTHER way from Monday: the +20.5% 1M print says the market is re-pricing the escalation tilt in flat price for the first time this cycle, rather than confining the war to cracks, gas, fertiliser and the rupee — BUT the 3-month column is still -7.9%, so this is a re-arming TOWARD, not through, the Feb-May peaks. Distillate still dominates underneath: heating oil +32.4% 1M; cracks hit all-time records 16-20 July and eased this week only because CRUDE CAUGHT UP to products. Watch the binary — a joint-campaign decision plausibly gaps this to triple digits; a ceasefire acceptance collapses it. CONFIRMED.")

current("brent-crude",
        price="Brent $93.84 (+3.1% 1D, +20.5% 1M, -7.9% 3M) — war-restart high; WTI $87.28 (+2.8%). Heating oil $4.10 (+32.4% 1M); RBOB $3.27 (-4.0%, likely roll artifact); Henry Hub $2.87 (-11.9% 1M, DECOUPLED). Computed cracks: diesel $84.92, 3-2-1 $61.68 (below the 16 Jul records as crude caught up).",
        delta_1d="+3.1%", delta_1m="+20.5%",
        regime="CRUDE HAS COUPLED IN FLAT PRICE for the first time this cycle (+20.5% 1M) on the escalation tilt — Trump 'not done,' no ceasefire decision, night 11, a 4th ship, the Houthi Saudi embargo. Still -7.9% over 3M = re-arming TOWARD not through the Feb-May peaks. Distillate remains the tight leg (HO +32.4% 1M). The binary: a joint-campaign decision gaps to triple digits; a ceasefire acceptance collapses it.")

snapshot("brent-crude", "$93.84 (+3.1%) — war-restart high",
         "The escalation tilt won the session: Trump 'We're not done in Iran' + declined the Iraqi channel + Axios 'eyes all-out war'; strike night 11 (Bushehr province); a 4th tanker struck; the Houthi Saudi-crude embargo turned three tankers back. First time this cycle the FLAT PRICE, not just cracks, priced the war. Still -7.9% over 3M.")

sig("fed",
    "**THE OIL-TO-FED TRANSMISSION HAS INVERTED — July hike odds fell to ~7.6% (reported, 21 Jul) from 15.5% (18 Jul) and 46.5% (13 Jul) EVEN AS Brent hit $94 and US pump gas sits at $4.00.** The channel that defined June is not merely quiet; the market is pricing the energy spike as DEFERRABLE. Fed blackout holds until the 29 July decision; Warsh's 'regime change' testimony remains the operative signal. **The live channel is POLITICAL — gasoline at $4.00 (+86c y/y) is a Congressional argument, and Hegseth's $37.5bn war-cost disclosure feeds the appropriations fight.** Note the single-source caveat: the 7.6% figure is reported (CME direct blocked); the DIRECTION (further down) is the reliable content. CONFIRMED (directional).")

current("fed",
        price="29 July FOMC: ~7.6% hike / ~92% hold (reported 21 Jul), DOWN from 15.5% (18 Jul) and 46.5% (13 Jul). US 10Y 4.63%; 2Y 3.73%. Sept ~73% odds of >=1 hike. Blackout until 29 Jul.",
        delta_1d="hike odds 15.5% -> ~7.6%",
        regime="TRANSMISSION INVERTED. Brent $94 and $4.00 gasoline moved July hike odds DOWN, not up — the market prices the energy spike as a SEPTEMBER problem (Sept ~73% for a hike). Both Fed and ECB deferring. If Brent gaps to triple digits on a joint-campaign decision, that deferral is the mispriced risk. The live channel is political, not monetary.")

sig("ecb",
    "**The ECB will HOLD Thursday 23 July, with September flagged as the 'reckoning.'** Eurozone CPI is 2.8% (20 Jul); this is a NON-projection meeting, so June's stale Q3 energy-inflation forecast (12.5%, set before TTF broke EUR57) stands unrevised while **TTF is now EUR61.37 (+44.8% 1M, a new cycle high)** on the continued absence of Qatari LNG through Hormuz. Like the Fed, the ECB is treating a genuine supply shock as deferrable — the September meeting, with fresh projections, is where the energy path bites. CONFIRMED.")

sig("european-ttf-gas",
    "**New cycle high — EUR61.37/MWh (22 Jul), +2.8% d/d and +44.8% over 30 days**, above the EUR58.74 of 20 July. The driver is unchanged and physical: no laden Qatari LNG carrier has transited Hormuz in ~2 weeks. EU storage ~51.8% (STALE — could not refresh; 15-year low stands), mandatory target already relaxed 90%->80%. Pakistan paid its highest LNG spot since 2022 (17 Jul), evidence of Asian scramble for non-Qatari cargo. Gas remains the channel with no buffer, and it is now the clearest single price expression of the Qatari outage. CONFIRMED.")

sig("gold",
    "**Gold +1.3% to $4,122 (silver +1.6% to $59.78) — the inverted-haven bid holds because the RATES leg is not transmitting.** With July Fed hike odds collapsing to ~7.6% even at Brent $94, real-yield pressure is absent and gold is trading the ABSENCE of a Fed response rather than the war. The regime is intact on 1M/3M (-1.4% / -12.9%) but has lifted off the July lows as the rate threat receded. Note the 10Y ROSE to 4.63%, so this is a Fed-expectations bid, not a duration bid. **Gold is now the cleanest expression of 'the central banks are deferring the energy shock to September.'** CONFIRMED.")

current("gold",
        price="Gold $4,122.50 (+1.3% 1D, -1.4% 1M, -12.9% 3M); Silver $59.78 (+1.6%); Platinum $1,664 (+2.3%).",
        delta_1d="+1.3%", delta_1m="-1.4%",
        regime="INVERTED-HAVEN REGIME INTACT but the RATES transmission has INVERTED — July hike odds fell to ~7.6% at Brent $94, real-yield pressure released, gold lifted off its July lows. Trading the ABSENCE of a Fed response, not the war. 10Y rose to 4.63%, so this is a Fed-expectations bid, not duration. Silver/platinum firm alongside.")

sig("nifty-50",
    "Monday's NIM re-rating extended into a broader risk-off Wednesday: Bank Nifty -1.4%, the index below 24,000. See the india node for the full driver split (oil $94 + the phased pharma tariff, partly offset by Jaishankar-Rubio). Q1 prints that landed were strong and domestic — Nestlé +48% PAT/+25% rev, TVS +67%, M&M Finance +70% — with NO visible war-cost signal, confirming the selloff is macro/tariff-driven, not earnings-driven. CONFIRMED.")

sig("shipping-tankers",
    "Tanker equities finally caught a war-risk bid — **Frontline +4.1%, BOAT +2.0% (22 Jul)** — on the day the Houthi Saudi-crude embargo turned three tankers back (AIS) and a fourth Hormuz tanker was struck. But the move prices a SECOND-chokepoint premium on a DECLARATION, not a closure: no Houthi ship-strike, Bab el-Mandeb open. The crew-supply constraint (Sinokor six-months' salary) remains the binding gate on Hormuz volume. CONFIRMED.")

sig("kospi",
    "Asia tech ripped again — KOSPI +0.7% (after Monday's snap-back), TAIEX +1.3%, SMH +4.5% — still -25.4% on the month; ~0% war contribution. **The key negative finding persists and is now a thesis test: NO fab production cut announced by Samsung, SK Hynix or TSMC, with chip stocks RECOVERING.** The helium-shortage thesis is failing on timing — the 8-12 week rationing-to-shipment lag implied output cuts by now — but the clock has not fully run out. Hold, do not raise the helium weight. CONFIRMED.")

sig("defense-sector",
    "**Fifth consecutive confirmation that defence does not rally on this war.** ITA +0.2% on the day, -3.9% on the month — through strike night 11, Hegseth's $37.5bn war-cost disclosure, and a munitions-replenishment fight in Congress. Re-armament is contractual; more war carries no new information for these earnings streams. Defence remains NOT a war-escalation hedge in this cycle, and de-escalation costs it nothing. CONFIRMED.")

sig("uranium-sector",
    "URA +4.1% on the day but still -15.8% 1M and -30.3% 3M — a froth-unwind bounce with spot uranium flat; the equity-vs-commodity divergence is unchanged and the -30% quarter remains ~85-90% non-crisis. De-escalation does not rescue uranium equities because the war never drove them down. CONFIRMED.")

sig("cf-industries",
    "**+19.5% on the month to $122.96** — still running on the gas/ammonia MARGIN (cheap Henry Hub at -11.9% 1M against elevated Middle East FOB), not a Hormuz-tightness story; the 19 July correction stands (urea de-escalated ~50% from April on Chinese export quotas; phosphate/DAP is the tight leg). Long a margin, not a shortage — more fragile than +19.5% suggests. Fertiliser CFR benchmarks could not be refreshed this cycle (STALE). CONFIRMED (equity) / STALE (benchmarks).")

sig("russia",
    "The Kremlin says it is 'in touch' with India after the summons over the four Odesa seafarer deaths (MV Golden Leo, 20 Jul) — Russia's first acknowledgement, contact not apology. This is the sharpest Delhi-Moscow friction of the war period, landing while Russia supplies ~50% of India's crude at record volumes and Washington threatens tariffs over that relationship. Separately the Black Sea chokepoint story remains the WHEAT bid (+14.1% 1M) — Kerch/Azov shut, ~25% of Russian exports affected — with ZERO Iranian content. Moscow continues to position as an Iran broker (TASS 'offers lifeline') while co-sponsoring the UNSC counter-draft with China. CONFIRMED.")

# ============================== TRIGGERS ==============================

trig_set("nuclear-program", "Fordow, Natanz or Esfahan", "watching",
         "REVIEWED 22 Jul — REMAINS AT WATCHING for a THIRD consecutive window. Fordow, Natanz, Esfahan and Pickaxe Mountain all UNSTRUCK. BUT strike night 11 hit BUSHEHR PROVINCE, which hosts Iran's operational, IAEA-safeguarded Bushehr Nuclear Power Plant — the three struck sites read as military targets and are NOT confirmed to be the reactor, but this is the nearest US ordnance has come to a live safeguarded reactor (air defences activated near the plant 20 Jul; an Iranian official alleged an airstrike near it, US unacknowledged; no IAEA statement yet). Trump renewed the threat to hit the underground enrichment site 'probably pretty soon' — RHETORIC. Iran's restraint posture is unchanged (UNSC filing invoking safeguards, no NPT threat, no enrichment escalation). Do not fire on proximity or on rhetoric.")

trig_set("nuclear-program", "Pickaxe Mountain", "watching",
         "REVIEWED 22 Jul — REMAINS AT WATCHING. Pickaxe UNSTRUCK. Trump publicly reiterated the threat ('probably pretty soon'), and the WSJ centrifuge-relocation claim stands as an ISRAELI ASSESSMENT with imagery-confirmed construction/concealment. Haaretz's 'ground invasion looms' framing raises the adjacent scenario. No strike; the trigger requires a confirmed strike on the enrichment programme itself.")

trig_set("iran", "rial breaks 2,000,000", "watching",
         "REVIEWED 22 Jul — REMAINS AT WATCHING; the threat is roughly stable. The rial is ~1,915,000 (22 Jul), the 3% reversal-off-its-19-July-peak having STALLED and turned slightly softer again, now 5.8% from the 2,000,000 threshold. Direction sideways-to-soft, no capitulation. The stall coincides with the ceasefire stalling and Trump's escalation rhetoric — the rial remains the cleanest real-time proxy for the diplomacy odds. Single-source (alanchand).")

trig_set("iran", "A US-Iran meeting actually convenes", "watching",
         "REVIEWED 22 Jul — REMAINS AT WATCHING, and the odds DID NOT improve. No meeting, no venue, no named negotiator. Two setbacks: Trump reportedly DECLINED the Iraqi (al-Zaidi) channel, and the 10-day proposal's AUTHORSHIP is now disputed (JPost: Iran secretly submitted it — single-source, inverts the baseline). Iran has neither accepted nor rejected it, and Iranian STATE MEDIA IS HIDING THE PROPOSAL entirely. Rubio holds the door open with blame pre-assigned to Tehran while Trump talks escalation. Per the standing rule, willingness is rhetoric until a meeting convenes. The binary Axios says resolves 'within days' has not resolved.")

trig_set("houthis", "First KINETIC Houthi attack on a Saudi-linked", "watching",
         "REVIEWED 22 Jul — REMAINS AT WATCHING. The Saudi-shipping embargo is enforced by warning EMAIL AND RADIO ONLY; three Saudi-crude tankers made AIS-confirmed U-turns, but NO vessel has been struck (~15 days since the US hit Iranian power infrastructure; the Reuters conditional order still unfired). Saudi loadings -36% on the threat. The trigger requires a CONFIRMED kinetic attack on a Saudi-linked hull; a declaration plus voluntary reroutes is not that. Resolution instrument: UKMTO/JMIC advisories and Kpler Yanbu loadings, not Houthi statements. A sanctioned Iranian vessel transiting the Red Sea freely underlines this is targeted coercion of Riyadh, not a closure.")

trig_set("houthis", "FIRED-CONDITION/ABSENT-RESPONSE WATCH", "watching",
         "REVIEWED 22 Jul — REMAINS AT WATCHING; the gap is now ~15 days. The US struck Iranian power infrastructure and Iran admitted it, yet the Reuters-reported Iranian order to close Bab el-Mandeb has NOT produced its predicted kinetic response. What moved instead was the Saudi-specific embargo (Yemen-internal casus belli), enforced non-kinetically. Reading (c) 'the Houthis pursue their own agenda' continues to strengthen relative to (a) 'Tehran's threshold is the national grid.'")

trig_set("inr-usd", "USD/INR breaks ₹96 within 5-7 sessions", "active_fired",
         "REVIEWED 22 Jul — STAYS active_fired, now at the RECORD. USD/INR touched ₹96.53 late session (22 Jul) — the 96.52/96.60 record of ~14 July is being REACHED, not cleanly breached (opened 96.34-96.36; gave up the hold as oil rallied to $94). The RBI is holding the line AT the record with $20.72bn of borrowed dollars and is CUTTING its forward book rather than spending spot reserves. This is the defence being tested precisely at its design level on a war-restart-high oil day. Watch the 24 July reserves release.")

trig_add("inr-usd",
         "USD/INR breaks ₹96.60 cleanly and holds for 3+ sessions — a clean break of the all-time record, distinct from the current touch-and-hold",
         "watching", ["india", "rbi", "brent-crude", "nifty-50"],
         "ADDED 22 Jul. The rupee is now TOUCHING the 96.52/96.60 record intraday (96.53 on 22 Jul) but the RBI is holding the line there with borrowed dollars. This trigger tests whether the defence BREAKS — a clean, sustained move beyond 96.60 — as opposed to the current defended touch. Given the defence is funded by a swap facility that reverses on maturity and the RBI is reportedly debating LIMITING intervention, a clean break is a live risk, especially if oil holds >$90 through the 24 July reserves print and the tariff cliff. Resolution: 3 consecutive closes beyond 96.60.")

trig_set("brent-crude", "Brent sustained above $100 for 5+ sessions by ~18 August", "watching",
         "REVIEWED 22 Jul — REMAINS AT WATCHING, and the approach is closer. Brent $93.84 is the war-restart high (+20.5% 1M), and for the first time this cycle the FLAT PRICE is pricing the war rather than just cracks. Goldman's re-emerged call: base $80 Q4, '$120 if Hormuz disruptions persist.' At $94 the market is roughly half-way to Goldman's conditional. The binary is Trump's ceasefire-vs-campaign decision (Axios: within days) — a joint-campaign choice plausibly gaps Brent to triple digits and fires this; a ceasefire acceptance collapses it. Still -7.9% over 3M — not yet through the Feb-May peaks.")

trig_add("united-states",
         "US authorises a ground operation into Iran, OR explicitly rules one out — the 'ground invasion looms' scenario (Haaretz, 22 Jul) that neither markets nor prediction data are pricing",
         "watching", ["iran", "israel", "brent-crude", "trump"],
         "ADDED 22 Jul. Haaretz's analytical desk framed a US ground operation as a live scenario ('As Ground Invasion Looms, U.S. and Iran Want Wild-card Israel Out of the Fight'), consistent with Frank Kendall's doctrinal point that air power must be coupled with ground operations to suppress mobile launchers, and with the observed exhaustion of the easy target set (night 11 hit military infrastructure in Bushehr/Ilam, not new high-value assets). This is the scenario NEITHER the oil market (VIX 17.46) NOR prediction data is pricing. Resolution instrument: a confirmed deployment order or an explicit administration ruling-out within ~2 weeks. Watch alongside Trump's ceasefire-vs-campaign decision.")

trig_add("india",
         "US phased generic-pharma tariff (0% -> 100% -> 200%) is finalised/formalised into rule, OR India secures a carve-out — a non-crisis structural headwind that does NOT reverse on a Hormuz ceasefire",
         "watching", ["indian-it", "united-states", "nifty-50"],
         "ADDED 22 Jul. Trump announced a phased tariff on generic drugs — 0% for ~2 years from ~1 Aug, then 100% (~2028), up to 200% (~2029) — targeting India's ~$9.7bn US generic exports. The 2-year grace means near-term cash impact is NIL; it is a medium-term relocation-pressure instrument analogous to the Section 301 track, and it hit Indian pharma (Aurobindo, Sun, Cipla, Lupin, Glenmark, Biocon) as a re-rating rather than an earnings event. It is a NON-crisis headwind: a Hormuz ceasefire does not reverse it. Watch whether it is formalised into rule (raising it from announcement to policy) or whether the Jaishankar-Rubio Manila channel secures an Indian carve-out in the 24 July trade framework.")

print("\n".join(str(x) for x in log))
print(f"\nTOTAL OPS: {len(log)}")
