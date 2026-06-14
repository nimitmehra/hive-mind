#!/usr/bin/env python3
"""Graph update for 2026-06-13 (Saturday) — deal moves to a NAMED Sunday signing date but the
text is CONTESTED, Khamenei's approval is third-hand, enrichment unresolved. Markets CLOSED —
no price changes since Friday. Discipline: 'signed Sunday' is a CLAIM, not a signature — no
trigger fires. Backup at backups/2026-06-13/graph/. Run from repo root."""
import json
DATE = "2026-06-13"
NODES = "graph/nodes"

def load(nid):
    with open(f"{NODES}/{nid}.json") as f: return json.load(f)
def save(nid, d):
    with open(f"{NODES}/{nid}.json", "w") as f: json.dump(d, f, indent=2, ensure_ascii=False)
def add_signal(d, h, s, v):
    d.setdefault("recent_signals", []); d["recent_signals"].insert(0, {"date": DATE, "headline": h, "sources": s, "verification": v}); d["recent_signals"] = d["recent_signals"][:26]
def bump_edges(d, ups):
    for to, ctx, w in ups:
        for e in d.get("top_edges", []):
            if e.get("to") == to:
                e["last_activated"] = DATE
                if isinstance(e.get("activation_count"), int): e["activation_count"] += 1
                if ctx: e["context"] = ctx
                if w is not None: e["weight"] = w
def trig_note(d, subs, key, text, ns=None):
    for t in d.get("active_triggers", []):
        c = t.get("condition", "")
        if all(s.lower() in c.lower() for s in subs):
            t[key] = text
            if ns: t["status"] = ns
            return True
    return False
CH = []

# ---- iran ----
d = load("iran")
add_signal(d,
  "DEAL MOVED TO A NAMED SUNDAY (14 JUN) SIGNING DATE — BUT THE TEXT IS CONTESTED AND IRAN IS INTERNALLY SPLIT. A 'final draft text' was reportedly agreed 12 Jun (two-part: MoU then peace deal), and Trump says it signs Sunday. But Iranian media published a draft with DIFFERENT terms (US withdrawals, reconstruction funding) that Trump rejected, and lawmaker Meisam Zohurian called the parliament-media text 'irresponsible' over implied enrichment recognition. FM Araghchi says the MoU covers nuclear/sanctions/Hormuz; other Iranian voices say nuclear is a SEPARATE track. Iran calls the reports 'preliminary.' Ceasefire largely held (no major new strikes 12-13 Jun).",
  ["Fox/CBS (signed Sunday)", "NBC (draft text)", "Iran Intl (Zohurian)", "The Tribune (Araghchi)"],
  "REPORTED (deal close/draft); CLAIMED (final text, Sunday signing); CONFIRMED (ceasefire held)")
d["summary"] = ("Day 106 / 2026-06-13 (Saturday). **THE DEAL HAS A SIGNING DATE — SUNDAY 14 JUN, PER TRUMP — BUT THE 'FINAL TEXT' IS CONTESTED, THE SUPREME LEADER'S APPROVAL IS THIRD-HAND, AND ENRICHMENT IS UNRESOLVED.** "
  "A draft was reportedly agreed 12 Jun (two-part: an MoU on ceasefire/Hormuz/blockade, then a peace deal), and the ceasefire largely held into the weekend (no major new strikes 12-13 Jun). But the optimism sits over real fractures: Iranian media published a competing draft (US withdrawals, reconstruction funding) Trump rejected; a sitting lawmaker branded the parliament text 'irresponsible' over enrichment; Iran calls the reports 'preliminary'; and the US still demands 'zero enrichment.' "
  "Iran intends to keep a Hormuz revenue role even in the deal ('service fees' ~$1/bbl, not 'tolls'), and Trump's claim that Mojtaba Khamenei approved is attributed to an INTERMEDIARY — implausible to confirm in real time given Khamenei's courier-based comms since the 28 Feb assassination of his father. This is the 9th 'deal close' claim of the war, now with a date but the most contested text yet. Sunday's signing (or slip) is the binary; treat the deal as unsigned until a single agreed text is published.")
bump_edges(d, [("united-states", "2026-06-13: Deal moved to a named Sunday signing date; ceasefire held; but the text is contested and enrichment unresolved. Still UNSIGNED.", None)])
trig_note(d, ["mou", "signed"], "note_2026-06-13",
  "STAYS WATCHING. Trump says the MoU signs Sunday 14 Jun, but the 'final text' is contested (competing Iranian draft Trump rejected; lawmaker calls it 'irresponsible'), Iran calls it 'preliminary,' and Khamenei's approval is third-hand via intermediary. Fires ONLY on a published signed text — NOT on a 'signs Sunday' claim. This is the weekend binary.")
trig_note(d, ["14-point"], "note_2026-06-13",
  "STAYS WATCHING. A draft (now reported as a two-part MoU+peace-deal structure) is claimed agreed but unsigned and internally contested.")
d["last_updated"] = DATE; save("iran", d); CH.append("iran")

