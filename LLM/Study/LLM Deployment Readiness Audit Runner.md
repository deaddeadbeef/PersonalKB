---
tags: [study, llm, deployment, local-llm, readiness, audit, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice, deep-dive]
last-verified: 2026-06-15
---

# LLM Deployment Readiness Audit Runner

> **One-line summary** A deployment choice is ready only when workload, model, route, app integration, quality, performance, privacy, operations, result synthesis, cost, rejected alternative, and retest evidence are all linked and machine-checkable.

Use this after [[LLM/Study/Local LLM Result Synthesis Runner|Local LLM Result Synthesis Runner]] and [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]], before the final deployment memo in [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]. The result synthesis runner reconciles keep, tune, reject, rerun, and deployment-memo readiness. The decision matrix explains how to reason. This runner checks whether the saved proof bundle is complete enough to defend.

This runner does not call a model, pull weights, contact a provider, or benchmark live traffic. It audits a manifest of evidence already collected from the local endpoint, client harness, application integration, benchmark, quality, result synthesis, security, observability, lifecycle, scheduler, RAG, tool, and capstone notes.

## What This Proves

| Evidence family | Checks | Why it matters |
|---|---|---|
| Workload contract | workload, user, data class, latency target, quality bar, failure cost | prevents "local vs cloud" from being abstract |
| Deployment choice | selected path, candidates, decision reason, result-synthesis proof, path-specific risk | ties the chosen local CPU/GPU, self-hosted, hosted, hybrid, or batch route to reconciled evidence |
| Model and runtime | model id, artifact, runtime, tokenizer/template, route compatibility | proves the bytes and serving layer match the workload |
| Endpoint and client | route proof, base URL, model-list, chat call, reusable client | separates UI success from reproducible inference |
| Application integration | app boundary, user flow, response handling, failure behavior, privacy/logging, promotion evidence | proves the local model is usable through the intended app path, not only through a standalone client |
| Benchmark and quality | latency, throughput, memory, rubric, pass/hold/fail | prevents speed-only or quality-only decisions |
| Security and privacy | endpoint exposure, data boundary, logs, RAG/tool/UI/export boundary | keeps local hosting from silently leaking data |
| Operations and lifecycle | owner, startup, monitoring, backup, rollback, validation | decides whether this is a one-off run or maintained service |
| Scheduler and concurrency | queue, backpressure, KV/cache, saturation, batch policy | catches multi-user and long-prompt failure before deployment |
| RAG/tool boundary | corpus/tool applicability, proof or explicit waiver | avoids hidden system risk behind a model-only decision |
| Cost, owner, review | cost model, operational owner, rejected alternative, retest trigger | turns the memo into a maintainable decision |

