---
tags: [study, llm, inference, local-llm, endpoint, evidence, audit, hosting, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM First Endpoint Evidence Audit Runner

> **One-line summary** A first local LLM endpoint counts only when the run folder proves machine state, model tag, runtime health, native or OpenAI-compatible response, health-bound debrief, template/tokenizer compatibility, security boundary, and next decision.

Use this after [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]], [[LLM/Study/Local LLM First Runtime Health Runner|Local LLM First Runtime Health Runner]] or [[LLM/Study/Local LLM First Runtime Health Snapshot|Local LLM First Runtime Health Snapshot]], [[LLM/Study/Local LLM First Smoke Request Runner|Local LLM First Smoke Request Runner]], [[LLM/Study/Local LLM First Response Debrief Runner|Local LLM First Response Debrief Runner]], and [[LLM/Study/Chat Template and Tokenizer Compatibility Runner|Chat Template and Tokenizer Compatibility Runner]] have produced files in a first-run folder.

The first endpoint is not proven by a screenshot, a memory of a chat response, or one command printed in the terminal. It is proven when another person can inspect the run folder and see what machine, runtime, model, route, prompt, response, timing, boundary, and decision were used.

## What This Proves

| Gate | Evidence checked | Why it matters |
|---|---|---|
| Run card | run id, runtime, model, base URL, boundary, next decision | gives the run a stable identity |
| Preflight | OS, shell, CPU/RAM, GPU/VRAM, disk, listener intent | prevents hardware or boundary guessing |
| Runtime install state | runtime version, PATH, existing model list, or install gate output | separates install/PATH failures from model failures |
| Model pull/custody | model tag, pull/list/show evidence, or model artifact proof | proves which model should answer |
| Runtime health | listener, model-list, loaded-model, OpenAI-compatible model ids | proves readiness before generation |
| Smoke response | native route and, when required, OpenAI-compatible route | proves the model can answer through the intended endpoint |
| Debrief | parsed text, timing conversion, mechanism owner, quality boundary | turns raw response into interpretable evidence |
| Template/tokenizer compatibility | first-response-bound compatibility runner output | proves chat formatting, role boundaries, stop behavior, and downstream quality claims are not detached from route proof |
| Decision | keep, tune, rerun, replace model, replace runtime, stop, or diagnose | prevents route proof from being mistaken for quality or deployment readiness |

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "first-endpoint-audit-001",
  "run_root": "D:/llm-runs/2026-06-15-first-endpoint",
  "vault_root": "D:/Vaults/PersonalKB",
  "require_openai_route": true
}
```

Optional gate override:

```json
{
  "run_id": "first-endpoint-audit-001",
  "run_root": "D:/llm-runs/2026-06-15-first-endpoint",
  "vault_root": "D:/Vaults/PersonalKB",
  "gates": [
    {
      "gate_id": "native-response",
      "required": true,
      "critical": true,
      "globs": ["first-smoke-request/*native*response*.json", "ollama-native-response.json"],
      "route": "LLM/Study/Local LLM First Smoke Request Runner"
    }
  ]
}
```

Use overrides when the first run is LM Studio, llama.cpp, vLLM, SGLang, or a native-only endpoint where the default Ollama-oriented file names do not apply.

## Default Required Evidence

| Gate id | Default evidence | Required by default |
|---|---|---|
| `run-card` | `run-card.txt`, `run-card.md`, or `run-root.txt` | yes |
| `preflight` | `preflight*.txt`, `preinstall-*.txt`, disk, GPU, or system text files | yes |
| `runtime-install-state` | runtime version, install gate, or model-list-before text | yes |
| `model-pull-or-custody` | `model-tag.txt`, pull/list/show output, or provenance card | yes |
| `runtime-health` | `first-runtime-health/*.json`, runner `*/*runtime-health*.json`, or runtime-health JSON | yes |
| `smoke-summary` | `first-smoke-request/*summary.json` or smoke summary JSON | yes |
| `native-response` | native Ollama response JSON or native response from smoke runner | yes |
| `openai-response` | OpenAI-compatible response JSON | yes unless `require_openai_route` is false |
| `first-response-debrief` | `first-response-debrief/*.json` or debrief JSON with status `pass` | yes |
| `template-tokenizer-compatibility` | `chat-template-tokenizer-compatibility-runs/*/*chat-template-compatibility.json` or compatibility JSON with status `pass` | yes |
| `decision` | decision note, decision text, or first endpoint decision row | yes |
| `quality-boundary` | first quality probe output or an explicit note that quality is not proven by smoke | optional but recommended |

## Standard-Library Runner

Save the code block as `first-endpoint-evidence-audit.py` or extract it directly from this note.

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
        "globs": ["run-card.txt", "run-card.md", "run-root.txt"],
        "route": "LLM/Study/Local LLM First Endpoint Run Sheet",
        "pass_signal": "Run id, runtime, model, base URL, boundary, and next decision have a stable home.",
    },
    {
        "gate_id": "preflight",
        "required": True,
        "critical": True,
        "globs": ["preflight*.txt", "preinstall-*.txt", "*system*.txt", "*gpu*.txt", "*disk*.txt", "nvidia-smi*.txt"],
        "min_matches": 1,
        "route": "LLM/Study/Local LLM Environment Preflight Lab",
        "pass_signal": "Machine, boundary, hardware, disk, or listener state is captured before inference.",
    },
    {
        "gate_id": "runtime-install-state",
        "required": True,
        "critical": True,
        "globs": ["*version*.txt", "*install*gate*.json", "*list-before*.txt", "*list-after-install*.txt"],
        "min_matches": 1,
        "route": "LLM/Study/Local LLM Windows Runtime Install Gate",
        "pass_signal": "Runtime command, version, PATH, or install state is known before model pull.",
    },
    {
        "gate_id": "model-pull-or-custody",
        "required": True,
        "critical": True,
        "globs": ["model-tag.txt", "*pull*.txt", "*list-after-pull*.txt", "*show*.json", "*provenance*.md", "*artifact*.md"],
        "min_matches": 1,
        "route": "LLM/Study/Local LLM First Model Pull Gate",
        "pass_signal": "The selected local model tag or artifact is known.",
    },
    {
        "gate_id": "runtime-health",
        "required": True,
        "critical": True,
        "globs": ["first-runtime-health/*.json", "*/*runtime-health*.json", "*runtime-health*.json", "*health*.json"],
        "route": "LLM/Study/Local LLM First Runtime Health Runner",
        "accepted_statuses": ["pass"],
        "pass_signal": "The server can list model state, model id visibility, and boundary evidence before generation.",
    },
    {
        "gate_id": "smoke-summary",
        "required": True,
        "critical": True,
        "globs": ["first-smoke-request/*summary.json", "*smoke*summary*.json"],
        "route": "LLM/Study/Local LLM First Smoke Request Runner",
        "accepted_statuses": ["pass"],
        "pass_signal": "The smoke runner summarized native and compatibility route behavior.",
    },
    {
        "gate_id": "native-response",
        "required": True,
        "critical": True,
        "globs": ["first-smoke-request/*native*response*.json", "ollama-native-response.json", "ollama-native-generate.json", "*native*response*.json"],
        "route": "LLM/Study/Local LLM First Smoke Request Runner",
        "pass_signal": "A local native route response is saved.",
    },
    {
        "gate_id": "openai-response",
        "required": True,
        "critical": True,
        "condition": "require_openai_route",
        "globs": ["first-smoke-request/*openai*response*.json", "ollama-openai-response.json", "ollama-openai-chat.json", "openai-compatible-chat.json", "*openai*response*.json"],
        "route": "LLM/Study/Local LLM OpenAI-Compatible API Contract Runner",
        "pass_signal": "The intended OpenAI-compatible route response is saved.",
    },
    {
        "gate_id": "first-response-debrief",
        "required": True,
        "critical": True,
        "globs": ["first-response-debrief/*.json", "*debrief*.json"],
        "route": "LLM/Study/Local LLM First Response Debrief Runner",
        "accepted_statuses": ["pass"],
        "pass_signal": "The saved first response has health-bound timing and mechanism interpretation.",
    },
    {
        "gate_id": "template-tokenizer-compatibility",
        "required": True,
        "critical": True,
        "globs": [
            "chat-template-tokenizer-compatibility-runs/*/*chat-template-compatibility.json",
            "chat-template-tokenizer-compatibility-runs/*.json",
            "*/*chat-template-compatibility.json",
            "*chat-template*compatibility*.json",
        ],
        "route": "LLM/Study/Chat Template and Tokenizer Compatibility Runner",
        "accepted_statuses": ["pass"],
        "pass_signal": "The endpoint has health-bound template, tokenizer, route, stop, and downstream-evidence compatibility proof.",
    },
    {
        "gate_id": "decision",
        "required": True,
        "critical": True,
        "globs": ["decision.md", "decision.txt", "*decision*.md", "*decision*.txt", "*decision*.json"],
        "route": "LLM/Study/Local LLM First Inference Evidence Pack",
        "pass_signal": "The endpoint proof has a keep, tune, rerun, replace, stop, or diagnosis decision.",
    },
    {
        "gate_id": "quality-boundary",
        "required": False,
        "critical": False,
        "globs": ["first-quality-probe*/*.json", "quality-row.md", "*quality*.json", "*quality*.md"],
        "route": "LLM/Study/Local LLM First Quality Probe Runner",
        "pass_signal": "The run either has a first quality signal or is explicitly limited to route proof.",
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
    if text.startswith("[" * 2) and text.endswith("]" * 2):
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
    manifest_value = os.environ.get("LOCAL_LLM_FIRST_ENDPOINT_AUDIT_MANIFEST")
    run_root_value = os.environ.get("LOCAL_LLM_FIRST_ENDPOINT_RUN_ROOT")
    if manifest_value:
        manifest_path = Path(manifest_value).expanduser().resolve()
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if not isinstance(manifest, dict):
            raise ValueError("Manifest must be a JSON object.")
        return manifest_path, manifest
    if run_root_value:
        run_root = Path(run_root_value).expanduser().resolve()
        manifest = {"run_root": str(run_root)}
        return run_root / "first-endpoint-evidence-audit-manifest.json", manifest
    raise ValueError("Set LOCAL_LLM_FIRST_ENDPOINT_AUDIT_MANIFEST or LOCAL_LLM_FIRST_ENDPOINT_RUN_ROOT.")


def status_from_data(data: Any) -> str:
    if not isinstance(data, dict):
        return ""
    candidates = [
        data.get("status"),
        data.get("decision"),
        data.get("overall_status"),
        data.get("route_decision"),
    ]
    for value in candidates:
        text = norm(value)
        if not text:
            continue
        if text in {"pass", "ready", "ok", "compatible", "first-endpoint-evidence-ready", "smoke-ready", "chat-template-compatibility-ready"}:
            return "pass"
        if text in {"hold", "partial", "incomplete", "not-ready", "blocked"}:
            return "hold"
        if text in {"fail", "failed", "error", "runner-exception"}:
            return "fail"
    return ""


def read_json_status(path: Path) -> tuple[str, str]:
    if path.suffix.lower() != ".json":
        return "", ""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return "hold", f"JSON file could not be parsed: {exc}"
    status = status_from_data(data)
    return status, ""


def gate_active(gate: dict[str, Any], manifest: dict[str, Any]) -> bool:
    condition = display(gate.get("condition"))
    if not condition:
        return True
    if condition == "require_openai_route":
        return bool_value(manifest.get("require_openai_route"), True)
    if condition == "require_quality_boundary":
        return bool_value(manifest.get("require_quality_boundary"), False)
    return bool_value(manifest.get(condition), True)


def find_matches(run_root: Path, gate: dict[str, Any]) -> list[Path]:
    matches: list[Path] = []
    for pattern in list_value(gate.get("globs")):
        for path in run_root.glob(pattern):
            if path.is_file():
                matches.append(path.resolve())
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
    return unique


def finding(level: str, gate_id: str, text: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "gate_id": gate_id,
        "finding": text,
        "evidence": evidence,
        "action": action,
    }


def evaluate_gate(gate: dict[str, Any], run_root: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    gate_id = display(gate.get("gate_id")) or "unnamed-gate"
    required = bool_value(gate.get("required"), True)
    critical = bool_value(gate.get("critical"), required)
    if not gate_active(gate, manifest):
        return {
            "gate_id": gate_id,
            "status": "skip",
            "required": required,
            "critical": critical,
            "matches": [],
            "match_count": 0,
            "route": display(gate.get("route")),
            "next_action": "Gate skipped by manifest condition.",
            "findings": [],
        }

    matches = find_matches(run_root, gate)
    min_matches = int(gate.get("min_matches") or 1)
    findings: list[dict[str, str]] = []
    accepted_statuses = {norm(item) for item in list_value(gate.get("accepted_statuses")) if norm(item)}

    if len(matches) < min_matches:
        if not required:
            return {
                "gate_id": gate_id,
                "status": "skip",
                "decision": "optional_evidence_absent",
                "required": required,
                "critical": critical,
                "matches": [],
                "match_count": len(matches),
                "route": display(gate.get("route")),
                "pass_signal": display(gate.get("pass_signal")),
                "next_action": f"Optional evidence for {gate_id} is absent.",
                "findings": [],
            }
        level = "hold"
        action = f"Add evidence for {gate_id} or override this gate with a documented waiver."
        findings.append(finding(level, gate_id, "Expected evidence file is missing.", ", ".join(list_value(gate.get("globs"))), action))

    file_statuses: list[str] = []
    parse_notes: list[str] = []
    for path in matches:
        status, note = read_json_status(path)
        if status:
            file_statuses.append(status)
        if note:
            parse_notes.append(f"{path.name}: {note}")
    if any(status == "fail" for status in file_statuses):
        findings.append(finding("fail", gate_id, "A matched JSON artifact reports fail or error.", ", ".join(str(path) for path in matches), "Fix the failed first-run artifact before accepting endpoint proof."))
    elif accepted_statuses and file_statuses and not any(status in accepted_statuses for status in file_statuses):
        findings.append(finding("hold", gate_id, "Matched JSON artifacts do not report an accepted status.", ", ".join(file_statuses), f"Rerun the producing note until one status is in {sorted(accepted_statuses)}."))
    for note in parse_notes:
        findings.append(finding("hold", gate_id, "A JSON artifact could not be parsed.", note, "Fix or replace the malformed artifact."))

    if any(item["level"] == "fail" for item in findings):
        status = "fail"
        decision = "gate_failed"
    elif findings:
        status = "hold"
        decision = "gate_incomplete"
    else:
        status = "pass"
        decision = "gate_ready"

    return {
        "gate_id": gate_id,
        "status": status,
        "decision": decision,
        "required": required,
        "critical": critical,
        "matches": [str(path) for path in matches],
        "match_count": len(matches),
        "route": display(gate.get("route")),
        "pass_signal": display(gate.get("pass_signal")),
        "next_action": findings[0]["action"] if findings else display(gate.get("pass_signal")) or "Evidence is present.",
        "findings": findings,
    }


def csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = ["gate_id", "status", "decision", "required", "critical", "match_count", "route", "next_action"]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def md_cell(value: Any) -> str:
    if isinstance(value, (list, dict)):
        value = json.dumps(value, ensure_ascii=True)
    return display(value).replace("|", "\\|").replace("\n", " ")


def render_markdown(record: dict[str, Any]) -> str:
    lines = [
        f"# Local LLM First Endpoint Evidence Audit - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Run root: `{record['run_root']}`",
        f"- Next action: {record['next_action']}",
        "",
        "## Gates",
        "",
        "| Gate | Required | Critical | Status | Matches | Next action |",
        "|---|---:|---:|---|---:|---|",
    ]
    for gate in record["gates"]:
        lines.append("| " + " | ".join([
            md_cell(gate["gate_id"]),
            md_cell(gate["required"]),
            md_cell(gate["critical"]),
            md_cell(gate["status"]),
            md_cell(gate["match_count"]),
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
    run_root = resolve_path(manifest.get("run_root") or os.environ.get("LOCAL_LLM_FIRST_ENDPOINT_RUN_ROOT") or ".", base_for_relative)
    vault_root_value = manifest.get("vault_root") or os.environ.get("LOCAL_LLM_FIRST_ENDPOINT_VAULT_ROOT")
    vault_root = resolve_path(vault_root_value, base_for_relative) if vault_root_value else None
    run_id = display(manifest.get("run_id") or os.environ.get("LOCAL_LLM_FIRST_ENDPOINT_AUDIT_RUN_ID") or f"{utc_stamp()}-{slug(run_root.name)}")
    output_root_value = manifest.get("output_root") or os.environ.get("LOCAL_LLM_FIRST_ENDPOINT_AUDIT_OUTPUT_ROOT") or "first-endpoint-evidence-audit"
    output_root = Path(str(output_root_value)).expanduser()
    if not output_root.is_absolute():
        output_root = run_root / output_root
    output_dir = output_root / slug(run_id)
    output_dir.mkdir(parents=True, exist_ok=True)

    gates_config = manifest.get("gates")
    gates = gates_config if isinstance(gates_config, list) else DEFAULT_GATES
    evaluated = [evaluate_gate(dict(gate), run_root, manifest) for gate in gates]
    evaluated.sort(key=lambda row: (STATUS_RANK.get(row["status"], 4), not row["critical"], row["gate_id"]))
    findings = [item for gate in evaluated for item in gate["findings"]]

    fail_count = sum(1 for gate in evaluated if gate["status"] == "fail")
    hold_count = sum(1 for gate in evaluated if gate["status"] == "hold")
    critical_gap_count = sum(1 for gate in evaluated if gate["critical"] and gate["status"] != "pass")
    if fail_count:
        status = "fail"
        decision = "first_endpoint_evidence_failed"
        next_action = "Fix the failed first endpoint artifact before using this run as evidence."
    elif hold_count or critical_gap_count:
        status = "hold"
        decision = "first_endpoint_evidence_incomplete"
        next_action = "Complete the first missing or held first endpoint gate."
    else:
        status = "pass"
        decision = "first_endpoint_evidence_ready"
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

    json_path = output_dir / f"{run_id}-first-endpoint-evidence-audit.json"
    markdown_path = output_dir / f"{run_id}-first-endpoint-evidence-audit.md"
    csv_path = output_dir / f"{run_id}-first-endpoint-evidence-audit.csv"
    jsonl_path = output_root / "first-endpoint-evidence-audits.jsonl"
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
        "run_root": str(run_root),
        "gate_count": record["gate_count"],
        "pass_count": record["pass_count"],
        "hold_count": record["hold_count"],
        "fail_count": record["fail_count"],
        "critical_gap_count": record["critical_gap_count"],
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
$env:LOCAL_LLM_FIRST_ENDPOINT_AUDIT_MANIFEST = "D:\llm-runs\first-endpoint\first-endpoint-audit-manifest.json"
$env:LOCAL_LLM_FIRST_ENDPOINT_VAULT_ROOT = "D:\Vaults\PersonalKB"
python .\first-endpoint-evidence-audit.py
```

