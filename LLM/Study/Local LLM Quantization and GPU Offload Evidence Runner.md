---
tags: [study, llm, inference, local-llm, quantization, gpu-offload, kv-cache, benchmark, quality, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice, deep-dive]
last-verified: 2026-06-16
---

# Local LLM Quantization and GPU Offload Evidence Runner

> **One-line summary** Quantization/offload decisions count only when the selected artifact, runtime support, memory estimate, load state, offload sweep, KV-cache/context row, benchmark, quality regression, and review trigger are all auditable.

Use this after [[LLM/Study/Local LLM Quantization and GPU Offload Lab|Local LLM Quantization and GPU Offload Lab]] when the lab rows should become pass, hold, fail, JSON, CSV, Markdown, and JSONL evidence. Use it before [[LLM/Study/Local LLM Result Synthesis Runner|Local LLM Result Synthesis Runner]] and [[LLM/Study/LLM Deployment Readiness Audit Runner|LLM Deployment Readiness Audit Runner]] whenever a lower-bit artifact, GPU-offload setting, CPU fallback, KV-cache precision, or "smaller high-precision versus larger quantized" choice supports the final local model decision.

This runner does not download models, benchmark endpoints, scrape model pages, or decide whether a runtime currently supports a quantization format. Runtime support changes. Put current, source-checked compatibility facts into the manifest, then let the runner check whether the decision evidence is complete enough to keep, tune, reject, or rerun.

## What This Proves

| Evidence family | Checks | Why it matters |
|---|---|---|
| Baseline scope | workload, quality gate, fixed prompts, sampler, context target, baseline or blocker | prevents "Q4 is good" claims without a comparison surface |
| Artifact/runtime support | model id, artifact container, quantization method, runtime, version, hardware path, support proof | catches unsupported GGUF/AWQ/GPTQ/FP8/INT8 paths before quality blame |
| Memory estimate | weight memory, KV-cache memory, runtime overhead, RAM/VRAM budget, headroom | separates "weights fit" from "service fits at target context/concurrency" |
| Load and offload | loaded model id, CPU/GPU split, GPU layers or percentage, device path, peak memory | proves where the model actually ran |
| KV-cache/context | cache dtype, context length, active sequences, long-context or concurrency row | prevents weight quantization from hiding KV-cache OOM risk |
| Benchmark | TTFT, TPOT or tokens/sec, total latency, prompt/output tokens, error class | distinguishes load, prefill, decode, and memory-bandwidth trade-offs |
| Quality regression | same prompt suite, same template, same sampler, pass/hold/fail result | rejects fast configurations that damage task quality |
| Decision card | accepted setting, rejected setting, failure owner, next route, review trigger | turns a sweep into an operational decision |

