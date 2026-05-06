#!/bin/bash
# Run the Hive Mind crisis brief pipeline
# Called by cron at 8 AM and 5 PM IST daily
# Runs each step explicitly since headless mode can't chain sub-skills

CLAUDE="/Users/nimitmehra/.local/bin/claude"
DIR="/Users/nimitmehra/Documents/Manus/hive-mind"
FLAGS="--dangerously-skip-permissions"
DATE=$(date +%Y-%m-%d)
HOUR=$(date +%H)
# Edition detection: <13:00 IST = morning, >=13:00 IST = evening (matches /crisis-brief)
if [ "$HOUR" -lt 13 ]; then
  EDITION="morning"
else
  EDITION="evening"
fi
LOG="$DIR/logs/cron-$DATE.log"

cd "$DIR"
mkdir -p "staging/$DATE-$EDITION" logs

echo "=== Pipeline started at $(date) | edition=$EDITION ===" >> "$LOG"

# Step 1: Gather Intelligence
echo "--- Step 1: gather-intel ---" >> "$LOG"
$CLAUDE -p '/gather-intel' $FLAGS >> "$LOG" 2>&1

# Step 2: Gather Markets
echo "--- Step 2: gather-markets ---" >> "$LOG"
$CLAUDE -p '/gather-markets' $FLAGS >> "$LOG" 2>&1

# Step 3: Update Graph
echo "--- Step 3: update-graph ---" >> "$LOG"
$CLAUDE -p '/update-graph' $FLAGS >> "$LOG" 2>&1

# Step 4: Write Brief
echo "--- Step 4: write-brief ---" >> "$LOG"
$CLAUDE -p '/write-brief' $FLAGS >> "$LOG" 2>&1

# Step 5: Verify Brief
echo "--- Step 5: verify-brief ---" >> "$LOG"
$CLAUDE -p '/verify-brief' $FLAGS >> "$LOG" 2>&1

# Step 6: Rebuild viewer and push to GitHub
echo "--- Step 6: publish ---" >> "$LOG"
python3 scripts/rebuild-viewer.py >> "$LOG" 2>&1
git add graph/ briefs/ viewer.html README.md >> "$LOG" 2>&1
git commit -m "Brief $DATE ($EDITION): automated daily pipeline run

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>" >> "$LOG" 2>&1

if git push origin main >> "$LOG" 2>&1; then
  echo "  ✓ pushed to origin/main" >> "$LOG"
else
  echo "  ✗ git push failed (auth/network) — Telegram will still fire from local brief" >> "$LOG"
fi

# Step 7: Telegram delivery — runs independently of push success
echo "--- Step 7: telegram delivery ---" >> "$LOG"
if [ -f "briefs/$DATE-$EDITION.md" ]; then
  python3 scripts/deliver-brief.py --date "$DATE" --edition "$EDITION" >> "$LOG" 2>&1
  if [ $? -eq 0 ]; then
    echo "  ✓ Telegram message sent" >> "$LOG"
  else
    echo "  ✗ Telegram delivery failed (see above)" >> "$LOG"
  fi
else
  echo "  (skip — brief file not found at briefs/$DATE-$EDITION.md)" >> "$LOG"
fi

echo "=== Pipeline completed at $(date) ===" >> "$LOG"
