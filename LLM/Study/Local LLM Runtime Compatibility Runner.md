---
tags: [study, llm, inference, local-llm, runtime, compatibility, artifact, tokenizer, chat-template, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM Runtime Compatibility Runner

> **One-line summary** A model is ready to load only when its artifact format, architecture, quantization, tokenizer, chat template, runtime, hardware path, model id, and API route have explicit compatibility evidence.

Use this after [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]], [[LLM/Study/Local LLM Model Acquisition and License Gate Runner|Local LLM Model Acquisition and License Gate Runner]], [[LLM/Study/Local LLM Artifact Custody Audit Runner|Local LLM Artifact Custody Audit Runner]], [[LLM/Study/Local LLM Model Metadata Card Runner|Local LLM Model Metadata Card Runner]], and [[LLM/Study/Local LLM Hardware Sizing Runner|Local LLM Hardware Sizing Runner]] when compatibility facts should become JSON, Markdown, CSV, and JSONL evidence. Use it before [[LLM/Study/Local LLM First Model Pull Gate|Local LLM First Model Pull Gate]], [[LLM/Study/Local LLM First Runtime Health Snapshot|Local LLM First Runtime Health Snapshot]], [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner|Local LLM OpenAI-Compatible API Contract Runner]], [[LLM/Study/Chat Template and Tokenizer Compatibility Runner|Chat Template and Tokenizer Compatibility Runner]], and [[LLM/Study/Local LLM Runtime Comparison Lab|Local LLM Runtime Comparison Lab]].

This runner does not scrape runtime documentation or decide whether a model family is currently supported. Runtime support, quantization kernels, model cards, and import paths change. Put source-checked facts into the manifest, then let the runner check whether the evidence is complete enough to load, serve, benchmark, or reject the candidate.

## What This Proves

