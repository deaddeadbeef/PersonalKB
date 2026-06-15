---
tags: [study, llm, local-llm, application, integration, inference, evidence, audit, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice, deep-dive]
last-verified: 2026-06-15
---

# Local LLM Application Integration Evidence Runner

> **One-line summary** A local LLM is not application-ready because a client script worked once; it is application-ready when the app boundary, request path, response handling, failure behavior, privacy/logging policy, evaluation handoff, operations handoff, and promotion decision are all saved as evidence.

Use this after [[LLM/Study/Local LLM First Client Harness Runner|Local LLM First Client Harness Runner]] or [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] proves a reusable client call. Use it before [[LLM/Study/Local LLM Result Synthesis Runner|Local LLM Result Synthesis Runner]] or [[LLM/Study/LLM Deployment Readiness Audit Runner|LLM Deployment Readiness Audit Runner]] when a local endpoint is being wired into a real app, UI, CLI job, notebook workflow, RAG assistant, or tool loop.

This runner does not call a model, open a UI, run a web server, or judge answer quality. It audits a manifest of artifacts already produced by the app integration pass. That keeps the proof separate from one-off chat success, and it prevents a deployment memo from hiding missing app behavior behind endpoint-only evidence.

## What This Proves

| Evidence family | Checks | Why it matters |
|---|---|---|
| App contract | app name, entry point, user task, data class, integration scope | defines what the local model is actually serving |
| Endpoint contract | base URL, route, model id, endpoint proof | proves the app is pointed at the intended local route |
| Client flow | request builder, timeout or retry policy, log path | separates app code from hand-edited curl commands |
| User flow | trigger, transcript or visible output, expected user result | proves the model path is reachable through the real workflow |
| Response handling | parser, output path, acceptance check | catches the gap between text generation and usable application state |
| Failure handling | failed probe, fallback or next action, expected behavior | prevents silent hangs, wrong-model errors, and parse failures from looking like success |
| Privacy and logging | endpoint scope, prompt storage, output storage, retention or redaction | keeps local inference from leaking private prompts through logs or exports |
| Evaluation handoff | prompt id, benchmark or quality proof, decision field | connects app behavior to quality and performance evidence |
| Operations handoff | startup method, health check, owner or runbook | distinguishes a personal demo from a maintainable local service |
| Promotion decision | promote, hold, or reject with limitations and next route | decides whether this app integration can support the capstone or deployment memo |

