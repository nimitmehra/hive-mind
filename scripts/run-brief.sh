#!/bin/bash
# Run the Hive Mind crisis brief pipeline
# Called by launchd at 12:00 noon IST daily (com.nimitmehra.hive-mind.brief.plist)
# Runs each step explicitly since headless mode can't chain sub-skills.
#
# v1.1 (2026-05-06) — hardening after May 6 silent Step-5 hang:
#   - gtimeout wraps every claude -p call so a single hang can't freeze the pipeline
#   - Per-step exit-code classification (FATAL aborts, WARN continues), mirroring
#     US-Stock-Tracker run-us-market-brief.sh v1.6 + NSE-Tracker run_daily_macos.sh v2.0
#   - Brief-existence guard before publish — we never push an empty commit
#   - All v1.0 log markers preserved byte-for-byte for verify-pipeline-run.sh
#   - NO `set -e` — each command runs regardless; explicit `||` per command
#
# v1.2 (2026-05-13) — retry-on-transient-transport-error:
#   - Anthropic API stream RST / idle-timeout closes (May 11 Step 1, May 13 Step 3)
#     present as rc=1 with recognizable error strings. These are transport-class
#     failures, not application-class — safe to retry because skills re-read
#     staging files and overwrite their outputs.
#   - update-graph rewrites tracked node/edge files in-place; a mid-stream RST
#     can leave partial writes (today: iran.json +65 lines, israel.json +4 lines
#     before the 12:44 close). Reset graph/ to HEAD before each retry attempt of
#     that step so retries start from the same clean baseline as attempt 1.
#   - gtimeout kills (rc=124), auth errors, and other non-transient rc≠0 stay
#     FATAL on attempt 1 — no behavior change for those.

CLAUDE="/Users/nimitmehra/.local/bin/claude"
DIR="/Users/nimitmehra/Manus/hive-mind"
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

# gtimeout (GNU coreutils) bounds every long-running subprocess. Installed via
# `brew install coreutils`. Same dependency US-Stock-Tracker + NSE-Tracker rely on.
TIMEOUT="/opt/homebrew/bin/gtimeout"

# Per-step wallclock caps (seconds). Sized at ~1.5x typical successful run.
# Today's run: gather-intel ~10min, gather-markets ~7min, update-graph ~33min,
# write-brief ~6min, verify-brief ~6min. Caps generous to avoid false-positive timeouts.
# 2026-05-09: bumped GRAPH_TIMEOUT 2700→3600 after high-volume day (4 proposed new
# nodes + 30+ existing-node updates) hit the cap at 46 min with all durable writes
# already on disk but the changelog write left undone. New cap = 80% headroom over
# typical 33-min run; old cap was 36% headroom.
INTEL_TIMEOUT=1800       # 30 min — /gather-intel
MARKETS_TIMEOUT=1800     # 30 min — /gather-markets
GRAPH_TIMEOUT=3600       # 60 min — /update-graph (typical 33 min, 2026-05-09 spike 46 min)
WRITE_TIMEOUT=2400       # 40 min — /write-brief
VERIFY_TIMEOUT=1800      # 30 min — /verify-brief
PUBLISH_TIMEOUT=300      # 5 min  — git add/commit/push + viewer rebuild
TELEGRAM_TIMEOUT=180     # 3 min  — Telegram delivery
KILL_GRACE=60            # 60s SIGTERM → SIGKILL grace per step

# Retry policy for transient transport-layer errors (v1.2).
# Worst-case wallclock per step = (MAX_RETRIES+1)*cap + MAX_RETRIES*RETRY_BACKOFF.
# For Step 3 at 3600s cap: 3*3600 + 2*30 = ~3h. Pipeline runs once daily at noon,
# so worst-case still finishes well before evening edition.
MAX_RETRIES=2
RETRY_BACKOFF=30

