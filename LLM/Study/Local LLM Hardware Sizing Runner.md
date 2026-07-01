---
tags: [study, llm, inference, local-llm, hardware, sizing, memory, kv-cache, quantization, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM Hardware Sizing Runner

> **One-line summary** A local model fits only when weight memory, KV-cache memory, runtime overhead, active sequences, context length, and real hardware headroom fit the selected serving path.

Use this after [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]] when the arithmetic should become saved JSON, Markdown, CSV, and JSONL evidence. Use [[LLM/Study/Local LLM KV Cache Sizing Runner|Local LLM KV Cache Sizing Runner]] first when GQA/MQA attention geometry, long context, active sequences, or cache precision should produce a head-aware `kv_cache_gb` estimate. Use this hardware runner before [[LLM/Study/Local LLM Model Selection Runner|Local LLM Model Selection Runner]], [[LLM/Study/Local LLM First Model Pull Gate|Local LLM First Model Pull Gate]], [[LLM/Study/Local LLM Quantization and GPU Offload Lab|Local LLM Quantization and GPU Offload Lab]], [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]], and [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab|Local LLM Concurrency and Batch Throughput Lab]].

This runner does not scrape model pages or recommend current model names. Model files, quantized derivatives, and runtime support change. Put source-checked model facts into the manifest, then let the runner apply the same memory gates every time. When the model uses GQA or MQA, prefer importing `kv_cache_gb` from [[LLM/Study/Local LLM KV Cache Sizing Runner|Local LLM KV Cache Sizing Runner]] instead of relying only on the simplified hidden-size formula.

## What This Proves

