---
tags: [study, llm, inference, local-llm, benchmark, metrics, latency, throughput, evidence, audit, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice, deep-dive]
last-verified: 2026-06-16
---

# Local LLM Benchmark Evidence Audit Runner

> **One-line summary** A benchmark row is useful only when it proves what ran, which route answered, which timing phase was measured, which token counts normalize it, which confounders were fixed, and what one next action follows.

Use this after [[LLM/Study/Local LLM First Benchmark Row Builder|Local LLM First Benchmark Row Builder]], [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]], [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner|Local LLM Concurrency and Batch Throughput Runner]], or a runtime-specific benchmark output has produced saved rows. Use it before [[LLM/Study/Local LLM Runtime Comparison Runner|Local LLM Runtime Comparison Runner]] when the benchmark row supports a runtime choice, before [[LLM/Study/Local LLM Result Synthesis Runner|Local LLM Result Synthesis Runner]], before [[LLM/Study/LLM Deployment Readiness Audit Runner|LLM Deployment Readiness Audit Runner]], or before any decision that says a runtime, model, quantization, context setting, prompt-cache setting, speculative-decoding path, or deployment mode is faster.

This runner does not benchmark a live endpoint. It audits saved benchmark rows and proof links. That makes it safe to run after Ollama native responses, OpenAI-compatible client logs, vLLM benchmark JSON, SGLang benchmark/profiling output, GenAI-Perf-style metrics, or a hand-entered benchmark-log row.

Current dated proof: [[LLM/Study/Local LLM First Benchmark Row Proof - 2026-06-16|Local LLM First Benchmark Row Proof - 2026-06-16]] records a `pass/benchmark_evidence_ready` audit for the first-smoke OpenAI-compatible benchmark row, scoped to interpretation-only use with quality, capacity, and comparison limits explicit.

## What This Proves

| Evidence family | Checks | Why it matters |
|---|---|---|
| Workload contract | task, latency/throughput target, quality bar, decision scope | prevents "fast" from being context-free |
| Run identity | run id, model, artifact, runtime, route, hardware boundary | prevents comparing the wrong model or endpoint |
| Source artifacts | proof paths for raw response, client log, streaming log, benchmark JSON, or metric export | makes numbers reviewable |
| Prompt and token accounting | prompt id, prompt tokens, output cap, output tokens, context setting | separates prefill, decode, and total length effects |
| Timing metrics | TTFT, TPOT/ITL, total latency, tokens/sec, request throughput, p50/p95 when relevant | ties each number to a request phase |
| Memory and context | peak RAM/VRAM, context margin, active sequences, queue depth, error class | catches fit and saturation risk |
| Fixed settings | sampler, template/tokenizer proof, cold/warm state, changed variable list | prevents confounded comparisons |
| Quality boundary | quality result, rubric link, or explicit "route/performance only" scope | prevents speed from replacing quality |
| Interpretation | mechanism owner, rejected alternative, next controlled action, review trigger | turns metrics into one action |

Academic bridge: benchmarking local LLMs is applied transformer theory. TTFT is usually prefill, queue, cold-load, or client overhead; TPOT/ITL belongs to decode; tokens/sec depends on output length and measurement window; prompt tokens and context drive KV-cache pressure; concurrency changes active sequences and scheduler behavior. This runner forces those distinctions into the row before the number is reused.

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "benchmark-audit-001",
  "run_root": "D:/llm-runs/benchmark-audit",
  "vault_root": "D:/Vaults/PersonalKB",
  "workload": "private local coding assistant",
  "decision_scope": "accept one local GPU baseline",
  "latency_target_ms": 2500,
  "selected_benchmark": "qwen-q4-json-01",
  "benchmark_rows": [
    {
      "id": "qwen-q4-json-01",
      "status": "pass",
      "decision": "keep",
      "proof": "D:/llm-runs/benchmark-audit/qwen-q4-json-01.json",
      "model_id": "example-model",
      "runtime": "llama.cpp",
      "route": "openai-compatible",
      "hardware_boundary": "Windows CUDA",
      "prompt_id": "JSON-01",
      "prompt_tokens": 420,
      "output_cap": 160,
      "output_tokens": 96,
      "cold_or_warm": "warm",
      "sampler": "temperature=0, top_p=1",
      "changed_variables": ["quantization"],
      "metrics": {
        "ttft_ms": 540,
        "tpot_ms": 24,
        "total_latency_ms": 2850,
        "tokens_per_second": 41.6,
        "peak_vram_gb": 7.2,
        "context_margin_tokens": 7200
      },
      "quality_result": "pass",
      "mechanism_owner": "decode",
      "next_action": "keep as single-user baseline, then run concurrency ladder"
    }
  ],
  "evidence": [
    {
      "id": "workload",
      "kind": "workload_contract",
      "status": "pass",
      "critical": true,
      "proof": "LLM/Study/Local LLM Inference Benchmark Log.md",
      "claim": "Interactive coding helper must stay under the latency target while preserving JSON quality."
    }
  ]
}
```

`proof` may be an absolute path, a vault-relative path, an Obsidian note path, an Obsidian link, or an `https://` source URL for benchmark-tool documentation. Use `waiver_reason` only when the audit is explicitly scoped to a narrow row, such as route-only smoke evidence where quality has not yet been tested.

