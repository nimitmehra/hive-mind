# Verification Report — 22 July 2026 (Evening)
Generated: ~16:20 IST | Fact-Checker: Red Team
Brief checked: `briefs/2026-07-22-evening.md`

## Summary
**6 Section-I items + 12 trigger decisions + 7 market data points checked. 2 corrections applied, 2 items flagged PLAUSIBLE, 1 claim excluded outright.**

The brief is the cleanest of the recent run — reading time is down to **~9 minutes** (from 11–14 earlier this week), the trigger discipline is intact (0 escalations across a war-restart-high oil day), and the insurance correction from Monday held. The two corrections are precision fixes, not substantive errors. What I most wanted to break — the "flat price finally coupled" thesis and the Bushehr-province escalation — both survived, because both are hedged against their own strongest counter-evidence in the text itself.

---

## Corrections Applied

### 1. Ceasefire authorship over-asserted (HIGH → fixed)
- **Issue:** The lead called it "the Qatar/Pakistan 10-day ceasefire" as settled fact. The staging file (intel A4) explicitly tags authorship **UNRESOLVED** — the Jerusalem Post reports Iran itself *secretly submitted* the proposal, inverting the baseline that Qatar/Pakistan conveyed it.
- **Why it matters:** This is exactly the tag-drift the pipeline exists to catch — a REPORTED/disputed detail hardening into an asserted one at the Editor handoff.
- **Correction applied:** now reads *"the mediated 10-day ceasefire (conveyed by Qatar and Pakistan; one report has Iran itself as the originator)."* Qatar/Pakistan as **mediators** is well-corroborated (four independent chains); only the drafting origin is disputed, so the fix preserves the confirmed part and hedges the disputed part.

### 2. Brent lead needed an as-of stamp (LOW → fixed)
- **Issue:** The lead cited Brent "$93.84" while the live front-month had already extended past $94.40 by mid-afternoon. A reader checking a live feed would see a discrepancy.
- **Correction applied:** *"$93.84 (the ~14:12 IST print; extending past $94 into the afternoon)."* The direction is if anything *more* supportive of the item's thesis.

---

## Items Flagged PLAUSIBLE — attributed, not asserted, left standing

### Flag A — the ~7.6% July Fed hike odds (single-source)
- **Status:** The figure is single-source (CoinGape; CME FedWatch was blocked to all desks). The brief hedges it as "roughly 7.6%… reported."
- **Verdict:** LEAVE. The *direction* — hike odds falling further even as Brent hit $94 — is corroborated by the whole prior week's trend (46.5% → 15.5% → lower) and is the load-bearing claim; the exact figure is not. The Section-III "transmission inverted" argument does not depend on 7.6% versus, say, 10%.

### Flag B — Haaretz's "ground invasion looms" (single analytical desk)
- **Status:** One outlet's analytical framing, not a reported fact. The brief attributes it explicitly to Haaretz twice and frames it as *"a scenario neither the oil market nor prediction data is pricing"* — i.e. it is presented as an unpriced risk, not an event.
- **Verdict:** LEAVE. It is doing legitimate analytical work — it is corroborated in *mechanism* by Frank Kendall's on-record doctrine ("air power must be coupled with ground operations") and by the observed exhaustion of the easy target set (night 11 hit military infrastructure, not new high-value sites). Properly labelled, it belongs in the Risk Landscape. It became a new `united-states` trigger, correctly at *watching*.

---

## Claim EXCLUDED outright

**The IRGC's "Operation Nasr-2" strikes on US bases in Kuwait, Bahrain and Jordan** (incl. "the digital eye of CENTCOM," "Amazon data infrastructure in Bahrain") — **CLAIMED, one-side, and host-denied by the established pattern** (the Aqaba/Al-Azraq contradictions of the prior window). Kept out of the brief entirely; logged on the `irgc`/`iran` nodes as CLAIMED. This is the correct treatment and the reason the brief does not carry a "fresh wave of Iranian strikes" item.

---

## Trigger Point Review — spot-check of the most critical

| Trigger | Changelog | My assessment | Agree? |
|---|---|---|---|
| Fordow/Natanz/Esfahan strike | watching | **watching** | ✅ Night 11 hit Bushehr *province*, not the complex; the "Isfahan/Bushehr = nuclear strike" trap was avoided a second time. Holding this through a reactor-proximity strike is correct. |
| Rial breaks 2,000,000 | watching | **watching** | ✅ ~1,915,000, reversal stalled. No fire on a soft drift. |
| USD/INR clean break of 96.60 | *new, watching* | **watching** | ✅ The rupee *touched* 96.53; a defended touch is not a break. The new trigger correctly separates "touch" from "clean break." |
| First kinetic Houthi attack on a Saudi hull | watching | **watching** | ✅ Three AIS turn-backs, zero ships struck. A declaration with effect is not an attack — the exact discipline the March 2026 Houthi error demands. |
| US ground operation | *new, watching* | **watching** | ✅ Correctly created at watching off Haaretz's framing, not fired. |

**Zero escalations, and I could not find one that should have fired.** The rupee touching its record and Brent making a war high are both genuine escalations of *degree* that correctly did not trip *threshold* triggers.

---

## Market Data Spot-Check

| Data point | Brief | Script | Match |
|---|---|---|---|
| Brent | $93.84 (~14:12) → >$94 pm | 94.40 | ✅ (stamped) |
| Nifty | 23,973.75 | 23,970.60 | ✅ |
| VIX | 17.46 | 17.47 | ✅ |
| USD/INR | 96.53 | 96.54 | ✅ |
| Gold | 4,122.50 | 4,119.50 | ✅ (intraday drift) |
| KOSPI | 6,797.70 | 6,797.70 | ✅ |
| URA | 40.25 | 40.25 | ✅ |

**7/7 within tolerance.** The Brent/gold drifts are live intraday movement since the brief was written, now stamped.

## Graph integrity check
- **The `inr-usd→india` edge was mistakenly downgraded 10→8.5 mid-run and restored to 10.0 in-session** — I confirmed it reads 10.0 in `edges.json`, and the rationale documents the correction. Credit for self-reporting; verifying the revert rather than trusting the changelog is the point.
- **`marine-war-risk-insurance→strait-of-hormuz` confirmed at 7.0** — the Monday correction held; no drift back toward the discredited capacity-cap framing.
- Edge count 394 in file and `meta.json` — reconciled.

## Completeness / Proportionality (Check 7)
- **Section I:** 3 geopolitical / 3 commodity-market-business. ✅ Balanced.
- **Section II:** Goldman (market), Kendall (military-technical), Rubio-vs-Trump (policy). ✅ Market voice present.
- **Section III Cascade Watch:** covers `brent-crude→india`, `inr-usd→india`, `qatar→ttf`, `united-states→indian-it`, `marine-war-risk-insurance`. ✅ Commodity cascades alongside the military triggers.
- **Graph completeness:** 29 nodes updated, matching both staging files' affected-node lists; the secondary-actor nodes (saudi-arabia, red-sea, oman, iraq) were all updated. ✅

---

## Final Verdict

**APPROVED WITH CORRECTIONS.**

Two precision fixes applied (ceasefire authorship, Brent stamp); two single-source items correctly left attributed rather than asserted; one interested-party claim (Nasr-2) correctly excluded. Trigger discipline held through the most market-active day of the week. The standing format problem is largely resolved — ~9 minutes is within reach of the standard for the first time this run.

The one honest residual: three of the six Section-I items rest partly on RSS-headline-level sourcing (bodies not retrievable under the web-budget constraint), and the brief flags this in its header. That is a collection limitation, transparently disclosed, not a verification failure.
