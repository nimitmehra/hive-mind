#!/usr/bin/env python3
"""Graph update for the 2026-07-23 MORNING brief.
Backup: backups/2026-07-23/graph_v1
Sources: staging/2026-07-23-morning/{intel,markets}.md
Run ONCE, capture output to a file — do NOT pipe to grep (that re-executes and duplicates).
"""
import json, os

D = "2026-07-23"
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


# ============================== THE FIREWALL CRACK ==============================

sig("houthis",
    "**THE RED SEA FIREWALL WENT KINETIC — the first confirmed Houthi ship-strike of the campaign.** After ~15 days enforcing the Saudi-shipping embargo by email/radio (three AIS turn-backs), the Houthis struck TWO Saudi crude tankers — **Encelia and Layla** — with missiles and drones; ONE SET ABLAZE; all crew reported safe. This is CONFIRMED, not one-side: **Saudi state news (SPA) confirmed a Saudi-owned vessel was targeted, and UKMTO/UK confirmed a tanker on fire** — corroborated across Reuters, NYT, Al Jazeera, Seatrade, CNBC, Splash247. The ship-strike count resets to Day 1. READ THE CALIBRATION AND LIMITS PRECISELY: tankers not warships, crew safe, no mass casualty; **Bab el-Mandeb is NOT closed — ISW counts 30 vessels transiting on 22 Jul, down from 64 the prior day (a HALVING, not a closure)**; NO Saudi military counterstrike on Yemen reported; and a sanctioned Iranian rocket-fuel vessel continues to transit the Red Sea FREELY — this is TARGETED COERCION of Saudi cargo, not a general shut strait. Houthi HOCC broadened the language to 'all vessels at Saudi ports prohibited.' Trump threatened to deploy heavy bombers against the Houthis (REPORTED, not executed). CONFIRMED (kinetic strike).")

sig("saudi-arabia",
    "**Two Saudi tankers struck by the Houthis (Encelia, Layla; one ablaze, crew safe) — and Riyadh has NOT retaliated militarily.** Saudi SPA confirmed the targeting; Saudi 'vows to protect shipping' but the 'mulling military escalation' from the prior window is STILL unconverted to action. Saudi loadings -36% on the threat. THE STRATEGIC COUNTERWEIGHT: the same window, a US-Saudi NUCLEAR COOPERATION PACT was announced ('historic') — Riyadh deepening US ties precisely as its tankers burn, which binds it CLOSER to Washington and further reduces any chance it restricts US operations. The commercial stakes are unchanged: the East-West Petroline to Yanbu is the Hormuz workaround the Houthi strike targets. CONFIRMED (strike, no retaliation) / REPORTED (nuclear pact).")

sig("red-sea",
    "The Houthi Saudi-crude embargo became KINETIC — two Saudi tankers struck, one ablaze (Saudi SPA + UKMTO CONFIRMED). BUT Bab el-Mandeb is NOT closed: ISW counts 30 transits on 22 Jul vs 64 the prior day — a coercive HALVING, not a closure, with >=7 vessels rerouting. A sanctioned Iranian vessel transits freely. Tanker equities did NOT spike (Frontline -1.3%) — the market prices a second-chokepoint premium in oil (Brent ~$97) but not a closure. Suez data could not be refreshed. CONFIRMED (kinetic) / the strait remains OPEN.")

# ============================== KINETIC / DIPLOMACY ==============================

sig("united-states",
    "**The US posture swung hard to CAMPAIGN overnight — but no formal decision (~Day 3 of 'within days').** Every vector moved toward escalation: **Rubio PRONOUNCED THE CEASEFIRE DEAD** — 'Iran's shipping attacks kill the ceasefire deal, but the door to diplomacy stays open' — the clearest US burial of the 10-day proposal yet, pinned to the tanker attacks. **Trump: 'Iran not ready to make a deal.'** The physical build-up is real (ACTION): WSJ 'US Surges Forces Toward Middle East, Giving Trump Options to Expand Iran War'; **B-1 supersonic bombers being deployed** — the platform that could reach Pickaxe. Trump renewed the threat to hit Iranian bridges and power plants; Iran's symmetric counter-threat: 'destroy multiple energy facilities for every bridge or power plant' struck. **The House PASSED the ~$1.15 trillion defence bill 213-207 party-line (22 Jul)** — Democrats made it a referendum on the war; it 'tees up billions more.' War cost officially $37.5bn. US deaths hold at 17; Al-Azraq MIA unresolved; ~100 injured in two weeks. The softening signal has MIGRATED to Fox's OPINION layer (Ingraham et al. framing the war as a midterm liability) while Trump personally hardens. CONFIRMED / REPORTED.")

