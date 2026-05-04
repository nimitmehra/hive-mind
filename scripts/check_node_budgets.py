#!/usr/bin/env python3
"""Validate every node JSON sits within the hot-tier token budget.

Per ARCHITECTURE_NODE_TIERING.md:
- Target: 1,500 tokens per node
- Operational tolerance: 2,000 tokens (warn, don't fail)
- Hard fail above 2,000 — node is too large, summary needs compression

Run as a pre-commit check or after any /update-graph run:
    python3 scripts/check_node_budgets.py
    python3 scripts/check_node_budgets.py --strict   # hard-fail at 1500
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NODES_DIR = ROOT / "graph" / "nodes"

TARGET = 1500
SOFT_LIMIT = 2000
BYTES_PER_TOKEN = 3.5


def estimate_tokens(path):
    """Estimate tokens by minified JSON length / chars-per-token.

    On-disk file uses indent=2 which adds ~30% whitespace overhead. We measure
    the underlying content (minified) so the metric matches the migration
    script and reflects what the LLM actually consumes when reading.
    """
    with open(path) as f:
        obj = json.load(f)
    minified = json.dumps(obj, ensure_ascii=False)
    return int(len(minified) / BYTES_PER_TOKEN)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true",
                        help="Hard-fail at TARGET (1500), not at SOFT_LIMIT (2000)")
    args = parser.parse_args()

    cap = TARGET if args.strict else SOFT_LIMIT
    label = "TARGET" if args.strict else "SOFT_LIMIT"

    over = []
    warn = []
    total = 0
    n_nodes = 0

    for path in sorted(NODES_DIR.glob("*.json")):
        tokens = estimate_tokens(path)
        total += tokens
        n_nodes += 1
        if tokens > cap:
            over.append((path.stem, tokens))
        elif tokens > TARGET:
            warn.append((path.stem, tokens))

    print(f"Checking {n_nodes} nodes against {label}={cap} tokens...")
    print(f"Total: {total:,} tokens ({total / n_nodes:.0f} avg)")

    if warn and not args.strict:
        print(f"\nWARNING: {len(warn)} nodes between {TARGET} and {SOFT_LIMIT}:")
        for name, t in warn:
            print(f"  {name}: {t} tokens")

    if over:
        print(f"\nFAIL: {len(over)} nodes over {label}={cap}:")
        for name, t in over:
            print(f"  {name}: {t} tokens")
        sys.exit(1)
    else:
        print(f"\nAll {n_nodes} nodes within {label}.")
        sys.exit(0)


if __name__ == "__main__":
    main()
