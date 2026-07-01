---
tags: [study, llm, inference, local-llm, serving, scheduler, kv-cache, batching, evidence, audit, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice, deep-dive]
last-verified: 2026-06-15
---

# Local LLM Scheduler Evidence Audit Runner

> **One-line summary** Scheduler mastery is credible when cold load, prefill, decode, KV-cache pressure, batching, queueing, and tuning claims are linked to evidence rows instead of inferred from one fast or slow response.

Use this after [[LLM/Study/Local LLM Serving Internals and Scheduler Lab|Local LLM Serving Internals and Scheduler Lab]] when the lab rows, concurrency output, prompt-cache run, observability snapshot, or benchmark rows should become one pass, hold, fail, JSON, Markdown, CSV, and JSONL audit.

This runner does not send generation requests. It audits a manifest of evidence you already collected from [[LLM/Study/LLM Inference Request Lifecycle Runner|LLM Inference Request Lifecycle Runner]], [[LLM/Study/Local LLM Observability and Operations Runner|Local LLM Observability and Operations Runner]], [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner|Local LLM Concurrency and Batch Throughput Runner]], [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner|Local LLM Prompt Cache and KV Reuse Runner]], [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]], or a dated capstone note.

## What This Proves

| Evidence family | Checks | Why it matters |
|---|---|---|
| Scheduler hypothesis | runtime, model, workload, symptom, suspected mechanism, fixed variable | prevents random tuning |
| Latency phase split | cold/warm, short/long, repeated-prefix, TTFT, TPOT, total latency | separates load, prefill, decode, and client overhead |
| Scheduler state | metrics, slots, queue, running/waiting, KV/cache, logs, not-exposed reason | grounds theory in the local runtime |
| Long-prompt interference | short-only, long-only, mixed, p95 TTFT, memory, errors | catches prefill/KV pressure before shared use |
| One-variable tuning | changed variable, before/after values, latency, throughput, memory, quality | prevents confounded runtime decisions |
| Capacity events | preemption, OOM, queue timeout, rejection, or explicit none-seen row | names the owner before increasing concurrency |
| Decision card | bottleneck, concurrency/slot policy, long-prompt policy, cache policy, retest trigger | turns measurements into an operational choice |