## Required Evidence Kinds

By default, the runner expects one evidence row for each kind:

| Kind | Required signal |
|---|---|
| `workload_contract` | workload, target, quality bar, decision scope, or proof |
| `run_identity` | model, runtime, route, hardware, artifact, or proof |
| `source_artifacts` | raw response, client log, benchmark JSON, streaming JSONL, or metric export proof |
| `prompt_token_accounting` | prompt id, prompt tokens or tokenizer proof, output cap/reserve, output tokens when available |
| `timing_metrics` | TTFT, TPOT/ITL, total latency, tokens/sec, throughput, p50/p95, or benchmark-tool output |
| `memory_context_metrics` | RAM/VRAM, context margin, active sequences, queue, or explicit not-exposed reason |
| `fixed_settings` | sampler, template/tokenizer, cold/warm state, changed variables, and controlled confounders |
| `quality_boundary` | quality result/rubric, quality-runner link, or explicit route/performance-only scope |
| `interpretation_next_action` | mechanism owner, decision, next action, rejected alternative, and retest trigger |

You can override this with `required_kinds` in the manifest.

## Standard-Library Runner

Save this as `local_llm_benchmark_evidence_audit_runner.py` inside the run folder. It uses only Python's standard library.

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
    "run_identity",
    "source_artifacts",
    "prompt_token_accounting",
    "timing_metrics",
    "memory_context_metrics",
    "fixed_settings",
    "quality_boundary",
    "interpretation_next_action",
]

KIND_HINTS = {
    "workload_contract": ("workload", "State workload, target, quality bar, and decision scope.", "LLM/Study/Local LLM Inference Benchmark Log"),
    "run_identity": ("identity", "Attach model, artifact, runtime, route, hardware, and environment identity.", "LLM/Study/Local LLM Runtime Stack Anatomy"),
    "source_artifacts": ("provenance", "Attach raw response, client log, streaming log, benchmark JSON, metrics export, or note proof.", "LLM/Study/Local LLM First Benchmark Row Builder"),
    "prompt_token_accounting": ("tokens", "Record prompt id, prompt tokens or tokenizer proof, output cap, and output tokens when exposed.", "LLM/Study/Local LLM Context Window and Token Budgeting Runner"),
    "timing_metrics": ("latency", "Record TTFT, TPOT/ITL, total latency, tokens/sec, p50/p95, or benchmark-tool output.", "LLM/Study/Local LLM Inference Metrics Field Guide"),
    "memory_context_metrics": ("capacity", "Record RAM/VRAM, context margin, active sequences, queue, or not-exposed reason.", "LLM/Study/Local LLM Hardware Sizing Runner"),
    "fixed_settings": ("confounders", "Freeze sampler, template/tokenizer, cold/warm state, changed variables, and route.", "LLM/Study/Decoding and Sampling Controls Runner"),
    "quality_boundary": ("quality", "Attach quality result/rubric or explicitly scope the row to performance only.", "LLM/Study/Local LLM Quality Evaluation Runner"),
    "interpretation_next_action": ("decision", "Name mechanism owner, decision, next action, rejected alternative, and retest trigger.", "LLM/Study/Local LLM Result Synthesis Runner"),
}

STATUS_VALUES = {
    "pass": "pass",
    "passed": "pass",
    "complete": "pass",
    "ready": "pass",
    "keep": "pass",
    "hold": "hold",
    "blocked": "hold",
    "gap": "hold",
    "missing": "hold",
    "incomplete": "hold",
    "not-started": "hold",
    "not started": "hold",
    "skip": "hold",
    "skipped": "hold",
    "fail": "fail",
    "failed": "fail",
    "reject": "fail",
    "rejected": "fail",
    "error": "fail",
    "timeout": "fail",
    "oom": "fail",
}

