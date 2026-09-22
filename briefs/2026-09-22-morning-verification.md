# Verification Report — 2026-09-22 (Morning)
Generated: ~12:20 IST | Fact-Checker: Red Team
Brief checked: briefs/2026-09-22-morning.md against staging/2026-09-22-morning/{intel,markets,graph-changelog}.md

## Summary
34 items checked (7 Section I items × 6 checks, Section II takes, Section III graph figures, Page 2 spot-check, graph node/edge review, completeness). **11 flags → 11 corrections applied (3 HIGH, 8 LOW). 0 CRITICAL.** No tag drift found on the five priority items; no trigger moved on rhetoric.

---

## Flags

### Flag 1: "the first attack on the capital of the cycle" (Riyadh) — HIGH
- **Issue:** Over-claim. Iran struck Gulf capitals in June (graph: `brent-crude` 10-Jun context, "Iranian strikes on three US-allied capitals"). Al Jazeera's own framing is "first air-raid alert in Riyadh since the July escalation began."
- **Correction:** "the first Houthi attack on the Saudi capital of this war and the first Riyadh air-raid alert since the July escalation." Applied in brief, `saudi-arabia` signal, `houthis → saudi-arabia` edge context, changelog. **Applied: Yes.**

### Flag 2: "six houses now expect 25bp" / "six-house consensus" — HIGH (number)
- **Issue:** Only five houses are named in staging for the October hike (HSBC, Nomura, StanChart, Citi, SBI Research); ICICI Sec PD/IDFC First are yield calls, not hike calls.
- **Correction:** "five houses… (HSBC, Nomura, Standard Chartered, Citi, SBI Research)" in Section I, II and III. **Applied: Yes.**

### Flag 3: Krieg 14-day test "day 10 … four days remain" — HIGH (date arithmetic)
- **Issue:** The 17-Sep brief had the test at day 6 with eight days remaining → 22 Sep is day 11, three remain, expiry ~25 Sep (not ~28 Sep). Researcher and Graph Engineer both carried "day 10".
- **Correction:** Day 11 / three days / ~25 Sep in Section II, III, Risk Landscape, dated tells; `houthis` and `brent-crude` trigger notes and signals; changelog. **Applied: Yes.**

### Flag 4: "below $100 intraday for the first time since 9 September" — LOW
- **Issue:** Settles were >$100 from 9 Sep; intraday lows on 9–10 Sep not verified. Inference presented as fact.
- **Correction:** "for the first time in roughly two weeks." **Applied: Yes.**

### Flag 5: "with Riyadh's airport fuel farm smouldering" — LOW
- **Issue:** Implies the fire was still burning on Sunday; unsupported. **Correction:** "a day after a fire at Riyadh's airport fuel farm." **Applied: Yes.**

### Flag 6: "Reuters imagery and the WSJ showed black smoke from a jet-fuel facility" — LOW (conflation)
- **Issue:** Reuters imagery showed smoke from the fuel-storage *area*; the WSJ *reported* a strike on a jet-fuel facility. **Correction:** attribution separated. **Applied: Yes.**

### Flag 7: "in Al Jazeera's phrase, 'referenced, not activated'" — LOW (attribution)
- **Issue:** The phrase is the fetch summary's paraphrase, not a verified Al Jazeera quote. **Correction:** "invoked in speeches but not formally activated," no attribution. **Applied: Yes.**

### Flag 8: "against ~125 a day before the war… counts sit near 15% of normal" — LOW (unit mixing)
- **Issue:** gCaptain's 17 (weekend) / 37 (prior week) / ~125 figures mix periods; "15%" was not in staging (UKMTO: ~90% below pre-conflict). **Correction:** "pre-war norm of well over 100 a day… roughly 90% below pre-conflict levels (UKMTO)." **Applied: Yes.**

