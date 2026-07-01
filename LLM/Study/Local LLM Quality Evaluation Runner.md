---
tags: [study, llm, evaluation, local-llm, benchmark, quality, audit, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice, deep-dive]
last-verified: 2026-06-15
---

# Local LLM Quality Evaluation Runner

> **One-line summary** A local model quality claim is ready only when each prompt-suite case has saved prompt and response artifacts, rubric scores, workload pass criteria, boundary-specific proof, and a pass/hold/fail decision.

Use this after [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] defines the prompt suite and rubric. Use [[LLM/Study/Local LLM Evaluation Set Design Runner|Local LLM Evaluation Set Design Runner]] first when the suite must support repeated model, runtime, RAG, tool, or deployment decisions. Use [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]], [[LLM/Study/Local LLM First Client Harness Runner|Local LLM First Client Harness Runner]], or an equivalent saved client run to produce the prompt and response artifacts this runner checks.

This runner does not call a model, judge an answer semantically, or replace human review. It audits the evidence you already saved from local inference: prompt files, response files, rubric rows, human or judge scores, latency rows, RAG/citation evidence, tool traces, reasoning-budget audits, and next actions.

## What This Proves

| Evidence family | Checks | Why it matters |
|---|---|---|
| Workload contract | workload, selected candidate, quality bar, pass threshold | prevents "good enough" from being an undefined feeling |
| Prompt and response custody | prompt artifact, response artifact, proof paths | makes the quality row reproducible and reviewable |
| Rubric scoring | required dimensions, scores, expected behavior, pass criteria | keeps evaluation tied to a written standard |
| Contamination control | private/local or held-out rows for acceptance decisions | avoids passing because the prompt came from public benchmark memory |
| Boundary-specific proof | RAG retrieval/citation, tool/schema/policy, reasoning-budget evidence | catches failures hidden behind generic quality scores |
| Review and action | human review, judge calibration, failure owner, next action | turns hold/fail rows into controlled reruns instead of vague concern |