Academic bridge: GPTQ, AWQ, SmoothQuant, LLM.int8(), GGUF K-quants, FP8, and KV-cache quantization are numerical compression choices, but local hosting turns them into system evidence. The proof question is not "which bit width is best?" It is "which artifact/runtime/offload/cache setting preserves the workload quality while meeting the memory and latency target on this hardware?"

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "quant-offload-001",
  "run_root": "D:/llm-runs/quant-offload",
  "vault_root": "D:/Vaults/PersonalKB",
  "workload": "private local coding assistant",
  "quality_gate": "JSON, code, local-note RAG, and refusal prompts pass",
  "selected_candidate": "qwen-q4-gpu",
  "baseline_candidate": "qwen-q8-gpu",
  "candidates": [
    {
      "candidate_id": "qwen-q4-gpu",
      "model_id": "example-model",
      "runtime": "llama.cpp",
      "runtime_version": "b0000",
      "artifact": "D:/models/example.Q4_K_M.gguf",
      "artifact_container": "GGUF",
      "quantization": "Q4_K_M",
      "hardware_path": "CUDA",
      "offload": "all GPU layers",
      "kv_cache_precision": "f16",
      "context_target": 8192,
      "active_sequences": 1,
      "weight_memory_gb": 4.5,
      "kv_cache_gb": 1.2,
      "peak_vram_gb": 7.3,
      "vram_budget_gb": 11.0,
      "quality_result": "pass",
      "decision": "keep"
    }
  ],
  "evidence": [
    {
      "id": "artifact-support",
      "kind": "artifact_runtime",
      "candidate_id": "qwen-q4-gpu",
      "status": "pass",
      "critical": true,
      "proof": "D:/llm-runs/quant-offload/load-log.txt",
      "claim": "GGUF Q4_K_M loads through llama.cpp CUDA with the intended model id.",
      "metrics": {
        "artifact_supported": true,
        "quantization_supported": true,
        "hardware_supported": true
      },
      "next_route": "LLM/Study/Local LLM Runtime Compatibility Runner"
    },
    {
      "id": "decision",
      "kind": "decision_card",
      "candidate_id": "qwen-q4-gpu",
      "status": "pass",
      "critical": true,
      "proof": "D:/llm-runs/quant-offload/decision.md",
      "decision": "keep",
      "metrics": {
        "accepted_quantization": "Q4_K_M",
        "accepted_offload": "all GPU layers",
        "kv_cache_precision": "f16",
        "memory_headroom_gb": 3.7,
        "retest_trigger": "new runtime, driver, context target, or workload"
      },
      "next_route": "LLM/Study/Local LLM Result Synthesis Runner"
    }
  ]
}
```

`proof` may be an absolute path, a vault-relative path, an Obsidian note path, an Obsidian link, or an `https://` source URL for current support facts. Use `waiver_reason` only when an evidence kind is intentionally out of scope, such as no GPU-offload control in the runtime being audited.

## Required Evidence Kinds

By default, the runner expects one row for each kind:

| Kind | Required signal |
|---|---|
| `baseline_scope` | workload, quality gate, fixed prompt/sampler/context surface, baseline or blocker |
| `artifact_runtime` | artifact container, quantization, runtime, hardware path, support proof |
| `memory_estimate` | weight, KV-cache, overhead or peak memory, plus RAM/VRAM budget/headroom |
| `load_state` | loaded model id or explicit load blocker, CPU/GPU split, device/offload proof |
| `offload_sweep` | CPU/partial/max-safe row, or explicit runtime-not-exposed waiver |
| `kv_cache_context` | cache dtype, context target, active sequences, or explicit not-relevant waiver |
| `benchmark` | TTFT, TPOT/tokens-sec, prompt/output tokens, latency, memory, error class |
| `quality_regression` | same prompt suite, same sampler/template, pass/hold/fail task quality |
| `decision_card` | accepted setting, rejected alternative, failure owner, next route, retest trigger |
| `rejected_candidate` | rejected quant/offload/model/runtime or explicit no-alternative blocker |

You can override this with `required_kinds` in the manifest.

## Standard-Library Runner

Save this as `local_llm_quantization_offload_evidence_runner.py` inside the run folder. It uses only Python's standard library.

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
    "baseline_scope",
    "artifact_runtime",
    "memory_estimate",
    "load_state",
    "offload_sweep",
    "kv_cache_context",
    "benchmark",
    "quality_regression",
    "decision_card",
    "rejected_candidate",
]

KIND_HINTS = {
    "baseline_scope": ("baseline", "Freeze workload, quality gate, prompts, sampler, context, and baseline comparison.", "LLM/Study/Local LLM Quantization and GPU Offload Lab"),
    "artifact_runtime": ("compatibility", "Attach artifact, quantization, runtime, hardware, and current support proof.", "LLM/Study/Local LLM Runtime Compatibility Runner"),
    "memory_estimate": ("capacity", "Record weight, KV-cache, runtime overhead, budget, and headroom.", "LLM/Study/Local LLM Hardware Sizing Runner"),
    "load_state": ("runtime", "Prove loaded model id, CPU/GPU split, device path, and peak memory or load blocker.", "LLM/Study/Local LLM Observability and Operations Runner"),
    "offload_sweep": ("offload", "Compare CPU, partial, max-safe, or explicitly waive because the runtime does not expose offload.", "LLM/Study/Local LLM Quantization and GPU Offload Lab"),
    "kv_cache_context": ("kv-cache", "Record cache dtype, context target, active sequences, and long-context/concurrency consequence.", "LLM/Study/Local LLM KV Cache Sizing Runner"),
    "benchmark": ("metrics", "Include TTFT, TPOT or tokens/sec, latency, prompt/output tokens, memory, and error class.", "LLM/Study/Local LLM Inference Metrics Field Guide"),
    "quality_regression": ("quality", "Run the same prompt suite, sampler, template, and quality rubric across candidates.", "LLM/Study/Local LLM Quality Evaluation Runner"),
    "decision_card": ("decision", "State accepted setting, rejected setting, failure owner, next route, and review trigger.", "LLM/Study/Local LLM Result Synthesis Runner"),
    "rejected_candidate": ("alternative", "Name the rejected quant/offload/model/runtime or why no alternative could be tested.", "LLM/Study/Local LLM Result Synthesis Runner"),
}

