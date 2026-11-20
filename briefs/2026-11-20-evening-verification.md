# Verification Report — 20 November 2026 (Evening, Full Edition, Day 266)
Generated: 21:28 IST Fri 20 Nov (`date`-checked) | Fact-Checker: Red Team
Brief checked: `briefs/2026-11-20-evening.md` (generated 21:17 IST). Read-only; nothing written outside this file and `verifier_scratch/`.

## Summary
I checked about 95 claims: all of Section I, Page 2, the Section II scorecard and the Section III deployment block. I re-pulled the market data independently: yfinance daily data for explicit contracts; 1-minute bars for 13:45–14:15 IST and 20:30–20:45 IST on Friday; 5-minute bars for the Thursday US session and the Friday Brent slide; FRED (HY OAS, Brent spot, DGS10); the Treasury par CSV. Three web sub-checks were run, one each on the US/Israel, Gulf/shipping and markets/India claims. I also diffed the graph against `backups/2026-11-20/graph_v1`.

**Flags: 0 CRITICAL, 6 HIGH, 11 LOW. Graph corrections: 5 (G1–G5).**

The graph diff confirms what the changelog says:
- exactly two status changes (`strait-of-hormuz` blacklist → fired; `china` → expired) and one new watch;
- all 134 triggers open at the start now carry a `note_2026-11-20`;
- the 138 review rows match;
- the five edge changes are exactly the five listed;
- `gu_corrections.py` did not double-apply anything (one `top_edges` entry each for `gold → rbi` and `semiconductors → fii-flows`; each summary replacement appears once).

The Trump "first" claim in the graph is not supportable (G1). The most consequential error is calendar arithmetic: **Tue 24 Nov is an NSE holiday** (H1).

---

## Flags

### HIGH

**H1 — The `inr-usd` and `fii-flows` dates ignore Tuesday's market holiday (Guru Nanak Jayanti, Tue 24 Nov)**
- **Brief text:**
  - Cascade Watch: "**`inr-usd`** below 93 for three sessions (one of three; earliest Tue 24 Nov)".
  - Dated tells: "**Tue 24 Nov:** the earliest `inr-usd` can fire".
  - Signal: "the `fii-flows` watch cannot fire before 25 November".
- **Problem:** our own graph records "NSE shut Tue 10 Nov (Balipratipada) and Tue 24 Nov (Guru Nanak Jayanti) (CONFIRMED)" (`graph/nodes/india.json`). The 8-Nov and 10-Nov dossiers say the same, citing BT and Zerodha, and say the closure includes currency derivatives. The sessions therefore run:
  - for `inr-usd`: Fri 20 (1), Mon 23 (2), **Wed 25 (3)**;
  - for `fii-flows` (three selling sessions): Mon 23, Wed 25, **Thu 26**.
- **Evidence:** `graph/nodes/india.json`; `staging/2026-11-08-morning/intel.md`; `staging/2026-11-10-morning/intel.md`. I did not re-check the FEDAI interbank calendar, but the NSE currency segment is shut and Guru Nanak Jayanti is normally a Mumbai bank holiday.
- **Replacement text:**
  - Cascade Watch: "…(one of three; earliest **Wed 25 Nov** — Tue 24 Nov is a market holiday)".
  - Dated tells: "**Mon 23 Nov:** the earliest leg (b) can complete. **Tue 24 Nov:** Indian markets shut (Guru Nanak Jayanti); ~24 Nov Fesharaki. **Wed 25 Nov:** the earliest `inr-usd` can fire."
  - Signal: "the `fii-flows` watch cannot fire before **26 November**."