| Gate | Evidence checked | Why it matters |
|---|---|---|
| Weight memory | parameter count, bytes per parameter, or explicit weight memory | prevents parameter-count-only guesses |
| KV cache | layers, hidden size, context target, active sequences, precision, or explicit KV memory | connects the academic KV-cache formula to local OOM risk |
| Runtime overhead | runtime buffers, CUDA graphs, metadata, extra buffers, and reserve | prevents "barely loads" from becoming "ready to serve" |
| Hardware budget | available VRAM, reserved headroom, optional RAM fallback | separates theoretical fit from this machine's fit |
| Route | pass, hold, fail, next route, and next action | decides whether to shortlist, reduce context, quantize, offload, or reject |

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "rtx3080ti-first-fit",
  "run_root": "D:/llm-runs/hardware-sizing",
  "vault_root": "D:/Vaults/PersonalKB",
  "hardware": {
    "gpu": "RTX 3080 Ti",
    "available_vram_gb": 9.5,
    "system_ram_gb": 64,
    "reserved_headroom_gb": 2
  },
  "workload": {
    "context_target_tokens": 4096,
    "active_sequences": 1,
    "latency_target": "interactive",
    "runtime": "Ollama"
  },
  "candidates": [
    {
      "candidate_id": "baseline-small",
      "parameter_count_b": 8,
      "bytes_per_parameter": 0.5,
      "layers": 32,
      "hidden_size": 4096,
      "kv_bytes_per_element": 2,
      "runtime_overhead_gb": 1,
      "extra_buffers_gb": 0.5,
      "offload": "gpu",
      "source": "model card or local tag checked on 2026-06-15",
      "next_route": "LLM/Study/Local LLM Model Selection Runner"
    }
  ]
}
```

`weight_memory_gb` and `kv_cache_gb` may be supplied directly when a model card, runtime probe, [[LLM/Study/Local LLM KV Cache Sizing Runner|KV-cache sizing output]], or prior benchmark gives better numbers than the simplified formulas.

## Standard-Library Runner

Save the code block as `local_llm_hardware_sizing_runner.py` or extract it directly from this note.

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


DEFAULT_MAX_UTILIZATION = 0.85


def utc_iso() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def slug(value: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return text or "local-llm-hardware-sizing"


def load_manifest() -> tuple[Path, dict[str, Any]]:
    raw_path = os.environ.get("LOCAL_LLM_HARDWARE_SIZING_MANIFEST")
    if len(sys.argv) > 1:
        raw_path = sys.argv[1]
    if not raw_path:
        raise ValueError("Set LOCAL_LLM_HARDWARE_SIZING_MANIFEST or pass a manifest path.")
    path = Path(raw_path).expanduser().resolve()
    return path, json.loads(path.read_text(encoding="utf-8"))


def list_value(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def number(value: Any, default: float | None = None) -> float | None:
    if value is None or value == "":
        return default
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def text(value: Any) -> str:
    return str(value or "").strip()


def bool_value(value: Any, default: bool = False) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def gb(value: float | None) -> float | None:
    if value is None:
        return None
    return round(value, 3)


def wiki_link(route: str) -> str:
    route = text(route)
    if not route:
        return "[[LLM/Study/Local LLM Model and Hardware Sizing Guide]]"
    if route.startswith("[["):
        return route
    return "[" + "[" + route.removesuffix(".md") + "]" + "]"


def csv_cell(value: Any) -> str:
    if isinstance(value, list):
        return ";".join(str(item) for item in value)
    if value is None:
        return ""
    return str(value)


def md_cell(value: Any) -> str:
    return csv_cell(value).replace("|", "\\|").replace("\n", " ")


def finding(level: str, owner: str, text_value: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "owner": owner,
        "finding": text_value,
        "evidence": evidence,
        "action": action,
    }


def candidate_context(candidate: dict[str, Any], workload: dict[str, Any]) -> int | None:
    return int(number(candidate.get("context_target_tokens"), number(workload.get("context_target_tokens"), None)) or 0) or None


def candidate_sequences(candidate: dict[str, Any], workload: dict[str, Any]) -> int | None:
    return int(number(candidate.get("active_sequences"), number(workload.get("active_sequences"), 1)) or 0) or None


def weight_memory(candidate: dict[str, Any]) -> tuple[float | None, str]:
    explicit = number(candidate.get("weight_memory_gb"), number(candidate.get("model_weight_memory_gb"), None))
    if explicit is not None:
        return explicit, "explicit weight_memory_gb"
    parameter_count_b = number(candidate.get("parameter_count_b"), None)
    bytes_per_parameter = number(candidate.get("bytes_per_parameter"), None)
    if parameter_count_b is None or bytes_per_parameter is None:
        return None, "missing parameter_count_b or bytes_per_parameter"
    return parameter_count_b * bytes_per_parameter, "parameter_count_b * bytes_per_parameter"


def kv_cache_memory(candidate: dict[str, Any], workload: dict[str, Any]) -> tuple[float | None, str]:
    explicit = number(candidate.get("kv_cache_gb"), number(candidate.get("kv_cache_memory_gb"), None))
    if explicit is not None:
        return explicit, "explicit kv_cache_gb"
    layers = number(candidate.get("layers"), None)
    hidden_size = number(candidate.get("hidden_size"), None)
    kv_bytes = number(candidate.get("kv_bytes_per_element"), None)
    context_tokens = candidate_context(candidate, workload)
    sequences = candidate_sequences(candidate, workload)
    if None in {layers, hidden_size, kv_bytes, context_tokens, sequences}:
        return None, "missing layers, hidden_size, kv_bytes_per_element, context_target_tokens, or active_sequences"
    raw_bytes = 2 * layers * context_tokens * hidden_size * kv_bytes * sequences
    return raw_bytes / (1024**3), "2 * layers * context * hidden_size * bytes * active_sequences"


def hardware_budget(hardware: dict[str, Any], candidate: dict[str, Any]) -> tuple[float | None, str]:
    offload = text(candidate.get("offload") or "gpu").lower()
    if offload in {"cpu", "system_ram", "ram"}:
        system_ram = number(hardware.get("system_ram_gb"), None)
        reserve = number(hardware.get("reserved_system_ram_gb"), number(hardware.get("reserved_headroom_gb"), 4))
        if system_ram is None:
            return None, "missing system_ram_gb"
        return max(system_ram - (reserve or 0), 0), "system_ram_gb - reserved_system_ram_gb"
    available_vram = number(hardware.get("available_vram_gb"), number(hardware.get("vram_gb"), None))
    reserve = number(hardware.get("reserved_headroom_gb"), 0) or 0
    if available_vram is None:
        return None, "missing available_vram_gb"
    return max(available_vram - reserve, 0), "available_vram_gb - reserved_headroom_gb"


def route_for_candidate(candidate: dict[str, Any], status: str) -> str:
    route = text(candidate.get("next_route"))
    if route:
        return route
    if status == "pass":
        return "LLM/Study/Local LLM Model Selection Runner"
    if status == "fail":
        return "LLM/Study/Local LLM Quantization and GPU Offload Lab"
    return "LLM/Study/Local LLM Model and Hardware Sizing Guide"


def evaluate_candidate(candidate: dict[str, Any], hardware: dict[str, Any], workload: dict[str, Any], max_utilization: float) -> dict[str, Any]:
    candidate_id = text(candidate.get("candidate_id") or candidate.get("id") or candidate.get("name"))
    source = text(candidate.get("source"))
    offload = text(candidate.get("offload") or "gpu").lower()
    runtime_overhead_gb = number(candidate.get("runtime_overhead_gb"), 0) or 0
    extra_buffers_gb = number(candidate.get("extra_buffers_gb"), 0) or 0
    context_tokens = candidate_context(candidate, workload)
    sequences = candidate_sequences(candidate, workload)
    findings: list[dict[str, str]] = []

    if not candidate_id:
        findings.append(finding("hold", "candidate", "Candidate id is missing.", str(candidate), "Give every row a stable candidate_id."))
        candidate_id = "unnamed-candidate"
    if not source:
        findings.append(finding("hold", candidate_id, "Candidate source is missing.", candidate_id, "Record the model card, registry URL, local tag, or measured artifact source."))
    if not text(candidate.get("next_route")):
        findings.append(finding("hold", candidate_id, "Next route is missing.", candidate_id, "Add the next evidence route before using this result in the capstone ledger."))

    weight_gb, weight_method = weight_memory(candidate)
    kv_gb, kv_method = kv_cache_memory(candidate, workload)
    if weight_gb is None:
        findings.append(finding("hold", candidate_id, "Weight memory cannot be computed.", weight_method, "Supply weight_memory_gb or parameter_count_b and bytes_per_parameter."))
    if kv_gb is None:
        findings.append(finding("hold", candidate_id, "KV-cache memory cannot be computed.", kv_method, "Supply kv_cache_gb or layers, hidden_size, kv_bytes_per_element, context_target_tokens, and active_sequences."))

    budget_gb, budget_method = hardware_budget(hardware, candidate)
    if budget_gb is None:
        findings.append(finding("hold", candidate_id, "Hardware budget cannot be computed.", budget_method, "Supply available_vram_gb for GPU fit or system_ram_gb for CPU fit."))

    required_gb = None
    safe_limit_gb = None
    margin_gb = None
    margin_percent = None
    if weight_gb is not None and kv_gb is not None:
        required_gb = weight_gb + kv_gb + runtime_overhead_gb + extra_buffers_gb
    if budget_gb is not None:
        safe_limit_gb = budget_gb * max_utilization
    if required_gb is not None and budget_gb is not None:
        margin_gb = budget_gb - required_gb
        margin_percent = (margin_gb / budget_gb * 100) if budget_gb else None

    cpu_fallback_allowed = bool_value(candidate.get("cpu_fallback_allowed"), False)
    offload_fallback_allowed = bool_value(candidate.get("offload_fallback_allowed"), False)
    fallback_allowed = cpu_fallback_allowed or offload_fallback_allowed or offload in {"mixed", "partial"}

    if required_gb is not None and budget_gb is not None and safe_limit_gb is not None:
        if required_gb <= safe_limit_gb:
            pass
        elif required_gb <= budget_gb:
            findings.append(finding(
                "hold",
                candidate_id,
                "Candidate fits only with thin headroom.",
                f"required={gb(required_gb)} budget={gb(budget_gb)} safe_limit={gb(safe_limit_gb)}",
                "Reduce context, reduce active sequences, measure runtime overhead, or benchmark before treating this as ready.",
            ))
        elif fallback_allowed:
            findings.append(finding(
                "hold",
                candidate_id,
                "Candidate exceeds the primary hardware budget but declares a fallback path.",
                f"required={gb(required_gb)} budget={gb(budget_gb)} offload={offload}",
                "Route to quantization/offload or CPU fallback evidence before pulling or serving.",
            ))
        else:
            findings.append(finding(
                "fail",
                candidate_id,
                "Candidate exceeds the hardware budget.",
                f"required={gb(required_gb)} budget={gb(budget_gb)} margin={gb(margin_gb)}",
                "Reject this candidate for the current hardware, or reduce model size, context, concurrency, precision, or runtime overhead.",
            ))

    if offload in {"cpu", "system_ram", "ram"} and text(workload.get("latency_target")).lower() == "interactive":
        findings.append(finding(
            "hold",
            candidate_id,
            "CPU fallback needs latency evidence for an interactive workload.",
            "offload=cpu latency_target=interactive",
            "Benchmark before accepting this candidate for interactive use.",
        ))

    fail_count = sum(1 for item in findings if item["level"] == "fail")
    hold_count = sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        status = "fail"
        decision = "candidate_does_not_fit"
    elif hold_count:
        status = "hold"
        decision = "candidate_needs_sizing_evidence"
    else:
        status = "pass"
        decision = "candidate_fits_with_headroom"

    next_route = route_for_candidate(candidate, status)
    return {
        "candidate_id": candidate_id,
        "status": status,
        "decision": decision,
        "source": source,
        "offload": offload,
        "context_target_tokens": context_tokens,
        "active_sequences": sequences,
        "weight_memory_gb": gb(weight_gb),
        "weight_method": weight_method,
        "kv_cache_gb": gb(kv_gb),
        "kv_method": kv_method,
        "runtime_overhead_gb": gb(runtime_overhead_gb),
        "extra_buffers_gb": gb(extra_buffers_gb),
        "required_memory_gb": gb(required_gb),
        "budget_gb": gb(budget_gb),
        "budget_method": budget_method,
        "safe_limit_gb": gb(safe_limit_gb),
        "margin_gb": gb(margin_gb),
        "margin_percent": gb(margin_percent),
        "next_route": next_route,
        "next_action": findings[0]["action"] if findings else "Use this candidate in the model selection runner before pulling or serving.",
        "findings": findings,
    }


def csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "candidate_id",
        "status",
        "decision",
        "source",
        "offload",
        "context_target_tokens",
        "active_sequences",
        "weight_memory_gb",
        "kv_cache_gb",
        "runtime_overhead_gb",
        "extra_buffers_gb",
        "required_memory_gb",
        "budget_gb",
        "safe_limit_gb",
        "margin_gb",
        "margin_percent",
        "next_route",
        "next_action",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: csv_cell(row.get(field)) for field in fields})


def render_markdown(record: dict[str, Any]) -> str:
    lines = [
        f"# Local LLM Hardware Sizing - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Hardware: `{record['hardware_summary']}`",
        f"- Workload: `{record['workload_summary']}`",
        f"- Candidates: `{record['candidate_count']}`",
        f"- Pass/Hold/Fail: `{record['pass_count']}` / `{record['hold_count']}` / `{record['fail_count']}`",
        "",
        "## Formula",
        "",
        "```text",
        "required memory = weight memory + KV-cache memory + runtime overhead + extra buffers",
        "KV cache ~= 2 * layers * context tokens * hidden size * bytes per element * active sequences",
        "safe limit = (available hardware memory - reserved headroom) * max utilization",
        "```",
        "",
        "## Candidate Results",
        "",
        "| Candidate | Status | Required GB | Safe limit GB | Margin GB | Context | Sequences | Next route |",
        "|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for row in record["candidates"]:
        lines.append(
            "| "
            + " | ".join([
                md_cell(row["candidate_id"]),
                md_cell(row["status"]),
                md_cell(row["required_memory_gb"]),
                md_cell(row["safe_limit_gb"]),
                md_cell(row["margin_gb"]),
                md_cell(row["context_target_tokens"]),
                md_cell(row["active_sequences"]),
                md_cell(wiki_link(row["next_route"])),
            ])
            + " |"
        )
    lines.extend([
        "",
        "## Next Actions",
        "",
    ])
    for row in record["candidates"]:
        lines.append(f"- `{row['candidate_id']}` -> {wiki_link(row['next_route'])}: {row['next_action']}")
    lines.append("")
    return "\n".join(lines)


