---
tags: [study, llm, inference, local-llm, windows, ollama, install, readiness, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-16
---

# Local LLM Windows Runtime Install Runner

> **One-line summary** Audit an installed Windows Ollama runtime without pulling a model or sending inference, then write pass/hold/fail evidence for PATH, model-store inheritance, loopback listener, `/api/version`, and `/api/tags`.

Use this with [[LLM/Study/Local LLM Windows Runtime Install Gate|Local LLM Windows Runtime Install Gate]] after [[LLM/Study/Local LLM Model Store Readiness Snapshot|Local LLM Model Store Readiness Snapshot]] and before [[LLM/Study/Local LLM First Model Pull Gate|Local LLM First Model Pull Gate]]. The install gate explains the manual steps. This runner turns the post-install state into JSON, Markdown, CSV, and JSONL proof.

The runner does not install Ollama, run `ollama pull`, call `/api/chat`, call `/api/generate`, or call `/v1/chat/completions`. It is deliberately a no-generation gate between runtime installation and model acquisition.

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| `ollama` command path | A new shell can resolve the runtime command. | The runtime can load a model. |
| `ollama --version` | The CLI can execute and report a version. | The local API listener is reachable. |
| `ollama ls` | The CLI can list the local model inventory, even if empty. | A selected model tag has been pulled. |
| `OLLAMA_MODELS` process/user evidence | The model-store decision is visible before the first pull when a custom store is expected. | That future pulls will be fast or fit disk. |
| listener and netstat rows | The planned native base URL is reachable and not obviously bound to a wildcard address. | Firewall, LAN, or tunnel exposure is globally impossible. |
| `/api/version` and `/api/tags` | The local read-only API surface is alive before model pull. | Generation quality, latency, or OpenAI-compatible route behavior. |

Academic bridge: this is a serving-layer falsification gate. It separates installation/PATH/env/listener failures from model artifact, tokenizer, prefill, decode, sampler, and quality failures.

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "first-local-inference-runtime-install",
  "run_root": "D:/llm-runs/2026-06-16-first-local-inference",
  "runtime": "ollama",
  "installer_source": "https://ollama.com/download/windows",
  "installer_method": "official Windows installer or existing install",
  "model_store_decision": "default user profile store accepted",
  "native_base_url": "http://127.0.0.1:11434",
  "require_loopback": true,
  "require_command": true,
  "require_listener": true,
  "require_api_version": true,
  "require_api_tags": true
}
```

Use `expected_ollama_models` only when the first model pull must use a custom store such as `D:\Models\ollama`. If the default user-profile store is intentionally accepted, leave `expected_ollama_models` blank and record that decision in `model_store_decision`.

Optional fields:

```json
{
  "output_root": "D:/llm-runs/windows-runtime-install",
  "expected_ollama_models": "D:/Models/ollama",
  "pass_next_route": "LLM/Study/Local LLM First Model Source Recheck Runner",
  "hold_next_route": "LLM/Study/Local LLM Windows Runtime Install Gate",
  "fail_next_route": "LLM/Study/Local LLM Security and Privacy Runbook"
}
```

`probe_override` is supported only for fixtures and runner tests. Do not use it for real install evidence.

## Standard-Library Runner

Save this as `windows-runtime-install-runner.py` in the run folder or extract it directly from this note.

```python
from __future__ import annotations

import csv
import datetime as dt
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


