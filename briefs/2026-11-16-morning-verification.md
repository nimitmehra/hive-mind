# Verification Report — 16 November 2026 (Day 262), morning edition
Generated: 12:54 IST Mon 16 Nov (`date`-checked) | Fact-Checker: Red Team
Brief checked: `briefs/2026-11-16-morning.md` (read-only; not edited)

## Summary
I checked 9 Section I items (61 discrete claims), the Updates box, the Signal, Deployment and the hold rule, 5 new calls and 9 scorecard rows, the trigger rulings (135 reviewed per the changelog), the new edge, the 4 rewritten summaries, and 44 market data points against a fresh yfinance pull (12:46 IST; 1-minute bars for Brent, gold, DXY, the Nifty and the rupee; closing bars for Korea, Taiwan and Japan). A forked agent ran web spot-checks on 12 claim groups.

**Flags: 1 CRITICAL, 4 HIGH, 12 LOW. Graph corrections: 6 (G1–G6). Trigger status changes: none. I agree with every trigger ruling.**

- **CRITICAL:** the KOSPI and Samsung closes are stale pre-auction prints. Our own 12:34 IST pull, my re-pull and a web source all give KOSPI **5,100.50 (−3.59%)**, not 5,082.39 (−3.94%). Samsung is **196,800 (−4.5%)**, not 195,800 (−5.0%).
- **HIGH:** (1) The NYT's "new" energy target list is not new: our own 26-Oct brief and graph recorded energy targets in the NYT's October reporting. (2) "Reuters says government forces retook Dhubab in October, which our record had missed" is wrong: our graph has recorded the Dhubab airfield taken since 13 Oct. (3) "Only oil moved", and the ~65% crisis share on the unexplained 11:17 IST rise: gold fell $27 in the same minutes. (4) The Bahrain heading re-presents Sunday morning's fire, which was in the 15-Nov brief, as news.

The lead (no strike on night thirteen), the FII correction (re-derived: **ten** is right), the Yemen withdrawal, WPI, the hold-rule logic and nearly all prices hold.

---

## Flags

### Flag C1 — KOSPI and Samsung closes (market data)
- **Brief text:**
  - Section I heading: "Asian chip stocks fell hard (Taiwan −6%, Korea −3.9%)".
  - Section I: "**Korea:** −3.9%. SK hynix fell 7.9% and Samsung 5.0%."
  - Page 2, Significant Moves: "**−6.0% / −3.9%**" and "−7.9% / −5.0% / −5.7%".
  - Page 2, Snapshot: "**5,082.39 / 1,120,000 / 195,800**".
  - Section III: "`kospi` below 5,000: 5,082 at the close."
- **Issue:** these are wrong at their stated basis, "close".
- **Evidence:**
  - `spot-raw-1211IST.txt` shows ^KS11 5,082.39 and 005930.KS 195,800.
  - The desk's own later pull (`spot-raw-1234IST.txt`) shows **^KS11 5,100.50** and **005930.KS 196,800**. My 12:46 IST re-pull agrees (daily bar C 5,100.50, L 5,069.83). The 12:11 pull came about 20 minutes after Korea's 15:30 KST close, so the delayed feed was showing the price from before the closing auction.
  - A web source gives KOSPI **−3.59%**, which matches 5,100.50 against Friday's 5,290.53 exactly.
  - SK hynix (1,120,000, −7.89%), TAIEX (41,040.08, −6.03%) and TSMC (2,215, −5.74%) did not change between the two pulls. They are correct.
- **Severity:** CRITICAL (wrong market data).
- **Recommended correction:**
  - Heading: "(Taiwan −6%, Korea −3.6%)".
  - Section I: "**Korea:** −3.6%. SK hynix fell 7.9% and Samsung 4.5%."
  - Page 2, Moves: "**−6.0% / −3.6%**" and "−7.9% / −4.5% / −5.7%".
  - Page 2, Snapshot: "**5,100.50 / 1,120,000 / 196,800**".
  - Section III: "`kospi` below 5,000: 5,100.50 at the close."
  - If the CoS can reach KRX or a wire close in 2 minutes, use that figure. Samsung's Friday base is 206,000 in the yfinance history; yfinance's `previousClose` field says 207,000, which would make it −4.9%. Confirm before printing a decimal, or write "about 4.5–5%".
- **Applied:** No (the CoS applies).

