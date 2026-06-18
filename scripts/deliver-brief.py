#!/usr/bin/env python3
"""
deliver-brief.py — Deliver hive-mind morning/evening brief via Telegram.

Called by run-brief.sh after the brief is published. Reads the brief at
briefs/{date}-{edition}.md, composes a phone-readable summary, posts to
Telegram via the Bot API. Mirrors the NSE-Tracker pattern.

Usage:
    python3 scripts/deliver-brief.py --date 2026-05-05 --edition morning
    python3 scripts/deliver-brief.py --date 2026-05-05 --edition morning --dry-run

Credentials read from project root (each on its own line, both gitignored):
    telegram_bot_token.txt   — Telegram bot API token (from @BotFather)
    telegram_chat_id.txt     — Recipient chat_id (numeric)

Exit codes:
    0 = sent (or dry-run)
    1 = brief missing or send failed
    2 = credentials missing
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


REPO = Path("/Users/nimitmehra/Manus/hive-mind")
TELEGRAM_TOKEN_FILE = REPO / "telegram_bot_token.txt"
TELEGRAM_CHAT_ID_FILE = REPO / "telegram_chat_id.txt"
IMESSAGE_RECIPIENT_FILE = REPO / "imessage_recipient.txt"

GITHUB_BRIEF_URL_TEMPLATE = (
    "https://github.com/nimitmehra/hive-mind/blob/main/briefs/{date}-{edition}.md"
)
GITHUB_VIEWER_URL = "https://nimitmehra.github.io/hive-mind/viewer.html"

TELEGRAM_API_BASE = "https://api.telegram.org/bot"
SUMMARY_MAX_LEN = 3500  # Telegram per-message limit is 4096; leave headroom


def read_credential(path: Path) -> str | None:
    if not path.exists():
        return None
    val = path.read_text().strip()
    return val if val else None


def parse_brief(text: str) -> dict:
    """Extract editor's note + lead headline + first paragraph + sections."""
    out = {
        "title": "",
        "editors_note": "",
        "lead_headline": "",
        "lead_paragraph": "",
        "section_list": [],
        "graph_footer": "",
    }

    m = re.search(r"^# (.+)$", text, re.MULTILINE)
    if m:
        out["title"] = m.group(1).strip()

    # Editor's note: paragraph starting with **Editor's note.**
    m = re.search(
        r"\*\*Editor's note\.\*\*\s+([\s\S]+?)(?=\n\n---|\n##)", text
    )
    if m:
        out["editors_note"] = re.sub(r"\s+", " ", m.group(1)).strip()

    # Lead from Section I — first ### headline and its paragraph
    m = re.search(
        r"## I\. What Happened\s*\n+### (.+?)\n+([\s\S]+?)(?=\n###|\n##|\Z)",
        text,
    )
    if m:
        out["lead_headline"] = re.sub(r"\s*\[(NEW|UPDATED).*?\]\s*", "", m.group(1)).strip()
        para = re.sub(r"\s+", " ", m.group(2)).strip()
        out["lead_paragraph"] = para

    out["section_list"] = re.findall(r"^## (.+)$", text, re.MULTILINE)

    # Graph footer line
    m = re.search(r"\*Graph updated:\s*([^\*]+)\*", text)
    if m:
        out["graph_footer"] = re.sub(r"\s+", " ", m.group(1)).strip()

    return out


def compose_telegram_summary(parsed: dict, date: str, edition: str) -> str:
    lines = []
    edition_label = edition.capitalize()

    lines.append(f"*Hive-Mind Crisis Brief — {date} ({edition_label})*")
    lines.append("")

    if parsed["editors_note"]:
        note = parsed["editors_note"]
        if len(note) > 700:
            note = note[:700].rsplit(" ", 1)[0] + "…"
        lines.append("*Editor's note*")
        lines.append(note)
        lines.append("")

    if parsed["lead_headline"]:
        lines.append(f"*Lead:* {parsed['lead_headline']}")
        para = parsed["lead_paragraph"]
        if len(para) > 600:
            para = para[:600].rsplit(" ", 1)[0] + "…"
        lines.append(para)
        lines.append("")

    if parsed["section_list"]:
        sections_shown = parsed["section_list"][:6]
        lines.append(f"*Sections:* {' · '.join(sections_shown)}")
        lines.append("")

    github_url = GITHUB_BRIEF_URL_TEMPLATE.format(date=date, edition=edition)
    lines.append(f"📄 Full brief: {github_url}")
    lines.append(f"🕸 Graph viewer: {GITHUB_VIEWER_URL}")

    if parsed["graph_footer"]:
        lines.append("")
        footer = parsed["graph_footer"]
        if len(footer) > 300:
            footer = footer[:300].rsplit(" ", 1)[0] + "…"
        lines.append(f"_{footer}_")

    out = "\n".join(lines)
    if len(out) > SUMMARY_MAX_LEN:
        out = (
            out[:SUMMARY_MAX_LEN].rsplit(" ", 1)[0]
            + "…\n\n_(summary truncated; full brief on GitHub)_"
        )
    return out


