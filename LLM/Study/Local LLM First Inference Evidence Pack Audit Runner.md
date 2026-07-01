---
tags: [study, llm, inference, local-llm, evidence, audit, capstone, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice]
last-verified: 2026-06-16
---

# Local LLM First Inference Evidence Pack Audit Runner

> **One-line summary** Audit the full first local inference packet after endpoint proof, API contract, client run, benchmark row, quality probes, security boundary, and final decision exist, so the run can be promoted into the capstone without hand-waving.

Use this after [[LLM/Study/Local LLM First Inference Evidence Pack|Local LLM First Inference Evidence Pack]] has a run folder and after [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner|Local LLM First Endpoint Evidence Audit Runner]] says the endpoint itself is ready. The endpoint audit proves the route. This pack audit proves the broader first-run packet is good enough to cite as applied mastery evidence.

This runner does not send inference requests. It reads saved artifacts, checks pass/hold/fail fields, writes JSON/CSV/Markdown/JSONL audit outputs, and names the first missing gate.

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| Endpoint audit | The route, runtime health, response debrief, template/tokenizer compatibility, and endpoint decision already passed. | The model is useful for a workload. |
| API contract | The OpenAI-compatible route, model id, streaming shape, and wrong-model behavior are known when the client depends on `/v1`. | Every OpenAI API feature is supported locally. |
| Client harness row | A reusable script called the endpoint and saved request, response, output, and JSONL evidence. | Fair benchmark coverage. |
| Streaming row | First event, first content delta, chunks, final text, and stream errors are captured when streaming matters. | That streaming is required for every workload. |
| Benchmark row | Timing, token, hardware, quality, missing-layer, and next-action fields are normalized. | Stable ranking across models. |
| Quality probe output | Smoke output was not mistaken for quality; the first private probes passed or held with owner. | Production-grade evaluation. |
| Security runner output | The endpoint, logs, RAG/tool/UI boundaries, and exposure posture have a no-generation security row. | Full compliance or penetration testing. |
| Final decision | The packet has a keep, tune, rerun, replace, stop, RAG/tool, or deployment next action. | That no future retest is needed. |

Academic bridge: a first local inference run is not just "the model answered." It is a measurement pipeline. The packet must connect serving mechanics, token/timing evidence, client behavior, evaluation boundaries, and security assumptions before it teaches anything durable.

## Manifest Shape

Minimum run-root mode:

```powershell
$env:LOCAL_LLM_FIRST_INFERENCE_RUN_ROOT = "D:\llm-runs\2026-06-16-first-local-inference"
python .\first-inference-evidence-pack-audit.py
```

Full manifest:

```json
{
  "run_id": "first-inference-pack-001",
  "run_root": "D:/llm-runs/2026-06-16-first-local-inference",
  "vault_root": "D:/Vaults/PersonalKB",
  "require_endpoint_audit": true,
  "require_openai_contract": true,
  "require_client": true,
  "require_streaming": false,
  "require_benchmark": true,
  "require_quality": true,
  "require_security": true,
  "require_final_decision": true
}
```

Turn a requirement off only when the packet explicitly says why the run is native-only, non-streaming, benchmark-pending, quality-pending, or security-pending. A skipped gate is not a pass; it is a scoped claim.

## Default Gates

| Gate id | Default evidence | Required by default |
|---|---|---|
| `run-card` | `run-card.md`, `run-card.txt`, or `run-root.txt` | yes |
| `endpoint-audit` | `first-endpoint-evidence-audit/*/*first-endpoint-evidence-audit.json` with pass/ready decision | yes |
| `openai-contract` | `openai-compatible-api-contract/*contract-results.json` or any `*contract-results.json` with compatible decision | yes |
| `client-harness` | `first-client-harness/client-runs.jsonl` with latest row `status=pass` | yes |
| `streaming-timing` | `first-streaming-timing/streaming-runs.jsonl` with latest row `status=pass` | no, unless `require_streaming=true` |
| `benchmark-row` | `first-benchmark-row/*benchmark-row.json` with `status=pass` | yes |
| `quality-probe` | `first-quality-probe-runner/*quality-probe-results.json` with `status=pass` | yes |
| `security-privacy` | `security-privacy-runner/*security-results.json` with `status=pass` | yes |
| `final-decision` | `decision.md`, `decision.txt`, or a decision JSON | yes |

## Standard-Library Runner

Save this as `first-inference-evidence-pack-audit.py` inside the run folder.

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