STATUS_VALUES = {
    "pass": "pass",
    "passed": "pass",
    "complete": "pass",
    "ready": "pass",
    "keep": "pass",
    "accepted": "pass",
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
    "unsafe": "fail",
    "unsupported": "fail",
    "error": "fail",
}

STATUS_RANK = {"pass": 0, "hold": 1, "fail": 2}
LINK_OPEN = "[" + "["
LINK_CLOSE = "]" + "]"


def utc_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def slug(value: Any) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value or "").strip().lower())
    return text.strip("-") or "quantization-offload"


def text(value: Any) -> str:
    return str(value or "").strip()


def norm(value: Any) -> str:
    return text(value).lower()


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
    manifest_path = os.environ.get("LOCAL_LLM_QUANT_OFFLOAD_MANIFEST")
    if not manifest_path:
        raise ValueError("Set LOCAL_LLM_QUANT_OFFLOAD_MANIFEST to a JSON manifest path.")
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
    missing: list[str] = []
    for proof in proofs:
        if re.match(r"^https?://", proof):
            continue
        paths = proof_candidates(proof, vault_root, manifest_dir)
        if paths and any(path.exists() for path in paths):
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


def row_quality_checks(row: dict[str, Any], issues: list[dict[str, Any]], vault_root: Path | None, manifest_dir: Path) -> None:
    kind = text(row.get("kind") or "uncategorized")
    owner, hint, route = KIND_HINTS.get(kind, ("evidence", "Attach proof.", "LLM/Study/LLM Study Index"))
    row_id = text(row.get("id") or kind)
    status = status_value(row.get("status"))
    proof_ok, proof_msg = proof_status(row, vault_root, manifest_dir)
    required = bool_value(row.get("required"), True)
    critical = bool_value(row.get("critical"), False)

    if not proof_ok and required:
        add_issue(issues, "fail" if critical else "hold", kind, owner, f"{hint} Proof problem: {proof_msg}.", route, row_id)
    if status == "fail":
        add_issue(issues, "fail" if critical else "hold", kind, owner, text(row.get("evidence") or row.get("claim") or "Evidence row is failed."), route, row_id)
    if status == "hold" and required and not text(row.get("waiver_reason")):
        add_issue(issues, "hold", kind, owner, text(row.get("evidence") or row.get("claim") or "Evidence row is incomplete."), route, row_id)

    if kind == "memory_estimate":
        has_memory = any(metric(row, name) is not None for name in ["weight_memory_gb", "kv_cache_gb", "runtime_overhead_gb", "peak_vram_gb", "peak_ram_gb", "memory_headroom_gb"])
        has_budget = any(metric(row, name) is not None for name in ["vram_budget_gb", "ram_budget_gb", "memory_budget_gb"])
        if required and (not has_memory or not has_budget):
            add_issue(issues, "hold", kind, owner, "Memory row needs both demand and budget/headroom signals.", route, row_id)
    elif kind == "benchmark":
        has_latency = any(metric(row, name) is not None for name in ["ttft_ms", "tpot_ms", "tokens_per_second", "output_tok_s", "total_latency_ms"])
        has_tokens = any(metric(row, name) is not None for name in ["prompt_tokens", "output_tokens", "context_tokens"])
        if required and (not has_latency or not has_tokens):
            add_issue(issues, "hold", kind, owner, "Benchmark row needs latency/rate plus prompt or output token counts.", route, row_id)
    elif kind == "quality_regression":
        result = status_value(metric(row, "quality_result", "result", "decision") or row.get("status"))
        suite = metric(row, "prompt_suite", "rubric", "quality_gate")
        if result == "fail":
            add_issue(issues, "fail" if critical else "hold", kind, owner, "Quality regression failed for this quantization/offload candidate.", route, row_id)
        if required and not suite:
            add_issue(issues, "hold", kind, owner, "Quality row needs prompt-suite, rubric, or quality-gate proof.", route, row_id)
    elif kind == "decision_card":
        needed = ["accepted_quantization", "accepted_offload", "kv_cache_precision", "retest_trigger"]
        missing = [name for name in needed if not metric(row, name)]
        if required and missing:
            add_issue(issues, "hold", kind, owner, "Decision card is missing: " + ", ".join(missing) + ".", route, row_id)


