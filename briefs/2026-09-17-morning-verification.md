# Verification Report — 2026-09-17 (Morning)
Generated: ~13:10 IST | Fact-Checker: Red Team
Brief checked: briefs/2026-09-17-morning.md | Evidence: staging/2026-09-17-morning/{intel,markets,graph-changelog}.md; yfinance re-pull; 3 independent web checks

## Summary
31 items checked (7 Section I items × 6 checks where applicable; 6 Section II takes; 3 trigger changes + 1 new edge + 2 down-weights; 8 market data points; completeness). **9 flags → 9 corrections applied (2 HIGH, 7 LOW). 0 CRITICAL.** No trigger moved on rhetoric. Brief APPROVED WITH CORRECTIONS.

---

## Flags

### Flag 1 (HIGH): Kurdistan strikes — actor stated as fact
- **Issue:** Brief: "Iran did fire five missiles into Iraqi Kurdistan." The `iran` and `iraq` node signals said "Iran fired"/"IRAN struck"; `iran → iraq` was raised +1.0 as "CONFIRMED (3 sources)."
- **Evidence:** Rudaw, Asayish and IranWire confirm five missiles STRUCK three Sulaimani sites (the event). Iranian ORIGIN is attributed by the Kurdistan Region Security Agency and Komala; **"Iran has not commented"** (Rudaw). No IRGC claim, no imagery of launch origin. That is an attributed action, not a confirmed actor.
- **Correction:** Brief rewritten — "an attack the Kurdish authorities attribute to Tehran, which has not commented." `iran`/`iraq` signals reworded to "attributed… Tehran silent." `iran → iraq` 8.5 → **8.0** (+0.5, attributed-action level). Changelog patched. **Applied: Yes.**

### Flag 2 (HIGH): New edge seeded above precedent
- **Issue:** `saudi-arabia → shipping-tankers` created at 6.0 using "2 activations × 1.0 × 3.0" — but there was one day of evidence, and the Vortexa loading figure reached the pipeline only via the GlobalSecurity aggregator (not read at source).
- **Evidence:** edges.json precedent for new 2-source edges: 4.0–5.0 ("Initial weight 4.0 (new, 2-source, causally clean)"). Axios (US official) + Frontline price action are independent; Vortexa is second-hand.
- **Correction:** weight **6.0 → 5.0**; node `top_edges` and changelog synced; brief text updated. **Applied: Yes.**

### Flag 3 (LOW): Dated Brent — single assessor's figure presented as the level
- **Issue:** "Dated Brent traded above $130 (Bloomberg)… a >$20 premium." The oprep also cited Reuters at ~$122, which would be a ~$13 premium.
- **Evidence:** Independent check: Energy Intelligence ("more than $20/bbl premium to front-month") and a second market letter corroborate >$130; Reuters' ~$122 stands as a lower assessment. Two sources support the brief's figure; the discrepancy should still be visible.
- **Correction:** "$122–130+ depending on the assessor, a $15–20+ premium" in both Section I and Section III. **Applied: Yes.**

### Flag 4 (LOW): Gold phrasing conflated Wednesday's move with Thursday's level
- **Evidence:** Yahoo: gold −1.15% Wednesday; yfinance GC=F Wed close $4,387.5, live Thu $4,325–4,337 (another −1.4%). TheStreet's "$4,263.91" is inconsistent with both and was not used. The brief's "$4,337 −1.1%" mixed the live level with Wednesday's percentage.
- **Correction:** "fell ~1.1% on the decision and trades ~$4,330 this morning." **Applied: Yes.**

### Flag 5 (LOW): "first 5-handle of the cycle"
- **Evidence:** Node history (max 4.97% pre-decision) supports "since the war began"; "of the cycle" is ambiguous (the 10Y touched 5% in Oct 2023).
- **Correction:** "first close above 5% since the war began." **Applied: Yes.**

### Flag 6 (LOW): Shanghai INE "record $138" — aggregator-only
- **Correction:** "reportedly." **Applied: Yes.**

### Flag 7 (LOW): Kpler transit counts (4 on Tue; 10-day avg 18) — reached via aggregator citing Reuters/Kpler
- **Evidence:** Consistent with straits.live/Reuters "8 on 13 Sep" and the 14-Sep brief's 7/day, but not read at source.
- **Correction:** attributed as "Reuters/Kpler data." **Applied: Yes.**

