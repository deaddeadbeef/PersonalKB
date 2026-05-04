#!/usr/bin/env python3
"""Operational monitor for the PersonalKB curation daemon."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "_ops" / "reports"
AUDIT_SUMMARY = REPORT_DIR / "audit-summary.json"
MONITOR_JSON = REPORT_DIR / "monitor-summary.json"
MONITOR_MD = REPORT_DIR / "monitor-summary.md"
MISSION_FILE = ROOT / "_ops" / "engineer-daemon-mission.md"
PILOT_FILE = REPORT_DIR / "cs-data-structures-pilot.md"

PROTECTED_DIR_NAMES = {".git", ".obsidian", "_raw", "_chunks", "_templates"}
PROTECTED_EXTENSIONS = {
    ".gif",
    ".jpeg",
    ".jpg",
    ".m4a",
    ".mp3",
    ".mp4",
    ".png",
    ".wav",
    ".webp",
}


@dataclass(frozen=True)
class DirtyFile:
    code: str
    path: str


def run_git(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return result.stdout.strip()


def git_branch() -> str:
    branch = run_git(["branch", "--show-current"])
    return branch or "(detached)"


def git_dirty_files() -> list[DirtyFile]:
    output = run_git(["status", "--porcelain=v1"])
    dirty: list[DirtyFile] = []
    for line in output.splitlines():
        if not line:
            continue
        code = line[:2]
        path = line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        dirty.append(DirtyFile(code=code, path=path.strip('"')))
    return dirty


def path_parts(path: str) -> set[str]:
    return {part for part in re.split(r"[\\/]+", path) if part}


def is_protected_path(path: str) -> bool:
    parts = path_parts(path)
    if parts.intersection(PROTECTED_DIR_NAMES):
        return True
    return Path(path).suffix.lower() in PROTECTED_EXTENSIONS


def load_audit_summary() -> dict[str, Any] | None:
    if not AUDIT_SUMMARY.exists():
        return None
    return json.loads(AUDIT_SUMMARY.read_text(encoding="utf-8"))


def run_audit() -> dict[str, Any]:
    result = subprocess.run(
        ["python", "_ops/personal_kb.py", "audit"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return json.loads(result.stdout)


def parse_pilot_budget() -> dict[str, Any]:
    if not PILOT_FILE.exists():
        return {"exists": False}

    text = PILOT_FILE.read_text(encoding="utf-8")
    used_match = re.search(r"Cycle 1 used (\d+) of the (\d+) pilot wiki-note edits", text)
    status_match = re.search(r"^Status: (.+?)\.$", text, flags=re.MULTILINE)
    changed_notes = re.findall(r"^- `CS Data Structures/.+?\.md`$", text, flags=re.MULTILINE)

    return {
        "exists": True,
        "status": status_match.group(1) if status_match else "unknown",
        "used": int(used_match.group(1)) if used_match else len(changed_notes),
        "limit": int(used_match.group(2)) if used_match else 10,
    }


def audit_age_hours(summary: dict[str, Any] | None, now: datetime) -> float | None:
    if not summary or "generated_at" not in summary:
        return None
    generated = datetime.fromisoformat(str(summary["generated_at"]))
    return round((now - generated).total_seconds() / 3600, 2)


def build_monitor(run_fresh_audit: bool) -> dict[str, Any]:
    now = datetime.now()
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    audit = run_audit() if run_fresh_audit else load_audit_summary()
    dirty = git_dirty_files()
    protected_dirty = [item for item in dirty if is_protected_path(item.path)]
    pilot = parse_pilot_budget()

    warnings: list[str] = []
    blockers: list[str] = []

    if not MISSION_FILE.exists():
        blockers.append("Missing _ops/engineer-daemon-mission.md")
    if audit is None:
        blockers.append("Missing _ops/reports/audit-summary.json; run python _ops/personal_kb.py audit")
    if protected_dirty:
        blockers.append("Protected-path changes are present in git status")
    if dirty:
        warnings.append("Working tree has uncommitted files; avoid unrelated changes")

    age = audit_age_hours(audit, now)
    if age is None:
        warnings.append("Audit age is unknown")
    elif age > 24:
        warnings.append(f"Audit report is {age} hours old; refresh before curation")

    if pilot.get("exists") and pilot.get("used", 0) >= pilot.get("limit", 10):
        warnings.append("CS Data Structures pilot budget is exhausted; use the human review gate")

    status = "ok"
    if warnings:
        status = "attention"
    if blockers:
        status = "blocked"

    return {
        "generated_at": now.isoformat(timespec="seconds"),
        "root": str(ROOT),
        "status": status,
        "branch": git_branch(),
        "mission_file": MISSION_FILE.relative_to(ROOT).as_posix(),
        "audit_age_hours": age,
        "audit": audit,
        "git": {
            "dirty_count": len(dirty),
            "dirty_files": [item.__dict__ for item in dirty],
            "protected_dirty_count": len(protected_dirty),
            "protected_dirty_files": [item.__dict__ for item in protected_dirty],
        },
        "pilot": pilot,
        "warnings": warnings,
        "blockers": blockers,
        "recommended_next_actions": recommended_next_actions(status, warnings, blockers),
    }


def recommended_next_actions(status: str, warnings: list[str], blockers: list[str]) -> list[str]:
    if blockers:
        return [
            "Stop daemon curation until blockers are resolved.",
            "Review protected-path or missing-artifact issues before editing wiki notes.",
        ]
    if status == "attention":
        actions = ["Proceed only with a bounded scope that avoids dirty files."]
        if any("Audit report" in warning for warning in warnings):
            actions.insert(0, "Refresh audit with python _ops/personal_kb.py audit.")
        return actions
    return ["Proceed with the next bounded mission cycle."]


def write_reports(report: dict[str, Any]) -> None:
    MONITOR_JSON.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    MONITOR_MD.write_text(render_markdown(report), encoding="utf-8")


def render_markdown(report: dict[str, Any]) -> str:
    audit = report.get("audit") or {}
    git = report["git"]
    pilot = report["pilot"]

    lines = [
        "# PersonalKB Monitor Summary",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"Status: **{report['status']}**",
        f"Branch: `{report['branch']}`",
        f"Audit age: `{report['audit_age_hours']}` hours",
        "",
        "## Git",
        "",
        f"- Dirty files: {git['dirty_count']}",
        f"- Protected dirty files: {git['protected_dirty_count']}",
    ]

    if git["dirty_files"]:
        lines.extend(["", "### Dirty Files", ""])
        for item in git["dirty_files"]:
            lines.append(f"- `{item['code']}` `{item['path']}`")

    lines.extend(
        [
            "",
            "## Audit",
            "",
            f"- Candidate articles: {audit.get('candidate_articles', 'unknown')}",
            f"- Empty notes: {audit.get('empty_notes', 'unknown')}",
            f"- Stubs under 1500 bytes: {audit.get('stubs_under_1500_bytes', 'unknown')}",
            f"- Missing `up`: {audit.get('missing_up', 'unknown')}",
            f"- Missing `confidence`: {audit.get('missing_confidence', 'unknown')}",
            f"- Missing references: {audit.get('missing_references', 'unknown')}",
            f"- Placeholder hits: {audit.get('placeholder_hits', 'unknown')}",
            f"- Broken link occurrences: {audit.get('broken_link_occurrences', 'unknown')}",
            f"- Orphan articles: {audit.get('orphan_articles', 'unknown')}",
            "",
            "## Pilot",
            "",
            f"- Exists: {pilot.get('exists')}",
            f"- Status: {pilot.get('status', 'unknown')}",
            f"- Budget: {pilot.get('used', 'unknown')} / {pilot.get('limit', 'unknown')}",
            "",
            "## Warnings",
            "",
        ]
    )

    if report["warnings"]:
        lines.extend(f"- {warning}" for warning in report["warnings"])
    else:
        lines.append("- None")

    lines.extend(["", "## Blockers", ""])
    if report["blockers"]:
        lines.extend(f"- {blocker}" for blocker in report["blockers"])
    else:
        lines.append("- None")

    lines.extend(["", "## Recommended Next Actions", ""])
    lines.extend(f"- {action}" for action in report["recommended_next_actions"])

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-audit", action="store_true", help="refresh audit reports before monitoring")
    parser.add_argument("--strict", action="store_true", help="return non-zero for attention or blocked status")
    args = parser.parse_args()

    report = build_monitor(run_fresh_audit=args.run_audit)
    write_reports(report)
    print(json.dumps(report, indent=2, ensure_ascii=False))

    if args.strict and report["status"] == "blocked":
        return 2
    if args.strict and report["status"] == "attention":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