| Gate | Evidence checked | Why it matters |
|---|---|---|
| Artifact fit | architecture, container, quantization, adapter/base relation | prevents trying to load the wrong file shape in the wrong runtime |
| Runtime support | runtime, version, supported artifact, supported quantization, hardware path | catches load failures before endpoint work |
| Tokenizer/template | tokenizer source, chat template source, stop/EOS policy | prevents role-marker leaks, prompt continuation, and false model-quality blame |
| Route contract | native route, OpenAI-compatible route, model id, endpoint surface | prevents client failures caused by route or id mismatch |
| Evidence handoff | custody proof, hardware sizing proof, compatibility decision, next route | makes the candidate auditable before model pull, smoke test, or benchmark |

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "first-ollama-compatibility",
  "run_root": "D:/llm-runs/runtime-compatibility",
  "vault_root": "D:/Vaults/PersonalKB",
  "workload": {
    "name": "personal loopback chat",
    "required_output_shape": "prose",
    "requires_chat_template": true,
    "requires_openai_compatible": false
  },
  "candidates": [
    {
      "candidate_id": "baseline-small-ollama",
      "model_id": "example:latest",
      "source": "model card or runtime tag checked on 2026-06-15",
      "artifact_container": "Ollama tag",
      "architecture": "decoder-only transformer",
      "quantization": "GGUF Q4 or runtime tag",
      "runtime": "Ollama",
      "runtime_version": "captured in install gate",
      "hardware_path": "CUDA or CPU fallback",
      "api_route": "native /api/chat",
      "model_id_visible": true,
      "architecture_supported": true,
      "artifact_supported": true,
      "quantization_supported": true,
      "runtime_available": true,
      "route_supported": true,
      "tokenizer_source": "runtime metadata or model package",
      "chat_template_source": "Modelfile or runtime metadata",
      "stop_policy": "runtime default checked in template runner",
      "model_metadata_card": "LLM/Study/Local LLM Model Metadata Card Runner",
      "artifact_custody_proof": "LLM/Study/Local LLM Artifact Custody Audit Runner",
      "hardware_sizing_proof": "LLM/Study/Local LLM Hardware Sizing Runner",
      "next_route": "LLM/Study/Local LLM First Runtime Health Snapshot"
    }
  ]
}
```

Use `partial_reason` when a route or feature is deliberately partial. Use `accepted_partial` only when that partial support is acceptable for this workload and the missing feature has a next-route proof.

## Standard-Library Runner

Save the code block as `local_llm_runtime_compatibility_runner.py` or extract it directly from this note.

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


REQUIRED_FIELDS = [
    "candidate_id",
    "model_id",
    "source",
    "artifact_container",
    "architecture",
    "quantization",
    "runtime",
    "hardware_path",
    "api_route",
]

SUPPORT_FIELDS = [
    "architecture_supported",
    "artifact_supported",
    "quantization_supported",
    "runtime_available",
    "route_supported",
    "model_id_visible",
]

DOMAIN_ROUTE = {
    "artifact": "LLM/Study/Local LLM Artifact Custody Audit Runner",
    "hardware": "LLM/Study/Local LLM Hardware Sizing Runner",
    "template": "LLM/Study/Chat Template and Tokenizer Compatibility Runner",
    "api": "LLM/Study/Local LLM OpenAI-Compatible API Contract Runner",
    "selection": "LLM/Study/Local LLM Model Selection Runner",
    "matrix": "LLM/Study/Local LLM Runtime and Model Compatibility Matrix",
    "health": "LLM/Study/Local LLM First Runtime Health Snapshot",
}


def utc_iso() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def slug(value: str) -> str:
    text_value = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return text_value or "local-llm-runtime-compatibility"


def load_manifest() -> tuple[Path, dict[str, Any]]:
    raw_path = os.environ.get("LOCAL_LLM_RUNTIME_COMPATIBILITY_MANIFEST")
    if len(sys.argv) > 1:
        raw_path = sys.argv[1]
    if not raw_path:
        raise ValueError("Set LOCAL_LLM_RUNTIME_COMPATIBILITY_MANIFEST or pass a manifest path.")
    path = Path(raw_path).expanduser().resolve()
    return path, json.loads(path.read_text(encoding="utf-8"))


def text(value: Any) -> str:
    return str(value or "").strip()


def list_value(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def bool_value(value: Any) -> bool | None:
    if value is None or value == "":
        return None
    if isinstance(value, bool):
        return value
    lowered = str(value).strip().lower()
    if lowered in {"1", "true", "yes", "y", "pass", "supported", "available", "visible"}:
        return True
    if lowered in {"0", "false", "no", "n", "fail", "unsupported", "unavailable", "missing"}:
        return False
    return None


def status_text(value: Any) -> str:
    normalized = text(value).lower().replace("_", "-")
    if normalized in {"pass", "passed", "ready", "compatible", "supported", "ok"}:
        return "pass"
    if normalized in {"fail", "failed", "incompatible", "unsupported", "rejected", "unsafe"}:
        return "fail"
    if normalized in {"partial", "partially-compatible", "limited"}:
        return "partial"
    if normalized in {"hold", "unknown", "pending", "missing", "untested", ""}:
        return "hold"
    return normalized


def wiki_link(route: str) -> str:
    route = text(route)
    if not route:
        return "[" + "[" + DOMAIN_ROUTE["matrix"] + "]" + "]"
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


def support_label(candidate: dict[str, Any], field: str) -> str:
    value = bool_value(candidate.get(field))
    if value is True:
        return "pass"
    if value is False:
        return "fail"
    return status_text(candidate.get(field))


def requires_chat_template(candidate: dict[str, Any], workload: dict[str, Any]) -> bool:
    if bool_value(candidate.get("requires_chat_template")) is not None:
        return bool_value(candidate.get("requires_chat_template")) is True
    workload_flag = bool_value(workload.get("requires_chat_template"))
    if workload_flag is not None:
        return workload_flag is True
    shape = text(workload.get("required_output_shape")).lower()
    return shape in {"chat", "prose", "json", "tools", "tool calls", "citations"} or "chat" in text(candidate.get("model_class")).lower()


def requires_openai_route(candidate: dict[str, Any], workload: dict[str, Any]) -> bool:
    value = bool_value(candidate.get("requires_openai_compatible"))
    if value is not None:
        return value
    value = bool_value(workload.get("requires_openai_compatible"))
    if value is not None:
        return value
    return "openai" in text(candidate.get("api_route")).lower()


def route_for_candidate(candidate: dict[str, Any], status: str, first_owner: str) -> str:
    route = text(candidate.get("next_route"))
    if route:
        return route
    if status == "pass":
        return DOMAIN_ROUTE["health"]
    if first_owner in DOMAIN_ROUTE:
        return DOMAIN_ROUTE[first_owner]
    if status == "fail":
        return DOMAIN_ROUTE["selection"]
    return DOMAIN_ROUTE["matrix"]


def evaluate_candidate(candidate: dict[str, Any], workload: dict[str, Any]) -> dict[str, Any]:
    candidate_id = text(candidate.get("candidate_id") or candidate.get("id") or candidate.get("name")) or "unnamed-candidate"
    findings: list[dict[str, str]] = []

    for field in REQUIRED_FIELDS:
        if not text(candidate.get(field)):
            findings.append(finding(
                "hold",
                "matrix",
                f"Required compatibility field `{field}` is missing.",
                candidate_id,
                f"Fill `{field}` from the model card, artifact card, runtime setting, or route proof.",
            ))

    for field in SUPPORT_FIELDS:
        label = support_label(candidate, field)
        if label == "fail":
            owner = "artifact" if field in {"architecture_supported", "artifact_supported", "quantization_supported"} else "api"
            if field == "runtime_available":
                owner = "matrix"
            findings.append(finding(
                "fail",
                owner,
                f"Compatibility check `{field}` is explicitly false.",
                field,
                "Reject this candidate for the selected runtime path or choose a different runtime/model/artifact.",
            ))
        elif label in {"hold", "unknown", "pending", "missing", "untested", ""}:
            findings.append(finding(
                "hold",
                "matrix",
                f"Compatibility check `{field}` is not proven.",
                field,
                f"Record source-checked evidence for `{field}` before serving or benchmarking.",
            ))
        elif label == "partial":
            if bool_value(candidate.get("accepted_partial")) is True and text(candidate.get("partial_reason")):
                findings.append(finding(
                    "hold",
                    "api",
                    f"Compatibility check `{field}` is partial but accepted for this workload.",
                    text(candidate.get("partial_reason")),
                    "Keep the partial-support reason linked and route missing features to API or template proof.",
                ))
            else:
                findings.append(finding(
                    "hold",
                    "api",
                    f"Compatibility check `{field}` is partial without an accepted partial reason.",
                    field,
                    "Add `partial_reason` and `accepted_partial`, or choose a route/runtime that fully supports the workload.",
                ))

    if not text(candidate.get("artifact_custody_proof")):
        findings.append(finding(
            "hold",
            "artifact",
            "Artifact custody proof is missing.",
            candidate_id,
            "Run or link the artifact custody audit before runtime compatibility supports serving evidence.",
        ))
    if not text(candidate.get("hardware_sizing_proof")):
        findings.append(finding(
            "hold",
            "hardware",
            "Hardware sizing proof is missing.",
            candidate_id,
            "Run or link the hardware sizing runner before compatibility supports model pull or serving.",
        ))

    if not text(candidate.get("tokenizer_source")):
        findings.append(finding(
            "hold",
            "template",
            "Tokenizer source is missing.",
            candidate_id,
            "Record tokenizer files, runtime metadata, or a token-count sanity source.",
        ))

    if requires_chat_template(candidate, workload) and not text(candidate.get("chat_template_source")):
        findings.append(finding(
            "hold",
            "template",
            "Chat template source is missing for a chat-like workload.",
            text(workload.get("required_output_shape")),
            "Run or link the chat template and tokenizer compatibility runner before quality or benchmark decisions.",
        ))

    if not text(candidate.get("stop_policy")):
        findings.append(finding(
            "hold",
            "template",
            "Stop/EOS policy is missing.",
            candidate_id,
            "Record the stop strings, EOS behavior, or runtime default before interpreting prompt continuation failures.",
        ))

    openai_status = status_text(candidate.get("openai_compatible"))
    if requires_openai_route(candidate, workload):
        if openai_status == "fail":
            findings.append(finding(
                "fail",
                "api",
                "OpenAI-compatible route is required but marked incompatible.",
                text(candidate.get("api_route")),
                "Use a native client path, a different runtime, or the OpenAI-compatible API contract runner to prove a partial route.",
            ))
        elif openai_status in {"hold", "unknown", "pending", "missing", "untested", ""}:
            findings.append(finding(
                "hold",
                "api",
                "OpenAI-compatible route is required but not proven.",
                text(candidate.get("api_route")),
                "Run the OpenAI-compatible API contract runner before pointing generic clients at this endpoint.",
            ))
        elif openai_status == "partial" and not text(candidate.get("partial_reason")):
            findings.append(finding(
                "hold",
                "api",
                "OpenAI-compatible route is partial without a reason.",
                text(candidate.get("api_route")),
                "Record which OpenAI-compatible features work and which are missing.",
            ))

    explicit_status = status_text(candidate.get("compatibility_status"))
    if explicit_status == "fail":
        findings.append(finding(
            "fail",
            "matrix",
            "Candidate compatibility status is explicitly failed.",
            candidate_id,
            "Resolve or reject the failed compatibility card before serving.",
        ))

    fail_count = sum(1 for item in findings if item["level"] == "fail")
    hold_count = sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        status = "fail"
        decision = "candidate_incompatible"
    elif hold_count:
        status = "hold"
        decision = "candidate_needs_compatibility_evidence"
    else:
        status = "pass"
        decision = "candidate_runtime_compatible"

    first_owner = findings[0]["owner"] if findings else "health"
    return {
        "candidate_id": candidate_id,
        "status": status,
        "decision": decision,
        "model_id": text(candidate.get("model_id")),
        "runtime": text(candidate.get("runtime")),
        "artifact_container": text(candidate.get("artifact_container")),
        "quantization": text(candidate.get("quantization")),
        "hardware_path": text(candidate.get("hardware_path")),
        "api_route": text(candidate.get("api_route")),
        "openai_compatible": text(candidate.get("openai_compatible")),
        "tokenizer_source": text(candidate.get("tokenizer_source")),
        "chat_template_source": text(candidate.get("chat_template_source")),
        "artifact_custody_proof": text(candidate.get("artifact_custody_proof")),
        "hardware_sizing_proof": text(candidate.get("hardware_sizing_proof")),
        "next_route": route_for_candidate(candidate, status, first_owner),
        "next_action": findings[0]["action"] if findings else "Load or health-check this runtime path before endpoint smoke testing.",
        "findings": findings,
    }


def csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "candidate_id",
        "status",
        "decision",
        "model_id",
        "runtime",
        "artifact_container",
        "quantization",
        "hardware_path",
        "api_route",
        "openai_compatible",
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
        f"# Local LLM Runtime Compatibility - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Workload: `{record['workload_summary']}`",
        f"- Candidates: `{record['candidate_count']}`",
        f"- Pass/Hold/Fail: `{record['pass_count']}` / `{record['hold_count']}` / `{record['fail_count']}`",
        "",
        "## Candidate Results",
        "",
        "| Candidate | Status | Runtime | Artifact | Quantization | Route | Next route |",
        "|---|---|---|---|---|---|---|",
    ]
    for row in record["candidates"]:
        lines.append(
            "| "
            + " | ".join([
                md_cell(row["candidate_id"]),
                md_cell(row["status"]),
                md_cell(row["runtime"]),
                md_cell(row["artifact_container"]),
                md_cell(row["quantization"]),
                md_cell(row["api_route"]),
                md_cell(wiki_link(row["next_route"])),
            ])
            + " |"
        )
    lines.extend(["", "## Next Actions", ""])
    for row in record["candidates"]:
        lines.append(f"- `{row['candidate_id']}` -> {wiki_link(row['next_route'])}: {row['next_action']}")
    lines.append("")
    return "\n".join(lines)


def workload_summary(workload: dict[str, Any]) -> str:
    name = text(workload.get("name") or "unspecified")
    shape = text(workload.get("required_output_shape") or "unspecified")
    openai = text(workload.get("requires_openai_compatible") or "unspecified")
    return f"name={name}; output_shape={shape}; requires_openai_compatible={openai}"


def main() -> int:
    manifest_path, manifest = load_manifest()
    workload = manifest.get("workload") or {}
    if not isinstance(workload, dict):
        raise ValueError("Manifest workload must be an object.")
    candidates = manifest.get("candidates", manifest.get("rows"))
    if not isinstance(candidates, list) or not all(isinstance(row, dict) for row in candidates):
        raise ValueError("Manifest candidates or rows must be a list of objects.")

    run_id = str(manifest.get("run_id") or os.environ.get("LOCAL_LLM_RUNTIME_COMPATIBILITY_RUN_ID") or f"{utc_stamp()}-{slug(manifest_path.stem)}")
    run_root_value = os.environ.get("LOCAL_LLM_RUNTIME_COMPATIBILITY_RUN_ROOT") or manifest.get("run_root", "local-llm-runtime-compatibility-runs")
    run_root = Path(str(run_root_value)).expanduser()
    if not run_root.is_absolute():
        run_root = manifest_path.parent / run_root
    run_root = run_root.resolve()
    run_dir = run_root / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    evaluated = [evaluate_candidate(dict(candidate), workload) for candidate in candidates]
    pass_count = sum(1 for row in evaluated if row["status"] == "pass")
    hold_count = sum(1 for row in evaluated if row["status"] == "hold")
    fail_count = sum(1 for row in evaluated if row["status"] == "fail")
    if pass_count:
        status = "pass"
        decision = "runtime_compatibility_ready"
    elif hold_count:
        status = "hold"
        decision = "runtime_compatibility_incomplete"
    else:
        status = "fail"
        decision = "runtime_compatibility_failed"

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "manifest_path": str(manifest_path),
        "vault_root": str(Path(str(manifest.get("vault_root") or os.environ.get("LOCAL_LLM_RUNTIME_COMPATIBILITY_VAULT_ROOT") or manifest_path.parent)).expanduser()),
        "run_root": str(run_root),
        "workload_summary": workload_summary(workload),
        "candidate_count": len(evaluated),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "candidates": evaluated,
        "outputs": {},
    }

    json_path = run_dir / f"{run_id}-runtime-compatibility.json"
    markdown_path = run_dir / f"{run_id}-runtime-compatibility.md"
    csv_path = run_dir / f"{run_id}-runtime-compatibility.csv"
    jsonl_path = run_root / "local-llm-runtime-compatibility-runs.jsonl"
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
$env:LOCAL_LLM_RUNTIME_COMPATIBILITY_MANIFEST = "D:\llm-runs\runtime-compatibility\runtime-compatibility-manifest.json"
$env:LOCAL_LLM_RUNTIME_COMPATIBILITY_RUN_ROOT = "D:\llm-runs\runtime-compatibility"
$env:LOCAL_LLM_RUNTIME_COMPATIBILITY_VAULT_ROOT = "D:\Vaults\PersonalKB"
python .\local_llm_runtime_compatibility_runner.py
```