sig("nuclear-program",
    "**THE TRIPWIRE HELD A FOURTH WINDOW — strike night 12 ran but Fordow, Natanz, Esfahan, Pickaxe Mountain and the Bushehr reactor are ALL UNTOUCHED**, even as the B-1 bombers that could reach Pickaxe surge into theatre. CENTCOM's 12th consecutive night hit missile, drone and air-defence sites (Reuters, Anadolu-per-CENTCOM); a provincial Iranian official reported central-Iran impacts, consistent with that set — NOT the nuclear complex. No new IAEA statement. Iran's restraint posture is UNCHANGED and remains the strongest non-weaponization signal: no NPT-withdrawal threat, no enrichment escalation, and it took the Darkhovin strike to the UNSC invoking safeguards in its own favour. Trump renewed the Pickaxe threat ('probably pretty soon') — RHETORIC. NEW ADJACENT DEVELOPMENT: a US-Saudi nuclear COOPERATION pact was announced, alarming Israel ('losing its seat at the table') and giving Iran a fresh regional-nuclearization grievance. CONFIRMED (the absences).")

sig("iran",
    "**CEASEFIRE-BY-ERASURE HARDENED INTO EFFECTIVE REJECTION.** Iranian state media (Mehr, Press TV) covers the 10-day proposal by pretending it does not exist — carrying only strike-claims and counter-threats, with the American-dead claim now location-specific ('killed in a strike on a compound in Jordan') and adopting Trump's own infrastructure-threat symmetry ('destroy multiple energy facilities for every bridge/power plant'). The mediation track appears ONLY in exile media: Iran International reports Pakistan/Qatar pressing a memorandum but that **'Tehran has NOT publicly endorsed the initiative.' That non-endorsement plus total state-media erasure IS the rejection** — the clearest read on Iran's answer. ISW corroborates: 'US-Iran Negotiations: Nothing significant to report.' No meeting, no venue, no named negotiator. The al-Zaidi Iraqi channel is contradictory (Trump 'declined' 21 Jul vs 'asks al-Zaidi to mediate' 22 Jul — UNRESOLVED); Pakistan/ISLAMABAD is emerging as the venue Washington may actually use. CONFIRMED (no process) / REPORTED (the erasure-as-rejection read).")

sig("strait-of-hormuz",
    "**The IRGC shifted tactics to MINE-LAYING and declared Hormuz 'completely closed.'** Separate from the Red Sea strikes, the IRGC says an oil tanker exploded after striking a MINE in the Strait, with two vessels turning back (Anadolu, Caliber.Az) — a shift from the earlier deniable 'accidents on an unsafe route' to an asserted mine mechanism — and now claims it 'stopped THREE oil tankers' (up from two). Vessel unnamed; no independent damage confirmation of the mine claim. Transit counts remain contradictory and unconfirmed: ~4/day (20 Jul, stale) vs a Fortune India '10' (23 Jul), neither a clean Kpler/Windward print — treat the level as directionally very low. The escorted southern corridor remains collapsed (~2% of transits, baseline). REPORTED/CLAIMED (IRGC origin).")

sig("shipping-tankers",
    "Two theatres now active: the Houthi kinetic strike on two Saudi tankers in the Red Sea (CONFIRMED) plus the IRGC mine-strike claim in Hormuz (REPORTED) — the struck/attacked toll is now 5-6 hulls across both. Tanker equities did NOT rally (Frontline -1.3%, BOAT flat) — the market prices volume collapse and a second-chokepoint premium in OIL, not in tanker earnings; utilisation not the war-risk headline drives the equity. Crew-supply constraint reconfirmed (Sinokor six-months' salary). No clean transit count. CONFIRMED (Red Sea) / REPORTED (Hormuz mine).")