DEFAULT_GATES = [
    {
        "gate_id": "run-card",
        "required": True,
        "critical": True,
        "globs": ["run-card.md", "run-card.txt", "run-root.txt"],
        "route": "LLM/Study/Local LLM First Inference Evidence Pack",
        "pass_signal": "Run id, runtime, model, route, boundary, and decision target have a stable home.",
    },
    {
        "gate_id": "endpoint-audit",
        "required": True,
        "critical": True,
        "condition": "require_endpoint_audit",
        "globs": [
            "first-endpoint-evidence-audit/*/*first-endpoint-evidence-audit.json",
            "first-endpoint-evidence-audit/*first-endpoint-evidence-audit.json",
            "*/*first-endpoint-evidence-audit.json",
            "*first-endpoint-evidence-audit.json",
        ],
        "accepted_statuses": ["pass"],
        "accepted_decisions": ["first_endpoint_evidence_ready"],
        "route": "LLM/Study/Local LLM First Endpoint Evidence Audit Runner",
        "pass_signal": "Endpoint proof has already passed route, debrief, template/tokenizer, and decision gates.",
    },
    {
        "gate_id": "openai-contract",
        "required": True,
        "critical": True,
        "condition": "require_openai_contract",
        "globs": [
            "openai-compatible-api-contract/*contract-results.json",
            "openai-contract/*contract-results.json",
            "*/*contract-results.json",
            "*contract-results.json",
        ],
        "accepted_statuses": ["pass"],
        "accepted_decisions": ["compatible"],
        "decision_fields": ["compatible_decision", "decision"],
        "route": "LLM/Study/Local LLM OpenAI-Compatible API Contract Runner",
        "pass_signal": "The `/v1` route contract is compatible enough for reusable client code.",
    },
    {
        "gate_id": "client-harness",
        "required": True,
        "critical": True,
        "condition": "require_client",
        "globs": ["first-client-harness/client-runs.jsonl", "*client-runs.jsonl"],
        "accepted_statuses": ["pass"],
        "route": "LLM/Study/Local LLM First Client Harness Runner",
        "pass_signal": "A reusable client run is logged with request, response, output, and JSONL evidence.",
    },
    {
        "gate_id": "streaming-timing",
        "required": True,
        "critical": False,
        "condition": "require_streaming",
        "condition_default": False,
        "globs": ["first-streaming-timing/streaming-runs.jsonl", "*streaming-runs.jsonl"],
        "accepted_statuses": ["pass"],
        "route": "LLM/Study/Local LLM First Streaming Timing Runner",
        "pass_signal": "Perceived latency and streaming event evidence are present for a streaming workload.",
    },
    {
        "gate_id": "benchmark-row",
        "required": True,
        "critical": True,
        "condition": "require_benchmark",
        "globs": ["first-benchmark-row/*benchmark-row.json", "*/*benchmark-row.json", "*benchmark-row.json"],
        "accepted_statuses": ["pass"],
        "route": "LLM/Study/Local LLM First Benchmark Row Builder",
        "pass_signal": "The first client/streaming evidence has been normalized into a benchmark row.",
    },
    {
        "gate_id": "quality-probe",
        "required": True,
        "critical": True,
        "condition": "require_quality",
        "globs": [
            "first-quality-probe-runner/*quality-probe-results.json",
            "*/*quality-probe-results.json",
            "*quality-probe-results.json",
        ],
        "accepted_statuses": ["pass"],
        "route": "LLM/Study/Local LLM First Quality Probe Runner",
        "pass_signal": "The first private quality probes passed after endpoint evidence passed.",
    },
    {
        "gate_id": "security-privacy",
        "required": True,
        "critical": True,
        "condition": "require_security",
        "globs": ["security-privacy-runner/*security-results.json", "*/*security-results.json", "*security-results.json"],
        "accepted_statuses": ["pass"],
        "accepted_decisions": ["loopback_private_ready"],
        "route": "LLM/Study/Local LLM Security and Privacy Runner",
        "pass_signal": "The endpoint boundary, source inventory, logs, and obvious secret scan have a pass row.",
    },
    {
        "gate_id": "final-decision",
        "required": True,
        "critical": True,
        "condition": "require_final_decision",
        "globs": ["decision.md", "decision.txt", "*decision.md", "*decision.txt", "*decision.json", "*decision*.json"],
        "route": "LLM/Study/Local LLM First Inference Evidence Pack",
        "pass_signal": "The packet has a keep, tune, rerun, replace, stop, RAG/tool, or deployment next action.",
    },
]

