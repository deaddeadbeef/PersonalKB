---
tags: [study, llm, inference, local-llm, llama-cpp, gguf, server, openai-compatible, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-16
---

# Local llama.cpp GGUF Server Runner

> **One-line summary** Prove a GGUF model is actually being served by llama.cpp before benchmark, quality, client, RAG, or deployment evidence depends on it.

Use this after [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Local LLM Artifact Download Cache and Conversion Lab]], [[LLM/Study/Local LLM Model Metadata Card Runner|Local LLM Model Metadata Card Runner]], [[LLM/Study/Local LLM Runtime Compatibility Runner|Local LLM Runtime Compatibility Runner]], and [[LLM/Study/Local LLM KV Cache Sizing Runner|Local LLM KV Cache Sizing Runner]] when the chosen runtime path is `llama-server`, `llama.cpp`, or a `llama-cpp-python` server over a GGUF file. Use it before [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner|Local LLM OpenAI-Compatible API Contract Runner]], [[LLM/Study/Local LLM First Client Harness Runner|Local LLM First Client Harness Runner]], [[LLM/Study/Local LLM First Benchmark Row Builder|Local LLM First Benchmark Row Builder]], [[LLM/Study/Local LLM Runtime Comparison Lab|Local LLM Runtime Comparison Lab]], or [[LLM/Study/Local LLM Quantization and GPU Offload Lab|Local LLM Quantization and GPU Offload Lab]] when the next claim depends on a local GGUF server.

This runner does not build llama.cpp, download a model, start a process, or send inference requests. It audits evidence you already saved from the run folder: launch command, binary/build proof, GGUF path, loopback listener, `/health`, `/v1/models`, `/v1/chat/completions`, optional `/props`, optional `/slots`, optional `/metrics`, GPU/offload proof, and linked model metadata/custody/compatibility cards.

## What This Proves

| Gate | Evidence checked | Why it matters |
|---|---|---|
| Launcher and model file | `llama-server` or `python -m llama_cpp.server`, GGUF path, alias, context, slots, GPU-offload flags | ties the endpoint to the exact local file and runtime configuration |
| Safety boundary | host, port, base URL, listener artifact, security proof for non-loopback exposure | prevents private prompt endpoints from being exposed by accident |
| Readiness | `/health` saved as `{"status":"ok"}` after loading | separates a loaded server from a still-loading model |
| Model identity | `/v1/models` returns the expected id or alias and metadata | catches wrong path, wrong alias, stale process, or router confusion |
| Inference route | saved OpenAI-compatible chat response has assistant text | proves route-level inference, not quality |
| Observability | optional `/props`, `/slots`, `/metrics`, log tail, GPU proof | makes concurrency, context, offload, and later benchmark claims auditable |

Academic bridge: llama.cpp makes local inference mechanics visible. GGUF quantization, `--ctx-size`, `--parallel`, GPU layer offload, prompt cache, slots, and OpenAI-compatible routes all map directly to the theory notes on quantization, KV cache, batching, prompt reuse, and serving architecture.

## Manual Evidence Capture

Start with one run folder:

```powershell
$RunRoot = Join-Path $HOME ("Documents\local-llm-runs\" + (Get-Date -Format "yyyy-MM-dd-HHmm") + "-llama-cpp")
New-Item -ItemType Directory -Force -Path $RunRoot | Out-Null
```

Record binary and model facts:

```powershell
llama-server --help | Tee-Object -FilePath "$RunRoot\llama-server-help.txt"
Get-FileHash "<path-to-model.gguf>" | ConvertTo-Json -Depth 5 |
  Tee-Object -FilePath "$RunRoot\gguf-hash.json"
```

Start a loopback server in a separate shell:

```powershell
llama-server `
  -m "<path-to-model.gguf>" `
  --alias "<served-model-id>" `
  --host 127.0.0.1 `
  --port 8080 `
  -c 4096 `
  -np 1 `
  --metrics