sig("marine-war-risk-insurance",
    "**THE CORRECTION HELD ANOTHER CYCLE — and a soft number must be rejected.** Despite 5-6 struck/attacked hulls across two theatres, there is STILL no war-risk premium print newer than the 9 July Marsh figure of 2-6% of vessel value (~14 days stale), no JWC listed-area circular, and no ITF/IBF Warlike-Operations-Area declaration (still OVERDUE). **REJECT the 'near-1,900% war-risk surge' number blanketing the tape: it traces to deVere Group CEO Nigel Green, a WEALTH-MANAGEMENT COMMENTATOR, describes a premium INCREASE not a percentage-of-hull rate, and is NOT a Marsh/WTW/JWC print — CLAIMED sentiment.** The binding constraint remains labour: Sinokor's six-months'-salary offer for one ~30-day Hormuz round trip stands. The market clears on seafarer refusal, not cover withdrawal. CONFIRMED (the absence of any hard print above 2-6%).")

sig("mojtaba-khamenei",
    "**Day 146 — still invisible — but President Pezeshkian PUBLICLY ELEVATED him, and the memorial drew NO coverage.** Pezeshkian described 'Supreme Leader Mojtaba Khamenei' as taking a 'hands-on role,' and Iranian media credited Mojtaba with uncovering an alleged Israeli 'secret armed group' inside Iran. **This is the civilian president openly naming and legitimising a successor who has not shown his face in ~4.5 months** — an attempt to manufacture authority for an absent Leader, consistent with the 'Vahidi writes for him / collective rule under the seal' reading. The memorial for his father, flagged for 23/24 July, drew NO coverage in any outlet — suppressed or not occurring. No public appearance, audio or verified photograph. An Iranian MP floated a petrol price rise despite the war — a domestic-distress signal. REPORTED (Pezeshkian's remarks single-origin) / CONFIRMED (the continued absence).")

# ============================== FIREWALLS HOLDING ==============================

sig("hezbollah",
    "**~Day 16 of complete silence toward Israel** — no rocket, missile or drone across Israeli, Lebanese and pan-Arab sources, through strike night 12, the US-Saudi nuclear pact and a second chokepoint going kinetic. No new IDF strike inside Lebanon, no new Qassem statement. The pilot zone stays notional — the only fresh item is the Lebanese PM visiting a border village (optics), with NO verified additional Israeli troop movement or additional villages beyond the one-village-packaged-as-three baseline. The National's editorial 'Gaza shows what truces without rules look like' is a pointed Gulf caution that pledge-only deals (Aoun-Trump; any US-Iran ceasefire) fail without enforcement mechanisms. CONFIRMED (the silence).")

sig("israel",
    "**Israel STILL has not struck Iran (12th American-only night) — and its fear FLIPPED from entrapment to ABANDONMENT.** The 'stay out' posture and 'ground invasion looms' frame persist (Haaretz's Harel; ToI treats Pickaxe as a US target). The new and more important shift is diplomatic, not military: **the surprise US-Saudi nuclear cooperation pact flipped Israeli anxiety from being dragged in to being CUT OUT** — Times of Israel 'US confirms nuclear pact with Saudi Arabia, to Israel's alarm'; Haaretz 'Israel is Losing Its Seat at the Table.' Relieved to be militarily excluded, alarmed to be diplomatically sidelined, with a Netanyahu-Trump RIFT widening ('beside himself with rage after Trump call'). No Iran-war polling; Netanyahu's campaign is not tied to the war by any outlet. CONFIRMED (no strike) / REPORTED (abandonment framing).")

sig("iraq",
    "Militia firewall holds — no confirmed attack on US forces; the one kinetic item was three drones INTERCEPTED near a US consulate in northern Iraq (no impact, no attribution). The al-Zaidi mediation channel is contradictory (Trump 'declined the relay' 21 Jul vs 'asks al-Zaidi to mediate' 22 Jul — UNRESOLVED); ISNA frames his Tehran visit as aiming to keep Baghdad OUT of the conflict. No new on the Kirkuk-Baniyas pipeline or the September withdrawal timetable. CONFIRMED (non-attack).")

