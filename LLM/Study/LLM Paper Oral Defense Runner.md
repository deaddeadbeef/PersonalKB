---
tags: [study, llm, papers, oral-defense, recall, academic, local-llm, audit, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [core, deep-dive, practice]
last-verified: 2026-06-15
---

# LLM Paper Oral Defense Runner

> **One-line summary** Academic LLM mastery counts only when paper claims can be answered from memory and connected to mechanism, evidence, limitation, local implication, and next proof route.

Use this after [[LLM/Study/LLM Paper Claim Audit Runner|LLM Paper Claim Audit Runner]] when the claim ledger is structurally complete but you still need no-notes oral or written proof. Use it before [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner|LLM Academic-to-Local Defense Matrix Runner]] when paper answers need to become defensible local inference claims.

This runner does not fetch papers, summarize PDFs, or judge whether an answer is semantically correct. It audits saved answer artifacts and rubric fields so academic knowledge becomes replayable evidence instead of a vague confidence claim.

## What This Proves

| Gate | Evidence checked | Why it matters |
|---|---|---|
| No-notes recall | each pass row says the answer was produced without notes | separates paper recognition from usable knowledge |
| Claim anatomy | paper, question, main claim, evidence type, and limitation | prevents fluent summaries from replacing research literacy |
| Mechanism bridge | mechanism, local implication, confounder, and follow-up route | ties papers to hosting, inference, RAG, evaluation, or deployment proof |
| Artifact custody | answer artifact path resolves, unless the answer text is embedded | makes oral practice auditable after the session |
| Scoring discipline | rubric score meets the manifest threshold | keeps "I think I know this" from counting as mastery |
| Remediation | hold/fail rows name failure owner and next action | routes weak paper clusters to the next study or local proof artifact |

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "paper-oral-defense-001",
  "run_root": "D:/llm-runs/paper-oral-defense",
  "vault_root": "D:/Vaults/PersonalKB",
  "minimum_score": 2,
  "expected_clusters": [
    "architecture-attention",
    "pretraining-scaling",
    "systems-serving",
    "alignment-posttraining",
    "adaptation-compression",
    "retrieval-rag",
    "tools-agents",
    "evaluation-deployment"
  ],
  "answers": [
    {
      "answer_id": "attention-001",
      "cluster": "architecture-attention",
      "status": "pass",
      "paper": "Attention Is All You Need",
      "question": "Why did self-attention replace recurrence for LLMs?",
      "answer_artifact": "D:/llm-runs/paper-oral-defense/attention-answer.md",
      "answered_without_notes": true,
      "main_claim": "Self-attention removes recurrent bottlenecks while preserving sequence modeling quality.",
      "evidence_type": "machine translation quality plus parallel training comparison",
      "limitation": "The paper does not prove chat alignment or long-context serving behavior.",
      "mechanism": "scaled dot-product attention, multi-head projections, positional encoding",
      "local_implication": "Local inference measurements must separate prefill attention cost from decode KV-cache reuse.",
      "confounder": "Hardware, batch size, context length, and kernel choice can hide the mechanism.",
      "follow_up_route": "LLM/Study/Attention Implementation Lab",
      "score": 3,
      "failure_owner": "academic",
      "next_action": "Promote this answer into the defense matrix."
    }
  ]
}
```

`answers` may also be called `rows`. Each row can embed `answer_text` instead of linking `answer_artifact`, but durable capstone evidence should keep the artifact.

## Required Fields

| Field family | Accepted keys |
|---|---|
| Answer id | `answer_id`, `id`, `row_id`, `defense_id` |
| Cluster | `cluster`, `paper_cluster`, `topic_cluster` |
| Status | `status`, `state`, `result` |
| Paper | `paper`, `title`, `short_label` |
| Question | `question`, `prompt`, `oral_prompt` |
| Answer artifact | `answer_artifact`, `artifact`, `proof`, `proof_path`, `answer_path` |
| Embedded answer | `answer_text`, `answer`, `oral_answer`, `written_answer` |
| Main claim | `main_claim`, `claim`, `retained_claim` |
| Evidence type | `evidence_type`, `evidence`, `evidence_summary` |
| Limitation | `limitation`, `key_limitation`, `does_not_prove` |
| Mechanism | `mechanism`, `mechanism_anchor`, `main_mechanism` |
| Local implication | `local_implication`, `local_consequence`, `deployment_implication` |
| Confounder | `confounder`, `baseline`, `control`, `threat_to_validity` |
| Follow-up route | `follow_up_route`, `follow_up_vault_route`, `proof_route`, `local_proof_route` |
| Score | `score`, `rubric_score`, `oral_score` |
| No-notes flag | `answered_without_notes`, `no_notes`, `closed_book`, `from_memory` |
| Failure owner | `failure_owner`, `owner`, `remediation_owner` |
| Next action | `next_action`, `remediation`, `todo` |

## Standard-Library Runner

Save this as `llm_paper_oral_defense_runner.py` inside the run folder. It uses only Python's standard library.

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

DEFAULT_EXPECTED_CLUSTERS = [
    "architecture-attention",
    "pretraining-scaling",
    "systems-serving",
    "alignment-posttraining",
    "adaptation-compression",
    "retrieval-rag",
    "tools-agents",
    "evaluation-deployment",
]

FIELD_GROUPS = {
    "answer_id": ("answer_id", "id", "row_id", "defense_id"),
    "cluster": ("cluster", "paper_cluster", "topic_cluster"),
    "status": ("status", "state", "result"),
    "paper": ("paper", "title", "short_label"),
    "question": ("question", "prompt", "oral_prompt"),
    "answer_artifact": ("answer_artifact", "artifact", "proof", "proof_path", "answer_path"),
    "answer_text": ("answer_text", "answer", "oral_answer", "written_answer"),
    "main_claim": ("main_claim", "claim", "retained_claim"),
    "evidence_type": ("evidence_type", "evidence", "evidence_summary"),
    "limitation": ("limitation", "key_limitation", "does_not_prove"),
    "mechanism": ("mechanism", "mechanism_anchor", "main_mechanism"),
    "local_implication": ("local_implication", "local_consequence", "deployment_implication"),
    "confounder": ("confounder", "baseline", "control", "threat_to_validity"),
    "follow_up_route": ("follow_up_route", "follow_up_vault_route", "proof_route", "local_proof_route"),
    "score": ("score", "rubric_score", "oral_score"),
    "answered_without_notes": ("answered_without_notes", "no_notes", "closed_book", "from_memory"),
    "failure_owner": ("failure_owner", "owner", "remediation_owner"),
    "next_action": ("next_action", "remediation", "todo"),
}

STATUS_RANK = {"pass": 0, "hold": 1, "fail": 2}


def utc_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def slugify(value: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return text or "llm-paper-oral-defense"


def norm(value: Any) -> str:
    return str(value or "").strip().lower()


def display(value: Any) -> str:
    text = str(value or "").strip()
    return text if len(text) <= 120 else text[:117] + "..."


def md_cell(value: Any) -> str:
    text = str(value or "").replace("\n", "<br>").replace("|", "\\|")
    return text


def list_value(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, tuple):
        return list(value)
    if isinstance(value, str):
        return [part.strip() for part in value.split(",") if part.strip()]
    return [value]


def status_value(value: Any) -> str:
    text = norm(value)
    if text in {"pass", "passed", "ready", "complete", "accepted", "green"}:
        return "pass"
    if text in {"fail", "failed", "rejected", "unsafe", "red"}:
        return "fail"
    return "hold"


def bool_value(value: Any, default: bool = False) -> bool:
    if value is None or value == "":
        return default
    if isinstance(value, bool):
        return value
    text = norm(value)
    if text in {"1", "true", "yes", "y", "pass", "passed", "closed-book", "closed_book", "no-notes", "no_notes"}:
        return True
    if text in {"0", "false", "no", "n", "fail", "failed", "open-book", "open_book"}:
        return False
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


def numeric_value(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


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


def finding(status: str, field: str, message: str, value: str, action: str) -> dict[str, str]:
    return {
        "status": status,
        "field": field,
        "message": message,
        "value": value,
        "action": action,
    }


def vague_local_implication(value: str) -> bool:
    text = norm(value)
    if len(text) < 30:
        return True
    vague_terms = {"local implication", "deployment implication", "n/a", "none", "unknown", "helps local llms"}
    return text in vague_terms


def evaluate_answer(row: dict[str, Any], vault_root: Path, minimum_score: float, fail_score: float) -> dict[str, Any]:
    findings: list[dict[str, str]] = []

    answer_id = first_text(row, "answer_id")
    cluster = first_text(row, "cluster")
    declared_status_text = first_text(row, "status")
    declared_status = status_value(declared_status_text)
    paper = first_text(row, "paper")
    question = first_text(row, "question")
    answer_artifact = first_text(row, "answer_artifact")
    answer_text = first_text(row, "answer_text")
    main_claim = first_text(row, "main_claim")
    evidence_type = first_text(row, "evidence_type")
    limitation = first_text(row, "limitation")
    mechanism = first_text(row, "mechanism")
    local_implication = first_text(row, "local_implication")
    confounder = first_text(row, "confounder")
    follow_up_route = first_text(row, "follow_up_route")
    failure_owner = first_text(row, "failure_owner")
    next_action = first_text(row, "next_action")
    score = numeric_value(first_value(row, "score"))
    answered_without_notes = bool_value(first_value(row, "answered_without_notes"), False)

    stable_id = answer_id or slugify(f"{paper}-{question}")

    for field_name, value in [
        ("answer_id", answer_id),
        ("cluster", cluster),
        ("status", declared_status_text),
        ("paper", paper),
        ("question", question),
    ]:
        if not value:
            findings.append(finding("hold", field_name, f"Answer row is missing {field_name}.", stable_id, f"Fill {field_name} before counting this oral defense answer."))

    if declared_status == "fail":
        findings.append(finding("fail", "status", "Answer row is explicitly failed.", stable_id, "Remediate this answer before using it as paper mastery proof."))
    elif declared_status != "pass":
        findings.append(finding("hold", "status", "Answer row is not marked pass.", stable_id, "Retake or review this paper question until it can be marked pass."))

    answer_artifact_resolved = ""
    answer_artifact_exists = False
    if answer_artifact:
        answer_artifact_resolved, answer_artifact_exists = resolve_path(answer_artifact, vault_root)
        if not answer_artifact_exists:
            findings.append(finding("hold", "answer_artifact", "Answer artifact path does not resolve.", answer_artifact_resolved, "Fix the saved oral/written answer path or embed answer_text."))
    elif not answer_text:
        findings.append(finding("hold", "answer_artifact", "Answer has no artifact path or embedded answer text.", stable_id, "Save the oral answer transcript or write answer_text in the row."))

    if declared_status == "pass" and not answered_without_notes:
        findings.append(finding("hold", "answered_without_notes", "Pass row was not answered without notes.", stable_id, "Retake the question closed-book before counting it as oral defense proof."))

    for field_name, value in [
        ("main_claim", main_claim),
        ("evidence_type", evidence_type),
        ("limitation", limitation),
        ("mechanism", mechanism),
        ("local_implication", local_implication),
        ("follow_up_route", follow_up_route),
    ]:
        if not value:
            findings.append(finding("hold", field_name, f"Answer row is missing {field_name}.", stable_id, f"Fill {field_name} so the paper answer has academic and local proof shape."))

    if local_implication and vague_local_implication(local_implication):
        findings.append(finding("hold", "local_implication", "Local implication is too vague to route to local proof.", local_implication, "Name the affected local inference, RAG, evaluation, adaptation, serving, or deployment behavior."))

    follow_up_route_resolved = ""
    follow_up_route_exists = False
    if follow_up_route:
        follow_up_route_resolved, follow_up_route_exists = resolve_path(follow_up_route, vault_root)
        if not follow_up_route_exists:
            findings.append(finding("hold", "follow_up_route", "Follow-up route does not resolve in the vault.", follow_up_route_resolved, "Fix the Obsidian note route for the next proof artifact."))

    if score is None:
        findings.append(finding("hold", "score", "Answer row has no numeric score.", stable_id, f"Score the answer against the rubric; pass needs at least {minimum_score:g}."))
    elif score < fail_score:
        findings.append(finding("fail", "score", "Answer score is below the fail threshold.", str(score), "Reread the paper and retake this question."))
    elif score < minimum_score:
        findings.append(finding("hold", "score", "Answer score is below the minimum pass threshold.", str(score), f"Raise the answer to at least {minimum_score:g} before counting this row."))

    needs_remediation = any(item["status"] in {"hold", "fail"} for item in findings)
    if needs_remediation and not failure_owner:
        findings.append(finding("hold", "failure_owner", "Incomplete row has no failure owner.", stable_id, "Set failure_owner to academic, mechanism, local, evaluation, systems, or exam."))
    if needs_remediation and not next_action:
        findings.append(finding("hold", "next_action", "Incomplete row has no next action.", stable_id, "Name the next concrete study, lab, or evidence route."))

    has_fail = any(item["status"] == "fail" for item in findings)
    if has_fail:
        status = "fail"
        decision = "paper_oral_answer_failed"
    elif findings:
        status = "hold"
        decision = "paper_oral_answer_incomplete"
    else:
        status = "pass"
        decision = "paper_oral_answer_ready"

    return {
        "answer_id": stable_id,
        "cluster": cluster,
        "paper": paper,
        "question": question,
        "status": status,
        "decision": decision,
        "declared_status": declared_status,
        "answered_without_notes": answered_without_notes,
        "score": score,
        "minimum_score": minimum_score,
        "answer_artifact": answer_artifact,
        "answer_artifact_resolved": answer_artifact_resolved,
        "answer_artifact_exists": answer_artifact_exists,
        "answer_text_present": bool(answer_text),
        "main_claim": main_claim,
        "evidence_type": evidence_type,
        "limitation": limitation,
        "mechanism": mechanism,
        "local_implication": local_implication,
        "confounder": confounder,
        "follow_up_route": follow_up_route,
        "follow_up_route_resolved": follow_up_route_resolved,
        "follow_up_route_exists": follow_up_route_exists,
        "failure_owner": failure_owner,
        "next_action": next_action if next_action else (findings[0]["action"] if findings else "Promote this answer into the academic-to-local defense matrix."),
        "finding_count": len(findings),
        "findings": findings,
    }


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def read_csv(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def load_tabular(path: Path) -> Any:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return read_csv(path)
    return read_json(path)


def load_manifest() -> tuple[dict[str, Any], Path]:
    manifest_env = os.environ.get("LLM_PAPER_ORAL_DEFENSE_MANIFEST", "")
    if not manifest_env:
        raise ValueError("Set LLM_PAPER_ORAL_DEFENSE_MANIFEST to a JSON manifest path.")

    manifest_path = Path(manifest_env)
    manifest_data = read_json(manifest_path)
    if isinstance(manifest_data, list):
        manifest: dict[str, Any] = {"answers": manifest_data}
    elif isinstance(manifest_data, dict):
        manifest = dict(manifest_data)
    else:
        raise ValueError("Manifest must be a JSON object or list of answer rows.")

    input_env = os.environ.get("LLM_PAPER_ORAL_DEFENSE_INPUT", "")
    if input_env:
        input_data = load_tabular(Path(input_env))
        if isinstance(input_data, list):
            manifest["answers"] = input_data
        elif isinstance(input_data, dict):
            for key in ("answers", "rows"):
                if isinstance(input_data.get(key), list):
                    manifest["answers"] = input_data[key]
                    break
            else:
                raise ValueError("Input JSON must include answers or rows.")
        else:
            raise ValueError("Input must be a JSON object, JSON list, or CSV file.")

    return manifest, manifest_path


def expected_clusters(manifest: dict[str, Any]) -> list[str]:
    configured = manifest.get("expected_clusters")
    values = list_value(configured) if configured is not None else DEFAULT_EXPECTED_CLUSTERS
    return [str(item).strip() for item in values if str(item).strip()]


def waived_clusters(manifest: dict[str, Any]) -> dict[str, str]:
    result: dict[str, str] = {}
    for item in list_value(manifest.get("waived_clusters")) + list_value(manifest.get("cluster_waivers")):
        if isinstance(item, dict):
            cluster = str(item.get("cluster") or item.get("id") or item.get("name") or "").strip()
            reason = str(item.get("reason") or item.get("waiver_reason") or "").strip()
        else:
            cluster = str(item).strip()
            reason = "Waived by manifest."
        if cluster:
            result[cluster] = reason
    return result


def rows_from_manifest(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    rows = manifest.get("answers", manifest.get("rows", []))
    if not isinstance(rows, list) or not all(isinstance(row, dict) for row in rows):
        raise ValueError("Manifest answers/rows must be a list of objects.")
    return [dict(row) for row in rows]


def cluster_summary(rows: list[dict[str, Any]], expected: list[str], waived: dict[str, str]) -> list[dict[str, Any]]:
    clusters = sorted(set(expected) | {row["cluster"] or "unspecified" for row in rows} | set(waived))
    summary: list[dict[str, Any]] = []
    for cluster in clusters:
        subset = [row for row in rows if (row["cluster"] or "unspecified") == cluster]
        pass_count = sum(1 for row in subset if row["status"] == "pass")
        hold_count = sum(1 for row in subset if row["status"] == "hold")
        fail_count = sum(1 for row in subset if row["status"] == "fail")
        covered = pass_count > 0 or cluster in waived
        summary.append({
            "cluster": cluster,
            "expected": cluster in expected,
            "waived": cluster in waived,
            "waiver_reason": waived.get(cluster, ""),
            "covered": covered,
            "answer_count": len(subset),
            "pass_count": pass_count,
            "hold_count": hold_count,
            "fail_count": fail_count,
        })
    return summary


def csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = [
        "answer_id",
        "cluster",
        "paper",
        "question",
        "status",
        "decision",
        "answered_without_notes",
        "score",
        "answer_artifact",
        "answer_artifact_exists",
        "follow_up_route",
        "follow_up_route_exists",
        "finding_count",
        "failure_owner",
        "next_action",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def render_markdown(record: dict[str, Any]) -> str:
    lines = [
        f"# LLM Paper Oral Defense Audit - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Answers: `{record['answer_count']}`",
        f"- Pass / hold / fail: `{record['pass_count']}` / `{record['hold_count']}` / `{record['fail_count']}`",
        f"- Expected clusters: `{record['expected_cluster_count']}`",
        f"- Covered expected clusters: `{record['covered_expected_cluster_count']}`",
        f"- Manifest: `{record['manifest_path']}`",
        "",
        "## Cluster Summary",
        "",
        "| Cluster | Expected | Covered | Pass | Hold | Fail | Waiver |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for row in record["clusters"]:
        lines.append("| " + " | ".join([
            md_cell(row["cluster"]),
            "yes" if row["expected"] else "",
            "yes" if row["covered"] else "",
            str(row["pass_count"]),
            str(row["hold_count"]),
            str(row["fail_count"]),
            md_cell(row["waiver_reason"]),
        ]) + " |")

    lines.extend([
        "",
        "## Answer Rows",
        "",
        "| Status | Cluster | Paper | Question | Score | No notes | Next action |",
        "|---|---|---|---|---:|---:|---|",
    ])
    for row in record["answers"]:
        lines.append("| " + " | ".join([
            md_cell(row["status"]),
            md_cell(row["cluster"]),
            md_cell(row["paper"]),
            md_cell(row["question"]),
            "" if row["score"] is None else f"{row['score']:g}",
            "yes" if row["answered_without_notes"] else "no",
            md_cell(row["next_action"]),
        ]) + " |")

    lines.extend(["", "## Findings", ""])
    findings_written = False
    for row in record["answers"]:
        for item in row["findings"]:
            findings_written = True
            lines.append(f"- `{row['answer_id']}` `{item['status']}` `{item['field']}`: {item['message']} Next: {item['action']}")
    for item in record["manifest_findings"]:
        findings_written = True
        lines.append(f"- `manifest` `{item['status']}` `{item['field']}`: {item['message']} Next: {item['action']}")
    if not findings_written:
        lines.append("- Paper oral defense evidence is ready for the academic-to-local defense matrix.")

    return "\n".join(lines) + "\n"


def main() -> int:
    manifest, manifest_path = load_manifest()
    run_id = str(manifest.get("run_id") or manifest_path.stem or "paper-oral-defense").strip()
    run_root_value = os.environ.get("LLM_PAPER_ORAL_DEFENSE_RUN_ROOT") or manifest.get("run_root", "llm-paper-oral-defense-runs")
    vault_root_value = os.environ.get("LLM_PAPER_ORAL_DEFENSE_VAULT_ROOT") or manifest.get("vault_root", ".")
    run_root = Path(str(run_root_value))
    vault_root = Path(str(vault_root_value))
    minimum_score = numeric_value(manifest.get("minimum_score")) or 2.0
    fail_score = numeric_value(manifest.get("fail_score")) or 1.0

    run_dir = run_root / slugify(run_id)
    run_dir.mkdir(parents=True, exist_ok=True)
    run_root.mkdir(parents=True, exist_ok=True)

    rows = rows_from_manifest(manifest)
    evaluated = [evaluate_answer(row, vault_root, minimum_score, fail_score) for row in rows]
    evaluated.sort(key=lambda row: (STATUS_RANK.get(row["status"], 3), row["cluster"], row["paper"], row["answer_id"]))

    expected = expected_clusters(manifest)
    waived = waived_clusters(manifest)
    clusters = cluster_summary(evaluated, expected, waived)

    manifest_findings: list[dict[str, str]] = []
    if not evaluated:
        manifest_findings.append(finding("hold", "answers", "Manifest has no answer rows.", str(manifest_path), "Add at least one oral defense answer row."))

    pass_clusters = {row["cluster"] for row in evaluated if row["status"] == "pass"}
    for cluster in expected:
        if cluster not in pass_clusters and cluster not in waived:
            manifest_findings.append(finding("hold", "expected_clusters", "Expected paper cluster has no passing oral defense answer.", cluster, "Add a pass row or waive the cluster with a reason."))
        if cluster in waived and not waived[cluster]:
            manifest_findings.append(finding("hold", "waived_clusters", "Waived cluster has no reason.", cluster, "Record why this cluster is out of scope for the current defense."))

    pass_count = sum(1 for row in evaluated if row["status"] == "pass")
    hold_count = sum(1 for row in evaluated if row["status"] == "hold")
    fail_count = sum(1 for row in evaluated if row["status"] == "fail")
    manifest_fail_count = sum(1 for item in manifest_findings if item["status"] == "fail")
    manifest_hold_count = sum(1 for item in manifest_findings if item["status"] == "hold")
    covered_expected_cluster_count = sum(1 for row in clusters if row["expected"] and row["covered"])

    if fail_count or manifest_fail_count:
        status = "fail"
        decision = "paper_oral_defense_failed"
        next_action = "Fix failed oral defense rows before using them as academic proof."
    elif hold_count or manifest_hold_count:
        status = "hold"
        decision = "paper_oral_defense_incomplete"
        next_action = "Complete the first held answer row or missing expected cluster."
    else:
        status = "pass"
        decision = "paper_oral_defense_ready"
        next_action = "Promote the passed rows into the academic-to-local defense matrix and capstone workbook."

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "next_action": next_action,
        "manifest_path": str(manifest_path),
        "vault_root": str(vault_root),
        "minimum_score": minimum_score,
        "fail_score": fail_score,
        "expected_cluster_count": len(expected),
        "covered_expected_cluster_count": covered_expected_cluster_count,
        "answer_count": len(evaluated),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "clusters": clusters,
        "answers": evaluated,
        "manifest_findings": manifest_findings,
        "outputs": {},
    }

    json_path = run_dir / f"{slugify(run_id)}-paper-oral-defense.json"
    markdown_path = run_dir / f"{slugify(run_id)}-paper-oral-defense.md"
    csv_path = run_dir / f"{slugify(run_id)}-paper-oral-defense.csv"
    jsonl_path = run_root / "llm-paper-oral-defense-runs.jsonl"
    record["outputs"] = {
        "json": str(json_path),
        "markdown": str(markdown_path),
        "csv": str(csv_path),
        "jsonl": str(jsonl_path),
    }

    csv_write(csv_path, evaluated)
    json_path.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    markdown_path.write_text(render_markdown(record), encoding="utf-8")
    with jsonl_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(json.dumps({
        "status": status,
        "decision": decision,
        "run_id": run_id,
        "answer_count": len(evaluated),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "covered_expected_cluster_count": covered_expected_cluster_count,
        "output_dir": str(run_dir),
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
$env:LLM_PAPER_ORAL_DEFENSE_MANIFEST = "D:\llm-runs\paper-oral-defense\paper-oral-defense-manifest.json"
$env:LLM_PAPER_ORAL_DEFENSE_VAULT_ROOT = "D:\Vaults\PersonalKB"
$env:LLM_PAPER_ORAL_DEFENSE_RUN_ROOT = "D:\llm-runs\paper-oral-defense"
python .\llm_paper_oral_defense_runner.py
```

