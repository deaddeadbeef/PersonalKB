---
tags: [study, llm, local-llm, operations, lifecycle, upgrade, rollback, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice, deep-dive]
last-verified: 2026-06-15
---

# Local LLM Service Lifecycle and Upgrade Runner

> **One-line summary** Turn a local LLM restart, upgrade, rollback, model-cache move, or UI change into a checked evidence package before anything is changed.

Use this after [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook|Local LLM Service Lifecycle and Upgrade Runbook]] defines the manual change gate. Use it before changing a daily-use local service, Docker/Compose stack, Open WebUI front end, model cache, runtime package, client contract, or startup wrapper. Use [[LLM/Study/Local LLM Security and Privacy Runner|Local LLM Security and Privacy Runner]] before and after changes that affect endpoint exposure, auth, config/logs, RAG corpora, tool roots, UI storage, or export boundaries.

This runner does not perform the upgrade. It validates a lifecycle manifest, checks that baseline or post-change artifacts exist, captures read-only route/version/model-list evidence when configured, records safe built-in version commands when available, and writes JSON, CSV, Markdown, and JSONL decision artifacts.

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| Lifecycle manifest | The change has a named owner, reason, workload, current state, target state, startup mode, backup, rollback, abort rule, and validation suite. | That the service has already survived the change. |
| Artifact inventory | Referenced observability, API contract, benchmark, quality, security, backup, and config files exist and have stable size/hash metadata. | That their internal contents are semantically correct. |
| Read-only route state | The configured OpenAI-compatible route and optional Ollama native route are reachable during this phase. | That generation quality is acceptable; use quality and benchmark artifacts. |
| Built-in version commands | Available local tools such as `ollama`, `lms`, `docker`, or `python` are pinned into the run folder. | That arbitrary startup scripts are safe to execute. |
| Decision card | The change is ready, incomplete, risky, or needs rollback without relying on memory. | Recovery from an unrecorded hidden dependency. |

Academic bridge: lifecycle evidence is the operational layer over serving mechanisms. KV cache, batching, prompt cache, quantization, and speculative decoding only matter for a maintained local system if the exact runtime, model artifact, cache paths, startup boundary, and rollback route survive restarts and upgrades.

## Manifest Contract

Save a manifest such as `lifecycle-manifest.json` next to the runner. Use `phase` as `before`, `after`, or `rollback`.

```json
{
  "change_id": "2026-06-15-ollama-version-freeze",
  "phase": "before",
  "runtime": "ollama",
  "reason": "version pin before model pull",
  "workload": "private local assistant baseline",
  "owner": "local",
  "current": {
    "runtime_version": "ollama 0.x",
    "model_id": "qwen3",
    "model_revision_or_digest": "tag or digest",
    "model_cache_path": "D:\\Models\\Ollama",
    "quantization": "runtime tag"
  },
  "target": {
    "runtime_version": "same",
    "model_id": "qwen3",
    "model_revision_or_digest": "same"
  },
  "startup": {
    "mode": "manual shell",
    "command": "ollama serve",
    "endpoint": "http://127.0.0.1:11434/v1",
    "native_api": "http://127.0.0.1:11434/api",
    "bind_address": "127.0.0.1",
    "port": 11434,
    "env_vars": ["OLLAMA_MODELS", "OLLAMA_HOST"],
    "working_directory": "C:\\Users\\fpan1"
  },
  "baseline_artifacts": {
    "observability": "D:\\LLM-Runs\\before\\observability-results.json",
    "api_contract": "D:\\LLM-Runs\\before\\contract-results.json",
    "benchmark": "D:\\LLM-Runs\\before\\benchmark-row.json",
    "quality": "D:\\LLM-Runs\\before\\quality-results.json",
    "security": "D:\\LLM-Runs\\before\\security-row.md"
  },
  "backup": {
    "paths": ["D:\\LLM-Backups\\ollama-env-before.json"],
    "restore_method": "restore env vars, confirm model cache path, restart service"
  },
  "rollback": {
    "target": "previous runtime, model id, env vars, model cache path, and port",
    "steps": [
      "stop service",
      "restore previous env/config",
      "start service",
      "run observability, API contract, benchmark, and quality checks"
    ]
  },
  "abort_conditions": [
    "expected model disappears",
    "route is unreachable",
    "benchmark or quality artifact is missing"
  ],
  "post_change_validation": [
    "observability",
    "smoke",
    "api_contract",
    "benchmark",
    "quality",
    "security"
  ]
}
```

## Standard-Library Runner

Save this as `service-lifecycle-upgrade-runner.py` inside the run folder. It uses only Python's standard library.

