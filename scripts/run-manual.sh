#!/bin/bash
#
# run-manual.sh — Manual-mode hive-mind crisis brief pipeline
#
# Single-command end-to-end flow:
#   1. Edition detection + light setup (no Claude calls)
#   2. Open interactive Claude with orchestration prompt copied to clipboard
#   3. You paste the prompt, Claude runs /gather-intel → /gather-markets →
#      /update-graph → /write-brief → /verify-brief sequentially
#   4. When you exit Claude, auto-publish (git push + Telegram delivery)
#
# Interactive Claude usage draws from Max interactive rate limits, NOT the
# $200 programmatic credit (which is what claude -p consumes after 2026-06-15).
#
# Usage:
#   bash /Users/nimitmehra/Manus/hive-mind/scripts/run-manual.sh

set -u

DIR="/Users/nimitmehra/Manus/hive-mind"
CLAUDE="/Users/nimitmehra/.local/bin/claude"
DATE=$(date +%Y-%m-%d)

# Edition detection: <13:00 IST = morning, ≥13:00 IST = evening
HOUR=$(date +%H)
if [ "$HOUR" -lt 13 ]; then
  EDITION="morning"
else
  EDITION="evening"
fi

BRIEF_PATH="$DIR/briefs/$DATE-$EDITION.md"
LOG="$DIR/logs/manual-pipeline-$DATE-$EDITION.log"

cd "$DIR" || { echo "FATAL: cannot cd to $DIR"; exit 1; }
mkdir -p "$DIR/logs"

echo "===================================================================" | tee -a "$LOG"
echo "=== Manual hive-mind pipeline — started at $(date) ===" | tee -a "$LOG"
echo "=== Edition: $EDITION                                         ===" | tee -a "$LOG"
echo "===================================================================" | tee -a "$LOG"
echo

# ----- Copy orchestration prompt to clipboard ------------------------------
PROMPT="Run the hive-mind crisis brief pipeline end-to-end. Edition: $EDITION.
1. /gather-intel
2. /gather-markets
3. /update-graph
4. /write-brief
5. /verify-brief
Wait for each step to complete before the next.
When all done, report:
   - Final brief location ($BRIEF_PATH)
   - Verifier STATUS (PASS / FLAG / FAIL)
Then exit the session (/exit or Ctrl+D)."

if command -v pbcopy >/dev/null 2>&1; then
  printf '%s' "$PROMPT" | pbcopy
  CLIPBOARD_NOTE="The orchestration prompt has been COPIED TO YOUR CLIPBOARD. Hit ⌘V (or right-click → Paste) and then Enter."
else
  CLIPBOARD_NOTE="(pbcopy not available — copy the prompt below manually)"
fi

cat <<EOF | tee -a "$LOG"

===================================================================
=== Opening interactive Claude now.                              ===
===================================================================

$CLIPBOARD_NOTE

Prompt (for reference):
──────────────────────────────────────────────────────────────────
$PROMPT
──────────────────────────────────────────────────────────────────

Expected runtime: ~45-75 min for the full LLM pipeline.

When Claude reports done and you exit, this script will auto-publish:
git push + Telegram delivery via deliver-brief.py.

If something goes wrong and you exit before the brief lands, publish
will detect the missing brief and skip itself.

===================================================================

EOF

# ----- Open interactive Claude (NOT exec) ----------------------------------
"$CLAUDE"

# ----- Auto-publish after Claude exits -------------------------------------
echo | tee -a "$LOG"
echo "=== Claude session exited at $(date) ===" | tee -a "$LOG"
echo | tee -a "$LOG"

if [ -f "$BRIEF_PATH" ]; then
  echo "Brief found at $BRIEF_PATH — running publish step..." | tee -a "$LOG"
  echo | tee -a "$LOG"
  EDITION="$EDITION" bash "$DIR/scripts/run-manual-publish.sh"
else
  echo "Brief NOT found at $BRIEF_PATH — skipping publish." | tee -a "$LOG"
  echo "If Claude completed but the brief is elsewhere, run publish manually:" | tee -a "$LOG"
  echo "  EDITION=$EDITION bash $DIR/scripts/run-manual-publish.sh" | tee -a "$LOG"
fi

echo | tee -a "$LOG"
echo "===================================================================" | tee -a "$LOG"
echo "=== Manual pipeline complete at $(date) ===" | tee -a "$LOG"
echo "===================================================================" | tee -a "$LOG"
