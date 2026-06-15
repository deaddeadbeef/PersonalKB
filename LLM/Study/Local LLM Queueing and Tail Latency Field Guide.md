---
tags: [study, llm, inference, local-llm, queueing, latency, throughput, capacity, scheduler, systems, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [core, deep-dive, practice]
last-verified: 2026-06-16
---

# Local LLM Queueing and Tail Latency Field Guide

> **One-line summary** Local LLM hosting becomes predictable when you can explain p95 latency as arrival rate, service time, queue wait, prefill, decode, KV-cache pressure, batching policy, and admission control instead of treating tokens/sec as capacity.

Use this after [[LLM/Study/Local LLM Inference Metrics Field Guide|Local LLM Inference Metrics Field Guide]] and before [[LLM/Study/Local LLM Serving Internals and Scheduler Lab|Local LLM Serving Internals and Scheduler Lab]], [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner|Local LLM Concurrency and Batch Throughput Runner]], or [[LLM/Study/Local LLM Capacity and SLO Planning Runner|Local LLM Capacity and SLO Planning Runner]] when the question is "will this local endpoint feel responsive under my workload?" rather than "can one prompt return?"

This guide is not a replacement for measurement. LLM serving is not a textbook M/M/1 queue: request lengths vary, prefill and decode stress different hardware paths, continuous batching changes service time, and KV-cache memory can become the real limiter. The queueing model is a discipline for asking the right questions before the local endpoint silently becomes an unbounded waiting room.

## The Mental Model

| Symbol or term | Local LLM meaning | What to measure |
|---|---|---|
| Arrival rate `lambda` | How many requests reach the endpoint per second or minute. | Expected and peak request rate from the workload. |
| Service time `S` | How long one request occupies useful serving capacity. | Total latency, TTFT, TPOT/ITL, output length, and route overhead. |
| Effective workers `c` | Slots, max sequences, max concurrent predictions, replicas, or batch capacity. | Runtime settings and measured concurrency level, not wishful hardware count. |
| Utilization `rho` | Approximate fraction of serving capacity consumed by arrivals. | `lambda * S / c` as a warning signal, then validate with load data. |
| Queue wait `Wq` | Time spent waiting before useful prefill/decode progress. | Runtime queue metrics, waiting counts, client timing, or controlled load tests. |
| Tail latency | The p95 or p99 user-visible wait, not the average. | p95/p99 total latency and p95 TTFT by prompt class. |
| Admission control | What happens when load exceeds the service envelope. | Queue limit, timeout, rejection status, retry rule, and user-facing fallback. |

Little's Law says average work-in-system equals arrival rate times average time-in-system. In local LLM terms: if requests arrive faster than the endpoint can complete them, either active/queued work grows, latency grows, errors/rejections appear, or the system must shed load. The exact formula is not enough for LLMs, but the invariant is a useful sanity check.

## Why LLM Queues Are Weird

| Ordinary web service assumption | LLM-serving complication | Local consequence |
|---|---|---|
| Requests have similar cost. | Prompt length, output length, tool/RAG context, and sampling can vary widely. | Measure by prompt class, not only one smoke prompt. |
| One worker handles one request at a time. | Continuous batching can mix active sequences each token step. | Slots and `max_num_seqs` are not the same as independent workers. |
| CPU time dominates. | Prefill can be compute-heavy, decode can be memory-bandwidth-heavy, and KV cache can be capacity-heavy. | Separate TTFT, TPOT, memory, and queue evidence. |
| More batching always helps. | Batching improves throughput but can hurt p95 TTFT or ITL. | Tune for the workload SLO, not peak tokens/sec. |
| Retries are harmless. | Retrying long prompts can double queue pressure and cache memory. | Use bounded retries and explicit overload behavior. |
| Average latency is enough. | Human-facing chat fails on tail latency. | Use p95/p99 and failed/timeout rows. |

## Phase Map