STATUS_RANK = {"pass": 0, "hold": 1, "fail": 2}
LINK_OPEN = "[" + "["
LINK_CLOSE = "]" + "]"


def utc_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def text(value: Any) -> str:
    return str(value or "").strip()


def norm(value: Any) -> str:
    return text(value).lower()


def slug(value: Any) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "-", text(value).lower())
    return cleaned.strip("-") or "benchmark-evidence"


def status_value(value: Any) -> str:
    return STATUS_VALUES.get(norm(value).replace("_", "-"), "hold")


def bool_value(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if value in (None, ""):
        return default
    lowered = norm(value).replace("_", "-").replace(" ", "-")
    if lowered in {"true", "yes", "y", "1", "required", "critical"}:
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
    manifest_path = os.environ.get("LOCAL_LLM_BENCHMARK_AUDIT_MANIFEST")
    if not manifest_path:
        raise ValueError("Set LOCAL_LLM_BENCHMARK_AUDIT_MANIFEST to a JSON manifest path.")
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


def proof_status(row: dict[str, Any], vault_root: Path | None, manifest_dir: Path) -> tuple[bool, str]:
    proofs = list_value(row.get("proofs")) + list_value(row.get("proof"))
    if not proofs:
        if text(row.get("waiver_reason")) or text(row.get("not_exposed_reason")):
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


def evidence_row_checks(row: dict[str, Any], issues: list[dict[str, Any]], vault_root: Path | None, manifest_dir: Path) -> None:
    kind = text(row.get("kind") or "uncategorized")
    owner, hint, route = KIND_HINTS.get(kind, ("evidence", "Attach proof.", "LLM/Study/LLM Study Index"))
    row_id = text(row.get("id") or kind)
    status = status_value(row.get("status"))
    required = bool_value(row.get("required"), True)
    critical = bool_value(row.get("critical"), False)
    proof_ok, proof_msg = proof_status(row, vault_root, manifest_dir)

    if required and not proof_ok:
        add_issue(issues, "fail" if critical else "hold", kind, owner, f"{hint} Proof problem: {proof_msg}.", route, row_id)
    if status == "fail":
        add_issue(issues, "fail" if critical else "hold", kind, owner, text(row.get("evidence") or row.get("claim") or "Evidence row failed."), route, row_id)
    if status == "hold" and required and not text(row.get("waiver_reason")):
        add_issue(issues, "hold", kind, owner, text(row.get("evidence") or row.get("claim") or "Evidence row incomplete."), route, row_id)


def benchmark_checks(manifest: dict[str, Any], issues: list[dict[str, Any]], vault_root: Path | None, manifest_dir: Path) -> list[dict[str, Any]]:
    rows = manifest.get("benchmark_rows") or manifest.get("benchmarks") or []
    if not isinstance(rows, list):
        add_issue(issues, "fail", "benchmark_rows", "manifest", "benchmark_rows must be a list.", "LLM/Study/Local LLM Inference Benchmark Log")
        return []
    normalized = [row for row in rows if isinstance(row, dict)]
    if not normalized:
        add_issue(issues, "hold", "benchmark_rows", "metrics", "No benchmark rows are present.", "LLM/Study/Local LLM First Benchmark Row Builder")
        return []

    selected = text(manifest.get("selected_benchmark"))
    by_id = {text(row.get("id")): row for row in normalized if text(row.get("id"))}
    if selected and selected not in by_id:
        add_issue(issues, "fail", "benchmark_rows", "selection", f"selected_benchmark is not present: {selected}", "LLM/Study/Local LLM Inference Benchmark Log")

    for row in normalized:
        row_id = text(row.get("id") or row.get("run_id") or "benchmark")
        required = bool_value(row.get("required"), True)
        critical = bool_value(row.get("critical"), False)
        proof_ok, proof_msg = proof_status(row, vault_root, manifest_dir)
        if required and not proof_ok:
            add_issue(issues, "fail" if critical else "hold", "source_artifacts", "provenance", f"Benchmark row proof problem: {proof_msg}.", "LLM/Study/Local LLM First Benchmark Row Builder", row_id)

        required_fields = ["model_id", "runtime", "route", "hardware_boundary", "prompt_id", "cold_or_warm", "sampler"]
        missing = [field for field in required_fields if not text(row.get(field))]
        if missing:
            add_issue(issues, "hold", "run_identity", "identity", "Benchmark row missing: " + ", ".join(missing) + ".", "LLM/Study/Local LLM Inference Benchmark Log", row_id)

        prompt_tokens = num_value(metric(row, "prompt_tokens", "input_tokens", "context_tokens"))
        output_tokens = num_value(metric(row, "output_tokens", "completion_tokens", "generated_tokens"))
        output_cap = num_value(metric(row, "output_cap", "max_tokens", "num_predict"))
        if prompt_tokens is None:
            add_issue(issues, "hold", "prompt_token_accounting", "tokens", "Benchmark row has no prompt/input token count or tokenizer proof.", "LLM/Study/Local LLM Context Window and Token Budgeting Runner", row_id)
        if output_tokens is None and output_cap is None:
            add_issue(issues, "hold", "prompt_token_accounting", "tokens", "Benchmark row has neither output tokens nor output cap.", "LLM/Study/Local LLM First Benchmark Row Builder", row_id)
        if any(value is not None and value < 0 for value in [prompt_tokens, output_tokens, output_cap]):
            add_issue(issues, "fail", "prompt_token_accounting", "tokens", "Token counts and caps cannot be negative.", "LLM/Study/Local LLM First Benchmark Row Builder", row_id)

        timing_names = ["ttft_ms", "time_to_first_token_ms", "tpot_ms", "itl_ms", "tokens_per_second", "output_tokens_per_second", "total_latency_ms", "p50_latency_ms", "p95_latency_ms", "request_throughput_per_s"]
        timing_values = [num_value(metric(row, name)) for name in timing_names if metric(row, name) is not None]
        if not timing_values:
            add_issue(issues, "hold", "timing_metrics", "latency", "Benchmark row has no TTFT, TPOT/ITL, total latency, throughput, or p50/p95 timing.", "LLM/Study/Local LLM Inference Metrics Field Guide", row_id)
        if any(value is not None and value < 0 for value in timing_values):
            add_issue(issues, "fail", "timing_metrics", "latency", "Timing metrics cannot be negative.", "LLM/Study/Local LLM Inference Metrics Field Guide", row_id)

        total_latency = num_value(metric(row, "total_latency_ms"))
        ttft = num_value(metric(row, "ttft_ms", "time_to_first_token_ms"))
        if total_latency is not None and ttft is not None and ttft > total_latency:
            add_issue(issues, "fail", "timing_metrics", "latency", "TTFT is greater than total latency.", "LLM/Study/Local LLM Inference Metrics Field Guide", row_id)
        if output_tokens is not None and output_tokens > 0 and total_latency is not None and total_latency <= 0:
            add_issue(issues, "fail", "timing_metrics", "latency", "Output tokens require positive total latency.", "LLM/Study/Local LLM First Benchmark Row Builder", row_id)

        memory_names = ["peak_vram_gb", "peak_ram_gb", "peak_vram_mb", "peak_ram_mb", "context_margin_tokens", "active_sequences", "queue_depth", "error_count"]
        if not any(metric(row, name) is not None for name in memory_names) and not text(row.get("not_exposed_reason")):
            add_issue(issues, "hold", "memory_context_metrics", "capacity", "Benchmark row has no memory/context/queue signal or not-exposed reason.", "LLM/Study/Local LLM Hardware Sizing Runner", row_id)

        changed = list_value(row.get("changed_variables"))
        decision_scope = norm(manifest.get("decision_scope"))
        if ("compare" in decision_scope or "beats" in decision_scope or "choose" in decision_scope) and len(changed) != 1:
            add_issue(issues, "hold", "fixed_settings", "confounders", "Comparison decisions should change exactly one variable or be labeled exploratory.", "LLM/Study/Local LLM Runtime Comparison Lab", row_id)
        if not changed and not text(row.get("single_run_scope")):
            add_issue(issues, "hold", "fixed_settings", "confounders", "Benchmark row should name changed_variables or single_run_scope.", "LLM/Study/Local LLM Inference Benchmark Log", row_id)

        quality = status_value(row.get("quality_result") or metric(row, "quality_result", "quality_status"))
        decision = norm(row.get("decision"))
        if quality == "fail" and decision in {"keep", "deploy", "accept", "pass"}:
            add_issue(issues, "fail", "quality_boundary", "quality", "Benchmark row keeps a setup whose quality_result is fail.", "LLM/Study/Local LLM Quality Evaluation Runner", row_id)
        if quality == "hold" and not text(row.get("quality_scope")) and not text(row.get("waiver_reason")):
            add_issue(issues, "hold", "quality_boundary", "quality", "Benchmark row needs quality_result, quality_scope, or waiver reason.", "LLM/Study/Local LLM Quality Evaluation Runner", row_id)

        if not text(row.get("mechanism_owner")):
            add_issue(issues, "hold", "interpretation_next_action", "decision", "Benchmark row has no mechanism_owner.", "LLM/Study/Local LLM Inference Metrics Field Guide", row_id)
        if not text(row.get("next_action")):
            add_issue(issues, "hold", "interpretation_next_action", "decision", "Benchmark row has no next_action.", "LLM/Study/Local LLM Result Synthesis Runner", row_id)

    return normalized


def evaluate(manifest_path: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    issues: list[dict[str, Any]] = []
    vault_text = text(manifest.get("vault_root"))
    vault_root = Path(vault_text).expanduser().resolve() if vault_text else None
    if vault_root and not vault_root.exists():
        add_issue(issues, "hold", "manifest", "vault", f"vault_root does not exist: {vault_root}", "LLM/Study/LLM Study Index")

    if not text(manifest.get("workload")):
        add_issue(issues, "hold", "workload_contract", "workload", "Manifest has no workload.", "LLM/Study/Local LLM Inference Benchmark Log")
    if not any(manifest.get(name) not in (None, "") for name in ["latency_target_ms", "throughput_target", "batch_window", "decision_scope"]):
        add_issue(issues, "hold", "workload_contract", "workload", "Manifest has no latency target, throughput target, batch window, or decision scope.", "LLM/Study/Local LLM Inference Benchmark Log")

    benchmarks = benchmark_checks(manifest, issues, vault_root, manifest_path.parent)
    evidence_rows = manifest.get("evidence") or []
    if not isinstance(evidence_rows, list):
        add_issue(issues, "fail", "evidence", "manifest", "evidence must be a list.", "LLM/Study/Local LLM Inference Benchmark Log")
        evidence_rows = []

    required_kinds = list_value(manifest.get("required_kinds")) or DEFAULT_REQUIRED_KINDS
    present_required: set[str] = set()
    status_by_kind: dict[str, str] = {}
    for row in evidence_rows:
        if not isinstance(row, dict):
            add_issue(issues, "hold", "evidence", "manifest", "Non-object evidence row ignored.", "LLM/Study/Local LLM Inference Benchmark Log")
            continue
        kind = text(row.get("kind") or "uncategorized")
        if bool_value(row.get("required"), True):
            present_required.add(kind)
        evidence_row_checks(row, issues, vault_root, manifest_path.parent)
        current = status_value(row.get("status"))
        previous = status_by_kind.get(kind, "pass")
        status_by_kind[kind] = current if STATUS_RANK[current] > STATUS_RANK[previous] else previous

    # Benchmark rows themselves can satisfy the common evidence families.
    if benchmarks:
        present_required.update({
            "run_identity",
            "source_artifacts",
            "prompt_token_accounting",
            "timing_metrics",
            "memory_context_metrics",
            "fixed_settings",
            "quality_boundary",
            "interpretation_next_action",
        })
        for kind in present_required:
            status_by_kind.setdefault(kind, "pass")

    for kind in required_kinds:
        if kind not in present_required:
            owner, hint, route = KIND_HINTS.get(kind, ("evidence", "Attach evidence.", "LLM/Study/LLM Study Index"))
            add_issue(issues, "hold", kind, owner, f"Missing required evidence kind: {kind}. {hint}", route)

    final_status = "pass"
    if any(issue["severity"] == "fail" for issue in issues):
        final_status = "fail"
    elif issues:
        final_status = "hold"

    if final_status == "pass":
        decision = "benchmark_evidence_ready"
        next_route = "LLM/Study/Local LLM Result Synthesis Runner"
    elif final_status == "fail":
        decision = "benchmark_evidence_blocked"
        next_route = first_route(issues, "LLM/Study/Local LLM Inference Benchmark Log")
    else:
        decision = "benchmark_evidence_incomplete"
        next_route = first_route(issues, "LLM/Study/Local LLM Inference Benchmark Log")

    return {
        "run_id": text(manifest.get("run_id") or manifest_path.stem),
        "generated_at": utc_iso(),
        "status": final_status,
        "decision": decision,
        "next_route": next_route,
        "workload": text(manifest.get("workload")),
        "decision_scope": text(manifest.get("decision_scope")),
        "selected_benchmark": text(manifest.get("selected_benchmark")),
        "benchmark_count": len(benchmarks),
        "required_kinds": required_kinds,
        "present_required_kinds": sorted(present_required),
        "missing_required_kinds": [kind for kind in required_kinds if kind not in present_required],
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
        f"# Local LLM Benchmark Evidence Audit - {result['run_id']}",
        "",
        f"- Generated: {result['generated_at']}",
        f"- Status: `{result['status']}`",
        f"- Decision: `{result['decision']}`",
        f"- Selected benchmark: `{result.get('selected_benchmark') or 'missing'}`",
        f"- Next route: {LINK_OPEN}{result['next_route']}{LINK_CLOSE}",
        "",
        "## Coverage",
        "",
        "| Required kind | Present | Status |",
        "|---|---:|---|",
    ]
    present = set(result.get("present_required_kinds") or [])
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
        "A `pass` means the benchmark evidence is ready for result synthesis. A `hold` means the row may still be useful but is missing proof, normalization, confounder control, quality boundary, or interpretation. A `fail` means a critical contradiction or invalid metric blocks reuse.",
    ])
    return "\n".join(lines) + "\n"


