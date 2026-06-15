---
tags: [study, llm, inference, local-llm, windows, commands, planning, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-16
---

# Local LLM First Run Command Plan Runner

> **One-line summary** Generate and audit one ordered PowerShell command plan for the first local LLM run before installing, pulling, or sending any inference request.

Use this after [[LLM/Study/Local LLM First Run Readiness Snapshot|Local LLM First Run Readiness Snapshot]], [[LLM/Study/Local LLM Model Store Readiness Snapshot|Local LLM Model Store Readiness Snapshot]], and [[LLM/Study/Local LLM First Model Candidate Ladder|Local LLM First Model Candidate Ladder]] have made the first runtime, model, model-store, and loopback assumptions explicit. This runner sits before [[LLM/Study/Local LLM Windows First-Run Quickstart|Local LLM Windows First-Run Quickstart]], [[LLM/Study/Local LLM Command Cookbook|Local LLM Command Cookbook]], and [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]] when you want one generated command sequence with evidence filenames already named. It also generates the manifest for [[LLM/Study/Local LLM Windows Runtime Install Runner|Local LLM Windows Runtime Install Runner]] so the installed-runtime check can be audited before the first pull.

The runner itself does not install Ollama, pull a model, call `/api/chat`, call `/api/generate`, or call `/v1/chat/completions`. It writes a reviewed command plan: JSON, Markdown, CSV, JSONL, and a PowerShell script that you can inspect before running.

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| Manifest | The intended runtime, model id, run folder, storage decision, install gate, pull gate, and security boundary are named before execution. | The model is downloaded or usable. |
| Command plan | The first-run sequence has explicit commands and evidence filenames. | The commands have been run. |
| Loopback check | Planned native and OpenAI-compatible base URLs are loopback unless explicitly waived. | Non-loopback exposure is safe. |
| Step inventory | Runtime install, model pull, runtime health, smoke request, debrief, endpoint audit, and full packet audit are ordered. | Any downstream audit has passed. |
| PowerShell review script | The exact commands can be reviewed as one file before touching the machine. | The script should be run without reading. |

Academic bridge: this is the boundary between planning and measurement. It turns "I will run a local model" into a falsifiable sequence of runtime, model, API route, response, timing, quality, and safety evidence.

## Manifest Shape

Minimum first-run manifest:

```json
{
  "run_id": "first-local-inference-001",
  "run_root": "D:/llm-runs/2026-06-16-first-local-inference",
  "runtime": "ollama",
  "runtime_boundary": "Windows native Ollama service",
  "model_id": "qwen3.5:4b",
  "source_page": "https://ollama.com/library/qwen3.5:4b",
  "source_checked_at": "2026-06-16",
  "native_base_url": "http://127.0.0.1:11434",
  "openai_base_url": "http://127.0.0.1:11434/v1",
  "security_boundary": "loopback only",
  "model_store_decision": "default user profile store accepted",
  "runtime_install_scope": "official Windows installer or existing signed install, then new-shell PATH proof",
  "model_pull_scope": "pull exactly one baseline tag, then list/tags/show proof",
  "require_loopback": true,
  "include_openai_route": true,
  "include_streaming": false
}
```

Optional fields:

```json
{
  "output_root": "D:/llm-runs/command-plans",
  "vault_root": "D:/Vaults/PersonalKB",
  "ollama_models_path": "D:/LocalModels/Ollama",
  "expected_source_digest": "2a654d98e6fb",
  "source_recheck_snippets": ["2a654d98e6fb", "3.4GB", "parameters 4.66B", "quantization Q4_K_M"],
  "security_review_proof": "",
  "native_smoke_prompt": "Reply with one sentence: local endpoint ready.",
  "openai_smoke_prompt": "Reply with one sentence: OpenAI-compatible route ready."
}
```

Keep `require_loopback: true` for the first run. Set it to `false` only when [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] already has a linked review for the planned exposure.

## Standard-Library Runner

Save this as `first-run-command-plan.py` in the planning folder or extract it directly from this note. It uses only Python's standard library and does not call the local runtime.