sig("oman",
    "**Public silence holds (Day 7+) — but the back-channel is now VISIBLE.** ONA unreachable; no Omani official statement in any RSS query. BUT 'Iran and Oman Just Floated a Plan to End the Hormuz Crisis' (National Security Journal) confirms Oman is mediating privately. Read: silence remains the METHOD. Any ONA statement is still a first-order signal not yet triggered. CONFIRMED (the silence).")

# ============================== INDIA ==============================

sig("india",
    "**THE DII WALL CRACKED — the first genuine crack this cycle — and the war led the tape lower a THIRD day.** On 22 July BOTH FIIs (-Rs819 cr) AND DIIs (-Rs418 cr) were net sellers, with DIIs selling two sessions running. **The domestic bid that absorbed every war gap-down for weeks turned SELLER — which is why the decline, while still orderly (~-0.6%, not a crash), is now PERSISTENT rather than instantly bought.** The Nifty closed 22 Jul at ~23,996 (Sensex 76,755, -715) and is a third day down 23 Jul (~23,861 intraday), below 24,000. Three overlapping drivers: oil near $100 into a June import bill already +48%; Trump's phased 200% pharma tariff; and the 24 July cliff at T-1, UNSIGNED. On the deal: the US State Dept calls the INTERIM tranche 'almost complete' post-Manila, but a US official puts the FULL deal 3-4 months out, and the pharma tariff is live friction in the room — NO Indian MEA confirmation, no signed text, no extension, no official snap-back clarification. CONFIRMED.")

sig("india",
    "**The rupee HELD its record — defended, NOT cleanly broken.** USD/INR ~96.48 early / ~96.54 now (23 Jul), with the RBI reported intervening as it 'nears record low'; it did NOT cleanly break 96.60 — the trigger did not fire. The RBI is holding the line with $20.72bn of BORROWED dollars (swap/FCNR(B)) and is CUTTING its record ~$104bn net-short forward book using deposit inflows — reducing future dollar-delivery obligations rather than spending spot reserves. **The 24 July weekly reserves release — the same day as the tariff cliff — will flatter the underlying spot defence.** The 200% pharma tariff is now the LEAD domestic market driver (India Infoline: 'Nifty Tumbles as Trump's Generic Drug Tariff Threat Sparks Pharma Sell-Off'); Indian pharma -3-4% and the industry is 'seeking engagement' with Washington — lobbying, NOT a government act. Dr Reddy's and Cipla report Q1 after the close, into the tariff overhang. CONFIRMED.")

sig("nifty-50",
    "Third consecutive down day, below 24,000 (23,861 intraday; 22 Jul close ~23,996). **The DII wall cracked** — both FIIs and DIIs net sellers 22 Jul (-Rs819 cr / -Rs418 cr), the domestic bid no longer unconditionally absorptive. Bank Nifty -1.2%. Drivers: oil near $100, the pharma tariff (pharma -3-4%), and the T-1 tariff cliff. Q1 prints that landed remain strong and domestic (no war-cost signal); Infosys/Dr Reddy's/Cipla report after close. Exact Bank Nifty/India VIX close and 23 Jul FII/DII could not be pinned (portals blocked). CONFIRMED (directional).")

sig("fii-flows",
    "**THE DII WALL CRACKED — both sides net sellers 22 July: FIIs -Rs819 cr AND DIIs -Rs418 cr**, per Moneycontrol provisional. DIIs have now sold two sessions (21 Jul was FII +Rs1,650 / DII -Rs657). This is the first time this cycle the domestic bid, which absorbed every war gap-down, turned net seller — the mechanism behind the persistent (not bought-instantly) grind lower. The standing derivatives posture is unchanged: FIIs net short 216,528 index futures; FPIs long >$4.2bn FAR bonds. 23 Jul provisional publishes after close. CONFIRMED (exchange provisional).")

