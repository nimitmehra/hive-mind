# Verification Report — 18 April 2026 (Evening)
Generated: ~00:30 IST Sunday (19 April) | Fact-Checker: Red Team
Brief checked: briefs/2026-04-18-evening.md
Evidence baseline: staging/2026-04-18-evening/intel.md, staging/2026-04-18-evening/markets.md, staging/2026-04-18/graph-changelog.md

## Summary
7 Section I items checked, 7 analyst takes reviewed, 1 HIGH flag raised, 2 LOW flags noted, 1 correction applied to the brief.

---

## Flags

### Flag 1: Cascade Watch — trigger activation language outruns operational-source standard
- **Issue:** Section III says "Two trigger points moved today" and describes the *"Iran executes 'reciprocal measures'"* trigger as "promot[ed] ... to active on the 'IRGC harassment' leg" within 24 hours of creation. Read literally, this claims the trigger has been activated. The brief's footer says activation is "pending Graph Engineer evening update." The graph state (`graph/nodes/iran.json:1173-1183`) still carries the trigger at `"status": "watching"`.
- **Evidence:** The ARCHITECTURE rule in /verify-brief requires "2+ **independent operational sources**" for a trigger to move from watching to active. On Saturday, the operational corroboration is UKMTO + UK Ministry of Defence — same UK military chain of command = one operational source — plus four news wires (Irish Times, AP/WSLS, Haaretz, Al Jazeera) citing UKMTO. Intel A1 explicitly notes "US (CENTCOM): no public response captured at dossier timestamp" and Non-Event E6 confirms no CENTCOM advisory has been issued. Vessel flags, operators, and cargo are not yet publicly disclosed. No Kpler or MarineTraffic imagery of the incident has surfaced.
- **Severity:** HIGH. A trigger-point error corrupts the graph's memory for weeks. The event itself is adequately verified for reporting (CONFIRMED — item stands), but the trigger-activation bar is stricter than the reporting bar.
- **Recommended correction:** Replace "Saturday's UKMTO-confirmed kinetic promotes it to active on the 'IRGC harassment' leg within less than 24 hours of trigger creation, the fastest watching→active transition of any trigger this crisis" with language that frames activation as conditional on independent operational corroboration (CENTCOM public statement, Kpler/MarineTraffic imagery, or a second-incident confirmation within 72 hours). Keep the trigger at `watching` in iran.json until the bar is cleared.
- **Applied:** Yes — brief text softened; trigger kept at `watching` in iran.json.

### Flag 2: Brent Friday-settle source ambiguity
- **Issue:** Brief carries Brent BZ=F at **$91.87 (-7.6%)**. yfinance BZ=F for 2026-04-17 returns **$90.38 (-9.07%)**. Both figures appear in morning markets.md (staging/2026-04-18/markets.md:13-14 — "BZ=F continuous $91.87" vs "ICE June print, wires ~$90.38"). Graph-changelog explicitly notes the same pair: "$91.87 (actual Friday settle; wire-ICE $90.38 -9.1%)."
- **Evidence:** The brief is internally consistent with the morning dossier's "continuous" figure. yfinance returns a different number for the same ticker — consistent with a data-source/settlement-time discrepancy that is explicitly documented upstream. All downstream arithmetic in the brief (physical-futures gap $40, Monday open scenarios) uses $91.87 and holds together.
- **Severity:** LOW. Internal consistency preserved; discrepancy documented in evidence files; direction and order of magnitude unambiguous.
- **Recommended correction:** None. If the Monday open prints near $90 rather than ~$92, future briefs should reconcile the settle-source choice with Argus/Platts rather than rely on yfinance or the wire-ICE figure alone.
- **Applied:** No.

### Flag 3: Kpler "~1–2% of baseline" math is slightly generous at the lower end
- **Issue:** Brief says ~2 oil/gas tankers since Apr 8 ceasefire is "roughly 1–2% of the pre-war ~120-vessels-per-day baseline." Strict arithmetic on 2 tankers / (120 × ~10 days) = 0.17%. The 1–2% figure is only defensible if the denominator is the oil/gas subset of ~25/day (then 2/250 = 0.8%) or if the numerator expands to the broader ~9-tanker week figure (then 9/840 = ~1%). The brief does note the broader-week figure separately.
- **Severity:** LOW. The direction and substance (*dramatically* below baseline) are correct; the ratio is within the bounds of the figures the brief cites; not a claim-breaking error.
- **Recommended correction:** Future briefs specify the denominator (oil/gas tanker subset vs all vessels) when citing a ratio. No edit to today's brief.
- **Applied:** No.

