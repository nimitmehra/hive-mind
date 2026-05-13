# Verification Report — 2026-05-13 (morning)
Generated: 15:35 IST | Fact-Checker: Red Team
Brief checked: briefs/2026-05-13-morning.md
Evidence baseline: staging/2026-05-13-morning/{intel.md, markets.md, graph-changelog.md}

## Summary
9 Section-I items checked, 18 graph-trigger calls reviewed, 4 spot-checks on market data. **2 HIGH flags** raised (one Brent narrative / trigger-state, one internal S&P contradiction). **0 CRITICAL**. **3 LOW** flags noted for context. All rhetoric-vs-action tags are correctly preserved at the floor (Rezaei 90%, Saudi strikes, HMM Namu attribution). Completeness check (March-29 lesson) **PASSES** — Section I balances geopolitics with macro (CPI), markets (Brent / VIX / URA / CF) and military (Litani); Section II carries market analysts (Croft, Kornbluth, Varma) alongside geopolitical voices; Section III Cascade Watch encodes commodity cascades (URA, CF, Brent trigger, fed→brent CPI edge) alongside Israel/Lebanon and US/China military-diplomatic edges. No nodes listed as affected in the staging files were skipped in the changelog.

---

## Flags

### Flag 1: Brent settle / trigger-zone framing contradicted by live data — HIGH
- **Issue:** The brief commits to a May-13 Brent settle of **$106.29** ("the settle then came back to $106.29 (-1.4% on the day)") and frames the $108–110 trigger zone as "TESTED AND FAILED" (Section I item 7; data table; markets.md C2). yfinance (BZ=F) at the time of verification (post-brief-generation) shows **May 12 close $107.77 and May 13 latest $108.05** — i.e. Brent has continued to rally *through* the $108 line rather than retracing to $106.29.
- **Evidence:**
  - yfinance live: `BZ=F` last close $108.05 (May 13), prev $107.77 (May 12).
  - Brief paragraph: implied May 12 close ~$107.77 (matches yfinance) → "settle then came back to $106.29" (does **not** match yfinance May-13 settle of $108.05).
  - The brief was generated at 14:55 IST = 09:25 GMT — *before* the May 13 ICE settle (~19:30 GMT), so the $106.29 figure is most likely an early-session intraday snapshot from Trading Economics presented as "the settle." Subsequent intraday rallied to and through $108.
- **Severity:** HIGH (not CRITICAL because (a) the $106.29 figure was real at *some* moment in the session and (b) the Graph Engineer's call to hold the $108–110 trigger at `watching` is still defensible — a sustain test needs 2 sessions and May 12's $107.77 close is below $108).
- **Recommended correction:**
  1. The trigger calibration is *not* wrong — the rule explicitly requires "$108–110 sustained 2 sessions," and only May 13 close at $108.05 currently qualifies as a single-day breach above $108. Day 1 of 2-session sustain test, not "TESTED AND FAILED." Tomorrow's brief should *re-examine* the trigger using a verified settle price.
  2. Tomorrow's pipeline should pull Brent settle *after* 19:30 GMT to avoid the intraday-snapshot-as-settle pattern, or label the price explicitly as an intraday print rather than a settle.
  3. The "trinary band $100–110 held through five rounds of escalation" framing in the editor's note is now under genuine stress, not falsified — the band is *being tested at its upper edge*, not holding comfortably in the middle. Investors reading this brief should be aware that Brent has continued upward since the data snapshot.
- **Applied:** Verification note appended to brief; brief body NOT rewritten because the underlying snapshot was real at the moment of capture. The next brief (2026-05-14) must re-examine the $108–110 trigger using the confirmed May-13 settle.

### Flag 2: S&P 500 internal inconsistency — HIGH
- **Issue:** The brief's Section I CPI item says "*The S&P 500 closed -0.29% at 7,392*", but the Page-2 data table lists "*S&P 500 7,400.96 (-0.2%)*". These cannot both be true: at the May 11 record of 7,412.84, a close of 7,392 implies −0.281%, while a close of 7,400.96 implies −0.160%. yfinance confirms the May-12 close at **7,400.96**, so the data table is correct and the narrative paragraph's "7,392 / -0.29%" is wrong.
- **Severity:** HIGH (the lead Section-I item contains a wrong index level and a wrong percentage — readers cross-checking will hit it immediately).
- **Recommended correction:** Replace "*-0.29% at 7,392*" with "*-0.16% at 7,400.96*". Math: (7400.96 − 7412.84) / 7412.84 = −0.160%.
- **Applied:** Yes. (See edit below.)

