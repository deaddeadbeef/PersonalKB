---
tags: [study, llm, inference, local-llm, readiness, windows, evidence, runner, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice]
last-verified: 2026-06-16
---

# Local LLM First Run Readiness Runner

> **One-line summary** This no-install runner refreshes the machine evidence needed before the first local LLM install, model pull, or smoke request: runtime commands, GPU visibility, disk, model-store paths, environment variables, common listener ports, and loopback safety.

Use this after [[LLM/Study/Local LLM First Run Readiness Snapshot|Local LLM First Run Readiness Snapshot]] and [[LLM/Study/Local LLM Model Store Readiness Snapshot|Local LLM Model Store Readiness Snapshot]] when either snapshot may be stale. Use it before [[LLM/Study/Local LLM Model Store Bootstrap Runner|Local LLM Model Store Bootstrap Runner]], [[LLM/Study/Local LLM Windows Runtime Install Gate|Local LLM Windows Runtime Install Gate]], [[LLM/Study/Local LLM First Model Pull Gate|Local LLM First Model Pull Gate]], [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]], or [[LLM/Study/Local LLM Windows First-Run Quickstart|Local LLM Windows First-Run Quickstart]] if the current runtime, storage, listener, or GPU state is uncertain.

The runner does **not** install Ollama or LM Studio, create `D:\Models`, set environment variables, download a model, call an endpoint, or generate text. It only observes the machine and writes evidence files.

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| Command inventory | Whether `ollama`, `lms`, `hf`, `python`, and `nvidia-smi` are currently discoverable from the shell. | The runtime is correctly installed or serving a model. |
| Disk and path inventory | Whether the intended run root and model-store paths exist and have enough free space nearby. | The model store will be accepted by the runtime after install. |
| Environment inventory | Whether model/cache variables are set in the process and user environments. | A new shell has inherited changed variables unless rerun there. |
| Listener inventory | Whether common local LLM ports are already listening and whether they are loopback-only. | The listener is healthy or model-backed. |
| GPU inventory | Whether `nvidia-smi` can report NVIDIA GPU state from this boundary. | That vLLM, SGLang, CUDA Python, or a model runtime can use the GPU. |
| Decision card | Whether the next step is safe to install, hold for storage/env setup, or stop for exposure risk. | Endpoint proof, quality proof, or deployment readiness. |

## Runner Manifest

Save a manifest such as `first-run-readiness-manifest.json` before running:

```json
{
  "run_id": "first-local-llm-readiness",
  "run_root": "C:/Users/fpan1/Documents/local-llm-runs/2026-06-16-first-local-llm-readiness",
  "storage_policy": "custom",
  "model_root": "D:/Models",
  "ollama_models_path": "D:/Models/ollama",
  "hf_home": "D:/Models/hf",
  "gguf_dir": "D:/Models/gguf",
  "require_loopback": true,
  "minimum_free_gb": 20
}
```

Use `storage_policy: "default"` only when the default runtime cache path is intentionally accepted. Use `storage_policy: "custom"` when `OLLAMA_MODELS`, Hugging Face cache roots, or GGUF paths should be pinned before large downloads.

## Standard-Library Runner

Save this as `local_llm_first_run_readiness_runner.py` inside a run folder. It uses only Python's standard library.

