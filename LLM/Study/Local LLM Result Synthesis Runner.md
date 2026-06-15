---
tags: [study, llm, inference, local-llm, decision, evaluation, deployment, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice, deep-dive]
last-verified: 2026-06-15
---

# Local LLM Result Synthesis Runner

> **One-line summary** A local model decision is ready only when endpoint, compatibility, benchmark, evaluation-set, quality, safety, and operations evidence point to the same keep, tune, reject, or deploy action.

Use this after [[LLM/Study/Local LLM Model Selection Runner|Local LLM Model Selection Runner]], [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner|Local LLM OpenAI-Compatible API Contract Runner]], [[LLM/Study/Local LLM Inference Metrics Field Guide|Local LLM Inference Metrics Field Guide]], [[LLM/Study/Local LLM Evaluation Set Design Runner|Local LLM Evaluation Set Design Runner]], [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]], and [[LLM/Study/Local LLM Quality Evaluation Runner|Local LLM Quality Evaluation Runner]] have evidence rows. If the decision is tune, train, serve an adapter, or explicitly avoid training, include [[LLM/Study/LLM Adaptation and Fine-Tuning Readiness Runner|LLM Adaptation and Fine-Tuning Readiness Runner]] output. Use this before [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]] so the final deployment memo starts from a reconciled local model/runtime decision, not a pile of unrelated artifacts.

This runner does not call a model, benchmark an endpoint, scrape model pages, or choose a current model by name. It audits the evidence already collected for one workload and selected candidate.

## What This Proves

| Evidence family | Checks | Why it matters |
|---|---|---|
| Workload and candidate | workload, quality bar, selected candidate, rejected alternative | keeps the decision tied to one job and one comparison set |
| Custody and compatibility | model id, artifact, license/source, runtime, tokenizer/template/API route | prevents mistaking a vague model name for a reproducible local setup |
| Endpoint and client | base URL, model-list, request/response, harmless failure or API contract | proves inference is callable outside a UI |
| Benchmark and metrics | latency, throughput, memory/context, interpretation | prevents quality-only decisions that cannot serve the workload |
| Evaluation and quality | evaluation-set design, held-out/private prompts, rubric, pass/hold/fail | prevents benchmark or vibe scores from replacing local acceptance |
| Security and operations | exposure, data/log boundary, owner, startup/restart/observability | separates a one-off experiment from a maintained local service |
| Decision synthesis | contradictions, missing critical proof, next owner, retest trigger | turns evidence into keep, tune, reject, or deployment-memo readiness |