```python
import csv
import hashlib
import json
import os
import platform
import re
import shutil
import socket
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path


SECRET_PATTERNS = [
    re.compile(r"(?i)(authorization:\s*bearer\s+)[A-Za-z0-9._\-+/=]+"),
    re.compile(r"(?i)(api[_-]?key['\"\s:=]+)[A-Za-z0-9._\-+/=]+"),
    re.compile(r"(?i)(token['\"\s:=]+)[A-Za-z0-9._\-+/=]+"),
    re.compile(r"(?i)(password['\"\s:=]+)\S+"),
    re.compile(r"(?i)(secret[_-]?key['\"\s:=]+)[A-Za-z0-9._\-+/=]+"),
]


def env_bool(name, default):
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() not in {"0", "false", "no", "off"}


def as_int(value, default):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def append_jsonl(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(data, ensure_ascii=True) + "\n")


def md_cell(value):
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=True)
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def redact(text):
    redacted = text
    for pattern in SECRET_PATTERNS:
        redacted = pattern.sub(r"\1<redacted>", redacted)
    return redacted


def join_url(base_url, route):
    return f"{base_url.rstrip('/')}/{route.lstrip('/')}"


def auth_headers():
    headers = {"Accept": "application/json, text/plain, */*"}
    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"
    return headers


def parse_json(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_blank(value):
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip()
    if isinstance(value, (list, tuple, dict)):
        return len(value) == 0
    return False


def get_path(data, dotted):
    current = data
    for part in dotted.split("."):
        if not isinstance(current, dict) or part not in current:
            return None
        current = current[part]
    return current


def load_manifest(path):
    if not path:
        return None, "missing_manifest_path"
    candidate = Path(path).expanduser().resolve()
    if not candidate.exists():
        return None, f"manifest_not_found: {candidate}"
    try:
        data = json.loads(candidate.read_text(encoding="utf-8"))
    except Exception as exc:
        return None, f"manifest_parse_error: {type(exc).__name__}: {exc}"
    if not isinstance(data, dict):
        return None, "manifest_must_be_json_object"
    data["_manifest_path"] = str(candidate)
    return data, ""


def write_manifest_template(path):
    template = {
        "change_id": "2026-06-15-local-llm-change",
        "phase": "before",
        "runtime": "ollama",
        "reason": "version pin before change",
        "workload": "private local assistant baseline",
        "owner": "local",
        "current": {
            "runtime_version": "ollama 0.x",
            "model_id": "qwen3",
            "model_revision_or_digest": "tag or digest",
            "model_cache_path": "D:\\Models\\Ollama",
            "quantization": "runtime tag"
        },
        "target": {
            "runtime_version": "same",
            "model_id": "qwen3",
            "model_revision_or_digest": "same"
        },
        "startup": {
            "mode": "manual shell",
            "command": "ollama serve",
            "endpoint": "http://127.0.0.1:11434/v1",
            "native_api": "http://127.0.0.1:11434/api",
            "bind_address": "127.0.0.1",
            "port": 11434,
            "env_vars": ["OLLAMA_MODELS", "OLLAMA_HOST"],
            "working_directory": "C:\\Users\\fpan1"
        },
        "baseline_artifacts": {
            "observability": "D:\\LLM-Runs\\before\\observability-results.json",
            "api_contract": "D:\\LLM-Runs\\before\\contract-results.json",
            "benchmark": "D:\\LLM-Runs\\before\\benchmark-row.json",
            "quality": "D:\\LLM-Runs\\before\\quality-results.json",
            "security": "D:\\LLM-Runs\\before\\security-row.md"
        },
        "backup": {
            "paths": ["D:\\LLM-Backups\\ollama-env-before.json"],
            "restore_method": "restore env vars, confirm model cache path, restart service"
        },
        "rollback": {
            "target": "previous runtime, model id, env vars, model cache path, and port",
            "steps": [
                "stop service",
                "restore previous env/config",
                "start service",
                "run observability, API contract, benchmark, and quality checks"
            ]
        },
        "abort_conditions": [
            "expected model disappears",
            "route is unreachable",
            "benchmark or quality artifact is missing"
        ],
        "post_change_validation": [
            "observability",
            "smoke",
            "api_contract",
            "benchmark",
            "quality",
            "security"
        ]
    }
    write_json(path, template)


def collect_file_refs(value, prefix="manifest"):
    refs = []
    if isinstance(value, dict):
        for key, item in value.items():
            child_prefix = f"{prefix}.{key}"
            lowered = str(key).lower()
            if isinstance(item, str) and (
                lowered.endswith(("path", "paths", "file", "json", "csv", "md", "txt", "folder", "dir"))
                or "artifact" in lowered
                or prefix.endswith(("artifacts", "paths", "config_paths"))
            ):
                refs.append((child_prefix, item))
            else:
                refs.extend(collect_file_refs(item, child_prefix))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            refs.extend(collect_file_refs(item, f"{prefix}[{index}]"))
    elif isinstance(value, str) and (
        prefix.endswith(("path", "paths", "file", "json", "csv", "md", "txt", "folder", "dir"))
        or ".paths[" in prefix
        or ".config_paths[" in prefix
    ):
        refs.append((prefix, value))
    return refs


def file_inventory(manifest):
    refs = []
    for section in ("baseline_artifacts", "after_artifacts", "rollback_artifacts", "backup", "config_paths"):
        if section in manifest:
            refs.extend(collect_file_refs(manifest[section], section))
    rows = []
    seen = set()
    for label, raw in refs:
        if not isinstance(raw, str) or not raw.strip():
            continue
        if raw.startswith("http://") or raw.startswith("https://"):
            continue
        path = Path(raw).expanduser()
        key = (label, str(path))
        if key in seen:
            continue
        seen.add(key)
        row = {
            "label": label,
            "path": str(path),
            "exists": path.exists(),
            "is_file": path.is_file() if path.exists() else False,
            "is_dir": path.is_dir() if path.exists() else False,
            "size_bytes": None,
            "sha256": "",
            "note": "",
        }
        try:
            if path.is_file():
                row["size_bytes"] = path.stat().st_size
                row["sha256"] = sha256_file(path)
            elif path.is_dir():
                row["note"] = "directory"
        except Exception as exc:
            row["note"] = f"{type(exc).__name__}: {exc}"
        rows.append(row)
    return rows


def write_inventory_csv(path, rows):
    fields = ["label", "path", "exists", "is_file", "is_dir", "size_bytes", "sha256", "note"]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def fetch_source(source_id, source_type, url, expect_json=False):
    started = time.perf_counter()
    record = {
        "source_id": source_id,
        "source_type": source_type,
        "url": url,
        "status": "error",
        "ok": False,
        "elapsed_ms": None,
        "bytes": 0,
        "result_path": "",
        "note": "",
    }
    request = urllib.request.Request(url, headers=auth_headers(), method="GET")
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            raw = response.read()
            status_code = getattr(response, "status", 200)
        text = raw.decode("utf-8", errors="replace")
        parsed = parse_json(text)
        extension = "json" if parsed is not None else "txt"
        result_path = OUT_DIR / f"{RUN_ID}-{source_id}.{extension}"
        if parsed is not None:
            write_json(result_path, parsed)
        else:
            write_text(result_path, text)
        record.update(
            {
                "status": str(status_code),
                "ok": 200 <= int(status_code) < 400 and (parsed is not None or not expect_json),
                "elapsed_ms": round((time.perf_counter() - started) * 1000, 3),
                "bytes": len(raw),
                "result_path": str(result_path),
                "note": "json" if parsed is not None else "text",
                "parsed": parsed,
            }
        )
    except urllib.error.HTTPError as exc:
        raw = exc.read()
        text = redact(raw.decode("utf-8", errors="replace"))
        result_path = OUT_DIR / f"{RUN_ID}-{source_id}-error.txt"
        write_text(result_path, text)
        record.update(
            {
                "status": f"HTTP {exc.code}",
                "elapsed_ms": round((time.perf_counter() - started) * 1000, 3),
                "bytes": len(raw),
                "result_path": str(result_path),
                "note": text[:200].replace("\n", " "),
            }
        )
    except Exception as exc:
        record.update(
            {
                "elapsed_ms": round((time.perf_counter() - started) * 1000, 3),
                "note": f"{type(exc).__name__}: {exc}",
            }
        )
    return record


def run_command(source_id, command):
    exe = shutil.which(command[0])
    record = {
        "source_id": source_id,
        "source_type": "command",
        "command": command,
        "status": "unavailable",
        "ok": False,
        "elapsed_ms": None,
        "bytes": 0,
        "result_path": "",
        "note": f"{command[0]} not found",
    }
    if not exe:
        return record
    started = time.perf_counter()
    try:
        completed = subprocess.run(command, capture_output=True, text=True, timeout=COMMAND_TIMEOUT_SECONDS, check=False)
        text = redact(completed.stdout + completed.stderr)
        result_path = OUT_DIR / f"{RUN_ID}-{source_id}.txt"
        write_text(result_path, text)
        record.update(
            {
                "status": f"exit {completed.returncode}",
                "ok": completed.returncode == 0,
                "elapsed_ms": round((time.perf_counter() - started) * 1000, 3),
                "bytes": len(text.encode("utf-8")),
                "result_path": str(result_path),
                "note": text[:200].replace("\n", " ") if completed.returncode != 0 else "captured",
            }
        )
    except Exception as exc:
        record.update(
            {
                "elapsed_ms": round((time.perf_counter() - started) * 1000, 3),
                "note": f"{type(exc).__name__}: {exc}",
            }
        )
    return record


def built_in_commands(runtime):
    normalized = runtime.lower().replace(" ", "")
    commands = []
    if "ollama" in normalized:
        commands.append(("ollama_version", ["ollama", "--version"]))
    if "lmstudio" in normalized or normalized == "lms":
        commands.extend(
            [
                ("lms_version", ["lms", "--version"]),
                ("lms_server_status", ["lms", "server", "status", "--json", "--quiet"]),
                ("lms_ps", ["lms", "ps", "--json"]),
            ]
        )
    if any(name in normalized for name in ("docker", "openwebui", "vllm", "sglang")):
        commands.append(("docker_ps", ["docker", "ps", "--format", "{{.Image}}\t{{.Names}}\t{{.Ports}}"]))
    commands.append(("python_version", [shutil.which("python") or "python", "--version"]))
    return commands


def openai_model_ids(parsed):
    ids = []
    if isinstance(parsed, dict):
        data = parsed.get("data")
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict) and item.get("id"):
                    ids.append(str(item["id"]))
    return ids


def ollama_model_ids(parsed):
    ids = []
    if isinstance(parsed, dict):
        models = parsed.get("models")
        if isinstance(models, list):
            for item in models:
                if isinstance(item, dict):
                    for key in ("name", "model", "id"):
                        if item.get(key):
                            ids.append(str(item[key]))
    return ids


def required_fields_for_phase(phase):
    base = [
        "change_id",
        "phase",
        "runtime",
        "reason",
        "workload",
        "owner",
        "current.runtime_version",
        "current.model_id",
        "startup.mode",
        "startup.command",
        "startup.endpoint",
        "backup.restore_method",
        "rollback.target",
        "rollback.steps",
        "abort_conditions",
        "post_change_validation",
    ]
    if phase == "after":
        return base + [
            "target.runtime_version",
            "target.model_id",
            "after_artifacts.observability",
            "after_artifacts.api_contract",
            "after_artifacts.benchmark",
            "after_artifacts.quality",
            "decision",
        ]
    if phase == "rollback":
        return base + [
            "rollback.executed_steps",
            "rollback.validation",
            "rollback_artifacts.observability",
            "rollback_artifacts.api_contract",
            "rollback_artifacts.benchmark",
            "decision",
        ]
    return base + [
        "baseline_artifacts.observability",
        "baseline_artifacts.api_contract",
        "baseline_artifacts.benchmark",
        "baseline_artifacts.quality",
    ]


def missing_required_fields(manifest, phase):
    missing = []
    for field in required_fields_for_phase(phase):
        if is_blank(get_path(manifest, field)):
            missing.append(field)
    return missing


def classify(manifest, manifest_error, sources, inventory, model_ids):
    if manifest_error:
        return {
            "status": "error",
            "decision": "manifest_missing_or_invalid",
            "reason": manifest_error,
            "next_route": "Create a lifecycle manifest from the template before changing the service.",
        }

    phase = str(manifest.get("phase", "before")).lower()
    if phase not in {"before", "after", "rollback"}:
        return {
            "status": "error",
            "decision": "unknown_phase",
            "reason": f"Unsupported phase `{phase}`.",
            "next_route": "Set phase to before, after, or rollback.",
        }

    missing_fields = missing_required_fields(manifest, phase)
    missing_files = [row for row in inventory if not row["exists"]]
    route_sources = [source for source in sources if source["source_type"] in {"openai_models", "ollama_version", "ollama_tags", "ollama_ps"}]
    route_failures = [source for source in route_sources if not source["ok"]]
    expected_model = EXPECTED_MODEL or str(get_path(manifest, "current.model_id") or "")
    expected_present = None
    if expected_model and model_ids:
        expected_present = expected_model in model_ids
    if expected_model and model_ids and not expected_present:
        return {
            "status": "hold",
            "decision": "expected_model_missing",
            "reason": f"Expected model `{expected_model}` was not visible in the captured route or model-list sources.",
            "next_route": "Check model id, route, loaded state, cache path, or first runtime health snapshot.",
            "missing_fields": missing_fields,
            "missing_files": [row["path"] for row in missing_files],
            "route_failures": [source["source_id"] for source in route_failures],
            "expected_model_present": False,
        }
    if missing_fields:
        return {
            "status": "hold",
            "decision": "lifecycle_manifest_incomplete",
            "reason": "Required lifecycle manifest fields are missing.",
            "next_route": "Fill the missing fields before changing the service.",
            "missing_fields": missing_fields,
            "missing_files": [row["path"] for row in missing_files],
            "route_failures": [source["source_id"] for source in route_failures],
            "expected_model_present": expected_present,
        }
    if missing_files:
        return {
            "status": "hold",
            "decision": "referenced_evidence_missing",
            "reason": "One or more referenced evidence, backup, or config paths do not exist.",
            "next_route": "Create the missing baseline/post-change/rollback artifacts or update the manifest paths.",
            "missing_fields": [],
            "missing_files": [row["path"] for row in missing_files],
            "route_failures": [source["source_id"] for source in route_failures],
            "expected_model_present": expected_present,
        }
    if route_failures and REQUIRE_ROUTE_OK:
        return {
            "status": "hold",
            "decision": "route_or_state_check_failed",
            "reason": "At least one configured route or native state check failed.",
            "next_route": "Run the observability runner or troubleshoot route/startup before the lifecycle change.",
            "missing_fields": [],
            "missing_files": [],
            "route_failures": [source["source_id"] for source in route_failures],
            "expected_model_present": expected_present,
        }
    if phase == "before":
        decision = "change_freeze_ready"
        reason = "The before-change manifest, baseline artifacts, backup route, rollback route, and validation suite are present."
    elif phase == "after":
        decision = "post_change_validation_ready"
        reason = "The after-change manifest and post-change artifacts are present for review."
    else:
        decision = "rollback_validation_ready"
        reason = "The rollback manifest and rollback artifacts are present for review."
    return {
        "status": "pass",
        "decision": decision,
        "reason": reason,
        "next_route": "Proceed only with the one named lifecycle action, then rerun the matching after or rollback phase.",
        "missing_fields": [],
        "missing_files": [],
        "route_failures": [source["source_id"] for source in route_failures],
        "expected_model_present": expected_present,
    }


def write_sources_csv(path, sources):
    fields = ["source_id", "source_type", "status", "ok", "elapsed_ms", "bytes", "url", "command", "result_path", "note"]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for source in sources:
            writer.writerow(source)


def write_markdown(path, result):
    decision = result["decision"]
    manifest = result.get("manifest") or {}
    lines = [
        f"# Service Lifecycle and Upgrade Runner - {RUN_ID}",
        "",
        "## Decision",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Status | `{decision['status']}` |",
        f"| Decision | `{decision['decision']}` |",
        f"| Reason | {md_cell(decision['reason'])} |",
        f"| Next route | {md_cell(decision['next_route'])} |",
        f"| Missing fields | {md_cell(decision.get('missing_fields', []))} |",
        f"| Missing files | {md_cell(decision.get('missing_files', []))} |",
        f"| Route failures | {md_cell(decision.get('route_failures', []))} |",
        f"| Expected model present | `{decision.get('expected_model_present')}` |",
        "",
        "## Change",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Change id | {md_cell(manifest.get('change_id'))} |",
        f"| Phase | `{manifest.get('phase', '')}` |",
        f"| Runtime | {md_cell(manifest.get('runtime'))} |",
        f"| Reason | {md_cell(manifest.get('reason'))} |",
        f"| Workload | {md_cell(manifest.get('workload'))} |",
        f"| Current model | {md_cell(get_path(manifest, 'current.model_id'))} |",
        f"| Target model | {md_cell(get_path(manifest, 'target.model_id'))} |",
        f"| Startup mode | {md_cell(get_path(manifest, 'startup.mode'))} |",
        f"| Endpoint | {md_cell(get_path(manifest, 'startup.endpoint'))} |",
        "",
        "## Sources",
        "",
        "| Source | Type | OK | Status | Result | Note |",
        "|---|---|---:|---|---|---|",
    ]
    for source in result["sources"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    md_cell(source["source_id"]),
                    md_cell(source["source_type"]),
                    md_cell(source["ok"]),
                    md_cell(source["status"]),
                    md_cell(source.get("result_path", "")),
                    md_cell(source.get("note", "")),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Evidence Inventory",
            "",
            "| Label | Exists | File | Size | SHA-256 |",
            "|---|---:|---:|---:|---|",
        ]
    )
    for row in result["inventory"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    md_cell(row["label"]),
                    md_cell(row["exists"]),
                    md_cell(row["is_file"]),
                    md_cell(row["size_bytes"]),
                    md_cell(row["sha256"][:16] if row["sha256"] else row["note"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Output Files",
            "",
            f"- Results JSON: `{result['results_json']}`",
            f"- Sources CSV: `{result['sources_csv']}`",
            f"- Inventory CSV: `{result['inventory_csv']}`",
            f"- Sources JSONL: `{result['sources_jsonl']}`",
            f"- Runs JSONL: `{result['runs_jsonl']}`",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def compact_source(source):
    return {key: value for key, value in source.items() if key != "parsed"}


RUN_ROOT = Path(os.environ.get("LOCAL_LLM_RUN_ROOT", ".")).expanduser().resolve()
RUN_ID = time.strftime("%Y%m%d-%H%M%S-lifecycle")
OUT_DIR = RUN_ROOT / "service-lifecycle-upgrade-runner"
MANIFEST_PATH = os.environ.get("LOCAL_LLM_LIFECYCLE_MANIFEST", "").strip()
BASE_URL = os.environ.get("LOCAL_LLM_BASE_URL", "").strip()
OLLAMA_API_URL = os.environ.get("LOCAL_LLM_OLLAMA_API_URL", "").strip()
API_KEY = os.environ.get("LOCAL_LLM_API_KEY", "").strip()
EXPECTED_MODEL = os.environ.get("LOCAL_LLM_EXPECTED_MODEL", "").strip()
TIMEOUT_SECONDS = max(1, as_int(os.environ.get("LOCAL_LLM_TIMEOUT_SECONDS"), 10))
COMMAND_TIMEOUT_SECONDS = max(1, as_int(os.environ.get("LOCAL_LLM_COMMAND_TIMEOUT_SECONDS"), 10))
ALLOW_COMMANDS = env_bool("LOCAL_LLM_LIFECYCLE_ALLOW_COMMANDS", True)
REQUIRE_ROUTE_OK = env_bool("LOCAL_LLM_LIFECYCLE_REQUIRE_ROUTE_OK", False)

OUT_DIR.mkdir(parents=True, exist_ok=True)
manifest, manifest_error = load_manifest(MANIFEST_PATH)
if manifest is None:
    template = OUT_DIR / "service-lifecycle-upgrade-runner-manifest-template.json"
    write_manifest_template(template)
    result = {
        "run_id": RUN_ID,
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "manifest": None,
        "manifest_error": manifest_error,
        "decision": classify(None, manifest_error, [], [], []),
        "sources": [],
        "inventory": [],
        "results_json": str(OUT_DIR / f"{RUN_ID}-lifecycle-results.json"),
        "results_md": str(OUT_DIR / f"{RUN_ID}-lifecycle-results.md"),
        "sources_csv": str(OUT_DIR / f"{RUN_ID}-lifecycle-sources.csv"),
        "inventory_csv": str(OUT_DIR / f"{RUN_ID}-lifecycle-inventory.csv"),
        "sources_jsonl": str(OUT_DIR / f"{RUN_ID}-lifecycle-sources.jsonl"),
        "runs_jsonl": str(OUT_DIR / "service-lifecycle-upgrade-runs.jsonl"),
        "template": str(template),
    }
    write_json(Path(result["results_json"]), result)
    write_markdown(Path(result["results_md"]), result)
    print(json.dumps({"status": "error", "decision": "manifest_missing_or_invalid", "template": str(template)}, indent=2))
    raise SystemExit(0)

phase = str(manifest.get("phase", "before")).lower()
runtime = str(manifest.get("runtime") or "").strip()
startup_endpoint = str(get_path(manifest, "startup.endpoint") or "").strip()
startup_native = str(get_path(manifest, "startup.native_api") or "").strip()
if not BASE_URL and startup_endpoint.startswith("http"):
    BASE_URL = startup_endpoint
if not OLLAMA_API_URL and startup_native.startswith("http"):
    OLLAMA_API_URL = startup_native

sources = []
host_platform = {
    "source_id": "host_platform",
    "source_type": "host_platform",
    "status": "ok",
    "ok": True,
    "elapsed_ms": 0,
    "bytes": 0,
    "url": "",
    "command": "",
    "result_path": "",
    "note": f"{socket.gethostname()} {platform.platform()} Python {platform.python_version()}",
}
sources.append(host_platform)

if BASE_URL:
    sources.append(fetch_source("openai_models", "openai_models", join_url(BASE_URL, "/models"), expect_json=True))
if OLLAMA_API_URL:
    sources.append(fetch_source("ollama_version", "ollama_version", join_url(OLLAMA_API_URL, "/version"), expect_json=True))
    sources.append(fetch_source("ollama_tags", "ollama_tags", join_url(OLLAMA_API_URL, "/tags"), expect_json=True))
    sources.append(fetch_source("ollama_ps", "ollama_ps", join_url(OLLAMA_API_URL, "/ps"), expect_json=True))

if ALLOW_COMMANDS:
    for source_id, command in built_in_commands(runtime):
        sources.append(run_command(source_id, command))

inventory = file_inventory(manifest)
model_ids = []
for source in sources:
    if source["source_type"] == "openai_models":
        model_ids.extend(openai_model_ids(source.get("parsed")))
    if source["source_type"] == "ollama_tags":
        model_ids.extend(ollama_model_ids(source.get("parsed")))
    if source["source_type"] == "ollama_ps":
        model_ids.extend(ollama_model_ids(source.get("parsed")))
model_ids = sorted(set(model_ids))
decision = classify(manifest, "", sources, inventory, model_ids)

results_json = OUT_DIR / f"{RUN_ID}-lifecycle-results.json"
results_md = OUT_DIR / f"{RUN_ID}-lifecycle-results.md"
sources_csv = OUT_DIR / f"{RUN_ID}-lifecycle-sources.csv"
inventory_csv = OUT_DIR / f"{RUN_ID}-lifecycle-inventory.csv"
sources_jsonl = OUT_DIR / f"{RUN_ID}-lifecycle-sources.jsonl"
runs_jsonl = OUT_DIR / "service-lifecycle-upgrade-runs.jsonl"

for source in sources:
    append_jsonl(sources_jsonl, compact_source(source))

result = {
    "run_id": RUN_ID,
    "created_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
    "phase": phase,
    "manifest_path": manifest.get("_manifest_path"),
    "manifest": {key: value for key, value in manifest.items() if key != "_manifest_path"},
    "base_url": BASE_URL,
    "ollama_api_url": OLLAMA_API_URL,
    "expected_model": EXPECTED_MODEL or str(get_path(manifest, "current.model_id") or ""),
    "model_ids": model_ids,
    "allow_commands": ALLOW_COMMANDS,
    "require_route_ok": REQUIRE_ROUTE_OK,
    "decision": decision,
    "sources": [compact_source(source) for source in sources],
    "inventory": inventory,
    "results_json": str(results_json),
    "results_md": str(results_md),
    "sources_csv": str(sources_csv),
    "inventory_csv": str(inventory_csv),
    "sources_jsonl": str(sources_jsonl),
    "runs_jsonl": str(runs_jsonl),
    "external_docs_checked": [
        "https://docs.ollama.com/api/introduction",
        "https://lmstudio.ai/docs/cli/serve/server-status",
        "https://github.com/lmstudio-ai/lms",
        "https://docs.vllm.ai/en/stable/deployment/docker/",
        "https://docs.openwebui.com/getting-started/updating/",
        "https://docs.openwebui.com/tutorials/maintenance/backups/",
        "https://docs.openwebui.com/reference/env-configuration/",
    ],
}

write_sources_csv(sources_csv, result["sources"])
write_inventory_csv(inventory_csv, inventory)
write_json(results_json, result)
write_markdown(results_md, result)
append_jsonl(
    runs_jsonl,
    {
        "run_id": RUN_ID,
        "phase": phase,
        "status": decision["status"],
        "decision": decision["decision"],
        "results_json": str(results_json),
        "results_md": str(results_md),
        "inventory_csv": str(inventory_csv),
    },
)

print(
    json.dumps(
        {
            "status": decision["status"],
            "decision": decision["decision"],
            "run_id": RUN_ID,
            "results_json": str(results_json),
            "results_md": str(results_md),
            "sources_csv": str(sources_csv),
            "inventory_csv": str(inventory_csv),
            "sources_jsonl": str(sources_jsonl),
            "runs_jsonl": str(runs_jsonl),
        },
        indent=2,
    )
)
```