| Phase | Queueing interpretation | Tail-latency symptom | First route |
|---|---|---|---|
| Arrival | Requests enter faster or slower than service capacity. | Waiting count rises before model metrics look bad. | Demand model in [[LLM/Study/Local LLM Capacity and SLO Planning Runner|Capacity and SLO Planning Runner]] |
| Queue wait | Request is admitted but not making model progress. | p95 total latency grows while TTFT may include hidden wait. | [[LLM/Study/Local LLM Observability and Operations Runner|Observability and Operations Runner]] |
| Prefill | Prompt tokens are processed and initial KV cache is built. | Long prompts spike TTFT and can delay short prompts. | [[LLM/Study/Local LLM Context Window and Token Budgeting Runner|Context Window and Token Budgeting Runner]] |
| Decode | Output tokens are generated one step at a time. | ITL/TPOT worsens or streaming feels slow after first token. | [[LLM/Study/Local LLM Inference Metrics Field Guide|Inference Metrics Field Guide]] |
| KV/cache allocation | Active sequences consume cache memory. | Higher concurrency or longer context causes preemption, OOM, or rejection. | [[LLM/Study/Local LLM KV Cache Sizing Runner|KV Cache Sizing Runner]] |
| Admission/backpressure | The system rejects, queues, times out, or reroutes overload. | User sees failures, stalls, or retry storms. | [[LLM/Study/Local LLM Capacity and SLO Planning Runner|Capacity and SLO Planning Runner]] |

## Tail-Latency Questions

Before changing runtime flags, answer these in order:

1. What is the workload class: single-owner interactive, shared household/team, batch/offline, RAG, tool loop, or product API?
2. What is the p95 user-visible latency target, and is TTFT or full completion more important?
3. What are p95 prompt tokens and output tokens for the workload?
4. What request rate and concurrency are expected at peak?
5. What does the concurrency ladder show at `C1`, the target concurrency, and one level above target?
6. Does the runtime expose queue, waiting, slots, KV/cache usage, preemption, errors, or rejected requests?
7. What happens at overload: queue, reject, timeout, degrade to smaller model, batch offline, or ask the user to retry later?
8. Which proof artifact would make the claim defensible: benchmark audit, scheduler audit, observability snapshot, capacity/SLO audit, or deployment readiness?

## Queueing Worksheet Fields

Record these before treating a local endpoint as usable beyond one prompt:

| Field | Meaning |
|---|---|
| `arrival_rate_rps` | Peak expected request arrival rate. Use requests per second; convert requests/minute by dividing by 60. |
| `mean_service_ms` | Mean observed completion latency at the selected concurrency. |
| `p95_total_ms` | Tail completion latency for the workload prompt class. |
| `p95_ttft_ms` | Tail time to first token when the workload is interactive. |
| `effective_parallelism` | Selected slots, max concurrent predictions, max sequences, replicas, or measured equivalent. |
| `target_p95_total_ms` | User-visible tail latency budget. |
| `target_p95_ttft_ms` | Optional responsiveness budget for streaming/chat. |
| `error_rate_percent` | Timeout, overload, HTTP error, failed parse, or rejected-request rate. |
| `max_error_rate_percent` | Error budget for the workload. |
| `admission_policy` | Queue limit, max concurrency, timeout, rejection/fallback, and retry rule. |

Approximate utilization:

```text
rho ~= arrival_rate_rps * (mean_service_ms / 1000) / effective_parallelism
```

Interpret `rho` cautiously. Continuous batching means service capacity is not a fixed independent-worker count. Still, when `rho` is near 1 and p95 is rising, the endpoint is not SLO-ready without admission or more capacity.

## Standard-Library Worksheet

Save this as `local_llm_queueing_tail_latency_worksheet.py` inside a run folder. It audits a saved manifest and writes JSON, CSV, Markdown, and JSONL outputs without calling a model.

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


FAIL_STATUSES = {"fail", "failed", "blocked", "error"}
HOLD_STATUSES = {"hold", "pending", "incomplete", "unknown", "missing"}
PASS_STATUSES = {"pass", "passed", "ok", "ready", "waived"}


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