def utc_iso() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def display(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def slug(value: Any) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", display(value)).strip("-")
    return text or "run"


def bool_value(value: Any, default: bool = False) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return display(value).lower() in {"1", "true", "yes", "y", "on"}


def norm_path_text(value: Any) -> str:
    text = display(value).replace("\\", "/").rstrip("/")
    return text.lower()


def finding(level: str, owner: str, text: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "owner": owner,
        "finding": text,
        "evidence": evidence,
        "action": action,
    }


def load_manifest() -> tuple[Path, dict[str, Any]]:
    manifest_value = os.environ.get("LOCAL_LLM_WINDOWS_RUNTIME_INSTALL_MANIFEST") or (
        sys.argv[1] if len(sys.argv) > 1 else ""
    )
    if manifest_value:
        manifest_path = Path(manifest_value).expanduser().resolve()
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if not isinstance(manifest, dict):
            raise ValueError("Manifest must be a JSON object.")
        return manifest_path, manifest

    root_value = os.environ.get("LOCAL_LLM_WINDOWS_RUNTIME_INSTALL_RUN_ROOT")
    if root_value:
        root = Path(root_value).expanduser().resolve()
        return root / "windows-runtime-install-manifest.json", {"run_root": str(root)}

    raise ValueError(
        "Set LOCAL_LLM_WINDOWS_RUNTIME_INSTALL_MANIFEST or LOCAL_LLM_WINDOWS_RUNTIME_INSTALL_RUN_ROOT."
    )


def parsed_host_port(url: str) -> tuple[str, int]:
    parsed = urllib.parse.urlparse(url)
    host = (parsed.hostname or "").strip().lower().strip("[]")
    if parsed.port:
        return host, parsed.port
    if parsed.scheme == "https":
        return host, 443
    return host, 80


def is_loopback_host(host: str) -> bool:
    clean = host.strip().lower().strip("[]")
    if clean in {"localhost", "::1"}:
        return True
    return clean.startswith("127.")


def is_wildcard_host(host: str) -> bool:
    clean = host.strip().lower().strip("[]")
    return clean in {"", "*", "0.0.0.0", "::"}


def run_command(args: list[str], timeout: int = 10) -> dict[str, Any]:
    started = utc_iso()
    try:
        completed = subprocess.run(
            args,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
        return {
            "ok": completed.returncode == 0,
            "returncode": completed.returncode,
            "stdout": completed.stdout.strip(),
            "stderr": completed.stderr.strip(),
            "started_at": started,
            "completed_at": utc_iso(),
        }
    except Exception as exc:
        return {
            "ok": False,
            "returncode": None,
            "stdout": "",
            "stderr": str(exc),
            "started_at": started,
            "completed_at": utc_iso(),
        }


def powershell_env(scope: str, name: str = "OLLAMA_MODELS") -> str:
    if os.name != "nt":
        return ""
    command = f"[Environment]::GetEnvironmentVariable('{name}', '{scope}')"
    result = run_command(["powershell", "-NoProfile", "-Command", command], timeout=8)
    return display(result.get("stdout"))


def read_only_http_json(url: str, timeout: float = 3.0) -> dict[str, Any]:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            raw = response.read().decode("utf-8", errors="replace")
        try:
            body: Any = json.loads(raw) if raw else None
        except json.JSONDecodeError:
            body = raw
        return {"ok": True, "status": getattr(response, "status", None), "json": body, "error": ""}
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {"ok": False, "status": None, "json": None, "error": str(exc)}


def socket_probe(host: str, port: int, timeout: float = 1.5) -> dict[str, Any]:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return {"ok": True, "host": host, "port": port, "error": ""}
    except OSError as exc:
        return {"ok": False, "host": host, "port": port, "error": str(exc)}


def parse_netstat_line(line: str, target_port: int) -> dict[str, Any] | None:
    parts = line.split()
    if len(parts) < 4:
        return None
    proto = parts[0].upper()
    if not proto.startswith("TCP"):
        return None
    local = parts[1]
    state = parts[3].upper() if len(parts) > 3 else ""
    pid = parts[4] if len(parts) > 4 else ""
    if state != "LISTENING":
        return None
    if local.startswith("[") and "]:" in local:
        host, port_text = local.rsplit("]:", 1)
        host = host.strip("[]")
    elif ":" in local:
        host, port_text = local.rsplit(":", 1)
    else:
        return None
    try:
        port = int(port_text)
    except ValueError:
        return None
    if port != target_port:
        return None
    return {"address": host, "port": port, "pid": pid, "raw": line.strip()}


def netstat_listeners(target_port: int) -> list[dict[str, Any]]:
    command = "netstat"
    if not shutil.which(command):
        return []
    result = run_command([command, "-ano", "-p", "tcp"], timeout=10)
    listeners: list[dict[str, Any]] = []
    for line in display(result.get("stdout")).splitlines():
        parsed = parse_netstat_line(line, target_port)
        if parsed:
            listeners.append(parsed)
    return listeners


def known_paths() -> list[dict[str, Any]]:
    home = Path.home()
    localapp = Path(os.environ.get("LOCALAPPDATA", home / "AppData" / "Local"))
    temp = Path(os.environ.get("TEMP", localapp / "Temp"))
    specs = [
        ("logs", localapp / "Ollama", "app, server, and upgrade logs"),
        ("binaries", localapp / "Programs" / "Ollama", "installed binaries and user PATH target"),
        ("default_model_config", home / ".ollama", "default model and config location"),
        ("temp", temp, "temporary ollama directories"),
    ]
    return [
        {"name": name, "path": str(path), "exists": path.exists(), "use": use}
        for name, path, use in specs
    ]


def collect_probe(manifest: dict[str, Any]) -> dict[str, Any]:
    override = manifest.get("probe_override")
    if isinstance(override, dict):
        probe = dict(override)
        probe["collected_by"] = "probe_override"
        return probe

    native_base = display(manifest.get("native_base_url") or "http://127.0.0.1:11434").rstrip("/")
    host, port = parsed_host_port(native_base)
    command_path = shutil.which(display(manifest.get("command_name") or "ollama")) or ""
    probe: dict[str, Any] = {
        "collected_by": "live",
        "native_base_url": native_base,
        "native_host": host,
        "native_port": port,
        "command_path": command_path,
        "env": {
            "process": os.environ.get("OLLAMA_MODELS", ""),
            "user": powershell_env("User"),
            "machine": powershell_env("Machine"),
        },
        "paths": known_paths(),
        "netstat_listeners": netstat_listeners(port),
    }

    if command_path:
        probe["version"] = run_command([command_path, "--version"], timeout=10)
        probe["list"] = run_command([command_path, "ls"], timeout=20)
    else:
        probe["version"] = {"ok": False, "stdout": "", "stderr": "ollama command not found"}
        probe["list"] = {"ok": False, "stdout": "", "stderr": "ollama command not found"}

    if host and not is_wildcard_host(host):
        probe["listener"] = socket_probe(host, port)
        probe["api_version"] = read_only_http_json(f"{native_base}/api/version")
        probe["api_tags"] = read_only_http_json(f"{native_base}/api/tags")
    else:
        probe["listener"] = {"ok": False, "host": host, "port": port, "error": "wildcard or missing host"}
        probe["api_version"] = {"ok": False, "status": None, "json": None, "error": "wildcard or missing host"}
        probe["api_tags"] = {"ok": False, "status": None, "json": None, "error": "wildcard or missing host"}

    return probe


def installer_source_ok(source: str) -> bool:
    parsed = urllib.parse.urlparse(source)
    host = (parsed.hostname or "").lower()
    return parsed.scheme == "https" and host in {"ollama.com", "www.ollama.com", "docs.ollama.com"}


def evaluate(manifest: dict[str, Any], probe: dict[str, Any]) -> dict[str, Any]:
    findings: list[dict[str, str]] = []
    native_base = display(manifest.get("native_base_url") or probe.get("native_base_url") or "http://127.0.0.1:11434")
    host, port = parsed_host_port(native_base)
    require_loopback = bool_value(manifest.get("require_loopback"), True)
    require_command = bool_value(manifest.get("require_command"), True)
    require_listener = bool_value(manifest.get("require_listener"), True)
    require_api_version = bool_value(manifest.get("require_api_version"), True)
    require_api_tags = bool_value(manifest.get("require_api_tags"), True)

    installer_source = display(manifest.get("installer_source"))
    installer_method = display(manifest.get("installer_method"))
    if not installer_source:
        findings.append(
            finding("hold", "install-source", "`installer_source` is missing.", "installer_source", "Record the official download page or existing-install source before pull.")
        )
    elif not installer_source_ok(installer_source):
        findings.append(
            finding("fail", "install-source", "`installer_source` is not an official Ollama HTTPS source.", installer_source, "Use the official Ollama Windows page or document a reviewed exception.")
        )
    if not installer_method:
        findings.append(
            finding("hold", "install-source", "`installer_method` is missing.", "installer_method", "Record Windows installer, PowerShell installer, or existing install.")
        )

    if is_wildcard_host(host):
        findings.append(
            finding("fail", "security", "`native_base_url` is wildcard or missing.", native_base, "Use `http://127.0.0.1:11434` or `http://localhost:11434` for the first run.")
        )
    elif require_loopback and not is_loopback_host(host):
        findings.append(
            finding("fail", "security", "`native_base_url` is not loopback while loopback is required.", native_base, "Return to loopback before first model pull.")
        )

    for listener in probe.get("netstat_listeners") or []:
        address = display(listener.get("address"))
        if require_loopback and not is_loopback_host(address):
            findings.append(
                finding("fail", "security", "A listener on the Ollama port is not loopback-only.", json.dumps(listener, ensure_ascii=True), "Stop before pull and review endpoint exposure.")
            )

    command_path = display(probe.get("command_path"))
    if require_command and not command_path:
        findings.append(
            finding("hold", "path", "`ollama` command was not found.", "command_path", "Open a new PowerShell or fix the user PATH from the Windows install.")
        )

    version = probe.get("version") or {}
    if bool_value(manifest.get("require_version"), True) and not bool_value(version.get("ok")):
        findings.append(
            finding("hold", "runtime", "`ollama --version` did not succeed.", display(version.get("stderr") or version.get("stdout")), "Fix the CLI install before model pull.")
        )

    model_list = probe.get("list") or {}
    if bool_value(manifest.get("require_model_list"), True) and not bool_value(model_list.get("ok")):
        findings.append(
            finding("hold", "runtime", "`ollama ls` did not succeed.", display(model_list.get("stderr") or model_list.get("stdout")), "Fix CLI/runtime state before model pull.")
        )

    model_store_decision = display(manifest.get("model_store_decision") or manifest.get("expected_model_store_decision"))
    if not model_store_decision:
        findings.append(
            finding("hold", "storage", "`model_store_decision` is missing.", "model_store_decision", "Choose default store or custom `OLLAMA_MODELS` before first pull.")
        )
    elif "hold" in model_store_decision.lower():
        findings.append(
            finding("hold", "storage", "Model-store decision is still hold.", model_store_decision, "Resolve storage before first pull.")
        )

    expected_store = display(manifest.get("expected_ollama_models"))
    env = probe.get("env") or {}
    if expected_store:
        process_store = display(env.get("process"))
        user_store = display(env.get("user"))
        if norm_path_text(process_store) != norm_path_text(expected_store):
            findings.append(
                finding("hold", "storage", "Process `OLLAMA_MODELS` does not match the expected store.", process_store or "<empty>", "Start a new shell after setting the user environment variable.")
            )
        if user_store and norm_path_text(user_store) != norm_path_text(expected_store):
            findings.append(
                finding("hold", "storage", "User `OLLAMA_MODELS` does not match the expected store.", user_store, "Correct the user environment variable before first pull.")
            )

    listener = probe.get("listener") or {}
    if require_listener and not bool_value(listener.get("ok")):
        findings.append(
            finding("hold", "listener", "The planned native base URL is not reachable.", display(listener.get("error")), "Start or reopen Ollama, then rerun the install runner.")
        )

    api_version = probe.get("api_version") or {}
    if require_api_version and not bool_value(api_version.get("ok")):
        findings.append(
            finding("hold", "listener", "`/api/version` did not return JSON.", display(api_version.get("error")), "Fix the runtime listener before model pull.")
        )

    api_tags = probe.get("api_tags") or {}
    if require_api_tags and not bool_value(api_tags.get("ok")):
        findings.append(
            finding("hold", "listener", "`/api/tags` did not return JSON.", display(api_tags.get("error")), "Fix the read-only model-list route before model pull.")
        )

    fail_count = sum(1 for item in findings if item["level"] == "fail")
    hold_count = sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        status = "fail"
        decision = "windows_runtime_install_unsafe"
        next_route = display(manifest.get("fail_next_route") or "LLM/Study/Local LLM Security and Privacy Runbook")
    elif hold_count:
        status = "hold"
        decision = "windows_runtime_install_incomplete"
        next_route = display(manifest.get("hold_next_route") or "LLM/Study/Local LLM Windows Runtime Install Gate")
    else:
        status = "pass"
        decision = "windows_runtime_install_ready"
        next_route = display(manifest.get("pass_next_route") or "LLM/Study/Local LLM First Model Source Recheck Runner")

    return {
        "status": status,
        "decision": decision,
        "next_route": next_route,
        "findings": findings,
        "fail_count": fail_count,
        "hold_count": hold_count,
        "native_host": host,
        "native_port": port,
    }


def md_cell(value: Any) -> str:
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=True, sort_keys=True)
    return display(value).replace("|", "\\|").replace("\n", " ")


def wiki_link(route: str) -> str:
    clean = display(route)
    if not clean:
        return ""
    label = clean.split("/")[-1]
    return "[[" + clean + "|" + label + "]]"


def render_markdown(record: dict[str, Any]) -> str:
    result = record["result"]
    probe = record["probe"]
    env = probe.get("env") or {}
    lines = [
        f"# Local LLM Windows Runtime Install - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Runtime: `{record['runtime']}`",
        f"- Native base URL: `{record['native_base_url']}`",
        f"- Command path: `{display(probe.get('command_path'))}`",
        f"- Process `OLLAMA_MODELS`: `{display(env.get('process'))}`",
        f"- User `OLLAMA_MODELS`: `{display(env.get('user'))}`",
        f"- Next route: {wiki_link(result['next_route'])}",
        "",
        "## Findings",
        "",
    ]
    if result["findings"]:
        for item in result["findings"]:
            lines.append(f"- `{item['level']}` `{item['owner']}`: {item['finding']} -> {item['action']}")
    else:
        lines.append("- No blocking findings. The runtime is ready for source recheck and first model pull planning.")

    lines.extend(
        [
            "",
            "## Probe Summary",
            "",
            "| Probe | Result | Evidence |",
            "|---|---|---|",
            f"| Command | {md_cell(bool(display(probe.get('command_path'))))} | {md_cell(probe.get('command_path'))} |",
            f"| Version | {md_cell((probe.get('version') or {}).get('ok'))} | {md_cell((probe.get('version') or {}).get('stdout') or (probe.get('version') or {}).get('stderr'))} |",
            f"| Model list | {md_cell((probe.get('list') or {}).get('ok'))} | {md_cell((probe.get('list') or {}).get('stdout') or (probe.get('list') or {}).get('stderr'))} |",
            f"| Listener | {md_cell((probe.get('listener') or {}).get('ok'))} | {md_cell(probe.get('listener'))} |",
            f"| `/api/version` | {md_cell((probe.get('api_version') or {}).get('ok'))} | {md_cell((probe.get('api_version') or {}).get('json') or (probe.get('api_version') or {}).get('error'))} |",
            f"| `/api/tags` | {md_cell((probe.get('api_tags') or {}).get('ok'))} | {md_cell((probe.get('api_tags') or {}).get('json') or (probe.get('api_tags') or {}).get('error'))} |",
            "",
            "## Copy Row",
            "",
            "| Field | Value |",
            "|---|---|",
            f"| Runtime install status | `{record['status']}` |",
            f"| Decision | `{record['decision']}` |",
            f"| Evidence JSON | `{record['outputs']['json']}` |",
            f"| Evidence Markdown | `{record['outputs']['markdown']}` |",
            f"| Findings CSV | `{record['outputs']['csv']}` |",
            f"| JSONL ledger | `{record['outputs']['jsonl']}` |",
            f"| Next route | {wiki_link(result['next_route'])} |",
        ]
    )
    return "\n".join(lines) + "\n"


def write_findings_csv(path: Path, findings: list[dict[str, str]]) -> None:
    fieldnames = ["level", "owner", "finding", "evidence", "action"]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for item in findings:
            writer.writerow(item)


def output_root_for(manifest_path: Path, manifest: dict[str, Any]) -> Path:
    raw_output = display(manifest.get("output_root") or os.environ.get("LOCAL_LLM_WINDOWS_RUNTIME_INSTALL_OUTPUT_ROOT"))
    if raw_output:
        output_root = Path(raw_output).expanduser()
    else:
        raw_run_root = display(manifest.get("run_root") or os.environ.get("LOCAL_LLM_WINDOWS_RUNTIME_INSTALL_RUN_ROOT"))
        output_root = Path(raw_run_root).expanduser() / "windows-runtime-install" if raw_run_root else manifest_path.parent / "windows-runtime-install"
    if not output_root.is_absolute():
        output_root = manifest_path.parent / output_root
    return output_root.resolve()


def main() -> int:
    manifest_path, manifest = load_manifest()
    run_id = display(manifest.get("run_id") or f"{utc_stamp()}-{slug(manifest_path.stem)}")
    output_root = output_root_for(manifest_path, manifest)
    output_dir = output_root / slug(run_id)
    output_dir.mkdir(parents=True, exist_ok=True)

    probe = collect_probe(manifest)
    result = evaluate(manifest, probe)
    native_base = display(manifest.get("native_base_url") or probe.get("native_base_url") or "http://127.0.0.1:11434")

    json_path = output_dir / f"{slug(run_id)}-runtime-install.json"
    markdown_path = output_dir / f"{slug(run_id)}-runtime-install.md"
    csv_path = output_dir / f"{slug(run_id)}-runtime-install-findings.csv"
    jsonl_path = output_root / "windows-runtime-install-runs.jsonl"

    record: dict[str, Any] = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "manifest_path": str(manifest_path),
        "status": result["status"],
        "decision": result["decision"],
        "runtime": display(manifest.get("runtime") or "ollama"),
        "native_base_url": native_base,
        "installer_source": display(manifest.get("installer_source")),
        "installer_method": display(manifest.get("installer_method")),
        "model_store_decision": display(manifest.get("model_store_decision") or manifest.get("expected_model_store_decision")),
        "expected_ollama_models": display(manifest.get("expected_ollama_models")),
        "probe": probe,
        "result": result,
        "outputs": {
            "json": str(json_path),
            "markdown": str(markdown_path),
            "csv": str(csv_path),
            "jsonl": str(jsonl_path),
        },
    }

    json_path.write_text(json.dumps(record, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown(record), encoding="utf-8")
    write_findings_csv(csv_path, result["findings"])
    with jsonl_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=True) + "\n")

    print(
        json.dumps(
            {
                "status": record["status"],
                "decision": record["decision"],
                "run_id": run_id,
                "hold_count": result["hold_count"],
                "fail_count": result["fail_count"],
                "output_dir": str(output_dir),
                "next_route": result["next_route"],
            },
            indent=2,
        )
    )
    return 0 if record["status"] == "pass" else 1 if record["status"] == "hold" else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(json.dumps({"status": "error", "decision": "runner_exception", "error": str(exc)}, indent=2), file=sys.stderr)
        raise SystemExit(3)