### Flag 8 (LOW): "has cost them Qatar" — a statement presented as a strategic outcome
- **Correction:** "cost them Qatar's neutrality, at least rhetorically." **Applied: Yes.**

### Flag 9 (LOW): Edge figures in Section III/footer needed syncing after Flags 1–2
- **Applied: Yes.**

---

## Items That Passed

### Fed hike (PASS)
- **Action:** FOMC statement — the highest-grade source. 12–0 confirmed by Fox Business, Schwab, CNBC independently; the Yahoo "three dissents" line was correctly traced to July. Dot median "one more" (12–16 of 18 — the count discrepancy is noted in intel, and the brief uses only the median). ✅
- **Quotes:** Warsh lines verbatim from Yahoo live blog; Trump Truth Social from CNBC/Yahoo. ✅
- **Other side:** Trump's reaction included; Brazil's cut noted in markets. ✅
- **Market reaction:** yfinance: 10Y 5.01–5.02 ✓, Dow −1.2 ✓, XLE −2.88 ✓, VIX 17.71 ✓. **CBO "40% of Q2 PCE"** — independently verified (NBC; syndicated CBO report coverage). ✅

### Brent six settles / retrace (PASS after Flag 3)
- **Data:** yfinance daily closes 9–16 Sep: 101.21, 107.63, 104.61, 105.68, 108.75, 105.83 — exactly six >$100; Wed −2.7% ✓. ✅
- **Causation:** Bloomberg half-capacity (via Investing.com) + Wright to CNBC — both on the record; CNBC's own "weeks" caveat carried. ✅
- **Restart NOT claimed as fact:** "no tracker has yet confirmed… Nothing has restarted" — correct. Yanbu-zero: Vortexa via oprep AND OilPrice independently. ✅

### Washington wind-down (PASS)
- **Rhetoric labelled:** "All of this is rhetoric and scheduling." ✅ Vance quotes: NY Post interview carried verbatim by 4 outlets. Trump 17 Sep: ToI liveblog timestamped. GCC meeting: Axios scoop, hedged "Axios reports." ✅
- **Actions:** House 220–204 (AP, Al Jazeera — independent) ✓; recess (WaPo, CNBC, US News) ✓; IG (CBS, NBC, France 24) ✓; CBO (CNBC, Roll Call, CNN) ✓. ✅
- **Other side:** Rezaei's "Period!" closes the paragraph. ✅

### Iran's two voices (PASS after Flag 1)
- Pezeshkian: India Today via 3 outlets ✓. Rezaei: Press TV primary, dated 14 Sep (Time's "Monday, Sept. 15" is a date error in Time; Press TV's own date used) ✓. "Press TV did not mention the president" — verified by reading the Press TV page ✓. Rasaei motion — single aggregated thread, hedged in the brief ✓. Araghchi/Tasnim contradiction — TASS + Reuters/Al-Monitor ✓. Amini strike — Iran International + IranWire + Euronews ✓. ✅

### India (PASS)
- CPI 4.82% (MoSPI via Bloomberg + Business Today) ✓; WPI 8.3% (BS) ✓; HSBC/Nomura/StanChart (BS, FXStreet) ✓; Nifty Tue 23,118.60 (HDFC Sky; yfinance Wed 23,217.60 ✓); ₹96.00 open (BS) — yfinance shows 95.83–95.99, the brief already flags the lag ✓; GOI 7.06% (TE) ✓; RBI intervention hedged "Reuters cites three traders" ✓. FPI gap disclosed. ✅

### Houthis / Mecca / Germany meeting (PASS after Flags 7–8)
- Interception: coalition statement (Al Jazeera, CNBC) ✓; Houthi denial verbatim (Saba via Euronews) ✓; F-15 "without evidence" ✓; Qatar quotes (ToI) ✓. Germany meeting: Axios WITH CENTCOM confirmation — meets the 2-source bar ✓. Tihamah correctly excluded as 12-Aug stale ✓. **Non-event** (no merchant attack) is the lead of the paragraph — correct proportionality. ✅

### Firebreak / Lebanon / Israel (PASS)
- Non-events from oprep cross-checked against CENTCOM releases and search (no strike reports) ✓; State Dept meeting (ToI) ✓; polls (JPost, ToI) ✓. ✅