def write_outputs(manifest_path: Path, manifest: dict[str, Any], result: dict[str, Any]) -> dict[str, str]:
    run_root = Path(text(manifest.get("run_root")) or manifest_path.parent).expanduser()
    if not run_root.is_absolute():
        run_root = manifest_path.parent / run_root
    run_root.mkdir(parents=True, exist_ok=True)
    base = run_root / f"{slug(result['run_id'])}-benchmark-evidence-audit"
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
            "event": "local_llm_benchmark_evidence_audit",
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
| complete warm single-run row with model/runtime/route, proof, prompt/output tokens, TTFT, TPOT, total latency, memory, quality pass, one next action | `pass/benchmark_evidence_ready` | benchmark can feed result synthesis |
| row missing prompt tokens and output cap | `hold/benchmark_evidence_incomplete` | latency is not normalized by input/output size |
| quality fails while decision says keep | `fail/benchmark_evidence_blocked` | performance cannot override failed workload quality |
| TTFT greater than total latency | `fail/benchmark_evidence_blocked` | timing fields contradict each other |
| comparison decision with two changed variables | `hold/benchmark_evidence_incomplete` | cannot assign the difference to one mechanism |
| benchmark row proof path missing | `hold/benchmark_evidence_incomplete` | numbers cannot be reviewed |