**H2 — Updates box: the explanation of Sonowal's "entire crew… safe" line is inference written as fact**
- **Brief text:** "The missing crew member is Jordanian; the minister's line referred to the ship's three Indians."
- **Problem:** two things are being run together.
  - The Jordanian nationality is CONFIRMED (Jordan's foreign ministry, 19 Nov; Khaleej Times confirms the ministry is "following up on the disappearance of its citizen").
  - What Sonowal's line referred to is not established. The only basis is a Khaleej Times sidebar **headline**, "Three Indian sailors safe after attack on oil tanker in Gulf on Nov 18: Minister". KIN marks it "headline only; ship not resolved", and it is dated 18 Nov while NAVIG8 MESSI was hit on 17 Nov. KIN's own wording was "his three Indians **may** be safe". The web check found Riviera (18 Nov) tying Sonowal's "entire crew… safe and accounted for, with no serious injuries" to the ADNOC ship, which still conflicts with ADNOC's 11 injured.
- **Replacement text:** "The missing crew member is Jordanian (Jordan's foreign ministry). The minister's 'entire crew… safe' line probably referred to the ship's Indian crew (a Khaleej Times headline speaks of 'three Indian sailors safe'; it does not name the ship). That is our reading, not a statement."
- **Graph:** the same sentence sits in `strait-of-hormuz` ("(his three Indians)"). See G4.

**H3 — Ship war, "The limits": one quote is misattributed and one is a paraphrase in quotation marks**
- **Brief text:** "JMIC: 'There are no attributions of responsibility for these strikes.' Martin Kelly of Orbital Risk (via Maritime Executive) says the list 'is often used after vessels have been struck'".
- **Problem:**
  - **The JMIC line:** the web check of the Gulf News page that relays JMIC Update 115 (last updated 20 Nov 05:07) found the sentence as Gulf News's own unattributed text: "There are no attributions of responsibility for these strikes and no later JMIC updates." The second half shows it is the journalist writing. What JMIC's log itself records is "unknown projectiles".
  - **The Kelly line:** KIN's desk file has it without quotation marks ("the list is often used after vessels have been struck"). The web check says Maritime Executive paraphrases Kelly. The quotation marks were added downstream (CoS R5, then the brief).
  - My confidence is moderate on the JMIC point (one fetched read; the JMIC PDF was not read). The fix costs nothing.
- **Replacement text:** "**The limits:** JMIC logs the hits as 'unknown projectiles', and Gulf News, relaying its update, notes no attribution of responsibility. Martin Kelly of Orbital Risk told Maritime Executive, in its paraphrase, that the list is often used after ships have been struck; 175 of 240 listed ships have no recorded attack, and this one was reportedly also struck in mid-August."
- **Graph:** see G4.

**H4 — Yemen headline: the coalition's own account is written as fact, against R14**
- **Brief text:** "…and on Friday the coalition struck Hodeidah port, the condition the Houthis set…"
- **Problem:** R14 says: "Use 'the coalition says' for Hodeidah strike claims." The body does this ("the coalition's own statements… No independent damage report"); the headline does not. The web check found al-Malki's words ("We targeted operational capabilities at Hodeidah port that were used in smuggling operations"). Yemen's information minister says the port is "fully operational". So the other side disputes the effect.
- **Replacement text:** "…and on Friday the coalition **said it struck** Hodeidah port, the condition the Houthis set for attacking 'all Saudi ports along the Red Sea coast'. No port strike had followed by ~20:25 IST."
- Optional addition to the Hodeidah bullet: "Yemen's (Houthi) information ministry says the port is 'fully operational'."

**H5 — Page 2: the "live at 20:37 IST" VIX figure is a stale quote**
- **Brief text:** US and Europe table, VIX, 20 Nov (live): "28.55 (high 29.69)".
- **Problem:** the 1-minute ^VIX bars put VIX at **27.39 at 20:37 IST** (27.33–27.50 in that minute; 27.3–27.6 from 20:29 to 20:39). The 28.55 matches the 20:15–20:21 bars, so the spot pull took a quote about 15–20 minutes old. The day high of 29.69 (20:01 bar) is correct.
- European indices show the same lag, but smaller:
  - DAX 25,001.42 matches 20:21–20:24 (25,025–25,042 at 20:37, about −1.65% rather than −1.82%);
  - STOXX 629.87 against 630.81 at 20:37.
  - S&P (7,176.94 against 7,178.78) and SOX (9,081.84 = the 20:37 open) are correct.
- No test depends on the VIX figure (above 25 either way), but it is wrong at its stated time.
- **Replacement text:** "VIX … **27.4 (high 29.69)**". Either relabel the DAX and STOXX live column "~20:20 IST", or use 25,042 and 630.8 (DAX −1.65%, STOXX −1.19%) and correct the Significant Moves row to "−1.34% / −1.82% Fri live (~20:20 IST)". VIX has since risen; my ~21:20 pull shows 29.89.

**H6 — Israel: the IDF line can be read as an operational denial; it is about public guidelines**
- **Brief text:** "**Israel:** the IDF spokesman, on the record: 'no change to the current instructions.'"
- **Problem:** the web check found ToI, 20 Nov ~20:25 IST: "IDF spokesman says no changes to **public guidelines** amid reports of plans to renew Iran war". The words are verbatim from Brig. Gen. Effie Defrin's post on X: "no change to the current instructions, and we will update you if any changes occur." Placed directly after CBS's assault report, the brief's line reads as Israel denying the plan.
  - A search summary (not opened) says Defrin issued a similar message less than a day before the 28-Feb war. That point is the mirror of Axios's "undecided the day before" and should only be added if the CoS can confirm it.
- **Replacement text:** "**Israel:** the IDF spokesman, Brig. Gen. Defrin, on the record: 'no change to the current instructions' **for the public** (Home Front guidance), not a comment on plans."

### LOW

**L1 — Cooper–MBS date.** The brief says the commander of CENTCOM "met Crown Prince Mohammed bin Salman on Thursday".
- The web check found Reuters (via Yahoo) published at 01:51 UTC Thu 19 Nov (07:21 IST), "SPA reported on Thursday". NBC says the meeting was "on Wednesday". A Riyadh meeting reported before 05:00 Riyadh time on Thursday was almost certainly held on Wednesday.
- **Replacement text:** "met Crown Prince Mohammed bin Salman in Riyadh (reported by SPA early Thursday)". See G5.

**L2 — Hodeidah evacuation time.** The brief has "(~17:00 IST)". The web check found the call already out by ~16:20 IST (Dawn, citing Reuters, updated 15:52 PKT = 16:22 IST; Ajel metadata 11:03 UTC = 16:33 IST).
- **Replacement text:** "(by ~16:20 IST)".
- The strike announcement times (19:02–19:28 IST, Newsquawk/AA per SAU) were not re-found. Keep them attributed.

**L3 — Brent "oil-only" holds for the steep leg, not the whole slide.** The brief says: "Friday's slide from $92.2 (13:30 IST) to $90.06 (~15:15 IST) was oil-only: S&P futures were flat and gold rose."
- My 1-minute bars for 13:45–14:15 IST: Brent 91.93 → 90.95 (low 90.67); ES 7,175 → 7,171 (flat); gold 3,573.6 → 3,590.9 → 3,583.6 (up); ZN 106.109 → 106.188 (yields down); DXY 103.806 → 103.845 (+0.04%, flat).
- Over the full 13:30 → 15:15 window: ES 7,172.5 → 7,145.8 (−0.37%) and gold 3,577 → 3,574 (flat), against Brent −2.1%. "Oil-specific" still holds, but the evidence sentence fits only the steepest leg.
- **Replacement text:** "…was oil-specific: in its steepest leg (13:50–14:15 IST) S&P futures were flat and gold rose; over the whole slide ES fell 0.4% to Brent's 2.1%."
- Page 2 "(ES flat, gold up, yields down in the same minutes)" is acceptable as written.

**L4 — Fox timing.** The brief says: "on Thursday, flying home from Shenzhen, he told… Fox, 'We'll see what happens after January 1.'"
- The web check found JPost saying the Fox interview "aired on Thursday"; ToI and Yahoo describe it as recorded on Wednesday in Shenzhen.
- If it is the same Shenzhen interview as the 18-Nov "finish it off — soon", then "soon" and "after January 1" sit in one interview.
- **Replacement text:** "…Fox (in an interview aired Thursday), 'We'll see what happens after January 1.'"

**L5 — Reserves: Reuters' caveat is written as a cause.** The brief has "for the rest, Reuters cites revaluation and 'the maturity of the central bank's FX swaps'" (Section I), and Page 2 has the same.
- The web check (Reuters via Business Recorder) found Reuters attributes the fall to "a fall in value of both the central bank's foreign currency and gold holdings". The revaluation and swap-maturity sentences are Reuters' standing caveat ("The reserves are also impacted by…"), not an attribution for this week.
- **Replacement text:** "Reuters attributes it to lower values of the currency and gold holdings, and notes, as it does each week, that revaluation and FX-swap maturities affect the figure."
- The brief's conclusion ("No source says how much, if any, was dollar selling") stands.

**L6 — Signal overreach and partial recycling.** The brief says: "The graph drew that link on 19 November, and within two sessions the money moved as it predicts."
- The edge was drawn **from** this flow: thirteen sessions had already run, and the 19-Nov brief's case against already said "part of the inflow is an AI-trade rotation (the new `semiconductors → fii-flows` edge) that could reverse".
- Two more sessions of the same flow continue the pattern; they do not confirm a prediction. What is new is the size (₹17,720 cr), Bank Nifty records, and Taiwan/Korea selling on the same days.
- **Replacement text:** "The graph drew that link on 19 November; in the two sessions since, the money kept moving the way it describes, at a larger size."
- The hedge bullet is good as written.

**L7 — WaPo dating.** The brief says: "The episode dates from October."
- The web check found no date in the ToI relay of the Post. The October dating rests on JPost tying it to Channel 12's 6-Nov report and on Channel 12 placing a Netanyahu–Gofman plan before the 27-Oct election.
- **Replacement text:** "The episode reportedly predates the 27-Oct election (Channel 12, JPost)".

**L8 — Cascade Watch omits three items the changelog rates closest or closer.** These are `israel` 72-hour imminence (active, CLOSEST, not re-fired), `brent-crude` $85 leg (CLOSER, −6.5% from live) and `strait-of-hormuz` limpet (CLOSER).
- Suggested addition to "Closest, not fired": "`israel` 72-hour imminence (active; not re-fired)". Optional for "Closer": "`brent-crude` $85 (−6.5% away)".

**L9 — NAVIG8 MESSI headline asserts what the body tags as reported.** The headline says "The ADNOC tanker hit on 17 November is *NAVIG8 MESSI*". The body says "(reported, two sources)", and ADNOC has not named it.
- **Replacement text:** "…The ADNOC tanker hit on 17 November is named by JMIC and Maritime Executive as *NAVIG8 MESSI*, a ship on Iran's list…"

**L10 — PIF Tower: new identification of an event already reported.** The 19-Nov brief carried the coalition's Thursday "debris fell and material damage is being assessed" in Riyadh. SAU A1 says the Civil Defence tower statement "upgrades Thursday morning's 'debris… material damage' line". The Houthis claim the financial centre "at dawn and in the evening".
- The brief presents the tower as a fresh event and never says when it was hit.
- **Suggested text:** "The Riyadh damage first reported on Thursday was at the PIF Tower…" Alternatively, give the time ("hit on Thursday; Saudi authorities confirmed the damage that afternoon").

**L11 — IAEA date (no change needed unless dated).** GOV.UK says the E3+US "stonewalling" statement was delivered on **18 Nov** and published on 19 Nov; Reuters frames it as Thursday. The brief does not date it, so this is fine. Do not add "Thursday".

---

## Graph corrections (list only; for the Graph Engineer)

- **G1 — `trump` (20-Nov signal):** "This is the first time he has put a date on the hold in his own words" is **not supportable**. Earlier examples in the same node:
  - the 13-Oct signal: "**8 Oct Truth Social: no attack on Iran before 3 Nov**";
  - the 26-Oct signal: 25 Oct, "There will not be a strike today";
  - the 3-Nov signal: asked on 2 Nov about strikes after the midterms, "No".
  
  Replace with: "He has dated a hold in his own words before (8 Oct: no attack before 3 Nov); this date is the furthest out, past the 30-Nov strike window." The brief's "He put a date on it" claims no first and is fine.
- **G2 — `inr-usd` note_2026-11-20 (and the node's other three "Tue 24 Nov" mentions):** "earliest fire Tue 24 Nov" → "earliest fire **Wed 25 Nov** (Tue 24 Nov: NSE/currency holiday, Guru Nanak Jayanti)". Also `india.json`, where "Tue 24 Nov" appears in the inr context.
- **G3 — `fii-flows` note_2026-11-20:** "earliest fire Wed 25 Nov" → "**Thu 26 Nov** (Tue 24 Nov holiday)".
- **G4 — `strait-of-hormuz` fired note, status-change text and `irgc` (also `graph-changelog.md`):**
  - "JMIC: 'There are no attributions of responsibility for these strikes'" → "JMIC logs 'unknown projectiles'; Gulf News notes no attribution".
  - Drop the quotation marks around Kelly's "is often used after vessels have been struck".
  - "(his three Indians)" → "(probably his Indian crew; a KT headline, ship not named)".
  - `uae` already says "crew figures conflict", so leave it.
- **G5 — `saudi-arabia`, `houthis`, `united-states`:** "Cooper met MBS 19 Nov / Thu 19 Nov" → "reported by SPA early Thu 19 Nov (NBC: Wednesday)".

**Not a correction, for hygiene:** `edges.json` holds 24 duplicate from→to pairs, all pre-existing (none added today). That includes two `saudi-arabia → iran` edges of the same type, weighted 10 and 9.0. Worth a separate clean-up run.

---

## Trigger Point Review

| Trigger | Changelog | My assessment | Agreement |
|---|---|---|---|
| `strait-of-hormuz` 2-Nov blacklist (KOTC/Bahri/ADNOC ship on list struck; "attack attributed or vessel identified") | watching → fired, dated 17 Nov | Four elements: struck (ADNOC on record); ADNOC vessel (ADNOC); identified (JMIC 115 via GN plus Maritime Executive, matching casualty figures); listed (web check re-read the Eagle page "as of November 3, 2026": row 17 "NAVIG8 MESSI \| 9482859"; row 131 "AL DHANNAH \| 9783734"; 239 rows). The text's "or vessel identified" makes it fire without an attacker. A 3-Nov snapshot that contains the 2-Nov expansion satisfies "named on the 2-Nov list". | ✅ AGREE (fired on its letter). Fix the JMIC/Kelly quotes (H3, G4). |
| `china` APEC readout naming Iran/Hormuz by 20 Nov | watching → expired | Web check: the Xi–Trump MFA readout does not even say "Middle East"; the trilateral readout says "the Middle East situation"; the declaration omits Iran (relays). | ✅ AGREE |
| `saudi-arabia` Houthi strike on a Red Sea port/Shuqaiq by 15 Dec (new) | new watch | Well-formed (strike that lands; named ports; Saudi/coalition/wire confirmation; excludes claims and interceptions). It does not duplicate the capacity watch, which is about throughput at Abqaiq, Ras Tanura, Yanbu and the East-West line. Saree's threat was conditional on Hodeidah (web check). | ✅ AGREE |
| `united-states` RESUME | fired, no reset | Night seventeen quiet. The Sabereen/NAYA items are correctly logged, not treated as events. Leg (a) unmet: Trump's interviews do not mention Qeshm. Leg (b): nights 18/19/20 = Fri→Sat, Sat→Sun, Sun→Mon, so the earliest completion is Mon 23 Nov morning ✓. | ✅ AGREE |
| `vix` (>25 with listed kinetic event) | closest, not fired | Bars: through 25 in the 21:00 IST bar (high 25.58), 28.99 at the 22:35 bar, matching AMD and Anthropic. | ✅ AGREE |
| `rbi` FCA >$3bn ex-valuation, heavy intervention confirmed | closest | Raw −$7.897bn; no source confirms intervention; Reuters' swap line is a caveat (L5). | ✅ AGREE (not fired) |
| `rbi` <$700bn | closer | Arithmetic checks: the RBI gold line fell 5.9% for −$6.183bn, implying ~$98.6bn of gold now; gold −8.1% gives ≈ −$8.0bn and ~$697bn. Labelled an estimate. | ✅ AGREE |
| `inr-usd` <93 ×3 | closer, session 1 | Correct count, wrong date (H1, G2). | ✅ status / ❌ date |
| `fii-flows` 3 selling sessions | further | Correct status, wrong date (H1, G3). | ✅ status / ❌ date |
| `us-10y-yield` (HY >3.75% with 10Y <5%) | closer | FRED 3.52; par 5.04 ✓ | ✅ AGREE |
| `bahrain`, `kuwait` | not fired | No new Iranian fire found since 18 Nov (KIN, SAU) | ✅ AGREE |
| `israel` cabinet | not fired | Channel 13 "approved plans" (19-Nov brief) and Ynet name no cabinet decision or approver. Ynet's "die has been cast" was not re-found on the web. | ✅ AGREE |
| `saudi-arabia` capacity | not fired | SADAF claimed only (NBC: "no immediate Saudi confirmation"); the PIF Tower is not energy | ✅ AGREE |
| `houthis` Aden | closest | No new wire item | ✅ AGREE |
| `kospi`, `gold` ratio (fired; logged) | logged | 4,869.96 is the second close below 5,000; ratio 83.08 on settles (3,685.5 / 44.359) ✓ | ✅ AGREE |

No trigger moved on rhetoric. Trump's date and the CBS "short term" report moved nothing.

---

## Market Data Spot-Check (my re-pull, 21:00–21:28 IST)

| Data point | Brief | Verified | Match |
|---|---|---|---|
| S&P / Nasdaq / Dow, Thu close | 7,175.83 −2.02% / −2.25% / −2.19% | 7,175.83 / 23,879.20 / 49,097.06 → −2.018 / −2.254 / −2.193% (AP via web check, same closes) | ✅ |
| SOX / NVDA / AMD, Thu | −2.41% / 145.98 / −7.72% | 9,419.72 (−2.415%); 145.98; 489.19 (−7.724%) | ✅ |
| VIX, Thu close | 24.56 → 28.44 (+15.8%) | 28.44 (+15.80%); 21:00 bar high 25.58; 22:35 bar high 28.99 | ✅ |
| US legs | 20:40–21:05; 22:20–22:35 IST | S&P 5-minute: 7,380 → 7,274 low (21:05 bar); 7,314 → 7,193.8 (22:35 bar) | ✅ |
| Anthropic open | $111.50 vs $83; "shortly before noon" | Web: first trade 11:48 ET = 22:18 IST | ✅ |
| TAIEX / KOSPI / Nikkei, Fri | 36,033.29 −6.23% / 4,869.96 −5.21% / 56,436.65 −5.06% | TAIEX ✓ (−6.229%; −17.50% w/w). KOSPI and Nikkei closes from the web (24/7 Wall St/Yahoo point changes; DigiTimes −6.23%); yfinance daily is NaN, last 5-minute bars before the auction 4,853.85 / 56,576 | ✅ |
| Samsung / SK hynix / TSMC | 183,100 / 1,113,000 / 2,000 | −7.01% / −5.92% consistent; TSMC 2,000 ✓ | ✅ |
| SoftBank / Advantest | −14.5% / −10.3% | Web ✓ (¥3,025) | ✅ |
| Gold Dec, Thu settle / live / w/w | 3,685.5 (−1.51%) / 3,576.6 (−2.95%) / −8.0% | 3,685.5 ✓; 20:37 bar 3,573.6 (−3.04%, within the feed lag); low 3,514.9 ✓; −7.97% w/w | ✅ |
| Silver / ratio | 44.359; 42.24 (−4.78%); 83.08 Thu; ~84.7 live | ✓; 83.08 ✓; 18 Nov 83.04 ✓; 13 Nov 79.12 ✓ | ✅ |
| Brent Jan Thu settle / Fri | 91.98 / low 90.06 (~15:15) / 90.89 live | 91.98 ✓; 15:15 bar low 90.06 ✓; 20:37–20:39 bars 91.05–90.88 ✓; 13:30 bar 92.18 ✓; 92.00 in the 18:20 bar ✓; Thu 93.48 high (19:30 60-minute bar) ✓ | ✅ |
| Jan–Dec27 spread | 15.09 / 14.57 | 91.98 − 76.89; 90.89 − 76.32 ✓ | ✅ |
| TTF | 80.85 → 84.46 → 87.30 (+8.0%) | ✓ (+7.98%) | ✅ |
| Treasury par 19 Nov | 4.76 / 5.04 / 5.40 | CSV ✓ (also 18 and 13 Nov rows ✓) | ✅ |
| ^TNX intraday | 4.984 | 20:35–20:37 bars 4.984–4.980 ✓ | ✅ |
| HY OAS | 3.23 (13) / 3.43 (17) / 3.47 / 3.52 | FRED ✓ | ✅ |
| Brent spot FRED | last 92.94 (17 Nov) | ✓ | ✅ |
| Fed 50bp odds | ~0–2% (ZQZ26 95.940) | Recomputed: implied 4.060% − EFFR 3.88 = 0.180 × 31/22 = 25.4bp → ~1.4%. 95.945 (desk; my 20:45 bar) → 24.7bp → 0%. Thu 95.925 → 9.9% ✓; 18 Nov 95.930 → ~7% ✓ | ✅ |
| Nifty / Sensex / Bank Nifty | 25,514.30 / 25,800.60; 83,919.71; 64,635.20 record | ✓. Highest close since 18 Feb (25,819.35) ✓. Bank Nifty prior max 62,273.25 (17 Nov), so both days are records ✓ | ✅ |
| Nifty pre-war | 25,178.65 | 27 Feb close ✓ | ✅ |
| India VIX; OMCs | 17.32 (+7.5%); +1.6–1.9% | +7.51%; IOC +1.83%, BPCL +1.95%, HPCL +1.63% ✓ | ✅ |
| FII streak | fifteen | 19-Nov brief: thirteen to Wed 18 Nov, + Thu + Fri = 15 ✓; 30-Oct start check: 15 regular sessions ✓ | ✅ |
| FII / DII sums | ₹17,720 cr; DII ₹6,216 cr | 17,719.83; 6,216.37 ✓ | ✅ |
| Rupee | 93.32 / 92.67 prov; first close stronger than 93 since 10 Apr (PTI) | PTI via web: "first time since April 10" (closed 92.83 then) ✓ | ✅ |
| Reserves | −$14.205bn to $705.342bn; FCA −$7.897bn; gold −$6.183bn | Web (ANI/Tribune; ETV) ✓ | ✅ |
| STOXX / DAX Thu; Fri live | −0.88%; −1.34% / −1.82% | Thu ✓; Fri figures are ~20:20 IST quotes (H5) | ⚠️ |
| VIX Fri live | 28.55 at 20:37 | 27.39 at 20:37 (H5) | ❌ |
| Metals Fri | Pt −2.4%; Cu −0.9%; Al −0.9% (−10.2% w/w) | 1,315/1,347.6 = −2.42%; 5.574/5.625 = −0.91%; 2,815/2,839.5 = −0.86%; 2,815/3,133.25 = −10.16% | ✅ |
| Henry Hub Dec | +0.5% | 3.285/3.268 = +0.52% | ✅ |
| CF | +1.8% / +2.4% | +1.81% / +2.41% | ✅ |

---

## Items that passed

- **Trump's quotes (lead).** Each quote matches its outlet:
  - Reuters, "Well, I'll talk to you about it after the beginning of the year" and "We've got time" (JPost/TIME);
  - Axios/Channel 12 in ToI's wording;
  - Fox, "We'll see what happens after January 1" (JPost).
  
  Relays differ: JPost and CBS/Yahoo carry "I'm not rushing to make any decisions on Iran". The brief uses one version per outlet, attributed, which is acceptable. "Confirmed that he said it; a timeline, not a decision" is the right tag. The Axios "undecided the day before" note is included (a ToI paraphrase of Axios; there are no quotation marks in the brief). "Could include… Pickaxe Mountain" is not re-found verbatim (Axios returns 403).
- **CBS.** Verbatim on cbsnews.com (Dov Lieber, 7:02 AM EST = 17:32 IST): "considering launching a new assault on Iran in the short term" and "could be mounted within two to four days, if such an order were given"; "sources familiar with the matter". The "White House declined to comment" line is correct (CBS: "The White House and U.S. military declined to comment"). It is correctly tagged as one outlet with unnamed sources.
- **Senate 48–51.** CBS: Collins, Murkowski and Paul voted for; "all but one Senate Democrat — Sen. John Fetterman". A concurrent resolution. Confirmed.
- **The hold rule and night seventeen.** The search list is in the KIN note. Sabereen/NAYA are kept out as events. Earliest new leg-(b) completion is Mon 23 Nov (calendar counted). Leg (a) is unmet. The rule is paraphrased, not quoted, and matches the 19-Nov brief's paraphrase and the node text. "No new Iranian fire at a Gulf host since 18 Nov" follows R3's wording. `bahrain` and `kuwait` are not fired.
- **PIF Tower.**
  - NBC/Reuters: "material damage to several floors of the building and nearby buildings, but no injuries"; "The statement did not identify the tower, but… SPA showed the PIF Tower"; "Three sources… struck by an incoming Houthi missile". The coalition's "debris had fallen" is confirmed.
  - The MFA's "all necessary measures" is confirmed (Arab News).
  - Damage is confirmed and the cause is reported. Correct.
- **Saree.** The port threat was conditional on Hodeidah being struck (web), and the brief says so. "Immediately evacuate their ships from these ports" and Shuqaiq are verified. No port strike was found by ~20:30–20:50 IST (MEE, Gulf News, MEMO). SADAF is claimed only (NBC). The 70 days count is correct (11 Sep → 20 Nov).
- **India.** Closes, records, the streak, flows, the rupee and reserves all check (table). The Shetti quote is verbatim on HDFC Sky ("Nifty is expected to zoom towards 26,000 and next 26,350 in the next 1 or 2 weeks"). No sentence says the RBI bought or sold dollars; "No report says the RBI bought dollars" is correct.
- **Deployment block.**
  - The three conditions match the 19-Nov brief word for word.
  - Scored correctly: condition 1 met (four settles below $95: 16, 17, 18 and 19 Nov); condition 2 fails on the credit leg (3.43 → 3.47 → 3.52 is widening, so even a sub-5% close fails); condition 3's inflation leg fails.
  - Open decisions (i)–(iv) carry over unchanged, with (ii)'s "fired at" record unchanged.
  - The recommendation and the tactical exception are unchanged and consistent.
- **Scorecard.**
  - Flynn met (91.95 < 92.76 on 18 Nov; final).
  - Lipow failed (no settle above $95 in the window).
  - Kalın failed.
  - Vijayakumar met (25,800.60 > 25,144.30).
  - Trump's "soon" is open.
  - Hasan Al Hasan holding; Firebrand leaning no; Reuters' "may hold off" holding.
  
  All are consistent with the 19-Nov tests. The new calls' tests are well-formed and dated: Spanjer is verbatim (CNBC); Shetti is verbatim.
- **Updates box.** "Sunday 22 November" → Monday 23 ✓; the *Al Dhannah* quote "one monitor shows it 'removed'" matches the 19-Nov text and is now corrected (row 131 re-read on the web) ✓; `china` closed ✓. The NAVIG8 MESSI line is fine apart from H2.
- **Cascade Watch edges and statuses.** Every id, status and weight matches `graph-changelog.md`, `edges.json` and the node files.
- **Balance (Check 7).** Section I has four geopolitical items and three markets items (AI/chips, India, oil/gas). Section II has two market voices (Spanjer, Shetti). Section III covers credit, reserves and gold. Balanced.

## Not independently re-found
- Hunterbrook's 21:00 IST publication stamp (the AMD report itself is confirmed; Bloomberg).
- The FT's TSMC/Samsung story at 15:51 IST Thu. One relay (The Fly) is stamped Fri 10:55 UTC (16:25 IST), and a search summary dates the FT story to 19 Nov. Reuters' 18:18 IST Thu "TSMC tightens China AI chip curbs" independently gives a Thursday chip-curb story. If the FT timing is wrong, Section I's "after an FT report…" should become "after reports of tighter TSMC China curbs (Reuters, Thursday)".
- The coalition's 19:02–19:28 IST strike stamps.
- Ynet's "the die has been cast" (ISR's read only).
- Axios's "could include" wording.
- The KRX/JPX close prints at source (consistent web point changes).
- Friday's FII/DII provisional figures at source (Thursday's are re-found via PTI).
- The original JMIC 115 PDF.
- The Jordan MFA page itself (Khaleej Times relay found).
- The full text of the four-point declaration.
- The China MFA trilateral page (the desk read it; the web check saw only summaries).

