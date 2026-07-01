---
tags: [study, llm, inference, local-llm, runtime, comparison, benchmark, quality, evidence, audit, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice, deep-dive]
last-verified: 2026-06-16
---

# Local LLM Runtime Comparison Runner

> **One-line summary** A runtime comparison is ready only when the same workload, prompt suite, sampler, context target, output cap, endpoint contract, benchmark evidence, quality boundary, and security boundary support one selected runtime and one rejected alternative.

Use this after [[LLM/Study/Local LLM Runtime Comparison Lab|Local LLM Runtime Comparison Lab]], [[LLM/Study/Local LLM Benchmark Evidence Audit Runner|Local LLM Benchmark Evidence Audit Runner]], and [[LLM/Study/Local LLM Quality Evaluation Runner|Local LLM Quality Evaluation Runner]] produce saved rows. Use it before [[LLM/Study/Local LLM Capacity and SLO Planning Runner|Local LLM Capacity and SLO Planning Runner]], [[LLM/Study/Local LLM Result Synthesis Runner|Local LLM Result Synthesis Runner]], [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]], or [[LLM/Study/LLM Deployment Readiness Audit Runner|LLM Deployment Readiness Audit Runner]] whenever a local deployment choice depends on Ollama, LM Studio, llama.cpp, vLLM, SGLang, a Docker/WSL serving path, or a UI over one of those providers.

This runner does not start servers, benchmark endpoints, scrape runtime docs, or decide which runtime is universally best. It audits a saved comparison manifest. That keeps the academic point visible: runtime differences are only meaningful after artifact, tokenizer/template, sampler, context, route, scheduler, memory, and quality confounders have been controlled or explicitly marked as approximate.

## What This Proves

| Evidence family | Checks | Why it matters |
|---|---|---|
| Workload contract | workload, decision scope, primary metric, acceptance threshold | prevents "best runtime" from becoming context-free |
| Candidate identity | runtime id, runtime name, model/artifact, route, base URL, hardware boundary | prevents comparing different model or endpoint identities by accident |
| Endpoint proof | compatibility, API contract, health/model-list, smoke/chat proof | separates "loaded in a UI" from reproducible inference |
| Frozen controls | prompt suite, sampler, context target, output cap, cold/warm state, changed variables | makes runtime the intended changed layer |
| Benchmark audit | timing, token accounting, memory/context, benchmark-evidence audit output | prevents raw latency rows from driving a runtime decision |
| Quality boundary | quality runner output, prompt-suite status, failure owner | prevents a faster runtime from winning after quality regresses |
| Security and operations | loopback or approved exposure, logs/data boundary, owner | keeps a useful local comparison from becoming an unsafe service decision |
| Decision card | selected runtime, rejected alternative, reason, uncertainty, review trigger | turns measurements into one defensible next route |

