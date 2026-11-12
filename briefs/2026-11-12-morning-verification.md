# Verification Report — 12 November 2026 (Day 258), morning edition
Generated: ~11:17–11:25 IST Thu 12 Nov 2026 (CoS correction from the file mtime, 11:25:07 IST; the report's own "11:35" end time was ahead of the clock) | Fact-Checker: Red Team
Brief checked: `staging/2026-11-12-morning/brief_draft.md` (draft; not yet in `briefs/`)

## Summary
- **Checked:** the header corrections; 7 Section I items plus "What held"; 4 new calls and the 7-row scorecard; source tone; Cascade Watch (1 expiry, 3 tested/closest rulings, 2 new watches, edges); the Signal; Risk Landscape; Deployment, the hold rule and the recommendation list (word for word against 11 Nov); dated tells; ~95 Page 2 figures, re-pulled from yfinance at 11:16–11:20 IST plus the CoS FRED and Treasury files.
- **Flags: 0 CRITICAL, 5 HIGH, 15 LOW.** Graph corrections: 3.
- **Market data:** clean. Every settle, close and percentage I recomputed matches, including the Jan–Dec27 spread ($13.83), the Fed odds (27.5bp, ~10%), the "first war-era close above pre-war" claim, and TAIEX −2.7% at 10:45 IST. One trivial copper mismatch (L14).
- **The lead holds.** The quotes match the desk record. The Europe-bases conditions are kept. Ghalibaf's Oman and Putin claims are labelled as claims. **"The same minute" is supported:** Tasnim's stamp is 12:44 Tehran (09:14 UTC), and the 1-minute bar opening at 09:14 UTC is the first to move (91.58 close at 09:13, then O 91.67 / H 91.88; WTI volume jumps from 92 to 425 in the same bar). Reuters' link is attributed, not asserted. The weakness is what the brief leaves out: the CoS header says "not new in substance", and the brief drops that, then calls Iran's terms "hardened" (H1).
- **Pattern, as in every brief since 8 Nov:** the HIGHs are in CoS framing lines (the Signal's hold-rule claim, "Iran's terms hardened") and in paraphrase drift (Eisenkot, "hit"), not in desk facts.

---

## Flags

### H1. HIGH: the lead does not say the two headline lines repeat earlier positions, and the deployment case calls them "hardened"
- **Brief text:**
  - The lead headline: "Iran's security chief said 'not a single particle' of its enriched uranium will leave the country, and the parliament speaker said Hormuz will 'never return' to its pre-war state."
  - The case against: "…Iran's terms hardened…".
  - Risk Landscape: "Rising, but only talk: Iran's terms (uranium stays; Hormuz 'never return'…)".
- **Issue:** the CoS header (DIP-A1) says Rezaei's uranium line is "**Not new in substance**: a similar Rezaei statement on 20 Oct". It also notes that Baghaei earlier said removal is "by no means" under consideration. On Hormuz, a JNS story dated 23 June is headlined "Tehran's chief negotiator: Strait of Hormuz won't return to pre-war status" (its headline wording; I re-found the page). Ghalibaf's "The ball is now in the American court" is his 3-Nov line, and our 3-Nov brief printed it. These are new statements of standing positions. "Hardened" in a line the reader acts on overstates the change. Our memory rule on Signal overreach applies.
- **Evidence:** intel.md CoS header line 39 and DIP-A1 ("Not new in substance"); JNS, 23 June (headline); `briefs/2026-11-03-morning.md` line 114.
- **Replacement:**
  - Add as the last bullet under "The words": "**Not new in substance:** Rezaei made a similar statement on 20 October (search summary, not opened), and Ghalibaf has said since June that the strait will not return to its pre-war state. What is new is the setting: a US talks report on the same day."
  - In the case against, replace "Iran's terms hardened" with "Iran restated its hardest terms in public".
  - In Risk Landscape, replace "Rising, but only talk: Iran's terms" with "Restated, only talk: Iran's terms".
- **Applied:** Yes (CoS, 11:27 IST).

### H2. HIGH: the Signal's "would not reset on an Israeli strike" rests on an incomplete list of resets
- **Brief text:**
  - The Signal's headline: "Our hold rule would not reset on an Israeli strike."
  - "Why it matters for capital: the hold rule resets on a US-owned strike, three straight nights of reported strikes, a declared US campaign, or confirmed Iranian fire on Oman. **A single Israeli strike on Iran meets none of these.**"
  - Deployment: "Resets: a US-owned strike, a declared campaign or confirmed Iranian fire on Oman."
- **Issue:** the hold rule is "no further **qualifying** strike", and "qualifying" means the `united-states` "RESUME" definition (9-Nov verification, H6). That definition has four legs: (a) a strike the US government acknowledges; (b) strikes on 3+ consecutive nights; (c) strikes on several sites in one night, or on targets beyond the air-defence/launcher pattern, reported by 2+ outlets with their own officials; (d) a strike on nuclear, energy or leadership targets. The 9-Nov verification tested night six against legs (c) and (d). The 10- and 11-Nov lists dropped them; the 11-Nov check agreed with the shorter list and missed this. Legs (b), (c) and (d) need **no US ownership**. They count *US* strikes, but they are judged on reporting.
  - A strike that is reported as Israel's alone meets none of the legs. Read that narrowly, the sentence is right.
  - If Iran blames the US as well (its usual "American-Zionist" framing), a single night's strike on several sites, or on a nuclear, energy or leadership target, could qualify under (c) or (d). The 7-Nov night was the precedent for ruling on reported US involvement.
  - The Signal's headline is therefore stronger than the rule allows. The deployment "Resets" line is also incomplete: it leaves out leg (b), although the "Strikes" line above covers it.
- **Evidence:** `graph/nodes/united-states.json`, the "RESUME 4–30 Nov" condition text; `briefs/2026-11-09-morning-verification.md` lines 76 and 193; `briefs/2026-11-11-morning.md` line 181.
- **Replacement:**
  - Signal headline: "**Israel's cabinet meets on Sunday, the day after our 14-November test. As written, our hold rule would not reset on a strike that is Israel's alone.**"
  - Why it matters: "**Why it matters for capital:** the hold rule resets on a qualifying US strike (one Washington owns; three straight nights of reported strikes; several sites in one night, or targets beyond the air-defence pattern; or a nuclear, energy or leadership target), a declared campaign, or confirmed Iranian fire on Oman. **A strike reported as Israel's alone meets none of these. One that Iran also blames on the US, on several sites or on a nuclear, energy or leadership target, would need a ruling.** **For your decision, not applied:** add 'a confirmed Israeli strike on Iranian territory' as a reset."
  - Deployment: "**Resets:** a qualifying US strike (any of the four legs above, including three straight nights), a declared campaign or confirmed Iranian fire on Oman. None is met."
- **Applied:** Yes (CoS).

### H3. HIGH: Eisenkot's letter is paraphrased as something it did not say
- **Brief text:**
  - Section I: "Gadi Eisenkot, who holds the mandate to form a government, wrote to Netanyahu and the attorney-general **asking that any operational action be properly approved**."
  - The Signal: "Eisenkot wants any action properly approved."
- **Issue:** no desk text supports "properly approved". The record (ISR-A1; desk bottom line):
  - To Netanyahu: "Exercise restraint and caution against dangerous moves that can wait until a new government" (JPost), and "I demand that you act with national responsibility during this sensitive period" (ToI).
  - To the attorney-general: a request for "regular, structured, and comprehensive security briefings".
  - ToI says the letter "does not mention Iran". JPost's headline ties it to Iran ("urges… restraint on Iran, demands briefings").
  - Approval procedure is Ynet's Section 40 point, not Eisenkot's. The mandate detail is supported (ISR-A4: 28 days "from Sunday").
- **Evidence:** intel.md ISR-A1 and line 137; research/04 line 214. A web search found only an October Eisenkot item about Zamir; the November letter was not re-found.
- **Replacement:**
  - Section I: "**Gadi Eisenkot,** who holds the mandate to form a government, urged Netanyahu to 'exercise restraint and caution against dangerous moves that can wait until a new government', and asked the attorney-general for regular security briefings (JPost; ToI says the letter does not name Iran)."
  - The Signal: "Eisenkot urged restraint until a new government."
- **Applied:** Yes (CoS).

### H4. HIGH: "hit" upgrades NCC Fajr's "possible attack", against the brief's own ruling
- **Brief text:** "**This is the second Gulf tanker with Indian crew hit in two days,** after Tuesday's *Fujairah Energy*."
- **Issue:** the only on-record source, India's shipping minister, says the ship "was involved in a possible attack". Damage is unconfirmed, no UKMTO notice names it, and iMariner marks it "claimed". Cascade Watch refuses to fire the blacklist trigger because "'possible attack' is not a confirmed strike". The same brief cannot then call it "hit". The IND desk's "was hit" wording carried through into the brief (tag drift, REPORTED → CONFIRMED).
- **Evidence:** KIN-A3; IND-B1; CoS header trigger call. *Fujairah Energy* was hit (India: a projectile), so the comparison only needs a different verb.
- **Replacement:** "**This is the second Gulf tanker with Indian crew caught up in an attack or possible attack in two days,** after Tuesday's *Fujairah Energy*, which India said a projectile hit."
- **Applied:** Yes. Graph: G1 applied.

### H5. HIGH: Didamar is presented without the Omani denial we printed on 11 November
- **Brief text:** "**Oman (reported):** three unnamed sources told Reuters that Iran attacked ship-navigation equipment on Oman's Didamar island. Reuters could not confirm whether anything was destroyed, and Oman has said nothing on the record."
- **Issue:** this fails the both-sides check. Our 11-Nov brief reported that "an unnamed senior Omani official told Maritime Executive the navigation aids there 'had not been struck'". KIN-A6 says "the 10-Nov Omani denial (MarEx) still stands". "Oman has said nothing on the record" is literally true, but it hides the only Omani voice we have, and that voice disagrees. The two accounts can both be true (an attack with no hit), and the reader should see both. The hold-rule line ("Reuters' unnamed sources say Iran attacked Didamar, but no one has confirmed damage") has the same gap.
- **Evidence:** `briefs/2026-11-11-morning.md` line 90; KIN-A6.
- **Replacement:** "…Reuters could not confirm whether anything was destroyed. On Tuesday, an unnamed senior Omani official told Maritime Executive that the aids 'had not been struck'. Oman has said nothing on the record." In the hold rule: "Oman: Reuters' unnamed sources say Iran attacked Didamar; an unnamed Omani official says the aids were not struck; no one has confirmed damage."
- **Applied:** Yes (CoS).

### L1. LOW: Page 2 says Tasnim "first published" the line
- **Brief text (Significant Moves, Brent 14:44–14:49 IST row):** "Began the minute Tasnim first published Rezaei's line".
- **Issue:** Section I correctly says "the first publication… **that we found**". DIP notes that Al Mayadeen's own release "must come before 09:14 UTC". The table drops the qualifier.
- **Replacement:** "Began in the minute of the first publication we found (Tasnim, 14:44 IST); Reuters ties the day's rise to the line".

### L2. LOW: the lead headline is stronger than Kan
- **Brief text:** "…after a report that the army was told to ready itself for a strike."
- **Issue:** Kan's headline (our translation) says "increase readiness toward a strike". "Ready itself for a strike" sits close to the relay wording ("orders army to prepare") that the brief itself warns against.
- **Replacement:** "…after a report that the army was told to raise its readiness for a possible strike."

### L3. LOW: 23:58 IST is the first relay, not Kan's own time
- **Brief text:** "Kan… reported late on Wednesday (23:58 IST)".
- **Replacement:** "Kan… reported late on Wednesday (first relay we found: 23:58 IST; Kan's page was unreadable)".

### L4. LOW: Ynet's 4-October decision is merged with Kan's order
- **Brief text:** "**Ynet:** the readiness order dates from the cabinet's last decision, on 4 October."
- **Issue:** Ynet says the 4-Oct decision "raised readiness for Iran scenarios, including an Israeli strike or an Iranian surprise attack". Zman's paraphrase of Kan says the instruction came "over the past month", and AA dates the last meeting to 5 Oct. Whether these are the same order is our inference.
- **Replacement:** "**Ynet:** the cabinet's last decision, on 4 October, 'raised readiness for Iran scenarios, including an Israeli strike or an Iranian surprise attack'. Ynet does not say whether that is the order Kan describes."

### L5. LOW: "could" is placed inside a translated quote
- **Brief text:** "…which he thinks '**could** ignite another round of fighting'."
- **Issue:** ISR-A1 quotes only "ignite another round of fighting". The words are N12/mako's account of Zamir's view, translated, not Zamir's own.
- **Replacement:** "Channel 12: army chief Zamir again opposes the prime minister's proposed steps, which it says he sees as liable to 'ignite another round of fighting'."

### L6. LOW: an active trigger is listed as "Closest, not fired"
- **Brief text:** under "Closest, not fired": "`israel`: the Channel 12/13 or Haaretz imminent-strike watch."
- **Issue:** this trigger's status is **active** (a standing trigger since April). The CoS ruling is "stays ACTIVE, not re-fired".
- **Replacement:** move it under its own label: "**Standing, not re-fired:** `israel`, the Channel 12/13 or Haaretz imminent-strike trigger (active). Kan is outside…"

### L7. LOW: "widest in days" is our superlative, attributed to Saudi Arabia
- **Brief text:** "Saudi Arabia reported its widest Houthi barrage in days, all shot down."
- **Issue:** this is the SAU desk's own judgement, with no comparison in the record. Saudi Arabia did not say it. The 10-Nov count was three missiles and a drone, so the claim is plausible.
- **Replacement:** "Saudi Arabia reported seven Houthi missiles and drones in one day, the most in days on our count, all shot down."

### L8. LOW: the 36 km distance is unattributed in the headline
- **Brief text (headline):** "Missile debris fell in the Mecca region, 36 km from the Grand Mosque."
- **Issue:** this is Sabq's straight-line estimate; Reuters' figures via search summary are 21–35 km. The body attributes it correctly.
- **Replacement:** "…about 36 km from the Grand Mosque (Sabq)."

### L9. LOW: "Saudi Arabia's state shipping company" and "a Saudi state fleet's ship… sailed with US support"
- **Brief text:** "Bahri is Saudi Arabia's state shipping company." Also, in the case against: "the ship war reached a Saudi state fleet's ship the day after it sailed with US support".
- **Issue:** no desk file sources "state". Bahri is listed, and large stakes are held by the PIF and Aramco (my background knowledge, not checked today). KIN says "with US government support" is a paraphrase; Bloomberg's headline says "With US Military Coordination". NCC Fajr is owned by National Chemical Carriers and is not shown to be one of the four ships Bahri sent through on 10 Nov.
- **Replacement:** "Bahri is Saudi Arabia's national shipping company." And: "the ship war reached a Bahri-managed ship the day after Bloomberg reported Bahri moving ships through with US military coordination".

### L10. LOW: OPEC's secondary-source estimate is called "one estimate from outside sources"
- **Brief text:** "one estimate from outside sources puts it about 1.4 million lower".
- **Issue:** the ~9.19 mb/d is the MOMR's own secondary-source assessment, carried by AA (a single relay). The current wording makes it sound like a third party's estimate.
- **Replacement:** "OPEC's own secondary-source estimate (via AA, one relay) puts it ~9.19 million, about 1.4 million lower."

### L11. LOW: the G7 "constrain" quote drops "continuing our coordination"; "no warships" is thin
- **Brief text:** "…committed 'to economically and politically constrain' Iran if there is no diplomatic solution. They offered no warships."
- **Issue:** the text says "we committed to continuing our coordination to economically and politically constrain". It also backs CENTCOM's demining and escorts and "recognises" a France–UK defensive initiative (ISR-A9/A10).
- **Replacement:** "…committed to 'continuing our coordination to economically and politically constrain' Iran if there is no diplomatic solution. They pledged no ships of their own; the text backs US demining and escorts and recognises a France–UK defensive initiative."

### L12. LOW: the header asserts a publication time we do not have
- **Brief text:** "It was published on Wednesday afternoon, after our brief (first copy we found: 18:28 IST)."
- **Issue:** SAU-B1 says the "time of publication was not found". "After our brief" is an inference.
- **Replacement:** "It is dated Wednesday; the first copy we found is 18:28 IST, after our brief."

### L13. LOW: "most are at 6.0%"
- **Brief text:** "every forecast we found is between 5.9% and 6.2%, and most are at 6.0%"; Cascade Watch: "most forecasts sit exactly on it".
- **Issue:** of the eight current forecasts, four sit at 6.0% (Mint, Informist, Nirmal Bang, BoB ~6%). Two are 6.1%, one is 6.05% and one is 5.93% (Reuters). Seven of eight are at or above 6.0%.
- **Replacement:** "…between 5.9% and 6.2%; half are at 6.0%, and all but Reuters' 5.93% are at or above it." Cascade Watch: "(today; half the forecasts sit exactly on it)".

### L14. LOW: the copper 10-Nov figure
- **Brief text (Page 2, 10 Nov):** "Copper Dec… $6.220".
- **Check:** yfinance HGZ26 10 Nov = 6.2345. The 11-Nov $6.290 and 12-Nov $6.247 match.
- **Replacement:** "$6.234" (or label the source of $6.220).

### L15. LOW: the Ghalibaf adviser's rejection is a paraphrase
- **Brief text:** "An adviser to Ghalibaf says Tehran rejected the request."
- **Replacement:** "An adviser to Ghalibaf, Mehdi Mohammadi, says Tehran rejected the request (Iran International's paraphrase)."

---

## Graph corrections (list only; CoS applies)
- **G1** `india` 12-Nov signal: "the second Gulf tanker with Indian crew hit in two days" → "the second Gulf tanker with Indian crew in an attack or possible attack in two days" (H4). Check `strait-of-hormuz → india` edge text: it says "in a 'possible attack'" (fine).
- **G2** Edge `semiconductors → taiwan` reason: "took TAIEX −1.2–1.85% Thursday (AP)" → "TAIEX −1.2% early (AP), ~−2.7% by 10:45 IST (yfinance)", to match the brief.
- **G3** `nifty-50` / deployment notes, wherever the hold-rule resets are stored: record the full reset list (all four "resume" legs, a declared campaign, confirmed Iranian fire on Oman) and the open question of a strike Iran blames on both Israel and the US (H2). Record Israeli-strike-as-reset as **proposed, not applied**.

## Trigger Point Review

| Trigger | Ruling | My assessment | Agreement? |
|---|---|---|---|
| `houthis` holy-city interception | TESTED, NOT FIRED | Civil Defence: "towards the Makkah region" (province). The 31-Oct note: "Do NOT fire on province-level wording". The 26-Oct note confirms "fired → watching — REVERTED by the independent fact-check" on debris ~20 km out, closer than today's ~36 km. "Fired on a near-identical case on 26 October and reversed on review" is accurate. Relays saying "over Makkah" overstate. | ✅ AGREE |
| `strait-of-hormuz` blacklist (KOTC/Bahri/ADNOC on 2-Nov list struck) | NOT FIRED, closer | Vessel identified, and Bahri is ISM manager (two registries). But "possible attack" is not "struck", and list membership is unknown. Firing conditions are stated. | ✅ AGREE |
| `israel` Ch12/13/Haaretz imminent-strike | stays ACTIVE, not re-fired | Kan is excluded by outlet (31-Oct note); N12 is a command dispute (26-Oct note); nobody says "imminent". Brief mislabels it "Closest, not fired" (L6). | ✅ AGREE (label L6) |
| `brent-crude` 8-Nov >$103.24 | EXPIRED, not fired | Settles 92.57 / 91.49 / 92.76 (yfinance re-pulled); Monday open 98.06 < $100. | ✅ AGREE |
| `brent-crude` 5-Nov >$100 / <$85 | NOT FIRED | $85 is $7.76 below the settle ✓. | ✅ AGREE |
| NEW `israel`: cabinet approves action (2 independent Israeli outlets or PMO/IDF) OR confirmed Israeli strike, by 30 Nov | watching | Well formed: dated, action-based, does not fire on readiness reports or relays. Matches the Ynet test in Section II (16 Nov). One gap: "two independent Israeli outlets" should exclude a single origin carried by two outlets (as Kan was here). Suggest adding "with their own sources". | ✅ AGREE (minor) |
| NEW `qatar`: second long-term buyer cancels/suspends OR FM extended past 31 Dec on record, by 31 Jan 2027 | watching | Well formed. Context the CoS may want: P&GJ (23 Oct) reported Orlen's first QatarEnergy cargo since force majeure (*Al Kharsaah*) due at Świnoujście on **14 Nov**, which is a dated tell for this watch. | ✅ AGREE |
| `united-states` RESUME | stays fired | No revert; nights 7–9 quiet; leg (b)'s earliest new run is nights ten–twelve, ending the morning of Sun 15 Nov ✓ (night *n* = (n+2)→(n+3) Nov). | ✅ AGREE |
| Hold rule, earliest pass 14 Nov | stays 14 Nov | Arithmetic right (7 Nov + 7). The reset list is incomplete (H2). | ✅ AGREE on date; ❌ on the reset wording |
| `oman` | NOT FIRED, steady | Unnamed sources; none is Oman, the US or UKMTO; the Omani denial stands (H5). | ✅ AGREE |
| `uae`, `saudi-arabia` Egypt/capacity, `houthis` Aden, `artesh` joint, `iran` restricted-zone/non-regional, `vance`, `china`, `nuclear-program` | NOT FIRED | Each rests on claims, conditionals or absence; reasons check out against desk text. | ✅ AGREE |
| `india` CPI ≥6.0% | PENDING 16:00 IST | Correct; wording on "most" (L13). | ✅ AGREE |
| Edges | 17 activations, no re-weight | Matches the changelog; no rhetoric-driven re-weight. | ✅ AGREE |

## Market Data Spot-Check (yfinance re-pulled 11:16–11:20 IST; CoS FRED/Treasury files)

| Data point | Brief | Verified | Match? |
|---|---|---|---|
| Brent Jan settle 10 / 11 Nov | 91.49 / 92.76 (+1.39%) | 91.49 / 92.76; +1.388% | ✅ |
| Brent Jan high 11 Nov; low 10 Nov | 94.73; 89.15 | 94.73; 89.15 | ✅ |
| Brent Thu | 91.86 (11:00 IST, −1.0%) | 91.80 (11:00 bar), 91.75 (11:05); −0.97% at 91.86 | ✅ |
| Jump 1 (1-min) | 14:44–14:49, 91.58 → 92.71 | 09:13Z C 91.58; 09:14Z first move; 09:19Z C 92.71 | ✅ |
| Feb / Jun / Dec-27, 10 and 11 Nov | 89.45/83.53/77.64; 90.71/84.78/78.93 | identical | ✅ |
| Jan–Dec27 spread | 13.85; 13.83; ~13.15 (10:40) | 13.85; 13.83; 91.62 − 78.46 = 13.16 | ✅ |
| WTI Dec; HO; RBOB; HH | 86.04/86.53; 4.131/4.211; 2.609/2.608; 3.296/3.215 | identical | ✅ |
| Gold Dec | 4,030.2 → 4,000.5 (−0.74%) → 3,978.6 | identical; −0.737% | ✅ |
| Silver; copper | 51.23/52.00; 6.220/6.290 | 51.225/52.002; **6.2345**/6.290 | ✅ / L14 |
| S&P / Nasdaq / Dow / SOX / VIX / NVDA | 7,619.38 (+1.31%) / 25,466.19 / 52,486.49 / 10,564.11 (+5.66%) / 17.49 / 173.73 | identical; +1.309%, +5.659% | ✅ |
| ES futures | 7,604 (11:00, ~−0.5%) | 7,604.25 vs 7,640.5 = −0.47% | ✅ |
| STOXX / DAX / FTSE / CAC | 663.05 / 26,662.77 / 10,835.47 / 8,332.87 | identical (FTSE 10,835.5) | ✅ |
| KOSPI / Nikkei / TAIEX / HSI, Wed and Thu | 5,375.36/61,248.59/44,257.15/24,315.92; 5,308/60,851/43,045/24,113 | identical | ✅ |
| TAIEX Thu % | ~−2.7% (10:45 IST) | 43,044.99/44,257.15 = −2.74% (AP's −1.2% was earlier) | ✅ |
| Nifty / Sensex / Bank Nifty Wed | 25,255.05 (+0.84%) / 81,879.40 (+0.95%) / 60,792.40 | identical; +0.840%, +0.953% | ✅ |
| Nifty Thu | 25,312.45 (11:10, +0.2%) | 25,312.45 (refresh); +0.23% | ✅ |
| "First war-era close above pre-war" | our check | ^NSEI 28 Feb–10 Nov: max close 25,044.65 (9 Nov); no close ≥25,178.65. 26 Feb 25,496.55 fits Reuters' "highest since Feb 26" | ✅ |
| Below record | 4.1% (26,328.55) | ATH close 26,328.55 (2 Jan); −4.08% | ✅ |
| India VIX; Nifty IT; IOC/BPCL/HPCL | 17.56→17.18; 32,295.60; 148.38/315.25/400.15 → 145.93/314.55/394.15 | identical | ✅ |
| TASI | 10,308.37 (+1.38%) | 10,308.37; vs 10,168.10 = +1.380% | ✅ |
| DXY / USD-JPY | 102.91 → 102.99 / 158.71 → 159.71 | 102.91 → 102.97 / 158.705 → 159.70 | ✅ |
| Treasury par 10 Nov | 4.73 / 4.98 / 5.35 | 4.73 / 4.98 / 5.35 | ✅ |
| HY OAS | 3.34% (9 Nov) | 3.34 (9 Nov, latest) | ✅ |
| Fed odds | 27.5bp / ~10% at 95.925 | (100 − 95.925 − 3.88) × 31/22 = 27.48bp; (27.5 − 25)/25 = 10%. ZQZ26 11-Nov settle 95.915 → 28.9bp / 15.5% (in the brief's stated range) | ✅ |
| EIA scorecard average | ~$97 for 2–11 Nov | 97.05 (8 settles) | ✅ |
| OPEC gap | ~1.4m | 10.563 − 9.19 = 1.373 | ✅ |
| US 2Y Thu | "+3bp to ~4.77%" | par 4.73 → 4.77 is +4bp; the +3bp is Bloomberg's own base (relay). Not a mismatch; noted. | ✅ |

## Items that passed (why)
- **Rezaei's words (lead):** the quotes match DIP-A1/A3 (Mehr English; AFP via France 24). "Both are tied to a new US war on Iran" is right: the AFP line is conditional on aircraft taking off "to bomb Iran", and the X post opens "If the US launches another war against Iran". Note that Borna's headline dropped the condition; the brief says so in its tone section. The Vance denial is in the record.
- **Oil timing:** "same minute" is supported to one-minute resolution (see Summary). The cause is attributed to Reuters (premarket and settle stories), not asserted. "Nothing published in that window" for jump 2 rests on five desks' searches and is worded as "we found". Thursday's causes are attributed (Reuters relays; Investing.com).
- **Ghalibaf:** the quotes match DIP-B1 verbatim, including the bracketed gloss. The Oman and Putin items are labelled "Claimed, not confirmed", with Oman and the Kremlin silent. "Parliament Speaker" is correct.
- **The WSJ Vance report:** unnamed officials, "no date set", the spokesman declined, both Iranian denials. Balanced.
- **Over Iran:** the third quiet night is a REPORTED absence. The Isfahan demolition caveat is a good catch. Trump's lines are flagged "relays differ".
- **Israel paragraph (apart from H3, L2–L5):** "single origin" is in the label. The PMO's "biased fake news" and the IDF's "declined to comment" are in the record. The caution on foreign relays is right. Nothing is stronger than the Israeli originals except L2.
- **At sea:** NCC Fajr's "possible attack" is quoted correctly. "Two ship registries list Bahri's ship-management arm as its manager" is right (MagicPort read directly; Riviera citing Equasis). Ambrey is labelled one source, and "about 7 nautical miles north-east of Lima" matches. The IRGC and regular-navy claims are labelled "Claimed". "Every cause we have from a non-Iranian source this week is a projectile or a drone" is accurate for the causes given (UKMTO 201-26 UAV, Ambrey projectile, India on *Fujairah Energy*); NCC Fajr and the 03:55 UKMTO notice gave no cause.
- **Saudi (apart from L7–L8):** coalition wording quoted in Arabic-faithful English. The other side (Saree's "a new slander") is included, and so is "Civil Defence did not" say "over Makkah". The Houthi KKIA/Yanbu claims are labelled unconfirmed, with Reuters' "did not confirm". Aden is labelled one source. TASI matches.
- **US markets/Fed:** CoreWeave (+24.7%) and the WSJ Nvidia report (REPORTED, "did not comment") are attributed. Goolsbee's "borderline disturbing" is CNBC's headline, and he is Chicago Fed president. Gold's causes are attributed to Kitco.
- **India:** every figure matches. "Seventh straight **regular** session" keeps the Muhurat qualifier. "Nearly $6 billion" is Reuters'. The rupee figure is PTI's. "First war-era close" is labelled as our check, and the data note says no outlet states it.
- **Europe/Lebanon (apart from L11–L12):** the G7 quotes match ISR-A9/SAU-B1. Qassem's quotes match ISR-A7, including "He said nothing on Hormuz". The Orlen item is attributed to The National, including "first buyer to cancel". The TTF explanation is labelled "the one explanation we found". The STOXX "record close" is Reuters'.
- **Deployment:** condition 1 is met ($92.76 < $95). Condition 2 is "met on the last prints" (par 4.98% on 10 Nov; HY 3.34% on 9 Nov) with the next test stated. Condition 3 is split correctly. **The recommendation bullets are word for word the 11-Nov list**; "(unchanged from 11 November)" is true. The added sentence "If it prints at or below 5.54%, the test is live and Sunday's cabinet is the next risk" sits outside the list and changes no condition. Earliest pass 14 Nov; three-night run ends 15 Nov ✓.
- **Brent after Kan:** 93.22 → 93.50 by 00:20 IST = +0.30% (ISR-A15 bars); the brief does not call it a reaction ✓.
- **Section II/scorecard:** the tests are dated and falsifiable. CIBC (best settle $98.32) failed; Brew held (no settle <$90; intraday $89.15); EIA "leaning wrong" with the spot caveat; Motilal failed at 25,255 > 25,141 ✓.
- **Completeness (Check 7):** Section I has 3 geopolitical items, 1 shipping item and 3 markets/commodity items (oil price in the lead, US/Fed/OPEC, India, TTF/Orlen). Section II mixes Ynet with three market voices (Bernstein, Nissan, UBS). Cascade Watch covers Brent, TTF, FII, CPI and Qatar LNG. Balanced.
- **Recycled content:** none presented as new beyond H1. CoreWeave's results were in the 11-Nov brief, but today's item is Wednesday's price move, which is new. The Nvidia CEO story moved on from a report to the WSJ board report.

## Not independently re-found (search index lag; said plainly)
- Rezaei's Al-Mayadeen lines (Tasnim/Mehr/AFP), the 11-Nov Brent settle story (Reuters), and Kan/Ynet/N12 on the cabinet: searches returned only older items. I relied on the desk records and on the yfinance bars, which I re-checked.
- Sonowal's NCC Fajr post: not re-found (searches returned October incidents).
- The G7 November declaration text: searches returned the March declaration only.
- Ghalibaf's 11-Nov Al Jazeera interview: not re-found. A **JNS piece dated 23 June** re-found has "won't return to pre-war status" as its headline (basis for H1).
- Orlen's termination (The National): not re-found. Re-found instead: **P&GJ, 23 Oct**: Orlen's first QatarEnergy cargo since force majeure (*Al Kharsaah*) is due at Świnoujście on 14 Nov, and "the force majeure remains in place". This is consistent with the brief, and is a dated tell for the new `qatar` watch.
- Eisenkot's November letter: not re-found (H3 rests on the desk's quoted text, which is fuller than the brief's paraphrase).
- Saudi Civil Defence's Sabouha post: not re-found. The 24-Oct precedent re-found (Wadi al-Mughammas, ~21–23 km from the Grand Mosque) matches the trigger's 26-Oct note.
- The WSJ Nvidia report, Ambrey via Riviera, the coalition's 11-Nov statements, Qassem (AFP), and the Nifty close (Reuters): not searched. The close was checked against yfinance.

## Final Verdict
**APPROVED WITH CORRECTIONS (5 HIGH, 15 LOW; no CRITICAL).** The reporting and every number hold up. The oil-timing claim is stated no more strongly than the minute bars allow, and the trigger rulings follow each trigger's own notes. Fix before publishing:
- H2, the Signal's reset list: the reader acts on it, and as written it reads as a guarantee the rule does not give.
- H1, "not new in substance" and "hardened".
- H3, Eisenkot.
- H4, "hit".
- H5, the Omani denial.


---
*CoS filing note (11:27 IST): all 5 HIGH and 15 LOW flags applied as written, except H1's Hormuz clause, worded to the JNS headline itself ("a June report carried the same Hormuz line") because the headline names "Tehran's chief negotiator", not Ghalibaf. G1–G3 applied (gu_part_post.py); the new `israel` watch now reads "two independent Israeli outlets with their own sources". The proposed Israeli-strike reset is recorded as NOT applied (user's decision).*