def hardware_summary(hardware: dict[str, Any]) -> str:
    gpu = text(hardware.get("gpu") or hardware.get("device") or "unspecified")
    vram = text(hardware.get("available_vram_gb") or hardware.get("vram_gb") or "unknown")
    ram = text(hardware.get("system_ram_gb") or "unknown")
    return f"{gpu}; available_vram_gb={vram}; system_ram_gb={ram}"


def workload_summary(workload: dict[str, Any]) -> str:
    context = text(workload.get("context_target_tokens") or "unknown")
    sequences = text(workload.get("active_sequences") or "1")
    runtime = text(workload.get("runtime") or "unspecified")
    latency = text(workload.get("latency_target") or "unspecified")
    return f"context={context}; active_sequences={sequences}; runtime={runtime}; latency={latency}"


def main() -> int:
    manifest_path, manifest = load_manifest()
    hardware = manifest.get("hardware") or {}
    workload = manifest.get("workload") or {}
    if not isinstance(hardware, dict):
        raise ValueError("Manifest hardware must be an object.")
    if not isinstance(workload, dict):
        raise ValueError("Manifest workload must be an object.")

    candidates = manifest.get("candidates", manifest.get("rows"))
    if not isinstance(candidates, list) or not all(isinstance(row, dict) for row in candidates):
        raise ValueError("Manifest candidates or rows must be a list of objects.")

    run_id = str(manifest.get("run_id") or os.environ.get("LOCAL_LLM_HARDWARE_SIZING_RUN_ID") or f"{utc_stamp()}-{slug(manifest_path.stem)}")
    run_root_value = os.environ.get("LOCAL_LLM_HARDWARE_SIZING_RUN_ROOT") or manifest.get("run_root", "local-llm-hardware-sizing-runs")
    run_root = Path(str(run_root_value)).expanduser()
    if not run_root.is_absolute():
        run_root = manifest_path.parent / run_root
    run_root = run_root.resolve()
    run_dir = run_root / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    max_utilization = number(manifest.get("max_utilization"), DEFAULT_MAX_UTILIZATION) or DEFAULT_MAX_UTILIZATION
    max_utilization = min(max(max_utilization, 0.1), 1.0)

    evaluated = [evaluate_candidate(dict(candidate), hardware, workload, max_utilization) for candidate in candidates]
    pass_count = sum(1 for row in evaluated if row["status"] == "pass")
    hold_count = sum(1 for row in evaluated if row["status"] == "hold")
    fail_count = sum(1 for row in evaluated if row["status"] == "fail")

    if pass_count:
        status = "pass"
        decision = "hardware_sizing_ready"
    elif hold_count:
        status = "hold"
        decision = "hardware_sizing_incomplete"
    else:
        status = "fail"
        decision = "hardware_sizing_failed"

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "manifest_path": str(manifest_path),
        "vault_root": str(Path(str(manifest.get("vault_root") or os.environ.get("LOCAL_LLM_HARDWARE_SIZING_VAULT_ROOT") or manifest_path.parent)).expanduser()),
        "run_root": str(run_root),
        "hardware_summary": hardware_summary(hardware),
        "workload_summary": workload_summary(workload),
        "max_utilization": max_utilization,
        "candidate_count": len(evaluated),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "candidates": evaluated,
        "outputs": {},
    }

    json_path = run_dir / f"{run_id}-hardware-sizing.json"
    markdown_path = run_dir / f"{run_id}-hardware-sizing.md"
    csv_path = run_dir / f"{run_id}-hardware-sizing.csv"
    jsonl_path = run_root / "local-llm-hardware-sizing-runs.jsonl"
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
        "candidate_count": len(evaluated),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "output_dir": str(run_dir),
    }, indent=2))
    return 0 if status == "pass" else 1 if status == "hold" else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(json.dumps({"status": "error", "decision": "runner_exception", "error": str(exc)}, indent=2), file=sys.stderr)
        raise