sig("inr-usd",
    "**The record HELD — ~96.48-96.54 (23 Jul), defended, NOT cleanly broken past 96.60.** After touching the 96.52/96.60 record intraday 22 Jul, the rupee recovered ~5 paise on RBI support at the 23 Jul open, then drifted back to ~96.54 as oil rallied toward $100. The RBI is holding the line AT the record with $20.72bn of borrowed dollars and is CUTTING its record ~$104bn net-short forward book. **The defence is being held precisely at its design level for a fourth session on a war-restart-high oil day; the clean-break trigger (>96.60 held 3 sessions) has NOT fired.** No '96.96' or sub-96 breakout appeared — reject any such print. CONFIRMED.")

# ============================== MARKET / COMMODITY ==============================

sig("brent-crude",
    "**OIL IS CHARGING TOWARD $100 — a SECOND straight ~3% day, Brent $96.93 (->$97.32 intraday), +25.8% over 30 days.** WTI $88.87. The escalation vector broke open overnight and every input added premium: strike night 12, B-1 bombers surging, Rubio declaring the ceasefire 'killed,' Trump 'Iran not ready,' the IRGC declaring Hormuz 'completely closed,' and the Houthis going KINETIC on two Saudi tankers. Goldman's $120 conditional is back in headlines. **The discipline check: Brent is still -7.7% over 3 MONTHS — a re-arm TOWARD not through the Feb-May peaks — but at $97 the market is ~half-way to Goldman's $120 conditional and knocking on the graph's sustained-$100 trigger.** THE BINARY IS NOW SHARPLY ASYMMETRIC: a formal joint-campaign decision plausibly gaps this through $100; only a ceasefire acceptance — which Rubio just pronounced dead — collapses it. Distillate still the tightest leg (heating oil +31.3% 1M). Cracks holding roughly flat as crude rises. CONFIRMED.")

current("brent-crude",
        price="Brent $96.93 (->$97.32 intraday) (+3.0% 1D, +25.8% 1M, -7.7% 3M); WTI $88.87 (+2.3%). Heating oil $4.14 (+31.3% 1M); RBOB $3.29 (-3.7%, roll artifact); Henry Hub $2.97 (-5.5% 1M). Cracks: diesel $85, 3-2-1 $61 (below the 16 Jul records). Brent-WTI spread $8.06.",
        delta_1d="+3.0%", delta_1m="+25.8%",
        regime="CHARGING TOWARD $100 — 2nd straight +3% day on the escalation tilt (night 12, B-1s surging, Rubio 'ceasefire killed,' Houthis kinetic, Hormuz 'completely closed'). ~half-way to Goldman's $120 conditional. Still -7.7% 3M = toward not through the peaks. BINARY: a joint-campaign decision gaps through $100; only a ceasefire (Rubio-pronounced-dead) collapses it. Distillate the tight leg.")

snapshot("brent-crude", "$96.93 (->$97.32) (+3.0%) — 2nd straight +3% day",
         "Escalation vector broke open: strike night 12, B-1 bombers surging, Rubio declared the ceasefire 'killed,' IRGC declared Hormuz 'completely closed,' and the Houthis went KINETIC on two Saudi tankers. +25.8% 1M. Knocking on the sustained-$100 trigger and ~half-way to Goldman's $120 conditional. Still -7.7% 3M.")

sig("sp-500",
    "**THE DIVERGENCE HIT AN EXTREME — VIX FELL to 16.64 (-2.4%), toward pre-war levels, on the day Brent charged toward $100 and a SECOND chokepoint went kinetic.** S&P -0.1% (22 Jul close), KOSPI +4.4%, Bovespa +2.4% — global equity is risk-ON. The war premium lives ENTIRELY in oil and the physical-supply complex; the US index-level war premium is not merely small, it is SHRINKING as the physical shock intensifies. One of two things is mispriced: either oil over-prices a supply shock equity thinks won't land, or equity vol is dangerously cheap into a binary (Trump's decision, the Friday UNSC vote) that could gap oil through $100. **Given Rubio just declared the ceasefire dead and B-1s are surging, the risk skew favours the latter — convexity in equity vol is cheap.** CONFIRMED.")