# ---- united-states ----
d = load("united-states")
add_signal(d,
  "TRUMP SETS A SUNDAY (14 JUN) SIGNING DATE + CLAIMS KHAMENEI APPROVED (THIRD-HAND). Trump said the US-Iran deal 'will be signed on Sunday,' possibly in Europe, and that he 'understands' Supreme Leader Mojtaba Khamenei approved the MoU — attributing it to an INTERMEDIARY, not direct confirmation; Tehran has not corroborated. He rejected the competing Iranian draft as not reflecting 'agreed terms,' and called a Hormuz 'service fee' 'a beautiful thing.' The blockade stays 'in full force until finalized'; ceasefire largely held (no major new strikes 12-13 Jun). A US official holds signing odds at ~80%.",
  ["Fox/CBS", "houseofsaud/wire (Khamenei claim)", "Gulf News (Trump 'beautiful thing')", "CNBC"],
  "CLAIMED (Sunday signing, Khamenei approval); CONFIRMED (ceasefire held, blockade stays)")
trig_note(d, ["strike", "iran"], "note_2026-06-13",
  "STAYS active but HOLDING. No major new US strikes 12-13 Jun; the ceasefire largely held into the signing window. The blockade remains 'in full force until finalized,' so the trigger stays active, but kinetics have paused pending the deal.")
trig_note(d, ["kharg"], "note_2026-06-13",
  "STAYS WATCHING — probability low. De-escalation holding; window closes 15 Jun with no Kharg posture.")
d["last_updated"] = DATE; save("united-states", d); CH.append("united-states")

# ---- trump ----
d = load("trump")
add_signal(d,
  "TRUMP: DEAL 'SIGNED SUNDAY,' KHAMENEI 'APPROVED' (via intermediary), HORMUZ FEE 'A BEAUTIFUL THING.' Set a named Sunday signing date, claimed (third-hand) the Supreme Leader approved, rejected the competing Iranian draft, and endorsed a persistent Hormuz 'service fee.' Driving the optimistic timeline personally; met with skepticism (competing texts, unverified approval, enrichment unresolved). 9th 'deal close' claim of the war, now with a date.",
  ["Fox/CBS", "Gulf News", "CNBC", "houseofsaud/wire"],
  "CLAIMED (signing date, Khamenei approval); the statements are CONFIRMED")
d["last_updated"] = DATE; save("trump", d); CH.append("trump")

# ---- mojtaba-khamenei ----
d = load("mojtaba-khamenei")
add_signal(d,
  "THE 'KHAMENEI APPROVED' CLAIM IS THIRD-HAND AND HARD TO VERIFY. Trump says he 'understands' Mojtaba Khamenei approved the MoU — attributed to an INTERMEDIARY, not direct confirmation; Tehran has not corroborated. Structural problem: Khamenei (who took the role after Ali Khamenei's 28 Feb assassination) has been in HIDING since, communicating via COURIER with multi-day delays — making a real-time approval claim on the reported timeline implausible to confirm. The most load-bearing claim under a Sunday signing rests on the weakest verification in the dossier. Tag CLAIMED.",
  ["houseofsaud/wire", "background reporting on Khamenei comms"],
  "CLAIMED (Trump's intermediary attribution; Tehran unconfirmed)")
d["last_updated"] = DATE; save("mojtaba-khamenei", d); CH.append("mojtaba-khamenei")

# ---- nuclear-program ----
d = load("nuclear-program")
add_signal(d,
  "ENRICHMENT STILL UNRESOLVED — AND NOW A DOMESTIC IRANIAN FIGHT. The US holds 'zero enrichment'; Iran's draft is internally disputed — lawmaker Zohurian called the published text 'irresponsible' for implying enrichment recognition, while some reports say nuclear is DEFERRED to a separate follow-on track beyond the MoU. The near-term deal is signable precisely because it fuzzes/defers the nuclear core. The hardliner rejection is the tell the gap is real, not closed — the single biggest risk the 'final text' doesn't survive a signature.",
  ["Iran Intl (Zohurian)", "Bloomberg", "House of Commons Library", "NBC"],
  "CONFIRMED (positions); the contradiction is the open question")
d["last_updated"] = DATE; save("nuclear-program", d); CH.append("nuclear-program")

# ---- strait-of-hormuz ----
d = load("strait-of-hormuz")
add_signal(d,
  "DEAL WOULD REOPEN HORMUZ 'IMMEDIATELY WITHOUT TOLLS' (~30 DAYS TO PRE-WAR VOLUMES) — BUT IRAN KEEPS A 'SERVICE FEE' (~$1/BBL) AND NORMALIZATION IS SLOW (DEMINING). Araghchi: international law bars 'tolls' but Iran collects 'service fees' (the Persian Gulf Strait Authority's ~$1/bbl since 5 May), with compensation to Iran in the plan; Trump called the fee 'a beautiful thing.' A subsequent deal phase is DEMINING the waterway; analysts stress idled fields must restart and damaged facilities be repaired before flows normalize. So a signed deal ends the acute crisis but leaves a structurally HIGHER chokepoint cost-floor and a multi-week physical normalization — capping the oil downside.",
  ["The National (service fees)", "Gulf News (Trump)", "CNBC (demining)", "NBC"],
  "REPORTED (reopening terms); CONFIRMED (service-fee + demining caveats)")