## Runtime Knobs

| Variable | Required | Meaning |
|---|---:|---|
| `LOCAL_LLM_RUN_ROOT` | no | Evidence root. Defaults to the current directory. |
| `LOCAL_LLM_LIFECYCLE_MANIFEST` | yes | Path to the lifecycle manifest JSON. If missing, a template is written. |
| `LOCAL_LLM_BASE_URL` | no | OpenAI-compatible base URL. Defaults to `startup.endpoint` when it is an HTTP URL. |
| `LOCAL_LLM_OLLAMA_API_URL` | no | Ollama native API base. Defaults to `startup.native_api` when it is an HTTP URL. |
| `LOCAL_LLM_EXPECTED_MODEL` | no | Model id expected in `/v1/models`, `/api/tags`, or `/api/ps`. Defaults to `current.model_id`. |
| `LOCAL_LLM_API_KEY` | no | Local placeholder or proxy token for model-list calls. |
| `LOCAL_LLM_LIFECYCLE_ALLOW_COMMANDS` | no | Set `0` to skip built-in version commands. Defaults to `1`. |
| `LOCAL_LLM_LIFECYCLE_REQUIRE_ROUTE_OK` | no | Set `1` to hold if configured route checks fail. Defaults to `0` because offline change-freeze cards are still useful. |
| `LOCAL_LLM_TIMEOUT_SECONDS` | no | HTTP timeout. Defaults to `10`. |
| `LOCAL_LLM_COMMAND_TIMEOUT_SECONDS` | no | Built-in command timeout. Defaults to `10`. |