def send_telegram_message(token: str, chat_id: str, text: str, dry_run: bool) -> dict:
    """POST to Telegram. Try Markdown first, fall back to plain on parser error."""
    if dry_run:
        return {
            "channel": "telegram",
            "status": "dry_run",
            "would_send_chars": len(text),
            "preview": text,
        }

    url = f"{TELEGRAM_API_BASE}{token}/sendMessage"

    def post(payload: dict) -> tuple[int, dict]:
        data = urlencode(payload).encode()
        try:
            req = Request(url, data=data, method="POST")
            with urlopen(req, timeout=30) as resp:
                return resp.status, json.loads(resp.read().decode())
        except HTTPError as e:
            try:
                err = json.loads(e.read().decode())
            except Exception:
                err = {"description": str(e)}
            return e.code, err
        except Exception as e:
            # Network error / timeout — return a sentinel so the channel fails
            # gracefully instead of crashing the whole run (and other channels).
            return 0, {"description": f"network error: {e}"}

    status, body = post({"chat_id": chat_id, "text": text, "parse_mode": "Markdown"})
    if status == 200 and body.get("ok"):
        return {
            "channel": "telegram",
            "status": "sent",
            "message_id": body["result"]["message_id"],
            "sent_at": datetime.now(timezone.utc).isoformat(),
            "parse_mode": "Markdown",
        }

    plain = text
    for marker in ("**", "*", "__", "_", "`"):
        plain = plain.replace(marker, "")
    status2, body2 = post({"chat_id": chat_id, "text": plain})
    if status2 == 200 and body2.get("ok"):
        return {
            "channel": "telegram",
            "status": "sent_plain",
            "message_id": body2["result"]["message_id"],
            "sent_at": datetime.now(timezone.utc).isoformat(),
            "markdown_error": body.get("description"),
        }

    return {
        "channel": "telegram",
        "status": "failed",
        "error": f"markdown={body.get('description')} | plain={body2.get('description')}",
    }


