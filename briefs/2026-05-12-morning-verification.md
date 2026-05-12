# Verification Report — 2026-05-12 (morning)
Generated: 13:50 IST | Fact-Checker: Red Team
Brief checked: briefs/2026-05-12-morning.md

## Summary
8 Section I items checked, 1 HIGH flag raised (graph completeness, March 29 lesson), 2 LOW notes. No CRITICAL flags. Brief is APPROVED WITH CORRECTIONS — graph staleness corrected on `houthis` and `red-sea` nodes; brief body left intact (no factual elevations detected).

---

## Flags

### Flag 1: `houthis` and `red-sea` nodes went stale across the May 11 Hodeidah incident — March 29 completeness gap
- **Issue:** Intel A9 lists `houthis` and `red-sea-shipping` (= `red-sea`) among "Nodes affected" by the May 11 UKMTO Hodeidah-area incident — the first potential break of the 80-day Houthi quiet in this cycle. The graph-changelog encoded the incident under `iran`, `shipping-tankers`, and `strait-of-hormuz` (new 7-day trigger added), but both `houthis.json` and `red-sea.json` were left at `last_updated: 2026-05-10` and still describe "Day 80 quiet" in their summaries. This is precisely the March 29 Saudi-Arabia parallel: a node listed as affected by a material event but never updated.
- **Evidence:** `jq '.last_updated' graph/nodes/houthis.json` returned `"2026-05-10"`; summary opened with "Day 80 quiet — UKMTO and Lloyd's List confirm no Houthi attacks…". Same for `red-sea.json`. The brief's Section I steady-state thread correctly tags the incident CONFIRMED action + UNCONFIRMED attribution (A9), so the failure is graph-side, not brief-side.
- **Severity:** HIGH (graph completeness; would have left two adjacent nodes inconsistent with the encoded `strait-of-hormuz` trigger and with the brief itself).
- **Recommended correction:** Update `last_updated` to 2026-05-12 on both nodes; rewrite summaries to reflect "Day 81 — non-event POSSIBLY BROKEN May 11" with CONFIRMED action + UNCONFIRMED attribution; add a May 12 signal to each `recent_signals` array preserving the non-claim itself as the signal and the 7-day window framing.
- **Applied:** Yes. Both nodes updated; conservative encoding (CONFIRMED action, UNCONFIRMED attribution); no edge weight changes (trigger watch only).

