---
tags: [study, llm, inference, local-llm, hosting, health, runtime, ollama, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM First Runtime Health Runner

> **One-line summary** Run one no-generation health probe for the first local LLM runtime, then save listener, native model-list, running-model, OpenAI-compatible model-list, expected-model, boundary, missing-layer, and next-route evidence.

Use this after [[LLM/Study/Local LLM First Model Pull Runner|Local LLM First Model Pull Runner]] says the selected model pull counts, and before [[LLM/Study/Local LLM First Smoke Request Runner|Local LLM First Smoke Request Runner]] sends the first prompt. This runner turns [[LLM/Study/Local LLM First Runtime Health Snapshot|Local LLM First Runtime Health Snapshot]] into repeatable JSON, Markdown, CSV, and JSONL evidence.

This runner does not call `/api/generate`, `/api/chat`, or `/v1/chat/completions`. It answers only: "Is the server reachable, does the runtime expose model-list routes, is the expected model visible, is anything loaded now, and is the next owner install, model id, route, security, or smoke?"

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| TCP listener probe | The selected host and port accept a connection. | The process is the intended runtime. |
| Native version or tags route | The native runtime API is reachable. | Generation quality or chat-template correctness. |
| `/api/tags` or equivalent model list | The local runtime can see installed model ids. | The model is loaded into memory. |
| `/api/ps` or equivalent running-model list | The runner captured loaded or idle state before prompting. | Empty loaded state is a failure. |
| `/v1/models` when required | The OpenAI-compatible model-list route is available. | Chat completions, streaming, tools, or JSON mode work. |
| Expected model check | The intended tag or served id is visible before smoke. | The selected model is good for the workload. |
| Boundary check | The probed URLs are loopback unless a security review is declared. | Production exposure is safe. |

Academic bridge: this is the pre-inference boundary between model custody and request execution. It proves runtime discovery and model-id visibility before any prefill or decode work happens. If this fails, do not interpret a later prompt failure as model quality.

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "first-runtime-health-001",
  "runtime": "ollama",
  "native_bases": ["http://127.0.0.1:11434"],
  "openai_bases": ["http://127.0.0.1:11434/v1"],
  "expected_model": "qwen3.5:4b",
  "security_boundary": "loopback only",
  "require_openai_models": true,
  "next_route": "LLM/Study/Local LLM First Smoke Request Runner"
}
```

Optional fields:

```json
{
  "run_root": "D:/llm-runs/2026-06-15-first-endpoint",
  "vault_root": "D:/Vaults/PersonalKB",
  "timeout_s": 3,
  "security_review_proof": "",
  "source_pull_runner": "path/to/first-model-pull.json",
  "notes": "No prompts were sent."
}
```

Use `require_openai_models: false` only when the first endpoint is intentionally native-only. If the endpoint is bound to a LAN address, `0.0.0.0`, a tunnel, or remote host, do not proceed to smoke until [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] has a linked review.

## Standard-Library Runner

Save this as `first-runtime-health-runner.py` in the run folder, or extract it directly from this note. It uses only Python's standard library.

```python
from __future__ import annotations

import csv
import datetime as dt
import json
import os
import re
import socket
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


def utc_iso() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def slug(value: Any) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value or "").strip()).strip("-")
    return text or "run"


def text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def bool_value(value: Any, default: bool = False) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() not in {"", "0", "false", "no", "off"}


def list_value(value: Any, default: list[str] | None = None) -> list[str]:
    if value is None:
        return list(default or [])
    if isinstance(value, list):
        return [str(item).strip().rstrip("/") for item in value if str(item).strip()]
    if isinstance(value, str):
        return [item.strip().rstrip("/") for item in value.split(",") if item.strip()]
    return [str(value).strip().rstrip("/")]


def load_manifest() -> tuple[Path, dict[str, Any]]:
    raw_path = os.environ.get("LOCAL_LLM_RUNTIME_HEALTH_MANIFEST") or (sys.argv[1] if len(sys.argv) > 1 else "")
    if not raw_path:
        raise SystemExit("Set LOCAL_LLM_RUNTIME_HEALTH_MANIFEST or pass a manifest path.")
    path = Path(raw_path).expanduser().resolve()
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Manifest must be a JSON object.")
    return path, data


def is_loopback_host(host: str) -> bool:
    normalized = host.strip().lower().strip("[]")
    if normalized in {"localhost", "::1"}:
        return True
    if normalized.startswith("127."):
        return True
    return False


def parsed_host(base_url: str) -> str:
    parsed = urllib.parse.urlparse(base_url)
    return parsed.hostname or ""


