# Verification Report — 13 October 2026 (Morning)
Generated: ~17:30 IST Tue 13 Oct 2026 | Fact-Checker: Red Team
Brief checked: `briefs/2026-10-13-morning.md`
Evidence record: `staging/2026-10-13-morning/intel.md`, `markets.md`, `graph-changelog.md`; graph nodes `strait-of-hormuz`, `houthis`, `red-sea` read directly.
Independent checks: about 45 fresh web searches and fetches (URLs below), plus yfinance pulls at ~17:15 IST for 30 tickers.

## Corrections applied (Chief of Station, ~18:00 IST)
All 22 flags were accepted on the evidence and applied: 43 exact text replacements in the brief (each matched once). Graph: `houthis` holy-city and `red-sea` ≥2% triggers reverted to watching with notes; `strait-of-hormuz` enforcement 'with attribution' label withdrawn (status ACTIVE kept; attribution REPORTED/CLAIMED); the matching wording fixed in `strait-of-hormuz`, `artesh`, `iran`, `irgc`, `brent-crude`, `fed`, `houthis` and `saudi-arabia`; `iran→strait-of-hormuz` edge context relabelled. Viewer rebuilt. Noted, not fixed: `edges.json` holds a duplicate `iran→strait-of-hormuz` entry (pre-existing).

## Summary

- **What was checked:** all 7 Section I items (about 55 separate claims), 8 Section II blocks, 4 Section III blocks, 21 trigger changes plus the Hormuz re-confirmation and 5 held triggers, and 30 market data points.
- **Flags raised: 22.**
  - **CRITICAL: 1.** A graph trigger was fired on a claim from one side that the other side denies.
  - **HIGH: 7.** Two Section I headlines get cause and effect or the arithmetic wrong; there is one tag drift on attribution, one wrong date, one reversed causal chain, one headline stronger than the brief's own body, and one trigger recorded under the wrong label.
  - **LOW: 14.** Precision, wording and completeness.
- **Market data:** clean on every headline number. One window intraday low is off by about $0.50. Two Page-2 "1D" changes actually span two sessions.
- **Recommendation: approve with corrections.** No correction kills a lead item. The changes are to two headlines, the date of one quote, one causal sentence, the attribution framing in the Hormuz item, and two trigger labels.

---

## Flags

### Flag C1: `houthis` "Mecca forensic OR second holy-city incident" was FIRED on a one-sided claim
- **Issue:** A trigger moved on insufficient evidence.
  - The changelog fires leg 2 because the coalition announced on 1 Oct that a Houthi drone hit Medina's Taibah power station on 29 Sep.
  - The only evidence for both the event and the attribution is the coalition itself (spokesman al-Maliki). The wreckage has not been published.
  - The Houthis call the claim "a lie". On 12 Oct they publicly exempted the Mecca and Medina airports from their warnings.
  - The trigger's own text asks for a holy-city *interception* to be announced. This was a claimed hit on a power substation.
  - The pipeline rule is: "Triggers move to active ONLY on confirmed actions verified by 2+ independent operational sources." What is confirmed here is the announcement, not the attack.
  - The node's cascade list (`brent-crude`, `red-sea`, `united-states`) means a "fired" status will be read downstream as a Houthi attack on a holy city.