```python
from __future__ import annotations

import csv
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


COMMON_PORTS = [11434, 1234, 8000, 8001, 8080, 30000]
COMMANDS = ["ollama", "lms", "hf", "python", "nvidia-smi"]
ENV_NAMES = ["OLLAMA_MODELS", "HF_HOME", "HF_HUB_CACHE"]
LOOPBACK = {"127.0.0.1", "::1", "localhost"}
WILDCARD = {"0.0.0.0", "::", "[::]"}


def now_iso() -> str:
    return dt.datetime.now().isoformat(timespec="seconds")


def text(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def as_bool(value: Any, default: bool = False) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def number(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def ps_json(script: str, timeout: int = 15) -> tuple[str, Any]:
    exe = shutil.which("powershell") or shutil.which("pwsh")
    if not exe:
        return "skipped:no_powershell", None
    try:
        proc = subprocess.run(
            [exe, "-NoProfile", "-Command", script],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except Exception as exc:
        return f"error:{type(exc).__name__}:{exc}", None
    output = proc.stdout.strip()
    if proc.returncode != 0:
        return f"error:returncode_{proc.returncode}:{proc.stderr.strip()}", None
    if not output:
        return "ok", None
    try:
        return "ok", json.loads(output)
    except json.JSONDecodeError:
        return "error:json_decode", output


def command_inventory() -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for command in COMMANDS:
        path = shutil.which(command)
        result[command] = {"available": bool(path), "path": path or ""}
    return result


def env_inventory() -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for name in ENV_NAMES:
        result[name] = {"process": os.environ.get(name, ""), "user": ""}
    if os.name == "nt":
        status, data = ps_json(
            "[pscustomobject]@{"
            "OLLAMA_MODELS=[Environment]::GetEnvironmentVariable('OLLAMA_MODELS','User');"
            "HF_HOME=[Environment]::GetEnvironmentVariable('HF_HOME','User');"
            "HF_HUB_CACHE=[Environment]::GetEnvironmentVariable('HF_HUB_CACHE','User')"
            "} | ConvertTo-Json -Compress"
        )
        if status == "ok" and isinstance(data, dict):
            for name in ENV_NAMES:
                result[name]["user"] = text(data.get(name))
        else:
            result["_user_env_status"] = {"process": status, "user": ""}
    return result


def disk_inventory(paths: list[str]) -> list[dict[str, Any]]:
    roots: list[str] = []
    for raw in paths:
        anchor = Path(raw).anchor
        if anchor and anchor not in roots:
            roots.append(anchor)
    for fallback in ["C:\\", "D:\\"] if os.name == "nt" else ["/"]:
        if fallback not in roots:
            roots.append(fallback)

    rows: list[dict[str, Any]] = []
    for root in roots:
        try:
            usage = shutil.disk_usage(root)
        except Exception as exc:
            rows.append({"root": root, "available": False, "error": str(exc)})
            continue
        rows.append(
            {
                "root": root,
                "available": True,
                "free_gb": round(usage.free / (1024**3), 1),
                "total_gb": round(usage.total / (1024**3), 1),
            }
        )
    return rows


def path_inventory(paths: list[str]) -> list[dict[str, Any]]:
    rows = []
    for raw in paths:
        path = Path(raw)
        rows.append({"path": str(path), "exists": path.exists(), "is_dir": path.is_dir()})
    return rows


def listener_inventory() -> tuple[str, list[dict[str, Any]]]:
    port_list = ",".join(str(port) for port in COMMON_PORTS)
    script = (
        "Get-NetTCPConnection -State Listen -ErrorAction SilentlyContinue | "
        f"Where-Object {{ $_.LocalPort -in {port_list} }} | "
        "Select-Object LocalAddress,LocalPort,OwningProcess | ConvertTo-Json -Compress"
    )
    status, data = ps_json(script)
    if status != "ok":
        return status, []
    if data is None:
        return "ok", []
    if isinstance(data, dict):
        data = [data]
    if not isinstance(data, list):
        return "error:unexpected_listener_shape", []
    rows = []
    for item in data:
        if isinstance(item, dict):
            rows.append(
                {
                    "local_address": text(item.get("LocalAddress")),
                    "local_port": item.get("LocalPort"),
                    "owning_process": item.get("OwningProcess"),
                }
            )
    return "ok", rows


def gpu_inventory(commands: dict[str, dict[str, Any]]) -> dict[str, Any]:
    nvidia = commands.get("nvidia-smi", {})
    if not nvidia.get("available"):
        return {"available": False, "rows": [], "status": "nvidia-smi not found"}
    try:
        proc = subprocess.run(
            [
                text(nvidia.get("path")) or "nvidia-smi",
                "--query-gpu=name,memory.total,driver_version",
                "--format=csv,noheader,nounits",
            ],
            capture_output=True,
            text=True,
            timeout=15,
        )
    except Exception as exc:
        return {"available": True, "rows": [], "status": f"error:{type(exc).__name__}:{exc}"}
    if proc.returncode != 0:
        return {"available": True, "rows": [], "status": f"error:returncode_{proc.returncode}:{proc.stderr.strip()}"}
    rows = []
    for line in proc.stdout.splitlines():
        parts = [part.strip() for part in line.split(",")]
        if len(parts) >= 3:
            rows.append({"name": parts[0], "memory_total_mib": parts[1], "driver_version": parts[2]})
    return {"available": True, "rows": rows, "status": "ok"}


def manifest_paths(manifest: dict[str, Any]) -> list[str]:
    paths = [
        text(manifest.get("run_root")),
        text(manifest.get("model_root")),
        text(manifest.get("ollama_models_path")),
        text(manifest.get("hf_home")),
        text(manifest.get("gguf_dir")),
    ]
    return [path for path in paths if path]


def collect(manifest: dict[str, Any]) -> dict[str, Any]:
    paths = manifest_paths(manifest)
    commands = command_inventory()
    listener_status, listeners = listener_inventory()
    scan = {
        "run_id": text(manifest.get("run_id")) or "local-llm-first-run-readiness",
        "generated_at": now_iso(),
        "manifest": manifest,
        "commands": commands,
        "environment": env_inventory(),
        "disks": disk_inventory(paths),
        "paths": path_inventory(paths),
        "listener_status": listener_status,
        "listeners": listeners,
        "gpu": gpu_inventory(commands),
    }
    scan["decision"] = classify(scan)
    return scan


def finding(level: str, owner: str, message: str, evidence: str, action: str) -> dict[str, str]:
    return {"level": level, "owner": owner, "finding": message, "evidence": evidence, "action": action}


def classify(scan: dict[str, Any]) -> dict[str, Any]:
    manifest = scan.get("manifest", {})
    findings: list[dict[str, str]] = []
    require_loopback = as_bool(manifest.get("require_loopback"), True)
    storage_policy = text(manifest.get("storage_policy") or "custom").lower()
    minimum_free_gb = number(manifest.get("minimum_free_gb"), 20)

    if not scan.get("paths"):
        findings.append(finding("hold", "manifest", "No run or model paths were provided.", "manifest", "Add run_root and storage paths."))

    for row in scan.get("paths", []):
        path = row.get("path", "")
        if path == text(manifest.get("run_root")) and not row.get("exists"):
            findings.append(finding("hold", "run_root", "Run root does not exist yet.", path, "Create the run folder before install or model pull."))
        if storage_policy == "custom" and path != text(manifest.get("run_root")) and not row.get("exists"):
            findings.append(finding("hold", "model_store", "Custom model-store path does not exist yet.", path, "Create the model-store directories before large downloads."))

    for disk in scan.get("disks", []):
        if disk.get("available") and number(disk.get("free_gb")) < minimum_free_gb:
            findings.append(finding("hold", "disk", "Disk free space is below the configured threshold.", f"{disk.get('root')} free_gb={disk.get('free_gb')}", "Free space or choose a different model root."))

    if storage_policy == "custom":
        wanted_ollama = text(manifest.get("ollama_models_path"))
        env = scan.get("environment", {}).get("OLLAMA_MODELS", {})
        current = text(env.get("process") or env.get("user"))
        if wanted_ollama and current and current.lower() != wanted_ollama.lower():
            findings.append(finding("hold", "environment", "OLLAMA_MODELS is set to a different path than the manifest.", current, "Align the variable or update the manifest."))
        elif wanted_ollama and not current:
            findings.append(finding("hold", "environment", "OLLAMA_MODELS is not set for the custom store decision.", wanted_ollama, "Set and verify OLLAMA_MODELS from a new shell before first pull."))

    if scan.get("listener_status") != "ok":
        findings.append(finding("hold", "listeners", "Listener scan did not complete cleanly.", text(scan.get("listener_status")), "Rerun from Windows PowerShell or record the blocker."))
    elif require_loopback:
        for row in scan.get("listeners", []):
            address = text(row.get("local_address"))
            if address in WILDCARD or (address and address not in LOOPBACK):
                findings.append(finding("fail", "security_boundary", "A common local LLM port is listening beyond loopback.", f"{address}:{row.get('local_port')}", "Stop or secure the listener before installing, pulling, or sending prompts."))

    runtime_available = any(scan.get("commands", {}).get(name, {}).get("available") for name in ("ollama", "lms"))
    if not runtime_available:
        findings.append(finding("info", "runtime", "No first-run runtime command is currently available.", "ollama/lms not found", "Proceed to the runtime install gate after run-root and storage holds are cleared."))

    if not scan.get("gpu", {}).get("rows"):
        findings.append(finding("info", "gpu", "No NVIDIA GPU row was captured.", text(scan.get("gpu", {}).get("status")), "Use CPU-only expectations or fix GPU visibility before GPU-serving claims."))

    if any(item["level"] == "fail" for item in findings):
        status, reason = "fail", "readiness_blocked"
    elif any(item["level"] == "hold" for item in findings):
        status, reason = "hold", "readiness_incomplete"
    else:
        status, reason = "pass", "ready_for_first_runtime_step"
    return {"status": status, "reason": reason, "findings": findings}


def output_paths(manifest: dict[str, Any], scan: dict[str, Any]) -> dict[str, Path]:
    root = Path(text(manifest.get("output_root") or manifest.get("run_root") or ".")).expanduser()
    run_id = scan["run_id"]
    return {
        "json": root / f"{run_id}-readiness.json",
        "csv": root / f"{run_id}-readiness-findings.csv",
        "md": root / f"{run_id}-readiness.md",
        "jsonl": root / "local-llm-first-run-readiness-runs.jsonl",
    }


def md_cell(value: Any) -> str:
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=True)
    return text(value).replace("|", "\\|").replace("\n", " ")


def write_outputs(manifest: dict[str, Any], scan: dict[str, Any]) -> dict[str, str]:
    paths = output_paths(manifest, scan)
    for path in paths.values():
        path.parent.mkdir(parents=True, exist_ok=True)
    paths["json"].write_text(json.dumps(scan, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    fields = ["level", "owner", "finding", "evidence", "action"]
    with paths["csv"].open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in scan["decision"]["findings"]:
            writer.writerow({field: row.get(field, "") for field in fields})
    lines = [
        f"# Local LLM First Run Readiness - {scan['run_id']}",
        "",
        f"- Decision: `{scan['decision']['status']}` / `{scan['decision']['reason']}`",
        f"- Generated: {scan['generated_at']}",
        "",
        "## Findings",
        "",
        "| Level | Owner | Finding | Evidence | Action |",
        "|---|---|---|---|---|",
    ]
    if scan["decision"]["findings"]:
        for row in scan["decision"]["findings"]:
            lines.append(f"| {md_cell(row['level'])} | {md_cell(row['owner'])} | {md_cell(row['finding'])} | {md_cell(row['evidence'])} | {md_cell(row['action'])} |")
    else:
        lines.append("| pass | readiness | No blocking findings. | scan | Continue to runtime install, pull, health, or smoke gate as appropriate. |")
    paths["md"].write_text("\n".join(lines) + "\n", encoding="utf-8")
    with paths["jsonl"].open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(scan, ensure_ascii=True) + "\n")
    return {key: str(path) for key, path in paths.items()}


def classify_fixture(scan: dict[str, Any]) -> str:
    return classify(scan)["status"]


def run_self_tests() -> None:
    complete = {
        "manifest": {"run_root": "C:/runs/a", "storage_policy": "custom", "ollama_models_path": "D:/Models/ollama", "minimum_free_gb": 20, "require_loopback": True},
        "paths": [
            {"path": "C:/runs/a", "exists": True},
            {"path": "D:/Models/ollama", "exists": True},
        ],
        "disks": [{"root": "D:/", "available": True, "free_gb": 200}],
        "environment": {"OLLAMA_MODELS": {"process": "D:/Models/ollama", "user": ""}},
        "listener_status": "ok",
        "listeners": [],
        "commands": {"ollama": {"available": False}, "lms": {"available": False}},
        "gpu": {"rows": [{"name": "GPU"}], "status": "ok"},
    }
    cases = [
        ("complete preinstall readiness", complete, "pass"),
        ("missing run root", {**complete, "paths": [{"path": "C:/runs/a", "exists": False}, {"path": "D:/Models/ollama", "exists": True}]}, "hold"),
        ("wildcard listener", {**complete, "listeners": [{"local_address": "0.0.0.0", "local_port": 11434}]}, "fail"),
        ("env mismatch", {**complete, "environment": {"OLLAMA_MODELS": {"process": "C:/Users/fpan1/.ollama/models", "user": ""}}}, "hold"),
    ]
    failures = []
    for name, scan, expected in cases:
        got = classify_fixture(scan)
        if got != expected:
            failures.append({"case": name, "expected": expected, "got": got})
    if failures:
        print(json.dumps({"self_test": "fail", "failures": failures}, indent=2))
        raise SystemExit(1)
    print(json.dumps({"self_test": "pass", "cases": len(cases)}, indent=2))


def load_manifest(argv: list[str]) -> dict[str, Any]:
    manifest_path = os.environ.get("LOCAL_LLM_FIRST_RUN_READINESS_MANIFEST") or (argv[1] if len(argv) > 1 else "")
    if not manifest_path:
        raise SystemExit("Set LOCAL_LLM_FIRST_RUN_READINESS_MANIFEST or pass a manifest JSON path.")
    with Path(manifest_path).open("r", encoding="utf-8") as handle:
        manifest = json.load(handle)
    if not isinstance(manifest, dict):
        raise SystemExit("Manifest root must be a JSON object.")
    return manifest


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        run_self_tests()
        return 0
    manifest = load_manifest(argv)
    scan = collect(manifest)
    scan["outputs"] = write_outputs(manifest, scan)
    print(json.dumps(scan, indent=2, ensure_ascii=True))
    status = scan["decision"]["status"]
    return 0 if status == "pass" else 2 if status == "hold" else 3


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
```