### Flag 9: Nifty "+1.5% off its 15 September low" at 23,414 — LOW (arithmetic)
- **Issue:** 23,414.30/23,118.60 = +1.28%; +1.5% applies to the live 23,463. **Correction:** "+1.3% off its low; ~23,410–23,460 live." **Applied: Yes.**

### Flag 10: "Lagarde said on Thursday" — LOW (date)
- **Issue:** Bloomberg piece dated 18 Sep = Friday. **Correction:** Friday. **Applied: Yes.** (Also: "Wang Yi… on Friday" → "on 19 September".)

### Flag 11: "no US strike ashore in twelve operational periods" — LOW
- **Issue:** Oprep count of 12 is as of 19 Sep; by 22 Sep it is higher. **Correction:** "at least twelve." **Applied: Yes.**

## Items That Passed

### Brent −7.7% to $100.34 (PASS)
- **Action or rhetoric?** Confirmed price action; drivers correctly split into rhetoric (Trump), non-action (cancelled strike), official claim (Cooper) and physical (Ras Tanura loadings). ✅
- **Numbers:** Nov Brent 15→21 Sep: 108.75 / 105.83 / 104.82 / 103.87 / 100.34 (yfinance BZX26) — four declines, −7.73%. Live $101.69 at check (brief "~$101.5"). ✅ Contract-roll correction carried into header and Page 2. ✅
- **Other side:** Ghalibaf/Zolqadr closure line included. ✅
- **Physical premium:** "are reported above $130" — hedged as REPORTED. ✅

### Houthi strike ordered/cancelled (PASS on tags)
- "Reports in the NYT, corroborated in part by Axios and Reuters" — REPORTED language preserved; "per an American official" attribution preserved; Trump on record. ✅ The unsupported "Saudi plea caused the stand-down" framing (Euronews/JPost headlines) is NOT in the brief. ✅

### Hormuz tanker strikes (PASS)
- UKMTO = operational source; "attributed none… Iran has claimed none" stated explicitly; JMIC assessment attributed. ✅ Enforcement trigger not re-fired in changelog. ✅

### Seven conditions via Qatar (PASS)
- "told Al Jazeera… neither Doha nor Washington has confirmed receipt, so this is one side's account of a document." REPORTED handled correctly. ✅ Trump's offer: "no Iranian institution has acknowledged" (IranWire). ✅

### India (PASS after Flags 2/9)
- INR 95.81 (PTI provisional; yfinance 96.01 Mon is a different fix — brief uses the PTI close consistently). Reserves $780.782bn −$4.924bn (RBI via BS ×2). FPI ₹23,676 cr (NSDL via ET — single outlet, brief attributes to NSDL). OMO ₹25k cr Mon / 28 Sep (BS). ✅ Baseline correction disclosed to the reader. ✅

### VIX / Nasdaq (PASS)
- VIX 15.44 / 14.81 / 14.87 (yfinance) ✅; Nasdaq 27,122.09 +2.26% ✅; SMH +4.0% ✅; ~75/25 attribution matches markets C2. Trigger written as complacency per node caveat. ✅

### Quiet threads (PASS after Flags 10/11)
- Israel polls 22.2/21.2/54.4 (JPost 17 Sep) ✅; ECB hold REPORTED — brief states it plainly but does not quote rate levels (stale-year risk avoided). ✅