sig("gold",
    "**Gold is NOT spiking at Brent $97 — the inverted-haven regime at its cleanest.** Gold -0.7% to $4,118, roughly flat on the month (-0.3%), on a day oil charged toward $100 and a second chokepoint went kinetic; under a normal haven regime it would be bid hard. The US 10Y ROSE to 4.66% — real-yield pressure caps gold even with July Fed hike odds near zero (~7.6%, stale), and with the oil->Fed transmission inverted (spike deferred to September) there is no near-term rate-cut impulse to lift it. Silver (-0.7%) confirms it is the whole precious complex. **This war moves gold sideways-to-down, via rates, not up — DE-escalation, not escalation, is what would help gold (by killing the oil-driven inflation impulse).** CONFIRMED.")

sig("fed",
    "**THE OIL->FED TRANSMISSION STAYS INVERTED — and the ECB just confirmed the thesis.** July Fed hike odds remain ~7.6% (stale 21 Jul; no fresh FedWatch) even as Brent charges toward $100 and US pump gas sits at $4.00; the market prices the energy spike as a SEPTEMBER problem. **The ECB's 23 July decision is a PAUSE explicitly citing Middle East/oil risk, with September flagged for a possible HIKE (not a cut)** — the first CENTRAL-BANK CONFIRMATION of the deferral thesis the graph has carried two cycles. Both the Fed and the ECB are underwriting a genuine supply shock as a Q3 problem. Fed blackout until 29 July; Warsh's 'regime change' testimony remains the operative signal. If Brent gaps through $100 on a joint-campaign decision, that deferral is the mispriced risk. CONFIRMED (directional).")

sig("ecb",
    "**The ECB PAUSED on 23 July, explicitly citing Middle East/oil risk — the stagflation frame now has central-bank confirmation.** Reuters: 'ECB to pause rate hikes but may signal more is needed'; Anadolu: 'remains cautious amid Middle East risks'; France 24: 'New Mideast fighting puts eurozone rate-setters on alert.' Eurozone CPI 2.8%; a non-projection meeting, so June's stale Q3 energy-inflation forecast (12.5%) stands unrevised while TTF prints a fresh cycle high (EUR63.75). **September is flagged as the decision point, and the debate is a HIKE not a cut** — i.e. the ECB is deferring the energy shock to Q3 exactly as the Fed is. This confirms the 'September reckoning' the graph flagged. CONFIRMED (decision landing just after the data window; well-corroborated).")

sig("european-ttf-gas",
    "New cycle high — EUR63.75/MWh (23 Jul), +EUR2.38 over EUR61.37, still driven by the absence of any laden Qatari LNG through Hormuz. EU storage ~53% (vs ~64% a year ago; refill lagging into a 15-year-low base). The ECB explicitly cited energy risk in pausing today. Gas remains the channel with no buffer and the clearest single price expression of the Qatari outage. JKM stale at $19.93 (16 Jul). CONFIRMED (TTF) / STALE (storage/JKM).")

sig("kospi",
    "Asia tech ripped again — KOSPI +4.4% to 7,096 (sharply recovered from -25% 1M last week to -13.5%), SMH +0.5%, TAIEX flat — ~0% war contribution, an oversold snap-back in the DRAM/AI complex. **THE HELIUM THESIS IS NOW TESTABLE-AND-FAILING: the 8-12 week rationing-to-shipment lag has ELAPSED and there is STILL no production cut announced by Samsung, SK Hynix or TSMC — only recycled March-era warnings. If a fab cut does not print soon, the helium-disruption thesis is being FALSIFIED, not merely delayed.** Hold the helium edge one more cycle, then cut if silent. CONFIRMED.")

sig("defense-sector",
    "**Sixth consecutive confirmation that defence does not rally on this war.** ITA +0.6% on the day, -1.9% on the month — through strike night 12, a $37.5bn war cost, and the House passing a $1.15 TRILLION defence bill 213-207. Re-armament is contractual; more war carries no new information for these earnings streams. Defence remains NOT a war-escalation hedge in this cycle, and de-escalation costs it nothing. CONFIRMED.")

sig("cf-industries",
    "+22.9% on the month (+3.6% on the day, to $127.35), Nutrien +2.5% — running on the gas/ammonia MARGIN (cheap Henry Hub vs elevated ME FOB), not a Hormuz-tightness story; the 19 July correction stands (urea de-escalated on Chinese quotas; phosphate/DAP is the tight leg). Long a margin, not a shortage. Fertiliser CFR benchmarks could not be refreshed (STALE). CONFIRMED (equity) / STALE (benchmarks).")