```python
from __future__ import annotations

import csv
import datetime as dt
import json
import os
import re
import sys
import urllib.parse
from pathlib import Path
from typing import Any


def utc_iso() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def slug(value: Any) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value or "").strip()).strip("-")
    return text or "run"


def display(value: Any) -> str:
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
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def list_value(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [display(item) for item in value if display(item)]
    if isinstance(value, str):
        return [item.strip() for item in re.split(r"[;\n]", value) if item.strip()]
    return [display(value)] if display(value) else []


def load_manifest() -> tuple[Path, dict[str, Any]]:
    manifest_value = os.environ.get("LOCAL_LLM_FIRST_RUN_COMMAND_PLAN_MANIFEST") or (
        sys.argv[1] if len(sys.argv) > 1 else ""
    )
    if manifest_value:
        manifest_path = Path(manifest_value).expanduser().resolve()
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if not isinstance(manifest, dict):
            raise ValueError("Manifest must be a JSON object.")
        return manifest_path, manifest

    run_root_value = os.environ.get("LOCAL_LLM_FIRST_RUN_COMMAND_PLAN_ROOT")
    if run_root_value:
        run_root = Path(run_root_value).expanduser().resolve()
        return run_root / "first-run-command-plan-manifest.json", {"run_root": str(run_root)}

    raise ValueError(
        "Set LOCAL_LLM_FIRST_RUN_COMMAND_PLAN_MANIFEST or LOCAL_LLM_FIRST_RUN_COMMAND_PLAN_ROOT."
    )


def ps_quote(value: Any) -> str:
    return "'" + display(value).replace("'", "''") + "'"


def parsed_host(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    return (parsed.hostname or "").strip().lower().strip("[]")


def is_loopback_host(host: str) -> bool:
    if host in {"localhost", "::1"}:
        return True
    if host.startswith("127."):
        return True
    return False


def wiki_link(route: str) -> str:
    clean = display(route)
    if not clean:
        return ""
    label = clean.split("/")[-1]
    open_link = "[" * 2
    close_link = "]" * 2
    return open_link + clean + "|" + label + close_link


def finding(level: str, owner: str, text: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "owner": owner,
        "finding": text,
        "evidence": evidence,
        "action": action,
    }


def make_step(
    step_id: str,
    phase: str,
    route: str,
    evidence_path: str,
    command: str,
    note: str,
    required: bool = True,
) -> dict[str, Any]:
    return {
        "step_id": step_id,
        "phase": phase,
        "required": required,
        "route": route,
        "evidence_path": evidence_path,
        "command": command.strip(),
        "note": note,
    }


def build_steps(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    include_openai = bool_value(manifest.get("include_openai_route"), True)
    include_streaming = bool_value(manifest.get("include_streaming"), False)
    ollama_models_path = display(manifest.get("ollama_models_path"))
    native_prompt = display(manifest.get("native_smoke_prompt")) or "Reply with one sentence: local endpoint ready."
    openai_prompt = display(manifest.get("openai_smoke_prompt")) or (
        "Reply with one sentence: OpenAI-compatible route ready."
    )

    steps = [
        make_step(
            "01-create-run-root",
            "run-folder",
            "LLM/Study/Local LLM First Endpoint Run Sheet",
            "run-root.txt",
            """
New-Item -ItemType Directory -Force -Path $RunRoot | Out-Null
"created $RunRoot" | Set-Content -Path (Join-Path $RunRoot "run-root.txt") -Encoding utf8
""",
            "Create the stable run folder before any install, pull, or endpoint command.",
        ),
        make_step(
            "02-write-run-card",
            "run-folder",
            "LLM/Study/Local LLM First Inference Evidence Pack",
            "run-card.txt",
            """
@"
run_id=$RunId
runtime=$Runtime
runtime_boundary=$RuntimeBoundary
model_id=$ModelId
native_base_url=$NativeBase
openai_base_url=$OpenAIBase
security_boundary=$SecurityBoundary
model_store_decision=$ModelStoreDecision
"@ | Set-Content -Path (Join-Path $RunRoot "run-card.txt") -Encoding utf8
""",
            "Record the run identity and boundaries before collecting machine evidence.",
        ),
        make_step(
            "03-capture-windows-preflight",
            "machine-preflight",
            "LLM/Study/Local LLM Environment Preflight Lab",
            "preflight-windows.json",
            """
Get-ComputerInfo | Select-Object CsName, WindowsProductName, WindowsVersion, OsBuildNumber, OsArchitecture |
  ConvertTo-Json -Depth 4 | Set-Content -Path (Join-Path $RunRoot "preflight-windows.json") -Encoding utf8
""",
            "Capture Windows build evidence for the first-run packet.",
        ),
        make_step(
            "04-capture-hardware-preflight",
            "machine-preflight",
            "LLM/Study/Local LLM Hardware Sizing Runner",
            "preflight-hardware.json",
            """
[ordered]@{
  cpu = Get-CimInstance Win32_Processor | Select-Object Name, NumberOfCores, NumberOfLogicalProcessors
  gpu = Get-CimInstance Win32_VideoController | Select-Object Name, AdapterRAM, DriverVersion
  disk = Get-PSDrive -PSProvider FileSystem | Select-Object Name, Root, Used, Free
} | ConvertTo-Json -Depth 6 | Set-Content -Path (Join-Path $RunRoot "preflight-hardware.json") -Encoding utf8
if (Get-Command nvidia-smi -ErrorAction SilentlyContinue) {
  nvidia-smi | Set-Content -Path (Join-Path $RunRoot "nvidia-smi.txt") -Encoding utf8
} else {
  "nvidia-smi not found" | Set-Content -Path (Join-Path $RunRoot "nvidia-smi.txt") -Encoding utf8
}
""",
            "Capture CPU, GPU, disk, and optional NVIDIA evidence before selecting performance expectations.",
        ),
        make_step(
            "05-record-model-store",
            "model-store",
            "LLM/Study/Local LLM Model Store Readiness Snapshot",
            "model-store-decision.json",
            """
[ordered]@{
  model_store_decision = $ModelStoreDecision
  ollama_models_process = $env:OLLAMA_MODELS
  ollama_models_user = [Environment]::GetEnvironmentVariable("OLLAMA_MODELS", "User")
  ollama_models_machine = [Environment]::GetEnvironmentVariable("OLLAMA_MODELS", "Machine")
} | ConvertTo-Json -Depth 5 | Set-Content -Path (Join-Path $RunRoot "model-store-decision.json") -Encoding utf8
""",
            "Save the storage decision and current OLLAMA_MODELS inheritance before the first large download.",
        ),
    ]

    if ollama_models_path:
        steps.append(
            make_step(
                "05b-review-custom-model-store",
                "model-store",
                "LLM/Study/Local LLM Windows Model Store and Cache Plan",
                "model-store-change-review.txt",
                f"""
# Review before executing in a normal PowerShell session:
# New-Item -ItemType Directory -Force -Path {ps_quote(ollama_models_path)} | Out-Null
# setx OLLAMA_MODELS {ps_quote(ollama_models_path)}
"custom model store requires a new shell after setx" |
  Set-Content -Path (Join-Path $RunRoot "model-store-change-review.txt") -Encoding utf8
""",
                "Plan the custom model-store change without applying it inside the planner.",
            )
        )

    steps.append(
        make_step(
            "06-plan-model-source-recheck",
            "model-source",
            "LLM/Study/Local LLM First Model Source Recheck Runner",
            "first-model-source-recheck-manifest.json",
            """
@{
  run_id = "$RunId-model-source-recheck"
  run_root = $RunRoot
  source_checked_at = $SourceCheckedAt
  next_route = "LLM/Study/Local LLM First Run Command Plan Runner"
  candidates = @(
    @{
      candidate_id = "first-run-selected-model"
      slot = "selected first-run model"
      model_id = $ModelId
      source_url = $SourcePage
      required = $true
      expected_snippets = $SourceRecheckSnippets
      next_route = "LLM/Study/Local LLM First Model Pull Gate"
    }
  )
} | ConvertTo-Json -Depth 10 | Set-Content -Path (Join-Path $RunRoot "first-model-source-recheck-manifest.json") -Encoding utf8
# Extract first-model-source-recheck.py, then run:
# $env:LOCAL_LLM_FIRST_MODEL_SOURCE_RECHECK_MANIFEST = Join-Path $RunRoot "first-model-source-recheck-manifest.json"
# python .\\first-model-source-recheck.py
""",
            "Prepare the dated source-page recheck before any model pull.",
        )
    )

    steps.extend(
        [
            make_step(
                "07-plan-runtime-install-runner",
                "runtime-install",
                "LLM/Study/Local LLM Windows Runtime Install Runner",
                "windows-runtime-install-manifest.json",
                """
@{
  run_id = "$RunId-runtime-install"
  run_root = $RunRoot
  runtime = $Runtime
  installer_source = "https://ollama.com/download/windows"
  installer_method = $RuntimeInstallScope
  model_store_decision = $ModelStoreDecision
  expected_ollama_models = $env:OLLAMA_MODELS
  native_base_url = $NativeBase
  require_loopback = $true
  require_command = $true
  require_listener = $true
  require_api_version = $true
  require_api_tags = $true
  pass_next_route = "LLM/Study/Local LLM First Model Source Recheck Runner"
  hold_next_route = "LLM/Study/Local LLM Windows Runtime Install Gate"
  fail_next_route = "LLM/Study/Local LLM Security and Privacy Runbook"
} | ConvertTo-Json -Depth 8 | Set-Content -Path (Join-Path $RunRoot "windows-runtime-install-manifest.json") -Encoding utf8
# Extract windows-runtime-install-runner.py, then run:
# $env:LOCAL_LLM_WINDOWS_RUNTIME_INSTALL_MANIFEST = Join-Path $RunRoot "windows-runtime-install-manifest.json"
# python .\\windows-runtime-install-runner.py
""",
                "Prepare the no-generation install-readiness runner manifest before first model pull.",
            ),
            make_step(
                "07-prove-runtime-install",
                "runtime-install",
                "LLM/Study/Local LLM Windows Runtime Install Runner",
                "runtime-install.txt",
                """
Get-Command ollama -ErrorAction SilentlyContinue |
  Select-Object Source, Version | Format-List | Out-String |
  Set-Content -Path (Join-Path $RunRoot "ollama-command.txt") -Encoding utf8
ollama --version 2>&1 | Tee-Object -FilePath (Join-Path $RunRoot "runtime-install.txt")
""",
                "Capture executable and version evidence after installing or opening the runtime.",
            ),
            make_step(
                "08-prove-runtime-listener",
                "runtime-install",
                "LLM/Study/Local LLM Windows Runtime Install Runner",
                "runtime-version.json",
                """
try {
  Invoke-RestMethod -Method Get -Uri "$NativeBase/api/version" |
    ConvertTo-Json -Depth 8 | Set-Content -Path (Join-Path $RunRoot "runtime-version.json") -Encoding utf8
} catch {
  $_ | Out-String | Set-Content -Path (Join-Path $RunRoot "runtime-version-error.txt") -Encoding utf8
}
""",
                "Check that the planned native base URL is reachable before model pull or smoke.",
            ),
            make_step(
                "09-pull-first-model",
                "model-pull",
                "LLM/Study/Local LLM First Model Pull Gate",
                "ollama-pull.txt",
                """
$ModelId | Set-Content -Path (Join-Path $RunRoot "selected-model.txt") -Encoding utf8
@"
gate=Local LLM First Model Pull Gate
runtime=$Runtime
selected_model=$ModelId
source_page=$SourcePage
source_checked_at=$SourceCheckedAt
source_recheck_output=$(Join-Path $RunRoot "first-model-source-recheck\$RunId-model-source-recheck\$RunId-model-source-recheck-model-source-recheck.json")
runtime_install_runner_output=$(Join-Path $RunRoot "windows-runtime-install\$RunId-runtime-install\$RunId-runtime-install-runtime-install.json")
model_store_decision=$ModelStoreDecision
next_gate=Local LLM First Runtime Health Runner
"@ | Set-Content -Path (Join-Path $RunRoot "model-pull-decision.txt") -Encoding utf8
ollama pull $ModelId 2>&1 | Tee-Object -FilePath (Join-Path $RunRoot "ollama-pull.txt")
ollama ls 2>&1 | Tee-Object -FilePath (Join-Path $RunRoot "ollama-ls-after-pull.txt")
""",
                "Pull only the selected first model and save CLI inventory output with pull-gate filenames.",
            ),
            make_step(
                "10-capture-native-model-list",
                "model-pull",
                "LLM/Study/Local LLM First Model Pull Gate",
                "ollama-api-tags-after-pull.json",
                """
Invoke-RestMethod -Method Get -Uri "$NativeBase/api/tags" |
  ConvertTo-Json -Depth 10 | Set-Content -Path (Join-Path $RunRoot "ollama-api-tags-after-pull.json") -Encoding utf8
""",
                "Capture the native model-list route after the pull.",
            ),
            make_step(
                "10b-capture-model-show",
                "model-pull",
                "LLM/Study/Local LLM First Model Pull Gate",
                "ollama-show-response.json",
                """
$ShowBody = @{ model = $ModelId; verbose = $false } | ConvertTo-Json -Depth 4
$ShowBody | Set-Content -Path (Join-Path $RunRoot "ollama-show-request.json") -Encoding utf8
Invoke-RestMethod -Method Post -Uri "$NativeBase/api/show" -ContentType "application/json" -Body $ShowBody |
  ConvertTo-Json -Depth 20 | Set-Content -Path (Join-Path $RunRoot "ollama-show-response.json") -Encoding utf8
""",
                "Capture local model metadata before any generation request.",
            ),
            make_step(
                "10c-plan-first-model-pull-runner",
                "model-pull",
                "LLM/Study/Local LLM First Model Pull Runner",
                "first-model-pull-manifest.json",
                """
@{
  run_id = "$RunId-first-model-pull"
  run_root = $RunRoot
  vault_root = $VaultRoot
  selected_model = $ModelId
  fallback_model = ""
  source_page = $SourcePage
  source_checked_at = $SourceCheckedAt
  source_recheck_output = (Join-Path $RunRoot "first-model-source-recheck\$RunId-model-source-recheck\$RunId-model-source-recheck-model-source-recheck.json")
  runtime_install_runner_output = (Join-Path $RunRoot "windows-runtime-install\$RunId-runtime-install\$RunId-runtime-install-runtime-install.json")
  expected_digest = $ExpectedSourceDigest
  expected_size = ""
  model_store_decision = $ModelStoreDecision
  pull_status = "pass"
  runtime_install_proof = "LLM/Study/Local LLM Windows Runtime Install Gate"
  model_store_proof = "LLM/Study/Local LLM Model Store Readiness Snapshot"
  runtime_compatibility_proof = "LLM/Study/Local LLM Runtime Compatibility Runner"
  artifacts = @{
    model_pull_decision = (Join-Path $RunRoot "model-pull-decision.txt")
    pull_output = (Join-Path $RunRoot "ollama-pull.txt")
    ollama_ls_after_pull = (Join-Path $RunRoot "ollama-ls-after-pull.txt")
    api_tags_after_pull = (Join-Path $RunRoot "ollama-api-tags-after-pull.json")
    api_show_response = (Join-Path $RunRoot "ollama-show-response.json")
  }
  next_route = "LLM/Study/Local LLM First Runtime Health Runner"
} | ConvertTo-Json -Depth 10 | Set-Content -Path (Join-Path $RunRoot "first-model-pull-manifest.json") -Encoding utf8
# Extract local_llm_first_model_pull_runner.py, then run:
# $env:LOCAL_LLM_FIRST_MODEL_PULL_MANIFEST = Join-Path $RunRoot "first-model-pull-manifest.json"
# $env:LOCAL_LLM_FIRST_MODEL_PULL_RUN_ROOT = $RunRoot
# $env:LOCAL_LLM_FIRST_MODEL_PULL_VAULT_ROOT = $VaultRoot
# python .\\local_llm_first_model_pull_runner.py
""",
                "Prepare the pull evidence audit manifest before runtime health.",
            ),
            make_step(
                "11-plan-runtime-health-runner",
                "runtime-health",
                "LLM/Study/Local LLM First Runtime Health Runner",
                "runtime-health-manifest.json",
                """
@{
  run_id = "$RunId-runtime-health"
  runtime = $Runtime
  native_bases = @($NativeBase)
  openai_bases = @($OpenAIBase)
  expected_model = $ModelId
  security_boundary = $SecurityBoundary
  require_openai_models = $IncludeOpenAI
  next_route = "LLM/Study/Local LLM First Smoke Request Runner"
} | ConvertTo-Json -Depth 8 | Set-Content -Path (Join-Path $RunRoot "runtime-health-manifest.json") -Encoding utf8
# Extract first-runtime-health-runner.py, then run:
# $env:LOCAL_LLM_RUNTIME_HEALTH_MANIFEST = Join-Path $RunRoot "runtime-health-manifest.json"
# $env:LOCAL_LLM_RUNTIME_HEALTH_RUN_ROOT = $RunRoot
# python .\\first-runtime-health-runner.py
""",
                "Prepare the no-generation runtime health manifest before smoke.",
            ),
            make_step(
                "12-send-native-smoke",
                "first-smoke",
                "LLM/Study/Local LLM First Smoke Request Runner",
                "native-chat-response.json",
                f"""
$NativeBody = @{{
  model = $ModelId
  messages = @(@{{ role = "user"; content = {ps_quote(native_prompt)} }})
  stream = $false
}} | ConvertTo-Json -Depth 8
Invoke-RestMethod -Method Post -Uri "$NativeBase/api/chat" -ContentType "application/json" -Body $NativeBody |
  ConvertTo-Json -Depth 20 | Set-Content -Path (Join-Path $RunRoot "native-chat-response.json") -Encoding utf8
""",
                "Send one deterministic native chat request only after health evidence is ready.",
            ),
        ]
    )

    if include_openai:
        steps.append(
            make_step(
                "13-send-openai-compatible-smoke",
                "first-smoke",
                "LLM/Study/Local LLM OpenAI-Compatible API Contract Runner",
                "openai-chat-completions-response.json",
                f"""
$OpenAIHeaders = @{{ Authorization = "Bearer ollama" }}
$OpenAIBody = @{{
  model = $ModelId
  messages = @(@{{ role = "user"; content = {ps_quote(openai_prompt)} }})
  stream = $false
}} | ConvertTo-Json -Depth 8
Invoke-RestMethod -Method Post -Uri "$OpenAIBase/chat/completions" -Headers $OpenAIHeaders -ContentType "application/json" -Body $OpenAIBody |
  ConvertTo-Json -Depth 20 | Set-Content -Path (Join-Path $RunRoot "openai-chat-completions-response.json") -Encoding utf8
""",
                "Prove the OpenAI-compatible route if reusable client code will use `/v1`.",
            )
        )

    if include_streaming:
        steps.append(
            make_step(
                "14-route-streaming-timing",
                "streaming",
                "LLM/Study/Local LLM First Streaming Timing Runner",
                "streaming-runner-manifest.json",
                """
@{
  run_id = "$RunId-streaming"
  base_url = $OpenAIBase
  model = $ModelId
  prompt = "Stream three short tokens."
} | ConvertTo-Json -Depth 8 | Set-Content -Path (Join-Path $RunRoot "streaming-runner-manifest.json") -Encoding utf8
# Use Local LLM First Streaming Timing Runner for event-level streaming evidence.
""",
                "Route streaming to the dedicated timing runner when streaming matters.",
                required=False,
            )
        )

    steps.extend(
        [
            make_step(
                "15-debrief-first-response",
                "response-debrief",
                "LLM/Study/Local LLM First Response Debrief Runner",
                "first-response-debrief-manifest.json",
                """
@{
  run_id = "$RunId-debrief"
  run_root = $RunRoot
  response_json = Join-Path $RunRoot "native-chat-response.json"
  runtime_health_json = Join-Path $RunRoot "runtime-health.json"
} | ConvertTo-Json -Depth 8 | Set-Content -Path (Join-Path $RunRoot "first-response-debrief-manifest.json") -Encoding utf8
# Extract first-response-debrief-runner.py, then run it against this manifest.
""",
                "Convert the first saved response into timing, route, and mechanism evidence.",
            ),
            make_step(
                "16-audit-endpoint-folder",
                "endpoint-audit",
                "LLM/Study/Local LLM First Endpoint Evidence Audit Runner",
                "first-endpoint-evidence-audit-manifest.json",
                """
@{
  run_id = "$RunId-endpoint-audit"
  run_root = $RunRoot
  require_runtime_health = $true
  require_smoke_response = $true
  require_debrief = $true
} | ConvertTo-Json -Depth 8 | Set-Content -Path (Join-Path $RunRoot "first-endpoint-evidence-audit-manifest.json") -Encoding utf8
# Run the endpoint evidence audit runner after all endpoint evidence files exist.
""",
                "Check whether the first endpoint folder is complete enough to count.",
            ),
            make_step(
                "17-audit-first-inference-pack",
                "packet-audit",
                "LLM/Study/Local LLM First Inference Evidence Pack Audit Runner",
                "first-inference-pack-audit-manifest.json",
                """
@{
  run_id = "$RunId-pack-audit"
  run_root = $RunRoot
  require_endpoint_audit = $true
  require_openai_contract = $IncludeOpenAI
  require_client = $true
  require_streaming = $IncludeStreaming
  require_benchmark = $true
  require_quality = $true
  require_security = $true
  require_final_decision = $true
} | ConvertTo-Json -Depth 8 | Set-Content -Path (Join-Path $RunRoot "first-inference-pack-audit-manifest.json") -Encoding utf8
# Run the full packet audit before linking this first run into the capstone workbook.
""",
                "Promote the first local inference run only after the full packet audit is scoped.",
            ),
        ]
    )

    return steps


def evaluate_plan(manifest: dict[str, Any], steps: list[dict[str, Any]]) -> dict[str, Any]:
    findings: list[dict[str, str]] = []
    required_fields = [
        ("run_root", "manifest", "Choose the evidence folder before generating the command plan."),
        ("runtime", "manifest", "Name the runtime before choosing CLI and API commands."),
        ("runtime_boundary", "runtime", "Name Windows native, WSL, Docker, or another boundary."),
        ("model_id", "model", "Choose one first model id before pull and smoke commands."),
        ("source_page", "source", "Link the current model page or tags page before pull."),
        ("source_checked_at", "source", "Record the source check date before pull."),
        ("security_boundary", "security", "State loopback-only or link the exposure review."),
        ("model_store_decision", "storage", "Decide default store or custom OLLAMA_MODELS before pull."),
        ("runtime_install_scope", "runtime", "Scope installer/PATH/listener proof before pull."),
        ("model_pull_scope", "model", "Scope first model pull/list/tags/show proof before endpoint smoke."),
    ]
    for field, owner, action in required_fields:
        if not display(manifest.get(field)):
            findings.append(finding("hold", owner, f"`{field}` is missing.", field, action))

    require_loopback = bool_value(manifest.get("require_loopback"), True)
    urls = {
        "native_base_url": display(manifest.get("native_base_url") or "http://127.0.0.1:11434"),
        "openai_base_url": display(manifest.get("openai_base_url") or "http://127.0.0.1:11434/v1"),
    }
    security_review = display(manifest.get("security_review_proof"))
    for field, url in urls.items():
        host = parsed_host(url)
        if not host or host in {"0.0.0.0", "::"}:
            findings.append(
                finding(
                    "fail",
                    "security",
                    f"`{field}` is a wildcard or unparsable URL.",
                    url,
                    "Use a loopback URL for the first run.",
                )
            )
        elif require_loopback and not is_loopback_host(host):
            findings.append(
                finding(
                    "fail",
                    "security",
                    f"`{field}` is not loopback while `require_loopback` is true.",
                    url,
                    "Return to loopback or set `require_loopback` false only with security review proof.",
                )
            )
        elif not is_loopback_host(host) and not security_review:
            findings.append(
                finding(
                    "hold",
                    "security",
                    f"`{field}` is not loopback and no security review proof is linked.",
                    url,
                    "Link the security and privacy runbook review before running this plan.",
                )
            )

    destructive_patterns = [
        r"\bRemove-Item\b",
        r"\brm\s+-",
        r"\bdel\s+",
        r"\brmdir\b",
        r"(?m)^\s*format\s+",
        r"\bClear-Content\b",
    ]
    command_text = "\n".join(display(step.get("command")) for step in steps)
    for pattern in destructive_patterns:
        if re.search(pattern, command_text, flags=re.IGNORECASE):
            findings.append(
                finding(
                    "fail",
                    "command-safety",
                    "Generated plan contains a destructive command pattern.",
                    pattern,
                    "Remove the destructive command before using the first-run plan.",
                )
            )

    fail_count = sum(1 for item in findings if item["level"] == "fail")
    hold_count = sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        status = "fail"
        decision = "first_run_command_plan_unsafe"
        next_route = "LLM/Study/Local LLM Security and Privacy Runbook"
    elif hold_count:
        status = "hold"
        decision = "first_run_command_plan_incomplete"
        next_route = "LLM/Study/Local LLM First Run Readiness Snapshot"
    else:
        status = "pass"
        decision = "first_run_command_plan_ready"
        next_route = "LLM/Study/Local LLM Windows First-Run Quickstart"

    return {
        "status": status,
        "decision": decision,
        "next_route": next_route,
        "findings": findings,
        "fail_count": fail_count,
        "hold_count": hold_count,
        "planned_step_count": len(steps),
        "required_step_count": sum(1 for step in steps if step.get("required")),
    }


def md_cell(value: Any) -> str:
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=True, sort_keys=True)
    return display(value).replace("|", "\\|").replace("\n", " ")


def render_markdown(record: dict[str, Any]) -> str:
    result = record["result"]
    lines = [
        f"# Local LLM First Run Command Plan - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Runtime: `{record['runtime']}`",
        f"- Model id: `{record['model_id']}`",
        f"- Run root: `{record['run_root']}`",
        f"- Native base URL: `{record['native_base_url']}`",
        f"- OpenAI-compatible base URL: `{record['openai_base_url']}`",
        f"- Planned steps: `{result['planned_step_count']}`",
        f"- Next route: {wiki_link(result['next_route'])}",
        "",
        "## Findings",
        "",
    ]
    if result["findings"]:
        for item in result["findings"]:
            lines.append(f"- `{item['level']}` `{item['owner']}`: {item['finding']} -> {item['action']}")
    else:
        lines.append("- No blocking findings. Review the generated PowerShell before running it.")

    lines.extend(
        [
            "",
            "## Planned Steps",
            "",
            "| Step | Phase | Required | Evidence | Route | Note |",
            "|---|---|---:|---|---|---|",
        ]
    )
    for step in record["steps"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    md_cell(step["step_id"]),
                    md_cell(step["phase"]),
                    md_cell(step["required"]),
                    md_cell(step["evidence_path"]),
                    md_cell(wiki_link(step["route"])),
                    md_cell(step["note"]),
                ]
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def render_powershell(record: dict[str, Any]) -> str:
    lines = [
        "# Local LLM first-run command plan",
        "# Generated by Local LLM First Run Command Plan Runner.",
        "# Review before running. The planner did not execute these commands.",
        "$ErrorActionPreference = 'Stop'",
        f"$RunId = {ps_quote(record['run_id'])}",
        f"$RunRoot = {ps_quote(record['run_root'])}",
        f"$Runtime = {ps_quote(record['runtime'])}",
        f"$RuntimeBoundary = {ps_quote(record['runtime_boundary'])}",
        f"$ModelId = {ps_quote(record['model_id'])}",
        f"$SourcePage = {ps_quote(record['source_page'])}",
        f"$SourceCheckedAt = {ps_quote(record['source_checked_at'])}",
        f"$ExpectedSourceDigest = {ps_quote(record['expected_source_digest'])}",
        "$SourceRecheckSnippets = @(" + ", ".join(ps_quote(item) for item in record["source_recheck_snippets"] if item) + ")",
        f"$VaultRoot = {ps_quote(record['vault_root'])}",
        f"$NativeBase = {ps_quote(record['native_base_url'].rstrip('/'))}",
        f"$OpenAIBase = {ps_quote(record['openai_base_url'].rstrip('/'))}",
        f"$SecurityBoundary = {ps_quote(record['security_boundary'])}",
        f"$ModelStoreDecision = {ps_quote(record['model_store_decision'])}",
        f"$RuntimeInstallScope = {ps_quote(record['runtime_install_scope'])}",
        f"$ModelPullScope = {ps_quote(record['model_pull_scope'])}",
        "$IncludeOpenAI = $" + str(bool(record["include_openai_route"])).lower(),
        "$IncludeStreaming = $" + str(bool(record["include_streaming"])).lower(),
    ]
    for step in record["steps"]:
        lines.extend(
            [
                "",
                f"# {step['step_id']} | {step['phase']} | evidence: {step['evidence_path']}",
                f"# route: {step['route']}",
                f"# note: {step['note']}",
                step["command"],
            ]
        )
    return "\n".join(lines) + "\n"


def write_steps_csv(path: Path, steps: list[dict[str, Any]]) -> None:
    fieldnames = ["step_id", "phase", "required", "route", "evidence_path", "note", "command"]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for step in steps:
            writer.writerow({field: step.get(field, "") for field in fieldnames})


def output_root_for(manifest_path: Path, manifest: dict[str, Any]) -> Path:
    raw_output = display(manifest.get("output_root") or os.environ.get("LOCAL_LLM_FIRST_RUN_COMMAND_PLAN_OUTPUT_ROOT"))
    if raw_output:
        output_root = Path(raw_output).expanduser()
    else:
        raw_run_root = display(manifest.get("run_root") or os.environ.get("LOCAL_LLM_FIRST_RUN_COMMAND_PLAN_ROOT"))
        output_root = Path(raw_run_root).expanduser() / "first-run-command-plan" if raw_run_root else manifest_path.parent / "first-run-command-plan"
    if not output_root.is_absolute():
        output_root = manifest_path.parent / output_root
    return output_root.resolve()


def main() -> int:
    manifest_path, manifest = load_manifest()
    steps = build_steps(manifest)
    result = evaluate_plan(manifest, steps)

    run_id = display(manifest.get("run_id") or f"{utc_stamp()}-{slug(manifest_path.stem)}")
    output_root = output_root_for(manifest_path, manifest)
    output_dir = output_root / slug(run_id)
    output_dir.mkdir(parents=True, exist_ok=True)

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "manifest_path": str(manifest_path),
        "status": result["status"],
        "decision": result["decision"],
        "run_root": display(manifest.get("run_root")),
        "runtime": display(manifest.get("runtime") or "ollama"),
        "runtime_boundary": display(manifest.get("runtime_boundary")),
        "model_id": display(manifest.get("model_id")),
        "source_page": display(manifest.get("source_page")),
        "source_checked_at": display(manifest.get("source_checked_at")),
        "expected_source_digest": display(manifest.get("expected_source_digest") or manifest.get("expected_digest")),
        "source_recheck_snippets": list_value(manifest.get("source_recheck_snippets")) or [
            display(manifest.get("model_id")),
            display(manifest.get("expected_source_digest")),
        ],
        "vault_root": display(manifest.get("vault_root") or "D:/Vaults/PersonalKB"),
        "native_base_url": display(manifest.get("native_base_url") or "http://127.0.0.1:11434"),
        "openai_base_url": display(manifest.get("openai_base_url") or "http://127.0.0.1:11434/v1"),
        "security_boundary": display(manifest.get("security_boundary")),
        "model_store_decision": display(manifest.get("model_store_decision")),
        "runtime_install_scope": display(manifest.get("runtime_install_scope")),
        "model_pull_scope": display(manifest.get("model_pull_scope")),
        "include_openai_route": bool_value(manifest.get("include_openai_route"), True),
        "include_streaming": bool_value(manifest.get("include_streaming"), False),
        "result": result,
        "steps": steps,
        "outputs": {},
    }

    json_path = output_dir / f"{slug(run_id)}-command-plan.json"
    markdown_path = output_dir / f"{slug(run_id)}-command-plan.md"
    ps1_path = output_dir / f"{slug(run_id)}-command-plan.ps1"
    csv_path = output_dir / f"{slug(run_id)}-command-plan-steps.csv"
    jsonl_path = output_root / "first-run-command-plans.jsonl"
    record["outputs"] = {
        "json": str(json_path),
        "markdown": str(markdown_path),
        "powershell": str(ps1_path),
        "csv": str(csv_path),
        "jsonl": str(jsonl_path),
    }

    json_path.write_text(json.dumps(record, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown(record), encoding="utf-8")
    ps1_path.write_text(render_powershell(record), encoding="utf-8")
    write_steps_csv(csv_path, steps)
    with jsonl_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=True) + "\n")

    print(
        json.dumps(
            {
                "status": record["status"],
                "decision": record["decision"],
                "run_id": run_id,
                "planned_step_count": result["planned_step_count"],
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

Create the manifest:

```powershell
$PlanRoot = "D:\llm-runs\first-local-inference-planning"
New-Item -ItemType Directory -Force -Path $PlanRoot | Out-Null
$Manifest = Join-Path $PlanRoot "first-run-command-plan-manifest.json"

