#!/usr/bin/env python3
"""Sync edges.json from node top_edges activated 2026-05-30, then refresh meta.json.
Idempotent: re-running only re-applies the same TODAY values."""
import json, os, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NODE_DIR = os.path.join(ROOT, "graph", "nodes")
EDGES_FILE = os.path.join(ROOT, "graph", "edges.json")
META_FILE = os.path.join(ROOT, "graph", "meta.json")
TODAY = "2026-05-30"

# Load all nodes
nodes = {}
for fp in glob.glob(os.path.join(NODE_DIR, "*.json")):
    with open(fp) as f:
        n = json.load(f)
    nodes[n["id"]] = n

with open(EDGES_FILE) as f:
    ej = json.load(f)
edges = ej["edges"]

# Index existing edges by (from,to) -> list of entries
from collections import defaultdict
idx = defaultdict(list)
for e in edges:
    idx[(e["from"], e["to"])].append(e)

updated, added = 0, 0
for nid, node in nodes.items():
    for te in node.get("top_edges", []):
        if te.get("last_activated") != TODAY:
            continue
        key = (nid, te["to"])
        if idx[key]:
            e = idx[key][0]  # update the primary entry for this directed pair
            e["weight"] = te["weight"]
            e["last_activated"] = TODAY
            e["directness"] = te.get("directness", e.get("directness", 1))
            if te.get("type"):
                e["type"] = te["type"]
            updated += 1
        else:
            e = {"from": nid, "to": te["to"], "weight": te["weight"],
                 "directness": te.get("directness", 2), "last_activated": TODAY,
                 "type": te.get("type", "linked")}
            edges.append(e)
            idx[key].append(e)
            added += 1

ej["edges"] = edges
ej["last_updated"] = TODAY
with open(EDGES_FILE, "w") as f:
    json.dump(ej, f, ensure_ascii=False, indent=2)

# meta.json
with open(META_FILE) as f:
    meta = json.load(f)
type_counts = defaultdict(int)
for n in nodes.values():
    type_counts[n.get("type", "unknown")] += 1
meta["last_updated"] = TODAY
meta["total_nodes"] = len(nodes)
meta["total_edges"] = len(edges)
meta["briefs_generated"] = meta.get("briefs_generated", 0) + 1
meta["node_types"] = dict(sorted(type_counts.items()))
with open(META_FILE, "w") as f:
    json.dump(meta, f, ensure_ascii=False, indent=2)

print(f"edges.json: updated {updated}, added {added}, total {len(edges)}")
print(f"meta.json: nodes={meta['total_nodes']} edges={meta['total_edges']} briefs={meta['briefs_generated']}")
print("node_types:", meta["node_types"])