sig("russia",
    "The wheat bid HARDENED — CBOT wheat +20.2% on the month (from +14.1%), still ENTIRELY the Russia/Kerch story (Azov chokepoints shut, ~25% of Russian exports affected), with ZERO Iranian content. On the seafarer thread: the death toll off Odesa holds at FOUR (MV Golden Leo, 20 Jul); Jaishankar raised it with Lavrov and the Kremlin says it is 'in touch' — contact, no apology. India has named Tehran and Moscow but still NOT Washington. Moscow continues to resist the US/Gulf UNSC Hormuz draft (vote scheduled Friday 24 Jul). CONFIRMED.")

# ============================== TRIGGER DECISIONS ==============================

trig_set("nuclear-program", "Fordow, Natanz or Esfahan", "watching",
         "REVIEWED 23 Jul — REMAINS AT WATCHING for a FOURTH consecutive window. Strike night 12 hit missile/drone/air-defence sites; Fordow, Natanz, Esfahan, Pickaxe and the Bushehr reactor are all UNSTRUCK, even as B-1 bombers that could reach Pickaxe surge into theatre. Trump renewed the Pickaxe threat ('probably pretty soon') — rhetoric. Iran's restraint posture unchanged (UNSC filing invoking safeguards; no NPT threat; no enrichment escalation). Do not fire on rhetoric or on the B-1 surge. The US-Saudi nuclear pact is a diplomatic development, not a strike.")

trig_set("nuclear-program", "Pickaxe Mountain", "watching",
         "REVIEWED 23 Jul — REMAINS AT WATCHING, probability rising. Unstruck, but the B-1 bombers that are the plausible delivery platform are now surging into theatre (WSJ), and Trump reiterated the threat. This is the sharpest approach yet to a strike on the enrichment programme itself, but it has NOT occurred. Requires a confirmed strike.")

trig_set("houthis", "First KINETIC Houthi attack on a Saudi-linked", "fired",
         "FIRED 23 Jul. The Houthis struck two Saudi crude tankers (Encelia, Layla) with missiles/drones — one ablaze, crew safe — CONFIRMED by Saudi SPA (host state) and UKMTO (authority), corroborated across Reuters/NYT/Al Jazeera/Seatrade/CNBC/Splash247. This converts the 20 July embargo DECLARATION into a confirmed KINETIC attack. The condition — 'first confirmed kinetic attack on a Saudi-linked vessel' — is met by 2+ independent operational sources including the host state. NOTE the calibration that keeps this from being the full escalation: tankers not warships, crew safe, Bab el-Mandeb NOT closed (ISW: 30 transits vs 64 prior day), no Saudi military retaliation, a sanctioned Iranian vessel transiting freely. This is a fired trigger on a CONFIRMED ACTION, not rhetoric.")

trig_set("houthis", "FIRED-CONDITION/ABSENT-RESPONSE WATCH", "watching",
         "REVIEWED 23 Jul — the SAUDI-directed response fired (kinetic strike on two Saudi tankers) but the ORIGINAL Reuters conditional — close Bab el-Mandeb if the US hits Iranian POWER infrastructure — STILL has not fired its predicted response: Bab el-Mandeb is NOT closed (ISW: 30 transits on 22 Jul, a halving not a closure). The Houthi action remains Saudi-directed on Yemen-internal grounds, NOT a general strait closure tied to the US-Iran power-infrastructure trigger. Reading (c) 'the Houthis pursue their own agenda' is now strongly confirmed by the kinetic strike being aimed at SAUDI cargo specifically.")

trig_set("brent-crude", "Brent sustained above $100 for 5+ sessions by ~18 August", "watching",
         "REVIEWED 23 Jul — REMAINS AT WATCHING, and this is the closest approach yet. Brent $96.93 (->$97.32 intraday), a SECOND straight +3% day, +25.8% 1M — knocking on $100 but not sustained above it. Goldman's $120 conditional is back in headlines; at $97 the market is ~half-way there. THE BINARY: Rubio pronounced the ceasefire 'killed' and B-1s are surging, so a formal joint-campaign decision plausibly gaps Brent through $100 and fires this within days; a ceasefire acceptance (now unlikely) collapses it. Still -7.7% 3M — not yet through the Feb-May peaks. Do not pre-fire on an approach.")