@{
  run_id = "first-local-inference-001"
  run_root = "D:\llm-runs\2026-06-16-first-local-inference"
  output_root = $PlanRoot
  runtime = "ollama"
  runtime_boundary = "Windows native Ollama service"
  model_id = "qwen3.5:4b"
  source_page = "https://ollama.com/library/qwen3.5:4b"
  source_checked_at = "2026-06-16"
  source_recheck_snippets = @("2a654d98e6fb", "3.4GB", "parameters 4.66B", "quantization Q4_K_M")
  native_base_url = "http://127.0.0.1:11434"
  openai_base_url = "http://127.0.0.1:11434/v1"
  security_boundary = "loopback only"
  model_store_decision = "default user profile store accepted"
  runtime_install_scope = "official Windows installer or existing signed install, then new-shell PATH proof"
  model_pull_scope = "pull exactly one baseline tag, then list/tags/show proof"
  require_loopback = $true
  include_openai_route = $true
  include_streaming = $false
} | ConvertTo-Json -Depth 8 | Set-Content $Manifest -Encoding utf8
```

Run the planner:

```powershell
$env:LOCAL_LLM_FIRST_RUN_COMMAND_PLAN_MANIFEST = $Manifest
python .\first-run-command-plan.py
```

Review the generated PowerShell before execution:

```powershell
Get-Content (Join-Path $PlanRoot "first-local-inference-001\first-local-inference-001-command-plan.ps1")
```

## Result Decisions

| Status / decision | Meaning | Next route |
|---|---|---|
| `pass/first_run_command_plan_ready` | Manifest is complete, planned API bases are loopback, and the command plan has no destructive command pattern. | [[LLM/Study/Local LLM Windows First-Run Quickstart]] |
| `hold/first_run_command_plan_incomplete` | Runtime, model id, run root, storage decision, install scope, pull scope, or security-review evidence is missing. | [[LLM/Study/Local LLM First Run Readiness Snapshot]] |
| `fail/first_run_command_plan_unsafe` | Planned URL is wildcard/non-loopback while loopback is required, or the plan contains a destructive command pattern. | [[LLM/Study/Local LLM Security and Privacy Runbook]] |

## Copy Row

| Field | Value |
|---|---|
| Command plan status | pass / hold / fail |
| Planner manifest |  |
| Command plan JSON |  |
| Command plan Markdown |  |
| Command plan PowerShell |  |
| Step CSV |  |
| Run root |  |
| Runtime |  |
| Model id |  |
| Native base URL |  |
| OpenAI-compatible base URL |  |
| First missing layer |  |
| Next route |  |

## Completion Gate

This command-plan output counts only when:

- [ ] manifest names run root, runtime, runtime boundary, model id, source page, source check date, native base, OpenAI-compatible base, security boundary, model-store decision, install scope, and pull scope
- [ ] `require_loopback` remains true for the first run unless a security review is linked
- [ ] generated JSON, Markdown, PowerShell, CSV, and JSONL outputs exist
- [ ] generated PowerShell has been reviewed before execution
- [ ] the generated plan routes to source recheck, runtime install runner, first model pull runner, runtime health, smoke request, first response debrief, endpoint audit, and first inference packet audit
- [ ] the copy row is linked from [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]] or [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]

## References

Internal routes:

- [[LLM/Study/Local LLM First Run Readiness Snapshot]]
- [[LLM/Study/Local LLM Model Store Readiness Snapshot]]
- [[LLM/Study/Local LLM First Model Candidate Ladder]]
- [[LLM/Study/Local LLM First Model Source Recheck Runner]]
- [[LLM/Study/Local LLM Windows First-Run Quickstart]]
- [[LLM/Study/Local LLM Command Cookbook]]
- [[LLM/Study/Local LLM Windows Runtime Install Gate]]
- [[LLM/Study/Local LLM Windows Runtime Install Runner]]
- [[LLM/Study/Local LLM First Model Pull Gate]]
- [[LLM/Study/Local LLM First Model Pull Runner]]
- [[LLM/Study/Local LLM First Runtime Health Runner]]
- [[LLM/Study/Local LLM First Smoke Request Runner]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner]]
- [[LLM/Study/Local LLM First Inference Evidence Pack Audit Runner]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]

External/current sources checked 2026-06-16:

- [Ollama Windows documentation](https://docs.ollama.com/windows)
- [Ollama Windows download](https://ollama.com/download/windows)
- [Ollama quickstart](https://docs.ollama.com/quickstart)
- [Ollama CLI reference](https://docs.ollama.com/cli)
- [Ollama qwen3.5:4b model page](https://ollama.com/library/qwen3.5:4b)
- [Ollama list local models API](https://docs.ollama.com/api/tags)
- [Ollama chat endpoint](https://docs.ollama.com/api/chat)
- [Ollama generate endpoint](https://docs.ollama.com/api/generate)
- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