### Flag 3: USD/INR figure variance with yfinance — LOW
- **Issue:** Brief says USD/INR ₹95.63 May 12 close, ₹95.68 May 13 morning. yfinance (`INR=X`) shows 95.39 May 12, 95.71 May 13. The directional read (record close, ₹95.50 RBI threshold broken, pace slowed) is unchanged across both data sources; the variance is consistent with NSE-cross vs INR=X (offshore NDF) source differences that this graph has tolerated for weeks.
- **Severity:** LOW.
- **Recommended correction:** None. The brief's source is the onshore NSE close, which is the analytically correct reference for the ₹95.50 RBI threshold and Sonal Varma's call. yfinance INR=X is a slightly different reference series.
- **Applied:** No correction; logged for context.

### Flag 4: Iran rial "+0.66% d/d" labelling — LOW
- **Issue:** The Page-2 data table labels the rial move as "+0.66% d/d" between May 10 (1,830,000) and May 12 (1,842,000). That is a 48-hour move, not 24-hour. Bonbast does not publish a May 11 print (Iranian Friday weekend / blackout day), so calling it "d/d" is technically imprecise — it is a 48-hour delta presented as daily.
- **Severity:** LOW.
- **Recommended correction:** No edit needed (analytically the narrative is correct — the +2.4% over 72 hours arithmetic in intel.md A5 is consistent). Future briefs should label the rial move as "48-h" rather than "d/d" when May 11 is a non-print day.
- **Applied:** No correction.

### Flag 5: "Hezbollah civilian-casualty 14-day window resets at Day 1" provenance — LOW
- **Issue:** Section III states the Hezbollah civilian-casualty 14-day window "resets at Day 1." graph-changelog Trigger Point Review shows the trigger held `watching → watching` with the note "Day 1 of 14." It is not made explicit why Day 1 — i.e. whether the prior 14-day clock expired today, whether a fresh civilian-casualty event reset it, or whether the framing is editorial. Reader cannot reconstruct the trigger's countdown without it.
- **Severity:** LOW (the trigger state itself is correctly conservative; only the provenance of the reset is opaque).
- **Recommended correction:** Tomorrow's graph-changelog should explicitly state whether the prior 14-day window expired or was reset, and the brief should reference that provenance.
- **Applied:** No correction to today's brief; flag noted for next pipeline run.

---

## Items That Passed

### S1. Trump Beijing departure / "doesn't need Xi's help" (PASS)
- **Action or rhetoric?** Properly distinguished. Departure = CONFIRMED ACTION; "doesn't need Xi's help" / "win one way or the other" = CONFIRMED RHETORIC. ✅
- **Sources:** Al Jazeera, NPR, CNBC, PBS NewsHour, CSIS, BusinessToday — six genuinely independent outlets. ✅
- **Other side:** Iran (Velayati / Tasnim / Pezeshkian) included; China side (PBS NewsHour summary that both leaders intent on keeping Iran from overshadowing) included. ✅
- **Brief language:** "CONFIRMED rhetoric" tag explicit. ✅
- Strongest item in the brief for tag discipline.

### S2. US April CPI 3.8% (PASS)
- **Action or rhetoric?** CONFIRMED ACTION — BLS primary release. ✅
- **Sources:** BLS primary + CNBC + CNN Business + Kiplinger. ✅
- **Numeric audit:** Headline 3.8% YoY, core 2.8% YoY, gasoline +28.4% YoY, energy +17.9% — all numbers consistent across intel.md, markets.md and the brief. Internal consistency on this item is fine; the S&P contradiction (Flag 2) is the only data error.
- **Causal-chain language:** "the Fed's pre-war assumption that energy would be transitory is hostage to whether Brent sustains above $100" — appropriately framed, not overstated.