```

Capture route evidence:

```powershell
$BaseUrl = "http://127.0.0.1:8080"
Invoke-RestMethod "$BaseUrl/health" |
  ConvertTo-Json -Depth 10 |
  Tee-Object -FilePath "$RunRoot\health.json"

Invoke-RestMethod "$BaseUrl/v1/models" |
  ConvertTo-Json -Depth 10 |
  Tee-Object -FilePath "$RunRoot\models.json"

$Body = @{
  model = "<served-model-id>"
  messages = @(@{ role = "user"; content = "Reply with exactly: local llm ok" })
  temperature = 0
  max_tokens = 16
} | ConvertTo-Json -Depth 6

$Body | Tee-Object -FilePath "$RunRoot\chat-request.json"
Invoke-RestMethod `
  -Uri "$BaseUrl/v1/chat/completions" `
  -Method Post `
  -ContentType "application/json" `
  -Headers @{ Authorization = "Bearer local" } `
  -Body $Body |
  ConvertTo-Json -Depth 20 |
  Tee-Object -FilePath "$RunRoot\chat-response.json"
```

Optional observability captures:

```powershell
Invoke-RestMethod "$BaseUrl/props" |
  ConvertTo-Json -Depth 20 |
  Tee-Object -FilePath "$RunRoot\props.json"

Invoke-WebRequest "$BaseUrl/metrics" |
  Select-Object -ExpandProperty Content |
  Tee-Object -FilePath "$RunRoot\metrics.txt"
```

Do not enable `--tools all` for a first proof. The llama.cpp server documentation describes built-in tools that can access the local filesystem from the Web UI; keep that disabled unless a later tool-use lab explicitly scopes and audits it.

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "llama-cpp-gguf-smoke",
  "run_root": "D:/llm-runs/llama-cpp-gguf-smoke",
  "vault_root": "D:/Vaults/PersonalKB",
  "runtime": "llama.cpp",
  "launcher": "llama-server",
  "model_id": "local-gguf-baseline",
  "model_alias": "local-gguf-baseline",
  "gguf_path": "D:/Models/gguf/model.Q4_K_M.gguf",
  "base_url": "http://127.0.0.1:8080",
  "host": "127.0.0.1",
  "port": 8080,
  "context_tokens": 4096,
  "parallel_slots": 1,
  "n_gpu_layers": 35,
  "metrics_required": false,
  "command": "llama-server -m D:/Models/gguf/model.Q4_K_M.gguf --alias local-gguf-baseline --host 127.0.0.1 --port 8080 -c 4096 -np 1 --metrics",
  "security": {
    "boundary": "loopback",
    "non_loopback_approval": ""
  },
  "artifacts": {
    "model_metadata_card": "D:/llm-runs/model-metadata/model-metadata-card.json",
    "runtime_compatibility": "D:/llm-runs/runtime-compatibility/runtime-compatibility.json",
    "kv_cache_sizing": "D:/llm-runs/kv-cache/kv-cache.json",
    "server_log": "server.log",
    "listener_artifact": "listeners.txt",
    "health_json": "health.json",
    "models_json": "models.json",
    "chat_request_json": "chat-request.json",
    "chat_response_json": "chat-response.json",
    "props_json": "props.json",
    "metrics_text": "metrics.txt"
  }
}
```

If you use `llama-cpp-python`, set `launcher` to `llama-cpp-python` and make the command `python -m llama_cpp.server --model <path> ...`. The proof obligations are the same: GGUF identity, loopback route, model-list identity, chat response, and downstream handoffs.

## Standard-Library Runner

Save this as `local_llama_cpp_gguf_server_runner.py` inside the run folder, or extract it from this note. It uses only Python's standard library.

```python
from __future__ import annotations

import csv
import datetime as dt
import json
import os
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


LOOPBACK_HOSTS = {"127.0.0.1", "localhost", "::1"}


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def clean_text(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def nonempty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, set, dict)):
        return bool(value)
    return True