## Reading The Result

| Runner status | Meaning | Next route |
|---|---|---|
| `pass/runtime_compatibility_ready` | at least one candidate has complete source, artifact, runtime, tokenizer/template, route, custody, and sizing evidence | [[LLM/Study/Local LLM First Runtime Health Snapshot]] or [[LLM/Study/Local LLM First Model Pull Gate]] |
| `hold/runtime_compatibility_incomplete` | required compatibility evidence is missing, unknown, partial, or not linked | follow each candidate's `next_route` |
| `fail/runtime_compatibility_failed` | every candidate has an explicit incompatibility, rejected route, unsupported artifact, or unsupported quantization path | [[LLM/Study/Local LLM Model Selection Runner]] or choose a different runtime/artifact |

A `pass` result says the runtime path is ready to load or health-check. It does not prove endpoint behavior, API compatibility, quality, or throughput.

## Capstone Row

| Evidence | Output |
|---|---|
| Runtime compatibility runner | `<run-id>-runtime-compatibility.json`, `<run-id>-runtime-compatibility.md`, `<run-id>-runtime-compatibility.csv`, and one `local-llm-runtime-compatibility-runs.jsonl` row |

## Completion Gate

This runner is useful when:

- [ ] every candidate has model id, source, artifact container, architecture, quantization, runtime, hardware path, and API route
- [ ] architecture, artifact, quantization, runtime availability, route support, and model-id visibility are explicit
- [ ] artifact custody and hardware sizing outputs are linked before serving evidence depends on them
- [ ] tokenizer source, chat-template source, and stop/EOS policy are explicit for chat-like workloads
- [ ] OpenAI-compatible support is audited when a generic client will call the endpoint
- [ ] partial compatibility has an accepted reason and a route for missing features
- [ ] output JSON, Markdown, CSV, and JSONL artifacts are saved before model pull, runtime health, smoke testing, or benchmarking

## References

- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM Runtime Stack Anatomy]]
- [[LLM/Study/Local LLM Artifact Custody Audit Runner]]
- [[LLM/Study/Local LLM Model Acquisition and License Gate Runner]]
- [[LLM/Study/Local LLM Model Metadata Card Runner]]
- [[LLM/Study/Local LLM Hardware Sizing Runner]]
- [[LLM/Study/Local LLM Model Selection Runner]]
- [[LLM/Study/Local LLM First Model Pull Gate]]
- [[LLM/Study/Local LLM First Runtime Health Snapshot]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Runner]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Lab]]
- [[LLM/Study/Local LLM Runtime Comparison Lab]]
- [[LLM/Study/Local LLM First Smoke Request Runner]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