def socket_probe(base_url: str, timeout_s: float) -> dict[str, Any]:
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


def http_get_json(url: str, timeout_s: float) -> dict[str, Any]:
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
                "raw_excerpt": " ".join(raw.split())[:500],
            }
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        elapsed_s = time.perf_counter() - started
        try:
            data = json.loads(body) if body else None
        except json.JSONDecodeError:
            data = None
        return {
            "url": url,
            "status": "error",
            "http_status": exc.code,
            "elapsed_s": round(elapsed_s, 3),
            "error_class": "HTTPError",
            "json": data,
            "raw_excerpt": " ".join(body.split())[:500],
        }
    except Exception as exc:
        elapsed_s = time.perf_counter() - started
        return {
            "url": url,
            "status": "error",
            "elapsed_s": round(elapsed_s, 3),
            "error_class": type(exc).__name__,
            "error": str(exc),
        }


def normalize_model(value: Any) -> str:
    return re.sub(r"[^a-z0-9._:/-]+", "", str(value or "").lower())


def models_from_ollama(response: dict[str, Any]) -> list[str]:
    data = response.get("json") if isinstance(response, dict) else None
    if not isinstance(data, dict):
        return []
    models = data.get("models") or []
    names: list[str] = []
    for item in models:
        if isinstance(item, dict):
            for value in [item.get("name"), item.get("model")]:
                if value:
                    names.append(str(value))
    return sorted(set(names))


def models_from_openai(response: dict[str, Any]) -> list[str]:
    data = response.get("json") if isinstance(response, dict) else None
    if not isinstance(data, dict):
        return []
    items = data.get("data") or []
    names: list[str] = []
    for item in items:
        if isinstance(item, dict) and item.get("id"):
            names.append(str(item["id"]))
    return sorted(set(names))


def finding(level: str, owner: str, text_value: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "owner": owner,
        "finding": text_value,
        "evidence": evidence,
        "action": action,
    }


def collect_live(manifest: dict[str, Any]) -> dict[str, Any]:
    runtime = text(manifest.get("runtime") or "ollama")
    native_bases = list_value(manifest.get("native_bases"), ["http://127.0.0.1:11434"])
    openai_bases = list_value(manifest.get("openai_bases"), ["http://127.0.0.1:11434/v1"])
    timeout_s = float(manifest.get("timeout_s") or os.environ.get("LOCAL_LLM_RUNTIME_HEALTH_TIMEOUT_S") or 3)

    socket_results = {base: socket_probe(base, timeout_s) for base in sorted(set(native_bases + openai_bases))}
    endpoint_results: dict[str, dict[str, Any]] = {}

    for base in native_bases:
        endpoint_results[f"{base}/api/version"] = http_get_json(f"{base}/api/version", timeout_s)
        endpoint_results[f"{base}/api/tags"] = http_get_json(f"{base}/api/tags", timeout_s)
        endpoint_results[f"{base}/api/ps"] = http_get_json(f"{base}/api/ps", timeout_s)

    for base in openai_bases:
        endpoint_results[f"{base}/models"] = http_get_json(f"{base}/models", timeout_s)

    return {
        "runtime": runtime,
        "native_bases": native_bases,
        "openai_bases": openai_bases,
        "timeout_s": timeout_s,
        "socket_results": socket_results,
        "endpoint_results": endpoint_results,
    }