def to_int(value: Any) -> int | None:
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    if isinstance(value, str):
        stripped = value.strip().replace(",", "")
        if stripped.lstrip("-").isdigit():
            return int(stripped)
    return None


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def finding(status: str, field: str, message: str, owner: str, next_action: str) -> dict[str, str]:
    return {
        "status": status,
        "field": field,
        "message": message,
        "owner": owner,
        "next_action": next_action,
    }


def path_candidates(ref: str, manifest_path: Path, manifest: dict[str, Any]) -> list[Path]:
    raw = Path(os.path.expandvars(ref))
    if raw.is_absolute():
        return [raw]
    roots = [manifest_path.parent]
    for key in ("run_root", "vault_root"):
        value = clean_text(manifest.get(key))
        if value:
            roots.append(Path(os.path.expandvars(value)))
    return [root / raw for root in roots]


def resolve_existing_path(ref: Any, manifest_path: Path, manifest: dict[str, Any]) -> Path | None:
    value = clean_text(ref)
    if not value:
        return None
    for candidate in path_candidates(value, manifest_path, manifest):
        if candidate.exists():
            return candidate
    return None


def load_json_ref(ref: Any, manifest_path: Path, manifest: dict[str, Any], label: str, findings: list[dict[str, str]], required: bool = False) -> Any:
    value = clean_text(ref)
    if not value:
        if required:
            findings.append(finding("hold", label, f"Missing required JSON artifact: {label}.", "evidence", "Save the artifact and add it to the manifest."))
        return None
    path = resolve_existing_path(value, manifest_path, manifest)
    if path is None:
        findings.append(finding("hold" if required else "hold", label, f"JSON artifact path does not exist: {value}.", "evidence", "Fix the path or regenerate the artifact."))
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        findings.append(finding("fail", label, f"JSON artifact is invalid: {path} ({exc}).", "evidence", "Regenerate the JSON artifact."))
        return None


def load_text_ref(ref: Any, manifest_path: Path, manifest: dict[str, Any], label: str, findings: list[dict[str, str]]) -> str:
    value = clean_text(ref)
    if not value:
        return ""
    path = resolve_existing_path(value, manifest_path, manifest)
    if path is None:
        findings.append(finding("hold", label, f"Text artifact path does not exist: {value}.", "evidence", "Fix the path or regenerate the artifact."))
        return ""
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        findings.append(finding("fail", label, f"Could not read text artifact: {path} ({exc}).", "evidence", "Regenerate or move the artifact."))
        return ""


def url_host(value: Any) -> str:
    text = clean_text(value)
    if not text:
        return ""
    parsed = urlparse(text)
    return parsed.hostname or ""


def url_port(value: Any) -> int | None:
    text = clean_text(value)
    if not text:
        return None
    try:
        return urlparse(text).port
    except ValueError:
        return None


def is_loopback(host: str) -> bool:
    return host.strip("[]").lower() in LOOPBACK_HOSTS


def extract_model_ids(models_json: Any) -> list[str]:
    if not isinstance(models_json, dict):
        return []
    rows = models_json.get("data")
    if not isinstance(rows, list):
        return []
    ids = []
    for row in rows:
        if isinstance(row, dict) and nonempty(row.get("id")):
            ids.append(clean_text(row.get("id")))
        elif isinstance(row, str):
            ids.append(row)
    return ids


def extract_chat_text(chat_json: Any) -> str:
    if not isinstance(chat_json, dict):
        return ""
    choices = chat_json.get("choices")
    if isinstance(choices, list) and choices:
        first = choices[0] if isinstance(choices[0], dict) else {}
        message = first.get("message") if isinstance(first.get("message"), dict) else {}
        content = message.get("content")
        if isinstance(content, list):
            parts = []
            for item in content:
                if isinstance(item, dict):
                    parts.append(clean_text(item.get("text") or item.get("content")))
                else:
                    parts.append(clean_text(item))
            return "".join(parts).strip()
        return clean_text(content)
    if isinstance(chat_json.get("content"), str):
        return clean_text(chat_json.get("content"))
    return ""


def linked_status(data: Any) -> str:
    if isinstance(data, dict):
        return clean_text(data.get("status") or data.get("decision"))
    return ""


