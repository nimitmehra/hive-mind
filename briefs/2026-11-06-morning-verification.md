# Verification Report — 6 November 2026 (edition "morning", Day 252)
Run: 17:13:55 → 17:33:14 IST Fri 6 Nov 2026 (`date`-checked at start and before writing) | Fact-Checker: Red Team | **Status at publish (CoS, 17:39 IST): all 23 brief flags (H1–H6, L1–L17) and all 10 graph corrections (G1–G10) APPLIED.** The fact-checker edited nothing; the Chief of Station applied the corrections (`gu_part_post2.py`; brief diff vs `brief_pre_verification.md`).
Brief checked: `briefs/2026-11-06-morning.md` (file written 17:13:21 IST).

**Evidence used:** the brief; `intel.md` (CoS header, all six desks, sections A–F); `markets.md`; `coS-spot-checks.md` and `-raw.txt`; `fred-check.txt`; `graph-changelog.md` (all 130 + 4 trigger rows); `graph/nodes/*.json` (fired triggers' full text and dated notes; today's signals and `current` fields); `graph/edges.json`; the 4-Nov and 5-Nov briefs (deployment and hold-rule wording; Section II tests); the 5-Nov verification report.

**My own re-pulls (17:19–17:30 IST):**
- yfinance daily: BZF27, BZG27, BZZ27, CLZ26, HOZ26, RBZ26, NGZ26, GCZ26, SIZ26, TTF=F, ZQX26, ZQZ26, ^GSPC, ^IXIC, ^DJI, ^SOX, ^VIX, ^TNX, ^NSEI, ^BSESN, ^KS11, ^N225, ^TWII, ^STOXX, ^GDAXI, DX-Y.NYB, INR=X. Every level in Page 2 matches.
- yfinance 15-minute January Brent bars, 4–6 Nov (rupee-close times; the Qatari-readout hour; Thursday's path vs the US open).
- History: S&P since 2025; SOX since 1994; Nikkei/TAIEX/KOSPI/S&P/Nasdaq/SOX closing peaks; Nifty since 2020 (closes after 27 Feb; weekly moves); VIX since 2016; BZ=F and INR=X on 27 Feb 2026; INR=X since 22 Apr.
- US Treasury par-curve CSV (2026, through 5 Nov); FRED BAMLH0A0HYM2, BAMLC0A0CM, DGS2, DGS10, T10YIE, EFFR (5-Nov HY OAS still unpublished at 17:23 IST).
- Recomputed: Fed December odds (9 old-rate days, EFFR 3.88), every % in Sections I–III and Page 2, the diesel crack, spreads, the 17-claim tally, the FII five-session total.

**Web checks (19 searches, 4 fetches):** the search index is ~1–2 days stale for most 5–6 Nov items. Re-found: RBI reserves (RBI release prid 63939, fetched); BoE 4% 8–1 (BoE Monetary Policy Summary, fetched); *Velos Sapphire* (Lloyd's List page fetched; Splash247, Maritime Executive, gCaptain, OSINT613 headlines); Aramco −$6.50 / $2 cut / "lowest since May 2020" (Newsquawk via ZeroHedge, fetched); November OSP −$5 ("widest discount since 2020", investingLive); Goldman's previous cut to $4,650 (consistent with "from $4,650"); Ante Zigman is Croatia's central-bank governor (name not invented). Not re-found: see the last section.

---

## Summary

- **About 210 items checked:** ~150 numbers; ~45 factual, attribution and quote claims; 4 fires, 1 amendment, 4 not-fired calls and 4 new watches; 12 graph signals/`current` fields; 6 edges.
- **Flags in the brief:** 0 CRITICAL, **6 HIGH**, **17 LOW**.
- **Graph corrections:** 10 (G1–G10; 3 HIGH, 7 LOW).
- **Market data:** every price, close, yield, spread and odds figure matches my re-pull. Every "worst/highest/best since" claim checks out on yfinance history. No CRITICAL data error.
- **Triggers:** I agree with all four fires and with the `vix` amendment. **No trigger moved on rhetoric.** One disagreement is about the *logged cause*, not the status: `inr-usd` is logged "flows, not oil" on a session-misaligned comparator (H2, G1).
- **Main problems (all in the CoS's own framing, as in past runs):**
  1. **"Record" foreign money** in the India headline. Reuters says the largest in *nearly six years*; larger days exist in 2020–21 (H1).
  2. **"Flows, not oil"** for the rupee compares Friday with Wednesday's *settle*, which came after Wednesday's rupee close. It also quotes Parmar's "flow-driven" and drops his "softer crude oil" in the same remark (H2).
  3. **The Signal You Might Miss** overreaches four ways: "India has priced the war out" (the rupee and India VIX say otherwise); "much of this week's money came because India has no AI stocks" (no fund data; the brief's own Thursday line says oil); "oil rose too" (at rupee closes Brent fell ~$5); "the 9–11 November window that officials flag" (H3, H4).
  4. **"Officials point at 9 November"** turns unnamed officials *noting a new moon* into officials pointing at a strike date, which is the TASS reading the kinetic desk said not to use (H4).
  5. **A conditional threat quoted as unconditional** (Akraminia's "If Iran is attacked…" dropped) (H5).
  6. **Saxo's test pinned on Yardeni** in Section II (H6).
- **Proportionality (Check 7): passes.** Section I has 4 market/economic items to 5 geopolitical. Section II is all market or market-linked voices this time (Rapidan/ING, Kotak, Yardeni/Truist); geopolitical calls such as Pusztai's "major wave mid-to-late Nov" are only in the scorecard. Section III's fires are all market cascades. Graph completeness gap: `bahrain` and `kuwait` were listed as affected and not updated (G10).

---

## Flags — HIGH

### H1: "Record foreign money" is wrong; Reuters says the largest in nearly six years
- **Severity:** HIGH (false superlative in a headline; repeated in the deployment case and the graph).
- **Evidence:**
  - Reuters (IND-A1, BR relay 08:13 and 15:37): ~$1.6bn, "the biggest single-day buying in nearly six years". That means larger days exist, around Dec 2020.
  - IND-A1: secondary relays conflict on "since when" (Sep 2024 / 24 Feb 2021 on ₹14,796 cr / Dec 2020 on ₹15,350 cr). The desk did not check the series.
  - Business Standard (web, Sep 2024): ₹14,064 cr was then "the largest single-day purchase since 24 February 2021". So bigger days exist before Feb 2021.
  - Outlook Money (IND-A1): FPIs are still −₹2.95 lakh cr year-to-date, "the worst annual exodus on record".
  - The Nifty is 0.59% *below* its 27-Feb close (my calculation: 25,030.35 vs 25,178.65), so "at its pre-war level" is fine as "near".
- **Current text (Section I heading):** `### India closed at its pre-war level, on record foreign money that came partly for a non-war reason.`
- **Replacement:** `### India closed near its pre-war level, on the largest foreign buying in nearly six years, some of it for a non-war reason.`
- **Current text (Deployment):** `**The case for acting now:** two of the three hold-rule legs are met, and the foreign money is the largest in six years.`
- **Replacement:** `**The case for acting now:** two of the three hold-rule legs are met, and Thursday's foreign buying was the largest single day in nearly six years (Reuters).`
- **Graph:** G3.

### H2: The rupee's "flows, not oil" rests on the wrong comparator and a clipped quote
- **Severity:** HIGH (causation claim; selective quotation; carried into a fired trigger's logged cause).
- **Evidence:**
  - **Wrong anchor.** Wednesday's $94.62 settle printed at ~01:00 IST Thursday, *after* Wednesday's rupee close. This is the same session misalignment as the 5-Nov G1.
  - **January Brent at India's 15:30 IST rupee closes (my 15-minute bars):**
    - Wed 4 Nov: **$102.25** (rupee 94.46).
    - Thu 5 Nov: **$96.04** (rupee 94.41).
    - Fri 6 Nov: **$96.82–97.47** (rupee 93.89).
  - **What the bars show:**
    - Thursday to Friday, Brent was ~$1 higher at the rupee close while the rupee gained 52 paise. So flows did most of Friday's gain.
    - Inside Friday's session, Brent fell from $100.71 (09:00 IST) to $96.82 (15:15). INR=X moved 94.44 → 93.91 over the same hours. The rally tracked the slide.
  - **Clipped quote.** Parmar's same remark (IND-A2): the move is "backed by the supportive mix of softer crude oil, easing yields" and inflows; "a flow-driven strength". The brief keeps only the second half.
  - **Other named sources cite oil:**
    - Reuters names "the post-midterm oil fall" among the drivers.
    - PTI's close copy names "declining crude".
    - IND-A2: "The ~$4 slide in Brent during India's Friday hours helped at the margin."
    - IND-B1: "Oil did help on Friday, within India's hours."
- **Current text (Section I, India):** `- Friday's gain came with Brent *above* Wednesday's settle, so it was flows, not oil. HDFC Securities' Parmar calls it "a flow-driven strength".`
- **Replacement:** `- Flows did most of it: between Thursday's and Friday's rupee closes Brent was about $1 higher, yet the rupee gained 52 paise. But Friday's rally also tracked a ~$4 intraday fall in Brent. HDFC Securities' Parmar calls it "a flow-driven strength", "backed by the supportive mix of softer crude oil, easing yields"; Reuters also cites the post-midterm oil fall.`
- **Also (Page 2, USD/INR row "Why"):** `Flows; no RBI action named` stands. Section III `inr-usd` line: `Logged cause: flows, not oil.` → `Logged cause: mainly flows; softer crude in India's hours helped.`
- **Graph:** G1, G2, G4.

### H3: The Signal You Might Miss overreaches on "priced out", on the AI share and on the oil–rupee edge
- **Severity:** HIGH (the CoS's own intent and share claims; one statement is factually wrong).
- **Evidence:**
  - **"Priced the war out".** Only the equity index is back near its pre-war level. The brief's own gap line has the rupee at 93.89 against ~91 (INR=X 91.007 on 27 Feb). India VIX's 17.47 is its highest close since at least 1 Sep (yfinance; 26 Oct 17.16). FPIs are still −₹2.95 lakh cr YTD.
  - **"Much of this week's money came because India has no AI stocks".** IND-B1: the rotation is "**inferred, not traced**"; "no fund-level data show the same money moving".
    - Thursday's ₹14,975 cr is 42% of the five-session ₹35,809 cr. PTI tied Thursday to West Asia de-escalation and the oil fall, and so does the brief's own line ("It traded Wednesday night's oil fall").
    - Friday's FII print is unpublished.
    - What *is* sourced: Reuters (6 Nov) says JPMorgan, Goldman and BlackRock "have highlighted India's appeal for investors diversifying away from AI-heavy markets".
  - **"The rupee rose on flows while oil rose too" is wrong at rupee-close times.** Brent fell from ~$102.3 to ~$96.0 between Wednesday's and Thursday's rupee closes, and the rupee moved 5 paise. That *fits* the asymmetry the edge encodes; it is not "untested because oil rose". On the week, January Brent fell 13.4%.
  - **The hedge.** IND-A1: FIIs cut the index-futures net short from 1.86 to 1.37 lakh contracts in one day, "so they covered shorts as well as buying cash". The desk says this weakens the "hedged" reading. The brief prints only the residual short.
- **Current text:** `India has priced the war out; oil has not.`
- **Replacement:** `India's stock index has priced the war out; its currency and oil have not.`
- **Current text:** `- **The engine:** much of this week's money came because India has no AI stocks. That is a reason that does not depend on Iran and that can reverse on its own.`
- **Replacement:** `- **The engine:** part of this week's money is a bet that India has no AI stocks (Reuters cites JPMorgan, Goldman and BlackRock on India's appeal to investors leaving AI-heavy markets); no fund-level data show how much. Thursday's biggest day in nearly six years was tied mainly to the oil fall (PTI). The AI reason does not depend on Iran and can reverse on its own.`
- **Current text:** `- **The edge:** the graph's `brent-crude → inr-usd` link (10.0) is marked asymmetric. It was not tested this week, because the rupee rose on flows while oil rose too. It would be tested by an oil spike.`
- **Replacement:** `- **The edge:** the graph's `brent-crude → inr-usd` link (10.0) is marked asymmetric: oil spikes pass through to the rupee, falls barely do. This week fits that: Brent fell ~$6 between Wednesday's and Thursday's rupee closes and the rupee moved 5 paise; Friday's 52-paise gain came with Brent ~$1 higher, on flows. Only an oil spike is a clean test.`
- **Current text:** `- **The hedge:** foreigners are still net short 1.37 lakh index-futures contracts.`
- **Replacement:** `- **The hedge:** foreigners are still net short 1.37 lakh index-futures contracts, down from 1.86 lakh a day earlier: they covered shorts as well as buying cash.`
- **"The risk" line:** see H4.

### H4: "Officials point at 9 November" amplifies an unnamed moon-phase note into a strike date
- **Severity:** HIGH (headline elevation of an unnamed-source hint; a "9–11 November window that officials flag" that no official named).
- **Evidence:**
  - KIN-A2: Fox's own text says only that officials "**noted**" that "Nov. 9 marks a new moon in the Middle East, meaning little to no moonlight". TASS's relay turned it into the US "considering… resuming the war on November 9". The desk's instruction: "**Use Fox's wording.**"
  - DIP-A1: "The new-moon line and the Reuters sources sharpen the 9–11 Nov window, but both are unnamed." The Reuters sources' affiliation is not given.
  - The "11" comes from the Iraqi airspace alert for 7–11 Nov. KIN-B2: "REPORTED, low", one OSINT origin, no NOTAM.
  - The new moon itself is right: the mean-lunation date is ~9 Nov 2026.
- **Current text (Section I heading):** `### Trump said a decision is coming; officials point at 9 November. Night three passed with no strike.`
- **Replacement:** `### Trump said a decision is coming; unnamed officials told Fox that 9 November is a new moon. Night three passed with no strike.`
- **Current text (Signal):** `- **The risk:** a qualifying strike in the 9–11 November window that officials flag would hit a market at its pre-war level from two sides, through oil and through the reversal of that hedged money.`
- **Replacement:** `- **The risk:** a qualifying strike, if it came around the 9-November new moon that unnamed officials noted to Fox, would hit a market at its pre-war level from two sides: through oil, and through the reversal of foreign money that is still partly hedged.`
- **Current text (Deployment, case against):** `... and the date officials flag (9 Nov) falls before the rule's own 11-Nov date.`
- **Replacement:** `... and the 9-November new moon that unnamed officials noted to Fox falls before the rule's own 11-Nov date.`
- **Graph:** G8.

### H5: Akraminia's threat is quoted without its condition
- **Severity:** HIGH (misquote; it turns a retaliatory threat into an open-ended one).
- **Evidence:**
  - KIN-A3 (Gulf News live, 11:48 Dubai 6 Nov) and DIP-A1: "**If Iran is attacked,** it will target all assets of the American enemy without regard to any geographical restrictions".
  - The `artesh` graph signal carries the full sentence. Only the brief drops the "if".
  - Balali's exact words (KIN-A3): "In the event of a new aggression, any country or force that helps America attack Iran can be a legitimate target of the Islamic Republic."
- **Current text:** `**The threats.** Army spokesman Akraminia: Iran will hit "all assets of the American enemy without regard to any geographical restrictions". An IRGC adviser: any country helping a US attack "can be a legitimate target".`
- **Replacement:** `**The threats.** Army spokesman Akraminia: "If Iran is attacked, it will target all assets of the American enemy without regard to any geographical restrictions." An IRGC adviser: "In the event of a new aggression, any country or force that helps America attack Iran can be a legitimate target".`

### H6: Saxo's test is pinned on Yardeni, and Lerner's quote is trimmed
- **Severity:** HIGH (misattributed falsification test; tomorrow's scorecard would grade Yardeni on a call he did not make).
- **Evidence:**
  - MAC analyst takes:
    - **Yardeni:** "I don't think this is an AI bubble bursting… an AI bubble losing some air very, very rapidly." Desk test: the NDX stays above a 20% drawdown (≥24,980) through 31 Dec.
    - **The "SOX back above 10,268.65 by 30 Nov" test** belongs to **Saxo's Neil Wilson** ("looks totally overdone").
  - Yardeni predicted no rebound, so a rebound test misstates him.
  - **Lerner's words:** "**something of** a buyers' strike in tech."
  - **"It moves money into India"** is stated as fact. IND-B1: inferred, not traced.
- **Current text:** `### Yardeni vs Truist on the AI sell-off — new (non-war, but it moves money into India)`
- **Replacement:** `### Yardeni vs Truist on the AI sell-off — new (non-war; brokers say it is moving money into India)`
- **Current text:** `Yardeni: "an AI bubble losing some air very, very rapidly", not bursting. Truist's Lerner: "a buyers' strike in tech".`
- **Replacement:** `Yardeni: "I don't think this is an AI bubble bursting… an AI bubble losing some air very, very rapidly." Truist's Lerner: "something of a buyers' strike in tech."`
- **Current text:** `**Test:** the SOX back above 10,268.65 by 30 November (Yardeni), or a close below 9,011 by 20 November (Lerner).`
- **Replacement:** `**Test:** the Nasdaq-100 stays within 20% of its peak (at or above ~24,980) through 31 December (Yardeni), or a SOX close below 9,011 by 20 November (Lerner).`

---

## Flags — LOW

### L1: The header stamp is in the future
- **Evidence:** the brief file was written at 17:13:21 IST. At 17:33 it still says "Generated ~17:45 IST… (`date`-checked)". See memory: run `date` before any "Generated" stamp, because the uploader publishes within ~2 minutes.
- **Current text:** `*Generated ~17:45 IST Friday (`date`-checked) | Graph: 63 nodes, 415 edges | Day 252*`
- **Replacement:** re-stamp with the actual `date` output at publication: `*Generated ~HH:MM IST Friday (`date`-checked) | Graph: 63 nodes, 415 edges | Day 252*`.

### L2: Oil "on the war" and "trading the Gulf again" are stated more firmly than the desks found
- **Evidence:**
  - January Brent was $94.13 at 12:15 IST and $97.73 at the 20:00 IST US open (my bars), then $98.29 at the settle. About 75% of the $3.67 came *before* the US crash, so "rose while US stocks fell" describes only the last ~$0.6.
  - MAC calls it "the first sign… that oil is back to trading the Gulf" and puts ~40% on non-crisis drivers. KIN: "part ship war, part retracement… attributed by Reuters, not proven."
  - "The rest was short-covering" is the desk's estimate, not an outlet's. Reuters itself names the Russian refinery strikes.
- **Current text (heading):** `### Wall Street had its worst day since April 2025 on AI, not Iran. Oil went the other way, on the war.`
- **Replacement:** `### Wall Street had its worst day since April 2025 on AI, not Iran. Oil went the other way, mainly on the ship war (Reuters).`
- **Current text:** `The rest was short-covering after a 16.6% three-day fall, and Ukrainian strikes on Russian refineries.`
- **Replacement:** `Reuters also cites Ukrainian strikes on Russian refineries; on our estimate about 40% of the rise was those and short-covering after a 16.6% three-day fall.`
- **Current text:** `**What it means.** Oil rose while US stocks fell 4.4%, so it is trading the Gulf again rather than risk appetite. The VIX spike is not a war signal (see III).`
- **Replacement:** `**What it means.** Oil held its gain while US stocks fell 4.4%, so on Thursday it was not trading risk appetite; most of the rise came before the US open. The VIX spike is not a war signal (see III).`

### L3: "After Thursday's oil settle" is an inference from a posting time
- **Evidence:** DIP: "the exact remark time is not pinned". KIN: "Not placed: the minute of Trump's Oval Office remarks." The basis is ToI's 16:54 ET post and Axios's "late Thursday". The settle is at 14:30 ET. My bars show no jump at the settle; Brent rose to $100 in Asia afterwards. The inference is probably right, but it should say what it rests on.
- **Current text:** `This came after his first Iran meeting with his security team since the midterms, and after Thursday's oil settle.`
- **Replacement:** `This came after his first Iran meeting with his security team since the midterms and, on the timestamps found (the Times of Israel posted it at 16:54 ET), after Thursday's 14:30 ET oil settle.`

### L4: Iraq's airspace: wrong tense and wrong verb
- **Evidence:** KIN-B2: the reported restriction covers 7–11 Nov, which have not started. It limits overflights to designated corridors; it does not close the airspace. It rests on one OSINT origin (Faytuks), with no NOTAM number.
- **Current text:** `A social-media report says Iraq has closed its airspace each morning on 7–11 Nov; no official notice was found.`
- **Replacement:** `OSINT accounts (one origin) report that Iraq will restrict its airspace to designated corridors 05:00–11:00 UTC daily on 7–11 Nov for "active military operations"; no NOTAM or official notice was found.`

### L5: Massie is not a Democrat; Schumer's line is Punchbowl's framing
- **Evidence:** DIP-A5:
  - Punchbowl: "many Democratic senators will likely want concessions".
  - Massie "told CNN he will trigger the Hegseth impeachment vote", and "Multiple GOP sources" expect it to pass.
  - Massie (R-KY) is a Republican. That is my knowledge, not in the dossier.
- **Current text:** `**Congress.** Democrats named levers but held no vote: Khanna proposes barring funding for combat in Iran, Schumer wants Iran concessions before extending funding, and Massie will force a vote to impeach Hegseth in the week of 9 November.`
- **Replacement:** `**Congress.** Levers were named but no vote held: Democrat Khanna proposes barring funding for combat in Iran; Schumer says many Democratic senators will want Iran concessions before extending funding (Punchbowl); and Republican Massie says he will force a vote to impeach Hegseth in the week of 9 November.`

### L6: "No Iranian fire at any state", the wording two desks warned against (repeat of 5-Nov H2)
- **Evidence:** KIN-B1: "Write 'no Iranian salvo at any state', not 'no Iranian fire'." ISR cross-desk: "word 'no Iranian fire at any state' carefully." The very next sentence reports Turkey's soldier killed by fire "assessed to have come from Iran". "What held" already uses "salvo".
- **Current text:** `**Fire.** There was no Iranian fire at any state (~57 days).`
- **Replacement:** `**Fire.** There was no Iranian missile or drone salvo at any state (~57 days).`

### L7: The Khamenei letter's delivery is stated as fact (CLAIMED, Iranian account only)
- **Evidence:** DIP-B1: "CLAIMED (Iranian account only): the letter's delivery and Putin's words". The Kremlin confirmed the meeting and detailed nothing else.
- **Current text:** `He delivered a letter from Mojtaba Khamenei to Putin; its contents were not disclosed.`
- **Replacement:** `Iranian state media say he delivered a letter from Mojtaba Khamenei to Putin (the Kremlin confirmed the meeting, not the letter); its contents were not disclosed.`

### L8: "Brent fell ~$2.4 in that hour": it took two hours, and Europe opened in the same hour
- **Evidence:**
  - **My bars:** the Qatari statement came ~08:00–08:05 UTC (13:30–13:35 IST). January Brent was $99.03 at the 13:30 IST open and its low within the hour was $97.27 (−$1.76). The $96.65 low came in the 15:15 IST bar, ~2 hours later.
  - **Same window:** Europe's cash open was 08:00 UTC, with the STOXX −1.6% at 08:10 GMT on the AI rout (ISR).
  - **Attribution:** Bloomberg does attribute it: oil "erased an earlier advance as traders weighed reports of US engagement in efforts to step up Middle East negotiations". MAC: "No outlet tied it to a specific event."
- **Current text:** `the emir urged no further escalation; Brent fell ~$2.4 in that hour.`
- **Replacement:** `the emir urged no further escalation. Brent fell ~$2.4 over the next two hours; Bloomberg says traders "weighed reports of US engagement" in negotiations, though Europe's open and the AI sell-off came in the same window.`

### L9: Ship war: "fatal" is not settled, and the place name is shortened
- **Evidence:** Lloyd's List (fetched): "has lost their life". IMO (Splash247): "one seafarer missing". The brief's own body says "killed… or is missing". UKMTO's place reference is "50 nm north of Madinat ash Shamal, Qatar".
- **Current text (heading):** `### The ship war: a fatal, verified hit north of Qatar, and a growing pile of unverified claims.`
- **Replacement:** `### The ship war: a verified hit north of Qatar with one seafarer killed or missing, and a growing pile of unverified claims.`
- **Current text:** `was hit by "two unidentified projectiles" 50 nautical miles north of Qatar.`
- **Replacement:** `was hit by "two unidentified projectiles" about 50 nautical miles north of Madinat ash Shamal, Qatar.`

### L10: "No US notice exists" is an absence we searched for, not a fact we can prove
- **Current text:** `called it a move "from aid to partnership"; no US notice exists.`
- **Replacement:** `called it a move "from aid to partnership"; no State, OMB or Pentagon notice was found.`

### L11: Aramco levels: the brief presents the weaker number as equal; "chasing volume" is the trigger's own definition
- **Evidence:**
  - Newsquawk (fetched) says "cuts… by USD 2/bbl to a USD 6.50/bbl discount… the lowest since May 2020". November was −$5.00 (The National; investingLive: a $3 cut, the widest since 2020), so a $2 cut gives −$7.00.
  - Argaam reproduces Aramco's grade table: Light −7.00; Extra Light −6.50. SAU-A6: "−$7.00 is the better-supported number."
  - "Lowest since May 2020" holds at either level, because May 2020 was −$7.30. That is my memory, not re-found.
- **Current text:** `Aramco cut its December Arab Light price for Asia by **$2**. Argaam has it at $7.00 below Oman/Dubai; Newsquawk has $6.50, "the lowest since May 2020". That is a seller chasing volume, not a scarcity signal, and it fires a graph trigger.`
- **Replacement:** `Aramco cut its December Arab Light price for Asia by **$2**, to $7.00 below Oman/Dubai on Argaam's copy of Aramco's table (a $2 cut from November's −$5.00). Newsquawk has $6.50 below, "the lowest since May 2020"; its figure matches Argaam's Extra Light line. On the graph trigger's own definition that is a seller chasing volume, not a scarcity signal, and it fires.`

### L12: Interception places are not as the coalition gave them
- **Evidence:** SAU-A2: "towards the Madinah region"; "towards Najran" (not "Najran region"); a drone "in the Makkah region"; a drone "in the Eastern Province".
- **Current text:** `The coalition announced interceptions again, toward the Madinah, Najran and Makkah regions and the Eastern Province (claims).`
- **Replacement:** `The coalition announced interceptions again: missiles "towards the Madinah region" and "towards Najran", and drones over the Makkah region and the Eastern Province (coalition claims).`

### L13: The "two engines" split hides Thursday's AI rotation, which the graph's own edge raise relies on
- **Evidence:**
  - IND-B1: "The divergence from Korea on Thursday was the chip story (KOSPI −5.3%)."
  - Foreigners sold ₩3.42trn of Korean shares on Thursday, the same day they bought ~$1.6bn of Indian shares.
  - The `kospi → nifty-50` raise (5→6) is justified on exactly those Thursday flows.
- **Current text:** `- **Thursday:** this came before the US crash. It traded Wednesday night's oil fall.`
- **Replacement:** `- **Thursday:** this came before the US crash, in India's first session after Wednesday night's oil fall (PTI's reason). Korea's AI sell-off had already begun: KOSPI −5.3%, foreigners −₩3.42 trillion that day.`

### L14: Nomura is scored "Met" before its test window closes
- **Evidence:** the 5-Nov test: "a close above 24,000 today that holds through month-end."
- **Current text:** `| Nomura: Nifty past 24,000 | **Met** (25,030.35). |`
- **Replacement:** `| Nomura: Nifty past 24,000, holding through month-end | **On track:** above 24,000 on both closes (25,030.35); the month-end leg is pending. |`

### L15: CIBC's row hides the intraday touch
- **Evidence:** the 5-Nov test says "January Brent back above $100 by 11 November" and does not say settle. It traded $100.92 on Friday. The Barker row mentions the touch; the CIBC row does not.
- **Current text:** `| CIBC (Babin): January above $100 by 11 Nov | **Pending:** $1.71 short on the settle. |`
- **Replacement:** `| CIBC (Babin): January above $100 by 11 Nov | **Pending on settles:** $1.71 short; it traded $100.92 intraday on Friday, which we do not count. |`

### L16: The `kospi → nifty-50` reason says "second week"; it is the second episode in one week
- **Evidence:** the changelog says "second episode in a week" (3 Nov, then 5–6 Nov). The `nifty-50` regime is "CAPITAL SUBSTITUTION RUNNING INDIA-POSITIVE (3 Nov)".
- **Current text:** `` - `kospi → nifty-50`, the substitution channel, raised from 5 to 6: the second week Korea's losses have been India's gains. ``
- **Replacement:** `` - `kospi → nifty-50`, the substitution channel, raised from 5 to 6: the second time this week (3 Nov, then 5–6 Nov) Korea's losses coincided with India's gains. Opposite same-day flows are confirmed; common funds are not traced. ``

### L17: OMCs' "Why" contradicts the India desk's margin arithmetic
- **Evidence:**
  - IND-A6: "A ~₹10–12/l diesel gap remained at ~$94 Brent. At ~$98 it is wider by ~₹2/l." Crude is not below the OMCs' diesel breakeven.
  - The outlet attribution is BS's headline: "OMCs… rally up to 7% as crude cools below $95".
- **Current text:** `| IOC / BPCL / HPCL | +3–6% in two days | Crude below their breakeven since Wednesday | ~90% |`
- **Replacement:** `| IOC / BPCL / HPCL | +3–6% in two days | Crude cooled below $95 on Wednesday night (BS); a diesel under-recovery of ~₹10–12/l remains (desk arithmetic) | ~90% |`

---

## Graph corrections (list only; not applied)

- **G1 (HIGH) — `inr-usd` › trigger "TWO consecutive PTI closes stronger than 94.50…" › `note_2026-11-06`.**
  - **Replace:** `LOG THE CAUSE: flows, not oil — Friday's gain came with January Brent ABOVE Wednesday's settle (~$98 vs $94.62); HDFC Securities' Parmar: 'a flow-driven strength'.`
  - **With:** `LOG THE CAUSE: mainly flows (FII ₹14,975 cr Thu; Parmar: 'a flow-driven strength'), with softer crude a named secondary factor (Parmar 'softer crude oil, easing yields'; Reuters 'post-midterm oil fall'; PTI). At India's 15:30 IST rupee closes January Brent was ~$102.3 (Wed), ~$96.0 (Thu), ~$97 (Fri): Thu→Fri Brent ~+$1 while the rupee gained 52 paise, but Friday's intraday rally tracked a ~$4 Brent slide. Wednesday's $94.62 settle came after Wednesday's rupee close and is the wrong comparator.`
  - **Add:** `Confirm Friday's PTI final (~20:45 IST).`
  - **Status:** stays FIRED.
- **G2 (HIGH) — `inr-usd` › `recent_signals[2026-11-06]`, the new watch's `notes`, and `current`.**
  - **Signal:**
    - `THE CAP IS GONE — ON FLOWS, NOT OIL (5–6 Nov)` → `THE CAP IS GONE — MAINLY ON FLOWS (5–6 Nov)`.
    - `Friday's gain came with January Brent above Wednesday's settle.` → `Between Thursday's and Friday's rupee closes Brent was ~$1 higher; Friday's intraday rally tracked a ~$4 Brent slide.`
  - **Watch "PTI close weaker than 95.00" `notes`:** `Friday's +52 paise came on flows with Brent above Wednesday's settle.` → `Friday's +52 paise came mainly on flows (see the fired two-close note).`
  - **`current`** is stale (price "94.46 PTI final (4 Nov)…"; driver "capped at 94.50 by dollar bids (RBI/SBI refill read)"):
    - price → `PTI 94.41 (5 Nov final), 93.89 (6 Nov provisional); Reuters 93.9050, strongest since 22 Apr`;
    - driver → `FII inflows (largest day in nearly six years) and AI-trade rotation; softer crude secondary; no RBI action named`;
    - regime → `94.50 cap broken on two PTI closes`.
- **G3 (HIGH) — "record" FII wording in five places → "the largest single-day FII buy in nearly six years (Reuters)".**
  - `india` › `recent_signals[2026-11-06]`: `record FII day`.
  - `nifty-50` › `recent_signals[2026-11-06]`: `record FII buying`.
  - `fii-flows` › new watch "FIIs turn net SELLERS… 3 consecutive sessions" › `notes`: `The 5-Nov record day`.
  - `edges.json` `fii-flows → inr-usd` › `context_2026-11-06`: `record FII buying`.
  - `edges.json` `us-10y-yield → fii-flows` › `context_2026-11-06`: `as FII buying hit a ~6-year record`.
- **G4 (LOW) — `edges.json` `brent-crude → inr-usd` › `context_2026-11-06`.**
  - **Replace:** `the rupee strengthened (PTI 94.41 → 93.89) while January Brent ROSE ($94.62 → $98.29) — flows overrode oil for two sessions. The asymmetry (spikes pass through in full, falls barely do) is not tested by this; it is tested only by a spike.`
  - **With:** `at India's rupee closes January Brent went ~$102.3 (Wed) → ~$96.0 (Thu) → ~$97 (Fri) while the rupee went 94.46 → 94.41 → 93.89: a ~$6 oil fall moved the rupee 5 paise (consistent with the asymmetry); Friday's 52-paise gain came on flows with Brent ~$1 higher. Only a spike is a clean test.`
  - **Weight:** hold at 10.0.
- **G5 (LOW) — `qatar` › `recent_signals[2026-11-06]`.**
  - **Replace:** `Brent fell from $99.03 to $96.65 in the hour of the readout (Bloomberg: 'reports of US engagement').`
  - **With:** `Brent fell from $99.03 (08:00 UTC) to $96.65 (~09:45 UTC) after the readout (Bloomberg: 'reports of US engagement'); Europe's open and the AI sell-off fell in the same window.`
- **G6 (LOW) — `brent-crude` › `recent_signals[2026-11-06]`.**
  - **Replace:** `$96.65 low (~15:00 IST, as Qatar read out the Trump–Tamim call)`
  - **With:** `$96.65 low (~15:15–15:30 IST), after the Qatari readout of the Trump–Tamim call (~13:30 IST)`
- **G7 (LOW) — stale `current` fields; the changelog says "price snapshots" were updated, but these still show old values.**
  - `india.current.status`: "Day 251… Nifty ~24,370…; rupee 95.22 (PTI, 26 Oct)" → Day 252: Nifty 25,030.35 (highest close since 27 Feb); rupee 93.89 PTI provisional; FII five-session streak fired; 10Y 7.17% (Thu); pumps frozen; government silent.
  - `nifty-50.current.price`: "23,960.60 (4 Nov close)" → `25,030.35 (6 Nov close); 24,536.60 (5 Nov)`.
  - `kospi.current.price`: "5,730.74 (30 Oct)" → `5,059.69 (6 Nov; intraday 4,911.28)`.
  - `vix.current.price`: "19.42 (30 Oct)" → `28.18 (5 Nov close; ~26.9 Fri); non-kinetic (AI crash)`.
  - `strait-of-hormuz.current.status`: "Day 250: VLCC Grit…" → Day 252: UKMTO 196-26 (*Velos Sapphire*, 4 Nov, north of Madinat ash Shamal; one seafarer killed or missing); ~17 Iranian mine/fire claims since 1 Nov, none verified.
  - `iran.current.status`: "Day 251…" → Day 252: Rezaei in Moscow, seven conditions on the record; proposal via Qatar reported (anonymous), unacknowledged; no salvo at a state ~57 days.
  - `saudi-arabia.current.status`: dated 31 Oct → add 5–6 Nov interceptions (Madinah region, Najran, Makkah region, Eastern Province; claims) and the OSP fire.
- **G8 (LOW) — `united-states` › `current.status` and `recent_signals[2026-11-06]`.**
  - `current.status`: `9-Nov new moon flagged by officials (Fox)` → `9-Nov new moon noted by unnamed officials (Fox)`.
  - Signal: `Schumer wants Iran concessions before extending funding; Massie forces a Hegseth impeachment vote week of 9 Nov` → `Schumer: many Democratic senators will want Iran concessions before extending funding (Punchbowl); Republican Massie says he will force a Hegseth impeachment vote the week of 9 Nov`.
  - The same wording sits in the `united-states` summary ("Democrats have named levers (a funding condition, a Hegseth impeachment vote)"). Change it to "members of Congress have named levers".
- **G9 (LOW) — `iran` and `mojtaba-khamenei` › `recent_signals[2026-11-06]`.**
  - `Rezaei delivered a letter from Mojtaba Khamenei to Putin` → `Iranian media say Rezaei delivered a letter from Mojtaba Khamenei to Putin (Kremlin confirms the meeting only)`.
  - On `mojtaba-khamenei` the tag is `[CONFIRMED]`. Change it to CLAIMED for the delivery, CONFIRMED for the meeting.
- **G10 (LOW; HIGH under the completeness rule) — `bahrain`, `kuwait`: listed as "Nodes affected" (SAU-A8, KIN-A3) and not updated today.**
  - **Add a 6-Nov signal:** `Kuwait and Bahrain condemned the 5-Nov missile 'towards the Madinah region'; Bahrain urged the UNSC to take 'deterrent' measures (res. 2216). Neither was named in Iran's 5–6 Nov threats; no base-use statement. (RHETORIC; intel SAU-A8, KIN-A3)`
  - I rate it LOW because the only new facts are condemnations, with no trigger or edge on either node.

---

## Trigger Point Review

| Trigger | Changelog | My assessment | Agree? |
|---|---|---|---|
| `us-10y-yield` "closes below 5.00% for 3 consecutive sessions… WITH HY OAS not widening" | FIRED | Its 3-Nov and 5-Nov notes set a fresh three-close run with OAS ≤3.44% (30-Oct base). Treasury CSV: 4.91 / 4.95 / 4.90 (2–4 Nov). FRED OAS: 3.43 / 3.40 / **3.32**. Both met on published data. A sixth close came at 4.84 on 5 Nov; 5-Nov OAS was still unpublished at 17:23 IST. | ✅ AGREE |
| `fii-flows` "FII flow turn POSITIVE for 5 consecutive sessions" | FIRED | Exchange provisional: +3,598.54 / +3,114.68 / +6,836.81 / +7,284.03 / +14,974.68 (30 Oct–5 Nov) = +35,808.74 (my sum matches). 29 Oct was −944, so the run starts 30 Oct. PTI quotes "according to exchange data". The CAVEAT note on premise is appropriate. | ✅ AGREE |
| `inr-usd` "TWO consecutive PTI closes stronger than 94.50 by 20 Nov" | FIRED | 94.41 (PTI final, Thu) and 93.89 (PTI provisional, Fri; 61 paise inside). Reuters 94.4750 / 93.9050 on the same side. Both post-date the trigger's creation (5 Nov, ~11:50 IST). The fire stands; confirm PTI's final tonight. | ✅ AGREE on status; ❌ **DISAGREE on the logged cause** ("flows, not oil"): see H2/G1 |
| `saudi-arabia` "December Asia OSP cut again (below −$5.00) … OR raised" | FIRED | Re-found Newsquawk: a $2 cut to −$6.50. The SAU desk has Argaam's Aramco table at −$7.00. Either is below −$5.00. The cut is a pricing *action*, from Aramco's sheet via two independent outlets. | ✅ AGREE (prefer −$7.00 in the note; L11) |
| `vix` ">25 = kinetic-event marker" | AMENDED, not fired | VIX 28.18 came with SOX −12.25% (3rd-largest 1-day % jump in 10 years and highest close since 30 Mar, both verified). No strike order, launch or Israeli strike in the window (four desks). The original *premise* was always the kinetic marker; the amendment aligns letter to premise, keeps `condition_original` and logs the breach as a false positive. Not a reinterpretation to dodge a fire, because a fire would itself have been the false war signal. Nit: the brief's "coincident strike or launch" drops "strike order". | ✅ AGREE |
| `united-states` "strikes RESUME 4–30 Nov" | not fired, 0/4 | No strike reported nights 1–3 (KIN English and Persian). Trump's words, Reuters' sources and Fox's moon are rhetoric or preparation. | ✅ AGREE |
| `qatar` "written answer acknowledged on the record…" | not fired | Anonymous Iranian official only; the Amiri Diwan gives no terms. | ✅ AGREE |
| `brent-crude` "settles back ABOVE $100" | not fired | $98.29 settle; $100.92 intraday doesn't count (needs a settle). | ✅ AGREE |
| `kospi` "closes below 5,000" | not fired | Close 5,059.69; intraday 4,911.28 (verified). The trigger says "closes". | ✅ AGREE |
| `houthis` holy-city | tested, not fired | Province-level wording per the 31-Oct rule. | ✅ AGREE |
| New: HY OAS >3.75% with 10Y <5%; FIIs net sellers ×3; PTI weaker than 95.00; Saudi–Houthi talks on record | watching (new) | All dated, falsifiable and not duplicates. Fix the "record day" wording in the FII watch (G3) and the cause wording in the rupee watch (G2). | ✅ |

**Edges:**
- `kospi → nifty-50` 5→6: modest rise on confirmed opposite same-day flows; OK (fix the reason, L16).
- `semiconductors → vix` 5→6: a second chip-driven non-war VIX spike; OK.
- `vance → brent-crude` held at 5 provisional: OK.
- **No edge moved on rhetoric.**

**Deployment section vs 4- and 5-Nov definitions:**
- Conditions 1–3 statuses: correct. Condition 1 un-met at $98.29 (met once on 4 Nov). Condition 2 met. Condition 3 buying leg met; CPI 12 Nov.
- Hold rule (4-Nov text: "until the window is a week old with no qualifying strike, foreign buying reaches five sessions and front-month Brent settles below $100"): two of three legs met; correct.
- The recommendation repeats the 5-Nov "hold to 11 November, then stage in one-third if all three legs are met" **as written**. No rule is reinterpreted.
- Only the "officials flag" wording (H4) and "largest in six years" (H1) need fixing.

---

## Market Data Spot-Check (my re-pull vs the brief)

| Data point | Brief | Verified | Match |
|---|---|---|---|
| Brent Jan settle 4 → 5 Nov | $94.62 → $98.29 (+3.9%) | 94.62 → 98.29 (+3.88%) | ✅ |
| "~40% of Wednesday's fall" | ~40% | 3.67 / 8.98 = 40.9% | ✅ |
| Feb / Jun / Dec-27; Jan–Dec27 spread | as printed | same; 15.50 → 19.02 → ~19.8 | ✅ |
| "16.6% three-day fall"; week like-for-like −13.4% | yes | 113.43 → 94.62 = −16.6%; 113.43 → 98.22 = −13.4% | ✅ |
| Fri high $100.92; ~$98.2 at 16:37 | yes | 15-min high 100.92 (09:00 IST bar); 98.17–98.51 at 16:15–16:30 | ✅ |
| WTI / HO / RBOB / HH Dec | as printed | same; crack 4.352×42 − 98.29 = 84.49 | ✅ |
| Gold / silver Dec | $4,113.5 / $52.38 | same | ✅ |
| S&P −4.36%, worst since 4 Apr 2025 | yes | −4.356%; only 3–4 Apr 2025 worse since 2025 | ✅ |
| SOX −12.25%, worst since Mar 2020 | yes | −12.246%; worse only 16 Mar 2020 (−15.9%); also the 2nd-largest since 1994 (Reuters "second-biggest on record" checks) | ✅ |
| VIX 16.61 → 28.18 | yes | same; 3rd-largest % jump in 10y; highest close since 30 Mar | ✅ |
| KOSPI / Nikkei / TAIEX (Fri) | −6.0% / −5.96% / −4.5% | −6.02 / −5.96 / −4.51%; KOSPI low 4,911.28 | ✅ |
| Nikkei, TAIEX >20% below peak | yes | −20.63% (25 Jun close peak) / −20.31% (6 Oct) | ✅ |
| Nifty 25,030.35, highest close since 27 Feb | yes | no close ≥25,030.35 after 27 Feb (25,178.65); best after was 24,865.70 (2 Mar) | ✅ |
| Within 0.6% of 27-Feb close | yes | −0.589% | ✅ |
| Best week since Feb 2021 (+8.6%) | yes | +8.58%; only week bigger since mid-2020: 5 Feb 2021 (+9.46%) | ✅ |
| Brent ~$72 / rupee ~91 on 27 Feb | yes | BZ=F 72.48; INR=X 91.007 | ✅ |
| India VIX 17.47 | yes | 17.465; highest close since at least Aug | ✅ |
| USD/INR PTI 94.41 / 93.89 | yes | yfinance 94.515 / 93.90 (cross-check only); PTI not re-found on web | ⚠ desk-sourced |
| FII +₹14,974.68 cr | yes | not re-found on web; five-session sum re-added | ⚠ desk-sourced |
| RBI reserves $717.06bn (−$2.69bn; FCA −$2.09bn) | yes | RBI release (fetched): 717,056 / −2,691; FCA 591,118 / −2,088 | ✅ |
| US 10Y / 2Y (5 Nov) | 4.84% / 4.46% | Treasury CSV 4.84 / 4.46 | ✅ |
| 10Y breakeven; HY OAS | 2.24%; 3.32% (4 Nov) | FRED 2.24; 3.32; 5-Nov unpublished | ✅ |
| Fed Dec hike odds | ~79 / ~82 / ~65% | ZQZ26 95.980 / 95.975 / 96.005 → 78.9 / 81.7 / 64.8%; Fri 96.000 → 67.6% | ✅ |
| XLE / FRO / LMT | −3.0 / −7.8 / −3.2% | −2.98 / −7.80 / −3.17% | ✅ |
| IOC / BPCL / HPCL two days | +3–6% | +2.97 / +4.99 / +5.68% | ✅ |
| MRPL / CPCL Thu | −7.2 / −9.5% | −7.16 / −9.47% | ✅ |
| STOXX / DAX; DXY | as printed | same | ✅ |
| Rupee "strongest since 22 April" (Reuters) | yes | INR=X has 93.80 on 23 Apr and a bad tick on 26 Aug (93.546 open = close, then 95.43) | ✅ as Reuters' claim |
| Footer: 60 of 63 touched; 415 edges | yes | 60 nodes `last_updated` 6 Nov; untouched: bahrain, kuwait, uae-barakah; edges 415 | ✅ |

---

## Checked and passed (with why)

- **Corrections block (all four correct).**
  - UKMTO 196-26 was posted 08:19 UTC 5 Nov, after the 5-Nov sweep (KIN).
  - India 10Y: the 5-Nov "~7.06%" was Investing.com's intraday low (7.053%). The close was 7.171%, −2bp from ~7.19% (IND-A4).
  - Herzog Sunday 8 Nov and UTJ all-seven-no-one (ISR-A1). The 5-Nov brief had "11 Nov" and "two undecided".
  - Wadephul on 3–4 Nov (ISR-A6), properly tagged "one relay".
- **Wall Street lead.** The NBC and Reuters causes are attributed; the war share is "none found" with the specific absences listed. Numbers verified.
- **Oil cause.** Reuters' list matches SAU-A1, KIN and MAC (tanker attacks; "at least five" since Sunday; Iran's terms; Citi). Only the "what it means" and "the rest" lines overreach (L2).
- **Trump quotes.** Consistent across five outlets in DIP-A1. Newsquawk (fetched) independently paraphrases "would rather not destroy the rest of Iran if possible, but maybe will have to" and "not doing anything without US approval".
- **Reuters' "planning to bomb" source quote.** Tagged "reported", two sources, quoted as in DIP-A1.
- **Fox's moon note in the body** ("Fox's officials note that 9 November is a new moon") matches Fox's wording. Only the headline and Section III over-read it (H4).
- **Night three.** A searched absence (English and Persian), tagged.
- **Iran proposal.** Reuters (one anonymous Iranian official) and NYT are both tagged. "Acknowledgement: none" is correct (DIP-A3; Newsquawk relays the same Reuters line).
- **Rezaei quote and title (SNSC secretary).** CONFIRMED (state TV via Reuters and Al Jazeera). Tasnim calls him "SNSC Chief".
- **Ghalibaf.** His X post, CONFIRMED.
- **Araghchi's nine calls; Oman's "ending the state of war".** CONFIRMED (DIP-B2).
- **Turkey border death.** Correctly framed as a border incident with the MoD's "assessed" wording.
- **UKMTO 196-26 and *Velos Sapphire*.** Re-found: Lloyd's List (fetched), Splash247 (IMO: missing), Maritime Executive, gCaptain, OSINT613. Time, distance and "two unidentified projectiles" match KIN. No claim of responsibility.
- **Claims tally.** 2+1+3+4+5+2 = 17 since 1 Nov; seven tankers and a tug in the window; none matched to UKMTO.
- **Israel.** 67–46 plus UTJ 7 = 120 (ISR-A1 arithmetic). Liberman's three lines are quoted from INN. The "needs Shas" arithmetic is the desk's (48 + 7 + 6). The PMO's "from aid to partnership" is CONFIRMED.
- **Saudi.**
  - The WSJ report is REPORTED.
  - Krimly's "pure fabrication by the writers or their alleged sources" was aimed at the demands; Asharq notes the denial covers the demands. "Did not deny the approach" is properly hedged "in the relays found".
  - The Turkish ratification (279–119) is consistent across four outlets.
- **Europe.**
  - BoE: +25bp to 4%, 8–1 (Mann 50bp), with energy and the Middle East conflict cited. Verified on the BoE's Monetary Policy Summary.
  - Ante Zigman is a real ECB council member (Croatia).
  - TTF −15% on the week from >€101.8; storage 73.42% (AGSI via tracker; REPORTED).
- **What held.** Each line matches a desk absence (KIN-A3, KIN-A10, SAU-A4, ISR-A5, ISR-A6, DIP-B1).
- **Section II.**
  - McNally's 80% and ING's quote are exact (MAC; DIP).
  - The Kotak/Banerjee quote and test are exact (IND).
  - Scorecard verdicts for Eurasia, Vaez/Barker, Parsi/Cancian, rupee dealers and ING/Lombard match the data.
  - Optional: add "(our horizon)" to McNally's 30-Nov test; he gave no date.
- **Source tone.**
  - Tasnim's "'Tell This to Your Boss'"; The National's "energy mix" editorial without "war"; Bowen's "blot out the electoral rout"; Reuters' India wrap without Iran. All in the dossier.
- **Section III Cascade Watch counts** (130 reviewed; 4 fired; 1 amended; 4 new; open 130) match the changelog.
- **Risk Landscape.** Fed odds are "our calculation" and the arithmetic checks. Goldman $4,150 from $4,650 is consistent with the earlier, re-found $4,900 → $4,650 cut.
- **Dated tells.**
  - ICE Brent settle 19:30 London = 01:00 IST (GMT since 25 Oct).
  - January Brent expires on the last business day of November (30 Nov).
  - FOMC 8–9 Dec.
- **Page 2 data notes.** Session conventions are correct. The Reuters "steepest since COVID" caveat is correct (it compares January with the expired December contract at $117.64).

## Not independently re-found (desk-sourced; the search index lags 1–2 days)
- FII **₹14,974.68 cr** and Reuters' "largest single-day net purchase in nearly six years".
- PTI rupee **94.41 / 93.89** and Reuters 93.9050 "highest since 22 April". yfinance agrees on direction and side of 94.50.
- Trump's exact Oval Office words, and the *minute* he said them (only a Newsquawk paraphrase found).
- Reuters' "**He is planning to bomb Iran. Don't listen to what he's saying.**"
- Fox's "Nov. 9 marks a new moon…" text.
  - The TASS distortion is the desk's report.
  - The astronomical new moon of ~9 Nov is from my mean-lunation reasoning.
- Herzog's **67–46** final count and the **Sunday** date. Web results show only the earlier 60–46 count. "11 Nov is the legal deadline" is also unverified.
- Bailey's quote. It is not in the BoE Monetary Policy Summary; it is presumably from his statement or press conference (CNBC per ISR).
- Goldman's **$4,150** cut itself. Only the prior $4,650 cut was found.
- **Argaam's −$7.00** table. Only Newsquawk's −$6.50 re-found. May 2020's −$7.30 is from memory.
- Massie's party (R-KY), from memory.
- The Trump–Tamim call **date** (Friday vs Thursday night US time); the Amiri Diwan text was not fetched.
- NSE holiday on 10 Nov (Balipratipada), Nvidia on 17 Nov, OPEC+ on 29 Nov: carried from the 5-Nov calendar and not re-checked.
- India 10Y Friday close (trackers disagree: 7.138% vs 7.19%). The brief correctly prints "unconfirmed".

## Final Verdict
**APPROVED WITH CORRECTIONS.**
- **Numbers:** clean. Every level and every "worst/highest/best since" claim verified.
- **Triggers:** all four fires meet their own thresholds on published data. The `vix` amendment is justified. Nothing moved on rhetoric.
- **Before publish:** apply H1–H6. They are the CoS's own overreach: a false "record"; "flows, not oil" on a misaligned comparator with a clipped quote; a Signal that claims more than the desks could trace; unnamed officials' moon note promoted to "officials point at 9 November"; a conditional threat quoted as unconditional; and a test pinned on the wrong analyst.
- **Graph:** G1–G3 should go in with the brief, so the rupee's logged cause and the "record" wording don't carry forward.
- **Header:** re-stamp it from `date` at publication (L1).


---

## Applied at publish (Chief of Station, 17:39 IST)
- **Brief:** H1–H6 and L1–L17 applied verbatim. The L1 header was re-stamped from `date` (17:38 IST). One extra instance of "record FII buying" in Page 2 (Nifty "Why" cell) was also corrected under H1.
- **Graph:** G1–G10 applied (`staging/2026-11-06-morning/gu_part_post2.py`, log `update_log_post2.json`). G10 added 6-Nov signals to `bahrain` and `kuwait`, so 62 of 63 nodes are now touched.
- **Re-found after the check:** Thursday's FII figure on QuantsApp (exchange data): +₹14,975 cr; gross ₹31,798 / ₹16,823 cr; DII −₹10,445 cr.
- **Still pending at publish:** Friday's FII figure (not out at ~17:40 IST); PTI's final Friday rupee close (~20:45 IST); FRED's 5-Nov HY OAS; US payrolls (19:00 IST); tonight's Brent settle.