### Section II (PASS)
- Goldman quote (TheStreet/CNBC) ✓; Cahill is a test-update, not a repeat ✓; RBI trio is new ✓; CBO framed as source ✓; Time trio ✓; Krieg is a day-count on a running test, one line ✓. Balance: 3 market / 3 geopolitical. ✅

---

## Trigger Point Review

| Trigger | Changelog | My assessment | Agreement? |
|---|---|---|---|
| fed — 16-Sep hike or hold | FIRED (hike) | FOMC statement = confirmed action; 3+ outlets | ✅ AGREE |
| brent-crude — >$100 5+ sessions | FIRED | yfinance: 6 settles >$100 (independently re-pulled) | ✅ AGREE |
| india — Aug CPI ≥5.0% OR RBI hawkish | CPI leg unfired; watching | 4.82% (MoSPI); RBI leg is forecast only | ✅ AGREE |
| saudi-arabia — RESTART | watching (not fired) | Correct — Wright/Bloomberg are guidance; Yanbu zero | ✅ AGREE — the most important non-move |
| houthis — non-Saudi hull | watching | No UKMTO/JMIC incident | ✅ AGREE |
| strait-of-hormuz — 15+/day | watching | US 40/day = claim | ✅ AGREE |
| iran — accepts direct talks | watching | Conditional offer negated | ✅ AGREE |
| brent-crude — >$130 (futures) | watching | Correctly NOT pre-fired on Dated print | ✅ AGREE |
| 5 new watches | watching | All dated/binary; none pre-judged | ✅ AGREE |
| Edge: iran → iraq +1.0 | 8.5 | Attribution not confirmed → +0.5 | ❌ DISAGREE → corrected to 8.0 |
| Edge: saudi → tankers 6.0 (new) | 6.0 | One day's evidence; precedent 4–5 | ❌ DISAGREE → corrected to 5.0 |
| Edges: qatar→urea 9→7; urea→india 10→8 | down | Argus/CRU + Fertilizer Daily + TE — data-driven | ✅ AGREE |
| houthis → saudi: no change on Mecca | held | Correct: CLAIMED attribution | ✅ AGREE |

## Market Data Spot-Check (yfinance re-pull, ~13:00 IST)

| Data point | Brief | Verified | Match? |
|---|---|---|---|
| Brent Wed settle | $105.83 (−2.7%) | 105.83; Tue 108.75 | ✅ |
| Brent settles >$100 | six (9–16 Sep) | 101.21/107.63/104.61/105.68/108.75/105.83 | ✅ |
| US 10Y | 5.02% close / 5.01% | 5.00→5.01 (^TNX) ; TheStreet 5.02 | ✅ |
| Frontline | +4.0% | +4.03% (51.59→53.67) | ✅ |
| XLE | −2.9% | −2.88% | ✅ |
| VIX | 17.71 | 17.71 | ✅ |
| Nifty Wed | 23,217.60 | 23,217.60 | ✅ |
| Gold | ~$4,330 (−1.1% Wed) | GC=F Wed 4,387.5 → Thu 4,325.5 live | ✅ after Flag 4 |
| USD/INR | ₹96.00 open (BS) | yfinance 95.83–95.99 (lag noted in brief) | ✅ with caveat |

## Completeness (Check 7)
- Section I: 3 market / 4 geopolitical ✅. Section II: 3 market voices ✅. Section III: commodity cascades (gold regime, Dated Brent, tankers, urea down-weights, TTF gap) present ✅. Graph: every node in both staging files' "Nodes affected" lists carries `last_updated: 2026-09-17` (programmatic check: 0 skipped) ✅. Gaps disclosed to the reader: VLCC print, war-risk print, NSDL FPI, India VIX ✅.
- **Length:** Page 1 ~3,600 words — over the 5-minute rule, in line with the last three briefs. Not a factual issue; noted for the PO.

## Final Verdict
**APPROVED WITH CORRECTIONS.** The pipeline held its most important line — three triggers fired on hard data, five high-profile rhetorical items (Vance, Trump, Pezeshkian, Rezaei, Wright/Bloomberg) and three contested claims (US 40/day, Mecca attribution, IRGC MQ-1s) were all held at their tags. The two HIGH corrections were both in the direction of over-confidence about *who* acted (Kurdistan) and *how much* new evidence a single day provides (the new edge) — the classic errors, caught before the reader saw them.