Academic bridge: deployment readiness is where mechanisms become engineering constraints. Tokenization affects context and cost, attention and KV cache affect memory, prefill affects time to first token, decode affects throughput, batching changes latency trade-offs, RAG changes the data boundary, and evaluation decides whether any of those trade-offs are acceptable.

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "deployment-readiness-001",
  "run_root": "D:/llm-runs/deployment-readiness",
  "vault_root": "D:/Vaults/PersonalKB",
  "workload": "private local research assistant",
  "selected_path": "local_gpu",
  "rows": [
    {
      "id": "workload",
      "kind": "workload_contract",
      "status": "pass",
      "critical": true,
      "proof": "LLM/Study/LLM Mastery Capstone Workbook.md",
      "workload": "private local research assistant",
      "data_sensitivity": "personal",
      "quality_bar": "answers cite provided local notes or refuse",
      "latency_target": "interactive",
      "failure_cost": "wrong local research summary",
      "next_route": "LLM/Study/Local LLM Workload to Model Selection Playbook"
    },
    {
      "id": "decision",
      "kind": "deployment_choice",
      "status": "pass",
      "critical": true,
      "proof": "LLM/Study/LLM Deployment Decision Matrix.md",
      "selected_path": "local_gpu",
      "candidate_paths": ["local_gpu", "hosted_api", "hybrid"],
      "decision": "Use local GPU while private-note quality is acceptable.",
      "result_synthesis": "LLM/Study/Local LLM Result Synthesis Runner.md",
      "evidence": "Benchmark, quality, security, and lifecycle rows are linked.",
      "next_route": "LLM/Study/LLM Deployment Decision Matrix"
    }
  ]
}
```

`proof` may be an absolute path, a vault-relative path, an Obsidian note path, or an Obsidian link. If a kind is deliberately out of scope, include a row with `required: false` and `waiver_reason`.

## Required Evidence Kinds

By default, the audit expects one row for each kind:

| Kind | Required fields or acceptable substitute |
|---|---|
| `workload_contract` | workload, data sensitivity, quality bar, latency or throughput target, failure cost |
| `deployment_choice` | selected path, candidate paths, decision reason, result-synthesis proof |
| `model_runtime` | model id, runtime, artifact or revision, compatibility proof |
| `artifact_custody` | source identity, local bytes or runtime id, verification, unsafe-file decision, conversion/import proof, cleanup plan |
| `endpoint_client` | route, base URL or client proof, model-list or chat evidence |
| `application_integration` | app boundary, user flow, response handling, failure behavior, privacy/logging, promotion decision |
| `benchmark_performance` | timing, throughput, memory, or context metric plus interpretation |
| `quality_evaluation` | quality evaluation runner output, evaluation-set design proof, rubric, score/result, failure owner or next action; reasoning-budget audit when thinking mode supports the quality decision |
| `security_privacy` | endpoint exposure, data boundary, log/export boundary |
| `operations_lifecycle` | owner, startup/restart, observability, backup or rollback |
| `scheduler_concurrency` | scheduler/concurrency/backpressure proof, or explicit single-user waiver |
| `rag_tool_boundary` | RAG/tool proof, or explicit no-RAG/no-tool waiver |
| `cost_owner` | cost model and operational owner |
| `rejected_alternative` | rejected path and measured or policy reason |
| `review_trigger` | trigger that invalidates the decision and next owner/action |

You can override the required list with `required_kinds` in the manifest.

## Standard-Library Runner

Save this as `llm_deployment_readiness_audit_runner.py` inside the run folder. It uses only Python's standard library.

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
    "workload_contract",
    "deployment_choice",
    "model_runtime",
    "artifact_custody",
    "endpoint_client",
    "application_integration",
    "benchmark_performance",
    "quality_evaluation",
    "security_privacy",
    "operations_lifecycle",
    "scheduler_concurrency",
    "rag_tool_boundary",
    "cost_owner",
    "rejected_alternative",
    "review_trigger",
]

ALLOWED_PATHS = {
    "local_cpu",
    "local_gpu",
    "self_hosted_server",
    "hosted_api",
    "hybrid",
    "batch",
}

KIND_HINTS = {
    "workload_contract": {
        "owner": "workload",
        "pass_signal": "The workload, data class, quality bar, latency/throughput target, and failure cost are explicit.",
        "next_route": "LLM/Study/Local LLM Workload to Model Selection Playbook",
    },
    "deployment_choice": {
        "owner": "deployment",
        "pass_signal": "One deployment path is selected from candidate paths with result-synthesis evidence and path-specific risk.",
        "next_route": "LLM/Study/LLM Deployment Decision Matrix",
    },
    "model_runtime": {
        "owner": "model/runtime",
        "pass_signal": "The model artifact, runtime, tokenizer/template, route, workload compatibility, and template/tokenizer runner evidence are linked when chat behavior affects the decision.",
        "next_route": "LLM/Study/Local LLM Runtime and Model Compatibility Matrix",
    },
    "artifact_custody": {
        "owner": "artifact",
        "pass_signal": "The selected model artifact has source identity, local bytes or runtime id, inventory, verification, unsafe-file decision, conversion/import proof, runtime handoff, and cleanup evidence.",
        "next_route": "LLM/Study/Local LLM Artifact Custody Audit Runner",
    },
    "endpoint_client": {
        "owner": "client",
        "pass_signal": "The endpoint route and reusable client evidence prove the intended local or provider route.",
        "next_route": "LLM/Study/Local LLM OpenAI-Compatible API Contract Runner",
    },
    "application_integration": {
        "owner": "application",
        "pass_signal": "The local model path is proven through the app, CLI, UI, job, RAG assistant, or tool loop with response handling, failure behavior, privacy/logging, evaluation, operations, and promotion evidence.",
        "next_route": "LLM/Study/Local LLM Application Integration Evidence Runner",
    },
    "benchmark_performance": {
        "owner": "performance",
        "pass_signal": "Latency, throughput, memory, context, and interpretation evidence support the selected path.",
        "next_route": "LLM/Study/Local LLM Inference Benchmark Log",
    },
    "quality_evaluation": {
        "owner": "quality",
        "pass_signal": "Workload prompts have quality evaluation runner output, evaluation-set design proof, rubric-backed pass, hold, or fail results with failure owners; LLM-as-judge rows have calibration proof when used for the decision.",
        "next_route": "LLM/Study/Local LLM Quality Evaluation Runner",
    },
    "security_privacy": {
        "owner": "security",
        "pass_signal": "Endpoint exposure, logs, data boundary, and export boundary are checked.",
        "next_route": "LLM/Study/Local LLM Security and Privacy Runner",
    },
    "operations_lifecycle": {
        "owner": "operations",
        "pass_signal": "Owner, startup, observability, restart, backup, rollback, and validation evidence exist.",
        "next_route": "LLM/Study/Local LLM Service Lifecycle and Upgrade Runner",
    },
    "scheduler_concurrency": {
        "owner": "scheduler",
        "pass_signal": "Scheduler, queue, KV/cache, concurrency, backpressure, or batch evidence supports the serving policy.",
        "next_route": "LLM/Study/Local LLM Scheduler Evidence Audit Runner",
    },
    "rag_tool_boundary": {
        "owner": "system boundary",
        "pass_signal": "RAG and tool surfaces are proven, or explicitly out of scope with a reason.",
        "next_route": "LLM/Study/Local RAG Evidence Runner",
    },
    "cost_owner": {
        "owner": "cost/owner",
        "pass_signal": "Hardware, API, electricity, support, and owner assumptions are written down.",
        "next_route": "LLM/Study/LLM Deployment Decision Matrix",
    },
    "rejected_alternative": {
        "owner": "deployment",
        "pass_signal": "At least one plausible alternative is rejected with measured, policy, privacy, cost, or operations evidence.",
        "next_route": "LLM/Study/LLM Deployment Decision Matrix",
    },
    "review_trigger": {
        "owner": "lifecycle",
        "pass_signal": "A new model, workload, data class, traffic, cost, or security change has a named retest route.",
        "next_route": "LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook",
    },
}

STATUS_VALUES = {
    "pass": "pass",
    "passed": "pass",
    "complete": "pass",
    "ready": "pass",
    "hold": "hold",
    "blocked": "hold",
    "gap": "hold",
    "missing": "hold",
    "not-started": "hold",
    "not started": "hold",
    "in-progress": "hold",
    "in progress": "hold",
    "skip": "hold",
    "skipped": "hold",
    "fail": "fail",
    "failed": "fail",
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
    return text.strip("-") or "llm-deployment-readiness"


def norm(value: Any) -> str:
    return str(value or "").strip().lower()


def status_value(value: Any) -> str:
    return STATUS_VALUES.get(norm(value).replace("_", "-"), "hold")


def bool_value(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if value in (None, ""):
        return default
    text = norm(value).replace("_", "-").replace(" ", "-")
    if text in {"true", "yes", "y", "1", "required", "critical", "applicable"}:
        return True
    if text in {"false", "no", "n", "0", "optional", "waived", "not-required", "not-applicable"}:
        return False
    return default


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
    manifest_path = os.environ.get("LLM_DEPLOYMENT_READINESS_MANIFEST")
    if not manifest_path:
        raise ValueError("Set LLM_DEPLOYMENT_READINESS_MANIFEST to a JSON manifest path.")
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


def wiki_link(route: str) -> str:
    return LINK_OPEN + route + LINK_CLOSE


def route_for_row(row: dict[str, Any], kind: str) -> str:
    route = str(row.get("next_route") or row.get("route") or row.get("proof") or "")
    if route:
        return strip_obsidian_link(route).removesuffix(".md")
    return KIND_HINTS.get(kind, {}).get("next_route", "LLM/Study/LLM Deployment Decision Matrix")


def finding(level: str, owner: str, text: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "owner": owner,
        "finding": text,
        "evidence": evidence,
        "action": action,
    }


def metric_value(metrics: dict[str, Any], *names: str) -> Any:
    for name in names:
        if name in metrics and metrics[name] not in (None, ""):
            return metrics[name]
    return None


def has_any_metric(metrics: dict[str, Any], names: tuple[str, ...]) -> bool:
    return any(metric_value(metrics, name) is not None for name in names)


def has_text(row: dict[str, Any], *names: str) -> bool:
    return any(str(row.get(name) or "").strip() for name in names)


def normalized_path(value: Any) -> str:
    text = str(value or "").strip().lower().replace("-", "_").replace(" ", "_").replace("/", "_")
    aliases = {
        "local": "local_gpu",
        "local_workstation": "local_gpu",
        "gpu": "local_gpu",
        "cpu": "local_cpu",
        "self_hosted": "self_hosted_server",
        "self-hosted": "self_hosted_server",
        "cloud": "hosted_api",
        "hosted": "hosted_api",
        "api": "hosted_api",
        "offline_batch": "batch",
    }
    return aliases.get(text, text)


def evaluate_kind_requirements(row: dict[str, Any], kind: str, manifest: dict[str, Any], findings: list[dict[str, str]]) -> None:
    metrics = row.get("metrics") if isinstance(row.get("metrics"), dict) else {}
    owner = KIND_HINTS.get(kind, {}).get("owner", kind)
    claim_or_evidence = has_text(row, "claim", "evidence", "decision", "summary", "reason")

    if kind == "workload_contract":
        if not (has_text(row, "workload") or has_text(manifest, "workload")):
            findings.append(finding("hold", owner, "Workload contract has no named workload.", kind, "Name one user task or product workflow."))
        if not has_text(row, "data_sensitivity", "data_class", "privacy_boundary"):
            findings.append(finding("hold", owner, "Workload contract has no data sensitivity or privacy boundary.", kind, "Classify public, personal, private, regulated, secret, or mixed data."))
        if not has_text(row, "quality_bar", "success_rubric", "pass_signal"):
            findings.append(finding("hold", owner, "Workload contract has no quality bar.", kind, "Write what pass, hold, and fail mean for this workload."))
        if not has_text(row, "latency_target", "throughput_target", "batch_window"):
            findings.append(finding("hold", owner, "Workload contract has no latency, throughput, or batch target.", kind, "Add an interactive latency target, throughput target, or batch window."))
        if not has_text(row, "failure_cost", "risk", "failure_tolerance"):
            findings.append(finding("hold", owner, "Workload contract has no failure cost.", kind, "State whether failure is annoying, expensive, unsafe, or a data leak."))
    elif kind == "deployment_choice":
        selected = normalized_path(row.get("selected_path") or manifest.get("selected_path"))
        candidates = [normalized_path(item) for item in list_value(row.get("candidate_paths") or manifest.get("candidate_paths"))]
        if selected not in ALLOWED_PATHS:
            findings.append(finding("hold", owner, "Deployment choice has no recognized selected path.", selected, "Use local_cpu, local_gpu, self_hosted_server, hosted_api, hybrid, or batch."))
        if not candidates:
            findings.append(finding("hold", owner, "Deployment choice has no candidate paths.", kind, "List at least two plausible candidate paths."))
        elif selected in ALLOWED_PATHS and selected not in candidates:
            findings.append(finding("hold", owner, "Selected path is not listed among candidate paths.", selected, "Add the selected path to candidate_paths."))
        if not claim_or_evidence:
            findings.append(finding("hold", owner, "Deployment choice has no decision reason.", kind, "Tie the selected path to workload, quality, latency, privacy, cost, and operations evidence."))
        if not has_text(row, "result_synthesis", "decision_synthesis", "synthesis_proof", "result_synthesis_proof"):
            findings.append(finding("hold", owner, "Deployment choice has no result-synthesis proof.", kind, "Run Local LLM Result Synthesis Runner or link the reconciled keep/tune/reject evidence."))
    elif kind == "model_runtime":
        if not has_text(row, "model", "model_id", "artifact", "revision"):
            findings.append(finding("hold", owner, "Model/runtime row has no model id, artifact, or revision.", kind, "Add the served model id and artifact provenance."))
        if not has_text(row, "runtime", "provider", "server"):
            findings.append(finding("hold", owner, "Model/runtime row has no runtime or provider.", kind, "Name Ollama, llama.cpp, vLLM, SGLang, LM Studio, hosted provider, or batch engine."))
        if not has_text(row, "compatibility", "tokenizer", "chat_template", "route", "api_contract"):
            findings.append(finding("hold", owner, "Model/runtime row has no compatibility evidence.", kind, "Link tokenizer/template/route/API contract evidence."))
        template_text = " ".join(str(row.get(key, "")) for key in ("compatibility", "tokenizer", "chat_template", "template", "route", "notes")).lower()
        if ("chat" in template_text or "template" in template_text or "tokenizer" in template_text) and not has_text(row, "template_compatibility", "chat_template_compatibility", "template_runner", "compatibility_runner"):
            findings.append(finding("hold", owner, "Model/runtime row has no template/tokenizer runner evidence.", kind, "Run Chat Template and Tokenizer Compatibility Runner or link its output before accepting chat-behavior evidence."))
    elif kind == "artifact_custody":
        if not has_text(row, "source_ref", "source", "repo", "artifact_source"):
            findings.append(finding("hold", owner, "Artifact custody row has no source identity.", kind, "Record registry, URL, source repo, or internal artifact source."))
        if not has_text(row, "revision", "revision_or_file", "tag", "filename", "digest"):
            findings.append(finding("hold", owner, "Artifact custody row has no pinned revision, tag, filename, or digest.", kind, "Record the exact artifact identity."))
        if not has_text(row, "local_path", "runtime_model_id", "artifact_path", "cache_path"):
            findings.append(finding("hold", owner, "Artifact custody row has no local path or runtime id.", kind, "Link the cache path, GGUF path, local mirror, or runtime-visible model id."))
        if not has_text(row, "verification", "verification_method", "hash", "digest", "verification_artifact"):
            findings.append(finding("hold", owner, "Artifact custody row has no verification evidence.", kind, "Link the artifact custody audit output, hash, digest, or verification log."))
        if not has_text(row, "artifact_custody_audit", "custody_audit", "custody_output"):
            findings.append(finding("hold", owner, "Artifact custody row has no custody audit output.", kind, "Run Local LLM Artifact Custody Audit Runner and link its JSON or Markdown output."))
    elif kind == "endpoint_client":
        if not has_text(row, "route", "base_url", "client", "api_contract", "request_path"):
            findings.append(finding("hold", owner, "Endpoint/client row has no route or client evidence.", kind, "Add base URL, route, client script, or API contract result."))
        if not has_text(row, "model_list", "chat_call", "response", "streaming", "wrong_model_failure"):
            findings.append(finding("hold", owner, "Endpoint/client row has no model-list, chat, streaming, or harmless failure evidence.", kind, "Prove the intended route with saved request/response evidence."))
    elif kind == "application_integration":
        if not has_text(row, "app_name", "entry_point", "app_contract", "integration_scope"):
            findings.append(finding("hold", owner, "Application row has no app boundary.", kind, "Add app name, entry point, app contract, or integration scope."))
        if not has_text(row, "user_flow", "flow_name", "trigger", "transcript", "visible_output"):
            findings.append(finding("hold", owner, "Application row has no user-flow evidence.", kind, "Link the CLI/UI/job/RAG/tool-loop trigger and visible result."))
        if not has_text(row, "response_handling", "parser", "output_path", "acceptance_check"):
            findings.append(finding("hold", owner, "Application row has no response-handling evidence.", kind, "Show how generated text becomes parsed, displayed, stored, or rejected application state."))
        if not has_text(row, "failure_handling", "failure_probe", "fallback", "fallback_or_next_action"):
            findings.append(finding("hold", owner, "Application row has no failure-handling evidence.", kind, "Probe one timeout, wrong-model, server-down, parse, RAG, or tool failure and record the expected app behavior."))
        if not has_text(row, "privacy_logging", "prompt_storage", "output_storage", "retention", "redaction"):
            findings.append(finding("hold", owner, "Application row has no privacy/logging evidence.", kind, "Record where prompts, outputs, logs, exports, and private data are stored or redacted."))
        if not has_text(row, "promotion_decision", "decision", "promote_hold_reject", "app_integration_audit"):
            findings.append(finding("hold", owner, "Application row has no promotion decision.", kind, "Run Local LLM Application Integration Evidence Runner or link its promote/hold/reject output."))
    elif kind == "benchmark_performance":
        metric_names = ("ttft_ms", "time_to_first_token_ms", "tpot_ms", "tokens_per_second", "total_latency_ms", "p95_latency_ms", "throughput_rps", "peak_vram_mb", "peak_ram_mb", "context_tokens", "batch_tokens_per_second")
        if not has_any_metric(metrics, metric_names):
            findings.append(finding("hold", owner, "Benchmark row has no latency, throughput, memory, or context metric.", kind, "Add TTFT, TPOT, tokens/sec, p95, memory, context tokens, or batch throughput."))
        if not claim_or_evidence:
            findings.append(finding("hold", owner, "Benchmark row has no interpretation.", kind, "State whether the numbers satisfy, block, or redirect the deployment path."))
    elif kind == "quality_evaluation":
        if not has_text(row, "rubric", "quality_bar", "prompt_suite", "score", "result"):
            findings.append(finding("hold", owner, "Quality row has no rubric, prompt suite, score, or result.", kind, "Add pass/hold/fail quality evidence for the workload."))
        if not has_text(row, "quality_evaluation_runner", "quality_runner", "quality_audit", "quality_evaluation_audit"):
            findings.append(finding("hold", owner, "Quality row has no quality evaluation runner output.", kind, "Run Local LLM Quality Evaluation Runner or link its JSON/Markdown output before deployment readiness depends on quality."))
        if not has_text(row, "eval_set_design", "evaluation_set_design", "prompt_suite_design", "heldout_proof"):
            findings.append(finding("hold", owner, "Quality row has no evaluation-set design proof.", kind, "Run Local LLM Evaluation Set Design Runner or link held-out/private prompt-suite and contamination-control evidence."))
        if not has_text(row, "failure_owner", "next_action", "decision") and not has_any_metric(metrics, ("score", "pass_rate", "win_rate")):
            findings.append(finding("hold", owner, "Quality row has no failure owner or score.", kind, "Add human score, pass rate, failure owner, or next controlled action."))
        judge_text = " ".join(str(row.get(key, "")) for key in ("method", "evaluator", "rubric", "notes", "result", "decision")).lower()
        if ("llm-as-judge" in judge_text or "llm judge" in judge_text) and not has_text(row, "judge_calibration", "calibration_proof", "human_calibration", "agreement_rate"):
            findings.append(finding("hold", owner, "LLM-as-judge quality row has no calibration proof.", kind, "Run Local LLM Judge Calibration Runner or link human agreement, AB/BA order, and bias-audit evidence."))
        reasoning_text = " ".join(str(row.get(key, "")) for key in ("method", "notes", "result", "decision", "quality_bar", "rubric")).lower()
        if any(token in reasoning_text for token in ("reasoning", "thinking", "test-time compute", "reasoning_effort", "reasoning.effort")) and not has_text(row, "reasoning_budget_audit", "reasoning_budget", "test_time_compute_audit"):
            findings.append(finding("hold", owner, "Reasoning-backed quality row has no reasoning-budget audit.", kind, "Run Local LLM Reasoning Budget and Test-Time Compute Runner or link its output before using thinking mode in the deployment decision."))
    elif kind == "security_privacy":
        if not has_text(row, "endpoint_exposure", "binding", "host_classification", "network_boundary"):
            findings.append(finding("hold", owner, "Security row has no endpoint exposure or network boundary.", kind, "Record loopback/LAN/public/provider boundary and model-list exposure."))
        if not has_text(row, "data_boundary", "privacy_boundary", "rag_boundary", "tool_boundary", "ui_boundary"):
            findings.append(finding("hold", owner, "Security row has no data boundary.", kind, "Record prompt, corpus, tool, UI, export, and storage boundaries."))
        if not has_text(row, "log_boundary", "secret_scan", "export_boundary", "retention"):
            findings.append(finding("hold", owner, "Security row has no log, secret, retention, or export evidence.", kind, "Add log/config scan or explicit no-log/no-export boundary."))
    elif kind == "operations_lifecycle":
        if not has_text(row, "owner", "operator", "oncall"):
            findings.append(finding("hold", owner, "Operations row has no owner.", kind, "Name who patches, monitors, restarts, and handles incidents."))
        if not has_text(row, "startup", "restart", "service_mode", "launch_command"):
            findings.append(finding("hold", owner, "Operations row has no startup or restart evidence.", kind, "Add startup mode, launch command, service wrapper, or restart check."))
        if not has_text(row, "observability", "metrics", "logs", "resource_pressure"):
            findings.append(finding("hold", owner, "Operations row has no observability evidence.", kind, "Link model state, metrics, logs, resource pressure, or loaded route evidence."))
        if not has_text(row, "backup", "rollback", "validation", "post_change_validation"):
            findings.append(finding("hold", owner, "Operations row has no backup, rollback, or validation evidence.", kind, "Add backup path, rollback target, and post-change validation."))
    elif kind == "scheduler_concurrency":
        if has_text(row, "single_user_reason", "no_concurrency_reason", "waiver_reason") and not has_text(row, "concurrency", "scheduler", "backpressure", "batch_policy"):
            return
        if not has_text(row, "concurrency", "scheduler", "queue", "backpressure", "batch_policy", "scheduler_audit"):
            findings.append(finding("hold", owner, "Scheduler/concurrency row has no scheduler, queue, batch, or waiver evidence.", kind, "Link scheduler audit, concurrency ladder, batch policy, or single-user waiver."))
        if not has_text(row, "saturation", "p95", "capacity", "policy", "decision"):
            findings.append(finding("hold", owner, "Scheduler/concurrency row has no capacity or policy decision.", kind, "Add saturation point, p95 behavior, backpressure, or batch policy."))
    elif kind == "rag_tool_boundary":
        if has_text(row, "no_rag_tool_reason", "waiver_reason", "out_of_scope_reason") and not has_text(row, "rag", "tool", "corpus", "tool_policy"):
            return
        if not has_text(row, "rag", "tool", "corpus", "retrieval", "citation", "tool_policy"):
            findings.append(finding("hold", owner, "RAG/tool boundary row has no proof or explicit waiver.", kind, "Link RAG/tool evidence or write why both are out of scope."))
        if has_text(row, "rag", "corpus", "retrieval") and not has_text(row, "citation", "refusal", "corpus_boundary"):
            findings.append(finding("hold", owner, "RAG row lacks citation, refusal, or corpus-boundary evidence.", kind, "Add citation audit, unsupported-question refusal, and corpus boundary."))
        if has_text(row, "tool", "tool_policy") and not has_text(row, "schema", "policy", "denial", "execution_log"):
            findings.append(finding("hold", owner, "Tool row lacks schema, policy, denial, or execution evidence.", kind, "Add schema validation, policy decision, harmless execution, and denial row."))
    elif kind == "cost_owner":
        if not has_text(row, "cost_model", "hardware_cost", "api_cost", "electricity", "support_cost"):
            findings.append(finding("hold", owner, "Cost row has no cost model.", kind, "Write hardware, API, electricity, rental GPU, maintenance, or support cost assumptions."))
        if not has_text(row, "owner", "operator", "payer", "maintenance_owner"):
            findings.append(finding("hold", owner, "Cost row has no owner.", kind, "Name who pays, operates, and revisits the cost model."))
    elif kind == "rejected_alternative":
        rejected = normalized_path(row.get("rejected_path") or row.get("alternative") or row.get("path"))
        if rejected not in ALLOWED_PATHS:
            findings.append(finding("hold", owner, "Rejected alternative has no recognized path.", rejected, "Name the rejected local_cpu, local_gpu, self_hosted_server, hosted_api, hybrid, or batch path."))
        if not has_text(row, "reason", "evidence", "policy_reason", "metric_reason", "cost_reason"):
            findings.append(finding("hold", owner, "Rejected alternative has no evidence-backed reason.", kind, "Reject with quality, latency, privacy, cost, operations, or policy evidence."))
    elif kind == "review_trigger":
        if not has_text(row, "trigger", "retest_trigger", "invalidates_when"):
            findings.append(finding("hold", owner, "Review row has no retest trigger.", kind, "Write what change invalidates the decision."))
        if not has_text(row, "owner", "next_owner", "next_action", "review_date"):
            findings.append(finding("hold", owner, "Review row has no owner or next action.", kind, "Name who reruns the audit and what route they use."))


def evaluate_row(row: dict[str, Any], vault_root: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    row_id = str(row.get("row_id") or row.get("id") or row.get("name") or "")
    kind = str(row.get("kind") or row.get("type") or "unspecified").strip().lower().replace(" ", "_")
    required = bool_value(row.get("required"), True)
    critical = bool_value(row.get("critical"), kind in DEFAULT_REQUIRED_KINDS)
    declared_status = status_value(row.get("status"))
    proof = str(row.get("proof") or row.get("proof_path") or row.get("artifact") or row.get("evidence_path") or "")
    pass_signal = str(row.get("pass_signal") or KIND_HINTS.get(kind, {}).get("pass_signal", "Evidence row is complete enough to support deployment readiness."))
    waiver_reason = str(row.get("waiver_reason") or row.get("skip_reason") or row.get("out_of_scope_reason") or "")
    findings: list[dict[str, str]] = []

    if not row_id:
        findings.append(finding("hold", kind, "Evidence row id is missing.", str(row), "Give every row a stable id before auditing."))

    if kind not in KIND_HINTS:
        findings.append(finding("hold", kind, "Evidence kind is not recognized.", kind, "Use one of the required deployment readiness kinds or add a waiver reason."))

    if not required:
        if not waiver_reason:
            findings.append(finding("hold", kind, "Optional or out-of-scope row has no waiver reason.", row_id, "Record why this evidence kind is not required for this deployment."))
        elif declared_status == "fail":
            findings.append(finding("fail", kind, "Waived row is marked failed.", row_id, "Either remove the waiver or resolve the failure."))
        status = "hold" if findings else "pass"
        decision = "waiver_needs_reason" if findings else "waived_with_reason"
        return {
            "row_id": row_id,
            "kind": kind,
            "required": required,
            "critical": critical,
            "declared_status": declared_status,
            "status": status,
            "decision": decision,
            "proof": proof,
            "proof_resolved": "",
            "proof_exists": False,
            "pass_signal": pass_signal,
            "next_route": route_for_row(row, kind),
            "next_action": findings[0]["action"] if findings else "Keep waiver with reason in the deployment memo.",
            "findings": findings,
        }

    if declared_status == "fail":
        findings.append(finding("fail", kind, "Evidence row is explicitly marked fail.", row_id, "Resolve the failed deployment readiness evidence before accepting the memo."))
    elif declared_status != "pass":
        findings.append(finding("hold", kind, "Evidence row is not marked pass.", declared_status, "Complete the evidence route and set status to pass only after the pass signal is met."))

    exists = False
    proof_resolved = ""
    if proof:
        exists, proof_resolved = proof_exists(vault_root, proof)
        if not exists:
            findings.append(finding("hold", kind, "Proof link or path does not resolve in the vault.", proof_resolved, "Fix the proof path or create the linked evidence artifact."))
    else:
        findings.append(finding("hold", kind, "Required evidence row has no proof link or path.", row_id, "Add a proof link to the manifest, capstone workbook, or deployment memo."))

    evaluate_kind_requirements(row, kind, manifest, findings)

    if not pass_signal:
        findings.append(finding("hold", kind, "Row has no explicit pass signal.", row_id, "Write the observable evidence condition that makes this row pass."))

    if critical and declared_status == "pass" and not proof:
        findings.append(finding("fail", kind, "Critical row is marked pass without proof.", row_id, "A critical deployment readiness claim needs linked evidence, not only status text."))

    fail_count = sum(1 for item in findings if item["level"] == "fail")
    hold_count = sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        status = "fail"
        decision = "row_failed"
    elif hold_count:
        status = "hold"
        decision = "row_incomplete"
    else:
        status = "pass"
        decision = "row_ready"

    return {
        "row_id": row_id,
        "kind": kind,
        "required": required,
        "critical": critical,
        "declared_status": declared_status,
        "status": status,
        "decision": decision,
        "proof": proof,
        "proof_resolved": proof_resolved,
        "proof_exists": exists,
        "pass_signal": pass_signal,
        "next_route": route_for_row(row, kind),
        "next_action": findings[0]["action"] if findings else "Keep this evidence linked in the deployment decision memo.",
        "findings": findings,
    }


def missing_kind_row(kind: str) -> dict[str, Any]:
    hint = KIND_HINTS.get(kind, {})
    return {
        "row_id": f"missing-{kind}",
        "kind": kind,
        "required": True,
        "critical": True,
        "declared_status": "hold",
        "status": "hold",
        "decision": "required_kind_missing",
        "proof": "",
        "proof_resolved": "",
        "proof_exists": False,
        "pass_signal": hint.get("pass_signal", f"Manifest includes at least one {kind} row."),
        "next_route": hint.get("next_route", "LLM/Study/LLM Deployment Decision Matrix"),
        "next_action": f"Add one {kind} evidence row to the deployment readiness manifest, or add a waived row with a reason.",
        "findings": [finding("hold", kind, "Required deployment readiness evidence kind is missing from the manifest.", kind, f"Add one {kind} row or document a waiver.")],
    }


def kind_summary(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    kinds = sorted({row["kind"] for row in rows}, key=lambda item: (KIND_ORDER.get(item, 99), item))
    summary = []
    for kind in kinds:
        subset = [row for row in rows if row["kind"] == kind]
        summary.append({
            "kind": kind,
            "row_count": len(subset),
            "pass_count": sum(1 for row in subset if row["status"] == "pass"),
            "hold_count": sum(1 for row in subset if row["status"] == "hold"),
            "fail_count": sum(1 for row in subset if row["status"] == "fail"),
            "critical_missing": sum(1 for row in subset if row["critical"] and row["status"] != "pass"),
        })
    return summary


def md_cell(value: Any) -> str:
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=True)
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "row_id",
        "kind",
        "required",
        "critical",
        "declared_status",
        "status",
        "decision",
        "proof",
        "proof_resolved",
        "proof_exists",
        "pass_signal",
        "next_route",
        "next_action",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({name: row.get(name, "") for name in fieldnames})


def render_markdown(record: dict[str, Any]) -> str:
    lines = [
        f"# LLM Deployment Readiness Audit - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Selected path: `{record.get('selected_path') or ''}`",
        f"- Workload: `{record.get('workload') or ''}`",
        f"- Evidence rows: `{record['row_count']}`",
        f"- Pass/Hold/Fail: `{record['pass_count']}` / `{record['hold_count']}` / `{record['fail_count']}`",
        f"- Critical gaps: `{record['critical_gap_count']}`",
        "",
        "## Kind Summary",
        "",
        "| Kind | Rows | Pass | Hold | Fail | Critical gaps |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in record["kinds"]:
        lines.append(
            "| "
            + " | ".join([
                md_cell(row["kind"]),
                md_cell(row["row_count"]),
                md_cell(row["pass_count"]),
                md_cell(row["hold_count"]),
                md_cell(row["fail_count"]),
                md_cell(row["critical_missing"]),
            ])
            + " |"
        )
    lines.extend([
        "",
        "## Evidence Rows",
        "",
        "| Row | Kind | Critical | Status | Proof exists | Next route |",
        "|---|---|---:|---|---:|---|",
    ])
    for row in record["rows"]:
        lines.append(
            "| "
            + " | ".join([
                md_cell(row["row_id"]),
                md_cell(row["kind"]),
                md_cell(row["critical"]),
                md_cell(row["status"]),
                md_cell(row["proof_exists"]),
                md_cell(wiki_link(row["next_route"])),
            ])
            + " |"
        )
    lines.extend(["", "## Next Actions", ""])
    incomplete = [row for row in record["rows"] if row["status"] != "pass"]
    for row in incomplete:
        lines.append(f"- `{row['row_id']}` -> {wiki_link(row['next_route'])}: {row['next_action']}")
    if not incomplete:
        lines.append("- Deployment evidence is ready to support the final decision memo.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    manifest_path, manifest = load_manifest()
    vault_root = Path(manifest.get("vault_root") or os.environ.get("LLM_DEPLOYMENT_READINESS_VAULT_ROOT") or manifest_path.parent).expanduser().resolve()
    run_id = str(manifest.get("run_id") or os.environ.get("LLM_DEPLOYMENT_READINESS_RUN_ID") or f"{utc_stamp()}-{slug(manifest_path.stem)}")
    run_root_value = os.environ.get("LLM_DEPLOYMENT_READINESS_RUN_ROOT") or manifest.get("run_root", "llm-deployment-readiness-runs")
    run_root = Path(str(run_root_value)).expanduser()
    if not run_root.is_absolute():
        run_root = manifest_path.parent / run_root
    run_root = run_root.resolve()
    run_dir = run_root / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    rows = manifest.get("rows")
    if rows is None:
        rows = manifest.get("evidence_rows")
    if not isinstance(rows, list) or not all(isinstance(row, dict) for row in rows):
        raise ValueError("Manifest rows must be a list of objects.")

    evaluated = [evaluate_row(dict(row), vault_root, manifest) for row in rows]
    required_kinds = list_value(manifest.get("required_kinds")) or DEFAULT_REQUIRED_KINDS
    present_kinds = {row["kind"] for row in evaluated}
    for kind in required_kinds:
        normalized = str(kind).strip().lower().replace(" ", "_")
        if normalized not in present_kinds:
            evaluated.append(missing_kind_row(normalized))

    evaluated.sort(key=lambda row: (
        STATUS_RANK.get(row["status"], 3),
        KIND_ORDER.get(row["kind"], 99),
        row["row_id"],
    ))

    pass_count = sum(1 for row in evaluated if row["status"] == "pass")
    hold_count = sum(1 for row in evaluated if row["status"] == "hold")
    fail_count = sum(1 for row in evaluated if row["status"] == "fail")
    critical_gap_count = sum(1 for row in evaluated if row["critical"] and row["status"] != "pass")

    if fail_count:
        status = "fail"
        decision = "deployment_readiness_failed"
    elif hold_count or critical_gap_count:
        status = "hold"
        decision = "deployment_readiness_incomplete"
    else:
        status = "pass"
        decision = "deployment_readiness_ready"

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "manifest_path": str(manifest_path),
        "vault_root": str(vault_root),
        "workload": str(manifest.get("workload") or ""),
        "selected_path": normalized_path(manifest.get("selected_path")),
        "row_count": len(evaluated),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "critical_gap_count": critical_gap_count,
        "kinds": kind_summary(evaluated),
        "rows": evaluated,
        "outputs": {},
    }

    json_path = run_dir / f"{run_id}-deployment-readiness-audit.json"
    markdown_path = run_dir / f"{run_id}-deployment-readiness-audit.md"
    csv_path = run_dir / f"{run_id}-deployment-readiness-audit.csv"
    jsonl_path = run_root / "llm-deployment-readiness-audit-runs.jsonl"
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
        "row_count": len(evaluated),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "critical_gap_count": critical_gap_count,
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
$env:LLM_DEPLOYMENT_READINESS_MANIFEST = "D:\llm-runs\deployment-readiness\deployment-readiness-manifest.json"
$env:LLM_DEPLOYMENT_READINESS_VAULT_ROOT = "D:\Vaults\PersonalKB"
$env:LLM_DEPLOYMENT_READINESS_RUN_ROOT = "D:\llm-runs\deployment-readiness"
python .\llm_deployment_readiness_audit_runner.py
```

