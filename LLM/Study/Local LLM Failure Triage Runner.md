---
tags: [study, llm, inference, local-llm, troubleshooting, diagnostics, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice, deep-dive]
last-verified: 2026-06-15
---

# Local LLM Failure Triage Runner

> **One-line summary** A failed local LLM run is useful only when the symptom is tied to one failed layer, one evidence packet, one mechanism owner, and one controlled next change.

Use this after [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]] when the diagnosis needs to be repeatable. The decision tree teaches the route. This runner validates the saved failure packet and turns it into JSON, Markdown, CSV, and JSONL evidence for the capstone workbook.

This runner does not call a model, inspect live ports, start a server, or scrape logs. It audits the artifacts you already saved from preflight, runtime health, client harness, request lifecycle, benchmark, quality, RAG, tool, security, or operations notes.

## What This Proves

| Gate | Evidence checked | Why it matters |
|---|---|---|
| Symptom | observed failure, command, status code, log excerpt, or output file | prevents vague "the model is bad" diagnoses |
| Failed layer | environment, artifact, model fit, server, route, client, template, context, performance, quality, RAG, tool, security, or operations | fixes the lowest unproven layer first |
| Proof link | vault-relative proof path or Obsidian link | keeps diagnosis auditable after the terminal scrollback is gone |
| Mechanism owner | request phase, academic mechanism, or metric family | connects practical failure to tokens, prefill, decode, KV cache, routing, evaluation, or safety |
| Ruled-out layers | explicit checks that passed or were not relevant | prevents changing multiple variables at once |
| Controlled next action | one next test, one rollback, one config change, or one rerun route | turns debugging into a reproducible experiment |

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "first-smoke-connection-refused",
  "run_root": "D:/llm-runs/failure-triage",
  "vault_root": "D:/Vaults/PersonalKB",
  "workload": "private local research assistant",
  "rows": [
    {
      "id": "smoke-001",
      "status": "pass",
      "symptom": "connection refused from OpenAI-compatible smoke request",
      "failed_layer": "server_process",
      "proof": "LLM/Study/Local LLM First Smoke Request Runner.md",
      "observed_error": "connect ECONNREFUSED 127.0.0.1:11434",
      "command": "curl http://127.0.0.1:11434/v1/models",
      "request_phase": "route reachability before inference",
      "academic_owner": "runtime route, not model quality",
      "ruled_out_layers": ["model_selection", "quality"],
      "one_change": "start the runtime service and rerun /v1/models before chat",
      "next_action": "route to Local LLM First Runtime Health Snapshot"
    }
  ]
}
```

`proof` may be an absolute path, a vault-relative path, an Obsidian note path, or an Obsidian link. If no failure occurred, include `no_failure_observed: true`, `status: pass`, and a proof link to the successful run.

## Layer Names

Use these canonical layer names when possible:

| Layer | Typical symptom | Next route |
|---|---|---|
| `environment` | runtime command missing, GPU invisible, disk/cache not ready | [[LLM/Study/Local LLM Environment Preflight Lab]] |
| `model_acquisition` | gated model, license/auth failure, floating source | [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]] |
| `artifact_cache` | wrong cache path, missing file, conversion/import drift | [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab]] |
| `model_fit` | OOM, unsupported size, context too large | [[LLM/Study/Local LLM Model and Hardware Sizing Guide]] |
| `runtime_compatibility` | artifact format, quantization, tokenizer, template, route mismatch | [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]] |
| `server_process` | connection refused, listener missing, stale process | [[LLM/Study/Local LLM First Runtime Health Snapshot]] |
| `route_model` | 404, wrong model id, native versus `/v1` route mix-up | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]] |
| `client` | SDK timeout, body shape, parser, retry, request config | [[LLM/Study/Local LLM First Client Harness Runner]] |
| `streaming` | non-streaming works but streaming chunks fail | [[LLM/Study/Local LLM First Streaming Timing Runner]] |
| `request_lifecycle` | prompt assembly, stop, detokenization, app handling | [[LLM/Study/LLM Inference Request Lifecycle Runner]] |
| `chat_template` | role leakage, ignored system message, exposed markers | [[LLM/Study/Chat Template and Tokenizer Compatibility Runner]] |
| `context_kv` | long prompt OOM, truncation, RAG/tool/history overflow | [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]] |
| `performance` | high TTFT, slow decode, memory pressure | [[LLM/Study/Local LLM Inference Metrics Field Guide]] |
| `scheduler_concurrency` | queueing, saturation, long-prompt interference | [[LLM/Study/Local LLM Scheduler Evidence Audit Runner]] |
| `prompt_cache` | repeated prefix not faster or privacy risk unclear | [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner]] |
| `speculative_decoding` | draft path slower, unsupported, or quality regressed | [[LLM/Study/Local LLM Speculative Decoding Runner]] |
| `quality` | plausible but wrong, invalid format, weak refusal | [[LLM/Study/Local LLM Quality Evaluation Harness]] |
| `rag` | retrieval miss, fake citation, unsupported answer | [[LLM/Study/Local RAG Evidence Runner]] |
| `tool` | bad schema, unsafe argument, missing tool result | [[LLM/Study/Local LLM Tool Calling and Structured Output Runner]] |
| `security_privacy` | endpoint exposure, log leak, data/export boundary failure | [[LLM/Study/Local LLM Security and Privacy Runner]] |
| `operations_lifecycle` | failure after restart, upgrade, cache move, rollback, or UI change | [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner]] |

## Standard-Library Runner

Save this as `local_llm_failure_triage_runner.py` inside the run folder. It uses only Python's standard library.

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


LINK_OPEN = "[" + "["
LINK_CLOSE = "]" + "]"

LAYER_ROUTES = {
    "environment": "LLM/Study/Local LLM Environment Preflight Lab",
    "model_acquisition": "LLM/Study/Local LLM Model Acquisition and Provenance Checklist",
    "artifact_cache": "LLM/Study/Local LLM Artifact Download Cache and Conversion Lab",
    "model_fit": "LLM/Study/Local LLM Model and Hardware Sizing Guide",
    "runtime_compatibility": "LLM/Study/Local LLM Runtime and Model Compatibility Matrix",
    "server_process": "LLM/Study/Local LLM First Runtime Health Snapshot",
    "route_model": "LLM/Study/Local LLM OpenAI-Compatible API Contract Runner",
    "api_contract": "LLM/Study/Local LLM OpenAI-Compatible API Contract Runner",
    "client": "LLM/Study/Local LLM First Client Harness Runner",
    "streaming": "LLM/Study/Local LLM First Streaming Timing Runner",
    "request_lifecycle": "LLM/Study/LLM Inference Request Lifecycle Runner",
    "chat_template": "LLM/Study/Chat Template and Tokenizer Compatibility Runner",
    "context_kv": "LLM/Study/Local LLM Context Window and Token Budgeting Runner",
    "performance": "LLM/Study/Local LLM Inference Metrics Field Guide",
    "quantization_offload": "LLM/Study/Local LLM Quantization and GPU Offload Lab",
    "scheduler_concurrency": "LLM/Study/Local LLM Scheduler Evidence Audit Runner",
    "prompt_cache": "LLM/Study/Local LLM Prompt Cache and KV Reuse Runner",
    "speculative_decoding": "LLM/Study/Local LLM Speculative Decoding Runner",
    "quality": "LLM/Study/Local LLM Quality Evaluation Harness",
    "rag": "LLM/Study/Local RAG Evidence Runner",
    "tool": "LLM/Study/Local LLM Tool Calling and Structured Output Runner",
    "security_privacy": "LLM/Study/Local LLM Security and Privacy Runner",
    "operations_lifecycle": "LLM/Study/Local LLM Service Lifecycle and Upgrade Runner",
    "deployment": "LLM/Study/LLM Deployment Readiness Audit Runner",
    "no_failure": "LLM/Study/LLM Mastery Capstone Workbook",
}

LAYER_ALIASES = {
    "env": "environment",
    "machine": "environment",
    "gpu": "environment",
    "download": "model_acquisition",
    "provenance": "model_acquisition",
    "cache": "artifact_cache",
    "conversion": "artifact_cache",
    "import": "artifact_cache",
    "sizing": "model_fit",
    "oom": "model_fit",
    "memory": "model_fit",
    "runtime": "runtime_compatibility",
    "compatibility": "runtime_compatibility",
    "server": "server_process",
    "listener": "server_process",
    "route": "route_model",
    "model_id": "route_model",
    "api": "api_contract",
    "openai_contract": "api_contract",
    "sdk": "client",
    "stream": "streaming",
    "lifecycle": "operations_lifecycle",
    "template": "chat_template",
    "tokenizer": "chat_template",
    "context": "context_kv",
    "kv_cache": "context_kv",
    "latency": "performance",
    "benchmark": "performance",
    "scheduler": "scheduler_concurrency",
    "concurrency": "scheduler_concurrency",
    "queue": "scheduler_concurrency",
    "prefix_cache": "prompt_cache",
    "speculative": "speculative_decoding",
    "security": "security_privacy",
    "privacy": "security_privacy",
    "ops": "operations_lifecycle",
    "operations": "operations_lifecycle",
    "none": "no_failure",
    "no_failure_observed": "no_failure",
}

STATUS_VALUES = {
    "pass": "pass",
    "passed": "pass",
    "ready": "pass",
    "diagnosed": "pass",
    "no_failure": "pass",
    "hold": "hold",
    "pending": "hold",
    "blocked": "hold",
    "incomplete": "hold",
    "missing": "hold",
    "fail": "fail",
    "failed": "fail",
    "unsafe": "fail",
    "unresolved": "fail",
}

STATUS_RANK = {"pass": 0, "hold": 1, "fail": 2}


def utc_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def slug(value: Any) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value or "").strip().lower())
    return text.strip("-") or "local-llm-failure-triage"


def norm(value: Any) -> str:
    return str(value or "").strip().lower().replace(" ", "_").replace("-", "_").replace("/", "_")


def display(value: Any) -> str:
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=True)
    return str(value if value is not None else "")


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
        return [part.strip() for part in re.split(r"[,;]", stripped) if part.strip()]
    return [str(value).strip()] if str(value).strip() else []


def bool_value(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if value in (None, ""):
        return default
    text = norm(value)
    if text in {"true", "yes", "y", "1", "pass", "passed", "no_failure"}:
        return True
    if text in {"false", "no", "n", "0", "fail", "failed", "hold"}:
        return False
    return default


def status_value(value: Any) -> str:
    return STATUS_VALUES.get(norm(value), "hold")


def canonical_layer(value: Any) -> str:
    layer = norm(value)
    return LAYER_ALIASES.get(layer, layer)


def has_text(row: dict[str, Any], *names: str) -> bool:
    return any(str(row.get(name) or "").strip() for name in names)


def proof_candidates(vault_root: Path, proof: str) -> list[Path]:
    text = proof.strip()
    if not text:
        return []
    if text.startswith(LINK_OPEN) and text.endswith(LINK_CLOSE):
        text = text[2:-2].split("|", 1)[0].split("#", 1)[0]
    text = text.replace("/", os.sep)
    path = Path(text).expanduser()
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


def finding(level: str, owner: str, text: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "owner": owner,
        "finding": text,
        "evidence": evidence,
        "action": action,
    }


def load_manifest() -> tuple[Path, dict[str, Any]]:
    manifest_path = os.environ.get("LOCAL_LLM_FAILURE_TRIAGE_MANIFEST")
    if not manifest_path:
        raise ValueError("Set LOCAL_LLM_FAILURE_TRIAGE_MANIFEST to a JSON manifest path.")
    path = Path(manifest_path).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open("r", encoding="utf-8") as handle:
        manifest = json.load(handle)
    if not isinstance(manifest, dict):
        raise ValueError("Manifest must be a JSON object.")
    return path, manifest


def evidence_present(row: dict[str, Any]) -> bool:
    if has_text(row, "proof", "proof_path", "evidence_path", "log_file", "response_file", "request_file"):
        return True
    if has_text(row, "observed_error", "log_excerpt", "command", "http_status", "request_path", "response_excerpt", "metric", "measurement"):
        return True
    return bool(list_value(row.get("evidence")) or list_value(row.get("evidence_paths")))


def evaluate_row(row: dict[str, Any], vault_root: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    row_id = str(row.get("id") or row.get("row_id") or row.get("failure_id") or "")
    status = status_value(row.get("status") or row.get("result"))
    no_failure = bool_value(row.get("no_failure_observed"), False) or status == "pass" and norm(row.get("failed_layer")) in {"no_failure", "none"}
    layer = "no_failure" if no_failure else canonical_layer(row.get("failed_layer") or row.get("layer") or "")
    proof = str(row.get("proof") or row.get("proof_path") or row.get("evidence_path") or "")
    findings: list[dict[str, str]] = []

    if not row_id:
        findings.append(finding("hold", "manifest", "Failure row has no stable id.", display(row), "Give every row an id or failure_id."))

    if not has_text(row, "symptom", "observed_error", "summary") and not no_failure:
        findings.append(finding("hold", "symptom", "Failure row has no symptom or observed error.", row_id, "Record the visible failure before diagnosing the layer."))

    if layer not in LAYER_ROUTES:
        findings.append(finding("hold", "layer", "Failed layer is missing or not canonical.", display(row.get("failed_layer")), "Use one of the canonical layer names from the runner note."))

    proof_ok = False
    proof_resolved = ""
    if proof:
        proof_ok, proof_resolved = proof_exists(vault_root, proof)
        if not proof_ok:
            findings.append(finding("hold", "proof", "Proof link or path does not resolve in the vault.", proof_resolved, "Fix the proof path or create the linked evidence artifact."))
    else:
        findings.append(finding("hold", "proof", "Failure row has no proof link or path.", row_id or layer, "Link the saved terminal output, request file, log note, benchmark row, or run sheet."))

    if not evidence_present(row):
        findings.append(finding("hold", "evidence", "Failure row has no observable evidence field.", row_id or layer, "Add command output, error text, HTTP status, request/response file, log excerpt, or metric."))

    if not no_failure and not has_text(row, "request_phase", "academic_owner", "mechanism", "metric_family"):
        findings.append(finding("hold", "mechanism", "Failure row has no mechanism or request-phase owner.", row_id or layer, "Name the mechanism: environment, route, tokenization, prefill, decode, KV cache, sampler, retrieval, tool, quality, or security."))

    if not no_failure and not list_value(row.get("ruled_out_layers")):
        findings.append(finding("hold", "control", "Failure row has no ruled-out layer list.", row_id or layer, "Record at least one layer checked before changing the next variable."))

    changes = list_value(row.get("changes_made") or row.get("controlled_changes"))
    if len(changes) > 1:
        findings.append(finding("hold", "control", "Failure row changes multiple variables at once.", ", ".join(changes), "Split the diagnosis into one row per controlled change."))

    if not has_text(row, "one_change", "next_action", "rerun_route", "rollback_action"):
        findings.append(finding("hold", "next_action", "Failure row has no controlled next action.", row_id or layer, "Add one rerun route, fix, rollback, or next test."))

    if status == "fail":
        findings.append(finding("fail", layer or "failure", "Failure row is explicitly unresolved or unsafe.", row_id or layer, "Resolve the failed layer before accepting downstream benchmark, quality, or deployment evidence."))
    elif status != "pass":
        findings.append(finding("hold", layer or "failure", "Failure row is not marked pass.", status, "Complete the diagnostic packet before using it as proof."))

    fail_count = sum(1 for item in findings if item["level"] == "fail")
    hold_count = sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        final_status = "fail"
        decision = "failure_unresolved"
    elif hold_count:
        final_status = "hold"
        decision = "triage_incomplete"
    else:
        final_status = "pass"
        decision = "diagnosis_ready"

    return {
        "row_id": row_id,
        "status": final_status,
        "declared_status": status,
        "decision": decision,
        "symptom": str(row.get("symptom") or row.get("observed_error") or row.get("summary") or ""),
        "failed_layer": layer,
        "route": LAYER_ROUTES.get(layer, "LLM/Study/Local LLM Troubleshooting Decision Tree"),
        "proof": proof,
        "proof_resolved": proof_resolved,
        "proof_exists": proof_ok,
        "request_phase": str(row.get("request_phase") or row.get("mechanism") or row.get("academic_owner") or row.get("metric_family") or ""),
        "ruled_out_layers": list_value(row.get("ruled_out_layers")),
        "next_action": str(row.get("next_action") or row.get("one_change") or row.get("rerun_route") or row.get("rollback_action") or ""),
        "findings": findings,
    }


def group_summary(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    layers = sorted({row["failed_layer"] for row in rows})
    summary = []
    for layer in layers:
        subset = [row for row in rows if row["failed_layer"] == layer]
        summary.append({
            "layer": layer,
            "route": LAYER_ROUTES.get(layer, "LLM/Study/Local LLM Troubleshooting Decision Tree"),
            "row_count": len(subset),
            "pass_count": sum(1 for row in subset if row["status"] == "pass"),
            "hold_count": sum(1 for row in subset if row["status"] == "hold"),
            "fail_count": sum(1 for row in subset if row["status"] == "fail"),
        })
    return summary


def csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = [
        "row_id",
        "status",
        "declared_status",
        "decision",
        "symptom",
        "failed_layer",
        "route",
        "proof",
        "proof_resolved",
        "proof_exists",
        "request_phase",
        "next_action",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({name: row.get(name, "") for name in fieldnames})


def md_cell(value: Any) -> str:
    return display(value).replace("|", "\\|").replace("\n", " ")


def render_markdown(record: dict[str, Any]) -> str:
    lines = [
        f"# Local LLM Failure Triage - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Workload: `{record['workload']}`",
        f"- Next action: {record['next_action']}",
        "",
        "## Rows",
        "",
        "| Row | Status | Failed layer | Symptom | Next action |",
        "|---|---|---|---|---|",
    ]
    for row in record["rows"]:
        lines.append("| " + " | ".join([
            md_cell(row["row_id"]),
            md_cell(row["status"]),
            md_cell(row["failed_layer"]),
            md_cell(row["symptom"]),
            md_cell(row["next_action"]),
        ]) + " |")
    lines.extend(["", "## Layer Summary", "", "| Layer | Rows | Pass | Hold | Fail | Route |", "|---|---:|---:|---:|---:|---|"])
    for row in record["layer_summary"]:
        lines.append("| " + " | ".join([
            md_cell(row["layer"]),
            md_cell(row["row_count"]),
            md_cell(row["pass_count"]),
            md_cell(row["hold_count"]),
            md_cell(row["fail_count"]),
            md_cell(row["route"]),
        ]) + " |")
    lines.extend(["", "## Findings", ""])
    if record["findings"]:
        for item in record["findings"]:
            lines.append(f"- `{item['level']}` {item['owner']}: {item['finding']} -> {item['action']}")
    else:
        lines.append("- No blocking findings.")
    return "\n".join(lines) + "\n"


def main() -> int:
    manifest_path, manifest = load_manifest()
    vault_root = Path(manifest.get("vault_root") or os.environ.get("LOCAL_LLM_FAILURE_TRIAGE_VAULT_ROOT") or manifest_path.parent).expanduser().resolve()
    run_id = str(manifest.get("run_id") or os.environ.get("LOCAL_LLM_FAILURE_TRIAGE_RUN_ID") or f"{utc_stamp()}-{slug(manifest_path.stem)}")
    run_root_value = os.environ.get("LOCAL_LLM_FAILURE_TRIAGE_RUN_ROOT") or manifest.get("run_root", "local-llm-failure-triage-runs")
    run_root = Path(run_root_value).expanduser()
    if not run_root.is_absolute():
        run_root = manifest_path.parent / run_root
    run_dir = run_root / slug(run_id)
    run_dir.mkdir(parents=True, exist_ok=True)

    raw_rows = manifest.get("rows")
    if raw_rows is None:
        raw_rows = manifest.get("failures")
    if not isinstance(raw_rows, list) or not all(isinstance(row, dict) for row in raw_rows):
        raise ValueError("Manifest rows/failures must be a list of objects.")

    rows = [evaluate_row(dict(row), vault_root, manifest) for row in raw_rows]
    rows.sort(key=lambda row: (STATUS_RANK.get(row["status"], 3), row["failed_layer"], row["row_id"]))
    findings = [item for row in rows for item in row["findings"]]

    if not str(manifest.get("workload") or "").strip():
        findings.append(finding("hold", "workload", "Manifest has no workload.", "manifest", "Name the workload or local run this failure diagnosis serves."))

    fail_count = sum(1 for row in rows if row["status"] == "fail") + sum(1 for item in findings if item["level"] == "fail")
    hold_count = sum(1 for row in rows if row["status"] == "hold") + sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        status = "fail"
        decision = "failure_triage_failed"
        next_action = "Resolve the failed or unsafe layer before accepting downstream evidence."
    elif hold_count:
        status = "hold"
        decision = "failure_triage_incomplete"
        next_action = "Complete the first held diagnostic row before changing another variable."
    else:
        status = "pass"
        decision = "failure_triage_ready"
        next_action = "Link this output from the capstone workbook or the run sheet it diagnoses."

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "next_action": next_action,
        "manifest_path": str(manifest_path),
        "vault_root": str(vault_root),
        "workload": str(manifest.get("workload") or ""),
        "row_count": len(rows),
        "pass_count": sum(1 for row in rows if row["status"] == "pass"),
        "hold_count": sum(1 for row in rows if row["status"] == "hold"),
        "fail_count": sum(1 for row in rows if row["status"] == "fail"),
        "layer_summary": group_summary(rows),
        "findings": findings,
        "rows": rows,
        "outputs": {},
    }

    json_path = run_dir / f"{run_id}-failure-triage.json"
    markdown_path = run_dir / f"{run_id}-failure-triage.md"
    csv_path = run_dir / f"{run_id}-failure-triage.csv"
    jsonl_path = run_root / "local-llm-failure-triage-runs.jsonl"
    record["outputs"] = {
        "json": str(json_path),
        "markdown": str(markdown_path),
        "csv": str(csv_path),
        "jsonl": str(jsonl_path),
    }

    csv_write(csv_path, rows)
    json_path.write_text(json.dumps(record, indent=2, ensure_ascii=True), encoding="utf-8")
    markdown_path.write_text(render_markdown(record), encoding="utf-8")
    with jsonl_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=True) + "\n")

    print(json.dumps({
        "status": status,
        "decision": decision,
        "run_id": run_id,
        "row_count": len(rows),
        "pass_count": record["pass_count"],
        "hold_count": record["hold_count"],
        "fail_count": record["fail_count"],
        "finding_count": len(findings),
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
$env:LOCAL_LLM_FAILURE_TRIAGE_MANIFEST = "D:\llm-runs\failure-triage\failure-triage-manifest.json"
$env:LOCAL_LLM_FAILURE_TRIAGE_VAULT_ROOT = "D:\Vaults\PersonalKB"
$env:LOCAL_LLM_FAILURE_TRIAGE_RUN_ROOT = "D:\llm-runs\failure-triage"
python .\local_llm_failure_triage_runner.py
```