Academic bridge: runtime choice is applied systems work for transformer inference. Prefill latency depends on prompt length, template rendering, scheduler state, and KV-cache allocation. Decode throughput depends on kernels, quantization, memory bandwidth, batching, speculative decoding, and output length. Endpoint differences can come from route wrappers, tokenizer/chat-template handling, UI prompt assembly, or unsupported sampling controls rather than model intelligence.

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "runtime-comparison-001",
  "run_root": "D:/llm-runs/runtime-comparison",
  "vault_root": "D:/Vaults/PersonalKB",
  "workload": "private local coding assistant",
  "decision_scope": "choose single-user local GPU runtime",
  "primary_metric": "quality_then_latency",
  "selected_runtime": "llama-cpp-q4",
  "rejected_runtime": "ollama-q4",
  "comparison_type": "exact_artifact",
  "frozen_controls": {
    "prompt_suite": ["SMOKE-01", "WORK-01", "JSON-01", "LONG-01"],
    "sampler": "temperature=0, top_p=1",
    "context_target": "8192",
    "output_cap": 256,
    "cold_or_warm": "warm",
    "changed_variables": ["runtime"]
  },
  "candidates": [
    {
      "runtime_id": "llama-cpp-q4",
      "runtime": "llama.cpp",
      "model_id": "example-model-q4",
      "artifact_id": "example-model.Q4_K_M.gguf",
      "route": "openai-compatible",
      "base_url": "http://localhost:8080/v1",
      "hardware_boundary": "Windows CUDA",
      "status": "pass",
      "decision": "select",
      "compatibility_proof": "D:/llm-runs/runtime-comparison/llama-compat.md",
      "api_contract_proof": "D:/llm-runs/runtime-comparison/llama-api.json",
      "benchmark_audit": "D:/llm-runs/runtime-comparison/llama-benchmark-audit.json",
      "quality_proof": "D:/llm-runs/runtime-comparison/llama-quality.json",
      "security_proof": "D:/llm-runs/runtime-comparison/llama-security.md",
      "metrics": {
        "ttft_ms": 510,
        "total_latency_ms": 2700,
        "tokens_per_second": 42,
        "peak_vram_gb": 7.5
      },
      "quality_status": "pass",
      "winner_reason": "same quality, lower total latency, explicit GGUF/offload control",
      "next_action": "promote to result synthesis"
    },
    {
      "runtime_id": "ollama-q4",
      "runtime": "Ollama",
      "model_id": "example-model:q4",
      "artifact_id": "example-model.Q4_K_M.gguf",
      "route": "openai-compatible",
      "base_url": "http://localhost:11434/v1",
      "hardware_boundary": "Windows CUDA",
      "status": "pass",
      "decision": "reject",
      "compatibility_proof": "D:/llm-runs/runtime-comparison/ollama-compat.md",
      "api_contract_proof": "D:/llm-runs/runtime-comparison/ollama-api.json",
      "benchmark_audit": "D:/llm-runs/runtime-comparison/ollama-benchmark-audit.json",
      "quality_proof": "D:/llm-runs/runtime-comparison/ollama-quality.json",
      "security_proof": "D:/llm-runs/runtime-comparison/ollama-security.md",
      "metrics": {
        "ttft_ms": 690,
        "total_latency_ms": 3200,
        "tokens_per_second": 36,
        "peak_vram_gb": 7.3
      },
      "quality_status": "pass",
      "rejection_reason": "same quality, slower on the frozen prompt suite",
      "next_action": "keep as fallback"
    }
  ],
  "decision_card": {
    "winner": "llama-cpp-q4",
    "rejected_alternative": "ollama-q4",
    "why_it_won": "same quality, lower latency, acceptable local boundary",
    "remaining_uncertainty": "not yet tested under concurrency",
    "next_review_trigger": "new model, new runtime version, or shared-use workload"
  }
}
```

Use `comparison_type: "closest_equivalent"` only when the exact artifact cannot be shared. Then include `approximation_reason` and mark the comparison as weaker than an exact artifact comparison. Use `comparison_type: "ui_over_same_provider"` when comparing a UI path against the same provider endpoint.

## Required Evidence Kinds

By default, the runner expects:

| Kind | Required signal |
|---|---|
| `workload_contract` | workload, decision scope, primary metric, acceptance threshold |
| `candidate_identity` | runtime ids, runtime names, model/artifact ids, base URL, route, hardware |
| `endpoint_proof` | compatibility and API-contract proof for each candidate |
| `frozen_controls` | same prompt suite, sampler, context target, output cap, cold/warm state |
| `benchmark_audit` | benchmark evidence audit or benchmark proof for each candidate |
| `quality_boundary` | quality proof and pass/hold/fail status for each candidate |
| `security_boundary` | loopback/local proof or approved exposure proof |
| `decision_card` | winner, rejected alternative, why, uncertainty, review trigger |

## Standard-Library Runner

Save this as `local_llm_runtime_comparison_runner.py` inside the run folder. It uses only Python's standard library.

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
from urllib.parse import urlparse


DEFAULT_REQUIRED_KINDS = [
    "workload_contract",
    "candidate_identity",
    "endpoint_proof",
    "frozen_controls",
    "benchmark_audit",
    "quality_boundary",
    "security_boundary",
    "decision_card",
]

STATUS_VALUES = {
    "pass": "pass",
    "passed": "pass",
    "ready": "pass",
    "complete": "pass",
    "select": "pass",
    "selected": "pass",
    "keep": "pass",
    "reject": "pass",
    "rejected": "pass",
    "hold": "hold",
    "blocked": "hold",
    "gap": "hold",
    "missing": "hold",
    "incomplete": "hold",
    "partial": "hold",
    "not-started": "hold",
    "not started": "hold",
    "skip": "hold",
    "skipped": "hold",
    "fail": "fail",
    "failed": "fail",
    "error": "fail",
    "timeout": "fail",
    "oom": "fail",
    "unsafe": "fail",
}

STATUS_RANK = {"pass": 0, "hold": 1, "fail": 2}
LINK_OPEN = "[" + "["
LINK_CLOSE = "]" + "]"


def utc_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def text(value: Any) -> str:
    return str(value or "").strip()


def norm(value: Any) -> str:
    return text(value).lower()


def slug(value: Any) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "-", text(value).lower())
    return cleaned.strip("-") or "runtime-comparison"


def status_value(value: Any) -> str:
    return STATUS_VALUES.get(norm(value).replace("_", "-"), "hold")


def bool_value(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if value in (None, ""):
        return default
    lowered = norm(value).replace("_", "-").replace(" ", "-")
    if lowered in {"true", "yes", "y", "1", "required", "critical", "approved"}:
        return True
    if lowered in {"false", "no", "n", "0", "optional", "waived", "not-required"}:
        return False
    return default


def num_value(value: Any) -> float | None:
    if value in (None, ""):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    match = re.search(r"-?\d+(?:\.\d+)?", str(value))
    return float(match.group(0)) if match else None


def list_value(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [text(item) for item in value if text(item)]
    if isinstance(value, tuple):
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


def load_manifest() -> tuple[Path, dict[str, Any]]:
    manifest_path = os.environ.get("LOCAL_LLM_RUNTIME_COMPARISON_MANIFEST")
    if not manifest_path:
        raise ValueError("Set LOCAL_LLM_RUNTIME_COMPARISON_MANIFEST to a JSON manifest path.")
    path = Path(manifest_path).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"Manifest path does not exist: {path}")
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError("Manifest must be a JSON object.")
    return path, data


def strip_obsidian_link(value: str) -> str:
    cleaned = value.strip()
    if cleaned.startswith(LINK_OPEN) and cleaned.endswith(LINK_CLOSE):
        inner = cleaned[2:-2]
        return inner.split("|", 1)[0].split("#", 1)[0].strip()
    return cleaned


def proof_candidates(proof: str, vault_root: Path | None, manifest_dir: Path) -> list[Path]:
    stripped = strip_obsidian_link(proof)
    if not stripped or re.match(r"^[a-z]+://", stripped):
        return []
    path = Path(stripped).expanduser()
    candidates = [path] if path.is_absolute() else [manifest_dir / path]
    if vault_root and not path.is_absolute():
        candidates.append(vault_root / path)
        if not stripped.lower().endswith(".md"):
            candidates.append(vault_root / f"{stripped}.md")
    return candidates


def proof_status(row: dict[str, Any], fields: list[str], vault_root: Path | None, manifest_dir: Path) -> tuple[bool, str]:
    proofs: list[str] = []
    for field in fields:
        proofs.extend(list_value(row.get(field)))
    proofs.extend(list_value(row.get("proofs")))
    if not proofs:
        if text(row.get("waiver_reason")) or text(row.get("not_applicable_reason")):
            return True, "waived"
        return False, "missing proof"
    missing = []
    for proof in proofs:
        if re.match(r"^https?://", proof):
            continue
        candidates = proof_candidates(proof, vault_root, manifest_dir)
        if candidates and any(path.exists() for path in candidates):
            continue
        missing.append(proof)
    if missing:
        return False, "unresolved proof: " + "; ".join(missing[:3])
    return True, "ok"


def metric(row: dict[str, Any], *names: str) -> Any:
    metrics = row.get("metrics") if isinstance(row.get("metrics"), dict) else {}
    for name in names:
        if name in row and row[name] not in (None, ""):
            return row[name]
        if name in metrics and metrics[name] not in (None, ""):
            return metrics[name]
    return None


def add_issue(issues: list[dict[str, Any]], severity: str, kind: str, owner: str, message: str, route: str, row_id: str = "") -> None:
    issues.append({
        "severity": severity,
        "kind": kind,
        "owner": owner,
        "row_id": row_id,
        "message": message,
        "next_route": route,
    })


def is_loopback_url(value: str) -> bool:
    if not value:
        return False
    parsed = urlparse(value if "://" in value else f"http://{value}")
    host = (parsed.hostname or "").lower()
    return host in {"localhost", "127.0.0.1", "::1"}


def is_exposed_url(value: str) -> bool:
    if not value:
        return False
    parsed = urlparse(value if "://" in value else f"http://{value}")
    host = (parsed.hostname or "").lower()
    return host in {"0.0.0.0", "::"} or bool(re.match(r"^(10\.|172\.(1[6-9]|2\d|3[0-1])\.|192\.168\.)", host))


def compare_sets(values: list[list[str]]) -> bool:
    if not values:
        return False
    first = values[0]
    return all(items == first for items in values[1:])


def check_manifest(manifest: dict[str, Any], issues: list[dict[str, Any]]) -> None:
    if not text(manifest.get("workload")):
        add_issue(issues, "hold", "workload_contract", "workload", "Manifest has no workload.", "LLM/Study/Local LLM Runtime Comparison Lab")
    if not text(manifest.get("decision_scope")):
        add_issue(issues, "hold", "workload_contract", "workload", "Manifest has no decision_scope.", "LLM/Study/Local LLM Runtime Comparison Lab")
    if not text(manifest.get("primary_metric")):
        add_issue(issues, "hold", "workload_contract", "metrics", "Manifest has no primary_metric.", "LLM/Study/Local LLM Inference Metrics Field Guide")
    if not text(manifest.get("selected_runtime")):
        add_issue(issues, "hold", "decision_card", "decision", "Manifest has no selected_runtime.", "LLM/Study/LLM Deployment Decision Matrix")
    if not text(manifest.get("rejected_runtime")) and not text(manifest.get("not_applicable_reason")):
        add_issue(issues, "hold", "decision_card", "decision", "Manifest has no rejected_runtime or not_applicable_reason.", "LLM/Study/Local LLM Runtime Comparison Lab")
    comparison_type = norm(manifest.get("comparison_type"))
    if comparison_type not in {"exact_artifact", "closest_equivalent", "ui_over_same_provider", "exploratory"}:
        add_issue(issues, "hold", "frozen_controls", "confounders", "comparison_type should be exact_artifact, closest_equivalent, ui_over_same_provider, or exploratory.", "LLM/Study/Local LLM Runtime Comparison Lab")
    if comparison_type in {"closest_equivalent", "exploratory"} and not text(manifest.get("approximation_reason")):
        add_issue(issues, "hold", "frozen_controls", "confounders", "Approximate or exploratory comparisons need approximation_reason.", "LLM/Study/Local LLM Runtime Comparison Lab")


def check_controls(manifest: dict[str, Any], candidates: list[dict[str, Any]], issues: list[dict[str, Any]]) -> None:
    controls = manifest.get("frozen_controls") if isinstance(manifest.get("frozen_controls"), dict) else {}
    prompt_suite = list_value(controls.get("prompt_suite") or manifest.get("prompt_suite"))
    if len(prompt_suite) < 2:
        add_issue(issues, "hold", "frozen_controls", "prompts", "Frozen prompt suite should contain at least two prompt ids.", "LLM/Study/Local LLM Runtime Comparison Lab")
    for field, route in [
        ("sampler", "LLM/Study/Decoding and Sampling Controls Runner"),
        ("context_target", "LLM/Study/Local LLM Context Window and Token Budgeting Runner"),
        ("output_cap", "LLM/Study/Local LLM First Benchmark Row Builder"),
        ("cold_or_warm", "LLM/Study/Local LLM Benchmark Evidence Audit Runner"),
    ]:
        if not text(controls.get(field) or manifest.get(field)):
            add_issue(issues, "hold", "frozen_controls", "confounders", f"Frozen control missing: {field}.", route)

    changed = list_value(controls.get("changed_variables") or manifest.get("changed_variables"))
    comparison_type = norm(manifest.get("comparison_type"))
    if comparison_type == "exact_artifact" and changed != ["runtime"]:
        add_issue(issues, "hold", "frozen_controls", "confounders", "Exact runtime comparisons should list changed_variables as only runtime.", "LLM/Study/Local LLM Runtime Comparison Lab")
    if len(changed) > 1 and comparison_type != "exploratory":
        add_issue(issues, "hold", "frozen_controls", "confounders", "Multiple changed variables require exploratory comparison_type or a weaker conclusion.", "LLM/Study/Local LLM Runtime Comparison Lab")

    candidate_suites = [list_value(candidate.get("prompt_suite")) for candidate in candidates if candidate.get("prompt_suite")]
    if candidate_suites and not compare_sets(candidate_suites):
        add_issue(issues, "fail", "frozen_controls", "prompts", "Candidate prompt_suite values differ.", "LLM/Study/Local LLM Runtime Comparison Lab")


def check_candidate(candidate: dict[str, Any], manifest: dict[str, Any], issues: list[dict[str, Any]], vault_root: Path | None, manifest_dir: Path) -> None:
    row_id = text(candidate.get("runtime_id") or candidate.get("runtime") or "candidate")
    required_fields = ["runtime_id", "runtime", "model_id", "route", "base_url", "hardware_boundary"]
    missing = [field for field in required_fields if not text(candidate.get(field))]
    if missing:
        add_issue(issues, "hold", "candidate_identity", "identity", "Candidate missing: " + ", ".join(missing) + ".", "LLM/Study/Local LLM Runtime Compatibility Runner", row_id)

    if status_value(candidate.get("status")) == "fail":
        add_issue(issues, "fail", "endpoint_proof", "endpoint", "Candidate status is fail.", "LLM/Study/Local LLM Runtime Compatibility Runner", row_id)

    for field, route in [
        ("compatibility_proof", "LLM/Study/Local LLM Runtime Compatibility Runner"),
        ("api_contract_proof", "LLM/Study/Local LLM OpenAI-Compatible API Contract Runner"),
    ]:
        proof_ok, proof_msg = proof_status(candidate, [field], vault_root, manifest_dir)
        if not proof_ok:
            add_issue(issues, "hold", "endpoint_proof", "endpoint", f"{field} problem: {proof_msg}.", route, row_id)

    benchmark_ok, benchmark_msg = proof_status(candidate, ["benchmark_audit", "benchmark_proof"], vault_root, manifest_dir)
    if not benchmark_ok:
        add_issue(issues, "hold", "benchmark_audit", "metrics", f"Benchmark audit proof problem: {benchmark_msg}.", "LLM/Study/Local LLM Benchmark Evidence Audit Runner", row_id)

    quality_ok, quality_msg = proof_status(candidate, ["quality_proof", "quality_runner_output"], vault_root, manifest_dir)
    if not quality_ok:
        add_issue(issues, "hold", "quality_boundary", "quality", f"Quality proof problem: {quality_msg}.", "LLM/Study/Local LLM Quality Evaluation Runner", row_id)

    quality_status = status_value(candidate.get("quality_status"))
    decision = norm(candidate.get("decision"))
    if quality_status == "fail" and decision in {"select", "selected", "keep", "winner", "deploy"}:
        add_issue(issues, "fail", "quality_boundary", "quality", "Selected/kept candidate has failing quality.", "LLM/Study/Local LLM Quality Evaluation Runner", row_id)
    if quality_status == "hold" and not text(candidate.get("quality_scope")) and not text(candidate.get("waiver_reason")):
        add_issue(issues, "hold", "quality_boundary", "quality", "Candidate needs quality_status, quality_scope, or waiver reason.", "LLM/Study/Local LLM Quality Evaluation Runner", row_id)

    timing_values = [num_value(metric(candidate, name)) for name in ["ttft_ms", "total_latency_ms", "tokens_per_second", "p95_latency_ms", "request_throughput_per_s"] if metric(candidate, name) is not None]
    if not timing_values:
        add_issue(issues, "hold", "benchmark_audit", "metrics", "Candidate has no timing or throughput metric summary.", "LLM/Study/Local LLM Benchmark Evidence Audit Runner", row_id)
    if any(value is not None and value < 0 for value in timing_values):
        add_issue(issues, "fail", "benchmark_audit", "metrics", "Timing and throughput metrics cannot be negative.", "LLM/Study/Local LLM Benchmark Evidence Audit Runner", row_id)

    base_url = text(candidate.get("base_url"))
    exposure = norm(candidate.get("exposure") or candidate.get("host_boundary"))
    security_ok, security_msg = proof_status(candidate, ["security_proof", "boundary_proof"], vault_root, manifest_dir)
    if is_exposed_url(base_url) and not bool_value(candidate.get("exposure_approved")):
        add_issue(issues, "fail", "security_boundary", "security", "Candidate base_url appears exposed without exposure_approved.", "LLM/Study/Local LLM Security and Privacy Runner", row_id)
    elif not is_loopback_url(base_url) and exposure not in {"loopback", "local", "approved", "approved-lan"} and not bool_value(candidate.get("exposure_approved")):
        add_issue(issues, "hold", "security_boundary", "security", "Candidate is not clearly loopback/local or approved.", "LLM/Study/Local LLM Security and Privacy Runner", row_id)
    if not security_ok:
        add_issue(issues, "hold", "security_boundary", "security", f"Security proof problem: {security_msg}.", "LLM/Study/Local LLM Security and Privacy Runner", row_id)

    if decision in {"select", "selected", "winner", "keep"} and not text(candidate.get("winner_reason")):
        add_issue(issues, "hold", "decision_card", "decision", "Selected candidate has no winner_reason.", "LLM/Study/LLM Deployment Decision Matrix", row_id)
    if decision in {"reject", "rejected"} and not text(candidate.get("rejection_reason")):
        add_issue(issues, "hold", "decision_card", "decision", "Rejected candidate has no rejection_reason.", "LLM/Study/LLM Deployment Decision Matrix", row_id)


def check_decision_card(manifest: dict[str, Any], candidates: list[dict[str, Any]], issues: list[dict[str, Any]]) -> None:
    card = manifest.get("decision_card") if isinstance(manifest.get("decision_card"), dict) else {}
    selected = text(manifest.get("selected_runtime") or card.get("winner"))
    rejected = text(manifest.get("rejected_runtime") or card.get("rejected_alternative"))
    ids = {text(candidate.get("runtime_id")) for candidate in candidates if text(candidate.get("runtime_id"))}
    if selected and selected not in ids:
        add_issue(issues, "fail", "decision_card", "decision", f"selected_runtime is not present: {selected}", "LLM/Study/Local LLM Runtime Comparison Lab")
    if rejected and rejected not in ids:
        add_issue(issues, "fail", "decision_card", "decision", f"rejected_runtime is not present: {rejected}", "LLM/Study/Local LLM Runtime Comparison Lab")
    if selected and rejected and selected == rejected:
        add_issue(issues, "fail", "decision_card", "decision", "selected_runtime and rejected_runtime are the same.", "LLM/Study/Local LLM Runtime Comparison Lab")
    for field in ["why_it_won", "remaining_uncertainty", "next_review_trigger"]:
        if not text(card.get(field) or manifest.get(field)):
            add_issue(issues, "hold", "decision_card", "decision", f"Decision card missing: {field}.", "LLM/Study/LLM Deployment Decision Matrix")


def evaluate(manifest_path: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    issues: list[dict[str, Any]] = []
    vault_text = text(manifest.get("vault_root"))
    vault_root = Path(vault_text).expanduser().resolve() if vault_text else None
    if vault_root and not vault_root.exists():
        add_issue(issues, "hold", "manifest", "vault", f"vault_root does not exist: {vault_root}", "LLM/Study/LLM Study Index")

    check_manifest(manifest, issues)
    candidates_raw = manifest.get("candidates") or manifest.get("runtimes") or []
    if not isinstance(candidates_raw, list):
        add_issue(issues, "fail", "candidate_identity", "manifest", "candidates must be a list.", "LLM/Study/Local LLM Runtime Comparison Lab")
        candidates_raw = []
    candidates = [candidate for candidate in candidates_raw if isinstance(candidate, dict)]
    if len(candidates) < 2 and not text(manifest.get("not_applicable_reason")):
        add_issue(issues, "hold", "candidate_identity", "identity", "Runtime comparison needs two candidates or a not_applicable_reason.", "LLM/Study/Local LLM Runtime Comparison Lab")

    check_controls(manifest, candidates, issues)
    for candidate in candidates:
        check_candidate(candidate, manifest, issues, vault_root, manifest_path.parent)
    check_decision_card(manifest, candidates, issues)

    required_kinds = list_value(manifest.get("required_kinds")) or DEFAULT_REQUIRED_KINDS
    present_kinds = set(DEFAULT_REQUIRED_KINDS)
    status_by_kind = {kind: "pass" for kind in present_kinds}
    for issue in issues:
        kind = str(issue.get("kind") or "unknown")
        present_kinds.add(kind)
        current = str(issue.get("severity") or "hold")
        previous = status_by_kind.get(kind, "pass")
        status_by_kind[kind] = current if STATUS_RANK[current] > STATUS_RANK[previous] else previous

    final_status = "pass"
    if any(issue["severity"] == "fail" for issue in issues):
        final_status = "fail"
    elif issues:
        final_status = "hold"

    if final_status == "pass":
        decision = "runtime_comparison_ready"
        next_route = "LLM/Study/Local LLM Result Synthesis Runner"
    elif final_status == "fail":
        decision = "runtime_comparison_blocked"
        next_route = first_route(issues, "LLM/Study/Local LLM Runtime Comparison Lab")
    else:
        decision = "runtime_comparison_incomplete"
        next_route = first_route(issues, "LLM/Study/Local LLM Runtime Comparison Lab")

    return {
        "run_id": text(manifest.get("run_id") or manifest_path.stem),
        "generated_at": utc_iso(),
        "status": final_status,
        "decision": decision,
        "next_route": next_route,
        "workload": text(manifest.get("workload")),
        "decision_scope": text(manifest.get("decision_scope")),
        "comparison_type": text(manifest.get("comparison_type")),
        "selected_runtime": text(manifest.get("selected_runtime")),
        "rejected_runtime": text(manifest.get("rejected_runtime")),
        "candidate_count": len(candidates),
        "required_kinds": required_kinds,
        "present_kinds": sorted(present_kinds),
        "missing_required_kinds": [kind for kind in required_kinds if kind not in present_kinds],
        "status_by_kind": status_by_kind,
        "issues": issues,
        "source_manifest": str(manifest_path),
    }


def first_route(issues: list[dict[str, Any]], fallback: str) -> str:
    for severity in ("fail", "hold"):
        for issue in issues:
            if issue.get("severity") == severity and issue.get("next_route"):
                return str(issue["next_route"])
    return fallback


def md_cell(value: Any) -> str:
    return text(value).replace("|", "\\|").replace("\n", " ")


def markdown_report(result: dict[str, Any]) -> str:
    lines = [
        f"# Local LLM Runtime Comparison Audit - {result['run_id']}",
        "",
        f"- Generated: {result['generated_at']}",
        f"- Status: `{result['status']}`",
        f"- Decision: `{result['decision']}`",
        f"- Selected runtime: `{result.get('selected_runtime') or 'missing'}`",
        f"- Rejected runtime: `{result.get('rejected_runtime') or 'missing'}`",
        f"- Next route: {LINK_OPEN}{result['next_route']}{LINK_CLOSE}",
        "",
        "## Coverage",
        "",
        "| Required kind | Present | Status |",
        "|---|---:|---|",
    ]
    present = set(result.get("present_kinds") or [])
    status_by_kind = result.get("status_by_kind") or {}
    for kind in result.get("required_kinds") or []:
        lines.append(f"| `{kind}` | {'yes' if kind in present else 'no'} | `{status_by_kind.get(kind, 'missing')}` |")
    lines.extend(["", "## Issues", ""])
    issues = result.get("issues") or []
    if not issues:
        lines.append("No blocking or hold issues found.")
    else:
        lines.extend(["| Severity | Kind | Owner | Message | Next route |", "|---|---|---|---|---|"])
        for issue in issues:
            lines.append(
                "| "
                + " | ".join([
                    md_cell(issue.get("severity")),
                    md_cell(issue.get("kind")),
                    md_cell(issue.get("owner")),
                    md_cell(issue.get("message")),
                    LINK_OPEN + md_cell(issue.get("next_route")) + LINK_CLOSE,
                ])
                + " |"
            )
    lines.extend([
        "",
        "## Interpretation",
        "",
        "A `pass` means the runtime comparison can feed result synthesis. A `hold` means the comparison may still be exploratory but is missing proof, frozen controls, benchmark audit, quality boundary, security proof, or decision-card fields. A `fail` means the comparison is contradicted or unsafe enough that it should not support deployment.",
    ])
    return "\n".join(lines) + "\n"


def write_outputs(manifest_path: Path, manifest: dict[str, Any], result: dict[str, Any]) -> dict[str, str]:
    run_root = Path(text(manifest.get("run_root")) or manifest_path.parent).expanduser()
    if not run_root.is_absolute():
        run_root = manifest_path.parent / run_root
    run_root.mkdir(parents=True, exist_ok=True)
    base = run_root / f"{slug(result['run_id'])}-runtime-comparison"
    json_path = base.with_suffix(".json")
    csv_path = base.with_suffix(".csv")
    md_path = base.with_suffix(".md")
    jsonl_path = base.with_suffix(".jsonl")

    json_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    md_path.write_text(markdown_report(result), encoding="utf-8")
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        fields = ["severity", "kind", "owner", "row_id", "message", "next_route"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for issue in result.get("issues") or []:
            writer.writerow({field: issue.get(field, "") for field in fields})
    with jsonl_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps({
            "event": "local_llm_runtime_comparison_audit",
            "recorded_at": utc_iso(),
            "run_id": result["run_id"],
            "status": result["status"],
            "decision": result["decision"],
            "issues": len(result.get("issues") or []),
        }, ensure_ascii=False) + "\n")
    return {
        "json": str(json_path),
        "csv": str(csv_path),
        "markdown": str(md_path),
        "jsonl": str(jsonl_path),
    }


def main() -> int:
    try:
        manifest_path, manifest = load_manifest()
        result = evaluate(manifest_path, manifest)
        result["outputs"] = write_outputs(manifest_path, manifest, result)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0
    except Exception as exc:
        error = {
            "generated_at": utc_iso(),
            "status": "error",
            "decision": "manifest_error",
            "error": str(exc),
        }
        print(json.dumps(error, indent=2, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
```