## Reading The Result

| Runner status | Meaning | Next route |
|---|---|---|
| `pass/deployment_readiness_ready` | every required deployment-readiness kind is pass or explicitly waived, and critical proof links resolve | copy the output into the final deployment memo |
| `hold/deployment_readiness_incomplete` | required proof, path choice, artifact custody, benchmark, quality, privacy, operations, cost, or retest evidence is missing | follow each row's `next_route` |
| `fail/deployment_readiness_failed` | a row is explicitly failed, unsafe, rejected, or a critical pass has no proof | resolve the failed row before accepting the deployment |

This runner validates the evidence bundle, not the service itself. Use live runners for artifact custody, endpoint, application integration, quality evaluation, observability, scheduler, lifecycle, security, RAG, and tool measurements.

## Capstone Row

| Gate | Required artifact | Pass signal |
|---|---|---|
| Deployment readiness audit | `<run-id>-deployment-readiness-audit.json`, `<run-id>-deployment-readiness-audit.md`, `<run-id>-deployment-readiness-audit.csv`, and one `llm-deployment-readiness-audit-runs.jsonl` row | workload, selected path, result synthesis, model/runtime, artifact custody, endpoint/client, application integration, benchmark, quality, security, operations, scheduler/concurrency, RAG/tool boundary, cost/owner, rejected alternative, and review trigger are pass or explicitly waived |

