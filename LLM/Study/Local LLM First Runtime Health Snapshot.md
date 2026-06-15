---
tags: [study, llm, inference, local-llm, hosting, health, runtime, ollama, evidence]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM First Runtime Health Snapshot

> **One-line summary** Before treating a local LLM server as ready for inference, capture one no-inference health snapshot: listener reachability, runtime API state, installed models, loaded models, OpenAI-compatible model ids, missing layers, and next action.

Use this after [[LLM/Study/Local LLM Windows Runtime Install Gate|Local LLM Windows Runtime Install Gate]] proves the runtime command/listener and after [[LLM/Study/Local LLM First Model Pull Gate|Local LLM First Model Pull Gate]] when a model tag should be visible. Use it before [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]] if you want a compact pre-smoke artifact, and again before [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]] if a restart, model pull, cache move, or UI change might have changed server state.

This snapshot does not run inference. It is a readiness artifact for hosting: "Is the server reachable, which model ids does it expose, what is loaded now, and what still blocks an endpoint smoke test?"

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| TCP listener probe | Something is reachable at the chosen host and port. | The process is the intended runtime. |
| `/api/tags` response | Ollama can list installed local models. | A model is loaded into memory. |
| `/api/ps` response | Ollama can list currently loaded/running models. | A model must be loaded when no request has run yet. |
| `/v1/models` response | An OpenAI-compatible model-list route is available. | Chat completions will succeed. |
| Expected model check | The intended tag or served id is visible. | Quality, speed, or prompt compatibility. |
| Health JSON/Markdown | The run can be linked from the endpoint sheet or capstone. | Production observability. |

For first setup, `/api/ps` may be empty before any request. That is a valid snapshot if `/api/tags` or `/v1/models` proves the model id is available.

## Fixed Conditions

Write these before running:

| Field | Value |
|---|---|
| Run folder |  |
| Runtime | Ollama / LM Studio / llama.cpp / vLLM / SGLang / other |
| Native base URL | `http://127.0.0.1:11434` for Ollama |
| OpenAI-compatible base URL | `http://127.0.0.1:11434/v1` for Ollama |
| Expected model id |  |
| Runtime boundary | Windows native / WSL / Docker / remote Linux / desktop GUI |
| Security boundary | loopback only / LAN / tunnel / remote |
| Next gate | endpoint smoke / model pull / install diagnosis / security review |

If a listener is bound to `0.0.0.0`, a LAN IP, or a tunnel, stop and route to [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] before running prompts.

## Standard-Library Health Snapshot

Save this as `first-runtime-health.py` inside the run folder. It uses only Python's standard library and makes no chat or generation request.

```python
import json
import os
import socket
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


def split_csv(value, default):
    text = value if value is not None else default
    return [item.strip().rstrip("/") for item in text.split(",") if item.strip()]


def http_get_json(url, timeout_s):
    started = time.perf_counter()
    try:
        request = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(request, timeout=timeout_s) as response:
            raw = response.read().decode("utf-8", errors="replace")
            elapsed_s = time.perf_counter() - started
            try:
                data = json.loads(raw) if raw else None
            except json.JSONDecodeError:
                data = None
            return {
                "url": url,
                "status": "pass",
                "http_status": getattr(response, "status", None),
                "elapsed_s": round(elapsed_s, 3),
                "json": data,
                "raw_excerpt": " ".join(raw.split())[:300],
            }
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        return {
            "url": url,
            "status": "error",
            "http_status": exc.code,
            "error_class": "HTTPError",
            "raw_excerpt": " ".join(body.split())[:300],
        }
    except Exception as exc:
        return {
            "url": url,
            "status": "error",
            "error_class": type(exc).__name__,
            "error": str(exc),
        }


def socket_probe(base_url, timeout_s):
    parsed = urllib.parse.urlparse(base_url)
    host = parsed.hostname or "127.0.0.1"
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    started = time.perf_counter()
    try:
        with socket.create_connection((host, port), timeout=timeout_s):
            elapsed_s = time.perf_counter() - started
        return {
            "base_url": base_url,
            "host": host,
            "port": port,
            "status": "pass",
            "elapsed_s": round(elapsed_s, 3),
        }
    except Exception as exc:
        return {
            "base_url": base_url,
            "host": host,
            "port": port,
            "status": "error",
            "error_class": type(exc).__name__,
            "error": str(exc),
        }


def models_from_tags(response):
    data = response.get("json") if isinstance(response, dict) else None
    if not isinstance(data, dict):
        return []
    models = data.get("models") or []
    names = []
    for item in models:
        if isinstance(item, dict):
            names.extend(value for value in (item.get("name"), item.get("model")) if value)
    return sorted(set(names))


def models_from_openai(response):
    data = response.get("json") if isinstance(response, dict) else None
    if not isinstance(data, dict):
        return []
    items = data.get("data") or []
    names = []
    for item in items:
        if isinstance(item, dict) and item.get("id"):
            names.append(item["id"])
    return sorted(set(names))


def md_cell(value):
    return str(value or "").replace("|", "\\|").replace("\n", " ")


def write_markdown(path, record):
    lines = [
        f"# Runtime Health Snapshot - {record['run_id']}",
        "",
        f"Status: `{record['status']}`",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Runtime | {md_cell(record['runtime'])} |",
        f"| Native base URLs | {md_cell(', '.join(record['native_bases']))} |",
        f"| OpenAI-compatible base URLs | {md_cell(', '.join(record['openai_bases']))} |",
        f"| Expected model | {md_cell(record['expected_model'])} |",
        f"| Installed model ids | {md_cell(', '.join(record['installed_model_ids']))} |",
        f"| Loaded model ids | {md_cell(', '.join(record['loaded_model_ids']))} |",
        f"| OpenAI model ids | {md_cell(', '.join(record['openai_model_ids']))} |",
        f"| Missing layer | {md_cell(record['missing_layer'])} |",
        f"| Next action | {md_cell(record['next_action'])} |",
        "",
        "## Endpoint Results",
        "",
    ]
    for name, result in record["endpoint_results"].items():
        lines.extend([
            f"### {name}",
            "",
            "```json",
            json.dumps(result, indent=2, ensure_ascii=True),
            "```",
            "",
        ])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