def validate_manifest_shape(manifest: dict[str, Any], findings: list[dict[str, str]]) -> None:
    required = ["run_id", "runtime", "launcher", "model_id", "gguf_path", "base_url", "host", "port", "command"]
    for field in required:
        if not nonempty(manifest.get(field)):
            findings.append(finding("hold", field, f"Missing required manifest field: {field}.", "manifest", "Fill this field before claiming llama.cpp server proof."))
    runtime = clean_text(manifest.get("runtime")).lower()
    if runtime and "llama" not in runtime:
        findings.append(finding("fail", "runtime", f"Runtime is not a llama.cpp path: {manifest.get('runtime')}.", "manifest", "Use the correct runner or fix the runtime field."))
    launcher = clean_text(manifest.get("launcher")).lower()
    if launcher and "llama-server" not in launcher and "llama-cpp-python" not in launcher and "llama_cpp.server" not in launcher:
        findings.append(finding("hold", "launcher", "Launcher is not clearly llama-server or llama-cpp-python.", "manifest", "Record the exact launcher command."))
    gguf_path = clean_text(manifest.get("gguf_path"))
    if gguf_path and not gguf_path.lower().endswith(".gguf"):
        findings.append(finding("fail", "gguf_path", "Model path is not a GGUF file.", "artifact", "Use the artifact download/cache lab to identify the actual GGUF file."))


def validate_command(manifest: dict[str, Any], text_artifacts: dict[str, str], findings: list[dict[str, str]]) -> None:
    command = clean_text(manifest.get("command")) or text_artifacts.get("command_log", "")
    lowered = command.lower()
    if not command:
        return
    if "llama-server" not in lowered and "llama_cpp.server" not in lowered:
        findings.append(finding("hold", "command", "Launch command does not show llama-server or llama_cpp.server.", "runtime", "Save the exact server launch command."))
    if "-m " not in lowered and "--model" not in lowered:
        findings.append(finding("hold", "command", "Launch command does not show a model argument.", "runtime", "Save the command with the GGUF model path."))
    host = clean_text(manifest.get("host"))
    port = clean_text(manifest.get("port"))
    if host and host not in command:
        findings.append(finding("hold", "host", "Launch command does not show the manifest host.", "runtime", "Record the exact host flag or explain the default."))
    if port and port not in command:
        findings.append(finding("hold", "port", "Launch command does not show the manifest port.", "runtime", "Record the exact port flag or explain the default."))


def validate_boundary(manifest: dict[str, Any], text_artifacts: dict[str, str], findings: list[dict[str, str]]) -> None:
    host = clean_text(manifest.get("host"))
    base_host = url_host(manifest.get("base_url"))
    base_port = url_port(manifest.get("base_url"))
    port = to_int(manifest.get("port"))
    security = manifest.get("security") if isinstance(manifest.get("security"), dict) else {}
    approval = clean_text(security.get("non_loopback_approval") or manifest.get("security_proof"))
    boundary = clean_text(security.get("boundary") or manifest.get("boundary")).lower()
    hosts = [item for item in (host, base_host) if item]
    if hosts and not all(is_loopback(item) for item in hosts) and not approval:
        findings.append(finding("fail", "host", "Server is not limited to loopback and no security approval is linked.", "security", "Bind to 127.0.0.1 or complete the security/privacy runner first."))
    if boundary and boundary != "loopback" and not approval:
        findings.append(finding("fail", "security.boundary", f"Boundary is {boundary!r} without approval proof.", "security", "Complete the security/privacy runner before non-loopback use."))
    if port and base_port and port != base_port:
        findings.append(finding("fail", "port", "Manifest port does not match base URL port.", "route", "Fix the manifest or captured route evidence."))
    listener = text_artifacts.get("listener_artifact", "")
    if listener and port and str(port) not in listener:
        findings.append(finding("hold", "listener_artifact", "Listener artifact does not show the manifest port.", "route", "Capture the active listener while the server is running."))