def evaluate_health(manifest: dict[str, Any], probe: dict[str, Any]) -> dict[str, Any]:
    findings: list[dict[str, str]] = []
    expected_model = text(manifest.get("expected_model"))
    security_boundary = text(manifest.get("security_boundary"))
    security_review_proof = text(manifest.get("security_review_proof"))
    require_openai_models = bool_value(manifest.get("require_openai_models"), True)

    native_bases = list_value(probe.get("native_bases"), ["http://127.0.0.1:11434"])
    openai_bases = list_value(probe.get("openai_bases"), ["http://127.0.0.1:11434/v1"])
    endpoint_results = probe.get("endpoint_results") if isinstance(probe.get("endpoint_results"), dict) else {}
    socket_results = probe.get("socket_results") if isinstance(probe.get("socket_results"), dict) else {}

    if not expected_model:
        findings.append(finding(
            "hold",
            "manifest",
            "Expected model id is missing.",
            "expected_model",
            "Record the pulled model id before runtime health can prove the intended model is visible.",
        ))

    non_loopback = []
    for base in sorted(set(native_bases + openai_bases)):
        host = parsed_host(base)
        if host and not is_loopback_host(host):
            non_loopback.append(base)
    if non_loopback and not security_review_proof:
        findings.append(finding(
            "fail",
            "security",
            "One or more probed bases are not loopback and no security review proof is linked.",
            ", ".join(non_loopback),
            "Route to the local LLM security and privacy runbook before sending prompts to this endpoint.",
        ))
    elif security_boundary and "loopback" not in security_boundary.lower() and not security_review_proof:
        findings.append(finding(
            "hold",
            "security",
            "Security boundary is not loopback-only and no review proof is linked.",
            security_boundary,
            "Link the security review before endpoint smoke.",
        ))

    listener_pass = any(isinstance(row, dict) and row.get("status") == "pass" for row in socket_results.values())
    if not listener_pass:
        findings.append(finding(
            "fail",
            "listener",
            "No configured native or OpenAI-compatible base accepted a TCP connection.",
            "socket_results",
            "Start the runtime, fix the port, or return to the Windows runtime install gate.",
        ))

    version_pass = any(key.endswith("/api/version") and value.get("status") == "pass" for key, value in endpoint_results.items())
    tags_pass = any(key.endswith("/api/tags") and value.get("status") == "pass" for key, value in endpoint_results.items())
    ps_seen = any(key.endswith("/api/ps") for key in endpoint_results)
    ps_pass = any(key.endswith("/api/ps") and value.get("status") == "pass" for key, value in endpoint_results.items())
    openai_pass = any(key.endswith("/models") and value.get("status") == "pass" for key, value in endpoint_results.items())

    if not version_pass and not tags_pass:
        findings.append(finding(
            "hold",
            "runtime-api",
            "Native runtime API did not return a version or model-list response.",
            "api/version, api/tags",
            "Confirm the base URL belongs to the intended runtime before smoke testing.",
        ))

    if ps_seen and not ps_pass:
        findings.append(finding(
            "hold",
            "loaded-model-state",
            "Running-model route was probed but did not return successfully.",
            "api/ps",
            "Capture loaded or idle state before claiming runtime health.",
        ))

    if require_openai_models and not openai_pass:
        findings.append(finding(
            "hold",
            "openai-compatible-route",
            "OpenAI-compatible model-list route did not pass.",
            "v1/models",
            "Fix the compatibility base URL or set require_openai_models to false only for an intentional native-only first run.",
        ))

    installed_model_ids: list[str] = []
    loaded_model_ids: list[str] = []
    openai_model_ids: list[str] = []
    for key, result in endpoint_results.items():
        if not isinstance(result, dict):
            continue
        if key.endswith("/api/tags"):
            installed_model_ids.extend(models_from_ollama(result))
        elif key.endswith("/api/ps"):
            loaded_model_ids.extend(models_from_ollama(result))
        elif key.endswith("/models"):
            openai_model_ids.extend(models_from_openai(result))

    installed_model_ids = sorted(set(installed_model_ids))
    loaded_model_ids = sorted(set(loaded_model_ids))
    openai_model_ids = sorted(set(openai_model_ids))
    visible_ids = installed_model_ids + loaded_model_ids + openai_model_ids

    if not installed_model_ids and not openai_model_ids:
        findings.append(finding(
            "hold",
            "model-list",
            "No installed or OpenAI-compatible model ids were visible.",
            "model lists empty",
            "Return to model pull, model-store, or runtime boundary diagnosis before smoke testing.",
        ))

    expected_visible = False
    if expected_model:
        expected_norm = normalize_model(expected_model)
        expected_visible = any(normalize_model(item) == expected_norm for item in visible_ids)
        if not expected_visible:
            findings.append(finding(
                "hold",
                "model-id",
                f"Expected model `{expected_model}` is not visible in installed, loaded, or OpenAI-compatible model ids.",
                ", ".join(visible_ids),
                "Fix the model id, pull/store boundary, or served model alias before sending a prompt.",
            ))

    fail_count = sum(1 for item in findings if item["level"] == "fail")
    hold_count = sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        status = "fail"
        decision = "runtime_health_failed"
    elif hold_count:
        status = "hold"
        decision = "runtime_health_incomplete"
    else:
        status = "pass"
        decision = "runtime_health_ready"

    if status == "pass":
        next_route = text(manifest.get("next_route") or "LLM/Study/Local LLM First Smoke Request Runner")
        next_action = "Run the first smoke request runner with the same model id and loopback base URLs."
    else:
        next_route = text(manifest.get("hold_route") or "LLM/Study/Local LLM First Runtime Health Snapshot")
        next_action = findings[0]["action"] if findings else "Fix the runtime health manifest before smoke testing."

    return {
        "runtime": text(probe.get("runtime") or manifest.get("runtime") or "ollama"),
        "native_bases": native_bases,
        "openai_bases": openai_bases,
        "expected_model": expected_model,
        "security_boundary": security_boundary,
        "require_openai_models": require_openai_models,
        "installed_model_ids": installed_model_ids,
        "loaded_model_ids": loaded_model_ids,
        "openai_model_ids": openai_model_ids,
        "expected_model_visible": expected_visible,
        "status": status,
        "decision": decision,
        "next_route": next_route,
        "next_action": next_action,
        "missing_layer": findings[0]["owner"] if findings else "",
        "findings": findings,
        "socket_results": socket_results,
        "endpoint_results": endpoint_results,
    }


