# Verification Report — 15 November 2026 (morning, Day 261)
Generated: 10:42 IST Sunday (`date`-checked) | Fact-Checker: Red Team
Brief checked: `briefs/2026-11-15-morning.md` (read-only; nothing in `briefs/`, `graph/` or `scripts/` was touched). Scratch: `staging/2026-11-15-morning/verifier_scratch/` (`pull.py`, `yf_out.txt`, `sun.py`).

## Summary
I checked about 95 claims: every Section I item, the Signal, the deployment section, the Section II calls and scorecard, the Cascade Watch, and all of Page 2. I re-pulled 44 tickers from yfinance, plus FRED and the Treasury CSV. I raised **19 flags: 1 CRITICAL, 9 HIGH and 9 LOW**, and I list **6 graph corrections**. No trigger status is wrong.

- **The lead's core finding holds.** No strike on Iran was reported on nights eleven or twelve; three desks checked. The hold rule did not reset. The four legs (a) to (d) match the trigger text word for word, including the (a) exception. Wednesday 18 November is the right date.
- **The lead headline's second and third sentences do not hold.** "Instead, Iran fired drones at Bahrain twice" counts a salvo from Friday morning, before night eleven. We already reported that salvo, as a claim, in the 13-Nov brief. "Washington's line moved from 'We don't need a deal' to 'may hold off'" is also wrong: Trump was already on record holding off (the 13-Nov brief quotes his Saudi "let it be" line), and Rubio said the same at the G7 on 10 Nov.
- **Most flags sit in the interpretive lines.** They are in the Signal (3 HIGH), the US headline ("mostly about the Fed", which our own futures data contradict) and India's "What it means". Two desk-level counting errors also reached Section I: the FII "three days running" and the OMC "third day".
- **One wrong market number:** the evening Brent slide was about $1.00 from 21:05 IST, not $1.60.
- Every settle, close, percentage, spread, ratio and Fed-odds figure I re-computed matches.

---

## Flags

### Flag 1 (HIGH): The lead headline. "Instead, Iran fired drones at Bahrain twice; the US and Bahrain report interceptions"
- **Issue:** this is a timing error, and it presents a reported event as new.
  - The first salvo was not an "instead" event for Friday or Saturday night. The Guards' claim was first reported at **07:42 IST on Fri 13 Nov**, which is before night eleven and before this window opened. The 13-Nov brief reported it, as a claim. What is new is CENTCOM's confirmation.
  - "The US and Bahrain report interceptions" blurs two days. Only the US spoke about Friday's salvo, and only Bahrain spoke about Sunday's; CENTCOM was silent on Sunday by 10:10 IST.
- **Evidence:** 13-Nov brief line 53 ("first reports 07:42 IST today"); KIN-A4 (IRGC statement no. 22 at 02:45 UTC 13 Nov); KIN-A5.
- **Correction:** replace the second sentence of the headline with: "CENTCOM confirmed that Iran fired two drones at Bahrain on Friday morning, and said both were shot down; Bahrain says it destroyed another drone this morning. No hit is confirmed."
- **Applied:** Yes (CoS, 10:44 IST)

### Flag 2 (HIGH): The lead headline. "Washington's line moved from 'We don't need a deal' to 'may hold off'"
- **Issue:** the brief presents a restatement as a shift, and treats an unnamed-source report as the official line.
  - Trump himself was already on record holding off. The 13-Nov brief (line 21) says he gave Saudi Arabia's "let it be the way it is now for a while" as his reason for holding off.
  - Reuters (11 Nov) reported that on 10 Nov Trump said he planned to hold off on strikes after appeals from regional countries.
  - Rubio said the same at the G7 on 10 Nov, before the "no deal" post: "We don't need to conduct military strikes if we're achieving the same objective through economic means" (Reuters via BusinessDay, 11 Nov).
  - Reuters Asia (13 Nov, MAC-A1) read "no deal needed" as reliance on the blockade, not escalation.
  - "May hold off" comes from three unnamed sources on private remarks. Trump posted nothing on Iran on Saturday, and his Friday posts were not checked.
- **Correction:** replace the headline's third sentence with: "Washington repeated its restraint line: Rubio said there is 'no need for military action', and Reuters' sources say Trump 'may hold off' absent new provocations." In the Washington block, add after the Reuters bullet: "This restates a hold Trump himself gave last week, citing Saudi Arabia's request; what is new is the 'provocations' condition."
- **Applied:** Yes (CoS, 10:44 IST)