Academic bridge: this is where mechanism knowledge becomes engineering judgment. Tokenization/template mistakes, context/KV-cache limits, prefill/decode latency, quantization effects, scheduler behavior, and evaluation contamination all become explicit blockers or reasons for the final decision.

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "local-decision-001",
  "run_root": "D:/llm-runs/result-synthesis",
  "vault_root": "D:/Vaults/PersonalKB",
  "workload": "private local research assistant",
  "decision_scope": "choose local GPU candidate for personal notes",
  "selected_candidate": "ollama-qwen-small",
  "service_mode": "personal_loopback",
  "candidates": [
    {
      "candidate_id": "ollama-qwen-small",
      "model_id": "qwen-example",
      "runtime": "Ollama",
      "artifact": "runtime tag or GGUF path",
      "source": "model card or local provenance row",
      "license": "acceptable"
    }
  ],
  "evidence": [
    {
      "id": "quality",
      "kind": "quality",
      "candidate_id": "ollama-qwen-small",
      "status": "pass",
      "proof": "D:/llm-runs/quality-eval/quality-eval-quality-evaluation.md",
      "quality_evaluation_runner": "D:/llm-runs/quality-eval/quality-eval-quality-evaluation.json",
      "eval_set_design": "D:/llm-runs/eval-set-design/eval-set-design.json",
      "rubric": "factuality, grounding, format, safety",
      "result": "pass",
      "failure_owner": "quality",
      "decision": "keep"
    }
  ]
}
```

`proof` may be an absolute path, a vault-relative path, an Obsidian note path, or an Obsidian link. If a required row is not applicable, set `required` to `false` and include `waiver_reason`.

## Evidence Kinds

By default, the runner expects these evidence kinds unless `required_kinds` overrides them:

| Kind | Required signal |
|---|---|
| `workload` | workload/task, data boundary, quality bar, latency or batch target |
| `model_selection` | shortlist or candidate reason plus selected candidate |
| `model_custody` | model id/source/license/artifact/revision or local path |
| `runtime_compatibility` | runtime, tokenizer/template or API route, artifact format |
| `endpoint_client` | base URL/route, model-list or chat evidence, request/response/client proof |
| `api_contract` | `/v1/models`, chat, stream or explicit non-streaming scope, and harmless failure |
| `benchmark` | TTFT/TPOT/tokens/sec/latency/memory/context plus interpretation |
| `evaluation_set_design` | held-out/private prompt-suite design and contamination/rubric proof |
| `quality` | quality evaluation runner output, rubric, result/score, failure owner or next action; reasoning-budget audit when thinking mode supports the quality decision |
| `security_privacy` | endpoint exposure, data boundary, log/export boundary |
| `operations` | owner, startup/restart, observability, backup/rollback or one-off waiver |
| `rejected_alternative` | rejected candidate/path plus measured or policy reason |
| `review_trigger` | what change invalidates the decision and who reruns it |

## Standard-Library Runner

Save this as `local_llm_result_synthesis_runner.py` inside the run folder. It uses only Python's standard library.

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


DEFAULT_REQUIRED_KINDS = [
    "workload",
    "model_selection",
    "model_custody",
    "runtime_compatibility",
    "endpoint_client",
    "api_contract",
    "benchmark",
    "evaluation_set_design",
    "quality",
    "security_privacy",
    "operations",
    "rejected_alternative",
    "review_trigger",
]

KIND_ALIASES = {
    "workload_contract": "workload",
    "candidate_selection": "model_selection",
    "shortlist": "model_selection",
    "custody": "model_custody",
    "provenance": "model_custody",
    "compatibility": "runtime_compatibility",
    "runtime": "runtime_compatibility",
    "endpoint": "endpoint_client",
    "client": "endpoint_client",
    "api": "api_contract",
    "api_client": "api_contract",
    "performance": "benchmark",
    "benchmark_performance": "benchmark",
    "eval_set": "evaluation_set_design",
    "eval_set_design": "evaluation_set_design",
    "prompt_suite_design": "evaluation_set_design",
    "quality_evaluation": "quality",
    "security": "security_privacy",
    "privacy": "security_privacy",
    "ops": "operations",
    "operations_lifecycle": "operations",
    "rejected": "rejected_alternative",
    "alternative": "rejected_alternative",
    "retest": "review_trigger",
}

STATUS_VALUES = {
    "pass": "pass",
    "passed": "pass",
    "complete": "pass",
    "ready": "pass",
    "ok": "pass",
    "keep": "pass",
    "hold": "hold",
    "blocked": "hold",
    "gap": "hold",
    "missing": "hold",
    "pending": "hold",
    "in-progress": "hold",
    "in progress": "hold",
    "tune": "hold",
    "rerun": "hold",
    "fail": "fail",
    "failed": "fail",
    "reject": "fail",
    "rejected": "fail",
    "unsafe": "fail",
    "error": "fail",
}

STATUS_RANK = {"pass": 0, "hold": 1, "fail": 2}
KIND_ORDER = {name: index for index, name in enumerate(DEFAULT_REQUIRED_KINDS)}
LINK_OPEN = "[" + "["
LINK_CLOSE = "]" + "]"


def utc_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def slug(value: Any) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value or "").strip().lower())
    return text.strip("-") or "local-llm-result-synthesis"


def norm(value: Any) -> str:
    return str(value or "").strip().lower().replace(" ", "_").replace("-", "_").replace("/", "_")


def display(value: Any) -> str:
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=True)
    return str(value if value is not None else "")


def status_value(value: Any) -> str:
    return STATUS_VALUES.get(norm(value).replace("_", "-"), "hold")


def bool_value(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if value in (None, ""):
        return default
    text = norm(value)
    if text in {"true", "yes", "y", "1", "required", "critical", "applicable", "maintained"}:
        return True
    if text in {"false", "no", "n", "0", "optional", "waived", "not_required", "not_applicable", "one_off"}:
        return False
    return default


def number_value(value: Any) -> float | None:
    if isinstance(value, (int, float)):
        return float(value)
    if value in (None, ""):
        return None
    try:
        return float(str(value).strip())
    except ValueError:
        return None


def list_value(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, tuple):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str):
        stripped = value.strip()
        if not stripped:
            return []
        if stripped.startswith("["):
            try:
                parsed = json.loads(stripped)
                if isinstance(parsed, list):
                    return [str(item).strip() for item in parsed if str(item).strip()]
            except json.JSONDecodeError:
                pass
        return [part.strip() for part in stripped.split(",") if part.strip()]
    return [str(value).strip()] if str(value).strip() else []


def load_manifest() -> tuple[Path, dict[str, Any]]:
    manifest_path = os.environ.get("LOCAL_LLM_RESULT_SYNTHESIS_MANIFEST")
    if not manifest_path:
        raise ValueError("Set LOCAL_LLM_RESULT_SYNTHESIS_MANIFEST to a JSON manifest path.")
    path = Path(manifest_path).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"Manifest path does not exist: {path}")
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError("Manifest must be a JSON object.")
    return path, data


def strip_obsidian_link(value: str) -> str:
    text = value.strip()
    if text.startswith(LINK_OPEN) and text.endswith(LINK_CLOSE):
        inner = text[2:-2]
        return inner.split("|", 1)[0].split("#", 1)[0].strip()
    return text


def proof_candidates(vault_root: Path, proof: str) -> list[Path]:
    proof_text = strip_obsidian_link(proof)
    if not proof_text:
        return []
    path = Path(proof_text).expanduser()
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


def proof_exists(vault_root: Path, proof: str) -> tuple[bool, str]:
    if not proof.strip():
        return False, ""
    candidates = proof_candidates(vault_root, proof)
    for candidate in candidates:
        if candidate.exists():
            return True, str(candidate)
    return False, str(candidates[0]) if candidates else proof


def has_text(row: dict[str, Any], *names: str) -> bool:
    return any(str(row.get(name) or "").strip() for name in names)


def metric_value(row: dict[str, Any], *names: str) -> Any:
    metrics = row.get("metrics") if isinstance(row.get("metrics"), dict) else {}
    for name in names:
        if row.get(name) not in (None, ""):
            return row.get(name)
        if metrics.get(name) not in (None, ""):
            return metrics.get(name)
    return None


def has_any_metric(row: dict[str, Any], names: tuple[str, ...]) -> bool:
    return any(metric_value(row, name) is not None for name in names)


def finding(level: str, owner: str, text: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "owner": owner,
        "finding": text,
        "evidence": evidence,
        "action": action,
    }


def canonical_kind(value: Any) -> str:
    kind = norm(value)
    return KIND_ALIASES.get(kind, kind)


def candidate_id(row: dict[str, Any]) -> str:
    return str(row.get("candidate_id") or row.get("candidate") or row.get("id") or "").strip()


def evaluate_candidate(row: dict[str, Any], selected: str) -> dict[str, Any]:
    cid = candidate_id(row)
    findings: list[dict[str, str]] = []
    if not cid:
        findings.append(finding("hold", "candidate", "Candidate id is missing.", display(row), "Give every candidate a stable candidate_id."))
    if not has_text(row, "model_id", "model", "model_family"):
        findings.append(finding("hold", "candidate", "Candidate has no model id or family.", cid, "Record the served model id, local tag, or model family."))
    if not has_text(row, "runtime", "provider", "server"):
        findings.append(finding("hold", "runtime", "Candidate has no runtime.", cid, "Name Ollama, LM Studio, llama.cpp, vLLM, SGLang, hosted API, or batch engine."))
    if not has_text(row, "artifact", "local_path", "revision", "tag"):
        findings.append(finding("hold", "custody", "Candidate has no artifact, local path, revision, or tag.", cid, "Link model custody or artifact provenance evidence."))
    if not has_text(row, "source", "model_card", "license"):
        findings.append(finding("hold", "custody", "Candidate has no source, model card, or license field.", cid, "Record source and license before accepting the candidate."))

    status = "fail" if any(item["level"] == "fail" for item in findings) else "hold" if findings else "pass"
    return {
        "candidate_id": cid,
        "model": str(row.get("model_id") or row.get("model") or row.get("model_family") or ""),
        "runtime": str(row.get("runtime") or row.get("provider") or row.get("server") or ""),
        "artifact": str(row.get("artifact") or row.get("local_path") or row.get("revision") or row.get("tag") or ""),
        "selected": cid == selected,
        "status": status,
        "findings": findings,
    }


def evaluate_kind_requirements(row: dict[str, Any], kind: str, manifest: dict[str, Any], findings: list[dict[str, str]]) -> None:
    owner = kind
    if kind == "workload":
        if not (has_text(row, "workload", "task", "workflow") or has_text(manifest, "workload")):
            findings.append(finding("hold", owner, "Workload row has no named workload.", kind, "Name the task this model/runtime decision serves."))
        if not has_text(row, "data_boundary", "data_sensitivity", "privacy_boundary"):
            findings.append(finding("hold", owner, "Workload row has no data or privacy boundary.", kind, "Classify public, personal, private, regulated, secret, or mixed data."))
        if not has_text(row, "quality_bar", "success_rubric", "acceptance_bar"):
            findings.append(finding("hold", owner, "Workload row has no quality bar.", kind, "State what pass, hold, and fail mean for the workload."))
        if not has_text(row, "latency_target", "throughput_target", "batch_window"):
            findings.append(finding("hold", owner, "Workload row has no latency, throughput, or batch target.", kind, "Add an interactive latency target, throughput target, or batch window."))
    elif kind == "model_selection":
        if not has_text(row, "candidate_id", "selected_candidate", "shortlist", "rank"):
            findings.append(finding("hold", owner, "Model-selection row has no candidate or shortlist evidence.", kind, "Link Local LLM Model Selection Runner output or write the shortlist reason."))
        if not has_text(row, "reason", "decision", "selection_reason", "rejection_trigger"):
            findings.append(finding("hold", owner, "Model-selection row has no selection reason.", kind, "Explain why this candidate was tried before alternatives."))
    elif kind == "model_custody":
        if not has_text(row, "model_id", "model", "model_family"):
            findings.append(finding("hold", owner, "Custody row has no model id.", kind, "Record exact model id, family, local tag, or served id."))
        if not has_text(row, "source", "model_card", "license"):
            findings.append(finding("hold", owner, "Custody row has no source/model-card/license evidence.", kind, "Link model card, license, and source-check evidence."))
        if not has_text(row, "artifact", "revision", "tag", "local_path", "hash"):
            findings.append(finding("hold", owner, "Custody row has no artifact, revision, local path, or hash.", kind, "Record the exact bytes or runtime package under test."))
    elif kind == "runtime_compatibility":
        if not has_text(row, "runtime", "provider", "server"):
            findings.append(finding("hold", owner, "Compatibility row has no runtime.", kind, "Name the runtime or provider."))
        if not has_text(row, "tokenizer", "chat_template", "template_runner", "api_route", "artifact_format"):
            findings.append(finding("hold", owner, "Compatibility row has no tokenizer/template/API/artifact-format evidence.", kind, "Link runtime compatibility or template/tokenizer runner output."))
    elif kind == "endpoint_client":
        if not has_text(row, "base_url", "route", "request_path", "client", "api_contract"):
            findings.append(finding("hold", owner, "Endpoint row has no base URL, route, request, client, or contract evidence.", kind, "Link endpoint or client proof."))
        if not has_text(row, "model_list", "chat_call", "response", "output_path", "streaming"):
            findings.append(finding("hold", owner, "Endpoint row has no model-list, chat, response, output, or streaming evidence.", kind, "Prove the route can answer outside a UI."))
    elif kind == "api_contract":
        if not has_text(row, "models_route", "model_list", "models_result"):
            findings.append(finding("hold", owner, "API contract row has no model-list proof.", kind, "Run or link the OpenAI-compatible API contract runner."))
        if not has_text(row, "chat_call", "chat_result", "non_streaming", "streaming"):
            findings.append(finding("hold", owner, "API contract row has no chat or streaming scope proof.", kind, "Record chat behavior and whether streaming is supported or out of scope."))
        if not has_text(row, "wrong_model_failure", "harmless_failure", "error_shape"):
            findings.append(finding("hold", owner, "API contract row has no harmless failure evidence.", kind, "Record wrong-model or invalid-request behavior."))
    elif kind == "benchmark":
        metric_names = ("ttft_ms", "time_to_first_token_ms", "tpot_ms", "tokens_per_second", "total_latency_ms", "p95_latency_ms", "peak_vram_mb", "peak_ram_mb", "context_tokens")
        if not has_any_metric(row, metric_names):
            findings.append(finding("hold", owner, "Benchmark row has no latency, throughput, memory, or context metric.", kind, "Add TTFT, TPOT, tokens/sec, total latency, memory, or context evidence."))
        if not has_text(row, "interpretation", "decision", "meets_target", "next_action"):
            findings.append(finding("hold", owner, "Benchmark row has no interpretation.", kind, "State whether performance satisfies, blocks, or redirects the decision."))
    elif kind == "evaluation_set_design":
        if not has_text(row, "eval_set_design", "evaluation_set_design", "prompt_suite_design", "heldout_proof", "proof"):
            findings.append(finding("hold", owner, "Evaluation-set row has no design proof.", kind, "Run Local LLM Evaluation Set Design Runner or link held-out/private prompt-suite evidence."))
        if not has_text(row, "heldout", "private_prompts", "local_prompts", "contamination_control", "rubric"):
            findings.append(finding("hold", owner, "Evaluation-set row lacks held-out/private, contamination, or rubric signal.", kind, "Record held-out/private coverage, contamination control, and rubric."))
    elif kind == "quality":
        if not has_text(row, "rubric", "quality_bar", "prompt_suite", "score", "result"):
            findings.append(finding("hold", owner, "Quality row has no rubric, prompt suite, score, or result.", kind, "Add pass/hold/fail quality evidence for the workload."))
        if not has_text(row, "quality_evaluation_runner", "quality_runner", "quality_audit", "quality_evaluation_audit"):
            findings.append(finding("hold", owner, "Quality row has no quality evaluation runner output.", kind, "Run Local LLM Quality Evaluation Runner or link its JSON/Markdown output before result synthesis depends on quality."))
        if not has_text(row, "failure_owner", "next_action", "decision") and not has_any_metric(row, ("score", "pass_rate", "win_rate")):
            findings.append(finding("hold", owner, "Quality row has no failure owner, score, or next action.", kind, "Add human score, pass rate, failure owner, or next controlled action."))
        if not has_text(row, "eval_set_design", "evaluation_set_design", "prompt_suite_design", "heldout_proof"):
            findings.append(finding("hold", owner, "Quality row is not tied to evaluation-set design proof.", kind, "Link Local LLM Evaluation Set Design Runner output or a waiver."))
        reasoning_text = " ".join(str(row.get(key, "")) for key in ("method", "notes", "result", "decision", "quality_bar", "rubric")).lower()
        if any(token in reasoning_text for token in ("reasoning", "thinking", "test-time compute", "reasoning_effort", "reasoning.effort")) and not has_text(row, "reasoning_budget_audit", "reasoning_budget", "test_time_compute_audit"):
            findings.append(finding("hold", owner, "Reasoning-backed quality row has no reasoning-budget audit.", kind, "Run Local LLM Reasoning Budget and Test-Time Compute Runner or link its output before result synthesis uses thinking mode as evidence."))
    elif kind == "security_privacy":
        if not has_text(row, "endpoint_exposure", "binding", "host_classification", "network_boundary"):
            findings.append(finding("hold", owner, "Security row has no endpoint exposure or network boundary.", kind, "Record loopback/LAN/public/provider boundary."))
        if not has_text(row, "data_boundary", "privacy_boundary", "rag_boundary", "tool_boundary"):
            findings.append(finding("hold", owner, "Security row has no data boundary.", kind, "Record prompt, corpus, tool, UI, export, and storage boundaries."))
        if not has_text(row, "log_boundary", "secret_scan", "export_boundary", "retention"):
            findings.append(finding("hold", owner, "Security row has no log, secret, retention, or export evidence.", kind, "Add log/config scan or explicit no-log/no-export boundary."))
    elif kind == "operations":
        service_mode = norm(row.get("service_mode") or manifest.get("service_mode"))
        if service_mode in {"one_off", "experiment", "smoke"} and has_text(row, "waiver_reason", "one_off_reason"):
            return
        if not has_text(row, "owner", "operator", "maintenance_owner"):
            findings.append(finding("hold", owner, "Operations row has no owner.", kind, "Name who patches, monitors, restarts, and handles incidents."))
        if not has_text(row, "startup", "restart", "service_mode", "launch_command"):
            findings.append(finding("hold", owner, "Operations row has no startup or restart evidence.", kind, "Record startup mode, launch command, service wrapper, or restart check."))
        if not has_text(row, "observability", "metrics", "logs", "resource_pressure"):
            findings.append(finding("hold", owner, "Operations row has no observability evidence.", kind, "Link model state, metrics, logs, resource pressure, or loaded route evidence."))
    elif kind == "rejected_alternative":
        if not has_text(row, "rejected_candidate", "rejected_path", "alternative", "candidate_id"):
            findings.append(finding("hold", owner, "Rejected-alternative row has no rejected candidate or path.", kind, "Name at least one plausible alternative that lost."))
        if not has_text(row, "reason", "evidence", "quality_reason", "latency_reason", "privacy_reason", "cost_reason", "ops_reason"):
            findings.append(finding("hold", owner, "Rejected-alternative row has no evidence-backed reason.", kind, "Reject with quality, latency, privacy, cost, operations, or policy evidence."))
    elif kind == "review_trigger":
        if not has_text(row, "review_trigger", "retest_trigger", "invalidates_when"):
            findings.append(finding("hold", owner, "Review-trigger row has no retest trigger.", kind, "Write what model, workload, data, traffic, cost, or security change invalidates the decision."))
        if not has_text(row, "owner", "next_action", "rerun_route"):
            findings.append(finding("hold", owner, "Review-trigger row has no owner or next action.", kind, "Name who reruns the synthesis and what route they use."))


def evaluate_evidence_row(row: dict[str, Any], vault_root: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    row_id = str(row.get("id") or row.get("row_id") or row.get("kind") or "")
    kind = canonical_kind(row.get("kind") or row.get("type") or "")
    cid = str(row.get("candidate_id") or row.get("candidate") or manifest.get("selected_candidate") or "")
    proof = str(row.get("proof") or row.get("proof_path") or row.get("evidence_path") or "")
    required = bool_value(row.get("required"), True)
    critical = bool_value(row.get("critical"), kind in DEFAULT_REQUIRED_KINDS)
    declared_status = status_value(row.get("status") or row.get("decision") or row.get("result"))
    findings: list[dict[str, str]] = []

    if not row_id:
        findings.append(finding("hold", "manifest", "Evidence row id is missing.", display(row), "Give every row a stable id."))
    if not kind:
        findings.append(finding("hold", "manifest", "Evidence kind is missing.", row_id, "Use one of the evidence kinds."))
    if kind not in KIND_ORDER:
        findings.append(finding("hold", "manifest", "Evidence kind is not recognized.", kind, "Use a known kind or add a waiver reason."))

    proof_ok = False
    proof_resolved = ""
    if proof:
        proof_ok, proof_resolved = proof_exists(vault_root, proof)
        if not proof_ok:
            findings.append(finding("hold", "proof", "Proof link or path does not resolve in the vault.", proof_resolved, "Fix the proof path or create the linked evidence."))
    elif required:
        findings.append(finding("hold", "proof", "Required evidence row has no proof link or path.", row_id or kind, "Link the source artifact before synthesis."))

    if not required:
        if not has_text(row, "waiver_reason", "out_of_scope_reason", "not_applicable_reason"):
            findings.append(finding("hold", kind or "waiver", "Optional or out-of-scope row has no waiver reason.", row_id or kind, "Record why this evidence is not required."))
    else:
        if declared_status == "fail":
            findings.append(finding("fail", kind, "Evidence row is explicitly failed.", row_id or kind, "Fix or reject the candidate before synthesis."))
        elif declared_status != "pass":
            findings.append(finding("hold", kind, "Evidence row is not marked pass.", declared_status, "Rerun or complete the proof before accepting the decision."))
        if kind in KIND_ORDER:
            evaluate_kind_requirements(row, kind, manifest, findings)

    fail_count = sum(1 for item in findings if item["level"] == "fail")
    hold_count = sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        status = "fail"
    elif hold_count:
        status = "hold"
    else:
        status = "pass"

    return {
        "row_id": row_id,
        "kind": kind,
        "candidate_id": cid,
        "required": required,
        "critical": critical,
        "declared_status": declared_status,
        "status": status,
        "proof": proof,
        "proof_resolved": proof_resolved,
        "proof_exists": proof_ok,
        "next_action": findings[0]["action"] if findings else "Carry this evidence into the decision memo.",
        "findings": findings,
    }


def missing_required_findings(evidence: list[dict[str, Any]], required_kinds: list[str]) -> list[dict[str, str]]:
    present = {row["kind"] for row in evidence if row["kind"] and row["required"]}
    findings = []
    for kind in required_kinds:
        if kind not in present:
            findings.append(finding("hold", kind, "Required evidence kind is missing.", kind, f"Add a {kind} row or waive it with a reason."))
    return findings


def choose_decision(selected_rows: list[dict[str, Any]], all_findings: list[dict[str, str]]) -> tuple[str, str, str]:
    fail_kinds = {row["kind"] for row in selected_rows if row["status"] == "fail"}
    hold_kinds = {row["kind"] for row in selected_rows if row["status"] == "hold"}
    if fail_kinds:
        if "quality" in fail_kinds:
            return "reject_candidate", "Quality evidence failed.", "Reject or adapt the model before deployment."
        if "security_privacy" in fail_kinds:
            return "reject_or_contain_candidate", "Security or privacy evidence failed.", "Fix exposure/data boundaries before any further use."
        if "endpoint_client" in fail_kinds or "api_contract" in fail_kinds:
            return "rerun_endpoint_layer", "Endpoint or client evidence failed.", "Fix route/API contract before judging model quality."
        return "reject_or_rebuild_candidate", f"Failed evidence kinds: {', '.join(sorted(fail_kinds))}.", "Fix failed proof or reject the candidate."
    if all_findings or hold_kinds:
        return "hold_for_missing_or_incomplete_evidence", "Required evidence is incomplete.", "Follow the first held row before making a keep/reject decision."
    return "keep_candidate_for_deployment_memo", "Selected candidate evidence is consistent.", "Write the deployment decision memo and run deployment readiness audit."


def md_cell(value: Any) -> str:
    return display(value).replace("|", "\\|").replace("\n", " ")


def csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = [
        "row_id",
        "kind",
        "candidate_id",
        "required",
        "critical",
        "declared_status",
        "status",
        "proof",
        "proof_resolved",
        "proof_exists",
        "next_action",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({name: row.get(name, "") for name in fieldnames})


def render_markdown(record: dict[str, Any]) -> str:
    lines = [
        f"# Local LLM Result Synthesis - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Selected candidate: `{record['selected_candidate']}`",
        f"- Workload: `{record['workload']}`",
        f"- Summary: {record['decision_reason']}",
        f"- Next action: {record['next_action']}",
        "",
        "## Candidate Rows",
        "",
        "| Candidate | Model | Runtime | Selected | Status |",
        "|---|---|---|---|---|",
    ]
    for row in record["candidates"]:
        lines.append("| " + " | ".join([
            md_cell(row["candidate_id"]),
            md_cell(row["model"]),
            md_cell(row["runtime"]),
            md_cell(row["selected"]),
            md_cell(row["status"]),
        ]) + " |")
    lines.extend(["", "## Evidence Rows", "", "| Row | Kind | Candidate | Status | Next action |", "|---|---|---|---|---|"])
    for row in record["evidence"]:
        lines.append("| " + " | ".join([
            md_cell(row["row_id"]),
            md_cell(row["kind"]),
            md_cell(row["candidate_id"]),
            md_cell(row["status"]),
            md_cell(row["next_action"]),
        ]) + " |")
    lines.extend(["", "## Findings", ""])
    if record["findings"]:
        for item in record["findings"]:
            lines.append(f"- `{item['level']}` {item['owner']}: {item['finding']} -> {item['action']}")
    else:
        lines.append("- No blocking findings.")
    return "\n".join(lines) + "\n"


def main() -> int:
    manifest_path, manifest = load_manifest()
    vault_root = Path(manifest.get("vault_root") or os.environ.get("LOCAL_LLM_RESULT_SYNTHESIS_VAULT_ROOT") or manifest_path.parent).expanduser().resolve()
    run_id = str(manifest.get("run_id") or os.environ.get("LOCAL_LLM_RESULT_SYNTHESIS_RUN_ID") or f"{utc_stamp()}-{slug(manifest_path.stem)}")
    run_root_value = os.environ.get("LOCAL_LLM_RESULT_SYNTHESIS_RUN_ROOT") or manifest.get("run_root", "local-llm-result-synthesis-runs")
    run_root = Path(run_root_value).expanduser()
    if not run_root.is_absolute():
        run_root = manifest_path.parent / run_root
    run_dir = run_root / slug(run_id)
    run_dir.mkdir(parents=True, exist_ok=True)

    selected_candidate = str(manifest.get("selected_candidate") or manifest.get("selected_candidate_id") or "").strip()
    candidate_rows = manifest.get("candidates") or []
    if not isinstance(candidate_rows, list) or not all(isinstance(row, dict) for row in candidate_rows):
        raise ValueError("Manifest candidates must be a list of objects.")
    candidates = [evaluate_candidate(dict(row), selected_candidate) for row in candidate_rows]

    evidence_rows = manifest.get("evidence")
    if evidence_rows is None:
        evidence_rows = manifest.get("rows")
    if not isinstance(evidence_rows, list) or not all(isinstance(row, dict) for row in evidence_rows):
        raise ValueError("Manifest evidence/rows must be a list of objects.")
    evidence = [evaluate_evidence_row(dict(row), vault_root, manifest) for row in evidence_rows]
    evidence.sort(key=lambda row: (KIND_ORDER.get(row["kind"], 99), STATUS_RANK.get(row["status"], 3), row["row_id"]))

    required_kinds = [canonical_kind(item) for item in list_value(manifest.get("required_kinds"))] or list(DEFAULT_REQUIRED_KINDS)
    findings = missing_required_findings(evidence, required_kinds)
    if not selected_candidate:
        findings.append(finding("hold", "candidate", "Manifest has no selected candidate.", "manifest", "Set selected_candidate to the candidate being synthesized."))
    elif selected_candidate not in {row["candidate_id"] for row in candidates}:
        findings.append(finding("fail", "candidate", "Selected candidate is not present in candidates.", selected_candidate, "Add the selected candidate row or correct selected_candidate."))
    if not str(manifest.get("workload") or "").strip():
        findings.append(finding("hold", "workload", "Manifest has no workload.", "manifest", "Name the workload this decision serves."))
    if not str(manifest.get("decision_scope") or "").strip():
        findings.append(finding("hold", "decision", "Manifest has no decision scope.", "manifest", "State whether this decides keep, tune, reject, model selection, runtime selection, or deployment readiness."))

    selected_rows = [row for row in evidence if row["candidate_id"] in {"", selected_candidate}]
    row_findings = [item for row in evidence for item in row["findings"]]
    candidate_findings = [item for row in candidates for item in row["findings"]]
    all_findings = findings + row_findings + candidate_findings
    decision, decision_reason, next_action = choose_decision(selected_rows, all_findings)

    fail_count = sum(1 for row in evidence if row["status"] == "fail") + sum(1 for row in candidates if row["status"] == "fail")
    hold_count = sum(1 for row in evidence if row["status"] == "hold") + sum(1 for row in candidates if row["status"] == "hold")
    finding_fail_count = sum(1 for item in findings if item["level"] == "fail")
    finding_hold_count = sum(1 for item in findings if item["level"] == "hold")

    if fail_count or finding_fail_count:
        status = "fail"
        if decision == "hold_for_missing_or_incomplete_evidence":
            decision = "result_synthesis_failed"
    elif hold_count or finding_hold_count:
        status = "hold"
        if decision == "keep_candidate_for_deployment_memo":
            decision = "result_synthesis_incomplete"
    else:
        status = "pass"
        decision = "result_synthesis_ready_for_deployment_memo"

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "decision_reason": decision_reason,
        "next_action": next_action,
        "manifest_path": str(manifest_path),
        "vault_root": str(vault_root),
        "workload": str(manifest.get("workload") or ""),
        "decision_scope": str(manifest.get("decision_scope") or ""),
        "selected_candidate": selected_candidate,
        "candidate_count": len(candidates),
        "evidence_count": len(evidence),
        "pass_count": sum(1 for row in evidence if row["status"] == "pass"),
        "hold_count": sum(1 for row in evidence if row["status"] == "hold"),
        "fail_count": sum(1 for row in evidence if row["status"] == "fail"),
        "findings": all_findings,
        "candidates": candidates,
        "evidence": evidence,
        "outputs": {},
    }

    json_path = run_dir / f"{run_id}-result-synthesis.json"
    markdown_path = run_dir / f"{run_id}-result-synthesis.md"
    csv_path = run_dir / f"{run_id}-result-synthesis.csv"
    jsonl_path = run_root / "local-llm-result-synthesis-runs.jsonl"
    record["outputs"] = {
        "json": str(json_path),
        "markdown": str(markdown_path),
        "csv": str(csv_path),
        "jsonl": str(jsonl_path),
    }

    csv_write(csv_path, evidence)
    json_path.write_text(json.dumps(record, indent=2, ensure_ascii=True), encoding="utf-8")
    markdown_path.write_text(render_markdown(record), encoding="utf-8")
    with jsonl_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=True) + "\n")

    print(json.dumps({
        "status": status,
        "decision": decision,
        "run_id": run_id,
        "selected_candidate": selected_candidate,
        "candidate_count": len(candidates),
        "evidence_count": len(evidence),
        "pass_count": record["pass_count"],
        "hold_count": record["hold_count"],
        "fail_count": record["fail_count"],
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
$env:LOCAL_LLM_RESULT_SYNTHESIS_MANIFEST = "D:\llm-runs\result-synthesis\result-synthesis-manifest.json"
$env:LOCAL_LLM_RESULT_SYNTHESIS_VAULT_ROOT = "D:\Vaults\PersonalKB"
$env:LOCAL_LLM_RESULT_SYNTHESIS_RUN_ROOT = "D:\llm-runs\result-synthesis"
python .\local_llm_result_synthesis_runner.py
```