```

## PowerShell Run

Create the manifest in the first endpoint run folder:

```powershell
$RunRoot = "D:\llm-runs\2026-06-16-first-local-inference"
$Manifest = Join-Path $RunRoot "windows-runtime-install-manifest.json"

@{
  run_id = "first-local-inference-runtime-install"
  run_root = $RunRoot
  runtime = "ollama"
  installer_source = "https://ollama.com/download/windows"
  installer_method = "official Windows installer or existing install"
  model_store_decision = "default user profile store accepted"
  expected_ollama_models = ""
  native_base_url = "http://127.0.0.1:11434"
  require_loopback = $true
  require_command = $true
  require_listener = $true
  require_api_version = $true
  require_api_tags = $true
  pass_next_route = "LLM/Study/Local LLM First Model Source Recheck Runner"
} | ConvertTo-Json -Depth 8 | Set-Content $Manifest -Encoding utf8
```

If you chose a custom model store, set `expected_ollama_models` to the exact path that a new PowerShell should see:

```powershell
expected_ollama_models = "D:\Models\ollama"
```

Run the runner:

```powershell
$env:LOCAL_LLM_WINDOWS_RUNTIME_INSTALL_MANIFEST = $Manifest
python .\windows-runtime-install-runner.py
```

## Result Decisions

| Status / decision | Meaning | Next route |
|---|---|---|
| `pass/windows_runtime_install_ready` | Official source/method are recorded, `ollama` resolves, version/list output works, model-store decision is not hold, loopback listener is reachable, and read-only API routes respond. | [[LLM/Study/Local LLM First Model Source Recheck Runner]] |
| `hold/windows_runtime_install_incomplete` | PATH, version, list, model-store inheritance, listener, or read-only API proof is missing. | [[LLM/Study/Local LLM Windows Runtime Install Gate]] |
| `fail/windows_runtime_install_unsafe` | Installer source is not an official Ollama HTTPS source, planned base URL is non-loopback while loopback is required, or the listener appears wildcard-bound. | [[LLM/Study/Local LLM Security and Privacy Runbook]] |

## Copy Row

| Field | Value |
|---|---|
| Runtime install status | pass / hold / fail |
| Runner manifest |  |
| Evidence JSON |  |
| Evidence Markdown |  |
| Findings CSV |  |
| JSONL ledger |  |
| Command path |  |
| Version output |  |
| `OLLAMA_MODELS` process/user |  |
| Listener status |  |
| `/api/version` status |  |
| `/api/tags` status |  |
| Next route |  |

## Completion Gate

This install runner counts only when:

- [ ] manifest names runtime, installer source, installer method, model-store decision, native base URL, and loopback requirement
- [ ] generated JSON, Markdown, CSV, and JSONL files exist
- [ ] output is copied into [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]] or [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]
- [ ] `pass` routes to current model source recheck and first model pull
- [ ] `hold` names the missing install/PATH/env/listener layer before any pull
- [ ] `fail` routes to endpoint exposure or install-source review before any pull

## References

Internal routes:

- [[LLM/Study/Local LLM Model Store Readiness Snapshot]]
- [[LLM/Study/Local LLM Windows Model Store and Cache Plan]]
- [[LLM/Study/Local LLM Windows Runtime Install Gate]]
- [[LLM/Study/Local LLM First Run Command Plan Runner]]
- [[LLM/Study/Local LLM First Model Source Recheck Runner]]
- [[LLM/Study/Local LLM First Model Pull Gate]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM First Runtime Health Runner]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]

External/current docs checked 2026-06-16:

- [Ollama Windows documentation](https://docs.ollama.com/windows)
- [Ollama Windows download page](https://ollama.com/download/windows)
- [Ollama CLI reference](https://docs.ollama.com/cli)
- [Ollama API introduction](https://docs.ollama.com/api/introduction)
- [Ollama list local models API](https://docs.ollama.com/api/tags)
- [Ollama get version API](https://docs.ollama.com/api-reference/get-version)
- [Ollama authentication documentation](https://docs.ollama.com/api/authentication)