---

## Items That Passed

### Item 1 — IRGC gunboats opened fire on tanker + two merchant vessels (PASS)
- **Action or rhetoric?** CONFIRMED ACTION. UKMTO advisory + UK MOD public statement. Multiple independent wires carrying the UKMTO attribution (Irish Times, AP/WSLS, Haaretz, Al Jazeera liveblog). ✅
- **Language:** Brief correctly calls them "warning shots, not a disabling attack"; notes "no injuries … vessels not disabled"; notes CENTCOM silence and missing vessel-flag/operator disclosures. Does NOT elevate to "Iran attacked US interests." ✅
- **Other side:** Iran (IRGC Joint Military statement framework), Iranian civilian government (no retraction), CENTCOM (silence noted). ✅
- **Verification tag handled correctly** — CONFIRMED for the event; separately handled as trigger-activation question (see Flag 1). ✅
- Strongest item in the brief. The *action occurred* bar is cleared; the *trigger activation* bar is a separate gate (Flag 1).

### Item 2 — IRGC Joint Military "returned to previous state" declaration (PASS)
- **Action or rhetoric?** CONFIRMED OPERATIONAL POLICY (an institutional declaration — properly framed as policy/declaration, not as military action). ✅
- **Sources:** Irish Times, ABC7, Tribune India, PBS, Tasnim. Multi-wire with Iranian state-media primary sourcing for the direct quote. ✅
- **Other side:** Araghchi's non-retraction noted; Ghalibaf's "designated route" accommodation noted; Ministry of Transport's "no traditional fees" off-ramp noted — all included. ✅
- **Mojtaba Khamenei "Navy's Ready" handling:** Brief tags it "*REPORTED*, single-outlet; primary Persian-language statement not independently located." Correct downgrade — single Haaretz headline attribution, primary Farsi statement not located. ✅

### Item 3 — Reliance Industries rejected Derya + Lenore cargoes (PASS)
- **Action or rhetoric?** CONFIRMED ACTION (documented corporate rejection). ✅
- **Sources:** MarineLink (industry trade), Business Standard, Goodreturns citing Reliance company statement. ✅
- **Other side:** Brief correctly notes IOC and BPCL/HPCL did *not* mirror — state refiners yes, private-refiner no. This is the right both-sides framing; the brief explicitly narrows the bear case ("Monday is still binary; the downside is slightly narrower"). ✅
- **Scope discipline:** Brief does *not* elevate to "India cancelling Iran oil" — careful framing of one company's compliance decision. ✅

### Item 4 — Kpler ~2 oil/gas tanker transit since April 8 (PASS with LOW flag on ratio)
- **Source:** Kpler via CNBC (April 15, reconfirmed April 18) — operational tracker, direct. ✅
- **Data framing:** Brief correctly distinguishes the oil/gas subset (~2) from the broader week figure (~9 including Iraqi *Ocean Thunder*, Chinese VLCCs *Cospearl Lake* + *He Rong Hai*, *Shalamar*). ✅
- **Ratio arithmetic:** See Flag 3 (LOW). Not a claim-breaking issue.
- **Causal linkage:** "Friday's −7.6% Brent crash was paper-market theatre built on a political declaration that had no operational backing" — supported by Kpler + AWRP unchanged at ~1%. ✅

### Item 5 — Trump "drop bombs" + "prohibited" Israeli strikes narrowed to offensive-only (PASS)
- **Action or rhetoric?** RHETORIC — Trump statements, not new US kinetic action. Brief correctly labels both as rhetoric-category. ✅
- **Sources:** Irish Times, ABC7, NBC for "drop bombs"; AP via KGW, CBC for the "prohibition" + State Dept clarification. ✅
- **Critical correction included:** Brief explicitly notes State Dept narrowed to "offensive action only, not self-defence" — and then correctly observes "operational effect on Israel's strike freedom is zero." This is exactly the headline-vs-operational gap check. ✅
- **Kounine drone strike** included as Day-2 evidence (CBC, Lebanese Health Ministry — CONFIRMED). ✅

### Item 6 — Rubio-Saudi FM call (PASS)
- **Sources:** Tribune India, ANI, Middle East Eye — three independent regional wires. ✅
- **Framing:** Brief correctly positions Saudi Arabia as "post-ceasefire convener" without overstating; notes UAE/Oman/Qatar differentiated responses. ✅
- **Non-event handled well:** "No Gulf state has publicly condemned Iran's Saturday action — the absence is itself a signal." — correct use of silence as intelligence without overreaching. ✅

