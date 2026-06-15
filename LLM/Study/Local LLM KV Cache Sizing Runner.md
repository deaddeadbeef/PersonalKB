---
tags: [study, llm, inference, local-llm, kv-cache, memory, context, concurrency, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [core, deep-dive, practice]
last-verified: 2026-06-16
---

# Local LLM KV Cache Sizing Runner

> **One-line summary** Estimate KV-cache memory from the model's attention geometry before choosing context length, active sequences, runtime cache precision, or a local serving candidate.

Use this after [[LLM/Study/LLM Math and Tensor Shape Primer|LLM Math and Tensor Shape Primer]] or [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse|KV Cache and Context Reuse]] when the cache arithmetic needs to become saved evidence. Use [[LLM/Study/Local LLM Model Metadata Card Runner|Local LLM Model Metadata Card Runner]] first when layers, hidden size, attention heads, key/value heads, context length, or tokenizer limits still need to be extracted from `config.json`, tokenizer files, GGUF metadata, or Ollama show output. Use this before [[LLM/Study/Local LLM Hardware Sizing Runner|Local LLM Hardware Sizing Runner]], [[LLM/Study/Local LLM Model Selection Runner|Local LLM Model Selection Runner]], [[LLM/Study/Local LLM Context Window and Token Budgeting Runner|Local LLM Context Window and Token Budgeting Runner]], and [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner|Local LLM Concurrency and Batch Throughput Runner]] whenever context length, active sequences, or GQA/MQA cache savings might decide whether the model can run locally.

The simplified planning formula `2 * layers * sequence length * hidden size * bytes * active sequences` is exact enough only for multi-head attention when key/value heads match query heads. Modern local models often use grouped-query attention (GQA) or multi-query attention (MQA), so a defensible fit estimate should use `num_attention_heads` and `num_key_value_heads` when those fields are available from a model config, model card, runtime metadata, or source-checked local artifact.

## What This Proves

| Gate | Evidence checked | Why it matters |
|---|---|---|
| Attention geometry | layers, hidden size, attention heads, key/value heads, and head dimension | prevents over- or under-estimating GQA/MQA cache memory |
| Context and concurrency | prompt/output context target and active sequences | turns RAG, chat history, and batch plans into memory pressure |
| Cache precision | FP16/BF16/FP8/INT8/INT4 or explicit bytes per cache element | separates weight quantization from cache precision |
| Budget | KV-cache budget or leftover VRAM/RAM after weights and overhead | tells whether context or concurrency must shrink before serving |
| Source proof | model config/source row and optional cache-quantization proof | stops stale model-family guesses from becoming pull decisions |

Academic bridge: KV cache is not just "extra memory." It is the stored key/value state produced by attention layers during autoregressive inference. MHA, MQA, and GQA change the number of stored key/value heads; context length and active sequences multiply that storage; cache dtype changes bytes per element. Those variables are exactly the variables you control when hosting a local model.

## Head-Aware Formula

Use this when `hidden_size`, `num_attention_heads`, and `num_key_value_heads` are known:

```text
head_dim = hidden_size / num_attention_heads
KV cache bytes =
  layers
  * context tokens
  * active sequences
  * 2
  * num_key_value_heads
  * head_dim
  * bytes per cache element
```

