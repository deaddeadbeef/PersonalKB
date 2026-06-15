---
tags: [study, llm, mastery, gaps, triage, audit, local-llm, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
---

# LLM Mastery Gap Triage Runner

> **One-line summary** When the mastery audit shows many holds or failures, this runner ranks the gaps and chooses the next concrete academic or local-inference proof route.

Use this after [[LLM/Study/LLM Mastery Evidence Audit Runner|LLM Mastery Evidence Audit Runner]] when the output has too many incomplete gates to act on by inspection. It also accepts rows from [[LLM/Study/LLM Recall and Remediation Audit Runner|LLM Recall and Remediation Audit Runner]], [[LLM/Study/LLM Paper Oral Defense Runner|LLM Paper Oral Defense Runner]], local inference runners, or a hand-written capstone workbook export if the rows use status, domain, route, and next-action fields.

This runner does not decide that mastery is complete. It decides what to do next.

## What This Proves

| Gate | Evidence checked | Why it matters |
|---|---|---|
| Gap inventory | incomplete rows from mastery, recall, paper, and local-run audits | prevents a large workbook from becoming a vague backlog |
| Priority | status, criticality, required flag, domain, route quality, proof state, and override score | keeps local endpoint and academic fundamentals from being buried |
| Next route | each top gap has an Obsidian route or evidence path | turns hold/fail status into a concrete next note |
| Next action | each top gap states the next study, lab, retest, or evidence capture | avoids another reading-only session |
| Domain balance | academic, mechanism, local-inference, system, and exam gaps are summarized | keeps applied hosting and academic mastery coupled |

## Manifest Shape

Minimum manifest pointing at a mastery audit output:

```json
{
  "run_id": "llm-gap-triage-001",
  "run_root": "D:/llm-runs/gap-triage",
  "vault_root": "D:/Vaults/PersonalKB",
  "top_n": 10,
  "sources": [
    "D:/llm-runs/mastery-audit/llm-mastery-audit-001/llm-mastery-audit-001-mastery-audit.json"
  ]
}
```

Inline rows also work:

```json
{
  "run_id": "manual-gap-triage-001",
  "vault_root": "D:/Vaults/PersonalKB",
  "rows": [
    {
      "gate_id": "local-endpoint",
      "domain": "local-inference",
      "status": "hold",
      "required": true,
      "critical": true,
      "proof": "",
      "next_route": "LLM/Study/Local LLM First Endpoint Run Sheet",
      "next_action": "Run the first loopback endpoint proof and save the response artifacts.",
      "pass_signal": "Endpoint response, model id, route, timing, and boundary evidence are saved."
    }
  ]
}
```

## Accepted Fields

| Field family | Accepted keys |
|---|---|
| Gap id | `gate_id`, `gap_id`, `id`, `row_id`, `answer_id`, `case_id` |
| Domain | `domain`, `area`, `category`, `cluster` |
| Status | `status`, `state`, `result`, `decision_status` |
| Critical flag | `critical`, `is_critical`, `hard_fail`, `hard_fail_domain` |
| Required flag | `required`, `is_required`, `must_pass` |
| Proof | `proof`, `proof_path`, `evidence`, `artifact`, `answer_artifact` |
| Proof exists | `proof_exists`, `artifact_exists`, `answer_artifact_exists`, `route_exists` |
| Next route | `next_route`, `route`, `follow_up_route`, `proof_route`, `local_proof_route` |
| Next action | `next_action`, `action`, `remediation`, `todo` |
| Pass signal | `pass_signal`, `success_criteria`, `completion_signal` |
| Owner | `failure_owner`, `owner`, `remediation_owner` |
| Effort | `effort`, `estimated_effort`, `size` |
| Priority override | `priority_override`, `priority`, `manual_priority` |
| Blocker | `blocked_by`, `blocker`, `dependency` |

## Standard-Library Runner

Save this as `llm_mastery_gap_triage_runner.py` inside the run folder. It uses only Python's standard library.

```python
from __future__ import annotations

import csv
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path
from typing import Any


LINK_OPEN = "[" + "["
LINK_CLOSE = "]" + "]"

FIELD_GROUPS = {
    "gap_id": ("gate_id", "gap_id", "id", "row_id", "answer_id", "case_id"),
    "domain": ("domain", "area", "category", "cluster"),
    "status": ("status", "state", "result", "decision_status"),
    "critical": ("critical", "is_critical", "hard_fail", "hard_fail_domain"),
    "required": ("required", "is_required", "must_pass"),
    "proof": ("proof", "proof_path", "evidence", "artifact", "answer_artifact"),
    "proof_exists": ("proof_exists", "artifact_exists", "answer_artifact_exists", "route_exists"),
    "next_route": ("next_route", "route", "follow_up_route", "proof_route", "local_proof_route"),
    "next_action": ("next_action", "action", "remediation", "todo"),
    "pass_signal": ("pass_signal", "success_criteria", "completion_signal"),
    "owner": ("failure_owner", "owner", "remediation_owner"),
    "effort": ("effort", "estimated_effort", "size"),
    "priority_override": ("priority_override", "priority", "manual_priority"),
    "blocked_by": ("blocked_by", "blocker", "dependency"),
}

STATUS_RANK = {"fail": 0, "hold": 1, "pass": 2, "waived": 3}
STATUS_WEIGHT = {"fail": 80, "hold": 45, "pass": 0, "waived": 0}
DOMAIN_WEIGHT = {
    "local-inference": 45,
    "academic": 40,
    "mechanism": 35,
    "system": 30,
    "exam": 25,
    "evaluation": 25,
    "rag": 25,
    "tools": 20,
    "unspecified": 10,
}
EFFORT_PENALTY = {
    "tiny": 0,
    "small": 0,
    "low": 0,
    "medium": 5,
    "moderate": 5,
    "large": 10,
    "hard": 10,
    "high": 10,
}


def utc_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def slugify(value: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return text or "llm-mastery-gap-triage"


def norm(value: Any) -> str:
    return str(value or "").strip().lower()


def md_cell(value: Any) -> str:
    return str(value or "").replace("\n", "<br>").replace("|", "\\|")


def list_value(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, tuple):
        return list(value)
    if isinstance(value, str):
        return [part.strip() for part in re.split(r"[;,]", value) if part.strip()]
    return [value]


def bool_value(value: Any, default: bool = False) -> bool:
    if value is None or value == "":
        return default
    if isinstance(value, bool):
        return value
    text = norm(value)
    if text in {"1", "true", "yes", "y", "pass", "required", "critical"}:
        return True
    if text in {"0", "false", "no", "n", "waived", "optional"}:
        return False
    return default


def numeric_value(value: Any, default: float = 0.0) -> float:
    if value in (None, ""):
        return default
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def first_value(row: dict[str, Any], family: str) -> Any:
    for key in FIELD_GROUPS[family]:
        if key in row and row[key] not in (None, ""):
            return row[key]
    return None


def first_text(row: dict[str, Any], family: str) -> str:
    value = first_value(row, family)
    if value is None:
        return ""
    return str(value).strip()


def status_value(value: Any) -> str:
    text = norm(value).replace("_", "-")
    if text in {"pass", "passed", "ready", "complete", "accepted", "green"}:
        return "pass"
    if text in {"fail", "failed", "rejected", "unsafe", "red", "error"}:
        return "fail"
    if text in {"waive", "waived", "skipped", "out-of-scope", "out of scope"}:
        return "waived"
    return "hold"


def clean_link(value: str) -> str:
    text = str(value or "").strip().strip('"').strip("'")
    if text.startswith(LINK_OPEN) and text.endswith(LINK_CLOSE):
        text = text[2:-2]
    if "|" in text:
        text = text.split("|", 1)[0]
    if "#" in text:
        text = text.split("#", 1)[0]
    return text.strip()


def path_candidates(raw: str, vault_root: Path) -> list[Path]:
    cleaned = clean_link(raw)
    if not cleaned:
        return []

    candidate = Path(cleaned)
    candidates: list[Path] = []
    if candidate.is_absolute():
        candidates.append(candidate)
        if candidate.suffix == "":
            candidates.append(candidate.with_suffix(".md"))
    else:
        candidates.append(vault_root / cleaned)
        if candidate.suffix == "":
            candidates.append(vault_root / f"{cleaned}.md")
        windows_cleaned = cleaned.replace("/", "\\")
        candidates.append(vault_root / windows_cleaned)
        if candidate.suffix == "":
            candidates.append(vault_root / f"{windows_cleaned}.md")

    unique: list[Path] = []
    seen: set[str] = set()
    for item in candidates:
        key = str(item)
        if key not in seen:
            unique.append(item)
            seen.add(key)
    return unique


def resolve_path(raw: str, vault_root: Path) -> tuple[str, bool]:
    candidates = path_candidates(raw, vault_root)
    for candidate in candidates:
        if candidate.exists():
            return str(candidate), True
    return (str(candidates[0]) if candidates else "", False)


def load_json_or_csv(path: Path) -> Any:
    if path.suffix.lower() == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return list(csv.DictReader(handle))
    return json.loads(path.read_text(encoding="utf-8"))


def extract_rows(payload: Any, source: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if isinstance(payload, list):
        iterable = payload
    elif isinstance(payload, dict):
        iterable = []
        for key in ("gates", "rows", "items", "gaps", "answers", "findings"):
            value = payload.get(key)
            if isinstance(value, list):
                iterable = value
                break
        if not iterable and isinstance(payload.get("record"), dict):
            return extract_rows(payload["record"], source)
    else:
        return rows

    for index, item in enumerate(iterable, 1):
        if isinstance(item, dict):
            row = dict(item)
            row.setdefault("_source", source)
            row.setdefault("_source_index", index)
            rows.append(row)
    return rows


def load_manifest() -> tuple[dict[str, Any], Path | None]:
    manifest_env = os.environ.get("LLM_MASTERY_GAP_TRIAGE_MANIFEST", "")
    if not manifest_env:
        return {}, None
    manifest_path = Path(manifest_env)
    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("Manifest must be a JSON object.")
    return payload, manifest_path


def load_input_rows(manifest: dict[str, Any], manifest_path: Path | None) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []

    inline_rows = extract_rows(manifest, str(manifest_path or "manifest"))
    rows.extend(inline_rows)

    source_values: list[Any] = []
    source_values.extend(list_value(manifest.get("sources")))
    source_values.extend(list_value(manifest.get("inputs")))
    input_env = os.environ.get("LLM_MASTERY_GAP_TRIAGE_INPUT", "")
    source_values.extend(list_value(input_env))

    for raw in source_values:
        source_path = Path(str(raw))
        payload = load_json_or_csv(source_path)
        rows.extend(extract_rows(payload, str(source_path)))

    return rows


def source_label(row: dict[str, Any]) -> str:
    source = str(row.get("_source") or "")
    if not source:
        return "manifest"
    try:
        return Path(source).name
    except OSError:
        return source


def domain_value(row: dict[str, Any]) -> str:
    domain = norm(first_text(row, "domain"))
    if not domain:
        return "unspecified"
    if "local" in domain or domain in {"inference", "endpoint", "serving"}:
        return "local-inference"
    if "academic" in domain or "paper" in domain:
        return "academic"
    if "rag" in domain or "retrieval" in domain:
        return "rag"
    if "tool" in domain or "structured" in domain:
        return "tools"
    if "eval" in domain or "quality" in domain or "judge" in domain:
        return "evaluation"
    return domain


def effort_penalty(row: dict[str, Any]) -> int:
    effort = norm(first_text(row, "effort"))
    if effort in EFFORT_PENALTY:
        return EFFORT_PENALTY[effort]
    if effort:
        return int(min(max(numeric_value(effort, 0), 0), 20))
    return 0


def priority_band(score: float) -> str:
    if score >= 140:
        return "P0"
    if score >= 105:
        return "P1"
    if score >= 70:
        return "P2"
    return "P3"


def route_quality(route: str, vault_root: Path) -> tuple[str, bool]:
    if not route:
        return "", False
    return resolve_path(route, vault_root)


def evaluate_gap(row: dict[str, Any], vault_root: Path) -> dict[str, Any]:
    gap_id = first_text(row, "gap_id") or f"gap-{row.get('_source_index', 0)}"
    domain = domain_value(row)
    status = status_value(first_value(row, "status"))
    critical = bool_value(first_value(row, "critical"), False)
    required = bool_value(first_value(row, "required"), True)
    proof = first_text(row, "proof")
    next_route = first_text(row, "next_route")
    next_action = first_text(row, "next_action")
    pass_signal = first_text(row, "pass_signal")
    owner = first_text(row, "owner") or domain
    blocked_by = first_text(row, "blocked_by")
    priority_override = numeric_value(first_value(row, "priority_override"), 0)

    proof_exists_value = first_value(row, "proof_exists")
    if proof_exists_value is None:
        proof_resolved, proof_exists = resolve_path(proof, vault_root) if proof else ("", False)
    else:
        proof_resolved, proof_exists = (proof, bool_value(proof_exists_value, False))

    route_resolved, route_exists = route_quality(next_route, vault_root)

    missing_route = status != "pass" and not next_route
    missing_action = status != "pass" and not next_action
    route_unresolved = bool(next_route) and not route_exists

    score = (
        STATUS_WEIGHT[status]
        + DOMAIN_WEIGHT.get(domain, DOMAIN_WEIGHT["unspecified"])
        + (35 if critical else 0)
        + (20 if required else 0)
        + (12 if missing_route else 0)
        + (12 if missing_action else 0)
        + (8 if route_unresolved else 0)
        + (8 if proof and not proof_exists else 0)
        + priority_override
        - effort_penalty(row)
    )

    if "endpoint" in gap_id or "runtime" in gap_id or "model" in gap_id:
        score += 8
    if "paper" in gap_id or domain == "academic":
        score += 5

    actionable = status != "pass" and bool(next_route) and bool(next_action)
    triage_status = "ready" if actionable else "needs-route" if missing_route else "needs-action" if missing_action else "passed"
    if route_unresolved:
        triage_status = "route-unresolved"

    return {
        "gap_id": gap_id,
        "domain": domain,
        "source": source_label(row),
        "status": status,
        "critical": critical,
        "required": required,
        "owner": owner,
        "score": round(score, 2),
        "priority_band": priority_band(score),
        "triage_status": triage_status,
        "proof": proof,
        "proof_resolved": proof_resolved,
        "proof_exists": proof_exists,
        "next_route": next_route,
        "next_route_resolved": route_resolved,
        "next_route_exists": route_exists,
        "next_action": next_action,
        "pass_signal": pass_signal,
        "blocked_by": blocked_by,
    }


def domain_summary(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    domains = sorted({row["domain"] for row in rows})
    summary: list[dict[str, Any]] = []
    for domain in domains:
        subset = [row for row in rows if row["domain"] == domain]
        summary.append({
            "domain": domain,
            "gap_count": len(subset),
            "fail_count": sum(1 for row in subset if row["status"] == "fail"),
            "hold_count": sum(1 for row in subset if row["status"] == "hold"),
            "critical_count": sum(1 for row in subset if row["critical"]),
            "top_score": max((row["score"] for row in subset), default=0),
            "top_gap": subset[0]["gap_id"] if subset else "",
        })
    summary.sort(key=lambda row: (-row["top_score"], row["domain"]))
    return summary


def csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = [
        "priority_band",
        "score",
        "gap_id",
        "domain",
        "status",
        "critical",
        "required",
        "triage_status",
        "owner",
        "next_route",
        "next_action",
        "pass_signal",
        "source",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def render_markdown(record: dict[str, Any]) -> str:
    lines = [
        f"# LLM Mastery Gap Triage - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Input rows: `{record['input_row_count']}`",
        f"- Ranked gaps: `{record['gap_count']}`",
        f"- Top gap: `{record['top_gap_id']}`",
        f"- Top route: `{record['top_next_route']}`",
        "",
        "## Next Action",
        "",
        record["top_next_action"] or "No incomplete gap needs action.",
        "",
        "## Ranked Gaps",
        "",
        "| Priority | Score | Gap | Domain | Status | Owner | Route | Next action |",
        "|---|---:|---|---|---|---|---|---|",
    ]
    for row in record["ranked_gaps"]:
        lines.append("| " + " | ".join([
            md_cell(row["priority_band"]),
            str(row["score"]),
            md_cell(row["gap_id"]),
            md_cell(row["domain"]),
            md_cell(row["status"]),
            md_cell(row["owner"]),
            md_cell(row["next_route"]),
            md_cell(row["next_action"]),
        ]) + " |")

    lines.extend([
        "",
        "## Domain Summary",
        "",
        "| Domain | Gaps | Fail | Hold | Critical | Top gap |",
        "|---|---:|---:|---:|---:|---|",
    ])
    for row in record["domains"]:
        lines.append("| " + " | ".join([
            md_cell(row["domain"]),
            str(row["gap_count"]),
            str(row["fail_count"]),
            str(row["hold_count"]),
            str(row["critical_count"]),
            md_cell(row["top_gap"]),
        ]) + " |")

    lines.extend(["", "## Triage Findings", ""])
    if record["triage_findings"]:
        for item in record["triage_findings"]:
            lines.append(f"- `{item['level']}` `{item['gap_id']}`: {item['message']} Next: {item['action']}")
    else:
        lines.append("- Top-ranked gaps have next routes and next actions.")

    return "\n".join(lines) + "\n"


def triage_finding(level: str, gap_id: str, message: str, action: str) -> dict[str, str]:
    return {"level": level, "gap_id": gap_id, "message": message, "action": action}


def main() -> int:
    manifest, manifest_path = load_manifest()
    run_id = str(manifest.get("run_id") or (manifest_path.stem if manifest_path else "llm-mastery-gap-triage")).strip()
    run_root_value = os.environ.get("LLM_MASTERY_GAP_TRIAGE_RUN_ROOT") or manifest.get("run_root", "llm-mastery-gap-triage-runs")
    vault_root_value = os.environ.get("LLM_MASTERY_GAP_TRIAGE_VAULT_ROOT") or manifest.get("vault_root", ".")
    top_n = int(numeric_value(manifest.get("top_n"), 10))
    include_passed = bool_value(manifest.get("include_passed"), False)
    run_root = Path(str(run_root_value))
    vault_root = Path(str(vault_root_value))
    run_dir = run_root / slugify(run_id)
    run_dir.mkdir(parents=True, exist_ok=True)
    run_root.mkdir(parents=True, exist_ok=True)

    input_rows = load_input_rows(manifest, manifest_path)
    evaluated = [evaluate_gap(row, vault_root) for row in input_rows]
    gaps = [row for row in evaluated if include_passed or row["status"] not in {"pass", "waived"}]
    gaps.sort(key=lambda row: (-row["score"], STATUS_RANK.get(row["status"], 9), row["domain"], row["gap_id"]))
    ranked = gaps[:top_n]

    findings: list[dict[str, str]] = []
    if not input_rows:
        findings.append(triage_finding("hold", "input", "No input rows were provided.", "Point sources or LLM_MASTERY_GAP_TRIAGE_INPUT at a mastery audit JSON/CSV."))
    for row in ranked[:3]:
        if row["status"] != "pass" and not row["next_route"]:
            findings.append(triage_finding("hold", row["gap_id"], "Top gap has no next route.", "Add next_route or route before using this triage as a daily plan."))
        elif row["status"] != "pass" and not row["next_route_exists"]:
            findings.append(triage_finding("hold", row["gap_id"], "Top gap next route does not resolve.", "Fix the route or create the missing note."))
        if row["status"] != "pass" and not row["next_action"]:
            findings.append(triage_finding("hold", row["gap_id"], "Top gap has no next action.", "Write the next concrete study, lab, retest, or evidence-capture action."))

    top = ranked[0] if ranked else {}
    if not input_rows:
        status = "hold"
        decision = "gap_triage_needs_input"
    elif findings:
        status = "hold"
        decision = "gap_triage_incomplete"
    else:
        status = "pass"
        decision = "gap_triage_ready" if ranked else "no_gaps_found"

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "manifest_path": str(manifest_path or ""),
        "vault_root": str(vault_root),
        "input_row_count": len(input_rows),
        "gap_count": len(gaps),
        "top_n": top_n,
        "top_gap_id": top.get("gap_id", ""),
        "top_next_route": top.get("next_route", ""),
        "top_next_action": top.get("next_action", ""),
        "ranked_gaps": ranked,
        "domains": domain_summary(gaps),
        "triage_findings": findings,
        "outputs": {},
    }

    json_path = run_dir / f"{slugify(run_id)}-gap-triage.json"
    markdown_path = run_dir / f"{slugify(run_id)}-gap-triage.md"
    csv_path = run_dir / f"{slugify(run_id)}-gap-triage.csv"
    jsonl_path = run_root / "llm-mastery-gap-triage-runs.jsonl"
    record["outputs"] = {
        "json": str(json_path),
        "markdown": str(markdown_path),
        "csv": str(csv_path),
        "jsonl": str(jsonl_path),
    }

    csv_write(csv_path, ranked)
    json_path.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    markdown_path.write_text(render_markdown(record), encoding="utf-8")
    with jsonl_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(json.dumps({
        "status": status,
        "decision": decision,
        "run_id": run_id,
        "input_row_count": len(input_rows),
        "gap_count": len(gaps),
        "top_gap_id": record["top_gap_id"],
        "top_next_route": record["top_next_route"],
        "output_dir": str(run_dir),
    }, indent=2))
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(json.dumps({"status": "error", "decision": "runner_exception", "error": str(exc)}, indent=2), file=sys.stderr)
        raise SystemExit(3)
```

## PowerShell Run

```powershell
$env:LLM_MASTERY_GAP_TRIAGE_MANIFEST = "D:\llm-runs\gap-triage\gap-triage-manifest.json"
$env:LLM_MASTERY_GAP_TRIAGE_VAULT_ROOT = "D:\Vaults\PersonalKB"
$env:LLM_MASTERY_GAP_TRIAGE_RUN_ROOT = "D:\llm-runs\gap-triage"
python .\llm_mastery_gap_triage_runner.py
```

Or point directly at a mastery audit JSON:

```powershell
$env:LLM_MASTERY_GAP_TRIAGE_INPUT = "D:\llm-runs\mastery-audit\latest\llm-mastery-audit.json"
$env:LLM_MASTERY_GAP_TRIAGE_VAULT_ROOT = "D:\Vaults\PersonalKB"
python .\llm_mastery_gap_triage_runner.py
```

## Reading The Result

| Runner status | Meaning | Next route |
|---|---|---|
| `pass/gap_triage_ready` | the top-ranked gaps have next routes and next actions | do the top action, then rerun the source audit |
| `pass/no_gaps_found` | the input contains no hold/fail rows | run the human exam or inspect whether the input was too narrow |
| `hold/gap_triage_needs_input` | no source rows were loaded | point the manifest at mastery audit, recall audit, paper defense, or local runner output |
| `hold/gap_triage_incomplete` | a top gap lacks a route, action, or resolving note | repair the row before treating it as today's plan |

## Capstone Row

| Evidence | Output |
|---|---|
| Mastery gap triage runner | `<run-id>-gap-triage.json`, `<run-id>-gap-triage.md`, `<run-id>-gap-triage.csv`, and one `llm-mastery-gap-triage-runs.jsonl` row |

## Completion Gate

- [ ] the source audit output is current
- [ ] the top gap has a resolving route
- [ ] the top gap has a concrete next action
- [ ] domain summary shows whether the next gap is academic, mechanism, local-inference, system, or exam
- [ ] the triage output is linked from [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]
- [ ] after completing the top action, the source audit is rerun

## References

- [[LLM/Study/LLM Mastery Dashboard]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Mastery Evidence Audit Runner]]
- [[LLM/Study/LLM Concept Dependency Map]]
- [[LLM/Study/LLM Recall and Remediation Audit Runner]]
- [[LLM/Study/LLM Paper Oral Defense Runner]]
- [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner]]
- [[LLM/Study/Local LLM Quality Evaluation Runner]]
- [[LLM/Study/Local LLM Result Synthesis Runner]]