Academic bridge: serving systems optimize the same transformer mechanisms you learn in the papers. Prefill builds KV cache, decode consumes memory bandwidth one token step at a time, PagedAttention reduces KV fragmentation, continuous batching changes the latency-throughput frontier, and chunked prefill trades prompt processing against interactive decode responsiveness.

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "scheduler-audit-001",
  "run_root": "D:/llm-runs/scheduler-audit",
  "vault_root": "D:/Vaults/PersonalKB",
  "runtime": "vLLM",
  "model": "example-model",
  "workload": "local chat plus short RAG",
  "rows": [
    {
      "id": "hypothesis",
      "kind": "hypothesis",
      "status": "pass",
      "critical": true,
      "proof": "LLM/Study/Local LLM Serving Internals and Scheduler Lab.md",
      "mechanism": "prefill",
      "claim": "Long prompts are increasing TTFT.",
      "evidence": "Hypothesis row freezes prompt suite, sampler, route, and one variable.",
      "next_route": "LLM/Study/Local LLM Serving Internals and Scheduler Lab"
    },
    {
      "id": "decision",
      "kind": "decision_card",
      "status": "pass",
      "critical": true,
      "proof": "LLM/Study/Local LLM Inference Benchmark Log.md",
      "mechanism": "scheduler",
      "claim": "Use a local queue with lower max active sequences for interactive chat.",
      "evidence": "Decision card links benchmark, concurrency, and observability rows.",
      "metrics": {
        "bottleneck": "prefill",
        "long_prompt_policy": "separate queue",
        "retest_trigger": "new model or context target"
      },
      "next_route": "LLM/Study/LLM Deployment Decision Matrix"
    }
  ]
}
```

`proof` may be an absolute path, a vault-relative path, an Obsidian note path, or an Obsidian link. Use `not_exposed_reason` when a runtime does not expose a scheduler field. Use `waiver_reason` only when a required evidence kind is deliberately out of scope.

## Required Evidence Kinds

By default, the audit expects one row for each kind:

| Kind | Required fields or acceptable substitute |
|---|---|
| `hypothesis` | `mechanism`, `claim`, `proof` |
| `latency_phase` | timing signal in `metrics`, plus `claim` or `evidence` |
| `scheduler_state` | scheduler/cache/queue signal in `metrics`, or `not_exposed_reason` |
| `long_prompt_interference` | comparison signal, decision, or explicit skipped reason |
| `tuning_delta` | changed variable and before/after, or explicit no-tuning decision |
| `capacity_event` | preemption/OOM/queue/rejection evidence, or explicit none-seen row |
| `decision_card` | bottleneck, policy, next route, and retest trigger |

You can override this with `required_kinds` in the manifest.

## Standard-Library Runner

Save this as `scheduler-evidence-audit-runner.py` inside the run folder. It uses only Python's standard library.

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
    "hypothesis",
    "latency_phase",
    "scheduler_state",
    "long_prompt_interference",
    "tuning_delta",
    "capacity_event",
    "decision_card",
]

KIND_HINTS = {
    "hypothesis": {
        "owner": "scheduler",
        "pass_signal": "Runtime, workload, symptom, suspected mechanism, fixed route, fixed sampler, and one variable are written before tuning.",
        "next_route": "LLM/Study/Local LLM Serving Internals and Scheduler Lab",
    },
    "latency_phase": {
        "owner": "prefill/decode",
        "pass_signal": "Cold/warm, short/long, or repeated-prefix rows separate TTFT, TPOT, total latency, prompt tokens, and output tokens.",
        "next_route": "LLM/Study/LLM Inference Request Lifecycle Runner",
    },
    "scheduler_state": {
        "owner": "runtime",
        "pass_signal": "Metrics, slots, queue, loaded-model, KV/cache, logs, or a not-exposed reason are attached.",
        "next_route": "LLM/Study/Local LLM Observability and Operations Runner",
    },
    "long_prompt_interference": {
        "owner": "prefill/KV cache",
        "pass_signal": "Short-only, long-only, and mixed traffic are compared, or the skip reason is explicit.",
        "next_route": "LLM/Study/Local LLM Serving Internals and Scheduler Lab",
    },
    "tuning_delta": {
        "owner": "scheduler policy",
        "pass_signal": "Exactly one scheduler/cache/concurrency variable changed with before/after latency, throughput, memory, and quality consequences.",
        "next_route": "LLM/Study/Local LLM Serving Internals and Scheduler Lab",
    },
    "capacity_event": {
        "owner": "capacity",
        "pass_signal": "Preemption, OOM, queue timeout, rejection, or explicit none-seen evidence is recorded.",
        "next_route": "LLM/Study/Local LLM Troubleshooting Decision Tree",
    },
    "decision_card": {
        "owner": "deployment",
        "pass_signal": "The final card states bottleneck, concurrency/slot policy, queue policy, long-prompt policy, cache decision, next route, and retest trigger.",
        "next_route": "LLM/Study/LLM Deployment Decision Matrix",
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
    return text.strip("-") or "scheduler-evidence-audit"


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
    if text in {"true", "yes", "y", "1", "required", "critical"}:
        return True
    if text in {"false", "no", "n", "0", "optional", "waived", "not-required"}:
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
    manifest_path = os.environ.get("LOCAL_LLM_SCHEDULER_AUDIT_MANIFEST")
    if not manifest_path:
        raise ValueError("Set LOCAL_LLM_SCHEDULER_AUDIT_MANIFEST to a JSON manifest path.")
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
    return KIND_HINTS.get(kind, {}).get("next_route", "LLM/Study/Local LLM Serving Internals and Scheduler Lab")


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


def evaluate_kind_requirements(row: dict[str, Any], kind: str, findings: list[dict[str, str]]) -> None:
    metrics = row.get("metrics") if isinstance(row.get("metrics"), dict) else {}
    owner = KIND_HINTS.get(kind, {}).get("owner", kind)
    claim_or_evidence = has_text(row, "claim", "evidence", "decision", "summary")

    if kind == "hypothesis":
        if not has_text(row, "mechanism", "suspected_mechanism"):
            findings.append(finding("hold", owner, "Scheduler hypothesis has no suspected mechanism.", kind, "Name cold load, prefill, decode, KV cache, queue, batching, prefix cache, or admission."))
        if not claim_or_evidence:
            findings.append(finding("hold", owner, "Scheduler hypothesis has no claim or evidence text.", kind, "Write the falsifiable symptom and one variable to change."))
    elif kind == "latency_phase":
        timing_names = ("ttft_ms", "time_to_first_token_ms", "tpot_ms", "itl_ms", "total_latency_ms", "prompt_eval_ms", "decode_ms", "tokens_per_second", "output_tokens")
        if not has_any_metric(metrics, timing_names):
            findings.append(finding("hold", owner, "Latency phase row has no timing or token metric.", kind, "Add TTFT, TPOT, total latency, prompt-eval time, output tokens, or tokens/sec."))
        if not claim_or_evidence:
            findings.append(finding("hold", owner, "Latency phase row has no interpretation.", kind, "State whether the owner is cold load, prefill, decode, queue, client, or unknown."))
    elif kind == "scheduler_state":
        scheduler_names = ("running", "waiting", "queued", "slots", "max_seqs", "kv_cache_usage", "cache_hit_rate", "preemptions", "oom", "metrics_url", "slots_url")
        if not has_any_metric(metrics, scheduler_names) and not has_text(row, "not_exposed_reason", "scheduler_state", "log_excerpt"):
            findings.append(finding("hold", owner, "Scheduler state row has no metrics, slots, logs, or not-exposed reason.", kind, "Attach runtime metrics/slots/log evidence or explain what the runtime does not expose."))
    elif kind == "long_prompt_interference":
        mix_names = ("short_only_p95_ttft_ms", "long_only_p95_ttft_ms", "mixed_p95_ttft_ms", "mixed_errors", "peak_vram_mb", "queue_wait_ms")
        if not has_any_metric(metrics, mix_names) and not has_text(row, "skip_reason", "decision", "comparison"):
            findings.append(finding("hold", owner, "Long-prompt interference row has no comparison or skip reason.", kind, "Compare short-only, long-only, and mixed traffic, or explain why the workload does not need the test."))
    elif kind == "tuning_delta":
        changed = has_text(row, "changed_variable", "variable") or has_any_metric(metrics, ("previous_value", "new_value"))
        if not changed and not has_text(row, "no_tuning_reason", "skip_reason"):
            findings.append(finding("hold", owner, "Tuning row has no one-variable change or no-tuning reason.", kind, "Record the exact scheduler/cache/concurrency variable changed, before value, and after value."))
        if changed and not (has_any_metric(metrics, ("p95_ttft_delta_ms", "tpot_delta_ms", "throughput_delta", "memory_delta_mb")) or has_text(row, "decision")):
            findings.append(finding("hold", owner, "Tuning row has no measured effect.", kind, "Add latency, throughput, memory, quality, or keep/revert decision."))
    elif kind == "capacity_event":
        capacity_names = ("preemptions", "oom_count", "queue_timeouts", "rejections", "rate_limited", "errors")
        if not has_any_metric(metrics, capacity_names) and not has_text(row, "none_seen", "capacity_event", "decision", "skip_reason"):
            findings.append(finding("hold", owner, "Capacity row has no event evidence or none-seen statement.", kind, "Record preemption, OOM, queue timeout, rejection, or explicit none-seen evidence."))
    elif kind == "decision_card":
        if not (metric_value(metrics, "bottleneck") or has_text(row, "bottleneck", "mechanism")):
            findings.append(finding("hold", owner, "Decision card has no bottleneck.", kind, "Name cold load, prefill, decode, KV cache, queue, scheduler, client, or unknown."))
        if not (metric_value(metrics, "retest_trigger") or has_text(row, "retest_trigger")):
            findings.append(finding("hold", owner, "Decision card has no retest trigger.", kind, "Write what change invalidates the decision: model, context, runtime, driver, traffic mix, or hardware."))
        if not (metric_value(metrics, "long_prompt_policy") or has_text(row, "policy", "decision")):
            findings.append(finding("hold", owner, "Decision card has no policy decision.", kind, "State queue, concurrency, long-prompt, cache, deployment, or rollback policy."))


def evaluate_row(row: dict[str, Any], vault_root: Path) -> dict[str, Any]:
    row_id = str(row.get("row_id") or row.get("id") or row.get("name") or "")
    kind = str(row.get("kind") or row.get("type") or "unspecified").strip().lower().replace(" ", "_")
    required = bool_value(row.get("required"), True)
    critical = bool_value(row.get("critical"), kind in DEFAULT_REQUIRED_KINDS)
    declared_status = status_value(row.get("status"))
    proof = str(row.get("proof") or row.get("proof_path") or row.get("artifact") or row.get("evidence_path") or "")
    mechanism = str(row.get("mechanism") or row.get("suspected_mechanism") or "")
    pass_signal = str(row.get("pass_signal") or KIND_HINTS.get(kind, {}).get("pass_signal", "Evidence row is complete enough to support the scheduler claim."))
    waiver_reason = str(row.get("waiver_reason") or row.get("skip_reason") or "")
    findings: list[dict[str, str]] = []

    if not row_id:
        findings.append(finding("hold", kind, "Evidence row id is missing.", str(row), "Give every row a stable id before auditing."))

    if kind not in KIND_HINTS:
        findings.append(finding("hold", kind, "Evidence kind is not recognized.", kind, "Use one of the required scheduler evidence kinds or add a waiver reason."))

    if not required:
        if not waiver_reason:
            findings.append(finding("hold", kind, "Optional or out-of-scope row has no waiver reason.", row_id, "Record why this evidence kind is not required for this run."))
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
            "mechanism": mechanism,
            "proof": proof,
            "proof_resolved": "",
            "proof_exists": False,
            "pass_signal": pass_signal,
            "next_route": route_for_row(row, kind),
            "next_action": findings[0]["action"] if findings else "Keep waiver with reason in the run note.",
            "findings": findings,
        }

    if declared_status == "fail":
        findings.append(finding("fail", kind, "Evidence row is explicitly marked fail.", row_id, "Resolve the failed scheduler evidence before using this decision."))
    elif declared_status != "pass":
        findings.append(finding("hold", kind, "Evidence row is not marked pass.", declared_status, "Complete the evidence route and set status to pass only after the pass signal is met."))

    exists = False
    proof_resolved = ""
    if proof:
        exists, proof_resolved = proof_exists(vault_root, proof)
        if not exists:
            findings.append(finding("hold", kind, "Proof link or path does not resolve in the vault.", proof_resolved, "Fix the proof path or create the linked evidence artifact."))
    else:
        findings.append(finding("hold", kind, "Required evidence row has no proof link or path.", row_id, "Add a proof link to the manifest, capstone note, or benchmark row."))

    evaluate_kind_requirements(row, kind, findings)

    if not pass_signal:
        findings.append(finding("hold", kind, "Row has no explicit pass signal.", row_id, "Write the observable evidence condition that makes this row pass."))

    if critical and declared_status == "pass" and not proof:
        findings.append(finding("fail", kind, "Critical row is marked pass without proof.", row_id, "A critical scheduler claim needs linked evidence, not only status text."))

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
        "mechanism": mechanism,
        "proof": proof,
        "proof_resolved": proof_resolved,
        "proof_exists": exists,
        "pass_signal": pass_signal,
        "next_route": route_for_row(row, kind),
        "next_action": findings[0]["action"] if findings else "Keep this evidence linked in the scheduler decision card.",
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
        "mechanism": "",
        "proof": "",
        "proof_resolved": "",
        "proof_exists": False,
        "pass_signal": hint.get("pass_signal", f"Manifest includes at least one {kind} row."),
        "next_route": hint.get("next_route", "LLM/Study/Local LLM Serving Internals and Scheduler Lab"),
        "next_action": f"Add one {kind} evidence row to the scheduler audit manifest.",
        "findings": [finding("hold", kind, "Required scheduler evidence kind is missing from the manifest.", kind, f"Add one {kind} row or document a waiver.")],
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
        "mechanism",
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
        f"# Local LLM Scheduler Evidence Audit - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Runtime: `{record.get('runtime') or ''}`",
        f"- Model: `{record.get('model') or ''}`",
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
        "| Row | Kind | Critical | Status | Proof exists | Mechanism | Next route |",
        "|---|---|---:|---|---:|---|---|",
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
                md_cell(row["mechanism"]),
                md_cell(wiki_link(row["next_route"])),
            ])
            + " |"
        )
    lines.extend(["", "## Next Actions", ""])
    incomplete = [row for row in record["rows"] if row["status"] != "pass"]
    for row in incomplete:
        lines.append(f"- `{row['row_id']}` -> {wiki_link(row['next_route'])}: {row['next_action']}")
    if not incomplete:
        lines.append("- Scheduler evidence is ready to support a deployment, runtime, or tuning decision.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    manifest_path, manifest = load_manifest()
    vault_root = Path(manifest.get("vault_root") or os.environ.get("LOCAL_LLM_SCHEDULER_AUDIT_VAULT_ROOT") or manifest_path.parent).expanduser().resolve()
    run_id = str(manifest.get("run_id") or os.environ.get("LOCAL_LLM_SCHEDULER_AUDIT_RUN_ID") or f"{utc_stamp()}-{slug(manifest_path.stem)}")
    run_root_value = os.environ.get("LOCAL_LLM_SCHEDULER_AUDIT_RUN_ROOT") or manifest.get("run_root", "scheduler-evidence-audit-runs")
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

    evaluated = [evaluate_row(dict(row), vault_root) for row in rows]
    required_kinds = list_value(manifest.get("required_kinds")) or DEFAULT_REQUIRED_KINDS
    present_kinds = {row["kind"] for row in evaluated if row["required"]}
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
        decision = "scheduler_evidence_failed"
    elif hold_count or critical_gap_count:
        status = "hold"
        decision = "scheduler_evidence_incomplete"
    else:
        status = "pass"
        decision = "scheduler_evidence_ready"

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "manifest_path": str(manifest_path),
        "vault_root": str(vault_root),
        "runtime": str(manifest.get("runtime") or ""),
        "model": str(manifest.get("model") or ""),
        "workload": str(manifest.get("workload") or ""),
        "row_count": len(evaluated),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "critical_gap_count": critical_gap_count,
        "kinds": kind_summary(evaluated),
        "rows": evaluated,
        "outputs": {},
    }

    json_path = run_dir / f"{run_id}-scheduler-audit.json"
    markdown_path = run_dir / f"{run_id}-scheduler-audit.md"
    csv_path = run_dir / f"{run_id}-scheduler-audit.csv"
    jsonl_path = run_root / "scheduler-evidence-audit-runs.jsonl"
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
$env:LOCAL_LLM_SCHEDULER_AUDIT_MANIFEST = "D:\llm-runs\scheduler-audit\scheduler-audit-manifest.json"
$env:LOCAL_LLM_SCHEDULER_AUDIT_VAULT_ROOT = "D:\Vaults\PersonalKB"
$env:LOCAL_LLM_SCHEDULER_AUDIT_RUN_ROOT = "D:\llm-runs\scheduler-audit"
python .\scheduler-evidence-audit-runner.py
```

