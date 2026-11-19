# Verification Report — 19 November 2026 (Day 265), morning edition
Generated: 14:10 IST Thu 19 Nov (`date`-checked) | Fact-Checker: Red Team
Brief checked: `briefs/2026-11-19-morning.md` (read-only; not edited)
Scratch: `staging/2026-11-19-morning/verifier_scratch/` (yfinance daily + 1-minute pulls at ~14:03 IST, Naver/KRX index history, FRED, Treasury CSV)

## Summary
About 95 claims checked: every price and percentage in Section I and Page 2 recomputed, the 15 priority items in the task, all Section III trigger and edge citations matched against `graph-changelog.md` and `edge_changes.json`, and nine web checks.
**Flags: 1 CRITICAL, 4 HIGH, 6 LOW.** Graph corrections: 4 (G1–G4). No trigger moved on rhetoric. The two status changes (`kospi`, `gold`) are sound.

---

## Flags

### CRITICAL

**C1. KOSPI's Thursday close is wrong (and so are the two chip stocks)**
- **Brief text:** Section I: "then recovered (5,112.97 on Thursday)". Page 2, Asia table, 19 Nov: "5,112.97"; SK hynix / Samsung "1,179,000 / 195,700". Data note: "KOSPI (Thursday): post-auction re-pull; our pulls differ by up to 6 points."
- **Issue:** this is wrong market data. The final close is **5,137.89 (+70.45, +1.39%)**.
- **Evidence:** the Naver Finance index API (KRX data) gives 19 Nov close 5,137.89, open 5,090.04, high 5,137.89, low 4,963.61. yfinance `^KS11`, re-pulled at ~14:03 IST, also gives 5,137.89. Both sources match exactly on 13, 16, 17 and 18 Nov (5,290.53 / 5,100.50 / 4,968.48 / 5,067.44). Our pulls drifted from 5,115.80 (12:54) to 5,112.97 (13:05) and 5,118.96 (13:16), so none of them was the final print. yfinance now shows SK hynix 1,183,000 and Samsung 196,900. (Naver's stock prices include after-hours NXT trading, so I am not using them for the stocks.)
- **Replacement:** Section I: "then recovered (5,137.89 on Thursday)". Page 2: KOSPI "5,137.89"; SK hynix / Samsung "1,183,000 / 196,900". Data note: "KOSPI (Thursday): Korea Exchange final close (via Naver; yfinance agrees). Our pulls at 12:54–13:16 IST (5,112.97–5,118.96) came before the final print."
- **Substance:** small. No watch, call or condition depends on Thursday's figure, and "recovered" still holds. It is CRITICAL only because the doctrine treats any wrong price that way.
- **Applied:** No (CoS applies).

### HIGH

**H1. The Fed-minutes quote leaves out who said it**
- **Brief text:** "**The Fed:** its October minutes say "an increase of more than 25 basis points could warrant consideration at the next meeting", with inflation "largely reflecting rises in energy prices this year due to the Middle East conflict"."
- **Issue:** this is a minority view written up as the minutes' own view. The Fed text reads: "**A couple of participants noted that** an increase of more than 25 basis points could warrant consideration at the next meeting…", and it attaches a condition: if incoming inflation data were unfavourable. Without the attribution, the reader gets a much more hawkish Committee than the text shows. The vote was 10–2 to hold, and the two dissenters wanted only 25bp.
- **Evidence:** I read `federalreserve.gov/monetarypolicy/fomcminutes20261028.htm` directly. The phrase "largely reflecting rises in energy prices this year due to the Middle East conflict" is verbatim. MAC A-7 quoted the fragment without its subject.
- **Replacement:** "**The Fed:** in its October minutes, "a couple of participants noted that an increase of more than 25 basis points could warrant consideration at the next meeting" if inflation data were unfavourable; the minutes describe inflation as "largely reflecting rises in energy prices this year due to the Middle East conflict"."
- **Graph:** G2.

**H2. The hold rule's leg (a) is stated as certain, but the rule's own text cuts the other way**
- **Brief text:** Section III: "Leg (a), a strike the US acknowledges on the record, is **closest**: an on-record admission of Qeshm would meet it." The hold-rule paragraph adds: "The carve-out in (a) would not cover Qeshm: the stated trigger was fire at a radar site."
- **Issue:** the `united-states` RESUME condition (node file, read) ends with a sentence the brief leaves out: "**Single 'defensive' counter-launcher hits of the kind reported on Qeshm (2 Nov) are logged, not fired.**" Tuesday's strike fits that description exactly: one IRGC missile launch site, on Qeshm, called "self-defense". So the claim that an on-record admission *would* reset the rule is a disputed reading, not a fact.
  - The brief's reading has support: the 8-Nov note fired leg (a) on Trump's on-camera "minor strikes" remark about a Qeshm anti-aircraft site.
  - But that was a CoS ruling over KIN and DIP, who both recommended "log, not fire" (the note records both readings).
  - The aircraft/ships carve-out argument is correct as far as it goes. It does not deal with the closing sentence.
- **Why it matters:** this is the "closest" path to a reset, and the reset drives the deployment posture.
- **Replacement (Section III bullet):** "Leg (a), a strike the US acknowledges on the record, is **closest**: under the 7-Nov precedent an on-record admission of Qeshm would likely meet it, though the rule's own text says single 'defensive' counter-launcher hits on Qeshm 'are logged, not fired'."
- **Replacement (hold-rule paragraph, last sentence):** "The carve-out in (a), "fire on US aircraft or ships", would not cover Qeshm, since the stated trigger was fire at a radar site. But the rule's closing line, that single 'defensive' counter-launcher hits on Qeshm 'are logged, not fired', points the other way; the 7-Nov precedent fired leg (a) on an owned strike of this kind."
- **Add to "For your decision":** "(iv) whether an on-record US admission of a single 'self-defense' launcher strike meets leg (a), or is 'logged, not fired'."
- **Graph:** G3.

**H3. "One site" is the US account; Iran's own official says "locations"**
- **Brief text:** "**What it was:** one launcher site…". Hold rule: "Qeshm does not qualify: owned only by unnamed officials, one night, one launcher site."
- **Issue:** this gives one side only, and it bears on leg (c) ("several sites in one night"). The brief's own Nafisi quote says "The American attack on **locations** on Qeshm Island…". IRNA's Persian has "نقاطی" (points). Mehr, cited by The National (read), says US forces "struck several locations on Qeshm Island". Fars and Tasnim report "several explosions" and "several projectiles". The US official names one site.
- **Why leg (c) still fails:** every Iranian account traces to one origin (the governorate). There are not 2+ outlets with their own officials reporting several sites. So the conclusion holds; the wording does not.
- **Replacement (What it was):** "one launcher site by the US account (Iran's governorate speaks of "locations" on the island), hit in the Tehran afternoon or at dusk…"
- **Replacement (hold rule):** "owned only by unnamed officials, one night, and one named site (Iran's governorate says "locations", but no second outlet with its own officials reports several sites)."

**H4. The NAVIG8 MESSI name conflicts with ADNOC's casualty figures, and the brief hides it**
- **Brief text:** "Indian sources name it *NAVIG8 MESSI*; shipping minister Sonowal says its three Indians are safe."
- **Issue:** the IND desk (intel IND-B1; `research/05-india.md`) records Sonowal (PTI, 18 Nov 18:48 IST) saying the three Indians **and the "entire crew"** are "safe and accounted for". ADNOC L&S says "One crew member remains unaccounted for" and "Eleven sustained injuries".
  - If both refer to NAVIG8 MESSI, they contradict each other. CoS R4's "not a contradiction" holds only for the three Indians.
  - ADNOC has not named its ship, and Safety4Sea says the link is "not confirmed".
  - So the brief pins ADNOC's casualties on a name that the cited minister's own words dispute.
  - The basis line's "moderate on crew figures (sources conflict)" is not enough, because the body states the pairing as fact.
- **Replacement:** "Indian sources name it *NAVIG8 MESSI* (ADNOC has not named it). Shipping minister Sonowal says that ship's "entire crew" is "safe and accounted for", which conflicts with ADNOC's figures, so either the name or one of the accounts is wrong."

### LOW

**L1. Hang Seng.** The final close is now posted: **22,841.62 (−1.95%)**. Page 2 shows "~22,818 (13:20 IST, −2.0%; final close not posted)". If the brief goes out after 13:30 IST, use the final close and drop the caveat in the Clock line and the data note.

**L2. Tuesday's oil step and the FT stamp.** The brief says the step came "minutes after the FT's first report (18:32 IST)". The 1-minute bars show a small rise from the 18:30 bar ($93.03 → $93.19 by 18:32), which is *at* the stamp. The main leg came at 18:49–18:52 ($93.29 → $93.64), 17–20 minutes after. Suggest: "A step came in the 20 minutes after the FT's first report…". The current wording is defensible.

**L3. Gold and the minutes.** The brief says "~70% of gold's fall came before the minutes". In fact *all* of the settle-to-settle fall came before the minutes, which were released at 00:30 IST Thu, after the settle. About 74% came by 13:30 IST Wed (bars: $3,865 → $3,774, against a settle of $3,741.9). Suggest: "~70% of gold's fall came in Asian hours; all of it came before the minutes, which were released after the settle."

**L4. Nissan scoring standard.** "Failed on the strike leg (we read "owned" loosely here, unlike leg (a)…)" scores an outside call on a reading the brief rejects for its own rule. This is disclosed, so LOW. Cleaner: "**Strike leg contested:** a strike came, owned only anonymously, so it fails on a loose reading and is unmet on our leg-(a) standard; the price leg held."

**L5. "3–13 nautical miles off Khasab".** The ~3 nm figure is *ON Phoenix*'s, and Riviera gives it as "~3 nm off Oman". Its position (NAVAREA: near Ras Hindi?) is not tied to Khasab. Suggest: "3–13 nautical miles off Oman's Musandam coast, mostly north of Khasab".

**L6. Gold/silver "settled at 82.2, 81.6 and 83.0".** Recomputed from the settles: 82.22 / 81.60 / 83.04. Correct. Thursday's live 82.5 ($3,735.0 / $45.290 = 82.47) is also correct. No change needed. Listed only because the task asked for a recomputation.

---

## Graph corrections (list only; CoS applies)
- **G1 — `kospi`, `south-korea`, `sk-hynix`, `samsung` (signals/current) and the changelog (`kospi` status-change text, signal #1):** replace "5,112.97 (Thu 19, final; MAC re-pull after the auction…)" with "5,137.89 (Thu 19, KRX final via Naver; yfinance agrees; our 12:54–13:16 pulls of 5,112.97–5,118.96 came before the final print)". Replace Thursday's SK hynix ₩1,179,000 with ₩1,183,000 and Samsung ₩195,700 with ₩196,900 (yfinance re-pull). The `kospi` firing on 17 Nov is unaffected.
- **G2 — `fed` node (two signals carrying the quote):** prefix the quote with its subject: "'A couple of participants noted that an increase of more than 25 basis points could warrant consideration at the next meeting' (if inflation data were unfavourable)". The `brent-crude → fed` 9.0 → 10.0 raise stands: the "largely reflecting… Middle East conflict" and "vast majority… high energy prices" lines are verbatim.
- **G3 — `united-states` RESUME `note_2026-11-19`:** after "an on-record admission WOULD meet (a)", add: "contested: the condition's last sentence ('Single defensive counter-launcher hits of the kind reported on Qeshm (2 Nov) are logged, not fired') supports the opposite reading; the 8-Nov firing on this kind of strike was a CoS ruling over KIN/DIP 'log, not fire'. Flag for the user's ruling." Status stays fired, no reset.
- **G4 — `united-states` / `irgc` / `iran` Qeshm signals:** where they say "one site", add "(US account; Iran's governorate: 'locations'/'points'; Mehr: 'several locations')". The `united-states → irgc` 7.5 → 9.0 raise stands (strike CONFIRMED by both sides).

---

## Trigger Point Review

| Trigger | Status in changelog | My assessment | Agreement? |
|---|---|---|---|
| `kospi` close < 5,000 | watching → fired | 4,968.48 on 17 Nov, confirmed by Naver/KRX and yfinance. "First close below 5,000 since 2 Feb" is verified: in 240 sessions of history the last close below 5,000 was 4,949.67 on 2 Feb 2026. Data threshold, not war-driven. | ✅ AGREE (rebound figure wrong: G1) |
| `gold` gold/silver > 80 on settles | watching → fired | Recomputed from GCZ26/SIZ26: 82.22 / 81.60 / 83.04. Scored on its own 16-Nov rule (settles). | ✅ AGREE |
| `united-states` RESUME (hold rule) | stays fired, no reset | No reset is correct: no on-record ownership, nights 14 and 16 quiet, leg (c) one origin, leg (d) a missile site. Sun 22 Nov is the correct earliest leg-(b) completion (nights 17–19). The 16-Nov "Thursday 19 Nov" test is correctly scored as failed: night 14 was quiet. | ✅ AGREE on status; ❌ DISAGREE that an on-record admission "would" meet (a) (H2, G3) |
| `bahrain` confirmed hit | not fired | Every on-record account says intercepted; "zero impacts" (US official). | ✅ AGREE |
| `kuwait` hit watch (new) | added | Well formed: fires only on a confirmed hit. Not a duplicate. The `kuwait` node supports "first since September" (3 Sep claim on Ahmad al-Jaber). | ✅ AGREE |
| `israel` joint campaign (new) | added | Well formed: both roles confirmed, 2+ nights, by 31 Dec. Distinct from the cabinet watch and the 8-Nov/14-Sep US watches. | ✅ AGREE |
| `israel` cabinet watch | not fired, closer | Channel 13 is one outlet with an unnamed officer. No PMO/IDF approval. | ✅ AGREE |
| `strait-of-hormuz` 2-Nov blacklist | closest | The list page is unread (Seatrade 403), the owner is silent and one monitor shows "removed". "Not certain" is honest. | ✅ AGREE |
| `houthis` Aden | closest | No wire puts Houthi forces on "the heights"; Tur al-Bahah holds (AP). | ✅ AGREE |
| `vix` > 25 with a kinetic event | closest | ^VIX 17 Nov close 25.46 confirmed. The timing of the 27.7 high is unproven and CNBC gives non-war causes. | ✅ AGREE |
| `european-ttf-gas` < €80 | closest | TTF=F 18 Nov 80.848; Thu 82.45. | ✅ AGREE |
| `inr-usd` < 93 | closer | Best PTI close 93.41; yfinance ~93.33 live. | ✅ AGREE |
| `fed` 50bp | closer | Recomputed: ~4% / ~4% / ~7% / ~10% (ZQZ26 95.935 / 95.935 / 95.930 / 95.925; EFFR 3.88; effective 10 Dec). | ✅ AGREE |
| `oman` | closer | Ships in Omani waters are not Omani territory; attacker unnamed. | ✅ AGREE |
| `china` Shenzhen readout | pending to 20 Nov | No Chinese readout naming Iran found by the desks. | ✅ AGREE |

The edges cited in the brief (5 raised, 1 new: `semiconductors → fii-flows` at 3, inverse sign) match `edge_changes.json` exactly. All raises rest on CONFIRMED actions or data. None rests on rhetoric.

---

## Market Data Spot-Check

| Data point | Brief | Verified | Match? |
|---|---|---|---|
| Brent Jan settles 13/16/17/18 Nov | 95.84 / 92.44 / 93.14 / 91.95 | BZF27: same | ✅ |
| % moves Mon/Tue/Wed | −3.55% / +0.76% / −1.28% | −3.55 / +0.757 / −1.278 | ✅ |
| Brent at 14:00 IST Mon | $96.62 | 96.62 | ✅ |
| Brent Tue low / high | 91.25 / 94.14 | 91.25 (08:03) / 94.14 (19:46) | ✅ |
| Brent Wed 22:34 low | $90.35 | 90.35 (22:34) | ✅ |
| Thu 06:30 → 07:24 | 91.23 → 93.05 (+$1.82) | high 93.05 at 07:24; ~91.2–91.4 at 06:30 | ✅ |
| "Only oil moved" (06:29–07:24 IST) | gold, ES, DXY flat | gold −0.04%, ES −0.28%, DXY +0.05%; Brent +1.84% | ✅ |
| "Mostly faded within the hour" | — | 93.02 (07:24) → 91.85 (08:30) | ✅ |
| Brent at 13:16 IST | $92.13 | spot-raw 92.13; 1-minute bars 92.03–92.29 | ✅ |
| Curve Feb/Jun/Dec-27; Jan–Dec spread | as tabled | BZG27/BZM27/BZZ27 match; spreads 15.86/14.55/15.96/15.69/15.64 | ✅ |
| WTI, HO, RBOB, NG Dec | as tabled | CLZ26/HOZ26/RBZ26/NGZ26 match | ✅ |
| TTF −11.1% to €80.85 | | 90.952 → 80.848 (−11.1%) | ✅ |
| FRED Brent spot | 92.90 / 92.94 | 92.90 / 92.94 | ✅ |
| Gold / silver / ratio | as tabled | match; ratio 79.1 / 82.2 / 81.6 / 83.0 | ✅ |
| Copper −5.3% / aluminium −4.0% | | −5.29% / −4.00% | ✅ |
| KOSPI 17 Nov / Thu | 4,968.48 / 5,112.97 | 4,968.48 / **5,137.89** | ✅ / ❌ C1 |
| TAIEX −4.40%; −12.0% since 13 Nov | 38,426.89 | 38,426.89; −4.399%; −12.02% | ✅ |
| Nikkei, TSMC | 59,444; 2,100 | 59,444.21; 2,100 | ✅ |
| Hang Seng | ~22,818 (13:20) | 22,818 at 13:20; final 22,841.62 | ✅ (L1) |
| S&P −3.15% Fri→Wed; Dow −1.64% / S&P −1.03% Tue | | −3.148% / −1.645% / −1.026% | ✅ |
| SOX −5.28% / Nvidia −4.1% Mon; Nvidia −2.9% Wed | | −5.279% / −4.12% / −2.89% | ✅ |
| STOXX −1.75% / −1.03% | | −1.75% / −1.025% | ✅ |
| VIX closes | 22.91 / 25.46 / 24.56 | same | ✅ |
| 10Y par (and 2Y/30Y) | 5.15/5.12/5.10/5.07 | Treasury CSV: same, all tenors | ✅ |
| HY OAS | 3.20 (12) / 3.23 / 3.34 / 3.43 | FRED BAMLH0A0HYM2: same | ✅ |
| Fed 50bp odds | ~4/~4/~7/~10% | recomputed: 4.3 / 4.3 / 7.1 / 9.9% | ✅ |
| Nifty closes; Thu 13:16; Thu low | 25,291.10 / 25,387.40 / 25,227.95; 25,355.75; 25,104.80 | same; 25,104.80 at the 09:30 bar | ✅ |
| Nifty +0.84% Fri→Thu; −0.63% Wed | | +0.841% / −0.628% | ✅ |
| Nifty IT −4.2% since Mon | 31,941.05 → 30,611.35 | −4.16% | ✅ |
| IOC/BPCL/HPCL +1.5–1.9% | | +1.83 / +1.52 / +1.86% | ✅ |
| DII three-day | −₹6,482 cr | −3,519 + 197 − 3,160 = −6,482 | ✅ |
| FII "thirteen straight" | 13 | 10 (to 13 Nov, as corrected in the 16-Nov brief) + Mon + Tue + Wed, all positive = 13 | ✅ |
| Signal: Brent −$3.71 since Friday; Tue war-led +$0.70 | | 95.84 − 92.13; 93.14 − 92.44 | ✅ |
| DXY | 103.86 / 103.81 live | 103.86 / 103.77 | ✅ |

---

## Items that passed (with why)

- **Qeshm strike (confirmed; ownership reported).** The language is right. The National (read) carries the unnamed US military official's statement. Gulf News and Arab News PK headlines match. The Iranian official is on the record (Nafisi via IRNA). No CENTCOM, Pentagon or White House ownership was found, and The National attributes the statement to "a US military official", not CENTCOM. "First strike on Iranian territory reported since 12–13 Nov" matches the 13-Nov brief (Sirik, night ten) and the 15/16-Nov briefs (nights 11–13 quiet). "Tuesday evening (IST)" fits a strike before the FT's 18:32 IST stamp. Caveats: H3.
- **Iranian fire at Bahrain and Kuwait.** The CENTCOM quote matches the Gulf News search summary. Kuwait's army wording and Iran's army claim are correctly tagged as claims. "First since September" is Reuters' wording per R14, and the graph is consistent with it. "Zero impacts" is correctly attributed to a US official. `bahrain` correctly not fired.
- **Washington.** The NYT is tagged as relays of unnamed officials, with "has not made a final decision" included. Trump's Fox quotes are tagged as relays and treated as rhetoric. "A waste of time" does not appear in quotation marks in the brief (it is not used at all). The CNN report is single-origin, with both sides' replies.
- **Israel.** Channel 13 is flagged as one outlet with the approver unnamed. Cooper at the Kirya rests on an IDF statement. The cabinet watch is not fired.
- **Oil causes.** Every day's attribution is sourced and hedged. The Thursday trigger is "not established", which is correct given the NYT stamp at 04:43 IST and the move starting at the 06:30 open. The Wednesday oil-specific minutes are consistent with the bars (22:00 → 22:34 IST: Brent −$0.92 while gold rose +$5 and ES +19).
- **Deployment conditions.** All three are word for word against the 16-Nov brief. Scoring is correct: condition 1 met; condition 2 fails on both legs (the credit leg 3.20 → 3.43 is confirmed); condition 3 half met. Posture unchanged.
- **Updates box.** All four entries are accurate against the 16-Nov brief and the evidence: the test failed on night fourteen; three carriers became two (Pacific Fleet spokesperson, R6); "since 2002" is withdrawn; *Al Dhannah* is carried with its caveat.
- **Yemen command.** The names and titles match SAU (Lt Gen Fayyad bin Hamed Al Ruwaili, CGS since 2018). Reuters' "up to six months" and "so far withheld" are tagged REPORTED. "60 targets" is a coalition claim. Houthi pumping-station claims are marked unconfirmed.
- **Recycled-content sweep.** None found. The CNN dirty-bomb report, Kallas, the command change, *ON Phoenix* and Gofman are all absent from the 16-Nov brief. The 16-Nov UKMTO notice was the 15-Nov Indian-authority report, which today's brief does not re-present as new.
- **Completeness (Check 7).** Section I has three market/business items out of seven. Section II has Morgan Stanley and HSBC. Cascade Watch covers TTF, VIX, gold, the Fed and the rupee. All 57 modified nodes are in the changelog.

## Not independently re-found (search index lags)
The NYT strike-planning wording and its 04:43 IST stamp; Trump's Fox interview; CENTCOM's X post (seen only through the Gulf News summary); Kuwait's army statement and Reuters' "first since September"; the *George Washington* departure; the MEA's *Tara Gas* statement; ADNOC L&S via WAM; UKMTO 207-26 and 208-26; the Channel 13, Maariv and Reuters Gofman reports; Reuters' Saudi six-month exclusive; the coalition's "60 targets"; NSDL ₹99,158 cr and BS's "highest-ever"; PTI's rupee closes and "seven-month high"; Araghchi and Qatar in Muscat; the IAEA Board and Grossi; Kallas (EEAS); the Sonowal "entire crew" line (H4 relies on the IND desk's text). These rest on the desks' sourcing.

## Final Verdict
**APPROVED WITH CORRECTIONS.** Fix C1 (KOSPI 5,137.89) and the four HIGHs before publishing.
- H1: the minutes' "a couple of participants".
- H2: the leg-(a) reading is contested by the rule's own last sentence, so it goes to the user as a decision.
- H3: Iran's "locations".
- H4: the NAVIG8 MESSI conflict.

The core picture holds on every check I could run: one strike, owned anonymously, no reset; Iranian fire intercepted; four or more ship hits with no attacker named; oil below $95 for non-war reasons; two market watches fired on data. The prices are clean apart from Korea's Thursday close.

*Basis: ran yfinance daily and 1-minute pulls (~14:03 IST), FRED (HY OAS, Brent spot, DGS2/10, EFFR), the Treasury par CSV and the Naver/KRX index history; read the brief, the CoS header and rulings, the DIP/KIN/IND/MAC sections, the changelog, `edge_changes.json`, the `united-states` RESUME condition and its notes, the `kuwait` node, the 13/15/16-Nov briefs and the Fed minutes page; web-fetched The National on Qeshm. Not checked: the NYT, Fox, Channel 13, MEA, ADNOC, UKMTO and Reuters exclusives at source (index lag). Confidence: high on C1, H1 and the market table; moderate-high on H2 (a reading of the rule text, which the user decides); moderate on H3; moderate on H4 (rests on one desk's relay of Sonowal).*

---

## Corrections applied by the Chief of Station (14:12–14:14 IST, 19 Nov)
- **C1** applied: KOSPI Thursday 5,137.89 (Section I, Page 2, data note); SK hynix ₩1,183,000, Samsung ₩196,900 (CoS re-pull 14:12 IST agrees).
- **H1** applied: the minutes quote now begins "a couple of participants noted that…", with the condition (unfavourable inflation data).
- **H2** applied: Section III bullet and the hold-rule paragraph now say leg (a) is contested (the rule's last sentence vs the 7-Nov precedent); added the user's decision **(iv)**.
- **H3** applied: "one launcher site by the US account (Iran's governorate speaks of 'locations')"; hold rule: "one named site… no second outlet with its own officials reports several sites".
- **H4** applied: NAVIG8 MESSI sentence now flags the conflict (ADNOC has not named its ship; Sonowal: "entire crew" safe).
- **L1** applied: Hang Seng final close 22,841.62 (−1.95%) in the table and Significant Moves; caveats removed from the Clock line and data note.
- **L2** applied: "in the 20 minutes after the FT's first report" (Section I and Page 2).
- **L3** applied: gold — "~70% in Asian hours; all of it before the minutes (released after the settle)".
- **L4** applied: Nissan row — "Strike leg contested".
- **L5** applied: "3–13 nautical miles off Oman's Musandam coast, mostly north of Khasab"; the Signal says "off Musandam".
- **L6:** no change needed.
- **CoS edit (own gate check):** the Muscat bullet now explains Iran's restated two-day reopening offer (sanctions relief, frozen assets, compensation); Risk Landscape wording matched.
- **Graph G1–G4** applied by `staging/2026-11-19-morning/gu_corrections.py` plus three `current`-field fixes in `kospi`/`south-korea` (backup `backups/2026-11-19/graph_v2_preverif`); JSON validated; viewer rebuilt (63 nodes, 417 edges). No trigger status or edge weight changed.
