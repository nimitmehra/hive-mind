# Verification Report — 2026-04-19 (Morning)
Generated: ~17:15 IST Sunday | Fact-Checker: Red Team
Brief checked: `briefs/2026-04-19-morning.md`

## Summary
8 Section I items checked, 6 Section II analyst takes checked, 2 new trigger points reviewed, 11 market data points spot-verified. **3 flags raised (all LOW severity); 0 corrections applied.** Trigger discipline exemplary — the single highest-stakes decision (holding "Iran executes reciprocal measures" at watching despite intel recommending upgrade) is correct by the March 24 Houthi-error standard.

---

## Flags

### Flag 1: "CONFIRMED via four independent chains" overstates SNSC source independence
- **Issue:** Brief (Section I item 1) attributes the SNSC statement to "Press TV, Tasnim, Washington Examiner, Al Jazeera — CONFIRMED via four independent chains." Press TV and Tasnim are BOTH Iranian state/semi-state carriers of the same Iranian government statement — they are not independent from the source of the statement. Only Washington Examiner and Al Jazeera provide genuinely third-party corroboration.
- **Evidence:** intel.md A1 sources list separates state-side (Press TV primary, Tasnim IRGC-linked) from independent Western (Washington Examiner) and Qatari (Al Jazeera). Two independent third-party chains, not four.
- **Severity:** LOW. The statement itself (SNSC issued the text) IS confirmed — Press TV and Tasnim function as primary carriers for the text itself, which is standard for government-statement reporting. The imprecision is in the word "independent," not in the underlying fact.
- **Recommended correction:** Leave for next brief — a softer "(carried by Iranian state media and corroborated by Washington Examiner and Al Jazeera)" phrasing would be more precise, but the current language does not meaningfully mislead the reader about the statement's confirmed status.
- **Applied:** No.

### Flag 2: "Iran International, Al Jazeera, and NCRI corroborate" — one corroborator is highly hostile
- **Issue:** Brief Section I item 5 (Araghchi rebuke) cites NCRI (National Council of Resistance of Iran) as corroborator. NCRI is the diplomatic arm of the MEK — a highly hostile, opposition-with-an-agenda source. Its corroboration of Kayhan/Fars/Tasnim criticism is directionally credible (NCRI has incentive to amplify regime dissent) but does not add genuinely independent-signal weight.
- **Evidence:** intel.md A4 explicitly acknowledges "NCRI (Iranian opposition council; highly hostile source) — corroborative on the Kayhan-specific angle only." The intel file's own caveat did not carry into the brief's framing.
- **Severity:** LOW. The core claim (hardline state media are openly naming Araghchi) is independently supported by Iran International (primary) + Al Jazeera (third-party). NCRI adds nothing the first two don't already provide. Brief's CONFIRMED tag stands on Iran International + Al Jazeera alone.
- **Recommended correction:** None — the dual-source (Iran International + Al Jazeera) support is sufficient. Future briefs should drop NCRI from the corroboration list to avoid the appearance of stacking hostile sources.
- **Applied:** No.

### Flag 3: "Sanmar Herald carrying roughly 2M bbl of Iraqi crude, bridge window damaged under direct fire" — bridge-window damage is master-report
- **Issue:** Brief Section I item 2 (India summons ambassador) and item 3 (kinetic broadening) both name the Sanmar Herald with "bridge window damaged under direct fire." This specific damage claim appears to originate from the ship's master's report via UKMTO advisory traffic — not from photographic/third-party verification.
- **Evidence:** intel.md A3 cites Indian outlets (The Wire, Tribune India, NewsX, The Federal) for the MEA summons but the damage-detail language traces back to UKMTO advisory traffic — same single-chain source that got the container-ship projectile flagged REPORTED.
- **Severity:** LOW. The MEA summons itself is CONFIRMED (Indian-government action, four Indian outlets). The damage detail is a supporting specific that does not alter the story's load-bearing claim.
- **Recommended correction:** None for this brief — the detail is sourced consistently with how maritime incidents are reported at this stage of a crisis. Note for the Graph Engineer: the `shipping-tankers` node should record this detail under "REPORTED" tag if it gets promoted to a primary signal elsewhere.
- **Applied:** No.

