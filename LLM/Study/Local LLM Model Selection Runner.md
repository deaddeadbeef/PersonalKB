---
tags: [study, llm, inference, local-llm, model-selection, hardware, evaluation, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM Model Selection Runner

Use this after [[LLM/Study/Local LLM Workload to Model Selection Playbook|Local LLM Workload to Model Selection Playbook]] when candidate facts should become a repeatable shortlist. The playbook teaches the decision. This runner turns a workload contract, hardware budget, and candidate manifest into JSON, Markdown, CSV, and JSONL evidence.

This runner does not scrape model pages or recommend current models by name. Model cards, licenses, quantized derivatives, and runtime support change. Put the source-checked facts into the manifest, then let the runner apply the gates consistently.

## What This Proves

| Gate | Evidence checked | Why it matters |
|---|---|---|
| Workload | task, output shape, data boundary, quality gate, latency target | prevents choosing a model from hype instead of job fit |
| Candidate custody | source, model-card date, license, artifact, runtime | prevents anonymous or stale model choices |
| Memory fit | weight memory, KV-cache risk, runtime overhead, headroom | prevents "largest model that might load" decisions |
| Compatibility | runtime support, chat template/tokenizer risk, output-shape risk | catches failures before download and benchmark time |
| Evidence state | benchmark and quality decisions when available | separates candidates worth serving from candidates only worth testing |
| Next action | pass, hold, fail, and owner | chooses the next controlled proof route |

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "first-local-chat-shortlist",
  "hardware": {
    "gpu": "RTX 3080 Ti",
    "vram_gb": 12,
    "available_vram_gb": 9.5,
    "system_ram_gb": 64
  },
  "workload": {
    "name": "personal loopback chat",
    "task": "private chat",
    "data_boundary": "personal",
    "required_output_shape": "prose",
    "context_target_tokens": 4096,
    "latency_target": "interactive",
    "quality_gate": "known-answer and instruction-following mini-suite",
    "maintenance_target": "personal endpoint"
  },
  "candidates": [
    {
      "candidate_id": "baseline-small",
      "slot": "baseline",
      "model_family": "example-instruct",
      "model_class": "chat",
      "source": "local model card or registry URL",
      "model_card_checked": "2026-06-15",
      "license": "acceptable",
      "artifact": "GGUF Q4 or runtime tag",
      "runtime": "Ollama",
      "parameter_count_b": 4,
      "bytes_per_parameter": 0.5,
      "kv_cache_gb": 1,
      "runtime_overhead_gb": 1,
      "chat_template_risk": "low",
      "output_shape_risk": "low",
      "benchmark_status": "pending",
      "quality_status": "pending"
    }
  ]
}
```

## Standard-Library Runner

Save the code block as `local_llm_model_selection_runner.py` or extract it directly from this note.

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


REQUIRED_WORKLOAD = [
    "name",
    "task",
    "data_boundary",
    "required_output_shape",
    "context_target_tokens",
    "latency_target",
    "quality_gate",
]

REQUIRED_CANDIDATE = [
    "candidate_id",
    "slot",
    "model_family",
    "model_class",
    "source",
    "model_card_checked",
    "license",
    "artifact",
    "runtime",
]

SLOT_RANK = {
    "baseline": 0,
    "baseline small candidate": 0,
    "control": 1,
    "practical": 2,
    "practical local candidate": 2,
    "specialized": 3,
    "stretch": 4,
    "stretch local candidate": 4,
    "reference": 5,
    "external reference": 5,
}

STATUS_RANK = {
    "pass": 0,
    "hold": 1,
    "fail": 2,
}

RISK_VALUES = {
    "low": 0,
    "medium": 1,
    "med": 1,
    "high": 2,
    "unknown": 2,
    "not needed": 0,
    "n/a": 0,
}


def utc_stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def utc_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def slug(value: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return text[:80] or "model-selection"


def compact(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.3f}"
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value)


def wiki_link(route: str) -> str:
    if not route:
        return ""
    return "[" + "[" + route + "]" + "]"


def as_float(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def as_int(value: Any) -> int | None:
    numeric = as_float(value)
    if numeric is None:
        return None
    return int(numeric)


def norm(value: Any) -> str:
    return str(value or "").strip().lower()


def risk_value(value: Any) -> int:
    return RISK_VALUES.get(norm(value), 2)


def status_value(value: Any) -> str:
    return norm(value).replace("_", "-").replace(" ", "-")


def load_manifest() -> tuple[Path, dict[str, Any]]:
    manifest_path = os.environ.get("LOCAL_LLM_MODEL_SELECTION_MANIFEST")
    if not manifest_path:
        raise ValueError("Set LOCAL_LLM_MODEL_SELECTION_MANIFEST to a JSON manifest path.")
    path = Path(manifest_path).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"Manifest path does not exist: {path}")
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError("Manifest must be a JSON object.")
    return path, data


def missing_fields(mapping: dict[str, Any], fields: list[str]) -> list[str]:
    return [field for field in fields if mapping.get(field) in (None, "", [])]


def estimate_weight_gb(candidate: dict[str, Any]) -> float | None:
    explicit = as_float(candidate.get("weight_memory_gb"))
    if explicit is not None:
        return explicit
    params_b = as_float(candidate.get("parameter_count_b"))
    bytes_per_parameter = as_float(candidate.get("bytes_per_parameter"))
    if params_b is None or bytes_per_parameter is None:
        return None
    return params_b * bytes_per_parameter


def estimate_total_gb(candidate: dict[str, Any]) -> float | None:
    weight = estimate_weight_gb(candidate)
    if weight is None:
        return None
    kv = as_float(candidate.get("kv_cache_gb")) or 0.0
    overhead = as_float(candidate.get("runtime_overhead_gb")) or 0.0
    safety = as_float(candidate.get("safety_headroom_gb")) or 0.0
    return weight + kv + overhead + safety


def classify_fit(total_gb: float | None, available_vram_gb: float | None, system_ram_gb: float | None, runtime: str) -> tuple[str, str]:
    if total_gb is None:
        return "hold", "missing memory estimate"
    if available_vram_gb is not None:
        if total_gb <= available_vram_gb * 0.85:
            return "pass", f"estimated {total_gb:.2f} GB <= 85 percent of available VRAM {available_vram_gb:.2f} GB"
        if total_gb <= available_vram_gb:
            return "hold", f"estimated {total_gb:.2f} GB fits only with thin VRAM headroom {available_vram_gb:.2f} GB"
        if "cpu" in runtime.lower() or "llama.cpp" in runtime.lower():
            if system_ram_gb is not None and total_gb <= system_ram_gb * 0.70:
                return "hold", f"does not fit VRAM but may be CPU/offload feasible within RAM {system_ram_gb:.2f} GB"
        return "fail", f"estimated {total_gb:.2f} GB exceeds available VRAM {available_vram_gb:.2f} GB"
    if system_ram_gb is not None and total_gb <= system_ram_gb * 0.70:
        return "hold", f"no VRAM budget supplied; estimated {total_gb:.2f} GB appears RAM-feasible"
    return "hold", "no hardware memory budget supplied"


def route_for_action(owner: str) -> str:
    if owner == "workload":
        return "LLM/Study/Local LLM Workload to Model Selection Playbook"
    if owner == "memory":
        return "LLM/Study/Local LLM Model and Hardware Sizing Guide"
    if owner == "custody":
        return "LLM/Study/Local LLM Model Acquisition and Provenance Checklist"
    if owner == "compatibility":
        return "LLM/Study/Local LLM Runtime and Model Compatibility Matrix"
    if owner == "quality":
        return "LLM/Study/Local LLM Quality Evaluation Harness"
    if owner == "benchmark":
        return "LLM/Study/Local LLM Inference Benchmark Log"
    if owner == "security":
        return "LLM/Study/Local LLM Security and Privacy Runner"
    return "LLM/Study/Local LLM First Model Pull Gate"


def evaluate_candidate(candidate: dict[str, Any], workload: dict[str, Any], hardware: dict[str, Any]) -> dict[str, Any]:
    findings: list[dict[str, str]] = []
    missing = missing_fields(candidate, REQUIRED_CANDIDATE)
    if missing:
        findings.append({
            "level": "hold",
            "owner": "custody",
            "finding": "Missing required candidate fields.",
            "evidence": ", ".join(missing),
            "action": "Fill the candidate card before ranking.",
        })

    available_vram = as_float(hardware.get("available_vram_gb") or hardware.get("vram_gb"))
    system_ram = as_float(hardware.get("system_ram_gb"))
    runtime = str(candidate.get("runtime", ""))
    weight_gb = estimate_weight_gb(candidate)
    total_gb = estimate_total_gb(candidate)
    fit_status, fit_evidence = classify_fit(total_gb, available_vram, system_ram, runtime)
    if fit_status == "fail":
        findings.append({
            "level": "fail",
            "owner": "memory",
            "finding": "Candidate does not fit the supplied memory budget.",
            "evidence": fit_evidence,
            "action": "Choose a smaller model, lower context/concurrency, stronger quantization, or a different machine.",
        })
    elif fit_status == "hold":
        findings.append({
            "level": "hold",
            "owner": "memory",
            "finding": "Candidate memory fit is not proven.",
            "evidence": fit_evidence,
            "action": "Fill sizing guide and benchmark actual load before accepting this candidate.",
        })

    license_status = status_value(candidate.get("license_status") or candidate.get("license"))
    if license_status in {"", "unknown", "unclear", "restricted"}:
        findings.append({
            "level": "hold",
            "owner": "custody",
            "finding": "License or use boundary is not proven acceptable.",
            "evidence": str(candidate.get("license", "")),
            "action": "Complete model acquisition and provenance before download or service use.",
        })
    if license_status in {"forbidden", "not-allowed", "not-acceptable"}:
        findings.append({
            "level": "fail",
            "owner": "custody",
            "finding": "License blocks this candidate.",
            "evidence": str(candidate.get("license", "")),
            "action": "Reject the candidate or choose a permitted source.",
        })

    if risk_value(candidate.get("chat_template_risk")) >= 2:
        findings.append({
            "level": "hold",
            "owner": "compatibility",
            "finding": "Chat template or tokenizer risk is high or unknown.",
            "evidence": str(candidate.get("chat_template_risk", "")),
            "action": "Run tokenizer/template compatibility check before quality judgment.",
        })
    if risk_value(candidate.get("output_shape_risk")) >= 2 and norm(workload.get("required_output_shape")) not in {"prose", "chat"}:
        findings.append({
            "level": "hold",
            "owner": "quality",
            "finding": "Output-shape risk is high for the workload contract.",
            "evidence": f"required={workload.get('required_output_shape')}; risk={candidate.get('output_shape_risk')}",
            "action": "Run structured output, citation, code, or tool quality gate before accepting.",
        })

    benchmark_status = status_value(candidate.get("benchmark_status"))
    quality_status = status_value(candidate.get("quality_status"))
    if benchmark_status in {"fail", "failed"}:
        findings.append({
            "level": "fail",
            "owner": "benchmark",
            "finding": "Candidate benchmark failed.",
            "evidence": str(candidate.get("benchmark_evidence", "")),
            "action": "Reject or change exactly one bottleneck before retesting.",
        })
    elif benchmark_status in {"", "pending", "not-started", "unknown"}:
        findings.append({
            "level": "hold",
            "owner": "benchmark",
            "finding": "Benchmark evidence is not yet available.",
            "evidence": benchmark_status or "missing",
            "action": "Run endpoint, lifecycle, and benchmark rows before deployment selection.",
        })

    if quality_status in {"fail", "failed"}:
        findings.append({
            "level": "fail",
            "owner": "quality",
            "finding": "Candidate quality gate failed.",
            "evidence": str(candidate.get("quality_evidence", "")),
            "action": "Reject, add RAG/tools, improve prompt, or test a different model class.",
        })
    elif quality_status in {"", "pending", "not-started", "unknown"}:
        findings.append({
            "level": "hold",
            "owner": "quality",
            "finding": "Quality gate is not yet available.",
            "evidence": quality_status or "missing",
            "action": "Run the workload-specific quality harness before accepting.",
        })

    fail_count = sum(1 for item in findings if item["level"] == "fail")
    hold_count = sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        status = "fail"
        decision = "reject_candidate"
    elif hold_count:
        status = "hold"
        decision = "candidate_needs_evidence"
    else:
        status = "pass"
        decision = "candidate_shortlisted"

    first_owner = findings[0]["owner"] if findings else "pull"
    next_route = route_for_action(first_owner)
    if status == "pass":
        next_action = "Use this as the current candidate and record review trigger."
    else:
        next_action = findings[0]["action"] if findings else "Continue to pull gate."

    slot = norm(candidate.get("slot"))
    score = 100
    score -= fail_count * 40
    score -= hold_count * 10
    score -= risk_value(candidate.get("chat_template_risk")) * 3
    score -= risk_value(candidate.get("output_shape_risk")) * 3
    score -= SLOT_RANK.get(slot, 3)
    if total_gb is not None and available_vram is not None and available_vram > 0:
        score -= max(0, int((total_gb / available_vram) * 10) - 5)
    score = max(0, score)

    return {
        "candidate_id": str(candidate.get("candidate_id", "")),
        "slot": str(candidate.get("slot", "")),
        "model_family": str(candidate.get("model_family", "")),
        "model_class": str(candidate.get("model_class", "")),
        "runtime": runtime,
        "artifact": str(candidate.get("artifact", "")),
        "source": str(candidate.get("source", "")),
        "license": str(candidate.get("license", "")),
        "model_card_checked": str(candidate.get("model_card_checked", "")),
        "missing_candidate_fields": missing,
        "weight_memory_gb": weight_gb,
        "estimated_total_gb": total_gb,
        "memory_status": fit_status,
        "memory_evidence": fit_evidence,
        "benchmark_status": benchmark_status,
        "quality_status": quality_status,
        "status": status,
        "decision": decision,
        "score": score,
        "next_route": next_route,
        "next_action": next_action,
        "findings": findings,
    }


def csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "rank",
        "candidate_id",
        "slot",
        "model_family",
        "model_class",
        "runtime",
        "artifact",
        "status",
        "decision",
        "score",
        "weight_memory_gb",
        "estimated_total_gb",
        "memory_status",
        "memory_evidence",
        "benchmark_status",
        "quality_status",
        "next_route",
        "next_action",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for index, row in enumerate(rows, start=1):
            payload = {"rank": index, **row}
            writer.writerow({field: compact(payload.get(field)) for field in fields})


def md_cell(value: Any) -> str:
    return compact(value).replace("\n", "<br>").replace("|", "\\|")


def render_markdown(record: dict[str, Any]) -> str:
    lines = [
        f"# Local LLM Model Selection - {record['run_id']}",
        "",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Created: `{record['created_at']}`",
        f"- Workload: `{record['workload'].get('name', '')}`",
        f"- Hardware: `{record['hardware'].get('gpu', '')}` with available VRAM `{record['hardware'].get('available_vram_gb', record['hardware'].get('vram_gb', ''))}` GB",
        "",
        "## Candidate Ranking",
        "",
        "| Rank | Candidate | Slot | Runtime | Status | Score | Memory | Next route |",
        "|---:|---|---|---|---|---:|---|---|",
    ]
    for index, row in enumerate(record["candidates"], start=1):
        lines.append(
            f"| {index} | {md_cell(row['candidate_id'])} | {md_cell(row['slot'])} | {md_cell(row['runtime'])} | {md_cell(row['status'])} | {md_cell(row['score'])} | {md_cell(row['memory_evidence'])} | {md_cell(wiki_link(row['next_route']))} |"
        )
    lines.extend(["", "## Findings", "", "| Candidate | Level | Owner | Finding | Action |", "|---|---|---|---|---|"])
    for row in record["candidates"]:
        for finding in row["findings"]:
            lines.append(
                f"| {md_cell(row['candidate_id'])} | {md_cell(finding['level'])} | {md_cell(finding['owner'])} | {md_cell(finding['finding'])} | {md_cell(finding['action'])} |"
            )
    if not any(row["findings"] for row in record["candidates"]):
        lines.append("| none | pass | selection | No hold/fail findings. | Continue to pull gate. |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    manifest_path, manifest = load_manifest()
    workload = manifest.get("workload") if isinstance(manifest.get("workload"), dict) else {}
    hardware = manifest.get("hardware") if isinstance(manifest.get("hardware"), dict) else {}
    candidates = manifest.get("candidates") if isinstance(manifest.get("candidates"), list) else []
    if not candidates:
        raise ValueError("Manifest must include a non-empty candidates list.")

    workload_missing = missing_fields(workload, REQUIRED_WORKLOAD)
    run_id = str(manifest.get("run_id") or os.environ.get("LOCAL_LLM_MODEL_SELECTION_RUN_ID") or f"{utc_stamp()}-{slug(workload.get('name', 'model-selection'))}")
    run_root = Path(os.environ.get("LOCAL_LLM_MODEL_SELECTION_RUN_ROOT", manifest.get("run_root", "model-selection-runs"))).expanduser().resolve()
    run_dir = run_root / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    evaluated = [evaluate_candidate(candidate, workload, hardware) for candidate in candidates if isinstance(candidate, dict)]
    evaluated.sort(key=lambda row: (STATUS_RANK.get(str(row["status"]), 3), -int(row["score"]), row["candidate_id"]))

    if workload_missing:
        for row in evaluated:
            row["findings"].insert(0, {
                "level": "hold",
                "owner": "workload",
                "finding": "Workload contract is incomplete.",
                "evidence": ", ".join(workload_missing),
                "action": "Fill the workload contract before accepting any model.",
            })
            if row["status"] == "pass":
                row["status"] = "hold"
                row["decision"] = "candidate_needs_evidence"
                row["next_route"] = route_for_action("workload")
                row["next_action"] = "Fill the workload contract before accepting any model."

    pass_count = sum(1 for row in evaluated if row["status"] == "pass")
    hold_count = sum(1 for row in evaluated if row["status"] == "hold")
    fail_count = sum(1 for row in evaluated if row["status"] == "fail")
    if pass_count:
        status = "pass"
        decision = "shortlist_ready"
    elif hold_count:
        status = "hold"
        decision = "shortlist_needs_evidence"
    else:
        status = "fail"
        decision = "no_viable_candidates"

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "manifest_path": str(manifest_path),
        "workload": workload,
        "hardware": hardware,
        "workload_missing_fields": workload_missing,
        "candidate_count": len(evaluated),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "candidates": evaluated,
        "outputs": {},
    }

    json_path = run_dir / f"{run_id}-model-selection.json"
    markdown_path = run_dir / f"{run_id}-model-selection.md"
    csv_path = run_dir / f"{run_id}-model-selection.csv"
    jsonl_path = run_root / "model-selection-runs.jsonl"
    record["outputs"] = {
        "json": str(json_path),
        "markdown": str(markdown_path),
        "csv": str(csv_path),
        "jsonl": str(jsonl_path),
    }

    csv_write(csv_path, evaluated)
    markdown_path.write_text(render_markdown(record), encoding="utf-8")
    json_path.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    with jsonl_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(
        json.dumps(
            {
                "status": status,
                "decision": decision,
                "run_id": run_id,
                "candidate_count": len(evaluated),
                "pass_count": pass_count,
                "hold_count": hold_count,
                "fail_count": fail_count,
                "output_dir": str(run_dir),
            },
            indent=2,
        )
    )
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
$env:LOCAL_LLM_MODEL_SELECTION_MANIFEST = "D:\llm-runs\candidate-selection\model-selection-manifest.json"
$env:LOCAL_LLM_MODEL_SELECTION_RUN_ROOT = "D:\llm-runs\candidate-selection"
python .\local_llm_model_selection_runner.py
```

## Reading The Result

| Runner status | Meaning | Next route |
|---|---|---|
| `pass/shortlist_ready` | at least one candidate has enough manifest, memory, compatibility, benchmark, and quality evidence to shortlist | [[LLM/Study/Local LLM First Model Pull Gate]] or service lifecycle review |
| `hold/shortlist_needs_evidence` | one or more candidates might work, but a required gate is missing | follow each candidate's `next_route` |
| `fail/no_viable_candidates` | every candidate violates a hard gate such as memory, license, or failed quality | revise workload, hardware, runtime, or candidate class |

A `hold` result is not bad. It prevents a smoke response or leaderboard rank from masquerading as model selection.

## Capstone Row

| Evidence | Output |
|---|---|
| Model selection runner | `<run-id>-model-selection.json`, `<run-id>-model-selection.md`, `<run-id>-model-selection.csv`, and one `model-selection-runs.jsonl` row |

## References

- [[LLM/Study/Local LLM Workload to Model Selection Playbook]]
- [[LLM/Study/Local LLM First Model Candidate Ladder]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