RUN_ROOT = Path(os.environ.get("LOCAL_LLM_RUN_ROOT", ".")).resolve()
RUNTIME = os.environ.get("LOCAL_LLM_RUNTIME", "ollama")
EXPECTED_MODEL = os.environ.get("LOCAL_LLM_EXPECT_MODEL", "")
NEXT_ACTION = os.environ.get("LOCAL_LLM_NEXT_ACTION", "endpoint smoke if health passes")
TIMEOUT_S = float(os.environ.get("LOCAL_LLM_HEALTH_TIMEOUT_S", "3"))

native_bases = split_csv(os.environ.get("LOCAL_LLM_NATIVE_BASES"), "http://127.0.0.1:11434")
openai_bases = split_csv(os.environ.get("LOCAL_LLM_OPENAI_BASES"), "http://127.0.0.1:11434/v1")

out_dir = RUN_ROOT / "first-runtime-health"
out_dir.mkdir(parents=True, exist_ok=True)

run_id = f"{time.strftime('%Y%m%d-%H%M%S')}-runtime-health"
timestamp = time.strftime("%Y-%m-%dT%H:%M:%S%z")

socket_results = {base: socket_probe(base, TIMEOUT_S) for base in native_bases + openai_bases}
endpoint_results = {}

for base in native_bases:
    endpoint_results[f"{base}/api/version"] = http_get_json(f"{base}/api/version", TIMEOUT_S)
    endpoint_results[f"{base}/api/tags"] = http_get_json(f"{base}/api/tags", TIMEOUT_S)
    endpoint_results[f"{base}/api/ps"] = http_get_json(f"{base}/api/ps", TIMEOUT_S)

for base in openai_bases:
    endpoint_results[f"{base}/models"] = http_get_json(f"{base}/models", TIMEOUT_S)

installed_model_ids = []
loaded_model_ids = []
openai_model_ids = []
for key, result in endpoint_results.items():
    if key.endswith("/api/tags"):
        installed_model_ids.extend(models_from_tags(result))
    elif key.endswith("/api/ps"):
        loaded_model_ids.extend(models_from_tags(result))
    elif key.endswith("/models"):
        openai_model_ids.extend(models_from_openai(result))

installed_model_ids = sorted(set(installed_model_ids))
loaded_model_ids = sorted(set(loaded_model_ids))
openai_model_ids = sorted(set(openai_model_ids))
visible_ids = set(installed_model_ids + loaded_model_ids + openai_model_ids)

reachable = any(result["status"] == "pass" for result in socket_results.values())
api_reachable = any(result.get("status") == "pass" for result in endpoint_results.values())
model_visible = not EXPECTED_MODEL or EXPECTED_MODEL in visible_ids

missing = []
if not reachable:
    missing.append("tcp listener")
if reachable and not api_reachable:
    missing.append("runtime api")
if EXPECTED_MODEL and not model_visible:
    missing.append("expected model id")
if not installed_model_ids and not openai_model_ids:
    missing.append("model list")

status = "pass" if reachable and api_reachable and model_visible else "hold"
if not reachable:
    status = "error"