### Flag 3 (HIGH): The Signal, bold line. "…leave it unchanged, whatever Washington does next"
- **Issue:** the line contradicts the Signal's own next bullet ("If the US answers with strikes, the hold rule resets the usual way"). A US strike in reply would reset the rule under (a) or (b). The Bahrain drones were aimed at a land site, so a reply to them is not covered by the "fire on US aircraft or ships" exception. The bold line also cuts "US strikes on Iran" down to any US strike, when only strikes meeting one of the four legs count.
- **Correction:** "**The weekend's escalation came from Iran and the Houthis, not the US, and by itself it resets nothing on our rules. The hold rule resets only on a US strike on Iran that meets one of the four legs, a declared US campaign, or confirmed Iranian fire on Oman. Iranian fire at Bahrain and Houthi missiles at Riyadh change it only if Washington answers with strikes.**"
- **Applied:** Yes (CoS, 10:44 IST)

### Flag 4 (HIGH): The Signal, "The sequence". "Reuters' sources named the two things that would end Trump's hold… By Sunday morning both had fired"
- **Issue:** this reverses the logic of the source, and it leaves out the counter-evidence.
  - Reuters said Trump "may hold off… if the US faces no new provocations". That is a condition for holding off. It does not say a provocation would end the hold.
  - Both kinds of fire came before the story. Iran's Friday drones at Bahrain had been confirmed by CENTCOM by ~17:17–18:44 IST Fri, and the Reuters story ran on Saturday (ToI 17:16 IST). The Houthis fired a ballistic and a cruise missile at Riyadh on 10 Nov (graph `saudi-arabia`, 10-Nov signal), and their pipeline-station claims ran all week.
  - So Sunday's salvos are more of the same, not obviously the "new provocations" in Reuters' wording.
- **Correction:** "**The sequence:** Reuters' sources said Trump 'may hold off on attacking Iran if the US faces no new provocations from Tehran or the Iran-backed Houthis'. They did not say what a provocation would trigger. The story ran after Friday's Iranian drones at Bahrain and after a week of Houthi fire at Saudi Arabia, including missiles at Riyadh on 10 November. On Sunday morning Iran fired at Bahrain again, and the coalition says the Houthis fired ballistic missiles at Riyadh. Bahrain and the coalition report interceptions; neither reports damage, though the Guards claim hits in Bahrain."
- **Applied:** Yes (CoS, 10:44 IST)

### Flag 5 (HIGH): The Signal. "this is the gap behind **your** proposed reset (ii)"
- **Issue:** this attributes the proposal to the wrong person. Reset (ii) was the brief's proposal, put to the user for a decision. The 13-Nov brief lists it under "For your decision, not applied", and PLAN.md says "OPEN FOR THE USER (proposed, not applied)". The user did not propose it. The deployment section words it correctly ("proposed 13 Nov").
- **Correction:** "**The open decision:** this is the gap in reset (ii), which we proposed on 13 November for your decision: 'confirmed Iranian fire **hitting** a Gulf state that hosts US forces'. It would not fire on today's facts, because no hit has been confirmed. With the bar at 'fired at', it would have fired on CENTCOM's 13-November statement."
- **Applied:** Yes (CoS, 10:44 IST)