def validate_health(health_json: Any, findings: list[dict[str, str]]) -> None:
    if health_json is None:
        findings.append(finding("hold", "health_json", "Missing /health evidence.", "route", "Capture /health after the model has loaded."))
        return
    if isinstance(health_json, dict) and clean_text(health_json.get("status")).lower() == "ok":
        return
    error = health_json.get("error") if isinstance(health_json, dict) and isinstance(health_json.get("error"), dict) else {}
    if clean_text(error.get("message")).lower().startswith("loading") or clean_text(error.get("code")) == "503":
        findings.append(finding("hold", "health_json", "Server health shows the model is still loading.", "route", "Repeat /health after loading completes."))
    else:
        findings.append(finding("fail", "health_json", "Server health is not ok.", "route", "Fix server load before client or benchmark evidence."))


def validate_models(manifest: dict[str, Any], models_json: Any, findings: list[dict[str, str]]) -> None:
    if models_json is None:
        findings.append(finding("hold", "models_json", "Missing /v1/models evidence.", "route", "Capture /v1/models after /health reports ok."))
        return
    ids = extract_model_ids(models_json)
    if not ids:
        findings.append(finding("hold", "models_json", "No model ids found in /v1/models.", "route", "Save the raw /v1/models response and check the server route."))
        return
    expected = clean_text(manifest.get("model_alias") or manifest.get("model_id"))
    model_id = clean_text(manifest.get("model_id"))
    accepted = {expected, model_id, clean_text(manifest.get("gguf_path"))}
    if expected and not any(item in accepted or item == expected for item in ids):
        findings.append(finding("fail", "models_json", f"/v1/models returned {ids}, not expected {expected!r}.", "route", "Fix --alias, model id, or stale server process."))


def validate_chat(manifest: dict[str, Any], chat_json: Any, findings: list[dict[str, str]]) -> None:
    if chat_json is None:
        findings.append(finding("hold", "chat_response_json", "Missing /v1/chat/completions response.", "route", "Send and save one non-streaming OpenAI-compatible chat request."))
        return
    if isinstance(chat_json, dict) and isinstance(chat_json.get("error"), dict):
        findings.append(finding("fail", "chat_response_json", f"Chat response is an error: {chat_json.get('error')}.", "route", "Fix the server route, model id, or request body before benchmarking."))
        return
    text = extract_chat_text(chat_json)
    if not text:
        findings.append(finding("hold", "chat_response_json", "Chat response has no assistant text.", "route", "Save the raw response and inspect the response schema."))
    expected = clean_text(manifest.get("expected_text"))
    if expected and expected.lower() not in text.lower():
        findings.append(finding("hold", "expected_text", "Assistant text did not contain the expected smoke string.", "route", "Treat as route proof only if the response is otherwise explainable."))


def validate_props(manifest: dict[str, Any], props_json: Any, findings: list[dict[str, str]]) -> None:
    if props_json is None:
        return
    total_slots = to_int(props_json.get("total_slots")) if isinstance(props_json, dict) else None
    expected_slots = to_int(manifest.get("parallel_slots"))
    if expected_slots and total_slots and total_slots != expected_slots:
        findings.append(finding("hold", "props_json", "Captured /props total_slots does not match manifest parallel_slots.", "runtime", "Check -np/--parallel and rerun /props."))
    props_model = clean_text(props_json.get("model_path")) if isinstance(props_json, dict) else ""
    gguf_name = Path(clean_text(manifest.get("gguf_path"))).name
    if props_model and gguf_name and gguf_name not in props_model:
        findings.append(finding("hold", "props_json", "Captured /props model_path does not match the manifest GGUF filename.", "runtime", "Check for a stale server process or wrong model path."))


def validate_metrics(manifest: dict[str, Any], metrics_text: str, findings: list[dict[str, str]]) -> None:
    required = bool(manifest.get("metrics_required"))
    if required and not metrics_text:
        findings.append(finding("hold", "metrics_text", "Metrics are required but no /metrics artifact is linked.", "observability", "Start with --metrics and save /metrics output."))
        return
    if metrics_text and "llamacpp:" not in metrics_text:
        findings.append(finding("hold", "metrics_text", "Metrics artifact does not contain llama.cpp metric names.", "observability", "Verify that /metrics was enabled and captured."))