# Patterns matched (case-insensitive) against an attempt's combined stdout+stderr
# to classify rc≠0 as transient. Keep this list narrow — a broad match like
# bare "API Error" would mask non-retryable failures (auth, malformed prompt).
TRANSIENT_ERROR_PATTERNS=(
  "socket connection was closed unexpectedly"
  "Stream idle timeout"
  "ECONNRESET"
  "ETIMEDOUT"
  "Connection reset by peer"
  "502 Bad Gateway"
  "503 Service Unavailable"
  "504 Gateway Timeout"
)

# Echoes the first matched pattern to stdout, returns 0 on match / 1 on no match.
# Caller uses $(is_transient_error "$tmpfile") + [ -n "$matched" ].
is_transient_error() {
  local tmpfile="$1"
  local pattern
  for pattern in "${TRANSIENT_ERROR_PATTERNS[@]}"; do
    if grep -qi "$pattern" "$tmpfile"; then
      echo "$pattern"
      return 0
    fi
  done
  return 1
}

cd "$DIR" || {
  echo "$(date): FATAL — cannot cd to $DIR" >> /tmp/hive-mind-cron-fallback.log
  exit 1
}
mkdir -p "staging/$DATE-$EDITION" logs

# Pre-flight: gtimeout must exist. If missing, log and bail before burning cycles.
if [ ! -x "$TIMEOUT" ]; then
  echo "$(date): FATAL — $TIMEOUT not found. Run 'brew install coreutils'." >> "$LOG"
  exit 127
fi

echo "=== Pipeline started at $(date) | edition=$EDITION ===" >> "$LOG"

# Helper: run a Claude headless step under gtimeout with FATAL/WARN classification.
# Args: step_label, cap_seconds, claude_prompt
#
# Exit-code classification (v1.2):
#   rc=0   → success, return
#   rc=124 → gtimeout SIGTERM (wallclock exceeded), FATAL, no retry
#   rc≠0 with transient transport pattern in output → WARN, retry up to MAX_RETRIES
#   rc≠0 with no transient pattern → FATAL on first failure (auth, malformed, etc)
#   rc≠0 after MAX_RETRIES on transient pattern → FATAL
#
# Pre-retry cleanup: update-graph rewrites graph/ files in-place, so a mid-stream
# failure leaves partial writes that would compound on retry. Reset graph/ to HEAD
# before each retry attempt of that step. Other steps overwrite single output files
# cleanly, so no per-step cleanup needed.
run_claude_step() {
  local label="$1"
  local cap="$2"
  local prompt="$3"
  echo "--- $label ---" >> "$LOG"

  local attempt=0
  local max_attempts=$((MAX_RETRIES + 1))
  local rc=0
  local tmpfile
  local matched

  while [ $attempt -lt $max_attempts ]; do
    attempt=$((attempt + 1))

    if [ $attempt -gt 1 ]; then
      echo "  retry $((attempt - 1))/$MAX_RETRIES after ${RETRY_BACKOFF}s backoff..." >> "$LOG"
      case "$label" in
        *update-graph*)
          echo "  resetting graph/ to HEAD (discards partial node/edge writes)" >> "$LOG"
          git checkout HEAD -- graph/ >> "$LOG" 2>&1
          ;;
      esac
      sleep $RETRY_BACKOFF
    fi

    tmpfile=$(mktemp -t hivemind-step.XXXXXX)
    "$TIMEOUT" --kill-after=$KILL_GRACE "$cap" "$CLAUDE" -p "$prompt" $FLAGS > "$tmpfile" 2>&1
    rc=$?
    cat "$tmpfile" >> "$LOG"

    if [ $rc -eq 0 ]; then
      rm -f "$tmpfile"
      return 0
    fi

    if [ $rc -eq 124 ]; then
      rm -f "$tmpfile"
      echo "FATAL: $label exceeded ${cap}s wallclock; SIGTERM sent. Aborting." >> "$LOG"
      echo "=== Pipeline aborted at $(date) | reason=timeout step='$label' ===" >> "$LOG"
      exit 1
    fi

    matched=$(is_transient_error "$tmpfile")
    rm -f "$tmpfile"

    if [ -n "$matched" ] && [ $attempt -lt $max_attempts ]; then
      echo "  WARN: $label hit transient transport error ('$matched') on attempt $attempt of $max_attempts — will retry." >> "$LOG"
      continue
    fi

    if [ -n "$matched" ]; then
      echo "FATAL: $label exhausted $MAX_RETRIES retries on transient error ('$matched'). Aborting." >> "$LOG"
    else
      echo "FATAL: $label failed (exit $rc). Aborting — downstream depends on this output." >> "$LOG"
    fi
    echo "=== Pipeline aborted at $(date) | reason=exit-$rc step='$label' ===" >> "$LOG"
    exit 1
  done
}