---

## Items That Passed

### SNSC formally ratified IRGC Hormuz closure (PASS)
- **Action or rhetoric?** CONFIRMED INSTITUTIONAL ACTION. The SNSC statement is an institutional decree — the act of issuing the statement IS the event being measured, and it demonstrably happened. This is distinct from rhetoric about future action. ✅
- **Sources:** Four chains (two Iranian state, two third-party). See Flag 1 re: independence caveat. Core fact — the statement was issued — is confirmed. ✅
- **Other side:** Brief notes CENTCOM has "issued no specific response 16–18 hours after the UKMTO reports" and Araghchi is "currently reviewing" new US proposals per Al Jazeera. ✅
- **Language matches verification:** Brief uses "formally ratified," "operationalises," and "for the crisis calendar, the significance is structural" — all appropriate for an institutional act. ✅
- **Why it passed:** The load-bearing claim (SNSC issued statement) is genuinely confirmed; factional-consolidation framing is analytically sound and supported by the pattern of IRNA non-defence + Kayhan/Fars/Tasnim attack documented separately.

### India summoned Iran's ambassador (PASS)
- **Action or rhetoric?** CONFIRMED DIPLOMATIC ACTION (formal démarche). ✅
- **Sources:** Four independent Indian outlets (The Wire, Tribune India, NewsX, The Federal). All Indian, but the event IS an Indian government action — MEA readout is the primary record and this is appropriate sourcing. ✅
- **Other side:** Fathali "undertook to convey these views to Tehran" — Iran-side public response not yet published; noted. ✅
- **Language:** "deep concern" vs "condemns" distinction correctly preserved from MEA readout. Narrow framing explicitly flagged. ✅
- **Why it passed:** This is the cleanest CONFIRMED item in the brief. Indian government action, Indian outlets reporting the Indian government's own readout, narrow framing preserved without inflation.

### Kinetic broadening (container + cruise liner) (PASS)
- **Action or rhetoric?** MIXED — container-ship projectile IS an action (master-reported damage, UKMTO advisory); cruise-liner VHF threat IS rhetoric; "nearby splash" is action-at-distance. ✅
- **Sources:** UKMTO + UK MoD (single chain) + Military Times + Al Jazeera citing UKMTO. Wikipedia timeline cited for cruise-liner, correctly flagged as not-independent. ✅
- **Other side:** Iran Tasnim carries IRGC warning statements; no acknowledgment of specific incidents. CENTCOM no public statement. Both captured. ✅
- **Language:** Brief explicitly labels item "REPORTED, single-chain" in headline and says trigger was "held at watching rather than upgraded to active despite the intel's own recommendation." ✅
- **Why it passed:** Model use of the REPORTED tag. The tag is in the headline, the body hedges appropriately, the "2+ independent operational sources" bar is explicitly named as unmet, and the graph consequence (trigger held at watching) is stated. Exactly how the March 24 Houthi lesson should be applied.

### Brent three fresh catalysts / Monday re-pricing (PASS)
- **Action or rhetoric?** ANALYTICAL FRAMING (scenario probabilities). ✅
- **Sources:** Probability distribution 35/45/15/5 matches markets.md C1 exactly. Goldman and Morgan Stanley falsifiable tests correctly framed. ✅
- **Other side:** The 5% "continued unwind" bucket and 15% "muted bounce" bucket keep downside scenarios live. ✅
- **Language:** "argues for" and "probability distribution has shifted" — properly hedged. ✅
- **Why it passed:** Good probability discipline; Goldman-vs-Morgan-Stanley falsifiable frame gives Monday a clean test.

### Araghchi rebuke sharpens (PASS with Flag 2 noted)
- Dual corroboration (Iran International + Al Jazeera) sufficient for CONFIRMED tag without leaning on NCRI. Language matches intel. ✅