## PowerShell Run

```powershell
$RunRoot = Join-Path $HOME ("Documents\local-llm-runs\" + (Get-Date -Format "yyyy-MM-dd-HHmm") + "-lifecycle")
New-Item -ItemType Directory -Force -Path $RunRoot | Out-Null

$env:LOCAL_LLM_RUN_ROOT = $RunRoot
$env:LOCAL_LLM_LIFECYCLE_MANIFEST = "D:\LLM-Runs\lifecycle-manifest.json"
$env:LOCAL_LLM_LIFECYCLE_ALLOW_COMMANDS = "1"
$env:LOCAL_LLM_LIFECYCLE_REQUIRE_ROUTE_OK = "1"
python .\service-lifecycle-upgrade-runner.py
```

For a dry template:

```powershell
$env:LOCAL_LLM_RUN_ROOT = $RunRoot
Remove-Item Env:\LOCAL_LLM_LIFECYCLE_MANIFEST -ErrorAction SilentlyContinue
python .\service-lifecycle-upgrade-runner.py
```

## Fixture Verification

Use this fake loopback server to verify the runner without changing a real service.

```python
import json
import os
import subprocess
import sys
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class FixtureHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        return

    def send_json(self, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/v1/models":
            self.send_json({"object": "list", "data": [{"id": "fixture-model", "object": "model"}]})
            return
        if self.path == "/api/version":
            self.send_json({"version": "0.fixture"})
            return
        if self.path == "/api/tags":
            self.send_json({"models": [{"name": "fixture-model", "model": "fixture-model"}]})
            return
        if self.path == "/api/ps":
            self.send_json({"models": [{"name": "fixture-model", "model": "fixture-model"}]})
            return
        self.send_response(404)
        self.end_headers()


def write_fixture_file(path, payload):
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: python fixture-test.py service-lifecycle-upgrade-runner.py")
    runner = Path(sys.argv[1]).resolve()
    if not runner.exists():
        raise SystemExit(f"runner not found: {runner}")

    server = ThreadingHTTPServer(("127.0.0.1", 0), FixtureHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_address[1]}"

    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        artifacts = {}
        for name in ("observability", "api_contract", "benchmark", "quality", "security"):
            path = root / f"{name}.json"
            write_fixture_file(path, {"name": name, "status": "fixture"})
            artifacts[name] = str(path)
        backup_path = root / "backup.json"
        write_fixture_file(backup_path, {"backup": "fixture"})
        manifest = {
            "change_id": "fixture-before",
            "phase": "before",
            "runtime": "ollama",
            "reason": "fixture validation",
            "workload": "fixture workload",
            "owner": "fixture",
            "current": {
                "runtime_version": "0.fixture",
                "model_id": "fixture-model",
                "model_revision_or_digest": "fixture-digest",
                "model_cache_path": str(root / "models"),
                "quantization": "fixture",
            },
            "target": {
                "runtime_version": "0.fixture",
                "model_id": "fixture-model",
                "model_revision_or_digest": "fixture-digest",
            },
            "startup": {
                "mode": "manual shell",
                "command": "fixture serve",
                "endpoint": f"{base}/v1",
                "native_api": f"{base}/api",
                "bind_address": "127.0.0.1",
                "port": server.server_address[1],
                "env_vars": ["FIXTURE_MODELS"],
                "working_directory": str(root),
            },
            "baseline_artifacts": artifacts,
            "backup": {"paths": [str(backup_path)], "restore_method": "restore fixture backup"},
            "rollback": {
                "target": "fixture previous state",
                "steps": ["stop", "restore", "start", "validate"],
            },
            "abort_conditions": ["fixture route fails"],
            "post_change_validation": ["observability", "api_contract", "benchmark", "quality", "security"],
        }
        manifest_path = root / "manifest.json"
        write_fixture_file(manifest_path, manifest)
        env = os.environ.copy()
        env.update(
            {
                "LOCAL_LLM_RUN_ROOT": str(root),
                "LOCAL_LLM_LIFECYCLE_MANIFEST": str(manifest_path),
                "LOCAL_LLM_EXPECTED_MODEL": "fixture-model",
                "LOCAL_LLM_LIFECYCLE_ALLOW_COMMANDS": "0",
                "LOCAL_LLM_LIFECYCLE_REQUIRE_ROUTE_OK": "1",
                "LOCAL_LLM_TIMEOUT_SECONDS": "5",
            }
        )
        completed = subprocess.run([sys.executable, str(runner)], text=True, capture_output=True, env=env, check=True)
        summary = json.loads(completed.stdout)
        results = json.loads(Path(summary["results_json"]).read_text(encoding="utf-8"))
        assert summary["status"] == "pass", summary
        assert summary["decision"] == "change_freeze_ready", summary
        assert results["decision"]["expected_model_present"] is True
        assert len(results["inventory"]) >= 6
        assert all(row["exists"] for row in results["inventory"]), results["inventory"]
        assert Path(summary["inventory_csv"]).exists()
        assert Path(summary["results_md"]).exists()
    server.shutdown()
    print("fixture pass")


if __name__ == "__main__":
    main()
```