record = {
    "run_id": run_id,
    "timestamp": timestamp,
    "status": status,
    "runtime": RUNTIME,
    "native_bases": native_bases,
    "openai_bases": openai_bases,
    "expected_model": EXPECTED_MODEL,
    "installed_model_ids": installed_model_ids,
    "loaded_model_ids": loaded_model_ids,
    "openai_model_ids": openai_model_ids,
    "socket_results": socket_results,
    "endpoint_results": endpoint_results,
    "missing_layer": ", ".join(missing),
    "next_action": NEXT_ACTION,
}

json_path = out_dir / f"{run_id}.json"
md_path = out_dir / f"{run_id}.md"
log_path = out_dir / "runtime-health-snapshots.jsonl"

json_path.write_text(json.dumps(record, indent=2, ensure_ascii=True), encoding="utf-8")
write_markdown(md_path, record)
with log_path.open("a", encoding="utf-8") as handle:
    handle.write(json.dumps(record, ensure_ascii=True) + "\n")

print(json.dumps({"status": status, "json_path": str(json_path), "markdown_path": str(md_path)}, indent=2))
```

PowerShell run:

```powershell
$env:LOCAL_LLM_RUN_ROOT = "<paste-run-folder-path>"
$env:LOCAL_LLM_RUNTIME = "ollama"
$env:LOCAL_LLM_NATIVE_BASES = "http://127.0.0.1:11434"
$env:LOCAL_LLM_OPENAI_BASES = "http://127.0.0.1:11434/v1"
$env:LOCAL_LLM_EXPECT_MODEL = "<model-tag-or-served-id>"
$env:LOCAL_LLM_NEXT_ACTION = "endpoint smoke from Local LLM First Endpoint Run Sheet"
python .\first-runtime-health.py
```

Pass signal: the script writes `first-runtime-health\<run-id>.json`, `first-runtime-health\<run-id>.md`, and `first-runtime-health\runtime-health-snapshots.jsonl`. A first setup can pass with an empty loaded-model list if the installed or OpenAI-compatible model list contains the expected model.

## Evidence Row

Copy this into the endpoint run sheet, evidence pack, or capstone workbook:

| Field | Value |
|---|---|
| Run id |  |
| Runtime |  |
| Native base URL |  |
| OpenAI-compatible base URL |  |
| Expected model |  |
| TCP listener status |  |
| `/api/tags` status |  |
| `/api/ps` status |  |
| `/v1/models` status |  |
| Installed model ids |  |
| Loaded model ids |  |
| OpenAI-compatible model ids |  |
| Health JSON |  |
| Health Markdown |  |
| Status | pass / hold / error |
| Missing layer |  |
| Next action | endpoint smoke / model pull / install diagnosis / security review |

## Failure Routing

| Observation | Likely owner | Route |
|---|---|---|
| TCP listener missing | runtime process, port, app startup, or Windows service/tray state | [[LLM/Study/Local LLM Windows Runtime Install Gate]] or [[LLM/Study/Local LLM Serving Runbook]] |
| `/api/tags` fails but TCP connects | wrong process, API route mismatch, proxy, or runtime crash | [[LLM/Study/Local LLM Serving Runbook]] |
| `/api/tags` works but expected model absent | model pull, store path, tag mismatch, or wrong runtime boundary | [[LLM/Study/Local LLM First Model Pull Gate]] |
| `/api/ps` is empty before any request | normal idle state for first setup | Continue to endpoint smoke if model list is correct. |
| `/v1/models` fails while native API works | OpenAI-compatible surface mismatch | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]] |
| listener is non-loopback | endpoint exposure and local network risk | [[LLM/Study/Local LLM Security and Privacy Runbook]] |

## Completion Gate

This health snapshot is complete only when:

- [ ] one run folder exists
- [ ] runtime, native base URL, OpenAI-compatible base URL, expected model, runtime boundary, and security boundary are written
- [ ] socket reachability is captured
- [ ] model-list route is captured through `/api/tags`, `/v1/models`, or the runtime's equivalent model-list route
- [ ] loaded-model state is captured or explicitly marked idle/not yet loaded
- [ ] health JSON, health Markdown, and health JSONL paths exist
- [ ] the missing layer and next action are explicit
- [ ] the snapshot is linked from [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]], [[LLM/Study/Local LLM First Inference Evidence Pack|Local LLM First Inference Evidence Pack]], or [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]

## References

Internal routes:

- [[LLM/Study/Local LLM Windows Runtime Install Gate]]
- [[LLM/Study/Local LLM First Model Pull Gate]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Command Cookbook]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]

External/current sources checked 2026-06-15:

- [Ollama API introduction](https://docs.ollama.com/api/introduction)
- [Ollama list models](https://docs.ollama.com/api/tags)
- [Ollama list running models](https://docs.ollama.com/api/ps)
- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