Run-folder-only mode:

```powershell
$env:LOCAL_LLM_FIRST_ENDPOINT_RUN_ROOT = "D:\llm-runs\2026-06-15-first-endpoint"
python .\first-endpoint-evidence-audit.py
```

## Result Decisions

| Status and decision | Meaning | Next route |
|---|---|---|
| `pass/first_endpoint_evidence_ready` | all critical first endpoint evidence is present, the debrief is pass, and template/tokenizer compatibility is pass | link the audit output in [[LLM/Study/Local LLM First Inference Evidence Pack|Local LLM First Inference Evidence Pack]] and [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]] |
| `hold/first_endpoint_evidence_incomplete` | a required file is missing or a producer output is held | complete the routed gate before treating the endpoint as proven |
| `fail/first_endpoint_evidence_failed` | a producer output reports failed or error | diagnose with [[LLM/Study/Local LLM Failure Triage Runner|Local LLM Failure Triage Runner]] before rerunning |

## First Endpoint Evidence Row

Copy this row into the evidence pack or capstone workbook after the runner passes or holds:

| Field | Value |
|---|---|
| Audit status | pass / hold / fail |
| Audit output |  |
| Run root |  |
| Model id |  |
| Runtime |  |
| Native route proof |  |
| OpenAI-compatible route proof |  |
| Debrief output |  |
| Template/tokenizer compatibility output |  |
| Missing gate |  |
| Next action |  |

## Completion Gate

This runner is useful when:

- [ ] the first endpoint run folder has a run card and preflight evidence
- [ ] model tag or artifact custody is saved
- [ ] runtime health exists before generation
- [ ] native and required compatibility response files exist
- [ ] first response debrief exists and is `pass`
- [ ] template/tokenizer compatibility output exists and is `pass`
- [ ] a decision row states route proof, quality boundary, and next action
- [ ] the audit output is linked into the evidence pack or capstone workbook

## References

- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM First Runtime Health Snapshot]]
- [[LLM/Study/Local LLM First Runtime Health Runner]]
- [[LLM/Study/Local LLM First Smoke Request Runner]]
- [[LLM/Study/Local LLM First Response Debrief Runner]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Runner]]
- [[LLM/Study/Local LLM First Quality Probe Runner]]
- [[LLM/Study/Local LLM Failure Triage Runner]]
- [[LLM/Study/Local LLM Hands-On Practicum Sequence]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Mastery Evidence Audit Runner]]

External/current sources checked 2026-06-15:

- [Ollama API introduction](https://docs.ollama.com/api/introduction)
- [Ollama generate endpoint](https://docs.ollama.com/api/generate)
- [Ollama chat endpoint](https://docs.ollama.com/api/chat)
- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
