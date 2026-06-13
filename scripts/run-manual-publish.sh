#!/bin/bash
#
# run-manual-publish.sh — Publish step for manual-mode hive-mind pipeline
#
# Runs AFTER you've completed the LLM phases in interactive Claude
# (via run-manual.sh). Handles:
#   1. Verify the brief exists
#   2. git push (private repo — also functions as public mirror for hive-mind)
#   3. Telegram delivery via scripts/deliver-brief.py
#
# Usage:
#   EDITION=morning bash /Users/nimitmehra/Manus/hive-mind/scripts/run-manual-publish.sh
#   EDITION=evening bash /Users/nimitmehra/Manus/hive-mind/scripts/run-manual-publish.sh

set -u

DIR="/Users/nimitmehra/Manus/hive-mind"
DATE=$(date +%Y-%m-%d)

# Edition: env var override, else auto-detect by current hour
if [ -z "${EDITION:-}" ]; then
  HOUR=$(date +%H)
  if [ "$HOUR" -lt 13 ]; then EDITION="morning"; else EDITION="evening"; fi
fi

BRIEF_PATH="$DIR/briefs/$DATE-$EDITION.md"
LOG="$DIR/logs/manual-pipeline-$DATE-$EDITION.log"

cd "$DIR" || { echo "FATAL: cannot cd to $DIR"; exit 1; }

echo "===================================================================" | tee -a "$LOG"
echo "=== Manual publish (hive-mind) — $EDITION — $(date) ===" | tee -a "$LOG"
echo "===================================================================" | tee -a "$LOG"

# ----- 1. Verify brief exists ----------------------------------------------
if [ ! -f "$BRIEF_PATH" ]; then
  echo "FATAL: $BRIEF_PATH does not exist. Aborting publish." | tee -a "$LOG"
  exit 1
fi

SIZE=$(wc -c < "$BRIEF_PATH")
echo "  ✓ $BRIEF_PATH ($SIZE bytes)" | tee -a "$LOG"
echo

# ----- 2. Git push (hive-mind uses single repo for code + public viewer) ---
echo "--- git push ---" | tee -a "$LOG"
git add -A 2>&1 | tee -a "$LOG" >/dev/null
git commit -m "Brief $DATE $EDITION (manual)" 2>&1 | tee -a "$LOG" >/dev/null || echo "  (nothing to commit)" | tee -a "$LOG"
git push origin main 2>&1 | tee -a "$LOG" >/dev/null || echo "  (push failed — non-fatal; Telegram will still fire)" | tee -a "$LOG"
echo

# ----- 3. Telegram delivery ------------------------------------------------
echo "--- Telegram delivery ---" | tee -a "$LOG"
if [ -f "$DIR/scripts/deliver-brief.py" ]; then
  python3 "$DIR/scripts/deliver-brief.py" --date "$DATE" --edition "$EDITION" 2>&1 | tee -a "$LOG" >/dev/null || echo "  (Telegram delivery failed)" | tee -a "$LOG"
else
  echo "  (deliver-brief.py not found — skipping Telegram)" | tee -a "$LOG"
fi
echo

echo "===================================================================" | tee -a "$LOG"
echo "=== Manual publish complete at $(date) ===" | tee -a "$LOG"
echo "===================================================================" | tee -a "$LOG"