## Reading The Result

| Runner status | Meaning | Next route |
|---|---|---|
| `pass/failure_triage_ready` | every row names the symptom, failed layer, proof, mechanism owner, ruled-out layers, and controlled next action | link the output from the run sheet or capstone workbook |
| `hold/failure_triage_incomplete` | the diagnosis lacks proof, canonical layer, mechanism owner, ruled-out layer, or one controlled next action | complete the held row before changing another variable |
| `fail/failure_triage_failed` | a row is explicitly unresolved, unsafe, or failed | resolve the failed layer before accepting benchmark, quality, or deployment evidence |

## Capstone Row

| Evidence | Output |
|---|---|
| Failure triage runner | `<run-id>-failure-triage.json`, `<run-id>-failure-triage.md`, `<run-id>-failure-triage.csv`, and one `local-llm-failure-triage-runs.jsonl` row |

## Completion Gate

- [ ] every failure has a symptom or explicit no-failure row
- [ ] every failure names one canonical failed layer
- [ ] proof links resolve in the vault
- [ ] the row names the mechanism, request phase, or metric family that owns the symptom
- [ ] ruled-out layers are recorded before changing another variable
- [ ] there is exactly one controlled next change, rerun route, or rollback action
- [ ] outputs are linked from [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]] when the failure affects the capstone

## References

- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM First Runtime Health Snapshot]]
- [[LLM/Study/Local LLM First Smoke Request Runner]]
- [[LLM/Study/LLM Inference Request Lifecycle Runner]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Runner]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/Local LLM Scheduler Evidence Audit Runner]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner]]
- [[LLM/Study/Local LLM Speculative Decoding Runner]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local RAG Evidence Runner]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Runner]]
- [[LLM/Study/Local LLM Security and Privacy Runner]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