def validate_gpu(manifest: dict[str, Any], text_artifacts: dict[str, str], findings: list[dict[str, str]]) -> None:
    n_gpu_layers = to_int(manifest.get("n_gpu_layers"))
    gpu_proof = text_artifacts.get("gpu_artifact", "")
    if n_gpu_layers and n_gpu_layers > 0 and not gpu_proof:
        findings.append(finding("hold", "gpu_artifact", "GPU offload is configured but no GPU evidence is linked.", "hardware", "Capture nvidia-smi, llama.cpp log offload lines, or hardware runner proof."))


def validate_linked_cards(json_artifacts: dict[str, Any], findings: list[dict[str, str]]) -> None:
    for label in ("model_metadata_card", "runtime_compatibility", "kv_cache_sizing"):
        data = json_artifacts.get(label)
        if data is None:
            continue
        status = linked_status(data)
        if status and status not in {"pass", "ready", "model_metadata_ready", "runtime_compatibility_ready", "kv_cache_sizing_ready"}:
            findings.append(finding("hold", label, f"Linked {label} is not pass/ready: {status}.", "handoff", "Resolve the upstream hold before using this server as downstream evidence."))


def status_from_findings(findings: list[dict[str, str]]) -> tuple[str, str]:
    statuses = {item["status"] for item in findings}
    if "fail" in statuses:
        return "fail", "llama_cpp_server_blocked"
    if "hold" in statuses:
        return "hold", "llama_cpp_server_incomplete"
    return "pass", "llama_cpp_server_ready"


def choose_next_route(status: str, findings: list[dict[str, str]]) -> str:
    if status == "pass":
        return "LLM/Study/Local LLM OpenAI-Compatible API Contract Runner"
    first = findings[0] if findings else {}
    owner = first.get("owner")
    if owner == "security":
        return "LLM/Study/Local LLM Security and Privacy Runner"
    if owner == "artifact":
        return "LLM/Study/Local LLM Artifact Download Cache and Conversion Lab"
    if owner == "hardware":
        return "LLM/Study/Local LLM Quantization and GPU Offload Lab"
    if owner == "handoff":
        return "LLM/Study/Local LLM Runtime Compatibility Runner"
    return "LLM/Study/Local LLM Troubleshooting Decision Tree"