### Flag 6 (HIGH): US headline and Treasuries. "The rise was mostly about the Fed"
- **Issue:** our own data contradict the attribution.
  - On Friday every fed-funds future priced *less* tightening than on Thursday. December rose 95.910 → 95.925, so the hike priced fell from 29.6 to 27.5bp and the half-point odds from ~18% to ~10%. February rose 95.650 → 95.660, and April rose 95.465 → 95.480.
  - The curve steepened (2s10s 24 → 27bp; the 2Y rose only 2bp against the 10Y's 5bp).
  - Most of the 10Y's rise came before any US data. ZN fell 105.344 → 105.219 between 11:00 and 18:30 IST, out of a 105.344 → ~105.19 day (`bars-30m-fri.txt`).
  - That pattern is a long-end move, not a new Fed bet. "Fed rate-rise certainty" is CNBC's explanation, and the brief should attribute it as CNBC's. The headline's "mostly about the Fed" and the graph line "the driver is the Fed" go further than the evidence.
- **Correction (headline):** "US ten-year yields rose to 5.15%, the highest close since 19 October, even though Fed rate-rise bets eased slightly; oil was flat. Chip stocks fell 3.4% on Nvidia, not on the war."
- **Correction (Treasuries bullet, add):** "Most of the ten-year's rise came in Asian and European hours, before the US data, and the curve steepened while fed-funds futures priced slightly less tightening. CNBC attributes it to Fed-rise certainty and Thursday's momentum."
- **Applied:** Yes (CoS, 10:44 IST)

### Flag 7 (HIGH): India trade, "What it means". "this is the clearest direct cost of the war to India in this window"
- **Issue:** this is an unsupported superlative, and the desk's own data cut against it.
  - The October deficit ($39.88bn) is still **below October 2025's $42.58bn**, a pre-war record (IND-B1).
  - Exports also hit a record ($49.47bn), and Business Standard says "Energy prices pushed exports, imports to record highs".
  - Gold imports tripled month on month ($1.80bn → $5.51bn).
  - Nothing ranks the deficit against the war's other costs to India. The headline's "on the oil bill" also gives the oil bill as the only cause.
- **Correction:** "**What it means:** the war shows up in the oil bill. Petroleum imports were up 54% from a year earlier (one trade outlet). But energy prices also lifted exports to a record, gold imports tripled from September, and the deficit is below October 2025's $42.58 billion." In the India headline, change "on the oil bill" to "with record imports".
- **Applied:** Yes (CoS, 10:44 IST)

### Flag 8 (HIGH): India FII line. "The daily amounts have shrunk three days running: ₹12,563 → ₹7,831 → ₹5,737 crore"
- **Issue:** the count is wrong. Those three figures show two falls. The day before, 9 Nov, was ₹7,212 crore (11-Nov and 12-Nov briefs), so 11 Nov was a *rise*. The Risk Landscape line has it right ("more than halved in two sessions").
- **Correction:** "The daily amount has fallen for two sessions running, from ₹12,563 crore on Wednesday to ₹7,831 crore and then ₹5,737 crore."
- **Applied:** Yes (brief + graph G1)

### Flag 9 (HIGH): India fuel retailers. "BPCL, HPCL and IOC fell for a third day"
- **Issue:** this is a market-data error. On 11 Nov HPCL rose from 385.75 to 400.15 and IOC from 146.85 to 148.38 (yfinance; the 12-Nov brief's own table). So HPCL and IOC fell for a **second** day. BPCL fell for a **fourth** session (319.90 → 316.00 → 315.25 → 311.50 → 302.00). The IND desk's "third straight falls for all three (from 11 Nov)" is the source of the error.
- **Correction:** "**Fuel retailers:** BPCL fell for a fourth session and is down 5.6% on the week; HPCL and IOC fell for a second day."
- **Applied:** Yes (brief + graph G5)

### Flag 10 (CRITICAL, wrong market data, easy fix): Oil's evening slide. "From 21:05 IST oil slid $1.60" (Section I); Page 2 "Brent, 21:05–22:30 IST | −$1.60"
- **Issue:** the bars do not support the number.
  - On our 5-minute bars, Brent stood at $96.53 at 21:05 IST and touched a low of $95.53 at 22:25. That is about **$1.00** (to the 22:30 close of $95.70, $0.83).
  - $1.60 is the fall from the day's high, $97.12 at 20:24 IST, to $95.53: that is $1.59. It may also be the gross sum of the three down-steps. It is not the fall from 21:05.
  - The settle is right; this intraday figure is wrong in two places.
- **Evidence:** `research/mac_scratch/us5m.txt` (BZF27 21:05 O 96.53; 22:25 L 95.53); `bars-30m-fri.txt` (20:00 bar H 97.12).
- **Correction (Section I):** "From its 20:24 IST high of $97.12, oil slid about $1.60 to $95.53 by 22:25 IST, most of it after 21:05 and alongside the US stock sell-off." **Page 2 row:** "Brent, 20:24–22:25 IST | $97.12 → $95.53 (−$1.59) | No headline; came with the US stock slide | unknown".
- **Applied:** Yes (CoS, 10:44 IST)

### Flag 11 (LOW): The header clock. "Night thirteen begins at dusk in Tehran (~18:25 IST)"
- **Issue:** the time is about 30–60 minutes early.
  - Tehran's sunset on 15 Nov is ~16:58 local, which is **~18:58 IST**; civil dusk is ~19:25 IST (NOAA formula, `verifier_scratch/sun.py`; Bandar Abbas gives 18:54 and 19:19).
  - 18:25 IST would be 16:25 Tehran. The likely cause is a 1:30 offset used in place of the correct 2:00 (Tehran is UTC+3:30 and IST is UTC+5:30).
- **Correction:** "Night thirteen begins at dusk in Tehran (~19:00 IST)."

### Flag 12 (LOW): The Signal. "If it does not, the region is getting more dangerous for Gulf hosts of US forces with no change on our scorecard"
- **Issue:** this is an unsourced trend claim. It also uses the wrong term: the scorecard tracks analysts' calls; this is the hold rule.
- **Correction:** "**If it does not,** Iranian fire at Gulf hosts of US forces (twice in three days so far, both intercepted) leaves the hold rule unchanged."

### Flag 13 (LOW): Risk Landscape. "Intensifying: Houthi fire at Riyadh (ballistic missiles, per the coalition)"
- **Issue:** the comparison does not hold. On 10 Nov the coalition reported a ballistic and a cruise missile at Riyadh, after three days of shelter alerts, and Riyadh's schools moved online (graph `saudi-arabia`, 10-Nov signal). The weekend's two missiles do not show escalation against that. In "The case against", "none of it is priced yet" fits Sunday's salvos, but not Houthi fire in general, which ran all week.
- **Correction:** move the item to a "Continuing" line: "Houthi fire at Riyadh (ballistic missiles again, per the coalition; also on 10 Nov)".

### Flag 14 (LOW): Scorecard, Lipow. "**Closer, not met.** Fire at Bahrain is confirmed; a hit is not."
- **Issue:** the call's test is "a hit on Gulf energy or shipping infrastructure, confirmed by UKMTO or a government". The Bahrain drones were aimed at a military radar, which is not energy or shipping, so they do not bring the call closer.
- **Correction:** "**Not met.** No hit on Gulf energy or shipping infrastructure is confirmed: the Houthi pipeline and Iranian mine claims are unconfirmed, and the Bahrain fire was aimed at a military site."

### Flag 15 (LOW): Credit. "Credit is calm: the junk-bond spread… narrowed to 3.20%"; "What held… narrower again (3.20%)"
- **Issue:** 3.20% is Thursday's (12 Nov) print. FRED has not posted Friday's figure, and Friday was a risk-off day (VIX intraday 20.92). Page 2 labels it correctly.
- **Correction:** "…narrowed to 3.20% on Thursday (Friday's figure is not yet out)."

### Flag 16 (LOW): The curve. "The back of the curve fell further than the front, so the near-term war premium held."
- **Issue:** the line names a single cause when there is a second one. The IEA itself says on-land stocks are the lowest "since at least 2016" (SAU-A6), and prompt physical tightness explains a firm front as well as a war premium does.
- **Correction:** "The back of the curve fell further than the front, so the front-end premium held; the IEA puts on-land stocks at their lowest since at least 2016."

### Flag 17 (LOW): The 19:16 IST burst. "on about 14 times normal volume"
- **Issue:** ~14× is WTI's ratio (2,420 lots against ~170). Brent's was much larger: 549 lots against ~8–11 in the minutes before (`spike1916.txt`).
- **Correction:** "…lifted Brent to $97.05, with WTI trading about 14 times its normal volume."

### Flag 18 (LOW): PPI. "described as the biggest annual rise since November 2022"
- **Issue:** the passive voice hides the source (relays: CNBC and Yahoo; BLS was not read).
- **Correction:** "…which CNBC and other relays call the biggest annual rise since November 2022."

### Flag 19 (LOW): IEA. "The price: Brent fell from $96.41 to $95.16 within about 90 minutes"
- **Issue:** the low came in the 16:00–16:30 bar, so the move took 90–120 minutes. The SAU desk's start point is $96.34 (the 14:30 bar open), while MAC's is $96.41 at 14:28. This is harmless.
- **Correction (optional):** "within about two hours".

---

## Graph corrections (list only; CoS/Graph Engineer to apply)
- **G1 `fii-flows`:** the summary, the 15-Nov signal and the 3-sessions trigger's `note_2026-11-15` say "shrunk/fallen three days running". Change to "two sessions running (₹12,563 → ₹7,831 → ₹5,737 cr; 9 Nov was ₹7,212 cr)".
- **G2 `us-10y-yield`:** the summary says "The driver is the Fed, not the war". Change to "Not the war. Friday's rise came mostly before the PPI release, with fed-funds futures pricing slightly less tightening and the curve steepening; CNBC attributes it to Fed-rise certainty." Edge `fed → us-10y-yield` context: change "on hike certainty" to "CNBC: hike certainty; futures eased".
- **G3 `united-states`:** the summary says "Washington's line has moved from 'We don't need a deal'… to restraint… Iran **then** fired drones at Bahrain on 13 and 15 Nov". Both the sequence and the shift are wrong. The 13-Nov drones came before Rubio's Friday remarks and the Reuters story, and Trump's own hold-off (Saudi request) came before the 12-Nov post. Rewrite as: "Washington repeated restraint (Rubio; Reuters' sources: 'may hold off' absent new provocations), restating Trump's own hold at Saudi request; Iranian drones were fired at Bahrain on 13 Nov (CENTCOM) and again on 15 Nov (Bahrain TV)."
- **G4 `bahrain`:** the summary says "since 13 Nov, a target of Iranian drones on the record". This contradicts the node's own June signals (Sheikh Isa, CENTCOM interceptions, a child injured) and July signals (Foreign Ministry condemnation). Change to "again a target of Iranian drones on the record (CENTCOM 13 Nov; Bahrain TV 15 Nov), as in June and July".
- **G5 `indian-oil-marketing`:** the 15-Nov signal says "third straight fall for all three". Change to "BPCL fourth straight fall; HPCL and IOC second". Separately, the node **summary is stale**: it reads "Day 241", "Brent Dec $116.72 (23 Oct)", "basket ~$120". It is not among today's 8 rewrites; flag it for the next run.
- **G6 `trump`/`united-states` (optional):** record that Reuters (11 Nov) had Trump saying on 10 Nov that he "plans to hold off on military strikes… after appeals from regional countries". This is the baseline the 14-Nov "may hold off" restates.

---

## Trigger Point Review

| Trigger | Status in changelog | My assessment | Agreement? |
|---|---|---|---|
| `united-states` RESUME (fired; hold-rule test) | stays fired; no reversal; legs a–d unmet | Leg (b) broke on night eleven: Hormozgan "no impact or explosion" to 22:25 Tehran, the IRGC Isfahan denial, and no wire or US/Israeli report (KIN, DIP, ISR). Night twelve rests on one OSINT feed. (a): no owner, and CENTCOM was silent on Sirik (RFE/RL). (c) and (d) unmet. Leaving out 15 Khordad (daytime Friday, OSINT, a previously hit site) is fair. Wed 18 Nov is the right earliest date (nights 13–15). | ✅ AGREE |
| `bahrain`: confirmed fire *hitting* a US/Bahraini military site | watching, closer | Fire *at* Bahrain is confirmed twice; there is no hit. CENTCOM says "no… damage"; the Khalifa Port blasts are unofficial, and it is a commercial port. | ✅ AGREE |
| `gold`: gold/silver ratio above 80:1 | watching, closer | I recomputed 3,886.3 / 49.121 = **79.12** (from 77.61). Spot ~78.1. Neither is above 80. | ✅ AGREE |
| `china`: APEC readout naming Iran/Hormuz by 20 Nov | pending 19 Nov | Only the White House confirmation and AFP's "does intend to talk about Iran". There is no readout. | ✅ AGREE |
| `israel`: cabinet approval (two outlets with their own sources, or PMO/IDF) | pending tonight | The meeting comes after the brief; no leaked draft. | ✅ AGREE |
| `inr-usd`: PTI close weaker than 95.00 | watching | 94.20 | ✅ AGREE |
| `fii-flows`: three selling sessions | watching, further | Correct, but the note's "three days running" needs fixing (G1). | ✅ AGREE (text fix) |
| `fed`: 50bp on 9 Dec | watching, further | Recomputed: (100 − 95.925 − 3.88) × 31/22 = 27.48bp, so ~10%. | ✅ AGREE |
| `rbi` reserves below $700bn / FCA −$3bn | watching | $719.55bn; FCA +$0.23bn | ✅ AGREE |
| `brent-crude` $100/$85 | watching | $95.84; +4.34% needed to reach $100 | ✅ AGREE |
| `saudi-arabia` capacity (lost throughput / imagery) | watching | PS-3 is a Houthi claim only; no Saudi, Aramco or imagery confirmation | ✅ AGREE |
| `oman` / hold-rule Oman reset | watching | Omani official: "had not been struck"; nothing new | ✅ AGREE |
| `strait-of-hormuz` blacklist enforcement | watching | No named vessel; the mine claims are unnamed and unverified | ✅ AGREE |
| `iran` restricted-zone (UKMTO-verified IRGC strike) | watching | The "east of the strait" claim is the regular navy's and unverified | ✅ AGREE |

No trigger that should have moved was left unmoved. **All 134 open triggers (128 watching + 6 active) carry a `note_2026-11-15`** (scripted check). The changelog's count of 0 status changes is correct.

---

## Market Data Spot-Check (independent yfinance pull, 10:33 IST; FRED and Treasury CSV)

| Data point | Brief | Verified | Match |
|---|---|---|---|
| Brent Jan (BZF27) settle / 1D | $95.84 / +2c | 95.84 / +0.02 | ✅ |
| Brent week (6 → 13 Nov) | ~−2.5% | 98.32 → 95.84 = −2.52% | ✅ |
| WTI Dec | $88.56 | 88.56 (week −2.50%) | ✅ |
| Feb / Jun / Dec-27 | 93.03 / 86.15 / 79.98 | same | ✅ |
| Jan–Dec27 spread | $15.86 (from $15.38) | 15.86 / 15.38 | ✅ |
| HO / RBOB / HH | 4.259 / 2.621 / 3.230 | 4.2585 / 2.6214 / 3.230 | ✅ |
| TTF | €90.95, −1.4% | 90.952, −1.42% | ✅ |
| Gold / silver / ratio | 3,886.3 / 49.12 / 79.1 | 3,886.3 / 49.121 / 79.12 (Thu 77.61) | ✅ |
| Copper | 6.090 | 6.0905 (−1.70%) | ✅ |
| 10Y / 2Y / 30Y (par) | 5.15 / 4.88 / 5.47 | Treasury CSV 5.15 / 4.88 / 5.47; last ≥5.15 was 19 Oct (5.15) | ✅ |
| Fed Dec / Jan / Mar | 27.5bp, ~10% / ~74% / ~72% | ZQZ 95.925 → 27.48bp; ZQG 95.660 → 74%; ZQJ 95.480 → 72% (EFFR 3.88, FRED) | ✅ |
| HY OAS | 3.20% (12 Nov) | FRED 3.20 (12 Nov), 3.30 (11 Nov) | ✅ |
| Brent spot (FRED) | latest $92.14 (11 Nov) | 92.14 | ✅ |
| EIA scorecard | avg $96.92; ~$100.7 needed | 8-day avg 96.92; (100×44 − 775.38)/36 = 100.68 | ✅ |
| S&P / Nasdaq / Dow | −0.40% / −0.91% / 52,347.55 | −0.40 / −0.91 / 52,347.55 | ✅ |
| SOX / NVDA / AVGO / AMD | −3.4 / −2.0 / −4.8 / −8.8 | −3.43 / −2.01 / −4.76 / −8.75 | ✅ |
| VIX | 19.30 (high 20.92) | 19.30 / 20.92 | ✅ |
| STOXX / DAX / FTSE / CAC | 664.14 / 26,749.95 / 10,902.6 / 8,368.91 | same | ✅ |
| KOSPI / Nikkei / TAIEX / HSI | 5,290.53 / 61,142.35 / 43,675.12 / 23,637.60 | same | ✅ |
| Nifty / gap to pre-war | 25,144.30, −0.61%, 34 pts | 25,144.30, −0.61%; 25,178.65 − 25,144.30 = 34.35; 11 and 12 Nov closes above | ✅ |
| Sensex / Bank Nifty / Nifty IT / India VIX | −0.39% / 61,034.10 / 31,931.15 / 15.50 (−6.7%) | same (VIX −6.74%) | ✅ |
| IOC / BPCL / HPCL | 144.04 / 302.00 / 381.50 | same; BPCL week −5.60% | ✅ (streak ❌, Flag 9) |
| "within 0.2% of pre-war" | — | 0.14% | ✅ |
| Bernstein gap | 3.8% | 26,100 / 25,144.3 − 1 = 3.80% | ✅ |
| DXY / USD-JPY | 103.41 / 159.9 | 103.41 / 159.875 | ✅ |
| Brent evening slide | −$1.60 from 21:05 | ~−$1.00 from 21:05 (96.53 → 95.53) | ❌ Flag 10 |
| FII pace | "shrunk three days running" | two falls (7,212 → 12,563 → 7,831 → 5,737) | ❌ Flag 8 |

---

## Items That Passed

- **Night eleven and night twelve (PASS).** This is a reported absence, worded correctly as "no strike on Iran was reported", not "quiet". The Iranian official denial (Hormozgan) and the IRGC Isfahan denial are both carried. The OSINT feed is given no weight, and its clock problems are noted. KIN, DIP and ISR each ran their own search, so "Three of our desks searched separately" is true, though they read overlapping liveblogs.
- **The hold-rule text (PASS).** The deployment paragraph matches the `united-states` RESUME condition, including the (a) exception. "No qualifying US strike since 7 November" matches the 13-Nov brief.
- **Deployment conditions 1–3 (PASS).** They match the 13-Nov brief word for word. "Fails, by $0.84" is correct. The inflation leg fails (6.09%) and cannot be re-tested before 14 Dec. Proposals (i)–(iii) are labelled "for your decision, not applied"; only the Signal's "your proposed" misattributes (Flag 5).
- **CENTCOM on 13 Nov (PASS).** The quote is exact, there is one origin (CENTCOM on X), and the brief rightly says it was CENTCOM, not "the Pentagon". "Out by 18:44 IST" is a safe upper bound; RFE/RL may have had it by ~17:17 IST.
- **Bahrain on 15 Nov (PASS).** The brief has the sirens at 07:00 IST and Bahrain TV at 07:43 IST, with the exact quote. The Guards' six-drone claim is labelled unconfirmed, and "second stage" and "clear aggression" are both in KIN's translation. "They name no new attack on Iran" matches the IRIB statement and Aftab's roundup. "Not a first" matches the graph's July signal; June is even earlier.
- **Riyadh (PASS).** The coalition is the only source and is named as such. The brief has 06:51 IST, "three loud explosions" (Arab News), "relays give one to three", and "about 20 minutes apart" (04:08 against 04:30 KSA). "No source links" them is correct. "No Houthi claim by 10:10 IST": I did not re-find any later claim.
- **Washington quotes (PASS on the words).** Rubio's quote is the AP text; "not new" matches the G7 remark of 10 Nov (Reuters via BusinessDay, 11 Nov), which is the same in substance. The Reuters wording, "no commitment", MBS (31 Oct) and Erdogan all match DIP. The White House line matches. "None of his Saturday posts mentions Iran" rests on the trumpstruth.org archive. I found no Friday post that contradicts the brief, but did not check Friday fully.
- **Israel (PASS).** "Sunday evening" is Ynet's phrase. Channel 12's list (Gofman, Zini, Ben Ezra, Leiter) includes Netanyahu, as the ISR desk's rendering does. The Kan and Ynet quotes match. Netanyahu's quote is right, and "not new in substance" holds: the graph has "once and for all" from election night, and on 10 Nov he said "remove this existential threat permanently". Eisenkot holds the mandate (graph trigger fired 8 Nov). The brief quotes ToI/Magid's "fear Netanyahu will authorize an operation" correctly, and attributes the Fox characterisation of Gofman's trip to Fox.
- **Iran, IAEA and diplomacy (PASS).** Darzi's condition is kept. Khamenei is described as giving "no policy statement since 4 Nov". The IAEA is "new to our record", not called a first, and the graph has no earlier "diversion" line. AFP's "does intend to talk about Iran" is quoted correctly (not "will"). The Turkey–Qatar communiqué is paraphrased fairly. The Kalın call is "failing".
- **Ships and Houthis (PASS).** "At least three" is the right floor given the double-count risk, none named and all CLAIMED. "No new UKMTO notice" is correct. CENTCOM's "cleared the main routes" is attributed. "Hormuz is closed" is said to restate June. The station numbers (11, 7, 3) are right, and Saudi silence is noted.
- **Oil and the IEA (PASS, apart from Flags 10, 16, 17, 19).** "For the first time since the outbreak of the war" is labelled as Reuters' wording. The 18.4 mb/d, "26% below", 9.99 against 10.563 and "dark crossings" all trace to relays of the IEA report. The 19:16 burst is called unexplained, and the CENTCOM timing rules out CENTCOM as the cause. Reuters' three causes are carried. "Partly the war easing on the supply side" is a reasonable reading of the export recovery.
- **The Updates box (PASS).** CENTCOM's rebuttal is labelled an update, not a correction. UKMTO's seven and JMIC's four are both given, each with its basis.
- **India, other (PASS).** The PTI and ANI quotes, the rupee timing caveat, reserves and FCA, Puri's line as "not a new pricing decision", Monday's WPI and the RBI consensus all check out. A "one-year high" deficit is correct (October 2025 was $42.58bn).
- **Section II (PASS, apart from Flag 14).** The quotes and tests for Singh, Firebrand, Flynn and Kan's source match the dossier, and the tests are well-formed. The Kilduff, EIA, Bernstein, Goldman and Nissan outcomes recompute correctly.
- **Completeness (PASS).** Section I carries oil, rates, chips, India trade, the rupee and OMCs alongside the geopolitics. Section II has Flynn and the RBI economists. Cascade Watch carries gold, Brent, Fed, RBI and INR. The no-change claims (0 status changes, 15 edges activated, 415 edges) match `edge_changes.json` and `meta.json`.

## Not independently re-found (the search index lags; these rest on desk relays)
- Reuters' 14-Nov "hold off" story itself (I found related Reuters stories from 11 Nov and July–Aug).
- CENTCOM on Sunday's wave: none found, which is consistent with the brief.
- The Bahrain TV/BNA text, and the IRGC's 15-Nov statement in its original.
- The coalition's Riyadh statement, and any later Houthi claim (none found).
- IRNA's Jask line and the Hormozgan governorate's statement.
- The IEA report itself (the desks also used relays). The BLS PPI release. India's trade release and the RBI reserves release.
- Netanyahu's video, Eisenkot, Channel 12 and Kan.
- The IAEA report, and AFP's Shenzhen quote.
- Trump's Friday posts: still unchecked (DIP gap); I found no contradicting post in search.

## Final Verdict
**APPROVED WITH CORRECTIONS.** The facts behind the lead are sound: no strike reported on nights eleven and twelve, no reset, legs (a)–(d) quoted faithfully, and the 18 November date right. Every price checked matches.

The CoS's own lines need the work. The lead headline's "Instead… twice" and "line moved" (Flags 1–2), the Signal's self-contradiction, its reversal of Reuters' logic and its "your proposed" (Flags 3–5), and the US headline's "mostly about the Fed" (Flag 6) should all be fixed before publishing. So should the two counting errors (Flags 8–9) and the $1.60 slide (Flag 10).

*Basis: ran yfinance (44 tickers), FRED (HY, EFFR, Brent spot), the Treasury CSV, the 1-, 5- and 30-minute bar files and the sunset computation; read the brief, the CoS header R1–R14, the KIN, DIP, ISR, SAU, IND and MAC sections, the 13-Nov brief, the `united-states`, `bahrain`, `israel`, `saudi-arabia`, `fii-flows`, `indian-oil-marketing` and `us-10y-yield` nodes, and all triggers; sourced Reuters via BusinessDay (11 Nov) for Rubio's G7 remarks and Trump's 10-Nov hold-off. Not checked: primary texts for the IEA, BLS, CENTCOM 15 Nov, Reuters 14 Nov, or Trump's Friday posts. Confidence: high on the market flags and the counting errors; moderate-to-high on the interpretive flags (they rest on the dossier's own facts).*


---
## CoS application note (10:46 IST, `date`-checked)
All 19 flags applied as recommended (Flags 11–19 included; Flag 19's optional wording taken). Graph corrections G1–G5 applied (backup `backups/2026-11-15/graph_v2_preverif`); G6 folded into the G3 rewrite of the `united-states` summary. The `indian-oil-marketing` summary staleness (Day 241) is carried to the next run. `markets.md` aligned (evening slide, OMC streaks, FII count, trade-deficit framing, the 10Y attribution). Viewer rebuilt.