### Flag H1 — "The new element is the target list" (NYT plans), which also feeds the Signal and the case against
- **Brief text:**
  - Section I: "The paper reported strike plans on 22 October too. The new element is the target list: October's relays said targeting would avoid oil infrastructure."
  - Signal: "What has changed is the posture (a third carrier) and the reported target list." Signal headline: "It would also be the one kind of strike that hits the oil supply directly."
  - Case against: "the reported strike plans now include the one target set that would move oil sharply".
  - Risk Landscape: "(a third carrier; reported energy targets)" is listed under Intensifying.
- **Issue:** the claim is contradicted by our own record.
- **Evidence:**
  - **Our 26-Oct brief** (line 37): "**NYT:** a short US–Israeli campaign after the election against nuclear, energy and missile targets."
  - **The 26-Oct intel, DIP-A3:**
    - The NYT on 21 Oct reported a campaign on "nuclear sites, energy infrastructure, and missile and drone capabilities".
    - The NYT on 24 Oct reported CENTCOM's expanded target list including "**energy infrastructure and other facilities vital to Iran's economy**". That is word for word the phrase this brief quotes as new.
    - One Israeli source said power plants were excluded.
  - **The `united-states` RESUME trigger, note of 4 Nov:** "NYT (3 Nov)… a three-day campaign on missile/drone arsenals, IRGC command and energy targets".
  - **The web check:** The Nightly's 22-Oct relay says the targets "would likely include Iran's energy infrastructure". It is the same relay that says some officials said targeting "will avoid refineries and oil infrastructure". So October's reporting was mixed; it did not exclude energy.
  - DIP's own A-3 notes that the Monday relays give "no date" for the NYT piece.
  - The "one kind of strike that hits the oil supply directly" line is a superlative. US strikes on Iranian tankers in September (tanker-for-tanker) also hit oil supply directly.
