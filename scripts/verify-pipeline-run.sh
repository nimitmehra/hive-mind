#!/bin/bash
# verify-pipeline-run.sh — post-hoc verification of a hive-mind cron pipeline run
#
# Run this after a scheduled or manual run to confirm every step landed cleanly.
# Designed in response to the 2026-05-06 silent-Step-5 incident: today's pipeline
# wrote brief + verification but never logged "Pipeline completed", never ran
# Step 6 (publish) or Step 7 (Telegram). A check like this would have flagged
# the divergence within minutes instead of hours.
#
# Usage:
#   ./scripts/verify-pipeline-run.sh                          # today, edition auto-detected from clock
#   ./scripts/verify-pipeline-run.sh 2026-05-06               # specific date, edition auto-detected
#   ./scripts/verify-pipeline-run.sh 2026-05-06 morning       # specific date + edition
#
# Exit codes: 0 = clean (PASS or PASS+WARN); 1 = at least one FAIL.

DIR="/Users/nimitmehra/Manus/hive-mind"
DATE="${1:-$(date +%Y-%m-%d)}"

# Edition: explicit arg wins; otherwise infer from clock (matches run-brief.sh logic)
if [ -n "$2" ]; then
  EDITION="$2"
else
  HOUR=$(date +%H)
  if [ "$HOUR" -lt 13 ]; then EDITION="morning"; else EDITION="evening"; fi
fi

LOG="$DIR/logs/cron-$DATE.log"
BRIEF="$DIR/briefs/$DATE-$EDITION.md"
VERIFICATION="$DIR/briefs/$DATE-$EDITION-verification.md"
STAGING="$DIR/staging/$DATE-$EDITION"

cd "$DIR" || { echo "FATAL: cannot cd to $DIR"; exit 1; }

PASS=0; FAIL=0; WARN=0

check() {
  local label="$1"; local outcome="$2"; local detail="$3"
  case "$outcome" in
    pass) echo "  ✓ $label${detail:+ — $detail}"; PASS=$((PASS+1)) ;;
    fail) echo "  ✗ $label${detail:+ — $detail}"; FAIL=$((FAIL+1)) ;;
    warn) echo "  ! $label${detail:+ — $detail}"; WARN=$((WARN+1)) ;;
  esac
}

echo "=================================================================="
echo "=== hive-mind pipeline verification — $DATE $EDITION ==="
echo "=================================================================="
echo ""

# === 1. Pipeline execution ===
echo "1. Pipeline execution:"
if [ -f "$LOG" ]; then
  check "log file exists" pass "$(wc -l <"$LOG" | tr -d ' ') lines"
  if grep -q "=== Pipeline started at" "$LOG"; then
    check "start banner present" pass
  else
    check "start banner missing" fail "log present but no start banner"
  fi
  if grep -q "=== Pipeline completed at" "$LOG"; then
    check "completion banner present" pass
  elif grep -q "=== Pipeline aborted at" "$LOG"; then
    reason=$(grep "=== Pipeline aborted at" "$LOG" | head -1 | grep -oE "reason=[^ ]+")
    check "pipeline aborted explicitly" warn "$reason"
  else
    check "completion banner missing" fail "pipeline started but never logged completion (silent hang or kill)"
  fi
  if grep -q "^FATAL:" "$LOG"; then
    fatal_count=$(grep -c "^FATAL:" "$LOG")
    check "FATAL lines in log" fail "$fatal_count found"
  else
    check "no FATAL lines" pass
  fi
else
  check "log file exists" fail "no $LOG — cron may not have fired"
fi
echo ""

# === 2. All 5 Claude steps emitted their step markers ===
echo "2. Claude step markers:"
if [ -f "$LOG" ]; then
  for step in "Step 1: gather-intel" "Step 2: gather-markets" "Step 3: update-graph" "Step 4: write-brief" "Step 5: verify-brief"; do
    if grep -q "^--- $step ---" "$LOG"; then
      check "$step marker present" pass
    else
      check "$step marker missing" fail "step skipped or pipeline aborted before reaching it"
    fi
  done
fi
echo ""