bump_edges(d, [("brent-crude", "2026-06-13: A signed deal reopens Hormuz but normalization is slow (demining/restart) and Iran keeps a ~$1/bbl service fee — the oil downside is capped above the pre-war baseline.", None)])
trig_note(d, ["reopens to all traffic"], "note_2026-06-13",
  "STAYS WATCHING. A signed deal would reopen 'immediately without tolls' (~30 days to pre-war volumes) — but it is unsigned, Iran retains a 'service fee' role, and demining/restart delays actual normalization. Fires only on operationally-confirmed restored transit.")
d["last_updated"] = DATE; save("strait-of-hormuz", d); CH.append("strait-of-hormuz")

# ---- pakistan ----
d = load("pakistan")
add_signal(d,
  "Pakistan continues as the lead mediator finalizing 'next steps' on the reported draft; PM Sharif's 'final, agreed-upon text' claim (12 Jun) is now contested by competing Iranian drafts and Iran's 'preliminary' framing. The Naqvi/Munir channel underpins Pakistan's central role into the Sunday signing target.",
  ["NBC", "CBS"], "REPORTED")
d["last_updated"] = DATE; save("pakistan", d); CH.append("pakistan")

# ---- lebanon / israel / hezbollah ----
d = load("lebanon")
add_signal(d,
  "Lebanon is written into the reported deal as an END TO FIGHTING, and remains an Iranian CONDITION for lastingly ending the war with the US — but Israel (outside the talks) has repeatedly broken prior Lebanon ceasefires, making its commitment the clearest near-term obstacle to the deal holding even if signed. No specific new major Lebanon strike confirmed this window (gap).",
  ["NBC"], "REPORTED (deal term + Iranian condition)")
d["last_updated"] = DATE; save("lebanon", d); CH.append("lebanon")

d = load("israel")
add_signal(d,
  "Israel is the unresolved variable in the deal: the MoU's Lebanon end-of-fighting clause requires Israeli restraint it has repeatedly broken, and Israel remains outside the formal negotiations. No Israeli rejection of the framework surfaced, but no commitment to the Lebanon clause either; Israeli focus is on verification/enforcement of Iran's nuclear commitments. Israel-Iran axis stayed quiet (ceasefire held).",
  ["NBC", "Al Jazeera"], "REPORTED")
d["last_updated"] = DATE; save("israel", d); CH.append("israel")

d = load("hezbollah")
add_signal(d,
  "Subsumed into the reported Lebanon end-of-fighting clause; whether Israel honors it is the open question. No new Hezbollah action confirmed this window.",
  ["NBC"], "REPORTED (deal term)")
d["last_updated"] = DATE; save("hezbollah", d); CH.append("hezbollah")

# ---- market nodes: forward-note only, NO price change (markets closed) ----
d = load("brent-crude")
add_signal(d,
  "WEEKEND (markets closed) — Friday levels carry (Brent ~$87.33, -6% on the week). FORWARD: a Sunday signing extends the deflation but the DOWNSIDE IS CAPPED — Hormuz demining, idled-field restart, facility repairs and a persistent ~$1/bbl Iranian 'service fee' keep the floor structurally above the ~$73 pre-war baseline. Paper (Brent -6% wk) has run ahead of physical (VLCC/insurance never unwound). 'Sub-$85 sustained' watch: WTI $84.88 below, Brent $87.33 above — not crossed; Monday prices the signing.",
  ["market-data.py (Fri carried)", "CNBC (demining)", "The National (service fee)"],
  "CONFIRMED (Fri levels); forward-looking structural read")
trig_note(d, ["below $85"], "note_2026-06-13",
  "STAYS WATCHING (markets closed Sat). WTI $84.88 below $85, Brent $87.33 above — carried from Friday, not crossed/sustained. A Sunday signing could test it Monday; do not pre-fire.")
d["last_updated"] = DATE; save("brent-crude", d); CH.append("brent-crude")

d = load("marine-war-risk-insurance")
add_signal(d,
  "STILL NOT UNWOUND (~7-10% of hull) — the cleanest paper-vs-physical tell. Paper-oil fell ~6% on the week on deal hope, but Gulf war-risk cover and VLCC rates stay elevated because the blockade remains 'in full force until finalized' and no ship has transited a reopened strait. Re-rates DOWN only on a confirmed reopening — and even then lags by the demining/restart weeks. The physical complex is pricing the deal at far below the paper market's ~80% odds.",
  ["Lloyd's List", "CNBC", "markets.md F"], "REPORTED (market structure)")
d["last_updated"] = DATE; save("marine-war-risk-insurance", d); CH.append("marine-war-risk-insurance")

print("NODES UPDATED:", len(CH)); print(", ".join(CH))