def build_record(manifest_path: Path) -> dict[str, Any]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    findings: list[dict[str, str]] = []
    artifacts = manifest.get("artifacts") if isinstance(manifest.get("artifacts"), dict) else {}
    json_artifacts = {
        "model_metadata_card": load_json_ref(artifacts.get("model_metadata_card"), manifest_path, manifest, "model_metadata_card", findings),
        "runtime_compatibility": load_json_ref(artifacts.get("runtime_compatibility"), manifest_path, manifest, "runtime_compatibility", findings),
        "kv_cache_sizing": load_json_ref(artifacts.get("kv_cache_sizing"), manifest_path, manifest, "kv_cache_sizing", findings),
        "health_json": load_json_ref(artifacts.get("health_json"), manifest_path, manifest, "health_json", findings),
        "models_json": load_json_ref(artifacts.get("models_json"), manifest_path, manifest, "models_json", findings),
        "chat_request_json": load_json_ref(artifacts.get("chat_request_json"), manifest_path, manifest, "chat_request_json", findings),
        "chat_response_json": load_json_ref(artifacts.get("chat_response_json"), manifest_path, manifest, "chat_response_json", findings),
        "props_json": load_json_ref(artifacts.get("props_json"), manifest_path, manifest, "props_json", findings),
        "slots_json": load_json_ref(artifacts.get("slots_json"), manifest_path, manifest, "slots_json", findings),
    }
    text_artifacts = {
        "command_log": load_text_ref(artifacts.get("command_log"), manifest_path, manifest, "command_log", findings),
        "listener_artifact": load_text_ref(artifacts.get("listener_artifact"), manifest_path, manifest, "listener_artifact", findings),
        "metrics_text": load_text_ref(artifacts.get("metrics_text"), manifest_path, manifest, "metrics_text", findings),
        "server_log": load_text_ref(artifacts.get("server_log"), manifest_path, manifest, "server_log", findings),
        "gpu_artifact": load_text_ref(artifacts.get("gpu_artifact"), manifest_path, manifest, "gpu_artifact", findings),
    }

    validate_manifest_shape(manifest, findings)
    validate_command(manifest, text_artifacts, findings)
    validate_boundary(manifest, text_artifacts, findings)
    validate_health(json_artifacts.get("health_json"), findings)
    validate_models(manifest, json_artifacts.get("models_json"), findings)
    validate_chat(manifest, json_artifacts.get("chat_response_json"), findings)
    validate_props(manifest, json_artifacts.get("props_json"), findings)
    validate_metrics(manifest, text_artifacts.get("metrics_text", ""), findings)
    validate_gpu(manifest, text_artifacts, findings)
    validate_linked_cards(json_artifacts, findings)

    if not findings:
        findings.append(finding("pass", "llama_cpp_server", "llama.cpp GGUF server evidence is ready.", "server", "Continue to OpenAI-compatible contract and client harness evidence."))
    status, decision = status_from_findings(findings)
    return {
        "run_id": manifest.get("run_id") or manifest_path.stem,
        "generated_at": now_iso(),
        "manifest_path": str(manifest_path),
        "status": status,
        "decision": decision,
        "next_route": choose_next_route(status, findings),
        "manifest": manifest,
        "observed": {
            "model_ids": extract_model_ids(json_artifacts.get("models_json")),
            "assistant_text": extract_chat_text(json_artifacts.get("chat_response_json")),
            "health": json_artifacts.get("health_json"),
            "props_total_slots": json_artifacts.get("props_json", {}).get("total_slots") if isinstance(json_artifacts.get("props_json"), dict) else None,
            "metrics_present": bool(text_artifacts.get("metrics_text")),
        },
        "findings": findings,
    }


def obsidian_link(target: str) -> str:
    return ("[" * 2) + target + ("]" * 2)


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_markdown(path: Path, record: dict[str, Any]) -> None:
    manifest = record["manifest"]
    observed = record["observed"]
    lines = [
        f"# llama.cpp GGUF Server - {record['run_id']}",
        "",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Next route: {obsidian_link(record['next_route'])}",
        f"- Base URL: `{manifest.get('base_url', '')}`",
        f"- Model id: `{manifest.get('model_id', '')}`",
        f"- GGUF: `{manifest.get('gguf_path', '')}`",
        "",
        "## Observed",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| model ids | `{json.dumps(observed.get('model_ids'), ensure_ascii=True)}` |",
        f"| health | `{json.dumps(observed.get('health'), ensure_ascii=True)}` |",
        f"| props total slots | `{observed.get('props_total_slots') or ''}` |",
        f"| metrics present | `{observed.get('metrics_present')}` |",
        f"| assistant text | `{str(observed.get('assistant_text') or '').replace('|', '/').replace(chr(10), ' ')[:240]}` |",
        "",
        "## Findings",
        "",
        "| Status | Field | Message | Owner | Next action |",
        "|---|---|---|---|---|",
    ]
    for item in record["findings"]:
        lines.append(f"| `{item['status']}` | `{item['field']}` | {item['message']} | `{item['owner']}` | {item['next_action']} |")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_csv(path: Path, findings: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["status", "field", "message", "owner", "next_action"])
        writer.writeheader()
        for item in findings:
            writer.writerow(item)