- **Severity:** HIGH (a significant factual error that drives the Signal's "what has changed").
- **Recommended correction:**
  - Section I: "The paper reported strike plans in October too, and its 24-October story already listed 'energy infrastructure and other facilities vital to Iran's economy' (in our 26-October brief), though some relays said refineries would be spared. So the target list is not new. What is new is the timing: the report follows Sunday's fire and comes as a third carrier arrives."
  - Signal: "What has changed is the posture (a third carrier) and the renewed reporting. Energy targets were in October's reporting too." Headline: "…It would also hit oil supply directly, which interceptions over Bahrain and claims about mines have not."
  - Case against: "the reported strike plans include energy targets, which would move oil directly".
  - Risk Landscape: "US military posture (a third carrier; the strike-plans report renewed)".
- **Applied:** No.

### Flag H2 — "which our record had missed" (Dhubab)
- **Brief text:** "Reuters says government forces retook Dhubab in October, which our record had missed. Sunday's withdrawal hands that gain back."
- **Issue:** our record did have it.
- **Evidence:**
  - The `houthis` reversal-test trigger, note "REVIEWED 2026-10-13": "AFP (10 Oct, government military sources) — Mayun/Perim 'remained in Houthi hands'; Mocha unconfirmed; **Dhubab airfield taken**."
  - The `saudi-arabia` node: "'Dawn of Yemen' ground offensive… **Dhubab airfield taken**".
  - The 13-Oct intel: "they took the **Dhubab airfield** and cut the Dhubab–strait road".
  - The web check: Korea Times (6 Oct) reported that government forces "retook Dhubab".
  - The 13-Oct *brief* did not name Dhubab; it said only that "Dawn of Yemen" launched. The graph has held the fact since then.
- **Severity:** HIGH (a factual error in a "what is new" claim about our own record; the CoS's R7 history check missed it).
- **Recommended correction:** "**What is new:** our record has Perim island and Mocha in Houthi hands since 10–11 September, and government forces taking the Dhubab airfield in early October (AFP, recorded 13 October). Sunday's withdrawal hands that gain back."
- **Applied:** No. See G2.

### Flag H3 — "Only oil moved" and the ~65% crisis share for the 11:17 IST rise
- **Brief text:**
  - Section I: "**Only oil moved;** the dollar, the yen and bond futures were flat, and gold fell."
  - Page 2: "Brent, 11:17–12:10 IST … **Not found.** Only oil moved… | ~65% (low confidence)".
- **Issue:** the 1-minute data contradict "only oil moved", and the 65% crisis share has no support.
- **Evidence (my 1-minute re-pull):**
  - **Gold** (GCZ26) fell from 3,869.0 at 11:15 IST to 3,841.7 at 11:20, about −$27 (−0.7%), in the same five minutes as Brent's first steps (95.53 at 11:16 → 95.77 at 11:17 → 95.83 at 11:19).
  - MAC's own text records this gold burst at 11:16 IST on "~26× volume, no headline found".
  - DXY was flat (103.379 → 103.391).
  - A simultaneous oil-up, gold-down burst does not fit a war headline, which would usually lift gold. It fits a cross-asset or macro flow (MAC ties gold's fall to Fed bets before Warsh).
  - With no cause found, a 65% war share is a guess. It is also inconsistent with the CoS's own R9 ("Cause NOT ESTABLISHED").
- **Severity:** HIGH (an unsupported attribution share, plus a misstated fact in the item about causes).
- **Recommended correction:**
  - Section I: "**Oil and gold moved together, in opposite directions:** in the minutes Brent began rising (11:16–11:20 IST), gold fell about $27 on heavy volume. The dollar, yen and bond futures were flat. A war headline would usually lift gold, so the pairing does not point to the war."
  - Page 2, crisis-linked column: "unknown (cause not found)".
- **Applied:** No.

### Flag H4 — Bahrain heading re-presents a reported event as news (recycled content)
- **Brief text:** "### Iran fired at Bahrain again on Sunday. Bahrain says it intercepted the attack, and the Gulf states condemned Iran by name. CENTCOM has said nothing about Sunday."
- **Issue:** the 15-Nov brief already reported Sunday morning's fire: "**This morning:** sirens sounded at ~07:00 IST. At 07:43 IST, Bahrain's state television said air defences 'intercepted and destroyed an Iranian drone'" (and in its heading: "Bahrain says it destroyed another drone this morning").
- **Evidence:** CoS R3 itself confirms that no further fire came after Sunday morning, and that The National's "Bahrain intercepts Iranian attacks" is the 15-Nov story. What is genuinely new is the reaction: the BDF's account of "several" attacks, the MFA's rejection, the Article 51 letter to the UNSC, the Saudi and GCC condemnations, and CENTCOM's silence.
- **Severity:** HIGH (standing rule: do not re-present the last brief's items as new).
- **Recommended correction:**
  - Heading: "### Bahrain took Sunday morning's Iranian fire (in our last brief) to the UN Security Council, and the Gulf states condemned Iran by name. CENTCOM has said nothing about Sunday."
  - First bullet label: "**Bahrain (confirmed; the fire itself was in our last brief):**".
- **Applied:** No.

### Flag L1 — UKMTO "since 13 November"
- **Brief text:** "It is the first new UKMTO incident notice we have found since 13 November."
- **Issue:** the previous notice, 204-26 (*Dominica Prosperity*), was for an incident at ~23:30 IST on 11 Nov. Our 13-Nov brief reported it. As written, the line implies a notice dated 13 Nov.
- **Recommended correction:** "It is the first new UKMTO incident notice we have found since notice 204-26 (11 November), which our 13-November brief reported."

### Flag L2 — "the cabinet's 4-October readiness order surfaced only about five weeks later"
- **Issue:** this merges two reports. Our 12-Nov brief said "Ynet does not say whether that [4-Oct decision] is the order Kan describes." Kan's readiness report surfaced on 11 Nov; Ynet dated the cabinet's last decision to 4 Oct.
- **Recommended correction:** "A late leak is possible: Kan's report that the army was told to raise readiness surfaced only on 11 November, and Ynet dates the cabinet's last decision to 4 October." See also G5.

### Flag L3 — "Three desks searched separately and found nothing more"
- **Issue:** DIP's absence check had a stated gap: "Not covered: Tehran dusk Sun (~13:30 UTC) to 00:59 UTC Mon, outside CBS and Fox." ISR checked Israeli feeds for an Israeli strike. Only KIN swept the whole night. KIN's "no wire service" rests on Iranian state wires, the Fox, ABC and Al Jazeera liveblogs and CENTCOM; it lists no Reuters, AP or AFP sweep.
- **Recommended correction:** "KIN searched the whole night, and DIP and ISR checked separately, and none found anything more." The confidence line ("high on the absence") is fine.

### Flag L4 — Rupee "firmer than Friday's 94.19"
- **Issue:** this compares yfinance's 94.07 with PTI's 94.19 (mixed bases). On yfinance alone, Friday was 94.034 and 12:35 was 94.067, which is flat to slightly weaker. PTI itself has the rupee at 94.13 early ("rose 6 paise"), so the direction holds on PTI's basis.
- **Recommended correction:** "opened at 94.22 and rose to 94.13 in early trade (PTI), firmer than Friday's 94.19; yfinance had ~94.07 at 12:35 IST."

### Flag L5 — Lipow scorecard reasoning
- **Brief text:** "a tanker is not infrastructure on a strict reading".
- **Issue:** the 15-Nov ruling treated the mine claims on tankers as the candidates that were "unconfirmed". That implies a confirmed tanker hit would count, so today's reason changes the reading without saying so. The stronger reason is the evidence itself: UKMTO relays "a report… of an attack", with damage "unknown". That is not a confirmed hit.
- **Recommended correction:** "**Closer, not met.** UKMTO relays a report of an attack on an unnamed tanker, damage unknown: a reported attack, not a confirmed hit."

### Flag L6 — FII correction: say "regular"
- **Issue:** the count of ten is correct (see "Items that passed"). But the 8-Nov Muhurat session (−₹0.25 cr) is technically a selling session; the 9-Nov brief said so, and the 11-Nov brief used "regular session".
- **Recommended correction:** "the **tenth** straight regular session of foreign buying (not counting the 8-November Muhurat session's ₹0.25-crore sale), not the ninth."

### Flag L7 — India's silence on the tanker
- **Brief text:** "the shipping ministry and the foreign ministry have said nothing."
- **Issue:** the web check found one relay (The Hawk) citing India's foreign ministry: 14 Indians aboard, 13 rescued, 1 killed. It is unverified, may be an earlier incident, and conflicts with UKMTO's "crew… accounted for and safe".
- **Recommended correction:** "we found no statement from the shipping ministry or the foreign ministry." If time allows, the CoS should run a 2-minute MEA/DG Shipping check before publishing.

### Flag L8 — Bessent's 10-day Nvidia demand: source
- **Issue:** the source is tech-press relays only (digitimes, BigGo, 05:55–06:06 IST, per MAC). It was not found on a wire, and the web check did not re-find it. The brief lists it among "causes reported" without naming a source.
- **Recommended correction:** "a reported demand (tech press) by Treasury Secretary Bessent that Nvidia explain within 10 days…"

### Flag L9 — Bahrain: the BDF quote
- **Issue:** "intercepted and destroyed" is word for word the state-TV quote about **one drone** in the 15-Nov brief. The web check found only Fox's paraphrase of the BDF ("several Iranian projectiles before they reached their targets"). It may be a merged quote.
- **Recommended correction:** the CoS should confirm the wording in The National or Tribune (R3's sources). Otherwise write: "the Bahrain Defence Force says it intercepted several Iranian aerial attacks before they reached their targets."

### Flag L10 — Nikkei labelled "live"
- **Issue:** the snapshot reads "~59,700 / ~23,750 (live)". The Nikkei had closed, at 59,662.02 (−2.42%).
- **Recommended correction:** "59,662 (close) / ~23,750 (live)".

### Flag L11 — "no EU statement… from 13 to 16 November"
- **Issue:** this is an absolute claim, and the brief itself says four European outlets were unreachable.
- **Recommended correction:** "we found no EU statement…".

### Flag L12 — Gold 80:1 "scored on settlement prices"
- **Issue:** the trigger's own text is just "Gold/silver ratio exceeds 80:1". Settle scoring is our practice (3-Nov note: "watch the close"); the trigger does not say it.
- **Recommended correction:** "We score it on settlement prices (our practice since 3 November)." The ruling stands.

---

## Graph corrections (for the CoS; I edited nothing)
- **G1 — KOSPI and Samsung.** Change 5,082.39 (−3.94%) to **5,100.50 (−3.59%)**, and Samsung −5.0% to about −4.5% (196,800), in:
  - the `kospi` trigger `note_2026-11-16`;
  - `kospi.current.level`;
  - the `kospi` 16-Nov recent signal ("82 points above" becomes "100.50 points above");
  - the `semiconductors` 16-Nov signal.
  - Separately, `kospi.current.price` still reads "5,239.13 (10 Nov close)"; refresh it.
- **G2 — Dhubab.** Correct "(which retook Dhubab in October — not previously in our record)" in the `houthis` reversal-trigger `note_2026-11-16`, and "(that retake was not in our record…)" in the `houthis` 16-Nov signal. Use: "recorded 13 Oct (AFP: Dhubab airfield taken)".
- **G3 — NYT "new" target set.** Change "the energy target set is new" (`united-states` 16-Nov signal) and "plans for renewed strikes now aimed at 'energy infrastructure'" (`united-states` declared-campaign `note_2026-11-16`) to "restates October's plans reporting, which already included energy targets (NYT 21 and 24 Oct)". Also reword "plan targets now include energy infrastructure" in the `nuclear-program` note the same way.
- **G4 — The `fii-flows` summary.** "The daily amount has fallen three sessions running (₹12,563 → 7,831 → 5,737 cr)" lists two declines. Change it to "two sessions running".
- **G5 — The `israel` summary.** "earlier cabinet orders have surfaced weeks late" (and the "Caution: the 4-Oct order surfaced ~11 Nov" note) should read "Kan's readiness report surfaced on 11 Nov; Ynet dates the cabinet's last decision to 4 Oct", per L2.
- **G6 — The `brent-crude` 16-Nov signal.** Replace "oil-only (dollar, yen, Treasury futures flat; gold fell)" with "gold fell ~$27 in the same minutes (11:15–11:20 IST); dollar flat".

---

## Trigger Point Review

| Trigger | Changelog | My assessment | Agreement? |
|---|---|---|---|
| `united-states` RESUME (fired) | stays fired; no reset | Night thirteen has no credible strike report (KIN-A1, with Persian searches of state outlets). Leg (b) needs nights 14–16, so Thursday 19 Nov is the earliest, which is correct. (c) and (d) are unmet. Night five's multi-site report was disputed, so "no strike since 4 Nov met (c) or (d)" holds. Leg (d) carries no ownership requirement, so "one night of US strikes on energy targets would reset" is correct. "An Israeli strike alone would not reset it" is correct: the trigger text is "US strikes", and (i) is the open decision. | ✅ AGREE |
| `houthis` Aden / Tur al-Bahah / heights | closest, not fired | The withdrawal is CONFIRMED. Only one wire (Reuters) says "in control", and that describes the effect of the withdrawal, not Houthi forces reported on the heights. AFP places them at Kharaz, and Reuters places them "near" Tur al-Bahah. Under the 2-source rule this does not fire. It is the strongest case on the board; re-test tomorrow. | ✅ AGREE |
| `gold` ratio > 80:1 | closest, not fired | 81.2 live (3,845.9 / 47.335) against 79.12 on Friday's settle. Settle scoring follows the 3-Nov precedent (L12). | ✅ AGREE |
| `kospi` < 5,000 | closer, not fired | It does not fire on either figure, but the value is **5,100.50**, not 5,082.39 (C1/G1). | ✅ AGREE (fix the number) |
| `bahrain` hit confirmed | not fired | Fire is confirmed; a hit is not. The IRGC's radar claim is CLAIMED, and Bahrain's MFA rejects it. | ✅ AGREE |
| `israel` cabinet watch | not fired | The meeting is reported (ToI and Maariv, citing Hebrew media). No approval has been reported by two outlets or by the PMO/IDF. | ✅ AGREE |
| `strait-of-hormuz` blacklist; `iran` restricted zone | not fired | The UKMTO vessel is unnamed and the attacker unnamed. The location is inside the Gulf. | ✅ AGREE |
| `saudi-arabia` capacity; `houthis` holy-city | not fired | Claims only, with province-level wording. | ✅ AGREE |
| `fii-flows` 3 selling sessions | not fired (0/3) | Correct. | ✅ AGREE |
| `rbi` December rise; `fed` 50bp; `inr-usd` > 95 | not fired | WPI 12.29% is not a decision. 50bp is at ~7%. Rupee ~94.1. | ✅ AGREE |

- **Coverage:** the changelog says "135 = all 134 open at start + the fired RESUME re-test". My count of `note_2026-11-16` entries on open or fired triggers is 135. No status changes. ✅
- **The new edge `brent-crude → indian-oil-marketing` (6.0, cost_pressure):** justified as a structural edge, given frozen pump prices and BPCL −5.6% on the week, and it was proposed twice. Today's own evidence for it is weak (OMCs flat to −1% on a $1 Brent rise). The weight is acceptable. ✅
- **The 14 edges activated at unchanged weights:** `edge_changes.json` has 15 rows, 14 of them with unchanged weights plus the new edge. ✅

---

## Market Data Spot-Check (re-pulled 12:46 IST; flagged only where wrong at the stated time)

| Data point | Brief | Verified | Match? |
|---|---|---|---|
| Brent Jan reopen / low | 95.29 (04:30) / 94.46 (~08:30) | 30m bars: 04:30 O 95.29; 08:30 bar L 94.46 | ✅ |
| Brent steps | 11:17 → 96.73 by 12:10; high 96.76 | 1m: 11:16 C 95.53, 11:17 C 95.77, 11:40, 11:51, 11:57, 12:00, 12:03 steps; 12:10 O 96.73, H 96.76 | ✅ |
| Brent at 12:35 | 96.40 | Pull 96.40; 1m 12:33 and 12:36 at 96.36 | ✅ |
| Feb / Jun / Dec-27 | 93.51 / 85.97 / 80.13 | 93.52 / 85.97 / 80.13 | ✅ |
| Jan–Dec27 spread | ~16.27 (from 15.86) | 96.40 − 80.13 = 16.27; Fri 95.84 − 79.98 = 15.86 | ✅ |
| WTI / HO / RBOB / HH | 89.09 / 4.306 / 2.647 / 3.122 | 89.09 / 4.306 / 2.647 / 3.122 | ✅ |
| Gold / silver | 3,845.9 (−1.0%) / 47.34 (−3.6%) | 3,845.9 / 47.335; −1.04% / −3.63% | ✅ |
| Gold/silver ratio | 79.1 Fri → ~81.2 | 79.12 → 81.25 | ✅ |
| Copper / aluminium | 6.032 / 3,108 | 6.032 / 3,108.25 | ✅ |
| TAIEX / TSMC | 41,040.08 (−6.0%) / 2,215 (−5.7%) | 41,040.08 (−6.03%) / 2,215 (−5.74%) | ✅ |
| **KOSPI** | **5,082.39 (−3.9%)** | **5,100.50 (−3.59%)** | ❌ C1 |
| SK hynix / **Samsung** | 1,120,000 (−7.9%) / **195,800 (−5.0%)** | 1,120,000 (−7.89%) / **196,800 (−4.47%)** | ✅ / ❌ C1 |
| Nikkei | −2.4% (~59,700 "live") | 59,662.02 close (−2.42%) | ✅ (L10 label) |
| Hang Seng | ~23,750 | 23,749.9 | ✅ |
| NQ "−1.7% from the open" | −1.7% | 28,198.75 (04:30 open) → ~27,712 (−1.73%) | ✅ |
| Nifty | 25,257.00 (+0.45%); open 25,206.15; high 25,337.60 | 25,257.00 (+0.448%); 25,206.15; 25,337.60; low 25,190.25 (> 25,178.65) | ✅ |
| Sensex / Bank Nifty / IT / VIX | 82,111 / 61,574 / 31,829 / 15.76 | 82,111.43 / 61,574.10 / 31,828.70 / 15.76 | ✅ |
| IOC / BPCL / HPCL | 142.65 / 301.95 / 381.45 | same | ✅ |
| USD/INR | ~94.07 | 94.067 (yfinance) | ✅ (L4 basis) |
| DXY | 103.46 live; 103.41 Fri | 103.463 / 103.410 | ✅ |
| TASI Sun | 10,258.22 (−0.66%) | −0.661% vs 10,326.47 | ✅ |
| Fed Dec 50bp | ~7% (from ~10%) | ZQZ26 95.930 → 4.070; (4.07 − 3.88) × 31/22 = 26.8bp → 7%; Friday 95.925 → 11% | ✅ |
| Fed Jan / Mar | ~73% / ~72% | Jan: post-Dec 4.151 vs ZQG27 4.335 → 18.4bp = 74%; Mar: ZQJ27 4.51 − 4.335 = 17.5bp = 70% now (72% on Friday's ZQJ 95.480) | ✅ (within drift) |
| Friday closes (S&P, Nasdaq, Dow, SOX, NVDA, VIX, STOXX, DAX, FTSE) | as printed | all match to the cent | ✅ |
| WPI Oct and parts | 12.29 / 12.10 / 11.39; fuel 32.84 from 25.85; crude & gas 70.80; food 8.58; manufactured 9.54 | Web (Reuters, Business Standard): all match; food was 8.66 and manufactured 9.76 in September, so "eased" is right | ✅ |
| China Oct | 4.8% (5.3%), 0.4% (0.8%), −8.1% | Web (CNBC, Reuters): match | ✅ |

---

## Items That Passed

- **The lead: no strike on night thirteen (PASS, with L3).** This is an absence finding. KIN ran Persian searches of IRNA, Tasnim, Fars, Mehr, ISNA, IRIB and Hormozgan for 24–25 Aban, and found the only "no impact" governorate items were dated 22 Aban, so they concern night eleven. The OSINT feed (FromIran/sh1n.org) is correctly excluded. The IRGC's Monday "US fighter jets" line claims no strike. "Thursday 19 November at the earliest" is correct: nights 14 to 16, the last ending Thursday morning.
- **Washington.**
  - Bessent's quote was found word for word (Fox "Sunday Morning Futures", 15 Nov).
  - Trump's 07:10 IST share was found: "A must read!!!" with the op-ed headline (Truth Social, dated 15 Nov US time, which is consistent).
  - The *Roosevelt* has several US officials behind it (ABC via Gulf News, CBS, Axios/Ravid via ToI, Al Jazeera). CENTCOM has not announced it.
  - The "provocations" absence is consistent with R4.
  - Reuters' "may hold off" was dated Saturday 14 Nov, which is correct.
- **Israel.**
  - The cabinet meeting is reported via ToI (22:11 IST) and Maariv citing Hebrew media, correctly tagged "reported".
  - The N12 quote: the ISR desk gives the Hebrew original (מערכת הביטחון סבורה שלא מוצדק לפעול באיראן בימים הרגישים מבחינה פוליטית), so the quotation marks are justified. The JPost relay supports the Aman dissent.
  - "Missed yesterday" is correct: the item is timed Sat 22:05 Israel, inside the 15-Nov window, and is absent from the 15-Nov brief, which carried only Channel 12's Zamir item.
  - Gofman–Witkoff (ToI) also re-found.
- **Yemen (PASS except H2).** Found on Reuters via NBC and US News: "redeployment… from Dhubab Airport and the Bab el Mandeb area", "priority of securing the capital, Aden", "leaving the Iran-aligned Houthis in control", "greater leverage over the maritime choke point", al-Suqyah "150 kilometers… west of Aden", and "still trying to push the Houthis". AFP's Kharaz "60 kilometres" is desk-sourced only (not re-found). The 66 days (since 11 Sep) recomputes.
- **At sea.** The UKMTO text was re-found through relays (Anadolu, IANS). "Unclear" whether it is one of Iran's ships is AFP's account of UKMTO. Iran's claims are correctly tagged unconfirmed, and "four or five, not six" matches KIN's count.
- **Oil.** The reopen, the low and the steps all match the 1-minute data. Goldman (2 mb/d; $78 end-2027) was found via Bloomberg and investingLive. The Reuters and investingLive headlines are attributed as headlines. The mine-claim timing (Reuters ~10:11–10:16 IST against the 11:17 rise) is about one hour, which is correct.
- **Gold and Fed.** "Fed Chair Warsh" is confirmed by PTI's own copy ("Fed Chair Kevin Warsh's speech"), and 12:00 ET is 22:30 IST. Goldman's "second cut in a month" is from relays (MAC).
- **India.**
  - **The FII streak, re-derived independently:**
    - The 31-Oct IND dossier gives 26 Oct −1,463; 27 Oct +4,240; 28 Oct +872; **29 Oct −944**; **30 Oct +3,599** (session 1).
    - Then 2 Nov +3,114.68 (2); 3 Nov +6,836.81 (3); 4 Nov +7,284.03 (4); 5 Nov +14,974.68 (5); 6 Nov +13,750 (6, which the 8-Nov brief itself called the "sixth"); [8 Nov Muhurat −0.25, excluded]; 9 Nov +7,212.20 (**7**, which the 11-Nov brief called "sixth"); 10 Nov had no session; 11 Nov +12,563.33 (8); 12 Nov +7,830.60 (9); 13 Nov +5,736.55 (**10**).
    - **Ten is correct.** The 11-Nov brief introduced the error, and the 12-, 13- and 15-Nov briefs carried it. The exchange sum is ₹82,901 cr, matching the `fii-flows` summary's ~₹82,900.
  - PTI's ₹84,290 cr and "since 2002" are attributed.
  - The Nifty's low (25,190.25) stayed above 25,178.65, so "all morning" holds.
- **Iran.** Gharibabadi's quote was found word for word (Press TV). Baghaei's lines are desk-sourced (not re-found on the web). Ghalibaf is labelled "not new"; Araghchi's trip is confirmed (R5). Saree's claims are tagged CLAIMED, and the stations No. 5 and 6 are on the East–West line per the Arabic text. The TASI is not attributed to the missiles, which is correct.
- **Signal logic (except H1).** Leg (d) quoted correctly; Israeli-only correctly excluded; "what we do not know" properly hedged; no "intends/signals" language.
- **Deployment.** Conditions 1–3 match the 15-Nov brief word for word, with numbers updated. "(ii)… met on 13 November, by CENTCOM's statement, and again on 15 November, by Bahrain's own forces" is consistent with the 15-Nov brief's line 175. The hold-rule paragraph is identical to 15 Nov.
- **Section II.**
  - The new calls' tests are well formed. One note: the N12 test ("before a new government is sworn in") has no date; consider adding "or by 31 January 2027".
  - Scorecard: Ynet "not borne out so far" is fair. Kalın "close to failing" is fair. Flynn "not met so far" is fair (a settle test; intraday low cited as context).
- **Balance (Check 7).** Section I has 4 geopolitical items and 3 market/commodity items (oil, chips/gold/Fed, India). Section II has Goldman and Vijayakumar alongside the Israeli calls. Cascade Watch covers gold, KOSPI, Brent and RBI. ✅

## Not independently re-found (the search index lags; not the same as wrong)
- The BDF's "intercepted and destroyed… several" (L9); the Bahrain MFA's "categorically rejects the false claims"; the Saudi MOFA's "strong condemnation of the Iranian attacks on Bahrain" (only June–July versions surfaced).
- CBS's "expected to be temporary" (DIP quotes CBS 18:56 ET).
- The November NYT article itself (relays only; DIP notes no date in the relays).
- AFP's Kharaz "60 kilometres"; Baghaei's "not waiting for anyone"; Bessent's 10-day Nvidia demand.
- The UKMTO number 205-26 (ukmto.org 403); The Hawk's MEA casualty relay (L7).

## Final Verdict
**APPROVED WITH CORRECTIONS.**
- **Fix before publishing:** C1 (KOSPI and Samsung, five places), H1 (the NYT "new target list" in Section I, the Signal, the case against and the Risk Landscape), H2 (Dhubab), H3 ("only oil moved" and the 65% share) and H4 (the Bahrain heading).
- **Optional:** the LOWs are one-line edits.
- **What held:** the lead, the FII correction, the hold-rule logic and almost every price. The errors cluster where the brief describes our own record ("new", "missed", "only"), which our own files contradict. That is the pattern to check first next time.

*Basis:*
- *Ran:* a yfinance re-pull at 12:46 IST (daily bars, plus 1-minute bars for Brent, gold, DXY and Korea); Fed-odds arithmetic; the FII streak re-derived from the 31-Oct dossier and nine briefs.
- *Read:* the brief, the CoS header R1–R14, the KIN, DIP, ISR, SAU, IND and MAC items, the changelog, the trigger notes, the edges, the 26-Oct and 13-Oct briefs and intel, and the 15-Nov brief.
- *Sourced:* web relays (Reuters via NBC and US News, Fox, Press TV, Bloomberg, Business Standard).

*Not checked:* KRX's official KOSPI release; the primary Bahrain and Saudi statements; the NYT original.

*Confidence:* high on C1 (two pulls plus a web match), H2 and H1 (our own files); moderate on H3's inference (the data are solid; that it rules out a war cause is reasoned).


---

## Corrections applied (Chief of Station, 13:00 IST Mon 16 Nov, `date`-checked)
All 17 flags were applied to `briefs/2026-11-16-morning.md` as recommended, with these notes:
- **C1:** KOSPI 5,100.50 (−3.6%), Samsung 196,800 (−4.5%, on yfinance's Friday base 206,000, the base used in the 15-Nov brief). CoS re-pull at 12:57 IST confirmed both. Fixed in the Section I heading and closes, Page 2 (both tables) and Section III. Nikkei 59,662 (close) (L10).
- **H1:** the NYT energy-target list is now "not new in substance" (24-Oct story, our 26-Oct brief); the lead headline, the Signal headline and "what has changed", the Risk Landscape and the case against were reworded. The Signal's rule logic (leg (d) resets in one night) stands — the verifier agreed.
- **H2:** Dhubab — "government forces taking the Dhubab airfield in early October (AFP, recorded 13 October)".
- **H3:** "Gold fell as oil rose" (−$27, 11:16–11:20 IST); the crisis share of the 11:17 rise is now "unknown (cause not found)" in the brief and in `markets.md`.
- **H4/L9:** Bahrain heading leads with the UNSC appeal and condemnations; the fire is marked as in the last brief; the BDF line is no longer in quotation marks.
- **L7:** CoS checked the india.com relay: its "14 Indian nationals… one died" MEA line sits beside the 3-Nov *Al Jusufi* paragraph and is not tied to this tanker. The brief says "we found no statement on this tanker".
- **L1–L6, L8, L11, L12:** applied as written.
- **Graph G1–G6:** applied (backup `backups/2026-11-16/graph_v2_preverif`); edge contexts for `semiconductors → kospi` and `united-states → iran` corrected too. `graph-changelog.md` regenerated with a post-verification line; viewer rebuilt. No trigger status changed.