STATUS_RANK = {"fail": 0, "hold": 1, "pass": 2, "skip": 3}


def utc_iso() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def slug(value: str) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value or "").strip()).strip("-")
    return text or "run"


def norm(value: Any) -> str:
    return re.sub(r"[^a-z0-9]+", "-", str(value or "").lower()).strip("-")


def display(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value)


def bool_value(value: Any, default: bool) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def list_value(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [display(item) for item in value if display(item)]
    if isinstance(value, str):
        return [item.strip() for item in re.split(r"[;,]", value) if item.strip()]
    return [display(value)] if display(value) else []


def clean_link(value: str) -> str:
    text = display(value)
    open_link = "[" * 2
    close_link = "]" * 2
    if text.startswith(open_link) and text.endswith(close_link):
        text = text[2:-2]
    return text.split("|", 1)[0].split("#", 1)[0].strip()


def resolve_path(value: Any, base: Path, vault_root: Path | None = None) -> Path:
    text = clean_link(display(value))
    path = Path(text).expanduser()
    if path.is_absolute():
        return path.resolve()
    candidate = (base / path).resolve()
    if candidate.exists():
        return candidate
    if vault_root:
        vault_candidate = (vault_root / path).resolve()
        if vault_candidate.exists():
            return vault_candidate
    return candidate


def load_manifest() -> tuple[Path, dict[str, Any]]:
    manifest_value = os.environ.get("LOCAL_LLM_FIRST_INFERENCE_PACK_MANIFEST")
    run_root_value = os.environ.get("LOCAL_LLM_FIRST_INFERENCE_RUN_ROOT")
    if manifest_value:
        manifest_path = Path(manifest_value).expanduser().resolve()
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if not isinstance(manifest, dict):
            raise ValueError("Manifest must be a JSON object.")
        return manifest_path, manifest
    if run_root_value:
        run_root = Path(run_root_value).expanduser().resolve()
        return run_root / "first-inference-evidence-pack-audit-manifest.json", {"run_root": str(run_root)}
    raise ValueError("Set LOCAL_LLM_FIRST_INFERENCE_PACK_MANIFEST or LOCAL_LLM_FIRST_INFERENCE_RUN_ROOT.")


def first_existing_path(root: Path, patterns: list[str]) -> Path | None:
    matches: list[Path] = []
    for pattern in patterns:
        matches.extend(path for path in root.glob(pattern) if path.is_file())
    if not matches:
        return None
    return sorted(matches, key=lambda item: item.stat().st_mtime, reverse=True)[0].resolve()


def read_json(path: Path) -> tuple[Any, str]:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig")), ""
    except Exception as exc:
        return None, f"{type(exc).__name__}: {exc}"


def read_last_jsonl(path: Path) -> tuple[Any, str]:
    last = None
    count = 0
    try:
        with path.open("r", encoding="utf-8-sig") as handle:
            for line in handle:
                text = line.strip()
                if not text:
                    continue
                last = json.loads(text)
                count += 1
    except Exception as exc:
        return None, f"{type(exc).__name__}: {exc}"
    if last is None:
        return None, "empty jsonl"
    return last, f"loaded {count} rows"


def load_record(path: Path) -> tuple[Any, str]:
    if path.suffix.lower() == ".jsonl":
        return read_last_jsonl(path)
    if path.suffix.lower() == ".json":
        return read_json(path)
    return None, "not a JSON status artifact"


def status_values(data: Any, gate: dict[str, Any]) -> tuple[set[str], set[str]]:
    statuses: set[str] = set()
    decisions: set[str] = set()
    if not isinstance(data, dict):
        return statuses, decisions
    for key in ["status", "overall_status", "route_status"]:
        value = norm(data.get(key))
        if value:
            statuses.add(value)
    decision_fields = list_value(gate.get("decision_fields")) or ["decision"]
    for key in decision_fields:
        value = norm(data.get(key))
        if value:
            decisions.add(value)
    endpoint_audit = data.get("endpoint_audit")
    if isinstance(endpoint_audit, dict):
        value = norm(endpoint_audit.get("status"))
        if value:
            statuses.add(f"endpoint-audit-{value}")
    return statuses, decisions


def gate_active(gate: dict[str, Any], manifest: dict[str, Any]) -> bool:
    condition = display(gate.get("condition"))
    if not condition:
        return True
    return bool_value(manifest.get(condition), bool_value(gate.get("condition_default"), True))


def find_matches(run_root: Path, gate: dict[str, Any]) -> list[Path]:
    matches: list[Path] = []
    for pattern in list_value(gate.get("globs")):
        matches.extend(path.resolve() for path in run_root.glob(pattern) if path.is_file())
    explicit = gate.get("path") or gate.get("proof")
    if explicit:
        path = resolve_path(explicit, run_root)
        if path.exists() and path.is_file():
            matches.append(path.resolve())
    seen: set[str] = set()
    unique: list[Path] = []
    for path in matches:
        key = str(path).lower()
        if key not in seen:
            seen.add(key)
            unique.append(path)
    return sorted(unique, key=lambda item: str(item).lower())


def finding(level: str, gate_id: str, text: str, evidence: str, action: str) -> dict[str, str]:
    return {"level": level, "gate_id": gate_id, "finding": text, "evidence": evidence, "action": action}


def evaluate_gate(gate: dict[str, Any], run_root: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    gate_id = display(gate.get("gate_id")) or "unnamed-gate"
    required = bool_value(gate.get("required"), True)
    critical = bool_value(gate.get("critical"), required)
    if not gate_active(gate, manifest):
        return {
            "gate_id": gate_id,
            "status": "skip",
            "decision": "manifest_skipped",
            "required": required,
            "critical": critical,
            "match_count": 0,
            "matches": [],
            "route": display(gate.get("route")),
            "next_action": "Gate skipped by manifest scope.",
            "findings": [],
        }

    matches = find_matches(run_root, gate)
    min_matches = int(gate.get("min_matches") or 1)
    findings: list[dict[str, str]] = []
    accepted_statuses = {norm(item) for item in list_value(gate.get("accepted_statuses")) if norm(item)}
    accepted_decisions = {norm(item) for item in list_value(gate.get("accepted_decisions")) if norm(item)}
    observed_statuses: set[str] = set()
    observed_decisions: set[str] = set()

    if len(matches) < min_matches:
        findings.append(
            finding(
                "hold",
                gate_id,
                "Expected evidence file is missing.",
                ", ".join(list_value(gate.get("globs"))),
                f"Complete {gate_id} through {display(gate.get('route'))}.",
            )
        )
    for path in matches:
        data, note = load_record(path)
        if note and (path.suffix.lower() in {".json", ".jsonl"}):
            if note.startswith("loaded "):
                pass
            else:
                findings.append(finding("hold", gate_id, "Status artifact could not be read.", f"{path}: {note}", "Fix or replace the malformed artifact."))
        statuses, decisions = status_values(data, gate)
        observed_statuses |= statuses
        observed_decisions |= decisions
        if statuses & {"fail", "failed", "error", "runner-exception"}:
            findings.append(finding("fail", gate_id, "Matched artifact reports fail or error.", str(path), "Diagnose the producing gate before promoting the packet."))

    if matches and (accepted_statuses or accepted_decisions):
        status_ok = bool(observed_statuses & accepted_statuses) if accepted_statuses else True
        decision_ok = bool(observed_decisions & accepted_decisions) if accepted_decisions else True
        if not (status_ok and decision_ok):
            evidence = f"statuses={sorted(observed_statuses)} decisions={sorted(observed_decisions)}"
            findings.append(finding("hold", gate_id, "Matched artifacts do not report the accepted pass decision.", evidence, f"Rerun or complete {gate_id} before capstone promotion."))

    if not findings:
        status = "pass"
        decision = "gate_ready"
        next_action = display(gate.get("pass_signal")) or "Evidence is present."
    elif any(item["level"] == "fail" for item in findings):
        status = "fail"
        decision = "gate_failed"
        next_action = findings[0]["action"]
    else:
        status = "hold"
        decision = "gate_incomplete"
        next_action = findings[0]["action"]

    return {
        "gate_id": gate_id,
        "status": status,
        "decision": decision,
        "required": required,
        "critical": critical,
        "match_count": len(matches),
        "matches": [str(path) for path in matches],
        "observed_statuses": sorted(observed_statuses),
        "observed_decisions": sorted(observed_decisions),
        "route": display(gate.get("route")),
        "pass_signal": display(gate.get("pass_signal")),
        "next_action": next_action,
        "findings": findings,
    }


def md_cell(value: Any) -> str:
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=True)
    return display(value).replace("|", "\\|").replace("\n", " ")


def write_csv(path: Path, gates: list[dict[str, Any]]) -> None:
    fieldnames = ["gate_id", "status", "decision", "required", "critical", "match_count", "route", "next_action"]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for gate in gates:
            writer.writerow({field: gate.get(field, "") for field in fieldnames})


def render_markdown(record: dict[str, Any]) -> str:
    lines = [
        f"# Local LLM First Inference Evidence Pack Audit - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Run root: `{record['run_root']}`",
        f"- Next action: {record['next_action']}",
        "",
        "## Gates",
        "",
        "| Gate | Required | Critical | Status | Matches | Observed | Next action |",
        "|---|---:|---:|---|---:|---|---|",
    ]
    for gate in record["gates"]:
        observed = ", ".join(gate.get("observed_statuses", []) + gate.get("observed_decisions", []))
        lines.append("| " + " | ".join([
            md_cell(gate["gate_id"]),
            md_cell(gate["required"]),
            md_cell(gate["critical"]),
            md_cell(gate["status"]),
            md_cell(gate["match_count"]),
            md_cell(observed),
            md_cell(gate["next_action"]),
        ]) + " |")
    lines.extend(["", "## Findings", ""])
    if record["findings"]:
        for item in record["findings"]:
            lines.append(f"- `{item['level']}` {item['gate_id']}: {item['finding']} -> {item['action']}")
    else:
        lines.append("- No blocking findings.")
    return "\n".join(lines) + "\n"


def main() -> int:
    manifest_path, manifest = load_manifest()
    base_for_relative = manifest_path.parent
    vault_root_value = manifest.get("vault_root") or os.environ.get("LOCAL_LLM_FIRST_INFERENCE_VAULT_ROOT")
    vault_root = resolve_path(vault_root_value, base_for_relative) if vault_root_value else None
    run_root = resolve_path(manifest.get("run_root") or os.environ.get("LOCAL_LLM_FIRST_INFERENCE_RUN_ROOT"), base_for_relative, vault_root)
    if not run_root.exists():
        raise ValueError(f"run_root does not exist: {run_root}")
    run_id = display(manifest.get("run_id") or os.environ.get("LOCAL_LLM_FIRST_INFERENCE_AUDIT_RUN_ID") or f"{utc_stamp()}-{slug(run_root.name)}")
    output_root_value = manifest.get("output_root") or os.environ.get("LOCAL_LLM_FIRST_INFERENCE_AUDIT_OUTPUT_ROOT") or "first-inference-evidence-pack-audit"
    output_root = Path(str(output_root_value)).expanduser()
    if not output_root.is_absolute():
        output_root = run_root / output_root
    output_dir = output_root / slug(run_id)
    output_dir.mkdir(parents=True, exist_ok=True)

    gates_config = manifest.get("gates")
    gates = gates_config if isinstance(gates_config, list) else DEFAULT_GATES
    evaluated = [evaluate_gate(dict(gate), run_root, manifest) for gate in gates]
    findings = [item for gate in evaluated for item in gate["findings"]]
    fail_count = sum(1 for gate in evaluated if gate["status"] == "fail")
    hold_count = sum(1 for gate in evaluated if gate["status"] == "hold")
    critical_gap_count = sum(1 for gate in evaluated if gate["critical"] and gate["status"] not in {"pass", "skip"})

    if fail_count:
        status = "fail"
        decision = "first_inference_pack_failed"
        next_action = "Diagnose the failed artifact before using the run as mastery evidence."
    elif hold_count or critical_gap_count:
        status = "hold"
        decision = "first_inference_pack_incomplete"
        first_gap = next((gate for gate in evaluated if gate["status"] == "hold"), None)
        next_action = first_gap["next_action"] if first_gap else "Complete held first-inference gates."
    else:
        status = "pass"
        decision = "first_inference_pack_ready"
        next_action = "Link this audit output into the first inference evidence pack and capstone workbook."

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "next_action": next_action,
        "manifest_path": str(manifest_path),
        "run_root": str(run_root),
        "vault_root": str(vault_root) if vault_root else "",
        "gate_count": len(evaluated),
        "pass_count": sum(1 for gate in evaluated if gate["status"] == "pass"),
        "hold_count": hold_count,
        "fail_count": fail_count,
        "skip_count": sum(1 for gate in evaluated if gate["status"] == "skip"),
        "critical_gap_count": critical_gap_count,
        "finding_count": len(findings),
        "findings": findings,
        "gates": evaluated,
        "outputs": {},
    }

    json_path = output_dir / f"{slug(run_id)}-first-inference-pack-audit.json"
    markdown_path = output_dir / f"{slug(run_id)}-first-inference-pack-audit.md"
    csv_path = output_dir / f"{slug(run_id)}-first-inference-pack-audit.csv"
    jsonl_path = output_root / "first-inference-pack-audits.jsonl"
    record["outputs"] = {"json": str(json_path), "markdown": str(markdown_path), "csv": str(csv_path), "jsonl": str(jsonl_path)}

    json_path.write_text(json.dumps(record, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown(record), encoding="utf-8")
    write_csv(csv_path, evaluated)
    with jsonl_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=True) + "\n")

    print(json.dumps({
        "status": status,
        "decision": decision,
        "run_id": run_id,
        "run_root": str(run_root),
        "gate_count": record["gate_count"],
        "pass_count": record["pass_count"],
        "hold_count": record["hold_count"],
        "fail_count": record["fail_count"],
        "skip_count": record["skip_count"],
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

Manifest mode:

```powershell
$env:LOCAL_LLM_FIRST_INFERENCE_PACK_MANIFEST = "D:\llm-runs\first-local-inference\first-inference-pack-audit-manifest.json"
$env:LOCAL_LLM_FIRST_INFERENCE_VAULT_ROOT = "D:\Vaults\PersonalKB"
python .\first-inference-evidence-pack-audit.py
```

Run-folder-only mode:

```powershell
$env:LOCAL_LLM_FIRST_INFERENCE_RUN_ROOT = "D:\llm-runs\2026-06-16-first-local-inference"
python .\first-inference-evidence-pack-audit.py
```

Native-only or non-streaming scope:

```json
{
  "run_root": "D:/llm-runs/native-only-first-run",
  "require_openai_contract": false,
  "require_client": false,
  "require_streaming": false,
  "require_benchmark": false,
  "require_quality": true,
  "require_security": true
}
```

That scope can prove a narrow native endpoint packet. It cannot prove reusable OpenAI-compatible client inference.

## Result Decisions

| Status and decision | Meaning | Next route |
|---|---|---|
| `pass/first_inference_pack_ready` | all scoped critical gates passed | link the audit output in [[LLM/Study/Local LLM First Inference Evidence Pack|Local LLM First Inference Evidence Pack]], [[LLM/Study/LLM Mastery Dashboard|LLM Mastery Dashboard]], and [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]] |
| `hold/first_inference_pack_incomplete` | a required artifact is missing or held | complete the routed gate before using the packet as capstone evidence |
| `fail/first_inference_pack_failed` | a producer output reports failed or error | diagnose with [[LLM/Study/Local LLM Failure Triage Runner|Local LLM Failure Triage Runner]] before rerunning |

## Copy Row

| Field | Value |
|---|---|
| Pack audit status | pass / hold / fail |
| Pack audit output |  |
| Run root |  |
| Endpoint audit |  |
| API contract |  |
| Client harness row |  |
| Streaming row | required / skipped / output |
| Benchmark row |  |
| Quality probe output |  |
| Security/privacy output |  |
| Missing gate |  |
| Next action |  |

## Completion Gate

This runner is useful when:

- [ ] the first inference run folder has a stable run card
- [ ] the endpoint evidence audit is pass, or the manifest explicitly scopes a narrower packet
- [ ] the API contract is pass before reusable OpenAI-compatible client evidence is claimed
- [ ] first client, benchmark, quality, and security outputs exist before capstone promotion
- [ ] streaming is either proven or explicitly not required
- [ ] final decision text states keep, tune, rerun, replace, stop, RAG/tool, or deployment next action
- [ ] the generated pack audit output is linked from the evidence pack and capstone workbook

## References

Internal routes:

- [[LLM/Study/Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]]
- [[LLM/Study/Local LLM First Client Harness Runner]]
- [[LLM/Study/Local LLM First Streaming Timing Runner]]
- [[LLM/Study/Local LLM First Benchmark Row Builder]]
- [[LLM/Study/Local LLM First Quality Probe Runner]]
- [[LLM/Study/Local LLM Security and Privacy Runner]]
- [[LLM/Study/Local LLM Failure Triage Runner]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]

External/current sources checked 2026-06-16:

- [Ollama chat endpoint](https://docs.ollama.com/api/chat)
- [Ollama usage metrics](https://docs.ollama.com/api/usage)
- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
- [OpenAI streaming responses](https://developers.openai.com/api/docs/guides/streaming-responses)