## Final Verdict
**APPROVED WITH CORRECTIONS.** Six HIGH fixes, all small wording or number changes:
- the holiday-shifted dates (H1);
- the Sonowal inference (H2);
- the JMIC and Kelly quote attribution (H3);
- "the coalition says" in the Yemen headline (H4);
- the stale live VIX and European quotes (H5);
- the IDF "instructions" context (H6).

The leads are well sourced and correctly tagged: Trump's three interviews, CBS as one outlet, the Senate vote, the PIF Tower and Hodeidah. The two trigger changes are sound. The graph needs G1 (the unsupportable "first time" claim) plus the date and quote fixes in G2–G5.

**Basis:** ran yfinance daily data, 1-minute and 5-minute bars, FRED, the Treasury CSV and a graph diff against the backup; read the brief, the CoS header R1–R15, the desk bottom lines, KIN/SAU/IND/MAC sections, the changelog, the node triggers and the 19-Nov brief; sourced the web checks through three sub-agents (direct page reads, some search summaries, as marked). **Not checked:** the items listed above, and the FEDAI interbank calendar for 24 Nov. **Confidence:** high on the market data, the calendar (our graph records the NSE holiday) and G1; moderate on H3's JMIC point and on L1/L2/L4 (single web reads).

---

## Chief of Station — corrections applied (21:25–21:35 IST Fri 20 Nov, `date`-checked)
Pre-correction backups: brief `backups/2026-11-20/2026-11-20-evening_v1.md`; graph `backups/2026-11-20/graph_v2_preverif`.