Academic bridge: this is where model behavior becomes system behavior. Tokenization, context budget, decoding, tool output, RAG grounding, latency, and safety are useful only after the application can preserve request and response evidence at the boundary where a user or job consumes the model.

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "app-integration-001",
  "run_root": "D:/llm-runs/app-integration",
  "vault_root": "D:/Vaults/PersonalKB",
  "app_name": "personal research assistant",
  "rows": [
    {
      "id": "app-contract",
      "kind": "app_contract",
      "status": "pass",
      "critical": true,
      "proof": "D:/llm-runs/app-integration/app-contract.md",
      "app_name": "personal research assistant",
      "entry_point": "scripts/chat_local.py",
      "user_task": "answer questions over local notes",
      "data_class": "personal notes",
      "integration_scope": "loopback CLI"
    },
    {
      "id": "endpoint",
      "kind": "endpoint_contract",
      "status": "pass",
      "critical": true,
      "proof": "LLM/Study/Local LLM OpenAI-Compatible API Contract Runner.md",
      "base_url": "http://127.0.0.1:11434/v1",
      "route": "/chat/completions",
      "model_id": "qwen2.5:0.5b"
    }
  ]
}
```

`proof` may be an absolute path, a vault-relative path, an Obsidian note path, or an Obsidian link. If a kind is deliberately out of scope, include a row with `required: false` and `waiver_reason`.

## Required Evidence Kinds

By default, the runner expects one row for each kind:

| Kind | Required fields or acceptable substitute |
|---|---|
| `app_contract` | app name, entry point, user task, data class, integration scope |
| `endpoint_contract` | base URL, route, model id, proof |
| `client_flow` | client path, request builder, timeout policy, log path |
| `user_flow` | flow name, trigger, visible output or transcript path |
| `response_handling` | parser, output path, acceptance check |
| `failure_handling` | failure probe, expected behavior, fallback or next action |
| `privacy_logging` | endpoint scope, prompt storage, output storage, redaction or retention rule |
| `evaluation_handoff` | prompt id, benchmark or quality proof, decision field |
| `operations_handoff` | startup method, health check, owner or runbook |
| `promotion_decision` | decision, accepted limitations, next route |

Optional but recommended rows:

| Kind | Use when |
|---|---|
| `rag_tool_boundary` | the app uses retrieval, tools, structured output, or local actions |
| `concurrency_boundary` | the app has multiple users, batch jobs, queues, or background workers |

## Standard-Library Runner

Save this as `local_llm_application_integration_evidence_runner.py` inside the run folder. It uses only Python's standard library.

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
    "app_contract",
    "endpoint_contract",
    "client_flow",
    "user_flow",
    "response_handling",
    "failure_handling",
    "privacy_logging",
    "evaluation_handoff",
    "operations_handoff",
    "promotion_decision",
]

OPTIONAL_KINDS = [
    "rag_tool_boundary",
    "concurrency_boundary",
]

KIND_HINTS = {
    "app_contract": {
        "fields": ["app_name", "entry_point", "user_task", "data_class", "integration_scope"],
        "owner": "app",
        "pass_signal": "The app boundary and local-model use case are explicit.",
        "next_route": "LLM/Study/Local LLM Capstone Project Blueprint",
    },
    "endpoint_contract": {
        "fields": ["base_url", "route", "model_id"],
        "owner": "endpoint",
        "pass_signal": "The app uses the intended base URL, route, and served model id.",
        "next_route": "LLM/Study/Local LLM OpenAI-Compatible API Contract Runner",
    },
    "client_flow": {
        "fields": ["client_path", "request_builder", "timeout_policy", "log_path"],
        "owner": "client",
        "pass_signal": "The request is built by app code with timeout or retry behavior and durable logging.",
        "next_route": "LLM/Study/Local LLM Client Harness Lab",
    },
    "user_flow": {
        "fields": ["flow_name", "trigger"],
        "owner": "user-flow",
        "pass_signal": "The local model is reachable through the intended workflow.",
        "next_route": "LLM/Study/Local LLM Hands-On Practicum Sequence",
    },
    "response_handling": {
        "fields": ["parser", "output_path", "acceptance_check"],
        "owner": "application",
        "pass_signal": "The generated output is parsed or displayed in a checked application state.",
        "next_route": "LLM/Study/LLM Inference Request Lifecycle Runner",
    },
    "failure_handling": {
        "fields": ["failure_probe", "expected_behavior", "fallback_or_next_action"],
        "owner": "resilience",
        "pass_signal": "At least one app-level failure mode has a controlled behavior.",
        "next_route": "LLM/Study/Local LLM Failure Triage Runner",
    },
    "privacy_logging": {
        "fields": ["endpoint_scope", "prompt_storage", "output_storage", "redaction_or_retention"],
        "owner": "privacy",
        "pass_signal": "Prompt, output, logs, exports, and endpoint scope have a local privacy policy.",
        "next_route": "LLM/Study/Local LLM Security and Privacy Runner",
    },
    "evaluation_handoff": {
        "fields": ["prompt_id", "benchmark_or_quality_proof", "decision_field"],
        "owner": "evaluation",
        "pass_signal": "The app run can be compared against benchmark or quality evidence.",
        "next_route": "LLM/Study/Local LLM Quality Evaluation Harness",
    },
    "operations_handoff": {
        "fields": ["startup_method", "health_check", "owner_or_runbook"],
        "owner": "operations",
        "pass_signal": "Startup, health, and ownership are known before the app is promoted.",
        "next_route": "LLM/Study/Local LLM Observability and Operations Runner",
    },
    "promotion_decision": {
        "fields": ["decision", "accepted_limitations", "next_route"],
        "owner": "decision",
        "pass_signal": "The app integration has a promote, hold, or reject decision with limitations.",
        "next_route": "LLM/Study/Local LLM Result Synthesis Runner",
    },
    "rag_tool_boundary": {
        "fields": ["boundary_type", "policy", "proof"],
        "owner": "extension",
        "pass_signal": "RAG, tools, structured output, or local actions have a checked boundary.",
        "next_route": "LLM/Study/Local LLM Tool Calling and Structured Output Runner",
    },
    "concurrency_boundary": {
        "fields": ["expected_concurrency", "backpressure_policy", "proof"],
        "owner": "capacity",
        "pass_signal": "Multi-user, queue, batch, or worker behavior has capacity evidence.",
        "next_route": "LLM/Study/Local LLM Concurrency and Batch Throughput Runner",
    },
}

STATUS_RANK = {"fail": 0, "hold": 1, "pass": 2, "skip": 3}


def utc_iso() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def slug(value: str) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip().lower())
    return text.strip("-") or "app-integration"


def norm(value: Any) -> str:
    return str(value or "").strip().lower().replace("-", "_").replace(" ", "_")


def display(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value).strip()


def bool_value(value: Any, default: bool = False) -> bool:
    if value is None or value == "":
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y", "pass", "required"}


def list_value(value: Any) -> list[Any]:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return value
    return [value]


def md_cell(value: Any) -> str:
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=True)
    return display(value).replace("|", "\\|").replace("\n", " ")


def unwrap_link(value: str) -> str:
    text = display(value)
    open_link = "[" * 2
    close_link = "]" * 2
    if text.startswith(open_link) and text.endswith(close_link):
        text = text[2:-2]
        if "|" in text:
            text = text.split("|", 1)[0]
    if "#" in text:
        text = text.split("#", 1)[0]
    return text.strip()


def resolve_proof(value: Any, vault_root: Path) -> tuple[bool, str]:
    proof = unwrap_link(display(value))
    if not proof:
        return False, ""
    if proof.startswith(("http://", "https://")):
        return True, proof

    path_text = proof.replace("/", "\\")
    path = Path(path_text).expanduser()
    candidates: list[Path] = []
    if path.is_absolute():
        candidates.append(path)
    else:
        candidates.append(vault_root / path)
    if not path.suffix:
        candidates.extend(candidate.with_suffix(".md") for candidate in list(candidates))

    for candidate in candidates:
        if candidate.exists():
            return True, str(candidate)

    if "\\" not in path_text and "/" not in proof:
        matches = list(vault_root.rglob(path_text + ".md"))
        if matches:
            return True, str(matches[0])

    return False, proof


def missing_fields(row: dict[str, Any], fields: list[str]) -> list[str]:
    missing: list[str] = []
    for field in fields:
        if field == "proof":
            continue
        value = row.get(field)
        if value is None or value == "":
            missing.append(field)
    return missing


def finding(level: str, kind: str, row_id: str, text: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "kind": kind,
        "row_id": row_id,
        "finding": text,
        "evidence": evidence,
        "action": action,
    }


def evaluate_row(row: dict[str, Any], kind: str, vault_root: Path, required_by_kind: bool) -> tuple[str, list[dict[str, str]], str]:
    hints = KIND_HINTS.get(kind, {})
    row_id = display(row.get("id")) or kind
    row_status = norm(row.get("status") or "hold")
    row_required = bool_value(row.get("required"), required_by_kind)
    waived = not row_required and bool_value(row.get("waived"), bool(row.get("waiver_reason")))
    findings: list[dict[str, str]] = []

    if waived:
        return "skip", findings, "Evidence row waived: " + display(row.get("waiver_reason"))

    if bool_value(row.get("unsafe")) or bool_value(row.get("unsafe_exposure")):
        findings.append(finding("fail", kind, row_id, "The row marks the integration as unsafe.", "unsafe=true", "Fix the unsafe app boundary before promotion."))

    if row_status in {"fail", "failed", "error"}:
        findings.append(finding("fail", kind, row_id, "The producer row reports failure.", row_status, display(row.get("next_route")) or str(hints.get("next_route", ""))))
    elif row_status not in {"pass", "passed", "ok", "ready", "skip", "skipped", "waived"}:
        findings.append(finding("hold", kind, row_id, "The producer row is not pass.", row_status or "missing", display(row.get("next_route")) or str(hints.get("next_route", ""))))

    fields = list(hints.get("fields", []))
    missing = missing_fields(row, fields)
    if missing and row_required:
        findings.append(finding("hold", kind, row_id, "Required app-integration fields are missing.", ", ".join(missing), "Fill the missing fields before promoting this app integration."))

    if "proof" in fields or row_required:
        proof = row.get("proof")
        proof_exists, resolved = resolve_proof(proof, vault_root)
        if not proof_exists:
            findings.append(finding("hold", kind, row_id, "Proof path or link does not resolve.", resolved or "(missing proof)", "Link the saved artifact or add a documented waiver."))

    if any(item["level"] == "fail" for item in findings):
        return "fail", findings, "Fix the failed app-integration row."
    if findings:
        return "hold", findings, findings[0]["action"]
    return "pass", findings, display(row.get("pass_signal")) or str(hints.get("pass_signal", "Evidence row is ready."))


def evaluate_kind(kind: str, rows: list[dict[str, Any]], required: bool, vault_root: Path) -> dict[str, Any]:
    hints = KIND_HINTS.get(kind, {})
    critical = any(bool_value(row.get("critical"), required) for row in rows) if rows else required
    if not rows:
        if required:
            return {
                "kind": kind,
                "status": "hold",
                "decision": "kind_missing",
                "required": True,
                "critical": critical,
                "row_count": 0,
                "owner": str(hints.get("owner", "")),
                "next_route": str(hints.get("next_route", "")),
                "next_action": "Add an app-integration evidence row for this kind.",
                "findings": [finding("hold", kind, kind, "Required evidence kind is missing.", kind, str(hints.get("next_route", "")))],
            }
        return {
            "kind": kind,
            "status": "skip",
            "decision": "kind_not_required",
            "required": False,
            "critical": False,
            "row_count": 0,
            "owner": str(hints.get("owner", "")),
            "next_route": str(hints.get("next_route", "")),
            "next_action": "Optional evidence kind is absent.",
            "findings": [],
        }

    statuses: list[str] = []
    findings: list[dict[str, str]] = []
    next_action = str(hints.get("pass_signal", "Evidence kind is ready."))
    for row in rows:
        status, row_findings, row_next = evaluate_row(row, kind, vault_root, required)
        statuses.append(status)
        findings.extend(row_findings)
        if row_findings and next_action == str(hints.get("pass_signal", "Evidence kind is ready.")):
            next_action = row_next

    if "fail" in statuses:
        status = "fail"
        decision = "kind_failed"
    elif "hold" in statuses:
        status = "hold"
        decision = "kind_incomplete"
    elif all(item == "skip" for item in statuses):
        status = "skip"
        decision = "kind_waived"
    else:
        status = "pass"
        decision = "kind_ready"

    return {
        "kind": kind,
        "status": status,
        "decision": decision,
        "required": required,
        "critical": critical,
        "row_count": len(rows),
        "owner": str(hints.get("owner", "")),
        "next_route": str(hints.get("next_route", "")),
        "pass_signal": str(hints.get("pass_signal", "")),
        "next_action": next_action,
        "findings": findings,
    }


def csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = ["kind", "status", "decision", "required", "critical", "row_count", "owner", "next_route", "next_action"]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def render_markdown(record: dict[str, Any]) -> str:
    lines = [
        f"# Local LLM Application Integration Evidence - {record['run_id']}",
        "",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- App: `{record.get('app_name', '')}`",
        f"- Run root: `{record['run_root']}`",
        f"- Gate count: `{record['gate_count']}`",
        f"- Pass/Hold/Fail/Skip: `{record['pass_count']}` / `{record['hold_count']}` / `{record['fail_count']}` / `{record['skip_count']}`",
        f"- Critical gaps: `{record['critical_gap_count']}`",
        f"- Findings: `{record['finding_count']}`",
        f"- Next action: {record['next_action']}",
        "",
        "## Evidence Kinds",
        "",
        "| Kind | Status | Required | Critical | Rows | Owner | Next route |",
        "|---|---:|---:|---:|---:|---|---|",
    ]
    for row in record["kinds"]:
        lines.append(
            "| "
            + " | ".join([
                md_cell(row["kind"]),
                md_cell(row["status"]),
                md_cell(row["required"]),
                md_cell(row["critical"]),
                md_cell(row["row_count"]),
                md_cell(row.get("owner")),
                md_cell(row.get("next_route")),
            ])
            + " |"
        )
    lines.extend(["", "## Findings", ""])
    if record["findings"]:
        lines.append("| Level | Kind | Row | Finding | Evidence | Action |")
        lines.append("|---|---|---|---|---|---|")
        for item in record["findings"]:
            lines.append(
                "| "
                + " | ".join([
                    md_cell(item["level"]),
                    md_cell(item["kind"]),
                    md_cell(item["row_id"]),
                    md_cell(item["finding"]),
                    md_cell(item["evidence"]),
                    md_cell(item["action"]),
                ])
                + " |"
            )
    else:
        lines.append("No findings.")
    return "\n".join(lines) + "\n"


def load_manifest() -> tuple[Path, dict[str, Any]]:
    manifest_value = os.environ.get("LOCAL_LLM_APP_INTEGRATION_MANIFEST")
    if not manifest_value:
        raise ValueError("Set LOCAL_LLM_APP_INTEGRATION_MANIFEST to a JSON manifest path.")
    manifest_path = Path(manifest_value).expanduser().resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict):
        raise ValueError("Manifest must be a JSON object.")
    return manifest_path, manifest


def main() -> int:
    manifest_path, manifest = load_manifest()
    base_for_relative = manifest_path.parent
    run_root_value = os.environ.get("LOCAL_LLM_APP_INTEGRATION_RUN_ROOT") or manifest.get("run_root") or base_for_relative
    run_root = Path(str(run_root_value)).expanduser()
    if not run_root.is_absolute():
        run_root = base_for_relative / run_root
    run_root = run_root.resolve()

    vault_root_value = manifest.get("vault_root") or os.environ.get("LOCAL_LLM_APP_INTEGRATION_VAULT_ROOT") or "."
    vault_root = Path(str(vault_root_value)).expanduser()
    if not vault_root.is_absolute():
        vault_root = base_for_relative / vault_root
    vault_root = vault_root.resolve()

    run_id = display(manifest.get("run_id") or os.environ.get("LOCAL_LLM_APP_INTEGRATION_AUDIT_RUN_ID") or f"{utc_stamp()}-{slug(run_root.name)}")
    output_root_value = manifest.get("output_root") or os.environ.get("LOCAL_LLM_APP_INTEGRATION_OUTPUT_ROOT") or "app-integration-evidence"
    output_root = Path(str(output_root_value)).expanduser()
    if not output_root.is_absolute():
        output_root = run_root / output_root
    output_root = output_root.resolve()
    output_dir = output_root / run_id
    output_dir.mkdir(parents=True, exist_ok=True)

    rows = manifest.get("rows") or []
    if not isinstance(rows, list) or not all(isinstance(row, dict) for row in rows):
        raise ValueError("Manifest rows must be a list of objects.")

    required_kinds = [norm(item) for item in list_value(manifest.get("required_kinds"))] or list(DEFAULT_REQUIRED_KINDS)
    optional_kinds = [norm(item) for item in list_value(manifest.get("optional_kinds"))] or list(OPTIONAL_KINDS)
    kinds_to_check = list(dict.fromkeys(required_kinds + optional_kinds + [norm(row.get("kind")) for row in rows if norm(row.get("kind"))]))

    by_kind: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        kind = norm(row.get("kind"))
        if not kind:
            kind = "unknown"
        by_kind.setdefault(kind, []).append(row)

    evaluated = [evaluate_kind(kind, by_kind.get(kind, []), kind in required_kinds, vault_root) for kind in kinds_to_check]
    evaluated.sort(key=lambda row: (STATUS_RANK.get(row["status"], 4), not row["critical"], row["kind"]))
    findings = [item for kind in evaluated for item in kind["findings"]]

    fail_count = sum(1 for kind in evaluated if kind["status"] == "fail")
    hold_count = sum(1 for kind in evaluated if kind["status"] == "hold")
    skip_count = sum(1 for kind in evaluated if kind["status"] == "skip")
    pass_count = sum(1 for kind in evaluated if kind["status"] == "pass")
    critical_gap_count = sum(1 for kind in evaluated if kind["critical"] and kind["status"] != "pass")

    if fail_count:
        status = "fail"
        decision = "application_integration_failed"
        next_action = "Fix the failed app-integration row before promotion."
    elif hold_count or critical_gap_count:
        status = "hold"
        decision = "application_integration_incomplete"
        next_action = "Complete the first missing or held app-integration evidence kind."
    else:
        status = "pass"
        decision = "application_integration_ready"
        next_action = "Link this audit output into result synthesis and the deployment readiness memo."

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "next_action": next_action,
        "manifest_path": str(manifest_path),
        "run_root": str(run_root),
        "vault_root": str(vault_root),
        "app_name": display(manifest.get("app_name")),
        "gate_count": len(evaluated),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "skip_count": skip_count,
        "critical_gap_count": critical_gap_count,
        "finding_count": len(findings),
        "findings": findings,
        "kinds": evaluated,
        "outputs": {},
    }

    json_path = output_dir / f"{run_id}-application-integration-evidence.json"
    markdown_path = output_dir / f"{run_id}-application-integration-evidence.md"
    csv_path = output_dir / f"{run_id}-application-integration-evidence.csv"
    jsonl_path = output_root / "application-integration-evidence-runs.jsonl"
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
        "app_name": record["app_name"],
        "gate_count": record["gate_count"],
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "skip_count": skip_count,
        "critical_gap_count": critical_gap_count,
        "finding_count": len(findings),
        "output_dir": str(output_dir),
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
$env:LOCAL_LLM_APP_INTEGRATION_MANIFEST = "D:\llm-runs\app-integration\app-integration-manifest.json"
$env:LOCAL_LLM_APP_INTEGRATION_VAULT_ROOT = "D:\Vaults\PersonalKB"
python .\local_llm_application_integration_evidence_runner.py
```

