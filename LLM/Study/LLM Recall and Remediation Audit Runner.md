---
tags: [study, llm, mastery, recall, remediation, audit, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [intuition, core, deep-dive, practice]
last-verified: 2026-06-15
---

# LLM Recall and Remediation Audit Runner

> **One-line summary** LLM knowledge counts only when recall attempts have scores, coverage, miss routes, remediation artifacts, and next-review dates; this runner turns active recall into audit evidence instead of a feeling.

Use this after [[LLM/Study/LLM Active Recall Question Bank|LLM Active Recall Question Bank]], [[LLM/Study/LLM Daily Mastery Session Run Sheet|LLM Daily Mastery Session Run Sheet]], or [[LLM/Study/LLM Mastery Exam Run Sheet|LLM Mastery Exam Run Sheet]] produces a set of answered prompts. Use it before [[LLM/Study/LLM Mastery Evidence Audit Runner|LLM Mastery Evidence Audit Runner]] when the final mastery bundle needs proof that missed academic and applied questions were routed, remediated, and scheduled for retest.

This runner does not grade answer quality by itself. It audits the scoring and remediation evidence you wrote down: prompt id, domain, score, route, answer artifact, miss reason, remediation artifact, next review, and applied proof when the missed question concerns local hosting, RAG, tools, safety, or deployment.

## What This Proves

| Evidence family | Checks | Why it matters |
|---|---|---|
| Coverage | academic, mechanism, local-inference, and system prompts are represented | prevents local setup from replacing conceptual mastery, and prevents theory from replacing hosting competence |
| Scoring | every answered prompt has numeric score and max score | turns recall into measured evidence |
| Miss routing | low-score answers have a route, miss reason, remediation artifact, and next review | turns forgetting into a repair plan |
| Hard-fail protection | zeros in local inference, RAG/evaluation, safety, or deployment domains fail the audit | prevents passing while the applied path is unsafe or unusable |
| Applied proof | applied-domain misses link a local artifact, command output, or blocker | keeps local hosting knowledge attached to real evidence |
| Session decision | pass, hold, or fail has a computed reason | avoids "I studied" as a mastery claim |

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "recall-2026-06-15",
  "run_root": "D:/llm-runs/recall-audit",
  "vault_root": "D:/Vaults/PersonalKB",
  "min_percent": 80,
  "rows": [
    {
      "prompt_id": "local-endpoint-01",
      "domain": "local-inference",
      "prompt": "What proves the served model id?",
      "score": 3,
      "max_score": 3,
      "answer_artifact": "D:/llm-runs/recall-audit/answers/local-endpoint-01.md",
      "route": "LLM/Study/Local LLM OpenAI-Compatible API Contract Lab",
      "applied_proof": "LLM/Study/Local LLM OpenAI-Compatible API Contract Runner.md"
    }
  ]
}
```

`answer_artifact`, `route`, `remediation_artifact`, and `applied_proof` may be absolute paths, vault-relative paths, Obsidian note paths, or Obsidian links. A low score is allowed only when it has remediation.

## Row Contract

| Field | Required when | Meaning |
|---|---|---|
| `prompt_id` | always | stable id from the question bank, daily session, or exam sheet |
| `domain` | always | `academic`, `mechanism`, `local-inference`, `system`, or `exam`; custom domains are allowed but do not satisfy default required coverage |
| `prompt` | always | the question answered without notes |
| `score` | always | numeric score |
| `max_score` | optional | default is `3` |
| `answer_artifact` | always | answer note, exam attempt, session run sheet, or saved row |
| `route` | always | note or lab used to check or remediate the answer |
| `miss_reason` | score below max | mechanism missing, evidence missing, consequence missing, practical link missing, or similar |
| `remediation_artifact` | score below max | corrected answer, lab proof, paper row, command output, or blocker row |
| `next_review` | score below max | date or session id for retest |
| `applied_proof` | local-inference or system rows | link to local hosting, RAG/tool, quality, safety, operations, or deployment evidence |

## Standard-Library Runner

Save this as `llm_recall_remediation_audit_runner.py` inside the run folder. It uses only Python's standard library.

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


DEFAULT_REQUIRED_DOMAINS = ["academic", "mechanism", "local-inference", "system"]
HARD_FAIL_DOMAINS = {"local-inference", "rag", "evaluation", "safety", "security", "deployment", "system"}
DOMAIN_ALIASES = {
    "local_inference": "local-inference",
    "local inference": "local-inference",
    "rag_evaluation": "system",
    "rag/evaluation": "system",
    "safety_deployment": "system",
    "safety/deployment": "system",
}


def utc_iso() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def slug(value: str) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value).strip().lower())
    return text.strip("-") or "recall-audit"


def display(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value).strip()


def norm_domain(value: Any) -> str:
    text = display(value).lower().replace("_", "-")
    return DOMAIN_ALIASES.get(text, text)


def bool_value(value: Any, default: bool = False) -> bool:
    if value is None or value == "":
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y", "pass", "required"}


def list_value(value: Any) -> list[Any]:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return value
    return [value]


def as_number(value: Any, default: float | None = None) -> float | None:
    try:
        if value is None or value == "":
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def md_cell(value: Any) -> str:
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=True)
    return display(value).replace("|", "\\|").replace("\n", " ")


def unwrap_link(value: Any) -> str:
    text = display(value)
    open_link = "[" * 2
    close_link = "]" * 2
    if text.startswith(open_link) and text.endswith(close_link):
        text = text[2:-2]
        if "|" in text:
            text = text.split("|", 1)[0]
    if "#" in text:
        text = text.split("#", 1)[0]
    return text.strip()


def proof_exists(vault_root: Path, value: Any) -> tuple[bool, str]:
    proof = unwrap_link(value)
    if not proof:
        return False, ""
    if proof.startswith(("http://", "https://")):
        return True, proof
    path_text = proof.replace("/", "\\")
    path = Path(path_text).expanduser()
    candidates: list[Path] = []
    if path.is_absolute():
        candidates.append(path)
    else:
        candidates.append(vault_root / path)
    if not path.suffix:
        candidates.extend(candidate.with_suffix(".md") for candidate in list(candidates))
    for candidate in candidates:
        if candidate.exists():
            return True, str(candidate)
    if "\\" not in path_text and "/" not in proof:
        matches = list(vault_root.rglob(path_text + ".md"))
        if matches:
            return True, str(matches[0])
    return False, proof


def finding(level: str, row_id: str, domain: str, text: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "row_id": row_id,
        "domain": domain,
        "finding": text,
        "evidence": evidence,
        "action": action,
    }


def first_text(row: dict[str, Any], keys: list[str]) -> str:
    for key in keys:
        value = display(row.get(key))
        if value:
            return value
    return ""


def row_proof(row: dict[str, Any], keys: list[str], vault_root: Path) -> tuple[bool, str]:
    value = first_text(row, keys)
    return proof_exists(vault_root, value)


def evaluate_row(row: dict[str, Any], vault_root: Path, default_max_score: float) -> dict[str, Any]:
    row_id = display(row.get("prompt_id") or row.get("id") or row.get("row_id"))
    domain = norm_domain(row.get("domain") or row.get("cluster"))
    prompt = display(row.get("prompt") or row.get("question"))
    score = as_number(row.get("score"))
    max_score = as_number(row.get("max_score"), default_max_score) or default_max_score
    findings: list[dict[str, str]] = []

    if not row_id:
        findings.append(finding("hold", "(missing)", domain, "Prompt id is missing.", json.dumps(row, ensure_ascii=True)[:160], "Give every recall row a stable prompt_id."))
        row_id = "(missing)"
    if not domain:
        findings.append(finding("hold", row_id, "(missing)", "Domain is missing.", row_id, "Set domain to academic, mechanism, local-inference, system, or exam."))
        domain = "(missing)"
    if not prompt:
        findings.append(finding("hold", row_id, domain, "Prompt text is missing.", row_id, "Copy or summarize the answered prompt."))
    if score is None:
        findings.append(finding("hold", row_id, domain, "Score is missing or not numeric.", display(row.get("score")), "Add a numeric recall score."))
        score = -1
    if max_score <= 0:
        findings.append(finding("hold", row_id, domain, "Max score must be positive.", display(row.get("max_score")), "Set max_score to a positive number."))
        max_score = default_max_score
    if score > max_score:
        findings.append(finding("hold", row_id, domain, "Score exceeds max score.", f"{score}/{max_score}", "Fix score or max_score."))
    if score < 0:
        findings.append(finding("hold", row_id, domain, "Score is negative.", str(score), "Use a score from 0 to max_score."))

    answer_exists, answer_resolved = row_proof(row, ["answer_artifact", "answer_path", "attempt_path", "session_path", "proof"], vault_root)
    if not answer_exists:
        findings.append(finding("hold", row_id, domain, "Answer artifact does not resolve.", answer_resolved or "(missing answer_artifact)", "Link the daily session, exam attempt, or answer note."))

    route_exists, route_resolved = row_proof(row, ["route", "route_if_missed", "miss_route", "check_route"], vault_root)
    if not route_exists:
        findings.append(finding("hold", row_id, domain, "Route link does not resolve.", route_resolved or "(missing route)", "Link the note or lab used to check or remediate the answer."))

    low_score = score < max_score
    if low_score:
        if not first_text(row, ["miss_reason", "why_missed", "gap"]):
            findings.append(finding("hold", row_id, domain, "Low-score row has no miss reason.", f"{score}/{max_score}", "Name whether the miss was mechanism, evidence, consequence, or practical-link related."))
        remediation_exists, remediation_resolved = row_proof(row, ["remediation_artifact", "corrected_answer", "next_proof_artifact", "fix_artifact"], vault_root)
        if not remediation_exists:
            findings.append(finding("hold", row_id, domain, "Low-score row has no remediation artifact.", remediation_resolved or "(missing remediation_artifact)", "Link the corrected answer, lab proof, paper row, command output, or blocker row."))
        if not first_text(row, ["next_review", "retake_date", "review_session"]):
            findings.append(finding("hold", row_id, domain, "Low-score row has no next review.", row_id, "Schedule a retest date or session id."))

    applied_domain = domain in {"local-inference", "system", "rag", "evaluation", "safety", "security", "deployment"}
    if applied_domain:
        applied_exists, applied_resolved = row_proof(row, ["applied_proof", "evidence_artifact", "local_artifact", "capstone_artifact"], vault_root)
        if not applied_exists:
            findings.append(finding("hold", row_id, domain, "Applied-domain row has no applied proof link.", applied_resolved or "(missing applied_proof)", "Link local endpoint, RAG/tool, quality, security, operations, or deployment evidence."))

    if bool_value(row.get("unsafe")) or bool_value(row.get("hard_fail")):
        findings.append(finding("fail", row_id, domain, "Row is marked unsafe or hard fail.", row_id, "Resolve the unsafe applied gap before using this session as mastery evidence."))
    if score == 0 and domain in HARD_FAIL_DOMAINS:
        findings.append(finding("fail", row_id, domain, "Hard-fail domain has a zero score.", f"{score}/{max_score}", "Retake this domain after remediation before claiming mastery."))

    if any(item["level"] == "fail" for item in findings):
        status = "fail"
        decision = "row_failed"
    elif findings:
        status = "hold"
        decision = "row_incomplete"
    else:
        status = "pass"
        decision = "row_ready"

    percent = 0.0 if max_score <= 0 else round((max(score, 0) / max_score) * 100, 2)
    return {
        "prompt_id": row_id,
        "domain": domain,
        "status": status,
        "decision": decision,
        "score": score,
        "max_score": max_score,
        "percent": percent,
        "prompt": prompt,
        "answer_artifact_resolved": answer_resolved,
        "route_resolved": route_resolved,
        "next_action": findings[0]["action"] if findings else "Keep this row in the recall evidence bundle.",
        "findings": findings,
    }


def domain_summary(rows: list[dict[str, Any]], required_domains: list[str]) -> list[dict[str, Any]]:
    domains = sorted(set(required_domains) | {row["domain"] for row in rows})
    summaries: list[dict[str, Any]] = []
    for domain in domains:
        subset = [row for row in rows if row["domain"] == domain]
        score = sum(float(row["score"]) for row in subset if row["score"] >= 0)
        max_score = sum(float(row["max_score"]) for row in subset)
        percent = round((score / max_score) * 100, 2) if max_score else 0.0
        summaries.append({
            "domain": domain,
            "required": domain in required_domains,
            "row_count": len(subset),
            "score": score,
            "max_score": max_score,
            "percent": percent,
            "zero_count": sum(1 for row in subset if row["score"] == 0),
            "pass_count": sum(1 for row in subset if row["status"] == "pass"),
            "hold_count": sum(1 for row in subset if row["status"] == "hold"),
            "fail_count": sum(1 for row in subset if row["status"] == "fail"),
        })
    return summaries


def csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = ["prompt_id", "domain", "status", "decision", "score", "max_score", "percent", "next_action", "prompt"]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def render_markdown(record: dict[str, Any]) -> str:
    lines = [
        f"# LLM Recall and Remediation Audit - {record['run_id']}",
        "",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Rows: `{record['row_count']}`",
        f"- Score: `{record['score']}` / `{record['max_score']}` (`{record['percent']}`%)",
        f"- Pass/Hold/Fail: `{record['pass_count']}` / `{record['hold_count']}` / `{record['fail_count']}`",
        f"- Findings: `{record['finding_count']}`",
        f"- Next action: {record['next_action']}",
        "",
        "## Domain Summary",
        "",
        "| Domain | Required | Rows | Score | Max | Percent | Zeroes | Pass | Hold | Fail |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in record["domains"]:
        lines.append(
            "| "
            + " | ".join([
                md_cell(row["domain"]),
                md_cell(row["required"]),
                md_cell(row["row_count"]),
                md_cell(row["score"]),
                md_cell(row["max_score"]),
                md_cell(row["percent"]),
                md_cell(row["zero_count"]),
                md_cell(row["pass_count"]),
                md_cell(row["hold_count"]),
                md_cell(row["fail_count"]),
            ])
            + " |"
        )
    lines.extend(["", "## Rows", "", "| Prompt | Domain | Status | Score | Percent | Next action |", "|---|---|---|---:|---:|---|"])
    for row in record["rows"]:
        lines.append(
            "| "
            + " | ".join([
                md_cell(row["prompt_id"]),
                md_cell(row["domain"]),
                md_cell(row["status"]),
                md_cell(f"{row['score']}/{row['max_score']}"),
                md_cell(row["percent"]),
                md_cell(row["next_action"]),
            ])
            + " |"
        )
    lines.extend(["", "## Findings", ""])
    if record["findings"]:
        lines.append("| Level | Prompt | Domain | Finding | Evidence | Action |")
        lines.append("|---|---|---|---|---|---|")
        for item in record["findings"]:
            lines.append(
                "| "
                + " | ".join([
                    md_cell(item["level"]),
                    md_cell(item["row_id"]),
                    md_cell(item["domain"]),
                    md_cell(item["finding"]),
                    md_cell(item["evidence"]),
                    md_cell(item["action"]),
                ])
                + " |"
            )
    else:
        lines.append("No findings.")
    return "\n".join(lines) + "\n"


def load_manifest() -> tuple[Path, dict[str, Any]]:
    manifest_value = os.environ.get("LLM_RECALL_REMEDIATION_AUDIT_MANIFEST")
    if not manifest_value:
        raise ValueError("Set LLM_RECALL_REMEDIATION_AUDIT_MANIFEST to a JSON manifest path.")
    manifest_path = Path(manifest_value).expanduser().resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict):
        raise ValueError("Manifest must be a JSON object.")
    return manifest_path, manifest


def main() -> int:
    manifest_path, manifest = load_manifest()
    base_for_relative = manifest_path.parent
    run_root_value = os.environ.get("LLM_RECALL_REMEDIATION_AUDIT_RUN_ROOT") or manifest.get("run_root") or base_for_relative
    run_root = Path(str(run_root_value)).expanduser()
    if not run_root.is_absolute():
        run_root = base_for_relative / run_root
    run_root = run_root.resolve()

    vault_root_value = manifest.get("vault_root") or os.environ.get("LLM_RECALL_REMEDIATION_AUDIT_VAULT_ROOT") or "."
    vault_root = Path(str(vault_root_value)).expanduser()
    if not vault_root.is_absolute():
        vault_root = base_for_relative / vault_root
    vault_root = vault_root.resolve()

    run_id = display(manifest.get("run_id") or os.environ.get("LLM_RECALL_REMEDIATION_AUDIT_RUN_ID") or f"{utc_stamp()}-{slug(run_root.name)}")
    output_root_value = manifest.get("output_root") or os.environ.get("LLM_RECALL_REMEDIATION_AUDIT_OUTPUT_ROOT") or "recall-remediation-audits"
    output_root = Path(str(output_root_value)).expanduser()
    if not output_root.is_absolute():
        output_root = run_root / output_root
    output_root = output_root.resolve()
    output_dir = output_root / run_id
    output_dir.mkdir(parents=True, exist_ok=True)

    rows = manifest.get("rows") or []
    if not isinstance(rows, list) or not all(isinstance(row, dict) for row in rows):
        raise ValueError("Manifest rows must be a list of objects.")
    default_max_score = as_number(manifest.get("default_max_score"), 3.0) or 3.0
    min_percent = as_number(manifest.get("min_percent"), 80.0) or 80.0
    required_domains = [norm_domain(item) for item in list_value(manifest.get("required_domains"))] or list(DEFAULT_REQUIRED_DOMAINS)

    evaluated = [evaluate_row(dict(row), vault_root, default_max_score) for row in rows]
    domains = domain_summary(evaluated, required_domains)
    findings = [item for row in evaluated for item in row["findings"]]

    missing_domains = [row["domain"] for row in domains if row["required"] and row["row_count"] == 0]
    for domain in missing_domains:
        findings.append(finding("hold", "(domain)", domain, "Required recall domain has no rows.", domain, "Add at least one recall row for this domain."))

    total_score = sum(float(row["score"]) for row in evaluated if row["score"] >= 0)
    total_max = sum(float(row["max_score"]) for row in evaluated)
    percent = round((total_score / total_max) * 100, 2) if total_max else 0.0
    pass_count = sum(1 for row in evaluated if row["status"] == "pass")
    hold_count = sum(1 for row in evaluated if row["status"] == "hold")
    fail_count = sum(1 for row in evaluated if row["status"] == "fail")

    if not evaluated:
        findings.append(finding("hold", "(session)", "(none)", "Manifest has no recall rows.", str(manifest_path), "Add answered recall, daily-session, or exam rows."))
    if percent < min_percent and evaluated:
        findings.append(finding("hold", "(session)", "(overall)", "Overall recall score is below threshold.", f"{percent}% < {min_percent}%", "Remediate misses and rerun a mixed recall session."))

    fail_count = sum(1 for item in findings if item["level"] == "fail")
    hold_findings = sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        status = "fail"
        decision = "recall_remediation_failed"
        next_action = "Retake the hard-fail recall domain after remediation."
    elif hold_findings:
        status = "hold"
        decision = "recall_remediation_incomplete"
        next_action = "Complete the first missing recall route, remediation artifact, or next-review field."
    else:
        status = "pass"
        decision = "recall_remediation_ready"
        next_action = "Link this audit output in the mastery exam run sheet and mastery evidence audit."

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "next_action": next_action,
        "manifest_path": str(manifest_path),
        "run_root": str(run_root),
        "vault_root": str(vault_root),
        "row_count": len(evaluated),
        "score": total_score,
        "max_score": total_max,
        "percent": percent,
        "min_percent": min_percent,
        "pass_count": pass_count,
        "hold_count": sum(1 for row in evaluated if row["status"] == "hold"),
        "fail_count": sum(1 for row in evaluated if row["status"] == "fail"),
        "finding_count": len(findings),
        "missing_domains": missing_domains,
        "domains": domains,
        "rows": evaluated,
        "findings": findings,
        "outputs": {},
    }

    json_path = output_dir / f"{run_id}-recall-remediation-audit.json"
    markdown_path = output_dir / f"{run_id}-recall-remediation-audit.md"
    csv_path = output_dir / f"{run_id}-recall-remediation-audit.csv"
    jsonl_path = output_root / "recall-remediation-audits.jsonl"
    record["outputs"] = {
        "json": str(json_path),
        "markdown": str(markdown_path),
        "csv": str(csv_path),
        "jsonl": str(jsonl_path),
    }

    csv_write(csv_path, evaluated)
    json_path.write_text(json.dumps(record, indent=2, ensure_ascii=True), encoding="utf-8")
    markdown_path.write_text(render_markdown(record), encoding="utf-8")
    with jsonl_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=True) + "\n")

    print(json.dumps({
        "status": status,
        "decision": decision,
        "run_id": run_id,
        "row_count": record["row_count"],
        "score": record["score"],
        "max_score": record["max_score"],
        "percent": record["percent"],
        "pass_count": record["pass_count"],
        "hold_count": record["hold_count"],
        "fail_count": record["fail_count"],
        "finding_count": record["finding_count"],
        "missing_domains": missing_domains,
        "output_dir": str(output_dir),
    }, indent=2))
    return 0 if status == "pass" else 1 if status == "hold" else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(json.dumps({"status": "error", "decision": "runner_exception", "error": str(exc)}, indent=2), file=sys.stderr)
        raise SystemExit(3)
```