- **Evidence:**
  - Coalition-only sourcing; Houthi denial: [Al-Monitor](https://www.al-monitor.com/originals/2026/10/saudi-coalition-accuses-houthis-drone-attack-medina), [Euronews 2 Oct](https://euronews.com/2026/10/02/houthis-deny-saudi-accusations-of-targeting-medinas-holy-sites), [Tribune PK 1 Oct](https://tribune.com.pk/story/2632475/saudi-led-coalition-says-houthis-attacked-power-station-in-medina).
  - No independent verification of the wreckage or the attribution was found.
  - intel SAU-A6 tags it CLAIMED.
- **Mitigation:** the node note already says CLAIMED, and no edge weight was attached. That is why the brief text needs only the footer and count fixes.
- **Severity:** CRITICAL (graph). The brief impact is LOW.
- **Recommended correction:**
  - **Graph (not edited by me):** set the `houthis` trigger back to `watching`, with this note: "TESTED 2026-10-13 on a coalition claim (Medina Taibah station, 29 Sep; wreckage unpublished; Houthis deny; Houthis exempted Mecca/Medina airports 12 Oct). Not fired: the event and the attribution are single-source." If the schema allows, use a `fired_on_claim` status with cascades suppressed.
  - **Brief, Section III, exact replacement:**
    - OLD: `The graph reviewed about 120 trigger points and changed 21. **14 fired, 6 resolved, 1 re-activated, and 23 new dated watches were added.**`
    - NEW: `The graph reviewed about 120 trigger points and changed 19. **12 fired, 6 resolved, 1 re-activated, and 23 new dated watches were added.** Two more — the Houthi holy-city and Red Sea war-risk triggers — were tested and held.`
  - **Brief, footer, exact replacement** (this also covers Flag H7):
    - OLD: `*Trigger points: ~120 reviewed, 21 changed. FIRED: saudi escalates-alone; saudi RESTART; houthis holy-city (announcement leg; attribution CLAIMED); red-sea war-risk (Saudi-linked only); iran US–Iran meeting (proximity);`
    - NEW: `*Trigger points: ~120 reviewed, 19 changed. TESTED AND HELD AT WATCHING: houthis holy-city (coalition says a Houthi drone hit a Medina power station on 29 Sep; Houthis deny; no independent confirmation); red-sea war-risk (≥2% only on Saudi port calls; neutral transit 0.2–0.3%). FIRED: saudi escalates-alone; saudi RESTART; iran US–Iran meeting (proximity);`
  - **If only one of C1 and H7 is accepted:** write "changed 20 / 13 fired" instead.
- **Applied:** Yes — by the Chief of Station after review (graph trigger reverted to watching; brief text replaced).

### Flag H1: Section I item 1 headline reverses the order of events and leaves out the Houthi side
- **Issue:** The headline says the Houthis attacked airports "and Riyadh answered by escalating alone". The evidence runs the other way.
  - Riyadh's escalation came first. Saudi jets struck Sanaa from 1 Oct, Dawn of Yemen was announced on 4 Oct and launched on 5 Oct, and the Mecca Pact was activated on 5 Oct.
  - The airport war came after, from 6 to 13 Oct.
  - Every item under "Riyadh's response" predates the first airport strike.
  - The Houthis claimed the 10-Oct strike and frame the airport campaign as retaliation for Saudi strikes on Yemeni civilian infrastructure, including Sanaa airport on 9–10 Oct per Al-Masirah. The brief does not carry that framing.
- **Evidence:**
  - intel SAU-A7: Sanaa from 1 Oct; offensive 4–5 Oct; pact 5 Oct.
  - intel SAU-B1: airport war 6–13 Oct; the Houthis frame it as retaliation.
  - [France 24 live, 11 Oct](https://www.france24.com/en/middle-east/20261011-live-saudi-arabia-vows-decisive-response-after-deadly-houthi-strike-on-riyadh-airport): "Houthis claim responsibility for Saturday's deadly attack on Riyadh airport".
  - [Al Jazeera 6 Oct](https://www.aljazeera.com/news/2026/10/6/pakistan-turkiye-join-saudi-deterrence-against-houthis-what-that-means): pact activated 5 Oct.
  - [Al Jazeera 11 Oct](https://www.aljazeera.com/news/2026/10/11/yemen-fighting-expands-as-houthis-attack-saudi-airport-what-to-know): offensive launched 4 Oct.
- **Severity:** HIGH. The sequence is inverted and the other side is missing.
- **Recommended correction:**
  - OLD: `### The Houthis turned their war with Saudi Arabia on civilian airports, and Riyadh answered by escalating alone.`
  - NEW: `### Saudi Arabia escalated alone in Yemen, and the Houthis answered with mass-casualty strikes on Saudi civilian airports.`
  - OLD: `- **Riyadh's response.** It did not wait for Washington.`
  - NEW: `- **Riyadh's escalation (it began before the airport strikes and has continued through them).** It did not wait for Washington.`
  - OLD: `It is the deadliest attack on the kingdom in more than a decade.`
  - NEW: `It is the deadliest attack on the kingdom in more than a decade. The Houthis claimed the 10 October strike and call the airport campaign retaliation for Saudi strikes on Yemeni civilian infrastructure, including, per Houthi media, Sanaa airport (9–10 October).`
- **Applied:** Yes — by the Chief of Station after review.

### Flag H2: "The Hormuz ship war roughly quintupled" compares counts over windows of different length
- **Issue:** The arithmetic is wrong.
  - The brief compares about 25 strikes in **20 days** (23 Sep–12 Oct) with 5 strikes in **6 days** (16–21 Sep).
  - As rates, that is about 1.25 a day against about 0.83 a day, a rise of roughly 50%.
  - The peak weeks were 11–12 attacks (UKMTO week to 9 Oct; Reuters 28 Sep–5 Oct), about 1.6–1.7 a day, which is roughly double the earlier rate.
  - "Quintupled" appears in the Section I headline and is echoed in Risk Landscape.
  - The tally of about 25 is itself defensible as "our count". The named incidents in KIN-A1 add up to roughly 25–28, depending on overlap in the delayed UKMTO reports.
- **Evidence:**
  - intel KIN-A1 (weekly counters).
  - Previous brief's "five UKMTO tanker strikes 16–21 Sep".
  - [gCaptain, 12 Oct: "Six Ships Struck in Single Day"](https://gcaptain.com/new-reports-reveal-five-more-ships-hit-near-hormuz/).
  - [Iran International: 12 attacked in one week](https://www.iranintl.com/en/202610139592).
  - [Reuters via GV Wire, 7 Oct: highest week of the war](https://gvwire.com/2026/10/07/attacks-on-tankers-in-hormuz-hit-highest-of-any-week-since-start-of-iran-war-sources-say/).
- **Severity:** HIGH. This is a quantitative error in a Section I headline.
- **Recommended correction:**
  - OLD: `### The Hormuz ship war roughly quintupled, and Iran now claims it.`
  - NEW: `### The Hormuz ship war intensified and spread, and the IRGC now claims strikes.`
  - OLD: `about **25 vessels were struck between 23 September and 12 October**, against five in the six days before the last brief. **Six were hit on Sunday 11 October alone.**`
  - NEW: `about **25 vessels were struck in the 20 days between 23 September and 12 October** — about 1.25 a day, against five in the six days before the last brief (about 0.8 a day). The peak weeks ran at 11–12 attacks (UKMTO; Reuters), roughly double the earlier rate. **Six were hit on Sunday 11 October alone.**`
  - OLD: `- The Hormuz ship war: about 25 hulls, an attacker who now claims it, anchorages and Indian crews.`
  - NEW: `- The Hormuz ship war: about 25 hulls in 20 days, IRGC claims of specific strikes (one shown false), anchorages and Indian crews.`
- **Applied:** Yes — by the Chief of Station after review.

### Flag H3: Sayyari's title is inflated, his statement is over-read as an "admission", and attribution is stated as fact
- **Issue:** There are three linked problems.
  - **The title is wrong.** The brief calls Sayyari "Iran's armed-forces chief of staff". Al Jazeera calls him "chief of staff and joint coordinator of the army", meaning the Artesh, the regular military. Press TV calls him "the Army's deputy coordinator". Iran's armed-forces chief of staff is a different person (Abdollahi, per intel ISR-A1).
  - **The statement does not say what the brief implies.** His words were "We have struck blows against enemy vessels. If anything else happens against Iran, we will strike them again." He does not say which vessels. Press TV headlined it as a conditional threat ("…if aggression resumes"), and its background cites a 7 May operation against US destroyers. Section III nonetheless says attribution now rests "on Iran's own admission", and Risk Landscape calls Iran "an attacker who now claims it". That turns undefined rhetoric into an admission of the merchant-ship campaign.
  - **Tags drift.**
    - Section I item 7 states flatly "Iran's fire has gone to ships".
    - "JMIC calls the attacks Iranian" is REPORTED in intel KIN-A2: gCaptain's reading plus a snippet of Update 104.
    - UKMTO still attributes none of the strikes, and no flag state, owner or India's MEA has named Iran.
    - The IRGC did claim specific strikes on 9, 10 and 12 Oct, so "the IRGC now claims strikes" is accurate. One of those claims (*NV Sunshine*) was denied by the ship's owner.
- **Evidence:**
  - [Al Jazeera, 11 Oct](https://www.aljazeera.com/news/2026/10/11/hormuz-attacks-intensify-as-efforts-to-end-war-on-iran-stall): title; quote; no referent; UKMTO "unidentified projectile".
  - [Press TV, 11 Oct](https://www.presstv.co.uk/Detail/2026/10/11/778092/Iran-vows-to-strike-enemy-vessels-in-Strait-of-Hormuz-if-hostile-actions-resume): "Army's deputy coordinator"; conditional framing.
  - intel KIN-A2 tags.
  - Node `strait-of-hormuz` note "WITH attribution on record".
  - Counterweight, not a source of attribution: Seatrade (6 Oct) describes "Iranian attacks" in its [report](https://seatrade-maritime.com/tankers/sinokor-maran-gas-and-sinogas-ships-hit-in-spate-of-hormuz-attacks).
- **Severity:** HIGH: tag drift, and rhetoric used as attribution. It is not CRITICAL because the trigger status did not change and the brief quotes the statement word for word with the UKMTO caveat.
- **Recommended correction:**
  - OLD: `  - **Iran's armed-forces chief of staff, Sayyari, said on 11 October: "We have struck blows against enemy vessels."**`
  - NEW: `  - **Habibollah Sayyari, chief of staff and joint coordinator of Iran's regular army (Artesh), said on 11 October: "We have struck blows against enemy vessels. If anything else happens against Iran, we will strike them again."** He did not say which vessels, and Press TV ran it as a conditional threat; it is not an admission of any specific merchant-ship strike.`
  - OLD: `  - The US-led maritime centre (JMIC) calls the attacks Iranian. UKMTO's individual notices still say "unknown projectile".`
  - NEW: `  - JMIC advisories (the US-led maritime centre that publishes through UKMTO), as relayed by gCaptain, describe the campaign as IRGC/Iranian. UKMTO's individual notices still say "unknown projectile", and no flag state, owner or India's MEA has named Iran.`
  - OLD: `No Iranian salvo at any state for about 34 days; Iran's fire has gone to ships.`
  - NEW: `No Iranian salvo at any state for about 34 days; the fire in the window has gone at ships, which the IRGC's own claims and JMIC tie to Iran but UKMTO has not attributed.`
  - OLD: ``- `strait-of-hormuz` **"enforcement on a neutral vessel"** is re-confirmed as active, now with attribution resting on Iran's own admission.``
  - NEW: ``- `strait-of-hormuz` **"enforcement on a neutral vessel"** stays active (UKMTO-verified strikes on neutral hulls, plus a UKMTO-reported IRGC hail-and-turn-back off Khasab ~4 October). Attribution of the strikes is still REPORTED/CLAIMED — IRGC claims (one shown false), a general Artesh statement and the US-led JMIC — not UKMTO or an independent tracker, which the trigger requires.``
  - Footer OLD: `Hormuz enforcement re-confirmed with attribution.`
  - Footer NEW: `Hormuz enforcement stays active; attribution still REPORTED/CLAIMED (no UKMTO or independent attribution).`
  - **Graph (not edited):** in the `strait-of-hormuz` ENFORCEMENT note and the `artesh` signal, replace "Iran's own armed-forces chief admitting the campaign" / "Sayyari's admission" with "Artesh chief of staff/joint coordinator Sayyari's general statement ('struck blows against enemy vessels'; referent unspecified; conditional threat)".
- **Applied:** Yes — by the Chief of Station after review.

### Flag H4: Gharibabadi's "finalizing" remark was made on 12 Oct, not "today"
- **Issue:** The date is wrong, and it carries a market attribution.
  - The remark was made on Monday 12 Oct, to Al-Araby TV.
  - Mehr's English report is datelined "TEHRAN, Oct. 12" at 20:40. Arutz Sheva (published 13 Oct, 04:39) says "Monday".
  - The brief, following intel DIP-A6, says "today" and partly blames today's −2% Brent move on the remark. Brent actually settled +1.8% on 12 Oct, the day the remark was made. CNBC attributes today's dip to Russian supply prospects.
  - The "two voices" contrast still holds: Rezaei spoke on 11 Oct, Gharibabadi and Baghaei on 12 Oct.
- **Evidence:**
  - [Mehr, 12 Oct](https://en.mehrnews.com/news/248533/Iran-ready-for-both-diplomacy-and-war-deputy-FM).
  - [Israel National News, 13 Oct](https://www.israelnationalnews.com/news/434516).
  - yfinance BZZ26: 12 Oct settle 106.65, +1.8%.
  - intel MAC-A1 (CNBC).
- **Severity:** HIGH. It is a factual date error, and it feeds a causal claim about the market.
- **Recommended correction:**
  - OLD: `  - Deputy foreign minister Gharibabadi said today that Iran is "finalizing" its response.`
  - NEW: `  - Deputy foreign minister Gharibabadi told Al-Araby TV on Monday 12 October that Iran is "finalizing" its response (Mehr).`
  - OLD: `It trades at $104.50 today (−2.0%) on Russian diesel supply and Iran's "finalizing" remark.`
  - NEW: `It trades at $104.50 today (−2.0%), which wires attribute mainly to Russian supply prospects.`
  - Page 2 OLD: `today: Russian diesel / "energy ceasefire" + Iran's "finalizing"`
  - Page 2 NEW: `today: Russian diesel / "energy ceasefire" (Iran's "finalizing" came on 12 Oct)`
- **Applied:** Yes — by the Chief of Station after review.

### Flag H5: Aramco's price cut is presented as a response to an event that came a week later
- **Issue:** The causal chain is reversed.
  - The brief says Asian buyers refused to charter inside Hormuz (Reuters, 12 Oct) and "Aramco **therefore** cut its Asian list price to −$5."
  - The cut was announced on **5 Oct**, a week earlier. The reasons reported at the time were to offset record freight and to protect market share.
  - The 12-Oct Reuters story describes what Aramco did *next*: it moved Hormuz-loaded November volumes into delivered spot sales, some about $20 over the official selling price (OSP).
  - Reuters' word is "refrained" from chartering, which is softer than "refused".
- **Evidence:**
  - [The National, 5 Oct](https://www.thenationalnews.com/business/energy/2026/10/05/saudi-aramco-cuts-asia-crude-prices-to-six-year-low-amid-recovery-as-oil-flows-rebound/).
  - [EnergyNow/Reuters, 5 Oct](https://energynow.com/2026/10/saudi-arabia-unexpectedly-cuts-november-oil-prices-to-asia-to-6-year-lows/): freight and market-share rationale.
  - [Business Recorder/Reuters, 12 Oct](https://www.brecorder.com/news/40443852/asian-refiners-buy-spot-nov-saudi-oil): buyers "refrained from chartering ships to load crude inside of the strait"; about $20 over the November OSP.
- **Severity:** HIGH. The brief misstates why a party acted.
- **Recommended correction:**
  - OLD: `- **Why the price held anyway.** Asian buyers **refused to charter ships to load inside Hormuz** (Reuters, 12 October). Aramco therefore cut its Asian list price to −$5 (deepest since 2020) while reportedly selling delivered cargoes about **$20 over it**. Physical crude tells the same story:`
  - NEW: `- **Why the price held anyway.** On 5 October Aramco cut its Asian list price to −$5 (deepest since 2020) to offset record freight and defend market share. A week later Reuters reported that Asian buyers **refrained from chartering ships to load inside Hormuz**, so Aramco moved those volumes into delivered spot sales — some reportedly about **$20 over** the list price. Physical crude tells the same story:`
- **Applied:** Yes — by the Chief of Station after review.

### Flag H6: "The war is pushing US rates up" is stronger than the brief's own attribution
- **Issue:** The headline is stronger than the body.
  - The Section I item 6 headline attributes the US rates move to the war.
  - The evidence record (markets.md C4) and the brief's own Page 2 row "US 10Y / 30Y … ~35%" put about 65% of the rise on non-war drivers: issuance, a global long-end selloff, AI bond supply and the Fed path on payrolls.
  - This matters for deployment. Condition 2 (US 10Y below 5%) will not be delivered by a peace deal alone if two-thirds of the move is not the war.
- **Evidence:** markets.md C4 ("Split: ~35% crisis-linked (oil → Fed path), ~65% non-crisis"); brief Page 2.
- **Severity:** HIGH. The headline contradicts the brief's own analysis.
- **Recommended correction:**
  - OLD: `### The war is pushing US rates up, not inflation expectations — and that, not Hormuz, is what is moving money out of Asia.`
  - NEW: `### US rates — not inflation expectations, and not Hormuz — are what is moving money out of Asia; the war explains about a third of the rise.`
- **Applied:** Yes — by the Chief of Station after review.

### Flag H7: The `red-sea` "≥2% (Lloyd's/Marsh) OR liner suspension" trigger was FIRED under the wrong label
- **Issue:** The evidence does not meet the trigger's own text.
  - The trigger asks for a *Red Sea/Bab el-Mandeb* war-risk print at or above 2% from *Lloyd's/Marsh*.
  - The 3–7% figures are broker quotes (Reuters; McGill and Partners) for **Saudi port calls** (Yanbu, Jizan). They are not a transit print, and they are not from Lloyd's or Marsh.
  - The neutral transit rate is 0.2–0.3%, falling and below July's 0.5%.
  - The liner leg is also unmet: carriers *added* Suez services.
  - The trigger's own design note says it is "the market's own verdict on whether Houthi 'safe for all but Saudi' is believed". That verdict is "believed", which means the trigger did **not** fire.
  - A binary trigger recorded as "fired (split)" will be read later as Red Sea war-risk at 2% or more.
  - The brief text is transparent about the split. The problem is the label in the graph and the footer.
- **Evidence:** intel SAU-A10 (Reuters, 25 Sep); node `red-sea` condition text and prior note.
- **Severity:** HIGH (graph label). The underlying data is real, which is why this is not CRITICAL.
- **Recommended correction:**
  - **Graph:** set the `red-sea` trigger to `watching` (or `resolved_not_fired`) with this note: "Neutral transit 0.2–0.3% (falling); Saudi-port-call premiums 3–7% logged as a separate signal; liner leg unmet."
  - **Brief:**
    - OLD: ``- The `red-sea` war-risk trigger **fired for Saudi-linked tonnage only** (3–7%, against 0.2–0.3% for neutral transits). The insurance market believes the Houthi pledge.``
    - NEW: ``- The `red-sea` war-risk trigger did **not** fire: premiums above 2% apply only to Saudi port calls (3–7%, broker quotes via Reuters), while neutral Red Sea transits pay 0.2–0.3%. The insurance market believes the Houthi pledge.``
  - **Footer:** covered by the C1 replacement.
- **Applied:** Yes — by the Chief of Station after review.

### Flag L1: KKIA was "hit on five days"
- **Issue:** The evidence shows **four** days with hits: 6 or 7 Oct, 8, 10 and 11 Oct. On 12 Oct missiles were intercepted over Riyadh, though Saree claimed "the hit was precise"; that is a CLAIMED hit. The 13 Oct strikes were at Khamis Mushait.
- **Evidence:** intel SAU-B1; [Khaleej Times explainer](https://www.khaleejtimes.com/gulf/houthi-attacks-saudi-airports-flight-disruptions-key-events).
- **Severity:** LOW.
- **Correction:**
  - OLD: `Riyadh's King Khalid airport (KKIA) was hit on five days between 6 and 13 October.`
  - NEW: `Riyadh's King Khalid airport (KKIA) was attacked on at least five days between 6 and 12 October and hit on four of them (6/7, 8, 10 and 11 October; on 12 October missiles were intercepted over Riyadh, though the Houthis claim a hit).`

### Flag L2: The Fujairah turn-back date and the "late September" wording
- **Issue:** Bloomberg *reported* on 12 Oct that ships "stopped or reversed course in recent days"; the turn-backs did not all happen on 12 Oct. Separately, the Lloyd's record is for the month of September, not "late September".
- **Evidence:** [Bloomberg, 12 Oct](https://www.bloomberg.com/news/articles/2026-10-12/supertankers-turn-from-gulf-oil-transfer-hub-amid-iran-s-attacks); intel KIN-A4.
- **Severity:** LOW.
- **Correction:**
  - OLD: `Bloomberg reports at least ten supertankers turned back from Fujairah on 12 October.`
  - NEW: `Bloomberg reported on 12 October that at least ten supertankers and several Suezmaxes bound for Fujairah had stopped or reversed course in recent days.`
  - OLD: `Late September was the busiest month of the war (Lloyd's List: 477-plus transits).`
  - NEW: `September was the busiest month of the war (Lloyd's List: 477-plus non-Iranian transits).`

### Flag L3: The Brent window low, and "That was the low"
- **Issue:**
  - yfinance shows the front month (December, on its first day as front month) trading at **$96.56 intraday on 1 Oct**. The 6-Oct low was $97.08.
  - "That was the low" ($99.25) contradicts "the low of the window was $97.06" two sentences later.
  - The scorecard's "never went below $97" is therefore wrong by about $0.50.
  - These are yfinance daily bars; confirm against ICE if possible.
- **Severity:** LOW. The $90 conclusion is unaffected.
- **Correction:**
  - OLD: `November Brent settled at $99.25 on 22 September, the day of the last brief. That was the low.`
  - NEW: `November Brent settled at $99.25 on 22 September, the day of the last brief — the lowest settle of the window.`
  - OLD: `The low of the window was $97.06 intraday on 6 October.`
  - NEW: `Intraday it dipped to about $97 twice: $96.56 on 1 October (the December contract's first day as front month) and $97.08 on 6 October.`
  - OLD: `**Not vindicated.** Brent never went below $97, even after Yanbu restarted.`
  - NEW: `**Not vindicated.** Front-month Brent never traded below about $96.5, even after Yanbu restarted.`

### Flag L4: "knocked off $2–5 for a day or two"
- **Issue:** On settlement prices this mostly did not happen.
  - G7 release (2 Oct): settle −$0.06, with an intraday low $4.6 below the high.
  - Trump pledge (8 Oct): settle +4.1%.
  - Russian diesel (9 Oct): settle +0.4%.
  - The dips were intraday.
- **Evidence:** yfinance BZ=F/BZZ26 daily bars; intel MAC-A1 table.
- **Severity:** LOW.
- **Correction:**
  - OLD: `Every Washington de-escalation headline — the G7's 100mb stock release, Trump's pledge, Russian diesel — knocked off $2–5 for a day or two at most.`
  - NEW: `Each de-escalation headline — the G7's 100mb stock release, Trump's pledge, Russian diesel — took $2–5 off intraday at most, and most of those dips were gone by the settle.`

### Flag L5: Rezaei's title
- **Issue:** Rezaei is the SNSC's secretary ("security chief" in IRNA's English). The president chairs the council. Calling him "head" implies he outranks Pezeshkian.
- **Evidence:** intel DIP-A5/E ("SNSC secretary Rezaei"); [IRNA](https://en.irna.ir/news/86289861/Security-chief-US-response-to-Iran-s-7-conditions-insufficient).
- **Severity:** LOW.
- **Correction:**
  - OLD: `Rezaei, head of Iran's Supreme National Security Council,`
  - NEW: `Rezaei, secretary of Iran's Supreme National Security Council (which the president chairs),`

### Flag L6: Small tag drifts in the US–Iran item
- **Issue:** Four small problems.
  - Vance's "softening" is the analysts' reading. Rubio, Hegseth and Trump have repeated only "no nuclear weapon".
  - The US rejection of Iran–Oman joint management of the strait is REPORTED by a single outlet (The National).
  - The NYT and Axios reports came on 8 Oct, the same day as the pledge; only The Atlantic's came the day before.
  - The second carrier group and the 10,000 personnel are REPORTED (Bloomberg, citing a US official).
- **Evidence:** intel DIP-A14, DIP-B2, DIP-B3, KIN-A12; [Al-Monitor/Reuters, Vance](https://www.al-monitor.com/originals/2026/10/interview-us-vice-president-vance-says-iran-must-cut-enrichment-end-war).
- **Severity:** LOW.
- **Correction:**
  - OLD: `Vance softened the US nuclear ask from zero enrichment to a "meaningful" cut.`
  - NEW: `Vance said Iran must make a "meaningful" cut in enrichment capacity (Reuters, 6 October) — read by analysts as a softening from zero enrichment.`
  - OLD: `and Washington has rejected Iranian–Omani management of the strait.`
  - NEW: `and Washington has reportedly rejected Iranian–Omani management of the strait (The National).`
  - OLD: `This came a day after The Atlantic, the NYT and Axios reported`
  - NEW: `This came a day after The Atlantic, and on the same day as the NYT and Axios, reported`
  - OLD: `A second carrier group and about 10,000 sailors and Marines are en route.`
  - NEW: `A second carrier group and about 10,000 sailors and Marines are reported en route (Bloomberg, citing a US official).`

### Flag L7: Precision in the rates, Fed and gold lines
- **Issue:**
  - The "~17%" October-hike probability comes from a secondary note (Avalon) whose own subtitle says 64.2%. Reuters/CME had 21.6% on 8 Oct.
  - The drop in odds began with soft core PCE on 30 Sep, before payrolls.
  - "Most violent month since July" can be read as describing gold rather than the war.
- **Evidence:** intel MAC-A4.
- **Severity:** LOW.
- **Correction:**
  - OLD: `A 28 October hike went from about 73% priced to about 17% after payrolls of +29k.`
  - NEW: `A 28 October hike went from about 73% priced (23 September) to about 17–22% after soft core PCE (30 September) and payrolls of +29k (2 October).`
  - OLD: `fell 3.8% in the most violent month since July.`
  - NEW: `fell 3.8% in the war's most violent stretch since July.`

### Flag L8: "Hezbollah has not fired back"
- **Issue:** Intel ISR-A3 records one Hezbollah explosive drone at IDF troops in the window (no casualties). What is true is that there was no fire *into Israel*.
- **Severity:** LOW.
- **Correction:**
  - OLD: `Israel struck 370-plus Hezbollah targets in September, and Hezbollah has not fired back.`
  - NEW: `Israel struck 370-plus Hezbollah targets in September; Hezbollah has not fired into Israel (one explosive drone at IDF troops inside Lebanon, no casualties).`

### Flag L9: How the RBI package is described
- **Issue:**
  - The "20% cash reserve" is a **Foreign Exchange Risk Reserve**. Banks hold 20% of the rupee value with the RBI, only on eligible rupee derivative contracts above $2mn notional that hedge current-account exposure where the user buys foreign currency.
  - The package also bans rebooking of cancelled contracts.
  - The "strongest since 2013" line is Bloomberg's, per intel. I could not find it in BusinessToday's write-up, so keep it attributed.
- **Evidence:** [BusinessToday, 10 Oct](https://www.businesstoday.in/latest/economy/story/rbis-rupee-defence-special-dollar-window-for-oil-firms-tighter-forex-derivative-rules-560793-2026-10-10).
- **Severity:** LOW.
- **Correction:**
  - OLD: `It also imposed a **20% cash reserve on rupee derivatives** and cut the threshold for hedging without documents to $5mn — Bloomberg calls it the strongest action since 2013.`
  - NEW: `It also required banks to hold a **20% foreign-exchange risk reserve with the RBI on eligible rupee derivative contracts above $2mn**, banned rebooking of cancelled contracts, and cut the threshold for hedging without proof of exposure from $100mn to $5mn — Bloomberg calls it the strongest action since 2013.`

### Flag L10: Paraphrases in Section II (Goldman and Nagi)
- **Issue:**
  - Goldman puts *today's* risk premium at "a little over $20" and expects it to shrink more slowly than it had thought. Going from $104.5 to a $90 December average is about $15, not $20.
  - Goldman's $125 is a **2027 average** scenario.
  - Araghchi's mediation offer appears only in Iran's readout of the call; SPA's readout omits it.
- **Evidence:**
  - [Business Standard, 12 Oct](https://www.business-standard.com/amp/markets/news/goldman-ups-dec-26-oil-forecast-to-90-bbl-2027-worst-case-pegged-at-125-126101200190_1.html).
  - [MarketScreener](https://www.marketscreener.com/news/goldman-sees-brent-at-90-in-december-as-supply-risks-delay-price-relief-ce785ddcde8ff420).
  - intel SAU-A14.
- **Severity:** LOW.
- **Correction:**
  - OLD: `raised its December Brent average to **$90** (from $85), which implies about $20 of risk premium decaying in seven weeks. It sees $125 if Gulf output stays 5 mb/d short.`
  - NEW: `raised its December Brent average to **$90** (from $85). It puts today's risk premium at a little over $20 and expects it to shrink more slowly than it had thought; $90 implies about $15 off today's price in seven weeks. Its $125 case is a 2027 average if Gulf output stays 5 mb/d below pre-war levels.`
  - OLD: `or the Iran-facilitated talks Araghchi offered on 11 October,`
  - NEW: `or the Iran-facilitated talks Araghchi offered on 11 October (per Iran's readout; Riyadh's omits the offer),`

### Flag L11: Precision in "The Signal You Might Miss"
- **Issue:**
  - The ₹80k crore of FPI selling covers 1 Sep to about 9 Oct. That is about five weeks, not "the same" three weeks as the KOSPI move.
  - The 194bp spread is from about 8 Oct. Today it is about 213bp (7.37–7.38% against 5.24%).
  - A KOSPI "sidecar" is a five-minute pause on program selling, not a "market halt".
- **Severity:** LOW.
- **Correction:**
  - OLD: `a Korean market halt today — and **the money still did not come to India.** Foreigners sold about ₹80,000 crore of Indian equities over the same five weeks.`
  - NEW: `a KOSPI sidecar (a five-minute halt to program selling) today — and **the money still did not come to India.** Foreigners sold about ₹80,000 crore of Indian equities from 1 September to about 9 October.`
  - OLD: `has pushed the India–US yield spread to about 194bp, near a 22-year low.`
  - NEW: `pushed the India–US yield spread to about 194bp in early October, near a 22-year low (about 213bp today, after India's own yields rose).`

### Flag L12: Page 2 "1D" for HCLTech/TCS (and IOC/BPCL/HPCL) covers two sessions
- **Issue:** yfinance has no 12-Oct row for these NSE stocks, so the "1D" figure is measured against 9 Oct. Example: HCLTech ₹1,216.7 → ₹1,326 = +9.0%. Intel IND-A8 has HCLTech +6–8% on 13 Oct. The Nifty IT +5.2% is a true one-day change and is correct.
- **Severity:** LOW.
- **Correction:**
  - OLD: `| HCLTech / TCS (NSE) | ₹1,326 / ₹2,269.3 | +9.0% / +5.3% | — |`
  - NEW: `| HCLTech / TCS (NSE) | ₹1,326 / ₹2,269.3 | +9.0% / +5.3% vs 9 Oct (two sessions; no 12-Oct print) | — |`

### Flag L13: Details on the Yemen offensive and the Mecca Pact
- **Issue:**
  - Dawn of Yemen was announced on 4 Oct by Yemen's Saudi-backed government (the PLC) and launched on 5 Oct, with about 100 coalition jets in support. Al Jazeera dates the launch to 4 Oct.
  - Türkiye offers air defence, electronic warfare and technical support, and rules out troops for attacks. That is more than "air defence only".
- **Evidence:** intel SAU-A7 and SAU-B2; [Al Jazeera, 11 Oct](https://www.aljazeera.com/news/2026/10/11/yemen-fighting-expands-as-houthis-attack-saudi-airport-what-to-know); [Shafaq: "100 jets"](https://shafaq.com/en/Middle-East/Aden-100-jets-support-government-push-on-Sanaa).
- **Severity:** LOW.
- **Correction:**
  - OLD: `  - A Saudi-directed ground offensive, "Dawn of Yemen", began on 5 October with about 100 aircraft.`
  - NEW: `  - "Dawn of Yemen", a Yemeni government ground offensive under Saudi oversight, was announced on 4 October and launched on 5 October with about 100 Saudi-led coalition jets in support.`
  - OLD: `Pakistani forces are in the kingdom, and Türkiye is offering air defence only.`
  - NEW: `Pakistani forces are in the kingdom (Pakistan's military spokesman), and Türkiye offers air defence, electronic warfare and technical support but no troops for attacks.`

### Flag L14: Completeness — the helium cascade is missing from Section III
- **Issue:**
  - The changelog keeps the helium buffer-depletion trigger "clock running" and calls Qatar's October LNG collapse (0.6 Mt) a "negative read-through". Qatar's LNG trains produce helium as a by-product.
  - Section III does not mention it. This is the 29 March failure mode.
  - Section I balance is fine: 4 geopolitical and 3 market/macro items. Section II has three market voices.
- **Severity:** LOW.
- **Correction:**
  - OLD: `- Europe's winter gas.`
  - NEW: `- Europe's winter gas.\n- Helium: no price print since 31 August, but Qatar's October LNG collapse (0.6 Mt tracked) cuts by-product helium supply; the graph's Q4 buffer-depletion clock is running.`

---

## Items That Passed

### Riyadh airport toll and closure (PASS)
- **Action or rhetoric?** Confirmed action.
  - 12 killed and 309 injured on 10 Oct (GACA). An Indian national died on 11 Oct, which the Indian Embassy confirmed and AIR reported as "death toll rises to 13".
  - Three Indians were in ICU.
  - GACA's cumulative count for 6–11 Oct is 20 dead and 356 injured, carried in a Yahoo/AP live blog citing GACA.
  - The NOTAM closes KKIA to 17 Oct.
- **Sources:** [Al Jazeera 10 Oct](https://www.aljazeera.com/news/2026/10/10/attack-on-airport-in-saudi-capital-riyadh-leaves-several-injured), [Arab News PK](https://www.arabnews.pk/saudi-arabia/riyadh-hospitals-treating-309-injured-in-deadly-airport-attack-3003843), [Gulf News: Indian death](https://gulfnews.com/world/asia/india/indian-national-injured-in-riyadh-airport-attack-dies-embassy-confirms-1.500706712), [News on AIR](https://newsonair.gov.in/indian-national-dies-after-riyadh-airport-attack-death-toll-rises-to-13/), [Yahoo: 20 killed](https://www.yahoo.com/news/politics/articles/iran-live-updates-trump-says-164343032.html). These are independent.
- **Other side:** the Houthis claimed the attack ([France 24](https://www.france24.com/en/middle-east/20261011-live-saudi-arabia-vows-decisive-response-after-deadly-houthi-strike-on-riyadh-airport)). The brief should say so; see H1.
- **Language:** "deadliest in more than a decade" is Reuters' wording. Matches.

### The Mecca Pact was activated on 5 Oct (PASS)
- **What happened:** a confirmed action. After an emergency meeting in Riyadh, Khalid bin Salman posted on X, and Pakistan's joint statement backed "rapid deployment" of forces.
- **Sources:** [Al Jazeera](https://www.aljazeera.com/news/2026/10/6/pakistan-turkiye-join-saudi-deterrence-against-houthis-what-that-means), [The Week](https://www.theweek.in/news/middle-east/2026/10/06/pakistan-saudi-arabia-turkey-makkah-defence-alliance-against-houthi-attacks.html), [Tribune India](https://www.tribuneindia.com/news/collective-defence/mecca-pact-invoked-amid-houthi-attacks-turkiye-pakistan-agree-to-swiftly-deploy-forces-military-capabilities-in-saudi-arabia).
- **Caveats the brief handles:** the statement does not name the Houthis, and force sizes are unspecified.

### "AFP: Mayun still Houthi-held" (PASS)
- Yemeni government military sources told AFP that Mayun "remained in Houthi hands" and that the waterway was not secured ([L'Orient/AFP](https://today.lorientlejour.com/article/1550349/government-forces-say-advancing-against-houthis-around-bab-al-mandeb)).
- The brief correctly treats the Saudi media victory claims as unverified.

### No US strike on the Houthis; Bukhaiti's threat (PASS)
- "We may. We're going to look at it" is rhetoric, and the brief presents it as such ([Al Jazeera 11 Oct](https://www.aljazeera.com/news/2026/10/11/yemen-fighting-expands-as-houthis-attack-saudi-airport-what-to-know)).
- "Intelligence and targeting, no strikes" matches AP (12 Oct) via intel SAU-A9.

### Individual Hormuz incidents (PASS)
- **Six on 11 Oct** (five tankers and a container ship; UKMTO 165–169 plus one earlier): [gCaptain, 12 Oct](https://gcaptain.com/new-reports-reveal-five-more-ships-hit-near-hormuz/).
- **Cape Dao, 23 Sep:** wiper Suraj Yadav killed; "unknown projectile"; no claim by either side ([gCaptain](https://gcaptain.com/seafarer-killed-in-hormuz-attack-as-trump-pushes-iran-deal-at-un/), [The National](https://www.thenationalnews.com/news/gulf/2026/09/24/indian-sailor-killed-as-two-torpedoes-hit-merchant-ship-off-oman/)).
- **Petro Dolphin, Sohar:** 2 Indians missing; 9 of 11 rescued; confirmed by Shipping Minister Sonowal ([Gulf News](https://gulfnews.com/world/asia/india/two-indian-seafarers-missing-after-vessel-hit-by-drone-in-strait-of-hormuz-1.500706843), [Arab News PK](https://www.arabnews.pk/middle-east/two-indian-sailors-missing-after-vessel-attacked-off-oman-3003865)).
- **The ~25 tally** is defensible as the brief's own labelled count. The KIN-A1 named incidents and the weekly counters add up to about 25–28; delayed UKMTO reports make an exact figure impossible, and the brief says so.

### Saudi pipeline restart and Aramco allocations (PASS)
- **5.8 mb/d:** the energy minister said this on the record on 6 Oct ([Al Jazeera](https://www.aljazeera.com/news/2026/10/6/saudi-arabia-says-east-west-pipeline-pumping-5-8-million-bpd), [Argus](https://www.argusmedia.com/pt/news-and-insights/latest-market-news/2887089-saudi-east-west-pipeline-at-5.8mn-b-d-energy-minister)). Argus notes it is the first official figure and that there is no damage assessment. The brief attributes it with "says", which is correct.
- **Europe:** full November allocations ([Newsquawk](https://www.newsquawk.com/headlines/saudi-aramco-is-going-to-supply-full-oil-volumes-to-european-customers-in-november)).
- **Iran's exports:** zero crude loadings in September, from Bloomberg tracking with Kpler and Vortexa agreeing ([Shafaq](https://shafaq.com/en/Middle-East/Iran-crude-loadings-fall-to-zero-in-September)).

### India data (PASS)
- **RBI:** raised the repo 25bp to 5.50% on 7 Oct, unanimously, with the "calibrated tightening" stance passed by majority ([Republic](https://www.republicworld.com/business/rbi-hikes-repo-rate-by-25-bps-to-550-signals-shift-to-calibrated-tightening-2026-10-07-138423), [Moneylife](https://www.moneylife.in/article/repo-rate-raised-to-550-percentage-by-rbi-amid-challenging-global-uncertainty-inflation/81869.html)).
- **CPI:** 5.54% for September, with food at 7.74% and onion at 108.09% ([BusinessToday](https://www.businesstoday.in/latest/economy/story/indias-retail-inflation-rises-to-5-54-in-september-food-inflation-hits-7-74-561057-2026-10-12), [Zee Biz](https://www.zeebiz.com/economy-infra/news-cpi-data-september-2026-retail-inflation-rises-to-554-on-higher-food-prices-rural-inflation-at-608-403779)).
- **FPI:** −₹35,861 crore in September ([Finnovate/NSDL](https://www.finnovate.in/learn/blog/fpi-flows-september-2026-sector-wise-investment)).
- **Reserves:** $734.61bn in the week to 2 Oct ([DTNext](https://www.dtnext.in/news/business/forex-reserves-drop-by-usd-12952-bn-to-usd-73461-bn)). The −$18.3bn fall in the week to 25 Sep was called the "largest weekly fall on record" by [JM Financial](https://www.jmfinancialservices.in/market-news-and-insights/1735026), and Bloomberg is cited in intel.
- **Rupee:** closed 96.73 on 9 Oct, with the all-time low at 96.96 (Khaleej Times/Reuters).
- **OMC dollar window and $5mn threshold:** confirmed by BusinessToday and [Khaleej Times](https://www.khaleejtimes.com/markets/india-central-bank-support-rupee-opens-dollar-window-oil-companies).

### US–Iran diplomacy (PASS, apart from H4, L5 and L6)
- **New York contact:** Witkoff/Kushner with Araghchi, mediated by Qatar and Pakistan; Witkoff wrote "through the mediators, who shuttled" ([Ynet/NYT](https://www.ynetnews.com/article/c5h38l8ag)).
- **Trump's 8-Oct pledge:** the exact text is confirmed ([The National](https://www.thenationalnews.com/news/us/2026/10/08/trump-rules-out-attack-on-iran-before-midterm-elections/), [Colorado Politics](https://www.coloradopolitics.com/2026/10/08/trump-pledges-not-to-attack-iran-before-midterm-elections/)).
- **Rezaei on 11 Oct:** "insufficient", "accepted some", "no longer in the process of responding" ([Tribune India](https://www.tribuneindia.com/news/world/response-inadequate-iran-claims-us-agreed-to-some-of-its-seven-conditions/), [gCaptain/Reuters](https://gcaptain.com/iran-says-us-response-to-its-proposal-to-reopen-hormuz-was-insufficient/)). The brief correctly marks "accepted some" as one side's claim, and the White House did not comment.
- **Vance quote on 6 Oct** is confirmed, and Iran's response is present.

### Macro (PASS)
- **ECB:** hiked to a 2.50% deposit rate on 10 Sep, its second hike of 2026 ([Nation Thailand](https://www.nationthailand.com/news/world/40070896), [fnnews](https://en.fnnews.com/news/202609102128479847)). The baseline correction is right.
- **US 10Y "highest since 2002":** Bloomberg says the 10Y broke its 2007 peak on 1 Oct (5.34%) ([BGOV](https://news.bgov.com/insurance/treasury-10-year-yield-hits-highest-since-2002-on-rate-outlook)). yfinance ^TNX shows a 7-Oct high of 5.364, with 13 closes above 5% since 23 Sep. The "5.35–5.37% on 7 Oct" is consistent.
- **Channel 12's "within three weeks"** and Israel's 27-Oct election ([Times of Israel](https://www.timesofisrael.com/trump-says-us-wont-hit-iran-this-month-as-zamir-said-to-warn-strike-could-delay-israels-election/)). It is correctly marked as single-source.
- **Goldman December $90** is confirmed; see L10 for the framing.

### Balance (PASS)
- **Section I:** 4 geopolitical items and 3 market/macro items. Oil, India and rates are each a full item.
- **Section II:** includes Goldman/EIA, ETI/Clarksons freight and Indian sell-side alongside the geopolitical analysts.
- **Section III:** covers TTF, Brent, the 10Y, the ECB, India and defence equities, not only military edges. Helium is missing (L14).
- **Graph completeness:** 62 of 63 nodes are stamped 2026-10-13. Every node that the staging files list as affected was updated.

---

## Trigger Point Review

| Trigger | Status in changelog | My assessment | Agreement? |
|---|---|---|---|
| saudi-arabia: escalates alone / Mecca Pact by ~5 Oct | FIRED (both legs) | Pact activation confirmed by several independent sources (Saudi defence minister on X, Pakistan joint statement, Al Jazeera, The Week). Sanaa strikes from 1 Oct: AFP via intel; the coalition confirmed Sanaa targets on 6 Oct. Either leg alone is enough. | ✅ AGREE |
| saudi-arabia: East-West RESTART | FIRED | The minister's 5.8 mb/d is on the record (Al Jazeera, Argus), and tracker data points the same way. | ✅ AGREE |
| houthis: Mecca forensic OR 2nd holy-city incident | FIRED (leg 2, attribution CLAIMED) | The event and the attribution come from the coalition alone, with an unpublished wreckage. The Houthis deny it and exempted the Mecca and Medina airports. The leg's wording is "interception", and this was a claimed hit. It fails the 2-independent-sources rule. | ❌ DISAGREE — hold at watching (tested on claim). See C1. |
| red-sea: ≥2% (Lloyd's/Marsh) OR liner suspension | FIRED (split) | The ≥2% figures are broker quotes for Saudi port calls, not a Red Sea transit print and not from Lloyd's/Marsh. Neutral transit is 0.2–0.3%. Liners expanded service. The trigger's own design question ("is the pledge believed?") resolves "believed". | ❌ DISAGREE — not fired. See H7. |
| strait-of-hormuz: ENFORCEMENT on neutral vessel | ACTIVE, "re-confirmed WITH attribution" | Status ACTIVE is fine: it has been active since 26 Jun on Windward-corroborated turn-backs, and UKMTO has verified many strikes on neutral hulls. A UKMTO-reported IRGC hail-and-turn-back (~4 Oct) is the better re-confirmation. The "with attribution" label rests on IRGC claims (which the trigger text excludes; one was shown false), Sayyari's general statement (mis-titled, with no stated target) and US-led JMIC (REPORTED). | ⚠️ AGREE on status / ❌ DISAGREE on the "attributed" label. See H3. |
| iran: restricted zone beyond the strait | watching (tested) | The Sohar strike was UKMTO-verified but nobody attributed it. Correctly held. | ✅ AGREE |
| iran: US–Iran meeting convenes (named venue + negotiators) | FIRED (proximity) | Both governments confirm talks: Witkoff on X, Trump, IRIB, and Rezaei saying Araghchi was authorised. The venue and negotiators are named. Proximity format is recorded as a caveat. A confirmed action. | ✅ AGREE (keep the "indirect/proximity" caveat) |
| iran: accepts direct talks publicly | watching | Correct: conditions were passed through mediators. | ✅ AGREE |
| iran: Pezeshkian endorsed or sidelined | RESOLVED ("absorbed") | Reasonable on the DIP-A4 evidence. | ✅ AGREE |
| united-states: Trump–GCC published framework | RESOLVED (no document) | No text was found by several outlets. | ✅ AGREE |
| united-states: strike on Houthi positions | watching | "We may" is rhetoric. | ✅ AGREE |
| china: Trump–Xi Iran/Hormuz commitment | RESOLVED (no commitment) | REPORTED from the readouts. | ✅ AGREE |
| houthis: first attack on a non-Saudi hull | watching | No UKMTO-attributed Houthi attack. The Chrystal Sky near-miss was not attributed. | ✅ AGREE |
| brent-crude: >$100 sustained 2+ weeks | FIRED (front-month) | yfinance: 14 consecutive front-month settles at or above $100.20, 23 Sep–12 Oct. On the December contract like-for-like, 8 settles to 12 Oct; it completes two weeks around 14 Oct if it holds (it is at $104.65 now). This is market data and the standard convention, with the caveat recorded. | ✅ AGREE |
| marine-war-risk-insurance: print above Marsh 2–6% | FIRED | Reuters (25 Sep) 6–9% and FT (Oct) 6–10%, two independent reports. The lower bound only touches 6%, so this is "above" at the midpoint and upper end. | ✅ AGREE (marginal) |
| marine-war-risk-insurance: dated Gulf print | RESOLVED (between bands) | Correct. | ✅ AGREE |
| us-10y-yield: crosses 5% | FIRED (13 closes) | Verified with yfinance: closes above 5% every session 23 Sep–9 Oct. | ✅ AGREE |
| ecb: September hike | FIRED (retro, 10 Sep) | Verified independently. | ✅ AGREE |
| european-ttf-gas: >€70 ×5 | RE-ACTIVATED | yfinance: closes above €70 every session since 30 Sep (9 sessions); 29 Sep was €69.81. | ✅ AGREE |
| defense-sector: ITA <$208 ×3 | FIRED (price) | Verified: 203.60 / 204.88 / 206.65 / 206.03 on 7–12 Oct. | ✅ AGREE |
| fertilizer-urea: DAP >$900 through August | RESOLVED (met) | Not independently checked. Rests on intel/markets data. | ✅ AGREE (unchecked) |
| india: CPI ≥5% OR RBI hikes 7 Oct | FIRED (leg 2) | The RBI hike is verified. | ✅ AGREE |
| india/fii-flows: FPI >₹25k cr in September | FIRED | −₹35,861 cr (NSDL) verified. | ✅ AGREE |
| rbi: 7-Oct MPC hike or hawkish hold | FIRED | Verified. | ✅ AGREE |
| rbi: direct INR intervention | FIRED (in substance) | OMC dollar window from reserves, verified (BusinessToday, Khaleej Times). A confirmed policy action. | ✅ AGREE |
| inr-usd: 96.60 held 3+ sessions | RESOLVED (re-anchored to 96.96) | The level was met 7–9 Oct, the record held, and the RBI reversed the move. A sensible resolution. | ✅ AGREE |
| nifty-50: <22,000 | watching | Low was 22,231.80, verified. | ✅ AGREE |
| fed: 2nd hike 28 Oct / pause needs Brent fall | watching, premise falsified | A hold is priced (~78–83%) with Brent higher. The rewrite is sensible. | ✅ AGREE |
| israel: Ch12/Haaretz imminent-strike prep | not re-fired (near-miss) | A US instruction that the President contradicted the same day. Correct. | ✅ AGREE |

**Edge weights:**
- The changes are proportionate. `houthis→saudi-arabia` +1.0 rests on confirmed mass-casualty strikes. `saudi-arabia→european-ttf-gas` was cut on the data. The +0.5 moves on `russia→brent-crude` and `uae→saudi-arabia` are modest, as they should be for a mix of rhetoric and action.
- No edge was raised on Sayyari's statement or on the holy-city leg.
- No objection to any edge.

---

## Market Data Spot-Check
yfinance, pulled about 17:15 IST on 13 Oct.

| Data point | Brief value | Verified value | Match? |
|---|---|---|---|
| Brent Dec (front), today | $104.50 (−2.0%) | $104.65 live (−1.9%) | ✅ (live drift) |
| Brent 12-Oct settle | $106.65 | 106.65 | ✅ |
| Front-month settles >$100 | 14 (23 Sep–12 Oct) | 14, minimum $100.20 (7 Oct) | ✅ |
| Brent Dec on 22 Sep (like-for-like base) | $95.41 | 95.41 | ✅ |
| Window intraday low | $97.06 (6 Oct) | $96.56 (1 Oct); $97.08 (6 Oct) | ❌ minor (L3) |
| WTI Nov | $91.86 | $91.89 | ✅ |
| Nifty 50 close | 22,721.95 (+1.6%) | 22,721.95 | ✅ |
| Nifty 8-Oct low close | 22,231.80 | 22,231.80 | ✅ |
| Sensex / Bank Nifty | 73,033.78 / 55,481.05 | 73,033.78 / 55,481.05 | ✅ |
| Nifty IT 1D | +5.2% | +5.22% (29,830.10 vs 28,349.60) | ✅ |
| India VIX | 14.12 (−7.4%) | 14.12 (vs 15.25) | ✅ |
| KOSPI close | 6,035.35 (−5.46%); AP −7.4% = intraday low | 6,035.35; low 5,911.11 (−7.41%) | ✅ |
| KOSPI since 22 Sep | −13.9% | −13.88% vs 7,007.72 | ✅ |
| Samsung / SK hynix | ₩232,000 / ₩1,443,000 | 232,000 / 1,443,000 | ✅ |
| Gold Dec | $4,207.70; −3.8% since 22 Sep | $4,204.4; −3.9% vs 4,376.4 | ✅ |
| US 10Y (9 Oct) | 5.24% | 5.244 | ✅ |
| US 10Y 7-Oct intraday | 5.35–5.37% | 5.364 high | ✅ |
| US 30Y | 5.60% | 5.60 | ✅ |
| USD/INR | ~95.3 (95.27) | 95.28 | ✅ |
| TTF | €86.65 | €85.99 live (open 86.65; 12 Oct 84.35) | ✅ (live drift) |
| VIX (12 Oct) | 15.21 | 15.21 | ✅ |
| DXY | 102.32 | 102.30 | ✅ |
| ITA / FRO / SMH (12 Oct) | 206.03 / 59.19 / 590.99 | 206.03 / 59.19 / 590.99 | ✅ |
| LMT / NOC since 22 Sep | −4.4% / −7.9% | −4.39% / −7.91% | ✅ |
| EEM | 66.15 (−3.9%) | 66.15 (−3.9%) | ✅ |
| RBOB roll | Dec $3.11 vs Nov like-for-like | RB=F 3.12 on 13 Oct (rolled) | ✅ |
| Sugar / corn / wheat since 22 Sep | +19.0% / −11.5% / −8.0% | +19.5% / −11.4% / −7.9% | ✅ |
| HCLTech / TCS 1D | +9.0% / +5.3% | vs 9 Oct (no 12-Oct row) | ⚠️ two-session (L12) |

**Data I could not independently confirm (all REPORTED in intel):**
- TD3C at $1,412,594/day. Search found WS1,140 = $1.21m earlier in the window; scaling to WS1,318.75 gives about $1.40m, so it is plausible.
- Eurasia Group's 35%.
- CME's "17%".
- India 10Y at about 7.40%.
- October FPI −₹44,166 cr.
- EIA's Q4 forecast of $104.69.
- The FAA NOTAM to 10 Dec.
- Hurricane Isaias' 72%.

---

## Final Verdict

**APPROVED WITH CORRECTIONS.**

The brief's factual core is sound. Casualty figures, Mecca Pact activation, the Hormuz incidents, Saudi pipeline flows, all India data, the ECB correction, the US 10Y record and every headline market number checked out against independent sources and live data.

Its weaknesses are in framing:
- Two Section I headlines are wrong. The Saudi–Houthi sequence is inverted, and the Hormuz "quintupled" compares counts over windows of different length.
- A third headline says more than the brief's own data on war and US rates.
- The Hormuz attribution leans on a mis-titled, undefined Iranian statement as an "admission".
- The Gharibabadi date is off by a day.
- The Aramco causal chain is reversed.

In the graph, two triggers should be held rather than fired:
- the Houthi holy-city trigger, which rests on a coalition claim the Houthis deny;
- the Red Sea war-risk trigger, where the premium is a Saudi port-call quote, not a transit print.

None of this changes the deployment call ("defensive — do not add"). Apply C1 and H1–H7 before publishing. The LOW flags are optional, but each is a mechanical swap of one string.

If the corrections are applied, the suggested footer is: `*Verified: 7 Section I items (~55 claims), 8 Section II blocks, 21 trigger changes checked; 22 flags (1 critical, 7 high, 14 low); corrections applied as listed in briefs/2026-10-13-morning-verification.md*`

**Basis:**
- Ran yfinance on 30 tickers.
- Read the brief, intel.md (synthesis and the KIN, SAU, DIP, IND, MAC and ISR items), markets.md, graph-changelog.md, and three node trigger blocks.
- Sourced about 45 web searches and fetches; the URLs are above.

**Not checked:**
- Primary UKMTO or JMIC documents (paywalled or blocked).
- The Bloomberg "strongest since 2013" line.
- The figures listed under "Data I could not independently confirm".
- Whether any Houthi statement specifically names the 10-Oct terminal strike: France 24 reports a claim, Al Jazeera only a general one.

**Confidence:** high on the market data, the dates and the titles; moderate on the trigger judgments, which involve interpretation of trigger texts.