## Fixture Matrix

Use these before trusting the audit:

| Fixture | Expected decision | Reason |
|---|---|---|
| complete exact-artifact two-runtime comparison with matching controls, proof links, quality pass, selected winner, rejected alternative, and review trigger | `pass/runtime_comparison_ready` | comparison can feed result synthesis |
| one runtime only with no not-applicable reason | `hold/runtime_comparison_incomplete` | no alternative was actually compared |
| closest-equivalent comparison without approximation reason | `hold/runtime_comparison_incomplete` | model/artifact difference weakens the claim |
| selected runtime has `quality_status: fail` | `fail/runtime_comparison_blocked` | speed cannot override failed workload quality |
| candidate binds to `0.0.0.0` without exposure approval | `fail/runtime_comparison_blocked` | deployment evidence cannot depend on accidental exposure |
| candidate prompt suites differ | `fail/runtime_comparison_blocked` | the comparison changed prompt inputs |
| missing benchmark audit proof | `hold/runtime_comparison_incomplete` | raw numbers are not reviewable |

## Completion Gate

This runner is complete when:

- [ ] workload, decision scope, primary metric, selected runtime, and rejected runtime are recorded
- [ ] two candidates have runtime id, model/artifact id, route, base URL, hardware boundary, compatibility proof, and API-contract proof
- [ ] prompt suite, sampler, context target, output cap, and cold/warm state are frozen
- [ ] exact comparisons change only `runtime`; approximate comparisons name the approximation reason
- [ ] each candidate links benchmark evidence audit output and quality evidence
- [ ] loopback/local security proof exists, or exposure approval is explicit
- [ ] the selected runtime has winner reason, rejected alternative, uncertainty, and review trigger
- [ ] the output routes to [[LLM/Study/Local LLM Result Synthesis Runner|Local LLM Result Synthesis Runner]] or a remediation note

## References

Internal:

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Runtime Comparison Lab]]
- [[LLM/Study/Local LLM Runtime Compatibility Runner]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]]
- [[LLM/Study/Local llama.cpp GGUF Server Runner]]
- [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab]]
- [[LLM/Study/Local LLM Docker GPU Container Serving Lab]]
- [[LLM/Study/Local LLM Benchmark Evidence Audit Runner]]
- [[LLM/Study/Local LLM Quality Evaluation Runner]]
- [[LLM/Study/Local LLM Security and Privacy Runner]]
- [[LLM/Study/Local LLM Result Synthesis Runner]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/Study/LLM Deployment Readiness Audit Runner]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching]]

Current external docs checked 2026-06-16:

- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
- [LM Studio OpenAI compatibility endpoints](https://lmstudio.ai/docs/developer/openai-compat)
- [llama.cpp server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
- [vLLM OpenAI-compatible server](https://docs.vllm.ai/en/latest/serving/online_serving/openai_compatible_server/)
- [SGLang OpenAI-compatible chat completions](https://docs.sglang.io/docs/basic_usage/openai_api_completions)
