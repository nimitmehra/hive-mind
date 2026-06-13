#!/usr/bin/env python3
"""
Graph update for 2026-06-07 (Sunday morning brief; covers 6 June US day -> 7 June IST).
Inputs: staging/2026-06-07-morning/intel.md + markets.md
Engineer: Graph. Respects verification tags. Trigger points need confirmed actions.

This script is the auditable record of every node change. Run once.
SUNDAY: cash & futures markets closed; Friday 5 June prints already encoded 2026-06-06
and are NOT re-encoded here. See payloads_2026_06_07.py header for the change set.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NODE_DIR = os.path.join(ROOT, "graph", "nodes")

TODAY = "2026-06-07"
NOTE_KEY = "note_" + TODAY
MULT = {1: 3.0, 2: 1.5, 3: 1.0}
changelog = []

def recalc(count, directness):
    return round(min(10.0, min(count, 20) * 1.0 * MULT.get(directness, 1.0)), 2)

def load(nid):
    with open(os.path.join(NODE_DIR, nid + ".json")) as f:
        return json.load(f)

def save(node):
    with open(os.path.join(NODE_DIR, node["id"] + ".json"), "w") as f:
        json.dump(node, f, ensure_ascii=False, indent=2)

def apply_node(nid, summary_prepend=None, signal=None, current=None, current_merge=None,
               snapshot=None, edge_bumps=None, new_edges=None,
               trigger_notes=None, trigger_status=None, new_triggers=None):
    node = load(nid)
    summary_changed = bool(summary_prepend)
    if summary_prepend:
        node["summary"] = summary_prepend.strip() + " " + node.get("summary", "")
    if signal:
        node.setdefault("recent_signals", []).insert(0, signal)
    if current is not None:
        node["current"] = current
    if current_merge:
        node.setdefault("current", {}).update(current_merge)
    if snapshot:
        node.setdefault("price_snapshots", []).insert(0, snapshot)
    edges_bumped = []
    for b in (edge_bumps or []):
        found = False
        for e in node.get("top_edges", []):
            if e.get("to") != b["to"]:
                continue
            if b.get("type_contains") and b["type_contains"] not in e.get("type", ""):
                continue
            e["activation_count"] = e.get("activation_count", 1) + 1
            if b.get("new_type"):
                e["type"] = b["new_type"]
            e["weight"] = recalc(e["activation_count"], e.get("directness", 1))
            e["last_activated"] = TODAY
            edges_bumped.append((b["to"], e["weight"], e["activation_count"]))
            found = True
            break
        if not found and b.get("create"):
            e = {"to": b["to"], "type": b.get("new_type", "linked"),
                 "weight": recalc(b.get("activation_count", 1), b.get("directness", 2)),
                 "directness": b.get("directness", 2), "last_activated": TODAY,
                 "activation_count": b.get("activation_count", 1)}
            node.setdefault("top_edges", []).append(e)
            edges_bumped.append((b["to"], e["weight"], e["activation_count"]))
        elif not found:
            raise SystemExit(f"EDGE BUMP MISS on {nid}: no edge to {b['to']} (type_contains={b.get('type_contains')})")
    for ne in (new_edges or []):
        e = {"to": ne["to"], "type": ne["type"],
             "weight": ne.get("weight", recalc(ne.get("activation_count", 1), ne.get("directness", 2))),
             "directness": ne.get("directness", 2), "last_activated": TODAY,
             "activation_count": ne.get("activation_count", 1)}
        node.setdefault("top_edges", []).append(e)
        edges_bumped.append((ne["to"], e["weight"], e["activation_count"]))
    for tn in (trigger_notes or []):
        hit = False
        for t in node.get("active_triggers", []):
            if tn["match"].lower() in t.get("condition", "").lower():
                t[NOTE_KEY] = tn["note"]; hit = True; break
        if not hit:
            raise SystemExit(f"TRIGGER NOTE MISS on {nid}: '{tn['match']}'")
    for ts in (trigger_status or []):
        hit = False
        for t in node.get("active_triggers", []):
            if ts["match"].lower() in t.get("condition", "").lower():
                t["status"] = ts["status"]
                if ts.get("note"): t[NOTE_KEY] = ts["note"]
                if ts.get("resolved"): t["resolved"] = TODAY
                hit = True; break
        if not hit:
            raise SystemExit(f"TRIGGER STATUS MISS on {nid}: '{ts['match']}'")
    for t in (new_triggers or []):
        node.setdefault("active_triggers", []).append(t)
    node["last_updated"] = TODAY
    save(node)
    changelog.append({"id": nid, "summary": summary_changed,
                      "signals": 1 if signal else 0, "edges": edges_bumped})
    return edges_bumped

from payloads_2026_06_07 import PAYLOADS  # noqa
for p in PAYLOADS:
    apply_node(**p)

# ---- report ----
print("Nodes updated:", len(changelog))
tot_sig = sum(c["signals"] for c in changelog)
tot_edge = sum(len(c["edges"]) for c in changelog)
print("Signals added:", tot_sig, "| Edge bumps/new:", tot_edge)
for c in changelog:
    e = ", ".join(f"{to}->{w}(x{n})" for to, w, n in c["edges"])
    print(f"  {c['id']:<22} sum={'Y' if c['summary'] else '-'} sig={c['signals']} edges=[{e}]")