### Flag 2: Editor's note framing of Iran's prior UAE-targeted strikes as "direct retaliation"
- **Issue:** Brief line 4 editor's note states: "Iran's prior UAE-targeted strikes were direct retaliation." The underlying WSJ scoop is tagged REPORTED (single primary), and intel B6 frames the causal read more carefully as "now retroactively contextualized as direct retaliation." The body text of Item 5 properly softens this with "the operative read." The editor's note runs slightly ahead of the body.
- **Severity:** LOW (the inference is plausible and the body preserves the right hedge; the editor's note compresses for emphasis).
- **Recommended correction:** Not applied — body text governs, and the editor's note's compression is within editorial latitude. Flagged for next-brief discipline.
- **Applied:** No.

### Flag 3: Internal inconsistency on Hormuz pre-war baseline (120/day vs 70/day)
- **Issue:** Editor's note (line 4) cites "~120/day pre-war" (Lloyd's List figure used throughout the cycle). Item 6 (line 26) cites "against roughly 70 pre-war" (Nasser's CEO quote). Both come from the staging files, but the brief doesn't reconcile them.
- **Severity:** LOW (both are sourced; Nasser's number is industry-CEO authority, Lloyd's List is the trade-publication standard; they likely measure different things — transits vs through-trips). A reader who notices will wonder.
- **Recommended correction:** Not applied — both figures are sourced and tagged correctly to their authors. Next brief should pick one baseline and note the other parenthetically.
- **Applied:** No.

---

## Items That Passed

### Item 1: Trump rejected Iran's counter-proposal — "TOTALLY UNACCEPTABLE" / "massive life support" (PASS)
- **Action or rhetoric?** CONFIRMED RHETORIC (Trump statements via Truth Social + Oval Office) — and the brief calls it "rhetoric" appropriately (line 11). Iran's formal delivery via Pakistan is CONFIRMED ACTION. Both correctly attributed. ✅
- **Sources:** Multi-source primary (WaPo, CNN, NBC, CBS, Bloomberg, Time, Truth Social, Press TV, IRNA, Axios). ✅
- **Other side:** Iran (Pezeshkian, Baghaei) included; Iran's "never bow" and "talks are not surrender" framing carried with same weight. ✅
- **Sit-Room handling:** Brief tags meeting occurrence CONFIRMED, contents REPORTED — matches intel B3 ("Axios primary, multi-amplified; NO ORDERS HAVE BEEN ISSUED"). No elevation of "Trump is going to hit them a bit" to action. ✅
- **Beijing pause:** Correctly framed as structurally precluding kinetic response over the clock-close window — matches intel B4. ✅

### Item 2: Iran's first HEU concession with return clause (PASS)
- **Action or rhetoric?** CONFIRMED ACTION (document delivered) + REPORTED on full terms (WSJ primary single-source). Brief tag "(REPORTED on terms — single-source primary with cascade amplification)" matches intel A2 exactly. ✅
- **Sources:** WSJ primary + Bloomberg/Reuters/IRNA/Tasnim/Press TV/Al Jazeera/NPR amplification. Brief correctly notes the amplification cascade rather than presenting it as independent corroboration. ✅
- **Russia custodian:** Correctly framed as "implicit" — no party has publicly named Russia. Matches intel A2 + B2. ✅
- **Return clause:** Operatively highlighted — brief correctly reads custody-flexibility vs permanent commitment. Tag discipline solid. ✅

### Item 3: Indian markets — Sensex -1,313 pts, INR ₹95.54, FII -₹8,437 cr (PASS)
- **Action or rhetoric?** CONFIRMED data (exchange + NSDL/NSE primary). ✅
- **Numbers cross-checked vs staging:** Sensex 76,015 / -1,312.91 / -1.70% (matches intel B11); Nifty 23,816 / -1.49% (matches); USD/INR ₹95.0930 May 11 / ₹95.54 May 12 (matches); FII ₹8,437.56 cr (matches); reserves -$7.79 bn to $690.69 bn (matches); GDP cut 6.7% → 6.2% (matches); S&P 7,413 / NASDAQ 26,274 / VIX 18.38 (matches markets.md). ✅
- **Causation:** Brief correctly identifies "FII channel withdrawal" as the transmission mechanism, not headline causation. ✅

### Item 4: CF Industries +8.2% — fertiliser regime shift (PASS)
- **Numbers cross-checked:** CF $124.48 +8.2% (matches); Nutrien +4.3% (matches); BASF +3.5% (matches); Linde +2.3% (matches); UBS PT $97→$140 (matches markets C1); DAP India tender $935/t (matches); urea US Gulf +50% (matches); QAFCO + SABIC ~35–40% global urea export capacity (matches). ✅
- **Modi seven-appeal attribution:** CONFIRMED multi-source (CNBC, Al Jazeera, DD News, Organiser). Brief correctly preserves Al Jazeera framing "Iran war effect: why is Modi asking Indians to avoid foreign trips, gold." ✅
- **Reversibility framing:** Low-reversibility claim is sourced to structural reasoning (Ras Laffan 60-day window + Q3 demand binding) rather than asserted as fact. ✅

### Item 5: WSJ UAE-Lavan revelation (PASS — with Flag 2 LOW note above)
- **Action or rhetoric?** CONFIRMED RETROACTIVE ACTION on the April 8 strike (REPORTED per WSJ primary); REPORTED on operational details. Brief tag "(REPORTED — WSJ primary single-source on operational details; amplified by Times of Israel, Middle East Eye, Jerusalem Post, Reuters, Türkiye Today, Mediaite)" matches intel B6. ✅
- **Other side:** UAE silent (acknowledged); Iran silent on WSJ exposure; Saudi distancing via Al-Hadath. All noted. ✅
- **Gulf media handling:** The National (UAE), Khaleej Times, Al Jazeera all correctly characterized — matches intel C tone section. ✅
- **Caveat:** Editor's note runs slightly stronger than body on causation (see Flag 2 above).

### Item 6: Aramco CEO Nasser — Hormuz 2–5 ships/day (PASS — with Flag 3 LOW note)
- **Action or rhetoric?** CONFIRMED industry-CEO authority (CNBC, Yahoo Finance, Eastern Herald). ✅
- **VLCC Agios Fanourios:** CONFIRMED (Bloomberg primary, gCaptain secondary). ✅
- **CENTCOM tally 58→61:** CONFIRMED (CENTCOM press releases). ✅
- **Brent $105.58 / +1.3% 1D / +6.3% 1M / +56.4% 3M:** matches markets.md. ✅
- **Goldman $85 / JPM $60 gap:** matches intel B12 and markets D5. ✅
- **AWRP ~1% (8x pre-war):** matches markets.md F. ✅
- **Caveat:** 70/day vs 120/day pre-war baseline left unreconciled (Flag 3 above).

### Item 7: Hezbollah killed IDF reservist Glovanyov; civilian trigger UNTRIPPED (PASS)
- **Glovanyov KIA:** CONFIRMED multi-source (Times of Israel, Ynet, Haaretz, Jerusalem Post, JNS, Xinhua, Middle East Eye, VINnews). ✅
- **Soldier vs civilian discipline:** Brief correctly identifies Glovanyov as soldier on the border, not civilian inside Israel. Trigger window correctly framed as expired UNTRIPPED. This is exactly the kind of distinction the fact-check process exists to enforce. ✅
- **SAM-at-IAF (CGTN):** Brief tags as "single-source, needs Israeli-side corroboration" — matches intel A6 exactly. NOT elevated. ✅
- **Netanyahu 60 Minutes:** CONFIRMED broadcast; quote rendered correctly. Haaretz "lifeline" critique rendered as Haaretz framing, not adopted as brief framing. ✅
- **Knesset reservist extension + Zamir 12,000 shortfall:** matches intel B10. ✅
- **Beirut southern-suburb strike "first since April 16 ceasefire":** matches intel A6. ✅

### Item 8 (steady-state thread): Houthi, Kharg, Doha, Rial, OFAC, Mojtaba, Kurdish, Bahrain (PASS — with Flag 1 graph correction)
- **Houthi Hodeidah:** CONFIRMED action / UNCONFIRMED attribution — tag discipline maintained in brief. Graph-side staleness fixed (Flag 1). ✅
- **Kharg slick:** PARTIALLY CONFIRMED (Fox primary, mainstream wires lagging) — tag preserved; cause "formally contested" framing matches intel A4. ✅
- **Doha Safesea Neha attribution:** CONFIRMED (IndexBox, FreightWaves, Seatrade Maritime). Pravda UAV attribution correctly held as UNCONFIRMED — not elevated. ✅
- **Rial 1,799K → 1,830K → 1,853K:** matches intel A8 exactly; +3% framing correct; May 19–21 trigger ETA framed as linear extrapolation, not prediction. ✅
- **OFAC 12 entities + 3 individuals:** matches intel B7. ✅
- **Mojtaba Day 4 silence:** matches intel A7. ✅
- **Kurdish camps non-event May 11–12:** matches intel A10. ✅
- **Bahrain unchanged + UAE airspace lapsed May 11:** matches intel A5. ✅

---

## Trigger Point Review

| Trigger | Status in Changelog | My Assessment | Agreement? |
|---|---|---|---|
| Iran formal response within Trump 1-week window | watching → activated_and_rejected | Iran delivered (CONFIRMED multi-source) + Trump rejected (CONFIRMED multi-source) | ✅ AGREE |
| Brent <$105 sustained 5+ sessions | watching → failed | $105.58 May 12 print is CONFIRMED data; thesis falsified for window | ✅ AGREE |
| Kharg slick re-appears within 14 days | watching → activated | Trigger framed on re-appearance (not cause); slick is PARTIALLY CONFIRMED (multiple satellite passes); cause remains formally contested but trigger condition met | ✅ AGREE (cause-CONTESTED note preserved) |
| USD/INR crosses ₹95 | breached_and_reversed → re_breached | ₹95.0930 May 11 + ₹95.54 May 12 fresh record (CONFIRMED data) | ✅ AGREE |
| USD/INR breaks ₹95.50 RBI direct-intervention | watching → activated | ₹95.54 May 12 intraday cleanly broke threshold (CONFIRMED data) | ✅ AGREE |
| Hezbollah Israeli civilian casualty by May 11 | watching → untripped_expired | Window closed May 11; Glovanyov is SOLDIER not civilian; ceiling held | ✅ AGREE |
| Iran rial 2M/USD | watching → watching | Conservative hold at 1,853K (still 7.9% from trigger) — correct discipline (approach is not breach) | ✅ AGREE |
| 9 new triggers added at `watching` | — | Each is sourced and properly conservative (Trump-orders-strikes, Brent $108–110, USD/INR ₹96, Red Sea 7-day, Russia HEU custodian, DAP $900, fertilizer subsidy, KOSPI 7,500, Hezbollah civilian 14-day extension) | ✅ AGREE |

No trigger elevation on insufficient evidence. Critical-check passed.

---

## Market Data Spot-Check

| Data Point | Brief Value | Staging Value | Match? |
|---|---|---|---|
| Brent | $105.58 (+1.3% 1D, +6.3% 1M, +56.4% 3M) | $105.58 (+1.3% / +6.3% / +56.4%) | ✅ |
| USD/INR | ₹95.54 (+1.2% 1D) | ₹95.54 (+1.2%) | ✅ |
| Sensex (May 11) | 76,015 (-1,312.91 / -1.70%) | 76,015.28 (-1,312.91 / -1.70%) | ✅ |
| Nifty (May 11) | 23,816 (-1.49%) | 23,815.85 (-1.49%) | ✅ |
| VIX | 18.38 (+6.9%) | 18.38 (+6.9%) | ✅ |
| CF Industries | $124.48 (+8.2%) | $124.48 (+8.2%) | ✅ |
| URA | $57.23 (+3.7% 1D, +12.3% 1M) | $57.23 (+3.7% / +12.3%) | ✅ |
| Gold | $4,711.30 (-0.2%) | $4,711.30 (-0.2%) | ✅ |
| IRR/USD | 1,853,000 (+1.26% 1D) | 1,853,000 (+1.26%) | ✅ |
| TTF Gas | €46.23 (+4.74%) | €46.23 (+4.74%) | ✅ |

All spot-checked numbers match the staging dossier. No transcription drift.

---

## Completeness / Proportionality (March 29 Check)

- **Section I:** 8 items — 4 geopolitical (Trump rejection, Iran HEU terms, WSJ UAE Lavan, Hezbollah KIA) + 3 market/commodity (Indian markets, CF Industries, Aramco/Hormuz) + 1 multi-topic steady-state refresh. Balanced. ✅
- **Section II analysts:** 6 individual takes + source-tone — 2 geopolitical (Sadjadpour, Nasr), 4 market/commodity (Croft, Kaneva-vs-Goldman, Varma, Kornbluth). Excellent balance. ✅
- **Section III Cascade Watch:** Mix of military (UAE-Israel, UAE-US covert-combatant edges) + commodity (fertilizer-urea→india, uranium-sector→iran weight raise to 8.5, marine-war-risk-insurance→brent 1st-order edge promotion, fii-flows new node) + diplomatic (nuclear-program new node). No commodity-cascade absence. ✅
- **Graph completeness:** 33 nodes modified; 4 new nodes; 20 new edges; 6 trigger status changes; 9 new triggers. **Gap found:** `houthis` and `red-sea` left stale across the Hodeidah event (Flag 1) — corrected by this verification pass. No other completeness gaps detected.

---

## Final Verdict

**APPROVED WITH CORRECTIONS.** Brief body is clean — no rhetoric-as-action elevations, no headline-as-fact errors, no single-source amplification dressed as consensus, no tag drift, no unjustified trigger moves, no market-data transcription error. Tag discipline on WSJ HEU-return-clause, WSJ UAE Lavan, Fox second-slick, CGTN SAM-at-IAF, and Pravda Doha UAV attribution is consistently conservative. The one substantive failure is graph-side: `houthis` and `red-sea` nodes went stale across the May 11 Hodeidah incident (March 29 pattern). Both corrected by this pass. Two minor language notes (UAE retaliation framing in editor's note; 120/70 Hormuz baseline inconsistency) logged as LOW for next-brief discipline; neither warrants body edits.

Editor's craft is high on a day with unusually heavy structural traffic — six MAJOR developments + a 48-hour gap to absorb — without losing tag discipline. The Section III "uranium decoupled long" thesis is the kind of synthesis the graph is supposed to enable; it follows from the new `nuclear-program` node + the uranium-sector→iran weight raise + the URA vs gold divergence and is not a leap.

*Verification: 8 Section I items checked, 1 HIGH graph correction applied (`houthis` + `red-sea` nodes), 0 brief-body corrections required, 2 LOW notes logged.*