## Reading The Result

| Runner status | Meaning | Next route |
|---|---|---|
| `pass/paper_oral_defense_ready` | every expected cluster has a passing no-notes answer with artifact/text, claim, evidence, limitation, mechanism, local implication, route, and score | promote the rows into [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner|LLM Academic-to-Local Defense Matrix Runner]] |
| `hold/paper_oral_defense_incomplete` | a row is missing a field, answer artifact, closed-book flag, minimum score, route, or expected cluster | retake or repair the first held answer |
| `fail/paper_oral_defense_failed` | a row is explicitly failed or below the fail score | reread the paper and repeat the oral defense attempt |

## Capstone Row

| Evidence | Output |
|---|---|
| Paper oral defense runner | `<run-id>-paper-oral-defense.json`, `<run-id>-paper-oral-defense.md`, `<run-id>-paper-oral-defense.csv`, and one `llm-paper-oral-defense-runs.jsonl` row |

## Completion Gate

- [ ] every required paper cluster has at least one passing no-notes answer
- [ ] every pass row links an answer artifact or embeds answer text
- [ ] every pass row names the paper claim, evidence type, limitation, mechanism, and local implication
- [ ] every follow-up route resolves in the vault
- [ ] hold/fail rows name failure owner and next action
- [ ] output JSON, Markdown, CSV, and JSONL artifacts are saved
- [ ] outputs are linked from [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]

## References

- [[LLM/Study/LLM Paper Reading Protocol]]
- [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map]]
- [[LLM/Study/LLM Paper Claim Ledger]]
- [[LLM/Study/LLM Paper Claim Audit Runner]]
- [[LLM/Study/LLM Paper-to-Local Proof Router]]
- [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Mastery Evidence Audit Runner]]
- [[LLM/Study/LLM Mastery Exam Run Sheet]]
- [[LLM/Study/Local LLM End-to-End Mental Model]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