## PowerShell Run

```powershell
$env:LLM_RECALL_REMEDIATION_AUDIT_MANIFEST = "D:\llm-runs\recall-audit\recall-manifest.json"
$env:LLM_RECALL_REMEDIATION_AUDIT_VAULT_ROOT = "D:\Vaults\PersonalKB"
python .\llm_recall_remediation_audit_runner.py
```

## Reading The Result

| Runner status | Meaning | Next route |
|---|---|---|
| `pass/recall_remediation_ready` | coverage is present, score is at or above threshold, low-score rows have remediation, and hard-fail domains have no zeroes | link the output in [[LLM/Study/LLM Mastery Exam Run Sheet|LLM Mastery Exam Run Sheet]] and [[LLM/Study/LLM Mastery Evidence Audit Runner|LLM Mastery Evidence Audit Runner]] |
| `hold/recall_remediation_incomplete` | recall exists, but score, coverage, route, remediation, next review, or applied proof is incomplete | complete the routed miss before using the session as mastery evidence |
| `fail/recall_remediation_failed` | a hard-fail applied domain has a zero or a row is marked unsafe/hard fail | remediate and retake that domain before claiming mastery |

## Completion Gate

This runner is complete for one recall or exam session when:

- [ ] academic, mechanism, local-inference, and system rows are present or explicitly overridden in the manifest
- [ ] every row has prompt id, domain, prompt, score, answer artifact, and route
- [ ] every low-score row has miss reason, remediation artifact, and next review
- [ ] every local-inference or system row has applied proof
- [ ] no hard-fail applied domain has a zero score
- [ ] output JSON, Markdown, CSV, and JSONL files are linked from the exam run sheet or mastery audit

## References

- [[LLM/Study/LLM Active Recall Question Bank]]
- [[LLM/Study/LLM Daily Mastery Session Run Sheet]]
- [[LLM/Study/LLM Mastery Exam Run Sheet]]
- [[LLM/Study/LLM Mastery Self-Assessment Exam]]
- [[LLM/Study/LLM Mastery Evidence Audit Runner]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]]
- [[LLM/Study/Local LLM Hands-On Practicum Sequence]]