Academic bridge: evaluation is part of the system, not an afterthought. A hosted or local model that passes a public benchmark can still fail your workload because of distribution shift, contamination, prompt formatting, retrieval errors, schema failures, or latency constraints.

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "quality-eval-2026-06-15",
  "run_root": "D:/llm-runs/quality-eval",
  "vault_root": "D:/Vaults/PersonalKB",
  "workload": "private note summarization",
  "selected_candidate": "ollama-qwen-small",
  "quality_bar": "answers preserve cited facts and refuse unsupported claims",
  "pass_threshold": 1.5,
  "required_dimensions": ["factuality", "instruction_following", "format_validity", "completeness", "safety", "latency_acceptability"],
  "evaluation_set_design": "LLM/Study/Local LLM Evaluation Set Design Runner.md",
  "cases": [
    {
      "case_id": "K-01",
      "task_class": "known_answer",
      "status": "pass",
      "candidate_id": "ollama-qwen-small",
      "model_id": "qwen-example",
      "runtime": "Ollama",
      "source_type": "private",
      "split": "heldout",
      "prompt_artifact": "D:/llm-runs/quality-eval/K-01.prompt.json",
      "response_artifact": "D:/llm-runs/quality-eval/K-01.response.json",
      "expected_behavior": "answer the locally verifiable fact with no invented support",
      "rubric": "factuality, instruction following, format, completeness, safety, latency",
      "scores": {
        "factuality": 2,
        "instruction_following": 2,
        "format_validity": 2,
        "completeness": 2,
        "safety": 2,
        "latency_acceptability": 2
      },
      "human_review": "accepted by reviewer",
      "latency_ms": 2400,
      "benchmark_artifact": "LLM/Study/Local LLM Inference Benchmark Log.md",
      "decision": "pass",
      "failure_owner": "quality",
      "next_action": "promote this row to result synthesis"
    }
  ]
}
```

`prompt_artifact`, `response_artifact`, `proof`, `benchmark_artifact`, `evaluation_set_design`, `judge_calibration_artifact`, `reasoning_budget_audit`, `rag_evidence`, `citation_audit`, `tool_evidence`, and `review_artifact` may be absolute paths, vault-relative paths, Obsidian note paths, or Obsidian links.

## Row Contract

| Field | Required when | Meaning |
|---|---|---|
| `case_id` | always | stable id for one prompt-suite case |
| `status` or `decision` | always | `pass`, `hold`, or `fail` for the saved case |
| `candidate_id`, `model_id`, `runtime` | always, unless inherited from manifest | identifies the local setup being scored |
| `task_class` | always | known-answer, schema, extraction, long-context, RAG, multi-turn, tool, constraint, domain-specific, or workload-specific |
| `prompt_artifact` | always | saved prompt, request JSON, or redacted prompt card |
| `response_artifact` | always | saved response, output text, transcript, or tool/RAG answer artifact |
| `expected_behavior`, `rubric`, or `pass_criteria` | always | written standard for judging the case |
| `scores` | always for pass | 0/1/2 dimensions or equivalent top-level fields |
| `source_type` and `split` | acceptance decisions | private/local/held-out, public benchmark, synthetic, or learning-only |
| `judge_calibration_artifact` | LLM-as-judge used | proof that judge order, agreement, and bias checks exist |
| `reasoning_budget_audit` | reasoning or thinking mode supports the decision | proof that quality gain justifies latency, parser, and trace policy cost |
| `rag_evidence` or `citation_audit` | RAG/citation task | retrieval, selected context, citation support, and missing-evidence behavior |
| `tool_evidence` | tool or function task | schema, policy, execution or denial, tool result, and final answer grounding |
| `failure_owner` and `next_action` | hold or fail | one owner and one controlled rerun or rejection step |

Use `waived_dimensions` only when a dimension is truly out of scope for that case, and write why in `waiver_reason`.

## Standard-Library Runner

Save this as `local_llm_quality_evaluation_runner.py` inside the run folder. It uses only Python's standard library.

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


STATUS_VALUES = {
    "pass": "pass",
    "passed": "pass",
    "ready": "pass",
    "complete": "pass",
    "accepted": "pass",
    "keep": "pass",
    "hold": "hold",
    "partial": "hold",
    "incomplete": "hold",
    "gap": "hold",
    "missing": "hold",
    "rerun": "hold",
    "tune": "hold",
    "fail": "fail",
    "failed": "fail",
    "reject": "fail",
    "rejected": "fail",
    "unsafe": "fail",
    "error": "fail",
}

STATUS_RANK = {"pass": 0, "hold": 1, "fail": 2}
LINK_OPEN = "[" + "["
LINK_CLOSE = "]" + "]"

DEFAULT_DIMENSIONS = [
    "factuality",
    "instruction_following",
    "format_validity",
    "completeness",
    "safety",
    "latency_acceptability",
]

DIMENSION_ALIASES = {
    "fact": "factuality",
    "facts": "factuality",
    "groundedness": "factuality",
    "instruction": "instruction_following",
    "instructions": "instruction_following",
    "instr": "instruction_following",
    "format": "format_validity",
    "schema": "format_validity",
    "json": "format_validity",
    "complete": "completeness",
    "coverage": "completeness",
    "safe": "safety",
    "boundary": "safety",
    "constraint": "safety",
    "latency": "latency_acceptability",
    "performance": "latency_acceptability",
    "speed": "latency_acceptability",
}

ACCEPTANCE_USES = {
    "acceptance",
    "model_selection",
    "runtime_selection",
    "deployment",
    "result_synthesis",
    "keep",
    "deploy",
}

PUBLIC_SOURCES = {"public", "benchmark", "public_benchmark", "leaderboard", "training_example"}


def utc_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def slug(value: Any) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value or "").strip().lower())
    return text.strip("-") or "local-llm-quality-evaluation"


def norm(value: Any) -> str:
    return str(value or "").strip().lower().replace(" ", "_").replace("-", "_").replace("/", "_")


def text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (list, tuple, set)):
        return ", ".join(text(item) for item in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=True, sort_keys=True)
    return str(value).strip()


def status_value(value: Any) -> str:
    return STATUS_VALUES.get(norm(value), "hold")


def bool_value(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if value in (None, ""):
        return default
    key = norm(value)
    if key in {"true", "yes", "y", "1", "pass", "required", "used"}:
        return True
    if key in {"false", "no", "n", "0", "waived", "skip", "skipped"}:
        return False
    return default


def number_value(value: Any) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    raw = text(value)
    if not raw:
        return None
    match = re.search(r"-?\d+(?:\.\d+)?", raw)
    if not match:
        return None
    try:
        return float(match.group(0))
    except ValueError:
        return None


def list_value(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [text(item) for item in value if text(item)]
    if isinstance(value, str):
        stripped = value.strip()
        if not stripped:
            return []
        if stripped.startswith("["):
            try:
                parsed = json.loads(stripped)
                if isinstance(parsed, list):
                    return [text(item) for item in parsed if text(item)]
            except json.JSONDecodeError:
                pass
        return [part.strip() for part in stripped.split(",") if part.strip()]
    return [text(value)] if text(value) else []


def has_text(row: dict[str, Any], *names: str) -> bool:
    return any(text(row.get(name)) for name in names)


def dimension_key(value: str) -> str:
    key = norm(value)
    return DIMENSION_ALIASES.get(key, key)


def score_map(row: dict[str, Any]) -> dict[str, float]:
    scores: dict[str, float] = {}
    raw = row.get("scores") or row.get("rubric_scores") or row.get("dimensions")
    if isinstance(raw, dict):
        for key, value in raw.items():
            number = number_value(value)
            if number is not None:
                scores[dimension_key(str(key))] = number
    for key, value in row.items():
        normalized = dimension_key(str(key))
        if normalized in DEFAULT_DIMENSIONS or normalized.endswith("_score"):
            number = number_value(value)
            if number is not None:
                scores[normalized.removesuffix("_score")] = number
    return scores


def strip_obsidian_link(value: str) -> str:
    raw = value.strip()
    if raw.startswith(LINK_OPEN) and raw.endswith(LINK_CLOSE):
        inner = raw[2:-2]
        return inner.split("|", 1)[0].split("#", 1)[0].strip()
    return raw


def proof_candidates(vault_root: Path, proof: str) -> list[Path]:
    cleaned = strip_obsidian_link(proof)
    if not cleaned:
        return []
    path = Path(cleaned).expanduser()
    candidates: list[Path] = []
    if path.is_absolute():
        candidates.append(path)
        if path.suffix == "":
            candidates.append(path.with_suffix(".md"))
    else:
        candidates.append(vault_root / path)
        if path.suffix == "":
            candidates.append((vault_root / path).with_suffix(".md"))
    return [candidate.resolve() for candidate in candidates]


def proof_exists(vault_root: Path, proof: str) -> bool:
    return any(candidate.exists() for candidate in proof_candidates(vault_root, proof))


def proof_status(vault_root: Path, proof: str) -> tuple[bool, str]:
    candidates = proof_candidates(vault_root, proof)
    if not candidates:
        return False, ""
    for candidate in candidates:
        if candidate.exists():
            return True, str(candidate)
    return False, " | ".join(str(candidate) for candidate in candidates[:3])


def finding(level: str, owner: str, message: str, evidence: str, next_action: str) -> dict[str, str]:
    return {
        "level": level,
        "owner": owner,
        "message": message,
        "evidence": evidence,
        "next_action": next_action,
    }


def md_cell(value: Any) -> str:
    return text(value).replace("|", "\\|").replace("\n", "<br>")


def wiki_link(route: str) -> str:
    if not route:
        return ""
    return LINK_OPEN + route + LINK_CLOSE


def case_identifier(row: dict[str, Any]) -> str:
    return text(row.get("case_id") or row.get("prompt_id") or row.get("id") or row.get("row_id"))


def inherited(row: dict[str, Any], manifest: dict[str, Any], *names: str) -> str:
    for name in names:
        value = text(row.get(name))
        if value:
            return value
    for name in names:
        value = text(manifest.get(name))
        if value:
            return value
    return ""


def decision_use(row: dict[str, Any], manifest: dict[str, Any]) -> set[str]:
    values = list_value(row.get("decision_use")) + list_value(manifest.get("decision_use"))
    scope = text(row.get("decision_scope") or manifest.get("decision_scope"))
    if scope:
        values.append(scope)
    decision = norm(row.get("decision") or row.get("result"))
    if decision:
        values.append(decision)
    return {norm(item) for item in values if item}


def requires_reasoning_audit(row: dict[str, Any]) -> bool:
    if bool_value(row.get("reasoning_used")) or bool_value(row.get("thinking_mode")):
        return True
    joined = " ".join(text(row.get(key)) for key in ("method", "notes", "decision", "rubric", "quality_bar")).lower()
    return any(token in joined for token in ("reasoning", "thinking", "test-time compute", "reasoning_effort", "reasoning.effort"))


def requires_judge_calibration(row: dict[str, Any]) -> bool:
    if bool_value(row.get("judge_used")) or bool_value(row.get("llm_as_judge")):
        return True
    joined = " ".join(text(row.get(key)) for key in ("method", "evaluator", "review", "rubric", "notes")).lower()
    return "llm-as-judge" in joined or "llm judge" in joined


def evaluate_case(row: dict[str, Any], manifest: dict[str, Any], vault_root: Path) -> dict[str, Any]:
    cid = case_identifier(row)
    required = bool_value(row.get("required"), True)
    declared_status = status_value(row.get("status") or row.get("decision") or row.get("result"))
    task_class = norm(row.get("task_class") or row.get("class") or row.get("type"))
    candidate_id = inherited(row, manifest, "candidate_id", "selected_candidate", "candidate")
    findings: list[dict[str, str]] = []

    if not cid:
        findings.append(finding("hold", "manifest", "Case id is missing.", text(row), "Give every prompt-suite case a stable case_id."))
    if not required:
        if not has_text(row, "waiver_reason", "out_of_scope_reason"):
            findings.append(finding("hold", "manifest", "Waived case has no waiver reason.", cid, "Explain why this case is not required."))
        status = "hold" if findings else "pass"
        return {
            "case_id": cid or "waived-case",
            "task_class": task_class,
            "candidate_id": candidate_id,
            "status": status,
            "declared_status": declared_status,
            "decision": "waived",
            "score_average": "",
            "score_min": "",
            "proof_exists": False,
            "next_route": "LLM/Study/Local LLM Quality Evaluation Harness",
            "next_action": text(row.get("next_action") or "Keep waiver with the capstone evidence bundle."),
            "findings": findings,
        }

    if not candidate_id:
        findings.append(finding("hold", "model", "Case has no candidate id.", cid, "Set candidate_id or manifest selected_candidate."))
    if not inherited(row, manifest, "model_id", "model"):
        findings.append(finding("hold", "model", "Case has no model id.", cid, "Record the served model id, local tag, or artifact id."))
    if not inherited(row, manifest, "runtime", "provider", "server"):
        findings.append(finding("hold", "runtime", "Case has no runtime.", cid, "Record Ollama, llama.cpp, vLLM, SGLang, LM Studio, or the provider/runtime."))
    if not task_class:
        findings.append(finding("hold", "rubric", "Case has no task class.", cid, "Classify the prompt as known_answer, schema, extraction, long_context, rag, tool, multi_turn, constraint, or domain_specific."))
    if not has_text(row, "expected_behavior", "expected_answer", "pass_criteria", "rubric"):
        findings.append(finding("hold", "rubric", "Case has no expected behavior, pass criteria, or rubric.", cid, "Write the acceptance standard before scoring the answer."))

    prompt_artifact = text(row.get("prompt_artifact") or row.get("prompt_path") or row.get("request_artifact") or row.get("request_path") or row.get("proof"))
    response_artifact = text(row.get("response_artifact") or row.get("response_path") or row.get("output_artifact") or row.get("output_path") or row.get("answer_artifact"))
    prompt_ok, prompt_resolved = proof_status(vault_root, prompt_artifact)
    response_ok, response_resolved = proof_status(vault_root, response_artifact)
    if not prompt_artifact:
        findings.append(finding("hold", "proof", "Case has no prompt artifact.", cid, "Link the saved request, prompt JSON, or redacted prompt card."))
    elif not prompt_ok:
        findings.append(finding("hold", "proof", "Prompt artifact does not resolve.", prompt_resolved, "Fix the prompt_artifact path or save the prompt evidence."))
    if not response_artifact:
        findings.append(finding("hold", "proof", "Case has no response artifact.", cid, "Link the saved response JSON, output text, transcript, or answer artifact."))
    elif not response_ok:
        findings.append(finding("hold", "proof", "Response artifact does not resolve.", response_resolved, "Fix the response_artifact path or save the response evidence."))

    scores = score_map(row)
    required_dimensions = [dimension_key(item) for item in (list_value(row.get("required_dimensions")) or list_value(manifest.get("required_dimensions")) or DEFAULT_DIMENSIONS)]
    waived_dimensions = {dimension_key(item) for item in list_value(row.get("waived_dimensions"))}
    missing_dimensions = [dim for dim in required_dimensions if dim not in scores and dim not in waived_dimensions]
    if missing_dimensions:
        findings.append(finding("hold", "rubric", "Case is missing required score dimensions.", ", ".join(missing_dimensions), "Add 0/1/2 scores or explicitly waive out-of-scope dimensions."))

    pass_threshold = number_value(row.get("pass_threshold") or manifest.get("pass_threshold")) or 1.5
    fail_threshold = number_value(row.get("fail_threshold") or manifest.get("fail_threshold"))
    if fail_threshold is None:
        fail_threshold = 1.0
    numeric_scores = [scores[dim] for dim in required_dimensions if dim in scores]
    if declared_status == "pass" and not numeric_scores:
        findings.append(finding("hold", "rubric", "Passing case has no numeric rubric scores.", cid, "Add score dimensions before declaring the case pass."))
    low_scores = [(dim, scores[dim]) for dim in required_dimensions if dim in scores and scores[dim] < pass_threshold]
    failing_scores = [(dim, score) for dim, score in low_scores if score < fail_threshold]
    if failing_scores:
        detail = ", ".join(f"{dim}={score:g}" for dim, score in failing_scores)
        findings.append(finding("fail", "rubric", "Required score is below the fail threshold.", detail, "Reject or rerun after fixing the failed quality dimension."))
    elif low_scores:
        detail = ", ".join(f"{dim}={score:g}" for dim, score in low_scores)
        findings.append(finding("hold", "rubric", "Required score is below the pass threshold.", detail, "Tune the prompt, model, RAG, tool boundary, or runtime and rerun this case."))

    source_type = norm(row.get("source_type") or row.get("source") or manifest.get("source_type"))
    split = norm(row.get("split") or row.get("eval_split"))
    uses = decision_use(row, manifest)
    if uses & ACCEPTANCE_USES and source_type in PUBLIC_SOURCES and split not in {"heldout", "private", "local"}:
        findings.append(finding("hold", "contamination", "Acceptance case relies on public or benchmark source without held-out/private coverage.", source_type or split, "Add private/local held-out rows or mark this case learning-only."))

    if requires_judge_calibration(row) and not has_text(row, "judge_calibration_artifact", "judge_calibration", "calibration_proof", "human_calibration"):
        findings.append(finding("hold", "judge", "LLM-as-judge case has no calibration proof.", cid, "Run Local LLM Judge Calibration Runner or link AB/BA human agreement evidence."))
    if requires_reasoning_audit(row) and not has_text(row, "reasoning_budget_audit", "reasoning_budget", "test_time_compute_audit"):
        findings.append(finding("hold", "reasoning", "Reasoning-backed case has no reasoning-budget audit.", cid, "Run Local LLM Reasoning Budget and Test-Time Compute Runner or link its output."))
    if "rag" in task_class or "citation" in task_class or "ground" in task_class:
        if not has_text(row, "rag_evidence", "retrieval_evidence", "citation_audit", "selected_context", "context_artifact"):
            findings.append(finding("hold", "rag", "RAG or citation case has no retrieval/citation proof.", cid, "Link retrieval hits, selected context, citation audit, or RAG evidence runner output."))
    if "tool" in task_class or "function" in task_class:
        if not has_text(row, "tool_evidence", "tool_trace", "schema_artifact", "policy_evidence", "tool_result"):
            findings.append(finding("hold", "tool", "Tool case has no tool/schema/policy proof.", cid, "Link schema validation, policy, execution or denial, tool result, and final answer evidence."))

    if declared_status == "fail":
        findings.append(finding("fail", "decision", "Case is explicitly marked fail.", cid, "Fix or reject the case before using this quality gate."))
    elif declared_status != "pass":
        findings.append(finding("hold", "decision", "Case is not marked pass.", declared_status, "Set status to pass only after prompt, response, rubric, and boundary evidence are complete."))
    if declared_status in {"hold", "fail"} and not (has_text(row, "failure_owner", "owner") and has_text(row, "next_action", "rerun_plan")):
        findings.append(finding("hold", "action", "Hold/fail case has no failure owner and next action.", cid, "Name the owner and one controlled rerun, tune, replacement, or rejection step."))

    status = "fail" if any(item["level"] == "fail" for item in findings) else "hold" if findings else "pass"
    if status != "pass":
        first = findings[0]
        next_action = first["next_action"]
    else:
        next_action = text(row.get("next_action") or "Promote this quality row to result synthesis or deployment readiness.")
    return {
        "case_id": cid,
        "task_class": task_class,
        "candidate_id": candidate_id,
        "status": status,
        "declared_status": declared_status,
        "decision": text(row.get("decision") or row.get("result") or declared_status),
        "score_average": round(sum(numeric_scores) / len(numeric_scores), 3) if numeric_scores else "",
        "score_min": min(numeric_scores) if numeric_scores else "",
        "proof_exists": prompt_ok and response_ok,
        "next_route": text(row.get("next_route") or "LLM/Study/Local LLM Quality Evaluation Harness"),
        "next_action": next_action,
        "findings": findings,
    }


def evaluate_manifest(manifest: dict[str, Any], evaluated: list[dict[str, Any]], vault_root: Path) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not has_text(manifest, "workload", "task", "workflow"):
        findings.append(finding("hold", "workload", "Manifest has no workload.", "manifest", "Name the workload this quality gate decides."))
    if not has_text(manifest, "selected_candidate", "candidate_id", "candidate"):
        findings.append(finding("hold", "model", "Manifest has no selected candidate.", "manifest", "Name the candidate being accepted, held, or rejected."))
    if not has_text(manifest, "quality_bar", "acceptance_bar", "success_rubric"):
        findings.append(finding("hold", "rubric", "Manifest has no quality bar.", "manifest", "State what pass, hold, and fail mean for this workload."))
    if not has_text(manifest, "evaluation_set_design", "eval_set_design", "prompt_suite_design", "eval_set_design_waiver"):
        findings.append(finding("hold", "evaluation_set", "Manifest has no evaluation-set design proof.", "manifest", "Run Local LLM Evaluation Set Design Runner or add an explicit waiver."))
    else:
        proof = text(manifest.get("evaluation_set_design") or manifest.get("eval_set_design") or manifest.get("prompt_suite_design"))
        if proof and not proof_exists(vault_root, proof):
            findings.append(finding("hold", "evaluation_set", "Evaluation-set design proof does not resolve.", proof, "Fix the evaluation_set_design link or save the design runner output."))

    minimum_cases = int(number_value(manifest.get("minimum_cases")) or 1)
    required_cases = [row for row in evaluated if row.get("decision") != "waived"]
    if len(required_cases) < minimum_cases:
        findings.append(finding("hold", "coverage", "Manifest has fewer required cases than minimum_cases.", f"{len(required_cases)} < {minimum_cases}", "Add enough prompt-suite cases before accepting the quality decision."))

    required_classes = {norm(item) for item in list_value(manifest.get("required_task_classes"))}
    if required_classes:
        present_classes = {norm(row.get("task_class")) for row in evaluated if row.get("status") == "pass"}
        missing = sorted(required_classes - present_classes)
        if missing:
            findings.append(finding("hold", "coverage", "Required task classes are not passed.", ", ".join(missing), "Add or complete cases for the missing task classes."))
    if not any(row.get("status") == "pass" for row in evaluated):
        findings.append(finding("hold", "coverage", "No quality case is passing.", "manifest", "Complete at least one case before using this run as quality evidence."))
    return findings


def load_manifest() -> tuple[Path, dict[str, Any]]:
    manifest_path = (
        os.environ.get("LOCAL_LLM_QUALITY_EVALUATION_MANIFEST")
        or os.environ.get("LOCAL_LLM_QUALITY_EVALUATION_AUDIT_MANIFEST")
    )
    if not manifest_path:
        raise ValueError("Set LOCAL_LLM_QUALITY_EVALUATION_MANIFEST to a JSON manifest path.")
    path = Path(manifest_path).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"Manifest path does not exist: {path}")
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError("Manifest must be a JSON object.")
    return path, data


def csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "case_id",
        "task_class",
        "candidate_id",
        "status",
        "declared_status",
        "decision",
        "score_average",
        "score_min",
        "proof_exists",
        "next_route",
        "next_action",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def markdown_report(record: dict[str, Any]) -> str:
    lines = [
        f"# Local LLM Quality Evaluation - {record['run_id']}",
        "",
        f"- Generated: `{record['generated_at']}`",
        f"- Workload: `{record['workload']}`",
        f"- Selected candidate: `{record['selected_candidate']}`",
        f"- Status: `{record['status']}/{record['decision']}`",
        f"- Cases: `{record['case_count']}`",
        f"- Findings: `{record['finding_count']}`",
        "",
        "## Cases",
        "",
        "| Case | Task class | Candidate | Status | Avg score | Proof exists | Next route |",
        "|---|---|---|---|---|---|---|",
    ]
    for row in record["cases"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    md_cell(row["case_id"]),
                    md_cell(row["task_class"]),
                    md_cell(row["candidate_id"]),
                    md_cell(row["status"]),
                    md_cell(row["score_average"]),
                    md_cell(row["proof_exists"]),
                    md_cell(wiki_link(row["next_route"])),
                ]
            )
            + " |"
        )
    incomplete = [row for row in record["cases"] if row["status"] != "pass"]
    if record["findings"] or incomplete:
        lines.extend(["", "## Next Actions", ""])
        for item in record["findings"]:
            lines.append(f"- `{item['owner']}`: {item['message']} Next: {item['next_action']}")
        for row in incomplete:
            lines.append(f"- `{row['case_id']}` -> {wiki_link(row['next_route'])}: {row['next_action']}")
    return "\n".join(lines) + "\n"


def main() -> int:
    manifest_path, manifest = load_manifest()
    run_id = text(manifest.get("run_id")) or slug(manifest_path.stem)
    run_root = (
        os.environ.get("LOCAL_LLM_QUALITY_EVALUATION_RUN_ROOT")
        or os.environ.get("LOCAL_LLM_QUALITY_EVALUATION_AUDIT_RUN_ROOT")
        or manifest.get("run_root")
        or manifest_path.parent
    )
    run_dir = Path(str(run_root)).expanduser().resolve()
    run_dir.mkdir(parents=True, exist_ok=True)
    vault_root = Path(
        str(
            os.environ.get("LOCAL_LLM_QUALITY_EVALUATION_VAULT_ROOT")
            or os.environ.get("LOCAL_LLM_QUALITY_EVALUATION_AUDIT_VAULT_ROOT")
            or manifest.get("vault_root")
            or Path.cwd()
        )
    ).expanduser().resolve()

    cases = manifest.get("cases")
    if cases is None:
        cases = manifest.get("rows")
    if not isinstance(cases, list) or not all(isinstance(row, dict) for row in cases):
        raise ValueError("Manifest cases must be a list of objects.")

    evaluated = [evaluate_case(dict(row), manifest, vault_root) for row in cases]
    manifest_findings = evaluate_manifest(manifest, evaluated, vault_root)
    all_findings = manifest_findings + [finding for row in evaluated for finding in row["findings"]]
    status = "fail" if any(item["level"] == "fail" for item in all_findings) else "hold" if all_findings else "pass"
    decision = {
        "pass": "quality_evaluation_ready",
        "hold": "quality_evaluation_incomplete",
        "fail": "quality_evaluation_failed",
    }[status]

    prefix = slug(f"{run_id}-quality-evaluation")
    json_path = run_dir / f"{prefix}.json"
    md_path = run_dir / f"{prefix}.md"
    csv_path = run_dir / f"{prefix}.csv"
    jsonl_path = run_dir / "local-llm-quality-evaluation-runs.jsonl"
    record = {
        "run_id": run_id,
        "generated_at": utc_iso(),
        "manifest_path": str(manifest_path),
        "vault_root": str(vault_root),
        "workload": text(manifest.get("workload") or manifest.get("task") or manifest.get("workflow")),
        "selected_candidate": text(manifest.get("selected_candidate") or manifest.get("candidate_id") or manifest.get("candidate")),
        "quality_bar": text(manifest.get("quality_bar") or manifest.get("acceptance_bar") or manifest.get("success_rubric")),
        "status": status,
        "decision": decision,
        "case_count": len(evaluated),
        "finding_count": len(all_findings),
        "findings": all_findings,
        "cases": evaluated,
        "outputs": {
            "json": str(json_path),
            "markdown": str(md_path),
            "csv": str(csv_path),
            "jsonl": str(jsonl_path),
        },
    }
    json_path.write_text(json.dumps(record, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    md_path.write_text(markdown_report(record), encoding="utf-8")
    csv_write(csv_path, evaluated)
    with jsonl_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps({"run_id": run_id, "generated_at": record["generated_at"], "status": status, "decision": decision, "json": str(json_path)}, ensure_ascii=True) + "\n")
    print(json.dumps({
        "status": status,
        "decision": decision,
        "run_id": run_id,
        "case_count": len(evaluated),
        "finding_count": len(all_findings),
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
$env:LOCAL_LLM_QUALITY_EVALUATION_MANIFEST = "D:\llm-runs\quality-eval\quality-eval-manifest.json"
$env:LOCAL_LLM_QUALITY_EVALUATION_VAULT_ROOT = "D:\Vaults\PersonalKB"
$env:LOCAL_LLM_QUALITY_EVALUATION_RUN_ROOT = "D:\llm-runs\quality-eval"
python .\local_llm_quality_evaluation_runner.py
```