## Status Interpretation

| Status | Decision | Meaning | Next route |
|---|---|---|---|
| `pass` | `change_freeze_ready` | Before-change card, baseline artifacts, backup, rollback, and validation suite are present. | Make only the named change, then rerun with `phase=after`. |
| `pass` | `post_change_validation_ready` | After-change artifacts are present for review. | Compare against baseline and decide keep, hold, or rollback. |
| `pass` | `rollback_validation_ready` | Rollback artifacts are present for review. | Record the failed change and troubleshooting owner. |
| `hold` | `lifecycle_manifest_incomplete` | Required fields are missing. | Fill the manifest before changing anything. |
| `hold` | `referenced_evidence_missing` | A referenced artifact, backup, or config path does not exist. | Create the missing artifact or correct the path. |
| `hold` | `expected_model_missing` | The expected model id was absent from captured route/model-list state. | Check route, cache path, load state, or runtime health. |
| `hold` | `route_or_state_check_failed` | A configured route or state check failed and route success was required. | Run observability or troubleshooting before change. |
| `error` | `manifest_missing_or_invalid` | The runner could not load a manifest. | Use the generated template. |

## Completion Gate

The runner output is usable when:

- [ ] manifest phase is `before`, `after`, or `rollback`
- [ ] required fields for that phase are filled
- [ ] referenced artifacts, backups, and configs exist or the missing path is a named blocker
- [ ] expected model visibility is captured when a route is configured
- [ ] built-in version/state commands are captured or intentionally disabled
- [ ] the decision names the next controlled lifecycle action
- [ ] the run folder contains results JSON, Markdown, source CSV, inventory CSV, source JSONL, and runs JSONL

## External Docs Checked

- [Ollama API introduction](https://docs.ollama.com/api/introduction)
- [LM Studio server status CLI](https://lmstudio.ai/docs/cli/serve/server-status)
- [LM Studio lms CLI](https://github.com/lmstudio-ai/lms)
- [vLLM Docker deployment](https://docs.vllm.ai/en/stable/deployment/docker/)
- [Open WebUI updating guide](https://docs.openwebui.com/getting-started/updating/)
- [Open WebUI backup guide](https://docs.openwebui.com/tutorials/maintenance/backups/)
- [Open WebUI environment configuration](https://docs.openwebui.com/reference/env-configuration/)

## References

- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook]]
- [[LLM/Study/Local LLM Observability and Operations Runner]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]]
- [[LLM/Study/Local LLM First Smoke Request Runner]]
- [[LLM/Study/Local LLM First Benchmark Row Builder]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Security and Privacy Runner]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Docker GPU Container Serving Lab]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