def number(value: Any) -> float | None:
    if value is None or value == "":
        return None
    if isinstance(value, bool):
        return float(value)
    if isinstance(value, (int, float)):
        return float(value)
    raw = str(value).strip().lower().replace(",", "")
    for suffix in ("requests/minute", "req/min", "rpm", "requests/second", "req/s", "rps", "ms", "s", "%"):
        raw = raw.replace(suffix, "")
    try:
        return float(raw.strip())
    except ValueError:
        return None


def pick(row: dict[str, Any], *keys: str) -> float | None:
    for key in keys:
        value = number(row.get(key))
        if value is not None:
            return value
    return None


def has_text(row: dict[str, Any], *keys: str) -> bool:
    return any(bool(text(row.get(key))) for key in keys)


def status(row: dict[str, Any]) -> str:
    return lower(row.get("status") or row.get("decision") or "unknown")


def finding(level: str, owner: str, message: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "owner": owner,
        "finding": message,
        "evidence": evidence,
        "action": action,
    }


def manifest_rows(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    rows = manifest.get("rows")
    if isinstance(rows, list):
        return [row for row in rows if isinstance(row, dict)]
    return []


def find_first(rows: list[dict[str, Any]], kind: str) -> dict[str, Any]:
    for row in rows:
        if lower(row.get("kind")) == kind:
            return row
    return {}


def target_from(manifest: dict[str, Any], row: dict[str, Any], *keys: str) -> float | None:
    slo = manifest.get("slo")
    if not isinstance(slo, dict):
        slo = {}
    for source in (row, slo, manifest):
        for key in keys:
            value = number(source.get(key))
            if value is not None:
                return value
    return None


def arrival_rate(manifest: dict[str, Any], demand: dict[str, Any]) -> float | None:
    rps = target_from(manifest, demand, "arrival_rate_rps", "peak_rps", "expected_rps")
    if rps is not None:
        return rps
    rpm = target_from(manifest, demand, "arrival_rate_rpm", "requests_per_minute", "peak_requests_per_minute")
    if rpm is not None:
        return rpm / 60.0
    return None


def utilization(arrival_rps: float | None, mean_service_ms: float | None, effective_parallelism: float | None) -> float | None:
    if arrival_rps is None or mean_service_ms is None or effective_parallelism is None or effective_parallelism <= 0:
        return None
    return arrival_rps * (mean_service_ms / 1000.0) / effective_parallelism


def validate_status_rows(rows: list[dict[str, Any]]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for row in rows:
        row_status = status(row)
        kind = lower(row.get("kind")) or text(row.get("id")) or "row"
        if row_status in FAIL_STATUSES:
            findings.append(finding("fail", kind, "Evidence row is marked failed.", text(row.get("id") or kind), "Fix the failed row before accepting the queueing worksheet."))
        elif row_status in HOLD_STATUSES:
            findings.append(finding("hold", kind, "Evidence row is not pass-ready.", text(row.get("id") or kind), "Complete the row or add a scoped waiver."))
        elif row_status and row_status not in PASS_STATUSES:
            findings.append(finding("hold", kind, "Evidence row has an unrecognized status.", row_status, "Use pass, hold, fail, or waived."))
    return findings


def validate_manifest(manifest: dict[str, Any]) -> dict[str, Any]:
    rows = manifest_rows(manifest)
    demand = find_first(rows, "demand_model")
    measurement = find_first(rows, "tail_latency_measurement")
    admission = find_first(rows, "admission_policy")
    proof = find_first(rows, "proof_links")
    findings: list[dict[str, str]] = []
    findings.extend(validate_status_rows(rows))

    if not text(manifest.get("workload")) and not has_text(demand, "workload"):
        findings.append(finding("hold", "workload", "No workload is named.", "manifest", "Name the local LLM workload."))
    if not demand:
        findings.append(finding("hold", "demand", "Missing demand_model row.", "rows", "Add arrival rate, prompt/output shape, and target concurrency."))
    if not measurement:
        findings.append(finding("hold", "measurement", "Missing tail_latency_measurement row.", "rows", "Add observed mean, p95, error rate, and effective parallelism."))
    if not admission:
        findings.append(finding("hold", "admission", "Missing admission_policy row.", "rows", "Add max concurrency, queue limit, timeout, overload behavior, and retry policy."))

    arrival = arrival_rate(manifest, demand)
    mean_service_ms = target_from(manifest, measurement, "mean_service_ms", "mean_total_ms", "avg_total_ms")
    p95_total_ms = target_from(manifest, measurement, "p95_total_ms", "p95_latency_ms", "p95_e2e_ms")
    p95_ttft_ms = target_from(manifest, measurement, "p95_ttft_ms", "ttft_p95_ms")
    effective_parallelism = target_from(manifest, measurement, "effective_parallelism", "slots", "max_concurrency", "max_num_seqs")
    target_p95_total_ms = target_from(manifest, demand, "target_p95_total_ms", "latency_target_ms", "p95_latency_target_ms")
    target_p95_ttft_ms = target_from(manifest, demand, "target_p95_ttft_ms", "ttft_target_ms")
    error_rate = target_from(manifest, measurement, "error_rate_percent", "timeout_rate_percent", "rejection_rate_percent")
    max_error_rate = target_from(manifest, demand, "max_error_rate_percent", "error_budget_percent")
    rho = utilization(arrival, mean_service_ms, effective_parallelism)

    if arrival is None:
        findings.append(finding("hold", "demand", "Arrival rate is missing.", "demand_model", "Add arrival_rate_rps or requests_per_minute."))
    if mean_service_ms is None:
        findings.append(finding("hold", "measurement", "Mean service time is missing.", "tail_latency_measurement", "Add mean_service_ms or mean_total_ms."))
    if p95_total_ms is None and p95_ttft_ms is None:
        findings.append(finding("hold", "measurement", "No p95 total latency or p95 TTFT is recorded.", "tail_latency_measurement", "Add tail latency for the target prompt class."))
    if effective_parallelism is None:
        findings.append(finding("hold", "measurement", "Effective parallelism is missing.", "tail_latency_measurement", "Add measured slots, max concurrency, max sequences, or replicas."))
    if target_p95_total_ms is None and target_p95_ttft_ms is None:
        findings.append(finding("hold", "slo", "No tail-latency target is recorded.", "slo", "Add p95 total latency target or TTFT target."))
    if error_rate is None:
        findings.append(finding("hold", "measurement", "Error rate is missing.", "tail_latency_measurement", "Add timeout, rejection, HTTP error, or failure rate."))
    if max_error_rate is None:
        findings.append(finding("hold", "slo", "Error budget is missing.", "slo", "Add max_error_rate_percent or error_budget_percent."))

    if rho is not None:
        if rho >= 1.0:
            findings.append(finding("fail", "queueing", "Estimated utilization is at or above saturation.", f"rho={rho:.3f}", "Lower arrival rate, increase capacity, reduce service time, or add admission control."))
        elif rho >= 0.8:
            findings.append(finding("hold", "queueing", "Estimated utilization is high enough that p95 may be fragile.", f"rho={rho:.3f}", "Validate with a concurrency ladder at peak load and one level above target."))

    if target_p95_total_ms is not None and p95_total_ms is not None and p95_total_ms > target_p95_total_ms:
        findings.append(finding("fail", "latency", "Observed p95 total latency exceeds target.", f"{p95_total_ms:g}ms > {target_p95_total_ms:g}ms", "Reduce load, tune scheduler, lower prompt/output size, change runtime/model, or revise the SLO."))
    if target_p95_ttft_ms is not None and p95_ttft_ms is not None and p95_ttft_ms > target_p95_ttft_ms:
        findings.append(finding("fail", "latency", "Observed p95 TTFT exceeds target.", f"{p95_ttft_ms:g}ms > {target_p95_ttft_ms:g}ms", "Reduce prefill, chunk/split long prompts, tune scheduler, or reject overloaded requests."))
    if max_error_rate is not None and error_rate is not None and error_rate > max_error_rate:
        findings.append(finding("fail", "errors", "Observed error rate exceeds budget.", f"{error_rate:g}% > {max_error_rate:g}%", "Fix overload, timeouts, or retries before accepting the service level."))

    if admission:
        for key, label in (("max_concurrency", "max concurrency"), ("queue_limit", "queue limit"), ("timeout_ms", "timeout"), ("overload_behavior", "overload behavior"), ("retry_policy", "retry policy")):
            if not has_text(admission, key):
                findings.append(finding("hold", "admission", f"Admission policy is missing {label}.", text(admission.get("id")), "Complete the overload contract before claiming capacity."))
    if proof and not has_text(proof, "benchmark_audit", "concurrency_runner", "observability_runner", "capacity_slo_runner"):
        findings.append(finding("hold", "proof", "Proof row does not link benchmark, concurrency, observability, or SLO evidence.", text(proof.get("id")), "Link the artifacts that make this worksheet inspectable."))
    elif not proof:
        findings.append(finding("hold", "proof", "Missing proof_links row.", "rows", "Link benchmark, concurrency, observability, and capacity/SLO artifacts."))

    if any(item["level"] == "fail" for item in findings):
        decision, reason = "fail", "tail_latency_blocked"
    elif any(item["level"] == "hold" for item in findings):
        decision, reason = "hold", "tail_latency_incomplete"
    else:
        decision, reason = "pass", "tail_latency_ready"

    return {
        "run_id": text(manifest.get("run_id")) or "queueing-tail-latency",
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "workload": manifest.get("workload"),
        "decision": decision,
        "reason": reason,
        "metrics": {
            "arrival_rate_rps": arrival,
            "mean_service_ms": mean_service_ms,
            "effective_parallelism": effective_parallelism,
            "estimated_utilization": rho,
            "p95_total_ms": p95_total_ms,
            "target_p95_total_ms": target_p95_total_ms,
            "p95_ttft_ms": p95_ttft_ms,
            "target_p95_ttft_ms": target_p95_ttft_ms,
            "error_rate_percent": error_rate,
            "max_error_rate_percent": max_error_rate,
        },
        "findings": findings,
    }


def md_cell(value: Any) -> str:
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=True)
    return text(value).replace("|", "\\|").replace("\n", " ")


def output_paths(manifest: dict[str, Any], result: dict[str, Any]) -> dict[str, Path]:
    run_root = Path(text(os.environ.get("LOCAL_LLM_QUEUEING_RUN_ROOT") or manifest.get("run_root") or ".")).expanduser()
    run_id = result["run_id"]
    return {
        "json": run_root / f"{run_id}-queueing-tail-latency.json",
        "csv": run_root / f"{run_id}-queueing-tail-latency-findings.csv",
        "md": run_root / f"{run_id}-queueing-tail-latency.md",
        "jsonl": run_root / "local-llm-queueing-tail-latency-runs.jsonl",
    }


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def write_csv(path: Path, findings: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = ["level", "owner", "finding", "evidence", "action"]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in findings:
            writer.writerow({field: row.get(field, "") for field in fields})


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    lines = [
        f"# Local LLM Queueing Tail Latency - {result['run_id']}",
        "",
        f"- Decision: `{result['decision']}` / `{result['reason']}`",
        f"- Workload: {md_cell(result.get('workload'))}",
        f"- Generated: {result['generated_at']}",
        "",
        "## Metrics",
        "",
        "| Metric | Value |",
        "|---|---|",
    ]
    for key, value in result["metrics"].items():
        lines.append(f"| {md_cell(key)} | {md_cell(value)} |")
    lines.extend(["", "## Findings", "", "| Level | Owner | Finding | Evidence | Action |", "|---|---|---|---|---|"])
    if result["findings"]:
        for item in result["findings"]:
            lines.append(f"| {md_cell(item['level'])} | {md_cell(item['owner'])} | {md_cell(item['finding'])} | {md_cell(item['evidence'])} | {md_cell(item['action'])} |")
    else:
        lines.append("| pass | queueing | No blocking findings. | manifest | Feed this worksheet into scheduler, concurrency, and capacity/SLO evidence. |")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def append_jsonl(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(data, ensure_ascii=True) + "\n")


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
        "workload": "private local chat",
        "slo": {
            "target_p95_total_ms": 6000,
            "target_p95_ttft_ms": 1200,
            "max_error_rate_percent": 1.0,
        },
        "rows": [
            {"id": "demand", "kind": "demand_model", "status": "pass", "arrival_rate_rps": 0.2, "prompt_tokens_p95": 1200, "output_tokens_p95": 256},
            {"id": "latency", "kind": "tail_latency_measurement", "status": "pass", "mean_service_ms": 2500, "p95_total_ms": 4300, "p95_ttft_ms": 900, "effective_parallelism": 2, "error_rate_percent": 0},
            {"id": "admission", "kind": "admission_policy", "status": "pass", "max_concurrency": 2, "queue_limit": 4, "timeout_ms": 20000, "overload_behavior": "503 after queue limit", "retry_policy": "one bounded retry after user confirmation"},
            {"id": "proof", "kind": "proof_links", "status": "pass", "benchmark_audit": "benchmark.json", "concurrency_runner": "concurrency.json", "observability_runner": "ops.json", "capacity_slo_runner": "slo.json"},
        ],
    }


def run_self_tests() -> None:
    cases: list[tuple[str, dict[str, Any], str, str]] = []
    base = complete_manifest()
    cases.append(("complete queueing worksheet", base, "pass", "tail_latency_ready"))

    missing_arrival = json.loads(json.dumps(base))
    missing_arrival["rows"][0].pop("arrival_rate_rps", None)
    cases.append(("missing arrival rate", missing_arrival, "hold", "tail_latency_incomplete"))

    high_utilization = json.loads(json.dumps(base))
    high_utilization["rows"][0]["arrival_rate_rps"] = 0.75
    cases.append(("high utilization", high_utilization, "hold", "tail_latency_incomplete"))

    saturated = json.loads(json.dumps(base))
    saturated["rows"][0]["arrival_rate_rps"] = 1.0
    cases.append(("saturated utilization", saturated, "fail", "tail_latency_blocked"))

    bad_tail = json.loads(json.dumps(base))
    bad_tail["rows"][1]["p95_total_ms"] = 7000
    cases.append(("p95 over target", bad_tail, "fail", "tail_latency_blocked"))

    bad_errors = json.loads(json.dumps(base))
    bad_errors["rows"][1]["error_rate_percent"] = 2.5
    cases.append(("errors over budget", bad_errors, "fail", "tail_latency_blocked"))

    missing_admission = json.loads(json.dumps(base))
    missing_admission["rows"][2].pop("queue_limit", None)
    cases.append(("missing queue limit", missing_admission, "hold", "tail_latency_incomplete"))

    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        for name, manifest, expected_decision, expected_reason in cases:
            manifest["run_root"] = tmp
            result = validate_manifest(manifest)
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
    manifest_path = os.environ.get("LOCAL_LLM_QUEUEING_MANIFEST")
    if not manifest_path and len(argv) > 1:
        manifest_path = argv[1]
    if not manifest_path:
        raise SystemExit("Set LOCAL_LLM_QUEUEING_MANIFEST or pass a manifest JSON path.")
    with Path(manifest_path).open("r", encoding="utf-8") as handle:
        manifest = json.load(handle)
    if not isinstance(manifest, dict):
        raise SystemExit("Manifest root must be a JSON object.")
    result = validate_manifest(manifest)
    result["outputs"] = write_outputs(manifest, result)
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0 if result["decision"] == "pass" else 2 if result["decision"] == "hold" else 3


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
```

## Worksheet Decisions

| Decision | Reason | Meaning |
|---|---|---|
| `pass` | `tail_latency_ready` | Demand, measurement, admission, proof, and target fit are ready to feed scheduler/concurrency/SLO evidence. |
| `hold` | `tail_latency_incomplete` | Missing demand, tail-latency, admission, proof, or fragile high-utilization evidence blocks the claim. |
| `fail` | `tail_latency_blocked` | Utilization saturation, p95 target breach, TTFT target breach, or error-budget breach contradicts the SLO. |

## Fixture Cases

Run:

```powershell
python local_llm_queueing_tail_latency_worksheet.py --self-test
```

Expected fixture coverage:

| Fixture | Expected |
|---|---|
| complete queueing worksheet | `pass/tail_latency_ready` |
| missing arrival rate | `hold/tail_latency_incomplete` |
| estimated utilization over 0.8 | `hold/tail_latency_incomplete` |
| estimated utilization at or above 1.0 | `fail/tail_latency_blocked` |
| p95 total latency over target | `fail/tail_latency_blocked` |
| error rate over budget | `fail/tail_latency_blocked` |
| missing queue limit in admission policy | `hold/tail_latency_incomplete` |

## Reading The Result

| Result pattern | Interpretation | Next action |
|---|---|---|
| Low utilization, p95 passes, errors pass | The load shape may fit, assuming quality and security also pass. | Feed into [[LLM/Study/Local LLM Capacity and SLO Planning Runner|Capacity and SLO Planning Runner]]. |
| Low average, high p95 | Bursty arrivals, long-prompt interference, decode contention, or queue wait is hidden by the mean. | Run [[LLM/Study/Local LLM Serving Internals and Scheduler Lab|Serving Internals and Scheduler Lab]]. |
| High utilization before p95 fails | The service is fragile; small workload drift can break tail latency. | Lower concurrency target, increase capacity, add admission control, or split queues. |
| TTFT fails but total latency passes | The answer eventually finishes but interactive feel is poor. | Reduce prompt/context, test chunked prefill, or separate long prompts. |
| Error budget fails | The endpoint is not reliably serving the workload. | Fix timeout/rejection/retry policy before deployment. |
| No admission policy | The benchmark is not a service contract. | Define max concurrency, queue limit, timeout, overload behavior, and retry rule. |

## Practical Rules

- Treat p95 as the default local-hosting decision metric for interactive work; reserve p99 for stricter service contracts.
- Do not use peak output tokens/sec as the capacity claim unless the workload is batch/offline.
- Run at least one load level above the intended target; a target that only passes exactly at the target has no drift margin.
- Separate short interactive prompts from long RAG/tool prompts when p95 matters.
- Set output caps before capacity tests; unbounded decode turns one user into a queueing incident.
- Prefer rejection or explicit "try later" behavior over an unbounded queue for personal and small-team services.
- Re-run this worksheet when model, quantization, context length, runtime, driver, hardware, route, prompt mix, or user count changes.

## Completion Gate

This guide has served its purpose when:

- [ ] Arrival rate and target concurrency are written down.
- [ ] Mean service time, p95 total latency, p95 TTFT if interactive, and error rate are measured.
- [ ] Effective parallelism is tied to actual runtime settings or measured concurrency, not hardware guesses.
- [ ] Estimated utilization is calculated and interpreted as a warning signal, not final proof.
- [ ] Admission policy names max concurrency, queue limit, timeout, overload behavior, and retry behavior.
- [ ] Benchmark, concurrency, observability, scheduler, and capacity/SLO artifacts are linked.
- [ ] A failed or held row routes to one controlled next action.

## References

Internal:

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM Scheduler Evidence Audit Runner]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner]]
- [[LLM/Study/Local LLM Observability and Operations Runner]]
- [[LLM/Study/Local LLM Capacity and SLO Planning Runner]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/_chunks/chunk-llm-117 PagedAttention Eliminates KV Fragmentation]]
- [[LLM/_chunks/chunk-llm-118 vLLM Continuous Batching Throughput]]
- [[LLM/_chunks/chunk-llm-119 PagedAttention Copy-on-Write Sharing]]

External sources checked 2026-06-16:

- [Orca: A Distributed Serving System for Transformer-Based Generative Models](https://www.usenix.org/conference/osdi22/presentation/yu)
- [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)
- [Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve](https://arxiv.org/abs/2403.02310)
- [vLLM Optimization and Tuning](https://docs.vllm.ai/en/stable/configuration/optimization/)
- [vLLM Production Metrics](https://docs.vllm.ai/en/v0.14.0/usage/metrics/)
- [SGLang Production Metrics](https://docs.sglang.io/docs/references/production_metrics)
- [llama.cpp server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
