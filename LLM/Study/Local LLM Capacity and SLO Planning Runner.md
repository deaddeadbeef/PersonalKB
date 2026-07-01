---
tags: [study, llm, inference, local-llm, capacity, slo, throughput, latency, queueing, operations, evidence, audit, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice, deep-dive]
last-verified: 2026-06-16
---

# Local LLM Capacity and SLO Planning Runner

> **One-line summary** Audit whether saved local LLM evidence supports one workload SLO: latency target, throughput target, concurrency limit, error budget, resource headroom, admission policy, security boundary, owner, and retest trigger.

Use this after [[LLM/Study/Local LLM Benchmark Evidence Audit Runner|Local LLM Benchmark Evidence Audit Runner]], [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner|Local LLM Concurrency and Batch Throughput Runner]], [[LLM/Study/Local LLM Observability and Operations Runner|Local LLM Observability and Operations Runner]], and [[LLM/Study/Local LLM Runtime Comparison Runner|Local LLM Runtime Comparison Runner]] have produced saved evidence. Use [[LLM/Study/Local LLM Queueing and Tail Latency Field Guide|Local LLM Queueing and Tail Latency Field Guide]] first when the workload still lacks an arrival-rate, utilization, p95/p99, queueing, or admission-policy explanation. Use this before [[LLM/Study/Local LLM Result Synthesis Runner|Local LLM Result Synthesis Runner]], [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]], or [[LLM/Study/LLM Deployment Readiness Audit Runner|LLM Deployment Readiness Audit Runner]] whenever a local endpoint is expected to carry more than a one-off prompt.

This runner does not start a server, load a model, scrape metrics, or generate traffic. It audits a saved capacity manifest. That keeps the academic point clear: capacity is not a single tokens-per-second number. It is a workload contract tied to queueing, prefill, decode, KV-cache pressure, batching policy, failure budget, privacy boundary, and an operator who will retest when the workload or runtime changes.

## What This Proves

| Evidence family | Checks | Why it matters |
|---|---|---|
| Workload SLO contract | workload, user class, data class, latency target, throughput target, error budget | prevents vague "fast enough" claims |
| Candidate serving path | selected runtime/path, model id, endpoint, route, loopback or network boundary | binds capacity to the exact service being planned |
| Demand model | expected requests, peak window, prompt/output token shape, active users, batch window | separates one-user testing from shared or batch service planning |
| Measured capacity | baseline, concurrency ladder, p95/p99 latency, TTFT/TPOT where available, throughput, errors, saturation point | makes the SLO decision evidence-backed |
| Resource headroom | RAM, VRAM, KV/cache, CPU/GPU, disk, thermal/power if relevant | catches capacity that only passes by exhausting the machine |
| Admission and backpressure | max concurrency, queue limit, timeout, retry, overload behavior, batch policy | prevents hidden infinite queues and user-visible stalls |
| Quality and privacy gates | quality pass, safety/security proof, endpoint exposure, log/export boundary | prevents a fast service from being unacceptable |
| Operations and review | metrics/logs, owner, cost, retest trigger, rejected path | turns a benchmark into a maintainable service decision |

Academic bridge: service-level planning turns transformer inference mechanics into systems constraints. TTFT is dominated by prompt processing, queueing, and prefill. TPOT and decode throughput shape response streaming. KV cache and attention state constrain active sequences. Continuous batching and slots can raise throughput while harming tail latency. A defensible local SLO therefore needs p95 or p99 latency, throughput, error budget, resource headroom, and admission policy together.

## References

These source notes were rechecked on 2026-06-16:

- [vLLM production metrics](https://docs.vllm.ai/en/v0.14.0/usage/metrics/) expose `/metrics` on the OpenAI-compatible API server and include request queue time, prefill time, time per output token, and time to first token histograms.
- [vLLM metrics design](https://docs.vllm.ai/en/stable/design/metrics/) describes queue, prefill, inter-token, TTFT, decode, inference, end-to-end latency, and KV-cache residency collection.
- [SGLang production metrics](https://docs.sglang.io/docs/references/production_metrics) are enabled with `--enable-metrics` and expose Prometheus counters and histograms such as prompt tokens, generation tokens, token usage, cache hit rate, and TTFT.
- [llama.cpp server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md) documents parallel server slots, continuous batching, Prometheus-compatible metrics, `/slots`, request processing, deferred request, and throughput counters.
- [NVIDIA NIM LLM benchmarking metrics](https://docs.nvidia.com/nim/benchmarking/llm/latest/metrics.html) defines TTFT, end-to-end request latency, and inter-token latency, including queueing/batching and network latency considerations.
- [NVIDIA GenAI-Perf](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/genai-perf/README.html) profiles LLM endpoints under specified concurrency or request rate and reports latency and throughput metrics, while noting that GenAI-Perf is being phased out.
- [Ollama usage metrics](https://docs.ollama.com/api/usage) document response fields such as total duration, model load duration, prompt token count/duration, output token count, and output generation duration.
- [LM Studio local server docs](https://lmstudio.ai/docs/developer/core/server) document serving local LLMs from localhost or the network through REST and compatibility endpoints.

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "capacity-slo-001",
  "run_root": "D:/llm-runs/capacity-slo",
  "vault_root": "D:/Vaults/PersonalKB",
  "workload": "private local research assistant",
  "selected_runtime": "llama.cpp-q4",
  "selected_path": "local_gpu",
  "slo": {
    "latency_target_ms": 6000,
    "latency_percentile": "p95",
    "ttft_target_ms": 1200,
    "throughput_target_rps": 0.25,
    "target_concurrency": 2,
    "error_budget_percent": 1.0,
    "quality_gate": "quality runner pass",
    "data_boundary": "personal loopback only"
  },
  "rows": [
    {
      "id": "contract",
      "kind": "workload_slo_contract",
      "status": "pass",
      "workload": "private local research assistant",
      "user_class": "single owner",
      "data_class": "personal notes",
      "latency_target_ms": 6000,
      "throughput_target_rps": 0.25,
      "target_concurrency": 2,
      "error_budget_percent": 1.0,
      "proof": "D:/llm-runs/capacity-slo/workload.md"
    },
    {
      "id": "serving-path",
      "kind": "candidate_serving_path",
      "status": "pass",
      "selected": true,
      "runtime": "llama.cpp",
      "model_id": "example-model-q4",
      "route": "openai-compatible",
      "base_url": "http://127.0.0.1:8080/v1",
      "endpoint_exposure": "loopback",
      "proof": "D:/llm-runs/capacity-slo/api-contract.json"
    },
    {
      "id": "demand",
      "kind": "demand_model",
      "status": "pass",
      "expected_rps": 0.12,
      "peak_rps": 0.25,
      "active_users": 2,
      "prompt_tokens_p95": 1800,
      "output_tokens_p95": 300,
      "peak_window": "evening study block",
      "proof": "D:/llm-runs/capacity-slo/demand.md"
    },
    {
      "id": "capacity",
      "kind": "measured_capacity",
      "status": "pass",
      "selected": true,
      "concurrency": 2,
      "p95_total_ms": 4300,
      "p99_total_ms": 5200,
      "p95_ttft_ms": 950,
      "throughput_rps": 0.31,
      "error_rate_percent": 0,
      "saturation_point": "C4 crosses latency target",
      "benchmark_audit": "D:/llm-runs/capacity-slo/benchmark-audit.json",
      "concurrency_proof": "D:/llm-runs/capacity-slo/concurrency.json"
    },
    {
      "id": "headroom",
      "kind": "resource_headroom",
      "status": "pass",
      "peak_vram_gb": 8.4,
      "vram_budget_gb": 12,
      "peak_ram_gb": 18,
      "ram_budget_gb": 64,
      "kv_cache_budget": "fits C2 with 20 percent reserve",
      "proof": "D:/llm-runs/capacity-slo/observability.md"
    },
    {
      "id": "admission",
      "kind": "admission_backpressure",
      "status": "pass",
      "max_concurrency": 2,
      "queue_limit": 4,
      "timeout_ms": 20000,
      "overload_behavior": "return 503 after queue limit",
      "batch_policy": "no offline batch on interactive endpoint",
      "proof": "D:/llm-runs/capacity-slo/admission.md"
    },
    {
      "id": "quality",
      "kind": "quality_boundary",
      "status": "pass",
      "quality_status": "pass",
      "quality_proof": "D:/llm-runs/capacity-slo/quality.json"
    },
    {
      "id": "security",
      "kind": "security_boundary",
      "status": "pass",
      "endpoint_exposure": "loopback",
      "data_boundary": "personal notes stay local",
      "log_export_boundary": "no prompt export",
      "security_proof": "D:/llm-runs/capacity-slo/security.md"
    },
    {
      "id": "ops",
      "kind": "observability_operations",
      "status": "pass",
      "metrics_proof": "D:/llm-runs/capacity-slo/metrics.txt",
      "log_proof": "D:/llm-runs/capacity-slo/log-tail.md",
      "owner": "local",
      "restart_procedure": "documented"
    },
    {
      "id": "review",
      "kind": "cost_owner_review",
      "status": "pass",
      "cost_model": "owned GPU, electricity only",
      "owner": "local",
      "retest_trigger": "new model, new runtime, LAN exposure, C2 p95 regression, or workload token growth"
    }
  ]
}
```

`proof` may be an absolute path, a vault-relative path, an Obsidian note path, or a URL. If a row is deliberately out of scope, set `required: false`, `status: "waived"`, and add `waiver_reason`. A single-user local scratch run can waive `admission_backpressure` only when `target_concurrency <= 1`, `throughput_target_rps` is empty, and the row states why no shared queue exists.

## Required Evidence Kinds

By default, the runner expects:

| Kind | Required signal |
|---|---|
| `workload_slo_contract` | workload, user/data class, latency target, throughput or single-user scope, target concurrency, error budget |
| `candidate_serving_path` | selected path/runtime, model id, route, endpoint boundary |
| `demand_model` | expected or peak request rate, active users or batch window, prompt/output token shape |
| `measured_capacity` | benchmark/concurrency proof, p95 or p99 latency, throughput, error rate, saturation or highest passing level |
| `resource_headroom` | RAM/VRAM/KV/cache/resource proof and budget or reserve |
| `admission_backpressure` | max concurrency, queue limit, timeout, overload behavior, or valid single-user waiver |
| `quality_boundary` | quality runner result or explicit quality gate with pass/hold/fail status |
| `security_boundary` | endpoint exposure, data boundary, log/export boundary, security proof if exposed beyond loopback |
| `observability_operations` | metrics/log/resource proof, owner, restart or support route |
| `cost_owner_review` | cost model, owner, retest trigger |

## Standard-Library Runner

Save this as `local_llm_capacity_slo_planning_runner.py` inside the run folder. It uses only Python's standard library.

```python
from __future__ import annotations

import csv
import datetime as dt
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any


DEFAULT_REQUIRED_KINDS = [
    "workload_slo_contract",
    "candidate_serving_path",
    "demand_model",
    "measured_capacity",
    "resource_headroom",
    "admission_backpressure",
    "quality_boundary",
    "security_boundary",
    "observability_operations",
    "cost_owner_review",
]

FAIL_STATUSES = {"fail", "failed", "error", "blocked"}
HOLD_STATUSES = {"hold", "pending", "incomplete", "unknown", "missing"}
PASS_STATUSES = {"pass", "passed", "ok", "ready", "waived"}
EXPOSED_BOUNDARIES = {"lan", "network", "public", "internet", "tunnel", "remote", "shared", "0.0.0.0"}


def text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (list, tuple, set)):
        return " ".join(text(item) for item in value)
    if isinstance(value, dict):
        return " ".join(f"{key} {text(item)}" for key, item in value.items())
    return str(value).strip()


def lower(value: Any) -> str:
    return text(value).lower()


def has_text(row: dict[str, Any], *keys: str) -> bool:
    return any(bool(text(row.get(key))) for key in keys)


def number(value: Any) -> float | None:
    if value is None or value == "":
        return None
    if isinstance(value, bool):
        return float(value)
    if isinstance(value, (int, float)):
        return float(value)
    raw = str(value).strip().replace(",", "")
    for suffix in ("ms", "s", "rps", "req/s", "%", "gb", "mb"):
        raw = raw.lower().replace(suffix, "")
    try:
        return float(raw.strip())
    except ValueError:
        return None


def pick_number(row: dict[str, Any], *keys: str) -> float | None:
    for key in keys:
        value = number(row.get(key))
        if value is not None:
            return value
    return None


def row_status(row: dict[str, Any]) -> str:
    return lower(row.get("status") or row.get("decision") or "unknown")


def is_selected(row: dict[str, Any], manifest: dict[str, Any]) -> bool:
    if row.get("selected") is True:
        return True
    selected_runtime = lower(manifest.get("selected_runtime") or manifest.get("selected_path"))
    candidates = [
        row.get("runtime_id"),
        row.get("runtime"),
        row.get("selected_runtime"),
        row.get("path"),
        row.get("selected_path"),
        row.get("id"),
    ]
    return bool(selected_runtime and any(lower(candidate) == selected_runtime for candidate in candidates))


def exposure_value(row: dict[str, Any], manifest: dict[str, Any]) -> str:
    candidates = [
        row.get("endpoint_exposure"),
        row.get("exposure"),
        row.get("network_boundary"),
        row.get("boundary"),
        row.get("base_url"),
        manifest.get("endpoint_exposure"),
        manifest.get("boundary"),
    ]
    return lower(" ".join(text(item) for item in candidates if item is not None))


def is_exposed(row: dict[str, Any], manifest: dict[str, Any]) -> bool:
    value = exposure_value(row, manifest)
    if not value:
        return False
    if "127.0.0.1" in value or "localhost" in value or "loopback" in value:
        return False
    return any(token in value for token in EXPOSED_BOUNDARIES)


def finding(level: str, owner: str, message: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "owner": owner,
        "finding": message,
        "evidence": evidence,
        "action": action,
    }


def group_rows(rows: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        kind = lower(row.get("kind"))
        if kind:
            grouped.setdefault(kind, []).append(row)
    return grouped


def manifest_slo(manifest: dict[str, Any]) -> dict[str, Any]:
    slo = manifest.get("slo")
    return slo if isinstance(slo, dict) else {}


def get_target(manifest: dict[str, Any], rows: list[dict[str, Any]], *keys: str) -> float | None:
    slo = manifest_slo(manifest)
    for key in keys:
        value = number(slo.get(key))
        if value is not None:
            return value
    for row in rows:
        if lower(row.get("kind")) == "workload_slo_contract":
            for key in keys:
                value = number(row.get(key))
                if value is not None:
                    return value
    for key in keys:
        value = number(manifest.get(key))
        if value is not None:
            return value
    return None


def target_concurrency(manifest: dict[str, Any], rows: list[dict[str, Any]]) -> float | None:
    return get_target(manifest, rows, "target_concurrency", "max_concurrency", "active_users", "users")


def throughput_target(manifest: dict[str, Any], rows: list[dict[str, Any]]) -> float | None:
    return get_target(manifest, rows, "throughput_target_rps", "target_rps", "requests_per_second", "peak_rps")


def error_budget(manifest: dict[str, Any], rows: list[dict[str, Any]]) -> float | None:
    return get_target(manifest, rows, "error_budget_percent", "max_error_rate_percent", "error_rate_budget_percent")


def latency_target(manifest: dict[str, Any], rows: list[dict[str, Any]]) -> float | None:
    return get_target(manifest, rows, "latency_target_ms", "p95_total_target_ms", "target_p95_total_ms", "e2e_latency_target_ms")


def ttft_target(manifest: dict[str, Any], rows: list[dict[str, Any]]) -> float | None:
    return get_target(manifest, rows, "ttft_target_ms", "target_ttft_ms", "p95_ttft_target_ms")


def row_proof(row: dict[str, Any]) -> bool:
    return has_text(
        row,
        "proof",
        "evidence",
        "benchmark_audit",
        "concurrency_proof",
        "quality_proof",
        "security_proof",
        "metrics_proof",
        "observability_proof",
        "log_proof",
        "source",
    )


def validate_required(grouped: dict[str, list[dict[str, Any]]], required: list[str]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for kind in required:
        rows = grouped.get(kind, [])
        if not rows:
            findings.append(finding("hold", kind, "Required evidence kind is missing.", kind, "Add a manifest row or an explicit waiver row."))
            continue
        for row in rows:
            status = row_status(row)
            if status in FAIL_STATUSES:
                findings.append(finding("fail", kind, "Evidence row is marked failed.", text(row.get("id") or kind), "Fix the failing row before capacity can be accepted."))
            elif status in HOLD_STATUSES or status == "unknown":
                findings.append(finding("hold", kind, "Evidence row is not pass-ready.", text(row.get("id") or kind), "Complete the row or record a valid waiver."))
            elif status not in PASS_STATUSES:
                findings.append(finding("hold", kind, "Evidence row has an unrecognized status.", status, "Use pass, hold, fail, or waived."))
    return findings


def validate_workload(manifest: dict[str, Any], rows: list[dict[str, Any]]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    contract_rows = [row for row in rows if lower(row.get("kind")) == "workload_slo_contract"]
    workload = text(manifest.get("workload"))
    for row in contract_rows:
        if not workload and not has_text(row, "workload"):
            findings.append(finding("hold", "workload", "Workload SLO contract has no named workload.", text(row.get("id")), "Name the task or product workflow."))
        if not has_text(row, "user_class", "user", "users", "audience", "owner"):
            findings.append(finding("hold", "workload", "Workload SLO contract has no user class.", text(row.get("id")), "State whether this is single owner, household, team, public, or batch."))
        if not has_text(row, "data_class", "data_boundary", "privacy_boundary", "data_sensitivity"):
            findings.append(finding("hold", "workload", "Workload SLO contract has no data/privacy class.", text(row.get("id")), "Classify public, personal, private, regulated, secret, or mixed data."))
    if latency_target(manifest, rows) is None and ttft_target(manifest, rows) is None:
        findings.append(finding("hold", "slo", "No latency or TTFT target is recorded.", "slo", "Add p95/p99 total latency target or TTFT target in milliseconds."))
    if throughput_target(manifest, rows) is None and (target_concurrency(manifest, rows) or 0) <= 1:
        if not any(has_text(row, "single_user_reason", "scratch_reason", "batch_window") for row in contract_rows):
            findings.append(finding("hold", "slo", "No throughput target or single-user waiver is recorded.", "slo", "Add throughput target, batch window, or explicit single-user reason."))
    if error_budget(manifest, rows) is None:
        findings.append(finding("hold", "slo", "No error budget is recorded.", "slo", "Add max allowed error rate percentage or failure budget."))
    return findings


def validate_serving_path(manifest: dict[str, Any], rows: list[dict[str, Any]]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    path_rows = [row for row in rows if lower(row.get("kind")) == "candidate_serving_path"]
    selected_rows = [row for row in path_rows if is_selected(row, manifest)]
    if not selected_rows and path_rows:
        findings.append(finding("hold", "serving path", "No candidate serving path is marked selected.", "candidate_serving_path", "Mark the selected runtime/path or set selected_runtime."))
    for row in selected_rows or path_rows:
        if not has_text(row, "runtime", "provider", "path", "selected_path"):
            findings.append(finding("hold", "serving path", "Serving path has no runtime or path.", text(row.get("id")), "Name Ollama, LM Studio, llama.cpp, vLLM, SGLang, hosted API, or batch path."))
        if not has_text(row, "model_id", "served_model", "artifact_id"):
            findings.append(finding("hold", "serving path", "Serving path has no model identity.", text(row.get("id")), "Record served model id, artifact, or revision."))
        if not has_text(row, "route", "base_url", "endpoint"):
            findings.append(finding("hold", "serving path", "Serving path has no route or endpoint.", text(row.get("id")), "Record OpenAI-compatible, native, batch, or UI route and base URL if applicable."))
        if not has_text(row, "endpoint_exposure", "network_boundary", "boundary", "base_url"):
            findings.append(finding("hold", "serving path", "Serving path has no endpoint exposure boundary.", text(row.get("id")), "Record loopback, LAN, tunnel, public, remote, or provider boundary."))
    return findings


def validate_demand(rows: list[dict[str, Any]]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for row in [item for item in rows if lower(item.get("kind")) == "demand_model"]:
        if not any(pick_number(row, key) is not None for key in ("expected_rps", "peak_rps", "requests_per_minute", "requests_per_hour", "batch_jobs")):
            findings.append(finding("hold", "demand", "Demand model has no request-rate or batch-volume estimate.", text(row.get("id")), "Add expected/peak RPS, requests per minute, requests per hour, or batch jobs."))
        if not any(pick_number(row, key) is not None for key in ("active_users", "target_concurrency", "concurrent_users", "batch_size")) and not has_text(row, "single_user_reason", "batch_window"):
            findings.append(finding("hold", "demand", "Demand model has no user/concurrency or batch shape.", text(row.get("id")), "Add active users, target concurrency, batch size, batch window, or single-user reason."))
        if not any(pick_number(row, key) is not None for key in ("prompt_tokens_p95", "input_tokens_p95", "context_tokens", "output_tokens_p95", "max_output_tokens")):
            findings.append(finding("hold", "demand", "Demand model has no prompt/output token shape.", text(row.get("id")), "Add prompt p95, output p95, context target, or output cap."))
    return findings


def validate_capacity(manifest: dict[str, Any], rows: list[dict[str, Any]]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    target_ms = latency_target(manifest, rows)
    target_ttft = ttft_target(manifest, rows)
    target_rps = throughput_target(manifest, rows)
    budget = error_budget(manifest, rows)
    capacity_rows = [row for row in rows if lower(row.get("kind")) == "measured_capacity"]
    selected_capacity = [row for row in capacity_rows if is_selected(row, manifest)] or capacity_rows
    for row in selected_capacity:
        if not row_proof(row):
            findings.append(finding("hold", "capacity", "Measured-capacity row has no proof link.", text(row.get("id")), "Link benchmark audit, concurrency runner, result JSON, or saved evidence."))
        p95_total = pick_number(row, "p95_total_ms", "p95_latency_ms", "p95_e2e_ms", "p95_request_ms")
        p99_total = pick_number(row, "p99_total_ms", "p99_latency_ms", "p99_e2e_ms", "p99_request_ms")
        p95_ttft = pick_number(row, "p95_ttft_ms", "ttft_p95_ms", "time_to_first_token_p95_ms")
        throughput = pick_number(row, "throughput_rps", "request_throughput_rps", "req_per_second", "requests_per_second")
        error_rate = pick_number(row, "error_rate_percent", "errors_percent", "failure_rate_percent")
        if p95_total is None and p99_total is None and p95_ttft is None:
            findings.append(finding("hold", "capacity", "Measured-capacity row has no tail-latency metric.", text(row.get("id")), "Add p95/p99 end-to-end latency or p95 TTFT."))
        if throughput is None:
            findings.append(finding("hold", "capacity", "Measured-capacity row has no throughput metric.", text(row.get("id")), "Add throughput RPS or request throughput."))
        if error_rate is None:
            findings.append(finding("hold", "capacity", "Measured-capacity row has no error-rate metric.", text(row.get("id")), "Add error rate, timeout rate, or failure count converted to percentage."))
        if not has_text(row, "saturation_point", "highest_passing_level", "capacity_decision", "decision"):
            findings.append(finding("hold", "capacity", "Measured-capacity row has no saturation or capacity decision.", text(row.get("id")), "Record first failing level, highest passing level, or explicit capacity decision."))
        if target_ms is not None:
            compared = p95_total if p95_total is not None else p99_total
            if compared is not None and compared > target_ms:
                findings.append(finding("fail", "capacity", "Selected capacity latency exceeds the SLO target.", f"{compared:g}ms > {target_ms:g}ms", "Lower concurrency, tune runtime, choose another model/path, or change the SLO."))
        if target_ttft is not None and p95_ttft is not None and p95_ttft > target_ttft:
            findings.append(finding("fail", "capacity", "Selected TTFT exceeds the SLO target.", f"{p95_ttft:g}ms > {target_ttft:g}ms", "Reduce prompt/context, improve prefill, change runtime, or change the SLO."))
        if target_rps is not None and throughput is not None and throughput < target_rps:
            findings.append(finding("fail", "capacity", "Selected throughput is below target.", f"{throughput:g} < {target_rps:g} rps", "Reduce demand, increase capacity, batch differently, or reject this path."))
        if budget is not None and error_rate is not None and error_rate > budget:
            findings.append(finding("fail", "capacity", "Observed error rate exceeds the error budget.", f"{error_rate:g}% > {budget:g}%", "Fix overload/timeouts/errors before accepting the service level."))
    return findings


def validate_headroom(rows: list[dict[str, Any]]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for row in [item for item in rows if lower(item.get("kind")) == "resource_headroom"]:
        if not any(has_text(row, key) or pick_number(row, key) is not None for key in ("peak_vram_gb", "vram_budget_gb", "peak_ram_gb", "ram_budget_gb", "kv_cache_budget", "cache_headroom", "resource_proof", "gpu_proof")):
            findings.append(finding("hold", "resources", "Resource-headroom row has no RAM, VRAM, KV/cache, or resource proof.", text(row.get("id")), "Add local resource metrics and a budget/reserve statement."))
        if not row_proof(row):
            findings.append(finding("hold", "resources", "Resource-headroom row has no proof link.", text(row.get("id")), "Link observability, nvidia-smi, OS resource snapshot, or cache sizing proof."))
    return findings


def validate_admission(manifest: dict[str, Any], rows: list[dict[str, Any]]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    target_c = target_concurrency(manifest, rows)
    target_rps = throughput_target(manifest, rows)
    shared_need = (target_c is not None and target_c > 1) or (target_rps is not None and target_rps > 0)
    admission_rows = [row for row in rows if lower(row.get("kind")) == "admission_backpressure"]
    for row in admission_rows:
        has_waiver = has_text(row, "single_user_reason", "waiver_reason", "no_queue_reason")
        has_policy = has_text(row, "max_concurrency", "queue_limit", "timeout_ms", "overload_behavior", "batch_policy", "admission_policy")
        if shared_need and has_waiver and not has_policy:
            findings.append(finding("hold", "admission", "Shared-use SLO cannot rely only on a single-user waiver.", text(row.get("id")), "Add max concurrency, queue limit, timeout, and overload behavior."))
        if not has_policy and not has_waiver:
            findings.append(finding("hold", "admission", "Admission row has no backpressure policy or waiver.", text(row.get("id")), "Add max concurrency, queue limit, timeout, overload behavior, batch policy, or single-user waiver."))
        if shared_need:
            for key, label in (("max_concurrency", "max concurrency"), ("queue_limit", "queue limit"), ("timeout_ms", "timeout"), ("overload_behavior", "overload behavior")):
                if not has_text(row, key):
                    findings.append(finding("hold", "admission", f"Admission row is missing {label}.", text(row.get("id")), "Complete the shared-use backpressure policy."))
    return findings


def validate_quality_security_ops(manifest: dict[str, Any], rows: list[dict[str, Any]]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for row in [item for item in rows if lower(item.get("kind")) == "quality_boundary"]:
        quality = row_status(row.get("quality_status") if isinstance(row.get("quality_status"), dict) else {"status": row.get("quality_status")})
        if not has_text(row, "quality_status", "quality_gate", "decision", "status"):
            findings.append(finding("hold", "quality", "Quality boundary has no pass/hold/fail status.", text(row.get("id")), "Link quality runner result and record the quality decision."))
        if "fail" in quality:
            findings.append(finding("fail", "quality", "Quality boundary is failed.", text(row.get("id")), "Do not accept capacity when quality is blocked."))
        if not row_proof(row):
            findings.append(finding("hold", "quality", "Quality boundary has no proof link.", text(row.get("id")), "Link quality runner output, evaluation rows, or a scoped waiver."))

    path_rows = [row for row in rows if lower(row.get("kind")) in {"candidate_serving_path", "security_boundary"}]
    exposed = any(is_exposed(row, manifest) for row in path_rows)
    for row in [item for item in rows if lower(item.get("kind")) == "security_boundary"]:
        if not has_text(row, "endpoint_exposure", "network_boundary", "boundary"):
            findings.append(finding("hold", "security", "Security boundary has no endpoint exposure.", text(row.get("id")), "Record loopback, LAN, tunnel, public, remote, or provider boundary."))
        if not has_text(row, "data_boundary", "data_class", "privacy_boundary"):
            findings.append(finding("hold", "security", "Security boundary has no data boundary.", text(row.get("id")), "Record prompt, corpus, tool, UI, storage, and export boundary."))
        if not has_text(row, "log_export_boundary", "log_boundary", "retention", "export_boundary"):
            findings.append(finding("hold", "security", "Security boundary has no log/export boundary.", text(row.get("id")), "Record logs, retention, secret scan, and export/no-export proof."))
        if exposed and not has_text(row, "security_proof", "auth_proof", "approval", "firewall_proof"):
            findings.append(finding("fail", "security", "Endpoint is exposed beyond loopback without security proof.", exposure_value(row, manifest), "Add security runner output, auth/firewall proof, and explicit approval before accepting capacity."))

    for row in [item for item in rows if lower(item.get("kind")) == "observability_operations"]:
        if not has_text(row, "metrics_proof", "observability_proof", "log_proof", "resource_proof"):
            findings.append(finding("hold", "operations", "Operations row has no metrics, logs, or resource proof.", text(row.get("id")), "Link observability runner output, metrics scrape, logs, or resource snapshot."))
        if not has_text(row, "owner", "operator", "maintenance_owner"):
            findings.append(finding("hold", "operations", "Operations row has no owner.", text(row.get("id")), "Name who monitors, restarts, patches, and handles incidents."))
        if not has_text(row, "restart_procedure", "support_route", "startup", "runbook"):
            findings.append(finding("hold", "operations", "Operations row has no restart or support route.", text(row.get("id")), "Add restart/startup procedure, runbook, or support route."))

    for row in [item for item in rows if lower(item.get("kind")) == "cost_owner_review"]:
        if not has_text(row, "cost_model", "cost", "budget", "electricity", "hardware_cost"):
            findings.append(finding("hold", "review", "Cost/review row has no cost model.", text(row.get("id")), "Write hardware, electricity, rental GPU, hosted API, maintenance, or support assumptions."))
        if not has_text(row, "owner", "payer", "operator", "maintenance_owner"):
            findings.append(finding("hold", "review", "Cost/review row has no owner.", text(row.get("id")), "Name who pays, operates, and revisits the SLO."))
        if not has_text(row, "retest_trigger", "review_trigger", "next_review", "review_date"):
            findings.append(finding("hold", "review", "Cost/review row has no retest trigger.", text(row.get("id")), "State what model, workload, traffic, runtime, cost, or exposure change invalidates the decision."))
    return findings


def decide(findings: list[dict[str, str]]) -> tuple[str, str]:
    if any(item["level"] == "fail" for item in findings):
        return "fail", "capacity_slo_blocked"
    if any(item["level"] == "hold" for item in findings):
        return "hold", "capacity_slo_incomplete"
    return "pass", "capacity_slo_ready"


def md_cell(value: Any) -> str:
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=True)
    return text(value).replace("|", "\\|").replace("\n", " ")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = ["level", "owner", "finding", "evidence", "action"]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def append_jsonl(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(data, ensure_ascii=True) + "\n")


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    lines = [
        f"# Local LLM Capacity SLO Audit - {result['run_id']}",
        "",
        f"- Decision: `{result['decision']}` / `{result['reason']}`",
        f"- Workload: {md_cell(result.get('workload'))}",
        f"- Selected runtime/path: {md_cell(result.get('selected'))}",
        f"- Generated: {result['generated_at']}",
        "",
        "## Targets",
        "",
        "| Target | Value |",
        "|---|---|",
    ]
    for key, value in result.get("targets", {}).items():
        lines.append(f"| {md_cell(key)} | {md_cell(value)} |")
    lines.extend(["", "## Findings", "", "| Level | Owner | Finding | Evidence | Action |", "|---|---|---|---|---|"])
    if result["findings"]:
        for item in result["findings"]:
            lines.append(f"| {md_cell(item['level'])} | {md_cell(item['owner'])} | {md_cell(item['finding'])} | {md_cell(item['evidence'])} | {md_cell(item['action'])} |")
    else:
        lines.append("| pass | capacity | No blocking findings. | manifest | Promote to result synthesis or deployment decision. |")
    lines.extend(["", "## Handoff", ""])
    if result["decision"] == "pass":
        lines.append("- Feed this output into result synthesis, deployment decision, and deployment readiness.")
    elif result["decision"] == "hold":
        lines.append("- Complete the missing capacity evidence before accepting shared-use or deployment claims.")
    else:
        lines.append("- Treat the selected local service level as blocked until failed rows are fixed and rerun.")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_audit(manifest: dict[str, Any]) -> dict[str, Any]:
    rows = manifest.get("rows") if isinstance(manifest.get("rows"), list) else []
    normalized_rows = [row for row in rows if isinstance(row, dict)]
    grouped = group_rows(normalized_rows)
    required = manifest.get("required_kinds") if isinstance(manifest.get("required_kinds"), list) else DEFAULT_REQUIRED_KINDS
    required = [lower(kind) for kind in required if text(kind)]

    findings: list[dict[str, str]] = []
    findings.extend(validate_required(grouped, required))
    findings.extend(validate_workload(manifest, normalized_rows))
    findings.extend(validate_serving_path(manifest, normalized_rows))
    findings.extend(validate_demand(normalized_rows))
    findings.extend(validate_capacity(manifest, normalized_rows))
    findings.extend(validate_headroom(normalized_rows))
    findings.extend(validate_admission(manifest, normalized_rows))
    findings.extend(validate_quality_security_ops(manifest, normalized_rows))

    decision, reason = decide(findings)
    run_id = text(manifest.get("run_id")) or "capacity-slo-audit"
    selected = text(manifest.get("selected_runtime") or manifest.get("selected_path"))
    result = {
        "run_id": run_id,
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "decision": decision,
        "reason": reason,
        "workload": manifest.get("workload"),
        "selected": selected,
        "targets": {
            "latency_target_ms": latency_target(manifest, normalized_rows),
            "ttft_target_ms": ttft_target(manifest, normalized_rows),
            "throughput_target_rps": throughput_target(manifest, normalized_rows),
            "target_concurrency": target_concurrency(manifest, normalized_rows),
            "error_budget_percent": error_budget(manifest, normalized_rows),
        },
        "required_kinds": required,
        "findings": findings,
    }
    return result


def output_paths(manifest: dict[str, Any], result: dict[str, Any]) -> dict[str, Path]:
    run_root_value = os.environ.get("LOCAL_LLM_CAPACITY_SLO_RUN_ROOT") or manifest.get("run_root") or "."
    run_root = Path(text(run_root_value)).expanduser()
    run_id = result["run_id"]
    return {
        "json": run_root / f"{run_id}-capacity-slo-audit.json",
        "csv": run_root / f"{run_id}-capacity-slo-findings.csv",
        "md": run_root / f"{run_id}-capacity-slo-audit.md",
        "jsonl": run_root / "local-llm-capacity-slo-runs.jsonl",
    }


def load_manifest(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise SystemExit("Manifest root must be a JSON object.")
    return data


def write_outputs(manifest: dict[str, Any], result: dict[str, Any]) -> dict[str, str]:
    paths = output_paths(manifest, result)
    write_json(paths["json"], result)
    write_csv(paths["csv"], result["findings"])
    write_markdown(paths["md"], result)
    append_jsonl(paths["jsonl"], result)
    return {key: str(value) for key, value in paths.items()}


def complete_manifest() -> dict[str, Any]:
    return {
        "run_id": "fixture-pass",
        "run_root": "",
        "workload": "private local research assistant",
        "selected_runtime": "llama-cpp-q4",
        "slo": {
            "latency_target_ms": 6000,
            "ttft_target_ms": 1200,
            "throughput_target_rps": 0.25,
            "target_concurrency": 2,
            "error_budget_percent": 1.0,
        },
        "rows": [
            {"id": "contract", "kind": "workload_slo_contract", "status": "pass", "workload": "private local research assistant", "user_class": "single owner", "data_class": "personal", "latency_target_ms": 6000, "throughput_target_rps": 0.25, "target_concurrency": 2, "error_budget_percent": 1.0, "proof": "contract.md"},
            {"id": "path", "kind": "candidate_serving_path", "status": "pass", "selected": True, "runtime": "llama.cpp", "model_id": "example-q4", "route": "openai-compatible", "base_url": "http://127.0.0.1:8080/v1", "endpoint_exposure": "loopback", "proof": "api.json"},
            {"id": "demand", "kind": "demand_model", "status": "pass", "expected_rps": 0.12, "peak_rps": 0.25, "active_users": 2, "prompt_tokens_p95": 1800, "output_tokens_p95": 300, "proof": "demand.md"},
            {"id": "capacity", "kind": "measured_capacity", "status": "pass", "selected": True, "concurrency": 2, "p95_total_ms": 4300, "p99_total_ms": 5200, "p95_ttft_ms": 950, "throughput_rps": 0.31, "error_rate_percent": 0, "saturation_point": "C4 crosses target", "benchmark_audit": "benchmark.json", "concurrency_proof": "concurrency.json"},
            {"id": "headroom", "kind": "resource_headroom", "status": "pass", "peak_vram_gb": 8.4, "vram_budget_gb": 12, "peak_ram_gb": 18, "ram_budget_gb": 64, "kv_cache_budget": "20 percent reserve", "proof": "obs.md"},
            {"id": "admission", "kind": "admission_backpressure", "status": "pass", "max_concurrency": 2, "queue_limit": 4, "timeout_ms": 20000, "overload_behavior": "503 after queue limit", "batch_policy": "no offline batch", "proof": "admission.md"},
            {"id": "quality", "kind": "quality_boundary", "status": "pass", "quality_status": "pass", "quality_proof": "quality.json"},
            {"id": "security", "kind": "security_boundary", "status": "pass", "endpoint_exposure": "loopback", "data_boundary": "local", "log_export_boundary": "no export", "security_proof": "security.md"},
            {"id": "ops", "kind": "observability_operations", "status": "pass", "metrics_proof": "metrics.txt", "log_proof": "logs.md", "owner": "local", "restart_procedure": "documented"},
            {"id": "review", "kind": "cost_owner_review", "status": "pass", "cost_model": "owned GPU", "owner": "local", "retest_trigger": "new model or LAN exposure"},
        ],
    }


def run_self_tests() -> None:
    cases: list[tuple[str, dict[str, Any], str, str]] = []
    base = complete_manifest()
    cases.append(("complete exact SLO", base, "pass", "capacity_slo_ready"))

    missing_latency = json.loads(json.dumps(base))
    del missing_latency["slo"]["latency_target_ms"]
    del missing_latency["slo"]["ttft_target_ms"]
    missing_latency["rows"][0].pop("latency_target_ms", None)
    cases.append(("missing latency target", missing_latency, "hold", "capacity_slo_incomplete"))

    high_latency = json.loads(json.dumps(base))
    high_latency["rows"][3]["p95_total_ms"] = 7800
    cases.append(("selected latency over target", high_latency, "fail", "capacity_slo_blocked"))

    high_error = json.loads(json.dumps(base))
    high_error["rows"][3]["error_rate_percent"] = 2.5
    cases.append(("error rate above budget", high_error, "fail", "capacity_slo_blocked"))

    exposed = json.loads(json.dumps(base))
    exposed["rows"][1]["base_url"] = "http://0.0.0.0:8080/v1"
    exposed["rows"][1]["endpoint_exposure"] = "LAN"
    exposed["rows"][7].pop("security_proof", None)
    cases.append(("exposed service no security proof", exposed, "fail", "capacity_slo_blocked"))

    missing_capacity_proof = json.loads(json.dumps(base))
    missing_capacity_proof["rows"][3].pop("benchmark_audit", None)
    missing_capacity_proof["rows"][3].pop("concurrency_proof", None)
    cases.append(("missing capacity proof", missing_capacity_proof, "hold", "capacity_slo_incomplete"))

    missing_queue = json.loads(json.dumps(base))
    missing_queue["rows"][5] = {"id": "admission", "kind": "admission_backpressure", "status": "pass", "single_user_reason": "scratch run"}
    cases.append(("shared SLO missing backpressure", missing_queue, "hold", "capacity_slo_incomplete"))

    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        for name, manifest, expected_decision, expected_reason in cases:
            manifest["run_root"] = tmp
            result = run_audit(manifest)
            if result["decision"] != expected_decision or result["reason"] != expected_reason:
                failures.append((name, result["decision"], result["reason"], result["findings"]))
            else:
                write_outputs(manifest, result)
    if failures:
        print(json.dumps({"self_test": "fail", "failures": failures}, indent=2, ensure_ascii=True))
        raise SystemExit(1)
    print(json.dumps({"self_test": "pass", "cases": len(cases)}, indent=2, ensure_ascii=True))


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        run_self_tests()
        return 0
    manifest_path = os.environ.get("LOCAL_LLM_CAPACITY_SLO_MANIFEST")
    if not manifest_path and len(argv) > 1:
        manifest_path = argv[1]
    if not manifest_path:
        raise SystemExit("Set LOCAL_LLM_CAPACITY_SLO_MANIFEST or pass a manifest JSON path.")
    manifest = load_manifest(Path(manifest_path))
    result = run_audit(manifest)
    result["outputs"] = write_outputs(manifest, result)
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0 if result["decision"] == "pass" else 2 if result["decision"] == "hold" else 3


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
```

## Runner Decisions

| Decision | Reason | Meaning |
|---|---|---|
| `pass` | `capacity_slo_ready` | The saved evidence supports the local service level as written. |
| `hold` | `capacity_slo_incomplete` | Missing targets, proof links, admission policy, or resource/ops evidence prevents an SLO claim. |
| `fail` | `capacity_slo_blocked` | Measured latency, throughput, errors, quality, or exposure/security evidence contradicts the SLO. |

## Fixture Cases

Run:

```powershell
python local_llm_capacity_slo_planning_runner.py --self-test
```

Expected fixture coverage:

| Fixture | Expected |
|---|---|
| complete exact two-concurrency local SLO | `pass/capacity_slo_ready` |
| missing latency or TTFT target | `hold/capacity_slo_incomplete` |
| selected p95 latency exceeds target | `fail/capacity_slo_blocked` |
| observed error rate exceeds budget | `fail/capacity_slo_blocked` |
| exposed LAN or `0.0.0.0` service lacks security proof | `fail/capacity_slo_blocked` |
| measured capacity row has no benchmark/concurrency proof | `hold/capacity_slo_incomplete` |
| multi-user SLO has only a single-user queue waiver | `hold/capacity_slo_incomplete` |

## Handoff

| Output | Files | Next route |
|---|---|---|
| Capacity/SLO audit | `<run-id>-capacity-slo-audit.json`, `<run-id>-capacity-slo-audit.md`, `<run-id>-capacity-slo-findings.csv`, and one `local-llm-capacity-slo-runs.jsonl` row | Feed into [[LLM/Study/Local LLM Result Synthesis Runner|Local LLM Result Synthesis Runner]], [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]], and [[LLM/Study/LLM Deployment Readiness Audit Runner|LLM Deployment Readiness Audit Runner]] |
| Hold remediation | findings table with owner and action | Return to benchmark, concurrency, scheduler, observability, security, lifecycle, or quality runners |
| Fail remediation | failed metric or boundary evidence | Lower load, tune runtime, choose a smaller model, change deployment path, add security controls, or revise the workload SLO |

## Quick Checklist

- [ ] Workload and data boundary are named.
- [ ] Latency percentile target, throughput target or waiver, target concurrency, and error budget are explicit.
- [ ] Benchmark/concurrency proof links cover the selected model/runtime/path.
- [ ] p95 or p99 latency, TTFT if interactive, throughput, error rate, and saturation point are recorded.
- [ ] RAM/VRAM/KV/cache/resource headroom has evidence and a reserve statement.
- [ ] Admission control includes max concurrency, queue limit, timeout, and overload behavior for shared use.
- [ ] Quality, security, observability, lifecycle, owner, cost, and retest trigger are not missing.
- [ ] Result is routed into synthesis and deployment readiness before a final deployment claim.