## PowerShell Run

```powershell
$RunRoot = Join-Path $HOME ("Documents\local-llm-runs\" + (Get-Date -Format "yyyy-MM-dd-HHmm") + "-first-readiness")
New-Item -ItemType Directory -Force -Path $RunRoot | Out-Null

$Manifest = @{
  run_id = "first-local-llm-readiness"
  run_root = $RunRoot
  storage_policy = "custom"
  model_root = "D:/Models"
  ollama_models_path = "D:/Models/ollama"
  hf_home = "D:/Models/hf"
  gguf_dir = "D:/Models/gguf"
  require_loopback = $true
  minimum_free_gb = 20
}

$ManifestPath = Join-Path $RunRoot "first-run-readiness-manifest.json"
$Manifest | ConvertTo-Json -Depth 5 | Set-Content -Encoding UTF8 $ManifestPath
python .\local_llm_first_run_readiness_runner.py $ManifestPath
```

Expected current outcome before the first setup pass: `hold/readiness_incomplete` if the run folder, `D:\Models` paths, or `OLLAMA_MODELS` are not ready yet; `pass/ready_for_first_runtime_step` only after the pre-install evidence boundary is ready.

## Decision Meanings

| Decision | Meaning | Next route |
|---|---|---|
| `pass/ready_for_first_runtime_step` | Readiness evidence is fresh, no common LLM listener is exposed beyond loopback, and required run/store paths and env choices are ready for the next first-run step. | [[LLM/Study/Local LLM Windows Runtime Install Gate]] or [[LLM/Study/Local LLM First Model Pull Gate]] depending on runtime state. |
| `hold/readiness_incomplete` | The machine state is observable but a required run root, model-store path, env variable, disk threshold, listener scan, or path choice is incomplete. | Use [[LLM/Study/Local LLM Model Store Bootstrap Runner]] for storage/env holds, or fix the named hold before install, pull, or smoke request. |
| `fail/readiness_blocked` | A common local LLM listener is exposed beyond loopback or another safety condition contradicts the first-run boundary. | Stop and route to [[LLM/Study/Local LLM Security and Privacy Runbook]] before prompts or model pulls. |

## Completion Gate

This runner has served its purpose when:

- [ ] a dated manifest exists
- [ ] command, environment, disk, path, listener, and GPU inventories are saved
- [ ] the decision is `pass`, `hold`, or `fail` with specific findings
- [ ] any non-loopback listener is resolved before prompts or model pulls
- [ ] the output is linked from [[LLM/Study/Local LLM First Run Readiness Snapshot|Local LLM First Run Readiness Snapshot]], [[LLM/Study/Local LLM Model Store Readiness Snapshot|Local LLM Model Store Readiness Snapshot]], or a dated run folder
- [ ] the next action points to runtime install, storage setup, model pull, endpoint smoke, or security remediation

## References

Internal routes:

- [[LLM/Study/Local LLM First Run Readiness Snapshot]]
- [[LLM/Study/Local LLM Model Store Readiness Snapshot]]
- [[LLM/Study/Local LLM Windows Model Store and Cache Plan]]
- [[LLM/Study/Local LLM Model Store Bootstrap Runner]]
- [[LLM/Study/Local LLM Windows Runtime Install Gate]]
- [[LLM/Study/Local LLM First Model Candidate Ladder]]
- [[LLM/Study/Local LLM First Model Pull Gate]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM Windows First-Run Quickstart]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