def write_jsonl(path: Path, record: dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        handle.write(json.dumps({"type": "summary", "run_id": record["run_id"], "status": record["status"], "decision": record["decision"], "next_route": record["next_route"]}, sort_keys=True) + "\n")
        for item in record["findings"]:
            handle.write(json.dumps({"type": "finding", "run_id": record["run_id"], **item}, sort_keys=True) + "\n")


def write_outputs(record: dict[str, Any], out_dir: Path) -> dict[str, str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = record["run_id"]
    paths = {
        "json": out_dir / f"{stem}-llama-cpp-server.json",
        "markdown": out_dir / f"{stem}-llama-cpp-server.md",
        "csv": out_dir / f"{stem}-llama-cpp-server-findings.csv",
        "jsonl": out_dir / f"{stem}-llama-cpp-server-findings.jsonl",
    }
    write_json(paths["json"], record)
    write_markdown(paths["markdown"], record)
    write_csv(paths["csv"], record["findings"])
    write_jsonl(paths["jsonl"], record)
    return {key: str(path) for key, path in paths.items()}


def main(argv: list[str]) -> int:
    if len(argv) not in {2, 3}:
        print("Usage: python local_llama_cpp_gguf_server_runner.py <manifest.json> [output_dir]", file=sys.stderr)
        return 2
    manifest_path = Path(argv[1]).resolve()
    if not manifest_path.exists():
        print(f"Manifest not found: {manifest_path}", file=sys.stderr)
        return 2
    record = build_record(manifest_path)
    out_dir = Path(argv[2]).resolve() if len(argv) == 3 else manifest_path.parent / "llama-cpp-server-results"
    outputs = write_outputs(record, out_dir)
    print(json.dumps({"status": record["status"], "decision": record["decision"], "next_route": record["next_route"], "outputs": outputs}, indent=2, sort_keys=True))
    return 1 if record["status"] == "fail" else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
```

## Fixture Checks

Use these before trusting an edited copy:

| Fixture | Expected status | Why |
|---|---|---|
| Loopback command, `.gguf` path, `/health` ok, `/v1/models` expected id, chat response text, and pass upstream cards | `pass` | The server route is ready for OpenAI-compatible contract and client evidence. |
| Non-loopback host with no security/privacy proof | `fail` | The first local proof should not expose private prompts by accident. |
| `/health` reports loading or 503 | `hold` | The model is not ready yet; repeat health and route capture after load. |
| `/v1/models` returns a different id than the manifest alias | `fail` | The endpoint may be a stale or wrong server. |
| Missing chat response artifact | `hold` | Model-list proof is not inference proof. |

## Completion Gate

This runner is complete when you have:

- [ ] exact launcher command, host, port, alias, GGUF path, context, slots, and offload settings recorded
- [ ] loopback listener proof, or security/privacy approval before non-loopback use
- [ ] `/health` captured after load
- [ ] `/v1/models` captured and matched to the expected id or alias
- [ ] one non-streaming `/v1/chat/completions` request and response saved
- [ ] model metadata, runtime compatibility, and KV-cache sizing cards linked when downstream decisions depend on them
- [ ] optional `/props`, `/slots`, `/metrics`, server log, and GPU evidence saved when concurrency, observability, or offload claims depend on them
- [ ] JSON, Markdown, CSV, and JSONL runner outputs saved before benchmark, quality, runtime comparison, or deployment evidence uses this server

## References

Internal:

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab]]
- [[LLM/Study/Local LLM Model Metadata Card Runner]]
- [[LLM/Study/Local LLM Runtime Compatibility Runner]]
- [[LLM/Study/Local LLM KV Cache Sizing Runner]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]]
- [[LLM/Study/Local LLM First Client Harness Runner]]
- [[LLM/Study/Local LLM First Benchmark Row Builder]]
- [[LLM/Study/Local LLM Runtime Comparison Lab]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Lab]]
- [[LLM/Study/Local LLM Security and Privacy Runner]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Runner]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]

Current external docs checked 2026-06-16:

- [llama.cpp server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
- [llama.cpp README server section](https://github.com/ggml-org/llama.cpp)
- [llama.cpp build documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md)
- [llama-cpp-python OpenAI-compatible server](https://llama-cpp-python.readthedocs.io/en/latest/server/)