## Completion Gate

This runner is complete when:

- [ ] workload, decision scope, and latency/throughput target are recorded
- [ ] each selected benchmark row names model, artifact or model id, runtime, route, hardware boundary, prompt id, sampler, cold/warm state, and changed variable
- [ ] proof paths resolve for raw response, client log, streaming log, benchmark JSON, metric export, or benchmark note
- [ ] prompt tokens, output cap or output tokens, timing metrics, and memory/context signals exist or have explicit non-exposure notes
- [ ] quality is linked or the row is explicitly scoped to route/performance only
- [ ] the interpretation names mechanism owner, next controlled action, and retest trigger
- [ ] the output routes to [[LLM/Study/Local LLM Result Synthesis Runner|Local LLM Result Synthesis Runner]] or a remediation note

## References

Internal:

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM First Benchmark Row Builder]]
- [[LLM/Study/Local LLM First Benchmark Row Proof - 2026-06-16]]
- [[LLM/Study/Local LLM First Streaming Timing Runner]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner]]
- [[LLM/Study/Local LLM Scheduler Evidence Audit Runner]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Evidence Runner]]
- [[LLM/Study/Local LLM Quality Evaluation Runner]]
- [[LLM/Study/Local LLM Runtime Comparison Runner]]
- [[LLM/Study/Local LLM Result Synthesis Runner]]
- [[LLM/Study/LLM Deployment Readiness Audit Runner]]
- [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]

Current external docs checked 2026-06-16:

- [Ollama usage metrics](https://docs.ollama.com/api/usage)
- [vLLM Benchmark CLI](https://docs.vllm.ai/en/latest/benchmarking/cli/)
- [SGLang benchmark and profiling](https://github.com/sgl-project/sglang/blob/main/docs/developer_guide/benchmark_and_profiling.md)
- [NVIDIA NIM LLM benchmarking metrics](https://docs.nvidia.com/nim/benchmarking/llm/latest/metrics.html)
- [NVIDIA GenAI-Perf](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html)