```

## PowerShell Run

```powershell
$env:LOCAL_LLM_HARDWARE_SIZING_MANIFEST = "D:\llm-runs\hardware-sizing\hardware-sizing-manifest.json"
$env:LOCAL_LLM_HARDWARE_SIZING_RUN_ROOT = "D:\llm-runs\hardware-sizing"
$env:LOCAL_LLM_HARDWARE_SIZING_VAULT_ROOT = "D:\Vaults\PersonalKB"
python .\local_llm_hardware_sizing_runner.py
```

## Reading The Result

| Runner status | Meaning | Next route |
|---|---|---|
| `pass/hardware_sizing_ready` | at least one candidate fits within the safe hardware limit with source and route evidence | [[LLM/Study/Local LLM Model Selection Runner]] |
| `hold/hardware_sizing_incomplete` | fields are missing, headroom is thin, or fallback/offload needs proof | [[LLM/Study/Local LLM Model and Hardware Sizing Guide]] or [[LLM/Study/Local LLM Quantization and GPU Offload Lab]] |
| `fail/hardware_sizing_failed` | every candidate exceeds the selected hardware budget without an accepted fallback | reduce model size, context, active sequences, precision, or runtime overhead |

A `pass` result says the candidate is worth shortlisting. It is not a license, compatibility, quality, or endpoint proof by itself.

## Capstone Row

| Evidence | Output |
|---|---|
| Hardware sizing runner | `<run-id>-hardware-sizing.json`, `<run-id>-hardware-sizing.md`, `<run-id>-hardware-sizing.csv`, and one `local-llm-hardware-sizing-runs.jsonl` row |

## Completion Gate

This runner is useful when:

- [ ] hardware budget uses measured or intentionally reserved available VRAM/RAM
- [ ] every candidate has source evidence and a next route
- [ ] weight memory is supplied or computed from parameter count and bytes per parameter
- [ ] KV-cache memory is supplied from a head-aware cache sizing output, measured runtime proof, or computed from layers, hidden size, context, precision, and active sequences
- [ ] runtime overhead and extra buffers are explicit, even if they are conservative estimates
- [ ] thin-headroom, fallback, and no-fit outcomes route to the next controlled evidence artifact
- [ ] output JSON, Markdown, CSV, and JSONL artifacts are saved before model pull or serving

## References

- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Workload to Model Selection Playbook]]
- [[LLM/Study/Local LLM KV Cache Sizing Runner]]
- [[LLM/Study/Local LLM Model Selection Runner]]
- [[LLM/Study/Local LLM First Model Pull Gate]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Lab]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/LLM Math and Tensor Shape Primer]]
- [[LLM/2022 — Alignment and Chat/Quantization]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