def csv_cell(value: Any) -> str:
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=True, sort_keys=True)
    return "" if value is None else str(value)


def csv_write(path: Path, findings: list[dict[str, str]]) -> None:
    fields = ["level", "owner", "finding", "evidence", "action"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in findings:
            writer.writerow({field: csv_cell(row.get(field)) for field in fields})


def md_cell(value: Any) -> str:
    if isinstance(value, (list, tuple)):
        value = ", ".join(str(item) for item in value)
    return str(value or "").replace("|", "\\|").replace("\n", " ")


def wiki_link(route: str) -> str:
    clean = str(route or "").strip()
    if not clean:
        return ""
    label = clean.split("/")[-1]
    open_link = "[" * 2
    close_link = "]" * 2
    return open_link + clean + "|" + label + close_link


def render_markdown(record: dict[str, Any]) -> str:
    result = record["result"]
    lines = [
        f"# Local LLM First Runtime Health - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Runtime: `{result['runtime']}`",
        f"- Expected model: `{result['expected_model']}`",
        f"- Expected model visible: `{result['expected_model_visible']}`",
        f"- Missing layer: `{result['missing_layer']}`",
        f"- Next route: {wiki_link(result['next_route'])}",
        "",
        "## Model State",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Native bases | {md_cell(result['native_bases'])} |",
        f"| OpenAI bases | {md_cell(result['openai_bases'])} |",
        f"| Installed model ids | {md_cell(result['installed_model_ids'])} |",
        f"| Loaded model ids | {md_cell(result['loaded_model_ids'])} |",
        f"| OpenAI model ids | {md_cell(result['openai_model_ids'])} |",
        f"| Security boundary | {md_cell(result['security_boundary'])} |",
        "",
        "## Findings",
        "",
    ]
    if result["findings"]:
        for item in result["findings"]:
            lines.append(f"- `{item['level']}` `{item['owner']}`: {item['finding']} -> {item['action']}")
    else:
        lines.append("- Runtime health is ready for the first smoke request runner.")
    lines.extend(["", "## Endpoint Results", ""])
    for name, item in result["endpoint_results"].items():
        lines.extend([
            f"### {name}",
            "",
            "```json",
            json.dumps(item, indent=2, ensure_ascii=True),
            "```",
            "",
        ])
    return "\n".join(lines)


def main() -> int:
    manifest_path, manifest = load_manifest()
    run_id = text(manifest.get("run_id") or os.environ.get("LOCAL_LLM_RUNTIME_HEALTH_RUN_ID") or f"{utc_stamp()}-{slug(manifest_path.stem)}")
    run_root_value = os.environ.get("LOCAL_LLM_RUNTIME_HEALTH_RUN_ROOT") or manifest.get("run_root", "local-llm-runtime-health-runs")
    run_root = Path(str(run_root_value)).expanduser()
    if not run_root.is_absolute():
        run_root = manifest_path.parent / run_root
    run_root = run_root.resolve()
    run_dir = run_root / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    probe = collect_live(manifest)
    result = evaluate_health(manifest, probe)
    status = result["status"]
    decision = result["decision"]

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "manifest_path": str(manifest_path),
        "status": status,
        "decision": decision,
        "result": result,
        "outputs": {},
    }

    json_path = run_dir / f"{run_id}-runtime-health.json"
    markdown_path = run_dir / f"{run_id}-runtime-health.md"
    csv_path = run_dir / f"{run_id}-runtime-health-findings.csv"
    jsonl_path = run_root / "local-llm-runtime-health-runs.jsonl"
    record["outputs"] = {
        "json": str(json_path),
        "markdown": str(markdown_path),
        "csv": str(csv_path),
        "jsonl": str(jsonl_path),
    }

    csv_write(csv_path, result["findings"])
    json_path.write_text(json.dumps(record, indent=2, ensure_ascii=True), encoding="utf-8")
    markdown_path.write_text(render_markdown(record) + "\n", encoding="utf-8")
    with jsonl_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=True) + "\n")

    print(json.dumps({
        "status": status,
        "decision": decision,
        "run_id": run_id,
        "missing_layer": result["missing_layer"],
        "output_dir": str(run_dir),
        "next_route": result["next_route"],
    }, indent=2))
    return 0 if status == "pass" else 1 if status == "hold" else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(json.dumps({"status": "error", "decision": "runner_exception", "error": str(exc)}, indent=2), file=sys.stderr)
        raise