def send_telegram_document(
    token: str, chat_id: str, file_path: Path, caption: str, dry_run: bool
) -> dict:
    """Send the full brief as a markdown document via Telegram (multipart upload via curl)."""
    if dry_run:
        return {
            "channel": "telegram_document",
            "status": "dry_run",
            "would_send": str(file_path),
        }
    if not file_path.exists():
        return {
            "channel": "telegram_document",
            "status": "failed",
            "error": f"file missing: {file_path}",
        }

    url = f"{TELEGRAM_API_BASE}{token}/sendDocument"
    cmd = [
        "curl", "-s", "-X", "POST", url,
        "-F", f"chat_id={chat_id}",
        "-F", f"document=@{file_path}",
        "-F", f"caption={caption[:1024]}",
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        body = json.loads(result.stdout) if result.stdout else {}
        if not body.get("ok"):
            return {
                "channel": "telegram_document",
                "status": "failed",
                "error": body.get("description", result.stderr[:200] or "no body"),
            }
        return {
            "channel": "telegram_document",
            "status": "sent",
            "message_id": body["result"]["message_id"],
            "sent_at": datetime.now(timezone.utc).isoformat(),
        }
    except subprocess.TimeoutExpired:
        return {"channel": "telegram_document", "status": "failed", "error": "timeout"}
    except Exception as e:
        return {
            "channel": "telegram_document",
            "status": "failed",
            "error": f"unexpected: {e}",
        }


def strip_markdown(text: str) -> str:
    """Remove Telegram/Markdown markers so the text reads cleanly in Messages."""
    text = text.replace("`", "")
    # Asterisks are only ever emphasis markers here (never in our URLs) → strip all.
    text = text.replace("*", "")
    # Underscores: unwrap _emphasis_ only when the span contains a space, so
    # URL slugs / file paths with underscores are left intact.
    text = re.sub(r"_([^_]*\s[^_]*)_", r"\1", text)
    return text


def compose_imessage_summary(parsed: dict, date: str, edition: str) -> str:
    """Plain-text summary for iMessage (no Markdown; links render tappable)."""
    full = compose_telegram_summary(parsed, date, edition)
    return strip_markdown(full)


def send_imessage(recipient: str, text: str, dry_run: bool) -> dict:
    """Send via macOS Messages.app over iMessage using osascript (AppleScript)."""
    if dry_run:
        return {
            "channel": "imessage",
            "status": "dry_run",
            "recipient": recipient,
            "would_send_chars": len(text),
            "preview": text,
        }

    # AppleScript: send `text` to `recipient` over the iMessage service.
    script = (
        'on run {targetHandle, msgText}\n'
        '    tell application "Messages"\n'
        '        set targetService to 1st account whose service type = iMessage\n'
        '        set targetBuddy to participant targetHandle of targetService\n'
        '        send msgText to targetBuddy\n'
        '    end tell\n'
        'end run'
    )
    try:
        result = subprocess.run(
            ["osascript", "-", recipient, text],
            input=script,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode == 0:
            return {
                "channel": "imessage",
                "status": "sent",
                "recipient": recipient,
                "sent_at": datetime.now(timezone.utc).isoformat(),
            }
        return {
            "channel": "imessage",
            "status": "failed",
            "recipient": recipient,
            "error": (result.stderr or "osascript nonzero exit").strip()[:300],
        }
    except subprocess.TimeoutExpired:
        return {"channel": "imessage", "status": "failed", "error": "timeout"}
    except FileNotFoundError:
        return {"channel": "imessage", "status": "failed", "error": "osascript not found (not macOS?)"}
    except Exception as e:
        return {"channel": "imessage", "status": "failed", "error": f"unexpected: {e}"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True, help="YYYY-MM-DD")
    ap.add_argument("--edition", choices=["morning", "evening"], default="morning")
    ap.add_argument(
        "--channel",
        choices=["telegram", "imessage", "both"],
        default="both",
        help="Delivery channel(s). Each is skipped gracefully if its credentials are missing.",
    )
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    brief_path = REPO / f"briefs/{args.date}-{args.edition}.md"
    if not brief_path.exists():
        print(f"ERROR: brief not found at {brief_path}", file=sys.stderr)
        return 1

    text = brief_path.read_text()
    parsed = parse_brief(text)

    want_tg = args.channel in ("telegram", "both")
    want_im = args.channel in ("imessage", "both")
    results = []

    # --- Telegram channel ---
    if want_tg:
        token = read_credential(TELEGRAM_TOKEN_FILE)
        chat_id = read_credential(TELEGRAM_CHAT_ID_FILE)
        if not token or not chat_id:
            print(
                "WARN: skipping Telegram — missing telegram_bot_token.txt or "
                f"telegram_chat_id.txt at {REPO}",
                file=sys.stderr,
            )
        else:
            summary = compose_telegram_summary(parsed, args.date, args.edition)
            msg_result = send_telegram_message(token, chat_id, summary, args.dry_run)
            print(json.dumps(msg_result, indent=2))
            results.append(msg_result)
            doc_caption = (
                f"Hive-Mind Crisis Brief — {args.date} ({args.edition.capitalize()})"
            )
            doc_result = send_telegram_document(
                token, chat_id, brief_path, doc_caption, args.dry_run
            )
            print(json.dumps(doc_result, indent=2))
            results.append(doc_result)

    # --- iMessage (Apple Messages) channel ---
    if want_im:
        recipient = read_credential(IMESSAGE_RECIPIENT_FILE)
        if not recipient:
            print(
                "WARN: skipping iMessage — missing imessage_recipient.txt at "
                f"{REPO} (put your phone number, e.g. +919004031732)",
                file=sys.stderr,
            )
        else:
            im_summary = compose_imessage_summary(parsed, args.date, args.edition)
            im_result = send_imessage(recipient, im_summary, args.dry_run)
            print(json.dumps(im_result, indent=2))
            results.append(im_result)

    # Write delivery receipt for audit (records all attempted channels)
    log_dir = REPO / f"staging/{args.date}-{args.edition}"
    log_dir.mkdir(parents=True, exist_ok=True)
    receipt = {
        "date": args.date,
        "edition": args.edition,
        "channel": args.channel,
        "results": results,
    }
    (log_dir / "delivery-log.json").write_text(json.dumps(receipt, indent=2))

    if not results:
        print("ERROR: no channels attempted (all credentials missing)", file=sys.stderr)
        return 2

    # Exit 0 if any channel succeeded; 1 if all attempted channels failed
    success_states = ("sent", "sent_plain", "dry_run")
    if any(r.get("status") in success_states for r in results):
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
