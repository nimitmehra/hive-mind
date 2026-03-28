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