## Completion Gate

- [ ] the manifest includes all required evidence kinds or explicit waivers
- [ ] critical rows cannot pass without proof
- [ ] the selected path is one of `local_cpu`, `local_gpu`, `self_hosted_server`, `hosted_api`, `hybrid`, or `batch`
- [ ] the deployment choice links a result-synthesis output or a remediation row
- [ ] the quality evidence links [[LLM/Study/Local LLM Quality Evaluation Runner|Local LLM Quality Evaluation Runner]] output when deployment readiness depends on quality
- [ ] the deployment choice rejects at least one plausible alternative with evidence
- [ ] the final review trigger names what change invalidates the decision
- [ ] outputs are linked from [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]

## References

- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/Study/Local LLM Result Synthesis Runner]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/Local LLM Capstone Project Blueprint]]
- [[LLM/Study/LLM Mastery Evidence Audit Runner]]
- [[LLM/Study/Local LLM Workload to Model Selection Playbook]]
- [[LLM/Study/Local LLM Artifact Custody Audit Runner]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Runner]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]]
- [[LLM/Study/Local LLM Application Integration Evidence Runner]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Quality Evaluation Runner]]
- [[LLM/Study/Local LLM Evaluation Set Design Runner]]
- [[LLM/Study/Local LLM Judge Calibration Runner]]
- [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Runner]]
- [[LLM/Study/Local LLM Security and Privacy Runner]]
- [[LLM/Study/Local LLM Observability and Operations Runner]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner]]
- [[LLM/Study/Local LLM Scheduler Evidence Audit Runner]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner]]
- [[LLM/Study/Local RAG Evidence Runner]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Runner]]
