#!/usr/bin/env python3
"""
Rebuild viewer.html by re-embedding graph data from graph/ directory.
Run after updating any node, edge, or meta file.
Usage: python3 scripts/rebuild-viewer.py
"""
import json, os, glob, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NODE_DIR = os.path.join(ROOT, "graph", "nodes")
EDGES_FILE = os.path.join(ROOT, "graph", "edges.json")
META_FILE = os.path.join(ROOT, "graph", "meta.json")
VIEWER_FILE = os.path.join(ROOT, "viewer.html")

# Load nodes
nodes = {}
for fp in sorted(glob.glob(os.path.join(NODE_DIR, "*.json"))):
    with open(fp) as f:
        node = json.load(f)
    nodes[node["id"]] = node

# Load edges and meta
with open(EDGES_FILE) as f:
    edges = json.load(f)
with open(META_FILE) as f:
    meta = json.load(f)

# Build data JSON
data_json = json.dumps({"nodes": nodes, "edges": edges, "meta": meta}, indent=2)

# Read viewer.html
with open(VIEWER_FILE, "r") as f:
    html = f.read()

# Replace the data block between markers
pattern = r'const GRAPH_DATA = \{[\s\S]*?\};\s*\n\s*// ={3,} END GRAPH DATA'
replacement = f'const GRAPH_DATA = {data_json};\n\n// ============ END GRAPH DATA'
html_new = re.sub(pattern, lambda m: replacement, html)

if html_new == html:
    print("WARNING: Pattern not matched. Viewer may not have been updated.")
else:
    with open(VIEWER_FILE, "w") as f:
        f.write(html_new)
    print(f"viewer.html updated: {len(nodes)} nodes, {len(edges['edges'])} edges, {os.path.getsize(VIEWER_FILE)/1024:.1f} KB")

# --- Auto-update README.md stats ---
README_FILE = os.path.join(ROOT, "README.md")
if os.path.exists(README_FILE):
    with open(README_FILE, "r") as f:
        readme = f.read()

    # Build node type listings from actual data
    type_groups = {}
    for node in nodes.values():
        ntype = node.get("type", "other")
        type_groups.setdefault(ntype, []).append(node["name"])
    for t in type_groups:
        type_groups[t].sort()

    type_labels = {
        "country": "Countries",
        "commodity": "Commodities",
        "institution": "Institutions",
        "index": "Indices",
        "trade_route": "Trade Routes",
        "sector": "Sectors",
        "person": "Persons"
    }

    # Build the node types block
    node_lines = []
    for tkey in ["country", "commodity", "institution", "index", "trade_route", "sector", "person"]:
        if tkey in type_groups:
            label = type_labels.get(tkey, tkey.title())
            names = ", ".join(type_groups[tkey])
            node_lines.append(f"- **{label}** ({len(type_groups[tkey])}): {names}")

    node_block = "\n".join(node_lines)
    total_nodes = len(nodes)
    total_edges = len(edges['edges'])

    # Replace the stats line
    readme = re.sub(
        r'The graph currently tracks \*\*\d+ nodes\*\* across \d+ types and \*\*\d+ weighted edges\*\*',
        f'The graph currently tracks **{total_nodes} nodes** across {len(type_groups)} types and **{total_edges} weighted edges**',
        readme
    )

    # Replace the node types block
    readme = re.sub(
        r'### Node Types\n(- \*\*(?:Countries|Commodities|Institutions|Indices|Trade Routes|Sectors|Persons)\*\*.*\n)+',
        f'### Node Types\n{node_block}\n',
        readme
    )

    with open(README_FILE, "w") as f:
        f.write(readme)
    print(f"README.md updated: {total_nodes} nodes, {total_edges} edges")