def candidate_checks(manifest: dict[str, Any], issues: list[dict[str, Any]]) -> list[dict[str, Any]]:
    candidates = manifest.get("candidates") or []
    if not isinstance(candidates, list):
        add_issue(issues, "fail", "candidates", "manifest", "candidates must be a list.", "LLM/Study/Local LLM Quantization and GPU Offload Lab")
        return []
    normalized = [candidate for candidate in candidates if isinstance(candidate, dict)]
    selected_id = text(manifest.get("selected_candidate"))
    baseline_id = text(manifest.get("baseline_candidate"))
    by_id = {text(candidate.get("candidate_id")): candidate for candidate in normalized if text(candidate.get("candidate_id"))}

    if not selected_id:
        add_issue(issues, "hold", "candidate", "decision", "Manifest needs selected_candidate.", "LLM/Study/Local LLM Result Synthesis Runner")
    elif selected_id not in by_id:
        add_issue(issues, "fail", "candidate", "decision", f"selected_candidate is not present in candidates: {selected_id}", "LLM/Study/Local LLM Quantization and GPU Offload Lab")

    if len(normalized) < 2 and not text(manifest.get("baseline_unavailable_reason")):
        add_issue(issues, "hold", "baseline_scope", "baseline", "Test at least two candidates or record baseline_unavailable_reason.", "LLM/Study/Local LLM Quantization and GPU Offload Lab")
    if baseline_id and baseline_id not in by_id:
        add_issue(issues, "hold", "baseline_scope", "baseline", f"baseline_candidate is not present in candidates: {baseline_id}", "LLM/Study/Local LLM Quantization and GPU Offload Lab")

    selected = by_id.get(selected_id, {})
    required_fields = ["model_id", "runtime", "artifact", "quantization", "hardware_path", "offload", "kv_cache_precision", "context_target"]
    missing = [field for field in required_fields if not text(selected.get(field))]
    if selected_id and missing:
        add_issue(issues, "hold", "candidate", "compatibility", "Selected candidate is missing: " + ", ".join(missing) + ".", "LLM/Study/Local LLM Runtime Compatibility Runner")

    for candidate in normalized:
        cid = text(candidate.get("candidate_id") or candidate.get("model_id") or "candidate")
        decision = norm(candidate.get("decision"))
        quality = status_value(candidate.get("quality_result"))
        peak = num_value(candidate.get("peak_vram_gb") or candidate.get("peak_ram_gb"))
        budget = num_value(candidate.get("vram_budget_gb") or candidate.get("ram_budget_gb"))
        if decision in {"keep", "accepted", "pass"} and quality == "fail":
            add_issue(issues, "fail", "quality_regression", "quality", f"Candidate {cid} is marked keep but quality_result is fail.", "LLM/Study/Local LLM Quality Evaluation Runner", cid)
        if peak is not None and budget is not None and peak >= budget:
            add_issue(issues, "fail", "memory_estimate", "capacity", f"Candidate {cid} peak memory meets or exceeds budget ({peak:g} >= {budget:g}).", "LLM/Study/Local LLM Hardware Sizing Runner", cid)
    return normalized