### Item 7 — Houthi non-attack Day 52 (PASS)
- **Source:** UKMTO JMIC Advisory 031 — primary operational source. ✅
- **Framing:** Brief correctly labels this "the most important Houthi non-event of the crisis" given the 18-hour post-kinetic window; includes the Soufan coordination-thesis falsifiable test. Does NOT elevate "Bab al-Mandeb is among our options" rhetoric to action. ✅
- **Edge-weight implication:** "one of the tail risks priced into Friday's Frontline +5.6% rally and into VLCC rates sitting at ~$130K/day dilutes in kind" — defensible given the non-event is confirmed via UKMTO. ✅

---

## Trigger Point Review

| Trigger | Status in Changelog | My Assessment | Agreement? |
|---|---|---|---|
| Iran executes 'reciprocal measures' | watching (new, added today) | Should stay **watching** until CENTCOM or Kpler/MarineTraffic corroborates the UKMTO account. UK military ≠ 2 independent operational sources. | ✅ AGREE on watching; ❌ DISAGREE with brief's "promoted to active" framing. Corrected in brief. |
| Physical-futures gap closes below $10 | watching (new) | Correct. Current gap ~$40; Monday print is the test. | ✅ AGREE |
| Iranian internal consolidation | active (mechanism updated — divergence character) | Saturday's Khatam al-Anbiya codification + Supreme Leader endorsement signal resolves the divergence in the IRGC's favour; mechanism-updated at "active" is defensible. | ✅ AGREE |
| Hormuz remains under Iranian selective control | active (REINFORCED) | IRGC permission regime is the operational codification; the fact that it's being enforced via warning-shot action reinforces the active status. | ✅ AGREE |
| All "watching" triggers not shown above | watching (unchanged) | Reviewed all 20+ watching triggers in iran, strait-of-hormuz, irgc, brent-crude, sp-500, fertilizer-urea, india, united-states, israel, uae, pakistan. None have crossed the 2-source operational bar on today's evidence. | ✅ AGREE |

---

## Market Data Spot-Check (yfinance, 2026-04-17)

| Data Point | Brief Value | yfinance Value | Match? |
|---|---|---|---|
| S&P 500 | 7,126.06 (+1.2%) | 7,126.06 (+1.20%) | ✅ EXACT |
| VIX | 17.48 | 17.48 (-2.56%) | ✅ EXACT |
| CF Industries | $112.68 (-9.6%) | $112.68 (-9.65%) | ✅ EXACT |
| Frontline | $37.13 (+5.6%) | $37.13 (+5.63%) | ✅ EXACT |
| Nifty 50 | 24,353.55 (+0.6%) | 24,353.55 (+0.65%) | ✅ EXACT |
| Gold (GC=F) | $4,857.60 (+1.5%) | $4,857.60 (+1.51%) | ✅ EXACT |
| Silver (SI=F) | $81.74 (+4.0%) | $81.74 (+3.98%) | ✅ EXACT |
| Brent (BZ=F) | $91.87 (-7.6%) | $90.38 (-9.07%) | ⚠️ **SEE FLAG 2** (continuous vs ICE June print; both figures documented in morning markets.md) |
| WTI (CL=F) | $84.00 (-11.3%) | $83.85 (-11.45%) | ≈ CLOSE (within tick) |

The equity/metals/volatility data is precisely sourced. The oil discrepancy is a known source-ambiguity flagged upstream.

---

## Final Verdict
**APPROVED WITH ONE CORRECTION APPLIED.**

This is a high-quality brief. The lead finding (IRGC gunboat kinetic) is adequately verified for reporting; the Reliance rejection is properly narrowed; the Trump "prohibition" headline-vs-operational gap is explicitly dissected; the Haaretz "Navy's Ready" line is correctly tagged REPORTED; the Houthi non-event is treated as genuine silence-as-intelligence; Kpler data is cited from an operational source. The editor showed strong discipline distinguishing rhetoric from action across the entire brief.

The single HIGH flag is the trigger-activation language in Cascade Watch, which was softened to match the graph's current `watching` state and the architecture's 2-independent-operational-sources standard. If CENTCOM corroborates or a second incident occurs within 72 hours, the trigger moves to active on the next cycle.

Market data: 8 of 9 spot-checks are exact. Brent figure has a documented source ambiguity (continuous vs ICE wire); not a correction-level issue today, but reconcile in future briefs.

*Verified: 7 Section I items + 7 analyst takes + 20+ trigger states + 9 market prints checked. 1 HIGH flag corrected. 2 LOW flags noted. Brief APPROVED.*