trig_set("iran", "A US-Iran meeting actually convenes", "watching",
         "REVIEWED 23 Jul — REMAINS AT WATCHING; the odds WORSENED. Rubio pronounced the ceasefire 'killed'; Iran has NOT endorsed the memorandum and its state media erases the proposal entirely (erasure = rejection); ISW reports 'nothing significant' on negotiations. The al-Zaidi Iraqi channel is contradictory; Islamabad is emerging as a possible venue but no meeting, venue or named negotiator exists. Willingness is rhetoric until a meeting convenes; the binary Axios said resolves 'within days' has not, and is now tilting to campaign.")

trig_set("inr-usd", "USD/INR breaks ₹96.60 cleanly and holds", "watching",
         "REVIEWED 23 Jul — REMAINS AT WATCHING; NOT fired. The rupee is holding AT the record (~96.48-96.54) but the RBI defended the line at the 23 Jul open (recovered ~5 paise) — there is NO clean, sustained break above 96.60. The defence is being held at its design level with $20.72bn of borrowed dollars while the RBI cuts its record ~$104bn forward book. The clean-break condition (3 consecutive closes beyond 96.60) is unmet. Given oil is charging toward $100 and the 24 July reserves print + tariff cliff both land tomorrow, a clean break is a live risk into that double event.")

trig_set("united-states", "US authorises a ground operation into Iran", "watching",
         "REVIEWED 23 Jul — REMAINS AT WATCHING, probability rising. Haaretz's 'ground invasion looms' frame persists and the B-1 bomber surge (WSJ 'US surges forces… options to expand') is the physical build-up consistent with it, but NO ground-operation order has been given and none ruled out. Kendall's doctrine (air power must couple with ground ops) plus the exhausted easy-target set (night 12 hit military infrastructure) keep this live. Still the scenario neither oil (VIX 16.64) nor prediction data is pricing.")

trig_add("saudi-arabia",
         "Saudi Arabia launches a kinetic military response against the Houthis in Yemen — converting 'vows to protect shipping' + 'mulling escalation' into action after the 23 July tanker strikes",
         "watching", ["houthis", "red-sea", "brent-crude", "iran"],
         "ADDED 23 Jul. The Houthis struck two Saudi tankers (one ablaze) on 23 July and Riyadh has NOT retaliated militarily — 'vows to protect shipping,' MEE's 'mulling escalation' still unconverted. A Saudi counterstrike on Yemen would be a major escalation of the Red Sea front and would put the >$130 Brent scenario's second-chokepoint logic in play. The countervailing pressure is the just-announced US-Saudi nuclear pact, which binds Riyadh to Washington's escalation-management. Resolution instrument: confirmed Saudi/coalition airstrikes on Yemen, vs. continued restraint. Watch alongside Trump's threatened US bomber deployment against the Houthis.")

trig_add("ecb",
         "The ECB HIKES in September (or explicitly signals a September hike), OR the energy-inflation deferral breaks and it is forced to act sooner — the 'September reckoning' the graph has flagged",
         "watching", ["fed", "european-ttf-gas", "brent-crude", "gold"],
         "ADDED 23 Jul. The ECB PAUSED on 23 July explicitly citing Middle East/oil risk, with September flagged as the decision point and the debate framed as a HIKE not a cut (eurozone CPI 2.8%, TTF at a cycle high EUR63.75). This mirrors the Fed deferring the oil shock to Q3 (July hike odds ~7.6%). The trigger tests whether the deferral holds to September or breaks sooner if Brent gaps through $100 on a joint-campaign decision. Next ECB meeting is the September projection meeting — the first with fresh forecasts since the war re-armed oil. Resolution: the September decision, or an inter-meeting move.")

print("\n".join(str(x) for x in log))
print(f"\nTOTAL OPS: {len(log)}")