def evaluate(manifest_path: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    issues: list[dict[str, Any]] = []
    vault_text = text(manifest.get("vault_root"))
    vault_root = Path(vault_text).expanduser().resolve() if vault_text else None
    if vault_root and not vault_root.exists():
        add_issue(issues, "hold", "manifest", "vault", f"vault_root does not exist: {vault_root}", "LLM/Study/LLM Study Index")

    candidates = candidate_checks(manifest, issues)
    rows = manifest.get("evidence") or manifest.get("rows") or []
    if not isinstance(rows, list):
        add_issue(issues, "fail", "evidence", "manifest", "evidence must be a list.", "LLM/Study/Local LLM Quantization and GPU Offload Lab")
        rows = []

    required_kinds = list_value(manifest.get("required_kinds")) or DEFAULT_REQUIRED_KINDS
    present_required: set[str] = set()
    status_by_kind: dict[str, str] = {}
    for row in rows:
        if not isinstance(row, dict):
            add_issue(issues, "hold", "evidence", "manifest", "Non-object evidence row ignored.", "LLM/Study/Local LLM Quantization and GPU Offload Lab")
            continue
        kind = text(row.get("kind") or "uncategorized")
        if bool_value(row.get("required"), True):
            present_required.add(kind)
        row_quality_checks(row, issues, vault_root, manifest_path.parent)
        current = status_value(row.get("status"))
        previous = status_by_kind.get(kind, "pass")
        status_by_kind[kind] = current if STATUS_RANK[current] > STATUS_RANK[previous] else previous

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
        decision = "quantization_offload_ready"
        next_route = "LLM/Study/Local LLM Result Synthesis Runner"
    elif final_status == "fail":
        decision = "quantization_offload_blocked"
        next_route = first_route(issues, "LLM/Study/Local LLM Quantization and GPU Offload Lab")
    else:
        decision = "quantization_offload_incomplete"
        next_route = first_route(issues, "LLM/Study/Local LLM Quantization and GPU Offload Lab")

    return {
        "run_id": text(manifest.get("run_id") or manifest_path.stem),
        "generated_at": utc_iso(),
        "status": final_status,
        "decision": decision,
        "next_route": next_route,
        "workload": text(manifest.get("workload")),
        "quality_gate": text(manifest.get("quality_gate")),
        "selected_candidate": text(manifest.get("selected_candidate")),
        "baseline_candidate": text(manifest.get("baseline_candidate")),
        "required_kinds": required_kinds,
        "present_required_kinds": sorted(present_required),
        "missing_required_kinds": [kind for kind in required_kinds if kind not in present_required],
        "status_by_kind": status_by_kind,
        "candidate_count": len(candidates),
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
        f"# Quantization and GPU Offload Evidence Audit - {result['run_id']}",
        "",
        f"- Generated: {result['generated_at']}",
        f"- Status: `{result['status']}`",
        f"- Decision: `{result['decision']}`",
        f"- Selected candidate: `{result.get('selected_candidate') or 'missing'}`",
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
        "A `pass` means the selected quantization/offload/cache setting can move to result synthesis. A `hold` means evidence is missing or waived too broadly. A `fail` means a critical support, memory, quality, or decision claim is contradicted.",
    ])
    return "\n".join(lines) + "\n"


def write_outputs(manifest_path: Path, manifest: dict[str, Any], result: dict[str, Any]) -> dict[str, str]:
    run_root = Path(text(manifest.get("run_root")) or manifest_path.parent).expanduser()
    if not run_root.is_absolute():
        run_root = manifest_path.parent / run_root
    run_root.mkdir(parents=True, exist_ok=True)
    base = run_root / f"{slug(result['run_id'])}-quantization-offload-evidence"
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
            "event": "quantization_offload_evidence_audit",
            "recorded_at": utc_iso(),
            "status": result["status"],
            "decision": result["decision"],
            "run_id": result["run_id"],
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

Use these before trusting local evidence rows:

