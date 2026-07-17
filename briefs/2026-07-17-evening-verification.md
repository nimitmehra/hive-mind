# Verification Report — 2026-07-17 (evening)
Generated: ~23:30 IST | Fact-Checker: Red Team
Brief checked: briefs/2026-07-17-evening.md

## Summary
6 Section-I items + 16 trigger decisions + 9 market data points checked. **5 corrections applied (1 editing defect, 1 HIGH, 3 LOW).**

## Flags

### Flag 0 (editing defect, caught pre-verification): garbled sentence in Section III
- **Issue:** "oil (violently, into five-year-low inventories nothing — wait, downward)" — a broken draft fragment survived into the Signal You Might Miss paragraph.
- **Severity:** HIGH (readability/credibility, not factual)
- **Correction:** Rewritten to "De-escalation now *reverses downward*: oil, CF Industries... and *rescues* the rupee..." **Applied.**

### Flag 1: Seafarer deaths — two source chains merged into one attribution
- **Issue:** "two seafarers confirmed dead by the IMO — both Indian nationals" equated the IMO's count with separate Indian-casualty reporting (GFS Galaxy 11 Jul; Al Bahyah/Mombasa B 14 Jul). Plausibly the same two people; the equation is an inference, not a sourced fact.
- **Severity:** HIGH (tag drift by merger)
- **Correction:** "the IMO confirming two seafarer deaths — Indian-casualty reporting identifies two Indian nationals killed in the window." **Applied.**

### Flag 2: Kimi K3 "released Wednesday" — 16 July 2026 was a Thursday
- **Severity:** LOW (factual slip)
- **Correction:** "released Thursday." **Applied.**

### Flag 3: Karari release printed flat; staging tags it REPORTED (single Reuters-origin chain)
- **Severity:** LOW (tag drift)
- **Correction:** "reportedly released (Reuters chain)." **Applied.**

### Flag 4: jordan node skipped by the Graph Engineer
- **Issue:** Jordan intercepted 8 Iranian missiles (9 Jul) — listed in intel A1's affected states; the jordan.json node exists and was not updated.
- **Severity:** LOW (graph completeness)
- **Correction:** Signal added to jordan node (CONFIRMED interceptions); viewer rebuilt. **Applied.**

## Items That Passed (evidence)
- **Item 1 (deal dead):** every limb multi-chain CONFIRMED (talks-fail negative finding; six strike nights; blockade; Gharibabadi IRIB statement). "Formal repudiation *in substance*" is the correct hedge — he did not utter a treaty-law renunciation. The Araghchi-message chain and the hawks-vs-Witkoff split are explicitly marked single-chain/REPORTED in the prose. ✅
- **Item 2 (Hormuz):** closure encoded as REAL on evidence (vessel kills), explicitly distinguished from the June rhetoric episode — the discipline cuts both ways and did. Transit-count conflicts (10 vs 14 on 12 Jul) carried, not resolved silently. CENTCOM's 8-mb escort claim tagged as a claim. ✅ (after Flag 1)
- **Item 3 (oil/Fed/gold):** all prints verified against script JSON (Brent 86.09, gold 4,009.50, 10Y 4.52); hike odds attributed as market-implied; June CPI framing (backward-looking) matches the attribution sweep's sourced reasoning. ✅
- **Item 4 (three crises):** the 65/35 KOSPI split and the wheat-is-Russia attribution are the brief's most valuable discipline — both rest on 2+ named-catalyst chains (lawsuit filing date, BoK statement, Kerch/WASDE). Nikkei print conflict flagged in-text rather than picking a side. ✅ (after Flag 2)
- **Item 5 (India):** all hard data verified (closes, FII dailies with single-source days flagged, RBI reserves, CPI/WPI); the CDSL +15,157 cr figure correctly framed as pre-reversal; deadline conflict (22 vs 24 Jul) carried. ✅
- **Item 6 (containment):** all four negative findings (no Hezbollah front, no Israeli strikes, no proxy mobilization, nuclear complex untouched) are search-documented absences across independent sweeps — the strongest kind. ✅ (after Flag 3)

## Trigger Point Review (the critical gate)
| Decision | My assessment | Agreement |
|---|---|---|
| signed-deal → COLLAPSED | All three pre-written conditions fired on confirmed actions + an authoritative official statement. The 4-Jul hold and the 17-Jul flip are the same discipline applied to opposite evidence. | ✅ AGREE |
| Hormuz "reopens" → reversed_closed; ">30×3" → failed_reversed | Operational data (49→3/day), declaration + kills + blockade | ✅ AGREE |
| "US naval escort/forced opening" → fired_active | The Day-1 trigger's exact scenario is occurring (blockade + escorts + counter-strikes on tankers) | ✅ AGREE |
| Brent & India sub-$85 → reversed_unfired | Price tape ($84.73 settle 14 Jul, $86 Fri) — the graph unwound its own state | ✅ AGREE |
| 10 holds (rial ~4% away, Mojtaba, VIX, ₹95, Kharg, direct-talks, etc.) | Each held with dated evidence notes; Kharg "takeover" musing correctly kept as rhetoric | ✅ AGREE |

**Zero rhetoric-driven trigger movements. The Asia crash was NOT wired to the war (kospi↔helium +1.0 only). Wheat was billed to Russia. This is the attribution discipline working under maximum drama.**

## Market Data Spot-Check
| Point | Brief | Verified | Match |
|---|---|---|---|
| Brent | $86.09 | 86.09 (script JSON) | ✅ |
| KOSPI | 6,820.60 / −6.4% | 6,820.60 | ✅ |
| Nifty / Sensex | 24,334.30 / 78,151.45 | script + multi-source | ✅ |
| USD/INR | 96.27–96.30 | 96.27 script | ✅ |
| Gold | $4,009 | 4,009.50 | ✅ |
| VIX | 18.3–18.4 | 18.31/18.42 (dual prints carried) | ✅ |
| US 10Y | 4.52% | 4.52 | ✅ |
| FII 5-day | ~−₹6,950 cr | sums from dailies | ✅ |
| Nikkei | conflict flagged in-text | script −2.8% vs wires −4/−5.2% | ✅ (honestly carried) |

## Completeness Check
Section I: 3 geopolitical / 3 market-weighted ✅. Section II: geopolitical (Brew, ISW) + market (Goldman/Croft, Polymarket) + tone ✅. Section III: commodity cascades (fed→gold, urea→india, kospi↔helium, russia↔india) alongside military ✅. Changelog-vs-staging node audit: complete after Flag 4 (49 nodes total). Negative findings promoted to a full Section-I item (Item 6) — the correct weight for the fortnight's most decision-relevant intelligence. ✅

## Final Verdict
**APPROVED WITH CORRECTIONS** (5 applied). The brief's central claims — deal collapsed on pre-written conditions, closure operationally real, the Asia crash majority-non-crisis, wheat belongs to a different war — all survive adversarial checking on multi-chain evidence. The graph moved a lot today and every movement is auditable.