## Reading The Result

| Runner status | Meaning | Next route |
|---|---|---|
| `pass/scheduler_evidence_ready` | every required scheduler evidence kind is pass and critical proof links resolve | use the decision in [[LLM/Study/LLM Deployment Decision Matrix]] or the capstone note |
| `hold/scheduler_evidence_incomplete` | required evidence, proof link, mechanism, timing, policy, or retest trigger is missing | follow each row's `next_route` |
| `fail/scheduler_evidence_failed` | a row is explicitly failed, unsafe, rejected, or a critical pass has no proof | fix the failed row before changing serving policy |

This runner can validate the evidence bundle, not the service itself. Use the actual concurrency, observability, prompt-cache, benchmark, quality, and security runners for live measurements.

## Capstone Row

| Gate | Required artifact | Pass signal |
|---|---|---|
| Scheduler evidence audit | `<run-id>-scheduler-audit.json`, `<run-id>-scheduler-audit.md`, `<run-id>-scheduler-audit.csv`, and one `scheduler-evidence-audit-runs.jsonl` row | required scheduler kinds pass or have explicit waivers, proof links resolve, and the decision card names bottleneck, policy, next route, and retest trigger |

## Completion Gate

- [ ] the manifest includes hypothesis, latency phase, scheduler state, long-prompt interference, tuning delta, capacity event, and decision card rows, or explicit waivers
- [ ] critical rows cannot pass without proof
- [ ] scheduler-state gaps say "not exposed" with a runtime/version reason instead of guessing
- [ ] the decision card names bottleneck, concurrency/queue policy, long-prompt policy, cache decision, next route, and retest trigger
- [ ] outputs are linked from [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]

## References

- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/LLM Inference Request Lifecycle Runner]]
- [[LLM/Study/Local LLM Observability and Operations Runner]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