## Trigger Point Review
| Trigger | Changelog | My assessment | Agreement? |
|---|---|---|---|
| `vix` <16 ×3 sessions | fired | Three yfinance closes <16 — data. Caveat carried into brief. | ✅ AGREE |
| `ecb` September hike | expired (unfired) | Hold + Lagarde quote; no levels encoded. | ✅ AGREE |
| `saudi-arabia` escalates alone / Mecca Pact (by ~5 Oct) | new, watching | Dated, resolvable on on-ground reporting/official activation. | ✅ AGREE |
| `china` Trump–Xi readout (25 Sep) | new, watching | Resolvable on official text. | ✅ AGREE |
| `brent-crude` >$100 2 weeks | watching | $100.34 settle; correctly "tested, not resolved." | ✅ AGREE |
| `saudi-arabia` RESTART | watching | No Aramco/tracker print; substitute not accepted as restart. | ✅ AGREE |
| `strait-of-hormuz` enforcement (UKMTO-verified, Iran fires) | active (carried), not re-fired | Attribution absent — correct. | ✅ AGREE |
| `houthis` non-Saudi hull | watching | None; pledge = rhetoric; day count corrected to 11/14. | ✅ AGREE (after Flag 3) |
| `united-states` Houthi strike | watching | Ordered/cancelled ≠ struck. | ✅ AGREE |
| `iran` Pezeshkian endorsed/sidelined; accepts talks; meeting convenes | watching | Neither; US offer + silence; no venue. | ✅ AGREE |
| `india` FPI >₹25k cr | watching | ₹23,676 cr. | ✅ AGREE |
| `united-states` Trump–GCC 22 Sep | watching (pending) | Event is today. | ✅ AGREE |

## Edge Weight Review
`houthis → saudi-arabia` 7.0→8.0 (confirmed missile at capital + fire + civilian death) — justified. `saudi-arabia → shipping-tankers` +0.5, `brent → 10Y` +0.5, `semis/kospi → nifty` +0.5 each, `china → hormuz` +0.5 — one confirmed activation each; modest. `oman → united-states` 3.0→5.0 on REPORTED-strong + outcome — the largest sub-cap move; acceptable given the mechanism change and the Engineer's own tempering from 6.0. New `houthis → united-states` 6.0 on a REPORTED-strong outcome — acceptable at 1st-order; would flag if >7. `saudi-arabia → european-ttf-gas` 4.0 seeded as watch-edge on single-origin Bloomberg — acceptable at 4.0. No edge moved on rhetoric alone. ✅

## Market Data Spot-Check
| Data point | Brief | Verified (yfinance 12:15 IST) | Match |
|---|---|---|---|
| Brent Nov settle Mon | $100.34 | 100.34 (BZX26) | ✅ |
| VIX Thu/Fri/Mon | 15.44/14.81/14.87 | 15.44/14.81/14.87 | ✅ |
| Nifty Mon close | 23,414.30 | 23,414.30 | ✅ |
| Nasdaq Mon | 27,122.09 | 27,122.09 | ✅ |
| Gold Mon | $4,383.90 | 4,383.90 | ✅ |
| TTF Mon | €73.25 (−7.9%) | 73.25 (from 79.52 = −7.9%) | ✅ |
| USD/INR Mon | 95.81 (PTI provisional) | yfinance 96.01 (different fix) | ✅ (source stated) |

## Completeness
Section I: 7 items — 4 carry market/commodity substance (oil, India, equities/VIX/gold/TTF, ECB), 3 geopolitical. ✅ Section II: 4 market/commodity voices (JPM, Kpler, Eurasia, Indian sell-side) + 4 geopolitical (Vaez/Vakil, NYT official, Krieg, Kpler-as-check). ✅ Section III: commodity cascades (VIX, TTF watch-edge, shipping two-leg, capital substitution, gold regime) alongside military edges. ✅ Graph: all "Nodes affected" in both staging files appear in the changelog (50 nodes); `europe`-side nodes (ecb, ttf, natural-gas-lng, cheniere) updated. ✅ Gaps disclosed to reader: war-risk premium (4th brief), TD3C (15 Sep), JMIC PDF, Qatar confirmation. ✅

## Final Verdict
**APPROVED WITH CORRECTIONS.** No rhetoric was elevated to action and no trigger moved on words; the three HIGH flags were an over-claim ("first attack on the capital"), a count ("six houses"), and a day-count drift on Krieg's test — all fixed in brief and graph. Reading length (I–III ~3,700 words) is consistent with the last two multi-day editions but above the 5-minute ideal; flagged, not corrected.