## Reading The Result

| Runner status | Meaning | Next route |
|---|---|---|
| `pass/quality_evaluation_ready` | all required cases pass, proof links resolve, rubric dimensions meet the threshold, and boundary-specific evidence exists | promote the output to [[LLM/Study/Local LLM Result Synthesis Runner|Local LLM Result Synthesis Runner]] |
| `hold/quality_evaluation_incomplete` | prompt, response, rubric, evaluation-set, judge, reasoning, RAG, tool, or next-action evidence is missing | complete the first held case and rerun |
| `fail/quality_evaluation_failed` | at least one required case fails, a required score is below the fail threshold, or the decision explicitly rejects the row | fix the failed quality dimension, change model/runtime, or reject the candidate |

## Capstone Row

| Gate | Required artifact | Pass signal |
|---|---|---|
| Quality evaluation runner | `<run-id>-quality-evaluation.json`, `<run-id>-quality-evaluation.md`, `<run-id>-quality-evaluation.csv`, and one `local-llm-quality-evaluation-runs.jsonl` row | prompt-suite cases have saved prompt/response proof, rubric scores, boundary-specific evidence, and pass/hold/fail decisions before result synthesis or deployment readiness depends on quality |

## Completion Gate

- [ ] workload, selected candidate, and quality bar are explicit
- [ ] evaluation-set design proof or a written waiver is linked
- [ ] every required case has prompt and response artifacts
- [ ] every required case has expected behavior, rubric, or pass criteria
- [ ] required score dimensions are present or explicitly waived
- [ ] public benchmark rows do not carry the acceptance decision by themselves
- [ ] LLM-as-judge rows link judge calibration output
- [ ] reasoning-backed rows link reasoning-budget audit output
- [ ] RAG/citation and tool cases link their boundary-specific proof
- [ ] every hold/fail case has a failure owner and next action

## References

- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Evaluation Set Design Runner]]
- [[LLM/Study/Local LLM First Quality Probe Runner]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM First Client Harness Runner]]
- [[LLM/Study/Decoding and Sampling Controls Runner]]
- [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Runner]]
- [[LLM/Study/Local LLM Judge Calibration Runner]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Result Synthesis Runner]]
- [[LLM/Study/LLM Deployment Readiness Audit Runner]]
- [[LLM/Study/Local RAG Evidence Runner]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Runner]]
- [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]]
- [[LLM/2023 — Open Models and Agents/LLM-as-Judge]]
- [[LLM/2022 — Alignment and Chat/Human Evaluation and Preference Studies]]
- [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes]]
- [[LLM/2020–2021 — The Scaling Era/Contamination and Data Leakage]]