```

PowerShell run:

```powershell
$Manifest = Join-Path $RunRoot "runtime-health-manifest.json"
@{
  run_id = "first-runtime-health-001"
  runtime = "ollama"
  native_bases = @("http://127.0.0.1:11434")
  openai_bases = @("http://127.0.0.1:11434/v1")
  expected_model = "<model-tag-or-served-id>"
  security_boundary = "loopback only"
  require_openai_models = $true
  next_route = "LLM/Study/Local LLM First Smoke Request Runner"
} | ConvertTo-Json -Depth 8 | Set-Content $Manifest

$env:LOCAL_LLM_RUNTIME_HEALTH_MANIFEST = $Manifest
$env:LOCAL_LLM_RUNTIME_HEALTH_RUN_ROOT = $RunRoot
python .\first-runtime-health-runner.py
```

Pass signal: the runner writes `<run-id>-runtime-health.json`, `<run-id>-runtime-health.md`, `<run-id>-runtime-health-findings.csv`, appends `local-llm-runtime-health-runs.jsonl`, and prints `pass/runtime_health_ready`.

## Decision Table

| Status / decision | Meaning | Next route |
|---|---|---|
| `pass/runtime_health_ready` | Listener, native API, model-list, expected model, and required OpenAI-compatible model-list checks are ready for a first prompt. | [[LLM/Study/Local LLM First Smoke Request Runner]] |
| `hold/runtime_health_incomplete` | The runtime is partly reachable but model id, route, loaded-state, OpenAI-compatible list, or manifest evidence is incomplete. | [[LLM/Study/Local LLM First Runtime Health Snapshot]] or [[LLM/Study/Local LLM Troubleshooting Decision Tree]] |
| `fail/runtime_health_failed` | Listener or security boundary evidence contradicts a safe first smoke request. | [[LLM/Study/Local LLM Windows Runtime Install Gate]] or [[LLM/Study/Local LLM Security and Privacy Runbook]] |

## Evidence Row

Copy this row into [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]], [[LLM/Study/Local LLM First Inference Evidence Pack|Local LLM First Inference Evidence Pack]], or [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]:

| Field | Value |
|---|---|
| Run id |  |
| Runtime |  |
| Native base URL |  |
| OpenAI-compatible base URL |  |
| Expected model |  |
| Installed model ids |  |
| Loaded model ids or idle state |  |
| OpenAI-compatible model ids |  |
| Security boundary |  |
| Status / decision |  |
| Missing layer |  |
| Health JSON |  |
| Health Markdown |  |
| Findings CSV |  |
| JSONL row |  |
| Next route |  |

## Completion Gate

This runner output counts only when:

- [ ] manifest names runtime, native base URL, OpenAI-compatible base URL, expected model, security boundary, and `require_openai_models`
- [ ] listener probe is saved
- [ ] native runtime API state is saved
- [ ] installed model ids are saved or the missing model-list layer is explicit
- [ ] loaded model ids or idle state is saved
- [ ] OpenAI-compatible model-list state is saved or intentionally waived
- [ ] expected model visibility is pass or the model-id mismatch is explicit
- [ ] non-loopback exposure is either absent or backed by security-review proof
- [ ] JSON, Markdown, CSV, and JSONL outputs are linked from the endpoint evidence folder

## References

Internal routes:

- [[LLM/Study/Local LLM First Runtime Health Snapshot]]
- [[LLM/Study/Local LLM First Model Pull Runner]]
- [[LLM/Study/Local LLM First Smoke Request Runner]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner]]
- [[LLM/Study/Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]

External/current sources checked 2026-06-15:

- [Ollama API introduction](https://docs.ollama.com/api/introduction)
- [Ollama list models](https://docs.ollama.com/api/tags)
- [Ollama list running models](https://docs.ollama.com/api/ps)
- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