- **H1** applied: `inr-usd` earliest fire Wed 25 Nov (Cascade Watch, Dated tells); `fii-flows` cannot fire before 26 Nov (Signal); Tue 24 Nov holiday added to Dated tells.
- **H2** applied: the Sonowal line is now "probably… our reading, not a statement", with the Khaleej Times headline named as its only basis.
- **H3** applied: JMIC "unknown projectiles"; Gulf News notes no attribution; Kelly's line without quotation marks ("in its paraphrase").
- **H4** applied: headline "the coalition said it struck Hodeidah port"; Hodeidah bullet adds the Houthi information ministry's "fully operational".
- **H5** applied: VIX live 27.4 (high 29.69); DAX/STOXX live labelled "~20:20 IST" in the snapshot and Significant Moves.
- **H6** applied: IDF line now "for the public (Home Front guidance), not a comment on plans"; spokesman named as the source names him. The "similar message before 28 Feb" point not added (not confirmed).
- **L1** applied (Cooper–MBS "reported by the Saudi news agency early Thursday"); **L2** applied ("by ~16:20 IST"; strike stamps "per relays"); **L3** applied (oil-specific in the steep leg; ES −0.4% vs Brent −2.1% over the whole slide); **L4** applied (Fox "in an interview aired Thursday"); **L5** applied (Section I and Page 2: Reuters' weekly caveat, not a cause); **L6** applied (Signal: "kept moving the way it describes, at a larger size"); **L7** applied ("reportedly predates the 27-Oct election (Channel 12, JPost)"); **L8** applied in part (`israel` 72-hour added to Closest); **L9** applied ("named by JMIC and Maritime Executive as"); **L10** applied (the hit "came on Thursday, and is probably the Riyadh 'material damage' our last brief carried — our reading"); **L11** no change (not dated in the brief).
- **Graph G1–G5** applied by `staging/2026-11-20-evening/gu_verif_corrections.py` (trump "first" removed; inr-usd/fii-flows holiday dates; JMIC/Kelly/Sonowal wording in strait-of-hormuz, irgc and the changelog; Cooper–MBS date in saudi-arabia, houthis, united-states). A double replacement in the changelog (inr-usd lines briefly read "Thu 26 Nov") was caught and fixed. All node JSON valid; viewer rebuilt (63 nodes, 418 edges).
- Edge-duplicate hygiene (24 pre-existing duplicate from→to pairs): not touched this run; noted for a clean-up.