The `2` is for keys and values. If `num_key_value_heads == num_attention_heads`, the model uses MHA and the formula collapses to the simplified hidden-size formula. If `num_key_value_heads == 1`, the model uses MQA. Values between those are GQA.

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "qwen-first-cache-fit",
  "run_root": "D:/llm-runs/kv-cache-sizing",
  "vault_root": "D:/Vaults/PersonalKB",
  "hardware": {
    "available_vram_gb": 9.5,
    "reserved_headroom_gb": 2.0
  },
  "workload": {
    "context_tokens": 8192,
    "active_sequences": 1,
    "kv_cache_budget_gb": 2.5,
    "runtime": "Ollama"
  },
  "candidates": [
    {
      "candidate_id": "source-checked-local-tag",
      "layers": 36,
      "hidden_size": 2560,
      "num_attention_heads": 20,
      "num_key_value_heads": 4,
      "cache_dtype": "fp16",
      "source": "model config, model card, or local metadata checked on 2026-06-16",
      "next_route": "LLM/Study/Local LLM Hardware Sizing Runner"
    }
  ]
}
```

If the exact cache size is measured by a runtime, supply `kv_cache_gb` directly. If the remaining hardware budget should be computed, provide `weight_memory_gb`, `runtime_overhead_gb`, and `extra_buffers_gb`; otherwise set `kv_cache_budget_gb` explicitly.

## Standard-Library Runner

Save this as `local_llm_kv_cache_sizing_runner.py` inside the run folder, or extract it from this note. It uses only Python's standard library.

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

DTYPE_BYTES = {
    "fp32": 4.0,
    "float32": 4.0,
    "f32": 4.0,
    "fp16": 2.0,
    "float16": 2.0,
    "f16": 2.0,
    "bf16": 2.0,
    "bfloat16": 2.0,
    "fp8": 1.0,
    "int8": 1.0,
    "q8": 1.0,
    "q8_0": 1.0,
    "int4": 0.5,
    "q4": 0.5,
    "q4_0": 0.5,
    "q4_k": 0.5,
}


def utc_iso() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def slug(value: str) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value or "").strip()).strip("-")
    return text or "local-llm-kv-cache-sizing"


def display(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def number(value: Any, default: float | None = None) -> float | None:
    if value is None or value == "":
        return default
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


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


def load_manifest() -> tuple[Path, dict[str, Any]]:
    raw_path = os.environ.get("LOCAL_LLM_KV_CACHE_SIZING_MANIFEST")
    if len(sys.argv) > 1:
        raw_path = sys.argv[1]
    if not raw_path:
        raise ValueError("Set LOCAL_LLM_KV_CACHE_SIZING_MANIFEST or pass a manifest path.")
    path = Path(raw_path).expanduser().resolve()
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Manifest must be a JSON object.")
    return path, data


def wiki_link(route: str) -> str:
    clean = display(route)
    if not clean:
        clean = "LLM/Study/Local LLM KV Cache Sizing Runner"
    open_link = "[" * 2
    close_link = "]" * 2
    if clean.startswith(open_link):
        return clean
    return open_link + clean.removesuffix(".md") + close_link


def md_cell(value: Any) -> str:
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=True)
    return display(value).replace("|", "\\|").replace("\n", " ")


def csv_cell(value: Any) -> str:
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=True, sort_keys=True)
    return "" if value is None else str(value)


def finding(level: str, owner: str, text_value: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "owner": owner,
        "finding": text_value,
        "evidence": evidence,
        "action": action,
    }


def dtype_bytes(candidate: dict[str, Any], workload: dict[str, Any]) -> tuple[float | None, str]:
    explicit = number(candidate.get("kv_bytes_per_element"), number(candidate.get("cache_bytes_per_element"), None))
    if explicit is not None:
        return explicit, "explicit bytes per cache element"
    dtype = display(candidate.get("cache_dtype") or candidate.get("kv_cache_dtype") or workload.get("cache_dtype") or workload.get("kv_cache_dtype") or "fp16").lower()
    if dtype in DTYPE_BYTES:
        return DTYPE_BYTES[dtype], dtype
    return None, f"unknown cache dtype: {dtype}"


def workload_int(candidate: dict[str, Any], workload: dict[str, Any], key: str, default: int | None = None) -> int | None:
    value = number(candidate.get(key), number(workload.get(key), default))
    if value is None or value <= 0:
        return None
    return int(value)


def attention_kind(attention_heads: int | None, kv_heads: int | None) -> str:
    if attention_heads is None or kv_heads is None:
        return "unknown"
    if kv_heads == attention_heads:
        return "mha"
    if kv_heads == 1:
        return "mqa"
    return "gqa"


def compute_kv_cache(candidate: dict[str, Any], workload: dict[str, Any]) -> tuple[float | None, dict[str, Any], list[dict[str, str]]]:
    findings: list[dict[str, str]] = []
    explicit = number(candidate.get("kv_cache_gb"), number(candidate.get("kv_cache_memory_gb"), None))
    if explicit is not None:
        return explicit, {"method": "explicit kv_cache_gb", "attention_kind": display(candidate.get("attention_kind") or "measured")}, findings

    candidate_id = display(candidate.get("candidate_id") or candidate.get("id") or "candidate")
    layers = workload_int(candidate, workload, "layers")
    hidden_size = workload_int(candidate, workload, "hidden_size")
    attention_heads = workload_int(candidate, workload, "num_attention_heads") or workload_int(candidate, workload, "attention_heads")
    kv_heads = workload_int(candidate, workload, "num_key_value_heads") or workload_int(candidate, workload, "kv_heads")
    context_tokens = workload_int(candidate, workload, "context_tokens") or workload_int(candidate, workload, "context_target_tokens")
    active_sequences = workload_int(candidate, workload, "active_sequences", 1)
    bytes_per_element, dtype_method = dtype_bytes(candidate, workload)

    for key, value, action in [
        ("layers", layers, "Record the model layer count from config, model card, or runtime metadata."),
        ("hidden_size", hidden_size, "Record hidden_size from config or metadata."),
        ("num_attention_heads", attention_heads, "Record num_attention_heads so head_dim can be computed."),
        ("num_key_value_heads", kv_heads, "Record num_key_value_heads; do not assume MHA for GQA/MQA models."),
        ("context_tokens", context_tokens, "Record the intended prompt plus output context budget."),
        ("active_sequences", active_sequences, "Record concurrent active sequences for this serving plan."),
        ("cache dtype bytes", bytes_per_element, "Record cache dtype or explicit kv_bytes_per_element."),
    ]:
        if value is None:
            findings.append(finding("hold", candidate_id, f"{key} is missing.", key, action))

    if findings:
        return None, {"method": "head-aware formula", "attention_kind": "unknown", "dtype_method": dtype_method}, findings

    assert layers is not None
    assert hidden_size is not None
    assert attention_heads is not None
    assert kv_heads is not None
    assert context_tokens is not None
    assert active_sequences is not None
    assert bytes_per_element is not None

    if hidden_size % attention_heads != 0:
        findings.append(finding(
            "fail",
            candidate_id,
            "hidden_size is not divisible by num_attention_heads.",
            f"hidden_size={hidden_size} num_attention_heads={attention_heads}",
            "Fix the architecture metadata before trusting the cache estimate.",
        ))
        return None, {"method": "head-aware formula", "attention_kind": "invalid", "dtype_method": dtype_method}, findings
    if kv_heads > attention_heads:
        findings.append(finding(
            "fail",
            candidate_id,
            "num_key_value_heads exceeds num_attention_heads.",
            f"kv_heads={kv_heads} attention_heads={attention_heads}",
            "Fix the architecture metadata before trusting the cache estimate.",
        ))
        return None, {"method": "head-aware formula", "attention_kind": "invalid", "dtype_method": dtype_method}, findings

    head_dim = hidden_size / attention_heads
    raw_bytes = layers * context_tokens * active_sequences * 2 * kv_heads * head_dim * bytes_per_element
    estimate_gb = raw_bytes / (1024**3)
    return estimate_gb, {
        "method": "layers * context * active_sequences * 2 * kv_heads * head_dim * bytes",
        "attention_kind": attention_kind(attention_heads, kv_heads),
        "layers": layers,
        "hidden_size": hidden_size,
        "num_attention_heads": attention_heads,
        "num_key_value_heads": kv_heads,
        "head_dim": head_dim,
        "context_tokens": context_tokens,
        "active_sequences": active_sequences,
        "bytes_per_element": bytes_per_element,
        "dtype_method": dtype_method,
    }, findings


def budget_for_candidate(candidate: dict[str, Any], hardware: dict[str, Any], workload: dict[str, Any]) -> tuple[float | None, str]:
    explicit = number(candidate.get("kv_cache_budget_gb"), number(workload.get("kv_cache_budget_gb"), None))
    if explicit is not None:
        return explicit, "explicit kv_cache_budget_gb"

    available = number(candidate.get("available_vram_gb"), number(hardware.get("available_vram_gb"), number(hardware.get("vram_gb"), None)))
    reserve = number(candidate.get("reserved_headroom_gb"), number(hardware.get("reserved_headroom_gb"), 0)) or 0
    weight = number(candidate.get("weight_memory_gb"), None)
    runtime_overhead = number(candidate.get("runtime_overhead_gb"), 0) or 0
    extra_buffers = number(candidate.get("extra_buffers_gb"), 0) or 0
    if available is None:
        return None, "missing available_vram_gb or kv_cache_budget_gb"
    if weight is None:
        return None, "missing weight_memory_gb for leftover-budget mode"
    return max(available - reserve - weight - runtime_overhead - extra_buffers, 0), "available_vram - reserve - weights - runtime_overhead - extra_buffers"


def evaluate_candidate(candidate: dict[str, Any], hardware: dict[str, Any], workload: dict[str, Any], max_utilization: float) -> dict[str, Any]:
    candidate_id = display(candidate.get("candidate_id") or candidate.get("id") or candidate.get("name") or "unnamed-candidate")
    source = display(candidate.get("source"))
    next_route = display(candidate.get("next_route") or "LLM/Study/Local LLM Hardware Sizing Runner")
    findings: list[dict[str, str]] = []

    if not source:
        findings.append(finding("hold", candidate_id, "Candidate source is missing.", candidate_id, "Link the model config, model card, local metadata, or measured runtime row."))

    kv_cache_gb, geometry, geometry_findings = compute_kv_cache(candidate, workload)
    findings.extend(geometry_findings)
    budget_gb, budget_method = budget_for_candidate(candidate, hardware, workload)
    if budget_gb is None:
        findings.append(finding("hold", candidate_id, "KV-cache budget cannot be computed.", budget_method, "Supply kv_cache_budget_gb or available_vram_gb plus weight_memory_gb."))

    dtype_method = display(geometry.get("dtype_method"))
    quantized_cache = dtype_method in {"fp8", "int8", "q8", "q8_0", "int4", "q4", "q4_0", "q4_k"} or (number(candidate.get("kv_bytes_per_element"), None) is not None and (number(candidate.get("kv_bytes_per_element"), 2) or 2) < 2)
    if quantized_cache and not (bool_value(candidate.get("cache_quantization_supported")) or display(candidate.get("cache_quantization_proof"))):
        findings.append(finding(
            "hold",
            candidate_id,
            "Quantized KV cache is assumed without runtime proof.",
            dtype_method,
            "Link runtime docs, command output, or benchmark evidence for the selected cache dtype before treating the fit as ready.",
        ))

    safe_limit_gb = budget_gb * max_utilization if budget_gb is not None else None
    margin_gb = budget_gb - kv_cache_gb if budget_gb is not None and kv_cache_gb is not None else None
    margin_percent = (margin_gb / budget_gb * 100) if budget_gb and margin_gb is not None else None

    if kv_cache_gb is not None and budget_gb is not None and safe_limit_gb is not None:
        if kv_cache_gb <= safe_limit_gb:
            pass
        elif kv_cache_gb <= budget_gb:
            findings.append(finding(
                "hold",
                candidate_id,
                "KV cache fits only with thin headroom.",
                f"kv_cache_gb={gb(kv_cache_gb)} budget_gb={gb(budget_gb)} safe_limit_gb={gb(safe_limit_gb)}",
                "Reduce context, reduce active sequences, or reserve more memory before serving.",
            ))
        else:
            findings.append(finding(
                "fail",
                candidate_id,
                "KV cache exceeds the selected budget.",
                f"kv_cache_gb={gb(kv_cache_gb)} budget_gb={gb(budget_gb)} margin_gb={gb(margin_gb)}",
                "Reduce context, reduce active sequences, choose a model with fewer KV heads, use proven cache quantization, or reject this serving shape.",
            ))

    fail_count = sum(1 for item in findings if item["level"] == "fail")
    hold_count = sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        status = "fail"
        decision = "kv_cache_does_not_fit"
    elif hold_count:
        status = "hold"
        decision = "kv_cache_sizing_incomplete"
    else:
        status = "pass"
        decision = "kv_cache_fits_with_headroom"

    return {
        "candidate_id": candidate_id,
        "status": status,
        "decision": decision,
        "source": source,
        "attention_kind": geometry.get("attention_kind", "unknown"),
        "kv_cache_gb": gb(kv_cache_gb),
        "budget_gb": gb(budget_gb),
        "safe_limit_gb": gb(safe_limit_gb),
        "margin_gb": gb(margin_gb),
        "margin_percent": gb(margin_percent),
        "budget_method": budget_method,
        "geometry": geometry,
        "next_route": next_route,
        "next_action": findings[0]["action"] if findings else "Use this cache estimate in the hardware sizing runner, model selection runner, or context/concurrency gate.",
        "findings": findings,
    }


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "candidate_id",
        "status",
        "decision",
        "source",
        "attention_kind",
        "kv_cache_gb",
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
        f"# Local LLM KV Cache Sizing - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Candidate count: `{record['candidate_count']}`",
        f"- Pass/Hold/Fail: `{record['pass_count']}` / `{record['hold_count']}` / `{record['fail_count']}`",
        "",
        "## Formula",
        "",
        "```text",
        "head_dim = hidden_size / num_attention_heads",
        "KV cache = layers * context * active_sequences * 2 * num_key_value_heads * head_dim * bytes_per_element",
        "safe limit = kv_cache_budget_gb * max_utilization",
        "```",
        "",
        "## Candidate Results",
        "",
        "| Candidate | Status | Attention | KV GB | Safe limit GB | Margin GB | Next route |",
        "|---|---|---|---:|---:|---:|---|",
    ]
    for row in record["candidates"]:
        lines.append("| " + " | ".join([
            md_cell(row["candidate_id"]),
            md_cell(row["status"]),
            md_cell(row["attention_kind"]),
            md_cell(row["kv_cache_gb"]),
            md_cell(row["safe_limit_gb"]),
            md_cell(row["margin_gb"]),
            md_cell(wiki_link(row["next_route"])),
        ]) + " |")
    lines.extend(["", "## Findings", ""])
    all_findings = [item for row in record["candidates"] for item in row["findings"]]
    if not all_findings:
        lines.append("- No blocking findings.")
    else:
        for item in all_findings:
            lines.append(f"- `{item['level']}` `{item['owner']}`: {item['finding']} -> {item['action']}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    manifest_path, manifest = load_manifest()
    hardware = manifest.get("hardware") or {}
    workload = manifest.get("workload") or {}
    candidates = manifest.get("candidates") or manifest.get("rows")
    if not isinstance(hardware, dict):
        raise ValueError("Manifest hardware must be an object.")
    if not isinstance(workload, dict):
        raise ValueError("Manifest workload must be an object.")
    if not isinstance(candidates, list) or not all(isinstance(row, dict) for row in candidates):
        raise ValueError("Manifest candidates or rows must be a list of objects.")

    run_id = display(manifest.get("run_id") or os.environ.get("LOCAL_LLM_KV_CACHE_SIZING_RUN_ID") or f"{utc_stamp()}-{slug(manifest_path.stem)}")
    run_root_value = os.environ.get("LOCAL_LLM_KV_CACHE_SIZING_RUN_ROOT") or manifest.get("run_root", "local-llm-kv-cache-sizing-runs")
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
        decision = "kv_cache_sizing_ready"
    elif hold_count:
        status = "hold"
        decision = "kv_cache_sizing_incomplete"
    else:
        status = "fail"
        decision = "kv_cache_sizing_failed"

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "manifest_path": str(manifest_path),
        "vault_root": display(manifest.get("vault_root") or os.environ.get("LOCAL_LLM_KV_CACHE_SIZING_VAULT_ROOT")),
        "run_root": str(run_root),
        "max_utilization": max_utilization,
        "candidate_count": len(evaluated),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "candidates": evaluated,
        "outputs": {},
    }

    json_path = run_dir / f"{run_id}-kv-cache-sizing.json"
    markdown_path = run_dir / f"{run_id}-kv-cache-sizing.md"
    csv_path = run_dir / f"{run_id}-kv-cache-sizing.csv"
    jsonl_path = run_root / "local-llm-kv-cache-sizing-runs.jsonl"
    record["outputs"] = {
        "json": str(json_path),
        "markdown": str(markdown_path),
        "csv": str(csv_path),
        "jsonl": str(jsonl_path),
    }

    json_path.write_text(json.dumps(record, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown(record), encoding="utf-8")
    write_csv(csv_path, evaluated)
    with jsonl_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=True) + "\n")

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
$env:LOCAL_LLM_KV_CACHE_SIZING_MANIFEST = "D:\llm-runs\kv-cache-sizing\kv-cache-sizing-manifest.json"
$env:LOCAL_LLM_KV_CACHE_SIZING_RUN_ROOT = "D:\llm-runs\kv-cache-sizing"
$env:LOCAL_LLM_KV_CACHE_SIZING_VAULT_ROOT = "D:\Vaults\PersonalKB"
python .\local_llm_kv_cache_sizing_runner.py
```

## Reading The Result

| Runner status | Meaning | Next route |
|---|---|---|
| `pass/kv_cache_sizing_ready` | at least one candidate has source-backed geometry and cache memory fits within the safe cache budget | [[LLM/Study/Local LLM Hardware Sizing Runner]] |
| `hold/kv_cache_sizing_incomplete` | geometry, source, budget, cache precision proof, or headroom is incomplete | [[LLM/Study/Local LLM Model and Hardware Sizing Guide]] |
| `fail/kv_cache_sizing_failed` | every candidate's cache exceeds the selected budget or has contradictory architecture metadata | reduce context, active sequences, KV heads, or cache precision, then retest |

A pass is only a cache-fit claim. It does not prove model weights fit, the runtime can load the artifact, the endpoint works, or answer quality is acceptable.

## Copy Row

| Field | Value |
|---|---|
| KV-cache sizing status | pass / hold / fail |
| Output JSON |  |
| Candidate |  |
| Attention kind | MHA / MQA / GQA / measured |
| Layers |  |
| Hidden size |  |
| Attention heads |  |
| KV heads |  |
| Head dim |  |
| Context tokens |  |
| Active sequences |  |
| Cache dtype |  |
| KV-cache GB |  |
| Budget GB |  |
| Margin GB |  |
| Source proof |  |
| Next route |  |

## Completion Gate

This runner output counts when:

- [ ] architecture fields come from a source-checked model config, model card, runtime metadata, or local artifact
- [ ] `num_key_value_heads` is supplied, or the cache size is measured directly
- [ ] context tokens include prompt, history, RAG/tool context, and output reserve
- [ ] active sequences match the intended serving mode
- [ ] cache dtype is explicit, and quantized cache precision has runtime proof before it supports a pass decision
- [ ] cache budget is explicit or computed from measured available memory after weights and overhead
- [ ] output JSON, Markdown, CSV, and JSONL artifacts are saved before model selection, pull, runtime-health, or concurrency evidence depends on the estimate

## References

Internal routes:

- [[LLM/Study/LLM Math and Tensor Shape Primer]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/Study/Local LLM Model Metadata Card Runner]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Hardware Sizing Runner]]
- [[LLM/Study/Local LLM Model Selection Runner]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Lab]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner]]
- [[LLM/_chunks/chunk-llm-213 Multi-Query Attention Shared KV Heads]]
- [[LLM/_chunks/chunk-llm-214 KV Cache Memory Bandwidth Bottleneck]]
- [[LLM/_chunks/chunk-llm-217 GQA Mechanism Interpolating MHA and MQA]]
- [[LLM/_chunks/chunk-llm-117 PagedAttention Eliminates KV Fragmentation]]

External/current sources checked 2026-06-16:

- [Hugging Face Transformers cache explanation](https://huggingface.co/docs/transformers/cache_explanation)
- [Hugging Face Transformers cache strategies](https://huggingface.co/docs/transformers/en/kv_cache)
- [Hugging Face Llama 2 config field for `num_key_value_heads`](https://huggingface.co/docs/transformers/en/model_doc/llama2)
- [vLLM PagedAttention design](https://docs.vllm.ai/en/latest/design/paged_attention/)
- [vLLM automatic prefix caching design](https://docs.vllm.ai/en/stable/design/prefix_caching/)