# === 3. Staging artifacts (Steps 1-3 outputs) ===
echo "3. Staging artifacts ($STAGING):"
for artifact in intel.md markets.md graph-changelog.md; do
  if [ -f "$STAGING/$artifact" ]; then
    size=$(wc -c <"$STAGING/$artifact" | tr -d ' ')
    check "$artifact exists" pass "$size bytes"
  else
    check "$artifact missing" fail "Step producing it did not complete"
  fi
done
echo ""

# === 4. Brief + verification ===
echo "4. Brief artifacts:"
if [ -f "$BRIEF" ]; then
  size=$(wc -c <"$BRIEF" | tr -d ' ')
  check "$(basename "$BRIEF") exists" pass "$size bytes"
else
  check "$(basename "$BRIEF") missing" fail "Step 4 (write-brief) did not produce a file"
fi

if [ -f "$VERIFICATION" ]; then
  size=$(wc -c <"$VERIFICATION" | tr -d ' ')
  check "$(basename "$VERIFICATION") exists" pass "$size bytes"
  # Verdict: extract just the "Verdict: APPROVED ..." segment up to the first
  # sentence-ending period. Verifications often pack the verdict mid-paragraph,
  # so we -oE the verdict span itself rather than the whole line.
  verdict=$(grep -m1 -oiE "verdict:?[*[:space:]]*(approved|rejected)[^.]*" "$VERIFICATION" | head -c 120 | sed 's/[*#]//g' | sed 's/^ *//')
  if [ -n "$verdict" ]; then
    if echo "$verdict" | grep -qi "rejected"; then
      check "verification verdict" warn "$verdict"
    else
      check "verification verdict" pass "$verdict"
    fi
  else
    check "verification verdict line not parseable" warn
  fi
else
  check "$(basename "$VERIFICATION") missing" fail "Step 5 (verify-brief) did not produce a file"
fi
echo ""

# === 5. Step 6 publish: brief-guard, viewer, commit, push ===
echo "5. Step 6 publish:"
if [ -f "$LOG" ]; then
  if grep -q "^--- Step 6: publish ---" "$LOG"; then
    check "Step 6 marker present" pass
    if grep -q "✓ pushed to origin/main" "$LOG"; then
      check "git push succeeded" pass
    elif grep -q "git push failed" "$LOG"; then
      check "git push failed" warn "Telegram should still have fired"
    else
      check "git push outcome unclear" warn "neither success nor explicit failure logged"
    fi
  else
    check "Step 6 marker missing" fail "publish step never started (today's failure mode)"
  fi
fi
echo ""

# === 6. Step 7 Telegram delivery ===
echo "6. Step 7 Telegram delivery:"
if [ -f "$LOG" ]; then
  if grep -q "^--- Step 7: telegram delivery ---" "$LOG"; then
    check "Step 7 marker present" pass
    if grep -q "✓ Telegram message sent" "$LOG"; then
      check "Telegram delivery succeeded" pass
    elif grep -q "Telegram delivery (failed|timed out)" "$LOG"; then
      check "Telegram delivery failed" fail
    else
      check "Telegram delivery outcome unclear" warn
    fi
  else
    check "Step 7 marker missing" fail "Telegram delivery never started"
  fi
fi
echo ""

# === 7. Git state (catches commits that never reached origin) ===
echo "7. Git state:"
unpushed=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo "?")
if [ "$unpushed" = "0" ]; then
  check "HEAD == origin/main" pass
elif [ "$unpushed" = "?" ]; then
  check "cannot determine origin/main state" warn "fetch may be needed"
else
  check "$unpushed local commit(s) ahead of origin/main" fail "publish step did not push"
fi

# Today's brief should be the HEAD commit (or at least in the last 5)
if git log -5 --pretty=format:"%s" 2>/dev/null | grep -q "Brief $DATE.*$EDITION"; then
  check "brief commit found in recent HEAD" pass
else
  check "no commit for $DATE $EDITION in last 5 HEADs" warn "brief may not be committed"
fi
echo ""

# === Summary ===
echo "=================================================================="
echo "=== Summary: $PASS passed | $FAIL failed | $WARN warnings ==="
echo "=================================================================="

if [ "$FAIL" -gt 0 ]; then
  echo ""
  echo "Investigate failures above. Log: $LOG"
  exit 1
elif [ "$WARN" -gt 0 ]; then
  echo ""
  echo "Pipeline completed with warnings. Review above."
  exit 0
else
  echo ""
  echo "Clean run. All checks passed."
  exit 0
fi