| Fixture | Expected decision | Reason |
|---|---|---|
| complete GGUF Q4 with Q8 baseline, offload sweep, KV-cache row, benchmark, quality pass | `pass/quantization_offload_ready` | selected setting has full support, memory, quality, and decision proof |
| only one candidate, no baseline blocker | `hold/quantization_offload_incomplete` | cannot tell whether quantization helped or harmed |
| selected candidate quality fails but decision says keep | `fail/quantization_offload_blocked` | speed cannot override task quality |
| peak VRAM exceeds budget | `fail/quantization_offload_blocked` | the selected setting is not deployable on target hardware |
| offload sweep absent with no waiver | `hold/quantization_offload_incomplete` | GPU/CPU split claim is unproven |
| unsupported quantization row marked critical fail | `fail/quantization_offload_blocked` | runtime/artifact mismatch must be fixed first |
| KV-cache row waived for short single-user workload | `pass/quantization_offload_ready` if other required rows pass and `required_kinds` is adjusted | context/concurrency gate can be explicitly out of scope |

## Completion Gate

This runner is complete when:

- [ ] a baseline or baseline-blocker is recorded before accepting a lower-bit artifact
- [ ] the selected candidate has model id, artifact container, quantization, runtime, hardware path, offload, KV-cache precision, and context target
- [ ] current runtime support proof is attached for the artifact and quantization path
- [ ] memory demand is compared with RAM/VRAM budget and headroom
- [ ] load state proves actual CPU/GPU split or load blocker
- [ ] offload sweep, KV-cache/context, benchmark, and quality rows are present or explicitly waived with scope
- [ ] at least one rejected alternative is named or the blocker explains why no alternative could be tested
- [ ] the final decision routes to [[LLM/Study/Local LLM Result Synthesis Runner|Local LLM Result Synthesis Runner]]

## References

Internal:

- [[LLM/Sources/Sources Index]]
- [[LLM/2022 — Alignment and Chat/Quantization]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Lab]]
- [[LLM/Study/Local LLM Runtime Compatibility Runner]]
- [[LLM/Study/Local LLM Hardware Sizing Runner]]
- [[LLM/Study/Local LLM KV Cache Sizing Runner]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/Local LLM Quality Evaluation Runner]]
- [[LLM/Study/Local LLM Result Synthesis Runner]]
- [[LLM/Study/LLM Deployment Readiness Audit Runner]]
- [[LLM/_chunks/chunk-llm-205 GPTQ Hessian-Based Weight Quantization]]
- [[LLM/_chunks/chunk-llm-207 GPTQ 3-4 Bit Accuracy vs FP16]]
- [[LLM/_chunks/chunk-llm-209 AWQ Activation-Aware Salient Channels]]
- [[LLM/_chunks/chunk-llm-211 AWQ INT4 Edge Deployment Performance]]
- [[LLM/_chunks/chunk-llm-214 KV Cache Memory Bandwidth Bottleneck]]

Academic references:

- [GPTQ](https://arxiv.org/abs/2210.17323)
- [AWQ](https://arxiv.org/abs/2306.00978)
- [SmoothQuant](https://arxiv.org/abs/2211.10438)
- [LLM.int8()](https://arxiv.org/abs/2208.07339)

Current external docs checked 2026-06-16:

- [vLLM quantization](https://docs.vllm.ai/en/latest/features/quantization/)
- [vLLM LLM Compressor](https://github.com/vllm-project/llm-compressor)
- [SGLang quantization](https://sgl-project.github.io/advanced_features/quantization.html)
- [llama.cpp server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
- [Ollama context length](https://docs.ollama.com/context-length)
- [Ollama FAQ](https://docs.ollama.com/faq)
- [LM Studio lms load](https://lmstudio.ai/docs/cli/local-models/load)
- [LM Studio per-model defaults](https://lmstudio.ai/docs/app/advanced/per-model)
- [Hugging Face Hub GGUF](https://huggingface.co/docs/hub/en/gguf)
- [Hugging Face Transformers GGUF](https://huggingface.co/docs/transformers/en/gguf)