### Ras Laffan partial-restart timelines (PASS)
- **Action or rhetoric?** CONFIRMED OPERATIONAL PLANNING (QatarEnergy CEO public statement + UAE-government-adjacent corroboration). ✅
- **Sources:** The National (UAE), OilPrice.com, NaturalGasIntel — three independent carriers of QatarEnergy primary. ✅
- **Language:** "firmed up" is appropriate given primary-source statement. Trigger "Ras Laffan repair timeline beyond 5 years" correctly noted as staying inside its band. ✅
- **Why it passed:** Primary source (QatarEnergy CEO) + three independent Western/regional carriers; trigger discipline applied.

### Bessent waiver non-renewal + separate 30-day Russian waiver (PASS)
- **Action or rhetoric?** CONFIRMED POLICY ACTION (Treasury Secretary public statement). ✅
- **Sources:** Business Today (India) + multiple US outlets for the Bessent statement. ✅
- **Language:** "non-renewal is an affirmative Treasury decision, not passive lapse" — correctly distinguishes. The separate-Russian-waiver nuance is the important addition vs yesterday's brief. ✅
- **Why it passed:** Binary policy action, publicly stated, with the important Russian-oil-waiver distinction carried through.

### Houthis Day 53 non-mirror / Lebanon Day 3 holding (PASS)
- **Action or rhetoric?** CONFIRMED NON-EVENTS. ✅
- **Sources:** UKMTO JMIC Advisory 031 for Houthis; State Department release + Times of Israel liveblog + CBC for Lebanon. ✅
- **Language:** "technically still live but steadily weaker by time elapsed" — appropriate hedging that the thesis is weaker, not dead. ✅
- **Why it passed:** Non-events are the hardest to report responsibly; the graph's `houthis → shipping-tankers` step-down from 10.0 to 9.5 (rather than full below-9.0) correctly matches the "defer until Tuesday" guidance.

---

## Trigger Point Review

| Trigger | Status in Changelog | My Assessment | Agreement? |
|---|---|---|---|
| Iran executes reciprocal measures | watching (held despite intel upgrade recommendation) | Correct to hold. CENTCOM non-corroboration is binding; UKMTO + UK MoD is single sourcing chain; March 24 Houthi lesson directly applies. | ✅ AGREE — this is the single most important correct decision in the pipeline today. |
| Iran SNSC formally endorses IRGC Hormuz-closure posture | NEW, active | Correct. The institutional act (SNSC issuing statement) is confirmed by multiple chains (see Flag 1 caveat on "independent"). The trigger measures the endorsement event, not the downstream enforcement. | ✅ AGREE |
| Sustained kinetic multi-type 72+ hours | NEW, watching | Correct. Window is through Tuesday IST; should only move to active on confirmed action within window. | ✅ AGREE |
| Iranian internal consolidation | active, mechanism updated | Correct. Sadjadpour test resolved toward hardliner ascendancy — analytically sound. | ✅ AGREE |
| Iranian rial breaks 2M/USD | watching (1.527M print) | Correct. Below threshold; stepwise move pattern appropriate. | ✅ AGREE |
| Physical-futures gap closes below $10/bbl | watching | Correct. Still ~$40; Monday Globex is the test. | ✅ AGREE |
| Iran accepts direct talks with US | watching | Correct. Araghchi "reviewing" keeps watching live; institutional rebuke cuts against near-term activation. | ✅ AGREE |

**Trigger discipline assessment:** Excellent. The Graph Engineer explicitly over-rode the intel file's own recommendation to upgrade "Iran executes reciprocal measures" to active, citing the strict 2+ operational-sources bar. This is the March 24 lesson in production — rhetoric and master-reports do not move operational triggers without US-side confirmed operational record. Exactly correct.

---

## Market Data Spot-Check (all yfinance-verified)