# Steps 1-5: each is fatal-on-failure (downstream depends on staging artifacts)
run_claude_step "Step 1: gather-intel"   $INTEL_TIMEOUT   '/gather-intel'
run_claude_step "Step 2: gather-markets" $MARKETS_TIMEOUT '/gather-markets'
run_claude_step "Step 3: update-graph"   $GRAPH_TIMEOUT   '/update-graph'
run_claude_step "Step 4: write-brief"    $WRITE_TIMEOUT   '/write-brief'
run_claude_step "Step 5: verify-brief"   $VERIFY_TIMEOUT  '/verify-brief'

# Step 6: Publish (rebuild viewer + commit + push). Brief-existence guard ensures
# we never push an empty commit or fire Telegram against a missing brief.
echo "--- Step 6: publish ---" >> "$LOG"
BRIEF_PATH="briefs/$DATE-$EDITION.md"
if [ ! -f "$BRIEF_PATH" ]; then
  echo "FATAL: $BRIEF_PATH does not exist after Step 4 — aborting publish." >> "$LOG"
  echo "=== Pipeline aborted at $(date) | reason=missing-brief ===" >> "$LOG"
  exit 1
fi
echo "  ✓ $BRIEF_PATH exists ($(wc -c < "$BRIEF_PATH" | tr -d ' ') bytes)" >> "$LOG"

"$TIMEOUT" --kill-after=$KILL_GRACE $PUBLISH_TIMEOUT python3 scripts/rebuild-viewer.py >> "$LOG" 2>&1 \
  || echo "  WARN: rebuild-viewer.py failed (non-fatal — viewer may be stale)" >> "$LOG"

git add graph/ briefs/ viewer.html README.md >> "$LOG" 2>&1
git commit -m "Brief $DATE ($EDITION): automated daily pipeline run

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>" >> "$LOG" 2>&1 \
  || echo "  (nothing to commit — brief may already be in HEAD)" >> "$LOG"

if "$TIMEOUT" --kill-after=$KILL_GRACE $PUBLISH_TIMEOUT git push origin main >> "$LOG" 2>&1; then
  echo "  ✓ pushed to origin/main" >> "$LOG"
else
  echo "  ✗ git push failed (auth/network) — Telegram will still fire from local brief" >> "$LOG"
fi

# Step 7: Telegram delivery — runs independently of push success. Bounded to
# TELEGRAM_TIMEOUT so a hung Bot API call can't freeze the pipeline indefinitely.
echo "--- Step 7: telegram delivery ---" >> "$LOG"
"$TIMEOUT" --kill-after=$KILL_GRACE $TELEGRAM_TIMEOUT python3 scripts/deliver-brief.py --date "$DATE" --edition "$EDITION" >> "$LOG" 2>&1
TG_RC=$?
if [ $TG_RC -eq 0 ]; then
  echo "  ✓ Telegram message sent" >> "$LOG"
elif [ $TG_RC -eq 124 ]; then
  echo "  ✗ Telegram delivery timed out (>${TELEGRAM_TIMEOUT}s)" >> "$LOG"
else
  echo "  ✗ Telegram delivery failed (exit $TG_RC)" >> "$LOG"
fi

echo "=== Pipeline completed at $(date) ===" >> "$LOG"