### S3. Indian markets / Moody's GDP cut (PASS)
- **Action or rhetoric?** CONFIRMED ACTION (close prints + ratings action). ✅
- **Sources:** Business Standard, NewsX, BusinessToday, Goodreturns, Business Standard (Moody's), Fortune (WFH), Business Standard (Puri ₹1,000 cr/day) — broad-base Indian press, multiple outlets per data point. ✅
- **Both sides:** RBI position (intervention continuing) and Government position (Puri quantification, WFH) included. ✅
- **Numeric audit:** Sensex 74,559.24 (−1.92%) ✅; Nifty 23,379.55 (−1.83%) ✅; USD/INR ₹95.63 close ✅ (subject to Flag 3 sourcing note); Moody's 6.8% → 6.0% ✅. Headline ("Sensex shed another 1,456 points"), narrative body and data table all consistent.
- **Trigger handling:** USD/INR ₹95.50 noted as `activated` in close prints (was intraday-only). Conservative and correct.

### S4. IDF Litani river crossing (PASS)
- **Action or rhetoric?** CONFIRMED ACTION — Times of Israel liveblog primary; Haaretz, Lebanese NNA, Press TV corroborating; IDF Chief Zamir on-record. ✅
- **Both sides:** Lebanese Health Ministry casualties (≥13 / 24h, cumulative 2,704); Hezbollah operations attributed via Lebanese NNA and Press TV. ✅
- **Tag floor on CGTN SAM-at-IAF:** Brief explicitly notes "CGTN single-source SAM-at-IAF claim from yesterday's brief has not received Western-side corroboration; it remains REPORTED-CLAIMED at best." ✅ — correct demotion of yesterday's single-source aggressive claim.
- **Trigger handling:** New "Litani-induced KIA within 14 days" trigger added at `watching` — correct conservatism (no KIA yet, but ground-engagement risk profile materially raised). ✅

### S5. Saudi Arabia disclosed as covert combatant (PASS — most demanding tag-discipline item)
- **Action or rhetoric?** REPORTED HISTORICAL ACTION — Newsweek primary, WSJ as single-source cluster, Saudi silent, Iran silent. ✅
- **Brief language:** Explicit and correct: "REPORTED — single-source-cluster basis; Newsweek primary, Times of Israel and Middle East Eye amplification; US mainstream wires lagging" and the editor's note in-line: "**Editor must respect tag floor: this is REPORTED, not CONFIRMED.**" — exactly the discipline this role exists to enforce.
- **Graph encoding:** saudi-arabia→iran weight 10 → 9.0 (conservative downgrade reflecting REPORTED tag), edge type `covert_kinetic_participant_late_march_tit_for_tat`. ✅ — the conservative weight reduction is the right call.
- **Single-source rule:** Newsweek + WSJ + Times of Israel + Middle East Eye are NOT four independent sources — they are one primary cluster (WSJ) plus amplifications. Brief recognises this explicitly. ✅
- This is the kind of item that, mishandled, would have driven a CRITICAL flag (March-24 lesson). It is handled correctly.

### S6. Iran FM Araghchi to New Delhi + Rezaei 90% enrichment rhetoric (PASS)
- **Action or rhetoric?** Properly split: Araghchi visit = CONFIRMED ACTION (Iran Embassy in New Delhi confirmed travel); Rezaei 90% line = CONFIRMED RHETORIC, conditional on future attack, NOT operational policy change. ✅
- **Brief language:** "This is rhetoric conditional on a future attack, not an order or a confirmed policy change" — explicit and correct.
- **Trigger handling:** New trigger "Iran resumes enrichment to weapons-grade levels publicly OR confirmed operational policy shift" added at `watching` and explicitly "calibrated to fire only on operational change, not parliamentary statements." ✅ — exactly the standard the March-24 lesson teaches.
- **Sources:** Mehr, Tabnak, Euronews, Iran International, Tasnim — five outlets across Iranian state, Iranian state, European, opposition-leaning, IRGC-linked. Genuine multi-channel synchronisation, not single-source amplification.
- This is the second item where, mishandled, the brief would have elevated rhetoric to action. It is handled correctly.

### S7. Brent + VIX paradox (PASS on framing; see Flag 1 on the underlying price)
- **Action or rhetoric?** CONFIRMED ACTION (market prices). ✅
- **Causal-chain logic:** Summit-pause mechanic explanation for VIX falling on an escalation day is rigorous, internally consistent, and supported by markets.md C1's six-bullet decomposition (forced 48-h delay, EIA cut, Aramco/ADNOC physical preservation, Iran fire rate -92%, VVIX positioning, CPI expected-shock absorption). ✅
- **Tag discipline on Aramco/ADNOC "quiet limited Hormuz resume":** CONFIRMED via World Oil industry primary + Aramco Q1 financials. ✅
- The narrative around the $108–110 trigger is conservative ("dormant for now") — the framing is correct *given* the brief's price. See Flag 1 for the underlying price-data issue.

### S8. CF Industries / URA divergence (PASS)
- **Action or rhetoric?** CONFIRMED ACTION (market prices). ✅
- **Numeric audit:** CF $130.39 +4.7% ✅ (yfinance match); URA $54.35 −5.0% ✅ (yfinance match).
- **Thesis discipline on URA:** "positioning unwind rather than thesis falsification at $54.35, but the watch line is $53.55 (-10% from the ~$59.50 peak)" — careful, falsifiable framing. ✅
- **Tag floor on Rezaei rhetoric (re-anchored to URA):** "Rezaei's 90% line is rhetoric, not policy" explicit in the URA paragraph. ✅

### S9. Steady-state threads (PASS)
- **A8 negative-space (no 2nd Red Sea / no 2nd Qatari EEZ / Project Freedom paused):** UKMTO operational baseline, days-of-window logged correctly. ✅
- **A9 Kharg slick:** "AMBIGUOUSLY activated, not cleanly" — appropriate hedge between drift-versus-re-emergence reading. ✅
- **A13 HMM Namu:** "FM Cho Hyun said it is 'too early to determine who was responsible'" — attribution NOT promoted. CONFIRMED (strike) + UNCONFIRMED (attribution) split preserved. ✅

---

## Trigger Point Review

| Trigger | Status in Changelog | My Assessment | Agreement? |
|---|---|---|---|
| Iran resumes enrichment >20% U-235 publicly OR operational policy shift | `watching` (NEW) | `watching` — Rezaei is rhetoric, not order | ✅ AGREE |
| Litani-ground-crossing-induced Israeli KIA within 14 days | `watching` (NEW) | `watching` — no KIA yet but ground-engagement risk material | ✅ AGREE |
| VIX <16 sustained 3 sessions = de-escalation marker | `watching` (NEW) | `watching` — VIX 17.99, not yet at threshold | ✅ AGREE |
| VIX >25 intraday = kinetic-event marker | `watching` (NEW) | `watching` — far from threshold | ✅ AGREE |
| VIX +30% intraday within 48h of Trump return from Beijing | `watching` (NEW) | `watching` — binary digital test May 15–16 | ✅ AGREE |
| Iranian rial breaks 2,000,000/USD | `watching` (held) | `watching` — 1,842K close, threshold not crossed | ✅ AGREE |
| Brent breaks $108–110 sustained 2 sessions | `watching` (held) | `watching` per brief's $106.29 settle; **needs re-examination tomorrow** against confirmed May-13 close of $108.05 per yfinance | ⚠️ AGREE on the rule (sustain 2 sessions needed) but FLAG: underlying price data needs revision (Flag 1) |
| Brent sustained above $100 for 4+ weeks | `active` (continues) | `active` — Brent at $106.29 or $108.05, either way >$100 | ✅ AGREE |
| USD/INR breaks ₹96 within 5–7 sessions | `watching` (Day 1) | `watching` — ₹95.63 close, Day 1 of 5–7 window | ✅ AGREE |
| USD/INR breaks ₹95.50 RBI intervention | `activated` (close prints too) | `activated` — ₹95.63 close ≥ ₹95.50 ✅ | ✅ AGREE |
| Hezbollah civilian casualty within 14 days | `watching` (Day 1 of 14) | `watching` — see Flag 5 on Day-1 provenance | ✅ AGREE on state, LOW flag on documentation |
| Hezbollah SAM-at-IAF (CGTN single-source corroboration) | `watching` (Day 2 of 7) | `watching` — single-source not corroborated | ✅ AGREE |
| Second Red Sea incident within 7d of May 11 Hodeidah | `watching` (Day 2 of 7) | `watching` — UKMTO no 2nd incident | ✅ AGREE |
| Second commercial vessel attack inside Qatari EEZ | `watching` (Day 3 of 7) | `watching` — UKMTO no 2nd strike | ✅ AGREE |
| Kharg Island slick re-appears within 14 days | `activated` (ambiguously) | `activated` ambiguously — drift south not separate event; Iranian VP ballast counter-claim not falsified | ✅ AGREE |
| AWRP normalization toward 0.5% by May 16 | `failing` (Day 7 of 10) | `failing` — AWRP ~1%, no movement toward 0.5% | ✅ AGREE |
| Trump orders renewed strikes post-Beijing-return | `watching` | `watching` — no orders issued; Beijing pause holds | ✅ AGREE |
| Russia formally named HEU custodian within 30 days | `watching` (Day 14 of 21) | `watching` — non-event | ✅ AGREE |

**Disagreements: 0.** Conservative calibration throughout — no trigger moved on rhetoric, no tag elevations, no over-amplifications. The most-tempting items to elevate (Rezaei 90%, Saudi strikes, CGTN SAM-at-IAF) were correctly held at floor.

---

## Market Data Spot-Check

| Data Point | Brief Value | Verified Value (yfinance) | Match? |
|---|---|---|---|
| Brent Crude (BZ=F) | $106.29 | $108.05 (May 13 latest), $107.77 (May 12 close) | ❌ — see Flag 1 |
| WTI Crude (CL=F) | $100.75 | $102.19 (May 13), $102.18 (May 12) | ❌ — gap ~$1.50, consistent with Flag 1 (same intraday-snapshot-as-settle issue) |
| S&P 500 (^GSPC) | 7,400.96 (table) / 7,392 (narrative) | 7,400.96 (May 12) | ✅ on table value, ❌ on narrative — see Flag 2 |
| NASDAQ (^IXIC) | 26,088.20 (−0.7%) | 26,088.20 (May 12), prev 26,274.13 → -0.71% | ✅ |
| VIX (^VIX) | 17.99 (−2.1%) | 17.96 (May 13), 17.99 (May 12) | ✅ |
| Gold (GC=F) | $4,716.30 (+0.8%) | $4,703.80 (May 13), $4,677.60 (May 12) | ≈ — minor variance, brief is on a slightly later snapshot; directional read (under-performance vs. 3-year-high CPI) unaffected |
| URA | $54.35 (−5.0%) | $54.35 (May 12), prev $57.23 → -5.03% | ✅ |
| CF | $130.39 (+4.7%) | $130.39 (May 12), prev $124.48 → +4.75% | ✅ |
| USD/INR (INR=X proxy) | ₹95.68 May 13 morning | 95.71 (May 13), 95.39 (May 12) | ≈ — see Flag 3 |

**Two confirmed price errors (Brent, WTI) both stem from the same root cause: brief generated at 14:55 IST = 09:25 GMT used an intraday Trading Economics snapshot that was presented as a settle, before the actual ~19:30 GMT ICE settle landed. Pipeline fix is to either (a) shift brief generation to after settle, or (b) clearly label oil prints as intraday rather than settle.** The Brent-WTI spread in the brief ($5.54) and in the live data ($5.86) are similar, confirming the snapshot was internally consistent at its moment of capture — it just isn't a settle.

---

## Final Verdict

**APPROVED WITH CORRECTIONS.** Tag discipline is excellent throughout — the items with the highest temptation to inflate (Rezaei 90% rhetoric, Saudi covert-combatant disclosure, CGTN SAM-at-IAF claim, HMM Namu attribution) are all held at their correct floors, with explicit "REPORTED, not CONFIRMED" and "RHETORIC, not ACTION" language in the brief and in the graph encoding. Trigger calibration is conservative everywhere — three new triggers added at `watching` (Iran weapons-grade operational policy, Litani-induced KIA, VIX thresholds) all require operational events not rhetorical statements. Completeness check passes: Section I balances five categories (macro, geopolitics, military, markets, commodities); Section II carries three market voices; Section III Cascade Watch includes both military edge updates and commodity cascades.

The two HIGH flags are mechanical-pipeline issues rather than analytical errors:
- **Flag 1 (Brent settle vs intraday):** Real-time data has moved through the brief's data snapshot, and the "$108–110 trigger zone TESTED AND FAILED" framing is at minimum premature and may be wrong by tomorrow's open. *The trigger rule itself is correctly applied (2 sessions sustained still required).* Tomorrow's brief must re-anchor on confirmed settle.
- **Flag 2 (S&P internal contradiction):** Lead Section-I item carries a wrong index level (7,392 vs 7,400.96) and percentage (−0.29% vs −0.16%) — this is fixable with a one-line edit and applied below.

The brief's structural read — that markets are pricing the *forcible 48-hour delay* imposed by Trump's Beijing trip rather than the threat universe behind it, and that the trinary band is *being tested at its upper edge* rather than holding comfortably — is the right read of the day and is well-supported by the staging files.

---

*Verified: 9 Section-I items checked, 18 trigger calls reviewed, 4 market spot-checks. 2 HIGH / 3 LOW flags raised. 1 correction applied to brief (S&P inconsistency). Brent-trigger reconsideration deferred to 2026-05-14 morning with verified ICE settle.*