## Reading The Result

| Runner status | Meaning | Next route |
|---|---|---|
| `pass/result_synthesis_ready_for_deployment_memo` | selected candidate has consistent workload, custody, compatibility, endpoint, API, benchmark, eval-set, quality, security, operations, alternative, and review-trigger evidence | write [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]] memo |
| `hold/result_synthesis_incomplete` | required evidence is missing, held, unresolved, or not tied to the selected candidate | follow the first held row's next action |
| `fail/result_synthesis_failed` | selected candidate is absent, critical evidence failed, or the evidence contradicts keep/deploy | reject, rebuild, or rerun the failed layer before deployment |

## Capstone Row

| Gate | Required artifact | Pass signal |
|---|---|---|
| Result synthesis | `<run-id>-result-synthesis.json`, `<run-id>-result-synthesis.md`, `<run-id>-result-synthesis.csv`, and one `local-llm-result-synthesis-runs.jsonl` row | selected candidate has consistent proof for workload, model/runtime, endpoint/client, benchmark, eval-set design, quality evaluation runner output, security, operations, rejected alternative, and review trigger before deployment memo |

## Completion Gate

- [ ] one selected candidate is named
- [ ] workload and decision scope are explicit
- [ ] endpoint/API proof exists outside a UI
- [ ] benchmark metrics and interpretation exist
- [ ] evaluation-set design and quality evaluation runner rows agree
- [ ] security/privacy and operations rows are pass or explicitly waived
- [ ] at least one plausible alternative is rejected with evidence
- [ ] adaptation readiness output is linked when the decision is tune, train, adapter serving, or no-train
- [ ] the next review trigger is written down

## References

- [[LLM/Study/Local LLM Model Selection Runner]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Runner]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/Local LLM Evaluation Set Design Runner]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Quality Evaluation Runner]]
- [[LLM/Study/LLM Adaptation and Fine-Tuning Readiness Runner]]
- [[LLM/Study/Local LLM Judge Calibration Runner]]
- [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Runner]]
- [[LLM/Study/Local LLM Security and Privacy Runner]]
- [[LLM/Study/Local LLM Observability and Operations Runner]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/Study/LLM Deployment Readiness Audit Runner]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