## Reading The Result

| Runner status | Meaning | Next route |
|---|---|---|
| `pass/application_integration_ready` | the app integration has complete critical evidence and no failing rows | link the audit output in [[LLM/Study/Local LLM Result Synthesis Runner|Local LLM Result Synthesis Runner]] and [[LLM/Study/LLM Deployment Readiness Audit Runner|LLM Deployment Readiness Audit Runner]] |
| `hold/application_integration_incomplete` | no hard failure, but a required app boundary, flow, privacy, evaluation, operations, or decision row is missing | complete the routed evidence kind before promotion |
| `fail/application_integration_failed` | a row reports failure or unsafe exposure | fix the app boundary before using this as capstone or deployment evidence |

## Completion Gate

This runner is complete for one app integration when:

- [ ] app contract, endpoint contract, client flow, user flow, response handling, failure handling, privacy/logging, evaluation handoff, operations handoff, and promotion decision rows exist or have explicit waivers
- [ ] the user flow proves the local model path is reachable through the actual app/CLI/job boundary
- [ ] the response handling row names how text becomes application state
- [ ] at least one failure mode has expected behavior instead of a hanging or silent failure
- [ ] prompt/output/log retention is explicit before private data is used
- [ ] output JSON, Markdown, CSV, and JSONL files are linked from the capstone or deployment evidence bundle

## References

- [[LLM/Study/Local LLM First Client Harness Runner]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/LLM Inference Request Lifecycle Runner]]
- [[LLM/Study/Local LLM Failure Triage Runner]]
- [[LLM/Study/Local LLM Security and Privacy Runner]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Observability and Operations Runner]]
- [[LLM/Study/Local LLM Result Synthesis Runner]]
- [[LLM/Study/LLM Deployment Readiness Audit Runner]]