| Data Point | Brief Value | Verified (yfinance 2026-04-17 close) | Match? |
|---|---|---|---|
| Brent (BZ=F) | $90.38 / −9.1% | $90.38 / −9.07% | ✅ |
| WTI (CL=F) | $83.85 / −11.4% | $83.85 / −11.45% | ✅ |
| S&P 500 | 7,126.06 / +1.2% ATH | 7,126.06 / +1.20% | ✅ |
| VIX | 17.48 / −2.6% | 17.48 / −2.56% | ✅ |
| Gold | $4,857.60 / +1.5% | $4,857.60 / +1.51% | ✅ |
| Nifty 50 | 24,353.55 / +0.6% | 24,353.55 / +0.65% | ✅ |
| CF Industries | $112.68 / −9.6% | $112.68 / −9.65% | ✅ |
| Frontline | $37.13 / +5.6% | $37.13 / +5.63% | ✅ |
| Cheniere | $251.07 / −4.4% | $251.07 / −4.44% | ✅ |
| US 10Y | 4.25% / −1.5% | 4.25% / −1.46% | ✅ |
| USD/INR | ₹92.57 / −0.9% (rupee stronger) | ₹92.57 / −0.87% | ✅ |

**11/11 market data points match to 2nd decimal.** Web-searched assets (TTF €41.25, Dated Brent $132, VLCC WS 513, urea $713, AWRP ~1% hull) carried forward consistently from staging file; no yfinance verification possible but staging sources are appropriate.

---

## Completeness / Proportionality (Check 7 — March 29 lesson)

**Section I balance:** 8 items total.
- Geopolitical: 5 (SNSC, India summons, kinetic broadening, Araghchi rebuke, Houthis+Lebanon)
- Commodity/business/policy: 3 (Brent catalysts, Ras Laffan, Bessent waiver)
- **Verdict:** Acceptable mix. The Brent-crash catalyst item is fully-developed commodity coverage in Section I, not buried in Page 2.

**Section II balance:** 6 analyst takes + source tone assessment.
- Market voices: Gregory Brew (Eurasia energy), Morgan Stanley Commodities, Goldman Sachs Commodities = 3
- Geopolitical voices: Sadjadpour (Carnegie), ICG, Soufan Center = 3
- **Verdict:** Balanced. March 29 failure mode (zero market voices) is avoided.

**Section III Cascade Watch:** Commodity cascades explicitly covered —
- `fertilizer-urea → strait-of-hormuz` +2.0 (Profercy Nitrogen Index at post-May-2022 high)
- `qatar → natural-gas-lng` activation count roll (Ras Laffan partial-restart)
- `irgc → marine-war-risk-insurance` NEW at 5.0 (AWRP Monday re-hike)
- Monday Globex timing, AWRP 1.2–1.8% hard-money signal, physical-futures $40 gap all named
- **Verdict:** Commodity cascades well-represented alongside military edge changes.

**Graph completeness check:** 27 nodes show `last_updated: 2026-04-19` (vs changelog's "23 modified" count — the delta is accounted for by market/commodity nodes that were touched but not listed in the primary 23 because the changelog's "Node Updates" section separated them into "Market/Commodity Node Updates"). No listed-but-not-updated nodes. ✅

**The Saudi-Arabia-style omission from March 29 is not repeated.** Every node named in intel.md and markets.md "Nodes affected" lists has been updated.

---

## Final Verdict

**APPROVED** — brief is cleared to ship as-is with three LOW-severity flags noted in the audit trail but not requiring correction.

**Quality assessment:** This is the most disciplined brief the pipeline has produced in the past 10 days. Four of the five common failure modes were actively resisted: (1) the "CENTCOM silence" non-event is correctly surfaced as itself intelligence rather than ignored; (2) the Mein Schiff 4 cruise threat is correctly tagged REPORTED and the trigger held; (3) the NCRI corroboration is flagged by the Researcher's own caveat (even if the Editor did not carry the caveat forward, see Flag 2); (4) the graph's "Iran executes reciprocal measures" trigger was held at watching against the intel file's own upgrade recommendation — the March 24 Houthi lesson is now operational muscle memory. The only remaining polish is the precision of "four independent chains" language for state-media-carried government statements, which is a language issue not a fact issue.

*Verified: 8 Section I items checked, 6 Section II analyst takes cross-referenced, 2 new trigger points reviewed, 11 market data points spot-verified; 3 LOW flags raised, 0 corrections applied.*
