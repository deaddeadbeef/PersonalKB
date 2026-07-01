---
tags: [study, llm, local-llm, open-webui, provider, ui, integration, security, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice]
last-verified: 2026-06-16
---

# Local Open WebUI Provider Integration Runner

> **One-line summary** Prove Open WebUI is connected to the intended local provider, model, storage, and network boundary before a UI chat transcript is allowed to support app, security, lifecycle, or capstone claims.

Use this after [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner|Local LLM OpenAI-Compatible API Contract Runner]], [[LLM/Study/Local llama.cpp GGUF Server Runner|Local llama.cpp GGUF Server Runner]], or [[LLM/Study/Local LLM Docker GPU Container Serving Lab|Local LLM Docker GPU Container Serving Lab]] proves the provider endpoint. Use it before [[LLM/Study/Local LLM Application Integration Evidence Runner|Local LLM Application Integration Evidence Runner]], [[LLM/Study/Local LLM Security and Privacy Runner|Local LLM Security and Privacy Runner]], [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook|Local LLM Service Lifecycle and Upgrade Runbook]], [[LLM/Study/Local LLM Result Synthesis Runner|Local LLM Result Synthesis Runner]], or [[LLM/Study/Local LLM Capstone Project Blueprint|Local LLM Capstone Project Blueprint]] when Open WebUI is part of the user-facing local LLM path.

This runner does not start Open WebUI, click the browser, or send a live model request. It audits saved evidence: UI install identity, bind address, provider base URL, model visibility, connection proof, chat transcript, persistent data path, secret-key management proof, logs, redacted config, and handoffs to endpoint/security/lifecycle/app evidence.

Open WebUI is a UI and provider router, not endpoint proof. Do not use an Open WebUI transcript to prove that a local provider loaded the right model. First prove the provider from the host with direct endpoint evidence such as `/v1/models`, `/v1/chat/completions`, `llama.cpp` `/health`, or the Docker provider proof, then use this runner to prove the UI layer is pointed at that provider.

## Official Anchors

- Open WebUI describes itself as a self-hosted AI platform that can operate offline and supports Ollama plus OpenAI-compatible APIs: [Open WebUI docs](https://docs.openwebui.com/).
- The Docker quick start publishes the UI on host port 3000, mounts persistent data at `/app/backend/data`, and says WebSocket support is required: [Open WebUI quick start](https://docs.openwebui.com/getting-started/quick-start/).
- The quick start warns that a persistent `WEBUI_SECRET_KEY` prevents logout and token decryption problems after container recreation: [Open WebUI quick start](https://docs.openwebui.com/getting-started/quick-start/).
- The OpenAI-compatible provider guide routes local servers such as llama.cpp, LM Studio, vLLM, LocalAI, and Docker Model Runner through provider base URLs and model detection: [OpenAI-compatible provider setup](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-openai-compatible/).
- The hardening guide covers API keys, route restrictions, roles, database choices, and the need to protect data and credentials: [Open WebUI hardening](https://docs.openwebui.com/getting-started/advanced-topics/hardening/).
- The FAQ says context-length failures come from the model provider rather than Open WebUI, which matters when triaging UI-visible errors: [Open WebUI FAQ](https://docs.openwebui.com/faq/).
- The upstream README repeats the persistent data-volume warning and `host.docker.internal` Docker connection pattern: [Open WebUI GitHub README](https://github.com/open-webui/open-webui).

## What This Proves

| Evidence family | Checks | Why it matters |
|---|---|---|
| Open WebUI identity | install method, image tag or version, base URL, host, port | distinguishes the active UI from a stale container, desktop app, or old Python service |
| Exposure boundary | loopback bind by default, non-loopback approval if shared | prevents private prompts, files, and admin surfaces from becoming LAN or public services by accident |
| Provider route | provider type, provider base URL, expected model id, direct endpoint proof | keeps the UI from hiding wrong-model, wrong-port, cloud-route, or stale-provider mistakes |
| Model visibility | saved model list from the UI or provider connection panel | proves the intended model is selectable before a transcript is trusted |
| Chat transcript | harmless prompt and assistant text from the expected model | proves the user-facing path works without using it as quality evidence |
| Persistent state | Open WebUI data volume/path, backup plan, version pin | makes chats, users, provider config, and rollback state auditable |
| Secret handling | `WEBUI_SECRET_KEY` proof without recording the value, redacted configs/logs | prevents vault notes from becoming a secret store |
| Handoffs | endpoint, security, lifecycle, app integration, result synthesis | connects the UI run to the rest of the local LLM evidence chain |

Academic bridge: the same model endpoint can behave differently once a UI adds chat history, tools, RAG files, system prompts, provider filters, context limits, auth, exports, and persistent storage. A local LLM is a system, not just a model process.

## Manual Evidence Capture

Start with a run folder:

```powershell
$RunRoot = Join-Path $HOME ("Documents\local-llm-runs\" + (Get-Date -Format "yyyy-MM-dd-HHmm") + "-open-webui-provider")
New-Item -ItemType Directory -Force -Path $RunRoot | Out-Null
```

Prefer a loopback publish for a personal workstation:

```powershell
docker run -d `
  -p 127.0.0.1:3000:8080 `
  --add-host=host.docker.internal:host-gateway `
  --env-file .env.open-webui `
  -v open-webui:/app/backend/data `
  --name open-webui `
  --restart always `
  ghcr.io/open-webui/open-webui:<pinned-tag>
```

Use a local env file, not a vault note, for secrets:

```dotenv
WEBUI_SECRET_KEY=<set locally, do not record in the vault>
```

Common local provider URL shapes:

| Provider position | Base URL shape | Notes |
|---|---|---|
| Provider on host, Open WebUI in Docker | `http://host.docker.internal:11434/v1` or provider port | works for host services reached from a container |
| Provider in the same Compose network | `http://provider-service:8000/v1` | service name is local to the Compose network |
| Open WebUI and provider both on host | `http://127.0.0.1:<port>/v1` | safest for desktop/pip installs |
| Provider on LAN | `http://192.168.x.y:<port>/v1` | requires explicit boundary, auth, and firewall proof |
| Cloud provider | `https://...` | not a local-LLM proof path unless explicitly approved and labeled hybrid |

Capture enough evidence to run the audit:

```powershell
docker ps --filter "name=open-webui" --no-trunc | Tee-Object -FilePath "$RunRoot\docker-ps.txt"
docker logs --tail 200 open-webui | Tee-Object -FilePath "$RunRoot\open-webui-log-tail.txt"

# Save a redacted Compose file, redacted env inventory, provider connection screenshot or JSON export,
# model-list evidence, and one harmless transcript from the UI.
```

Harmless prompt for the UI transcript:

```text
Reply with exactly: local llm ok
```

Do not paste raw API keys, raw `WEBUI_SECRET_KEY`, private chat exports, private RAG files, cookies, session tokens, or admin passwords into the vault. Record that they exist and where they are managed.

## Manifest Shape

Save `open-webui-provider-manifest.json` next to the runner:

```json
{
  "run_id": "open-webui-provider-001",
  "run_root": "D:/llm-runs/open-webui-provider",
  "vault_root": "D:/Vaults/PersonalKB",
  "webui": {
    "base_url": "http://127.0.0.1:3000",
    "host": "127.0.0.1",
    "port": 3000,
    "install_method": "docker",
    "image_or_version": "ghcr.io/open-webui/open-webui:<tag>",
    "data_path_or_volume": "open-webui:/app/backend/data",
    "secret_key_proof": "env file has WEBUI_SECRET_KEY set; value not recorded",
    "backup_plan": "docker volume backup before upgrade"
  },
  "provider": {
    "type": "llama.cpp",
    "base_url": "http://host.docker.internal:10000/v1",
    "expected_model": "local-gguf-baseline",
    "public_provider_approval": ""
  },
  "security": {
    "boundary": "loopback",
    "non_loopback_approval": "",
    "export_boundary": "local-only",
    "prompt_storage": "Open WebUI data volume",
    "log_retention": "local run folder only",
    "secrets_allowed_in_files": false
  },
  "artifacts": {
    "provider_endpoint_proof": "openai-contract-results.json",
    "security_privacy_proof": "security-privacy-results.json",
    "application_integration_proof": "",
    "lifecycle_proof": "",
    "connection_proof": "connection-proof.json",
    "model_visibility_json": "models.json",
    "chat_transcript_json": "chat-transcript.json",
    "container_or_process_artifact": "docker-ps.txt",
    "config_artifacts": ["compose.yml", ".env.open-webui.redacted"],
    "log_artifacts": ["open-webui-log-tail.txt"]
  },
  "expected_text": "local llm ok",
  "require_application_integration": false,
  "require_lifecycle": false
}
```

Result semantics:

| Decision | Meaning | Next move |
|---|---|---|
| `pass/open_webui_provider_ready` | UI identity, boundary, provider proof, expected model, transcript, persistence, and secret handling are all evidenced. | Use the transcript in app integration, lifecycle, or capstone evidence. |
| `hold/open_webui_provider_incomplete` | Required evidence is missing or ambiguous but no dangerous boundary was proven. | Fill the missing artifact and rerun without changing unrelated layers. |
| `fail/open_webui_provider_blocked` | The UI is exposed unsafely, points to a public provider without approval, misses the expected model, contains raw secrets, or has failed upstream proof. | Fix that layer before trusting UI output. |

## Standard-Library Runner

Save this as `local_open_webui_provider_integration_runner.py` inside the run folder, or extract it from this note. It uses only Python's standard library.

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
from urllib.parse import urlparse
import ipaddress


LOOPBACK_HOSTS = {"127.0.0.1", "localhost", "::1"}
CONTAINER_HOSTS = {"host.docker.internal", "host.containers.internal"}
PASS_WORDS = {"pass", "passed", "ready", "compatible", "ok", "open_webui_provider_ready"}
HOLD_WORDS = {"hold", "held", "partial", "incomplete", "unknown", "pending"}
FAIL_WORDS = {"fail", "failed", "error", "blocked", "unsafe", "not-compatible", "not_compatible"}

SECRET_PATTERNS = [
    ("authorization_bearer", re.compile(r"(?i)(authorization\s*:\s*bearer\s+)([A-Za-z0-9._\-+/=]{8,})")),
    ("named_api_key", re.compile(r"(?i)\b([A-Z0-9_]*(?:API|AUTH|ACCESS)[_-]?KEY)\b\s*[:=]\s*([^\s#\"']{8,})")),
    ("webui_secret", re.compile(r"(?i)\b(WEBUI_SECRET_KEY|WEBUI_JWT_SECRET_KEY|OPENAI_API_KEY|HF_TOKEN|HUGGING_FACE_HUB_TOKEN)\b\s*[:=]\s*([^\s#\"']{8,})")),
    ("password_or_token", re.compile(r"(?i)\b(password|passwd|token|secret)\b\s*[:=]\s*([^\s#\"']{8,})")),
]


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def clean(value: Any) -> str:
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


def as_bool(value: Any, default: bool = False) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() not in {"0", "false", "no", "off", ""}
    return bool(value)


def add_check(checks: list[dict[str, Any]], status: str, gate: str, message: str, evidence: str = "") -> None:
    checks.append({"status": status, "gate": gate, "message": message, "evidence": evidence})


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8-sig") as handle:
        return json.load(handle)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def md_cell(value: Any) -> str:
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=True)
    return clean(value).replace("|", "\\|").replace("\n", " ")


def iter_artifact_values(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value] if value.strip() else []
    if isinstance(value, (list, tuple)):
        result: list[str] = []
        for item in value:
            result.extend(iter_artifact_values(item))
        return result
    return [str(value)]


def resolve_artifact(raw: str, manifest_dir: Path, run_root: Path | None, vault_root: Path | None) -> Path | None:
    text = clean(raw)
    if not text:
        return None
    text = text.strip()
    open_link = "[" * 2
    close_link = "]" * 2
    if text.startswith(open_link) and text.endswith(close_link):
        text = text[2:-2].split("|", 1)[0]
        if not text.lower().endswith(".md"):
            text += ".md"
    text = text.replace("\\", os.sep).replace("/", os.sep)
    candidate = Path(text).expanduser()
    candidates = [candidate] if candidate.is_absolute() else []
    if not candidate.is_absolute():
        candidates.append(manifest_dir / candidate)
        if run_root:
            candidates.append(run_root / candidate)
        if vault_root:
            candidates.append(vault_root / candidate)
    for item in candidates:
        if item.exists():
            return item
    return candidates[0] if candidates else None


def parse_host_from_url(url: str) -> str:
    parsed = urlparse(url)
    return clean(parsed.hostname or "")


def classify_host(host_or_url: str) -> dict[str, str]:
    text = clean(host_or_url)
    host = parse_host_from_url(text) or text
    host = host.strip("[]").lower()
    if not host:
        return {"host": "", "class": "missing"}
    if host in LOOPBACK_HOSTS:
        return {"host": host, "class": "loopback"}
    if host in CONTAINER_HOSTS:
        return {"host": host, "class": "container-host"}
    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        if "." not in host:
            return {"host": host, "class": "compose-service"}
        if host.endswith(".local") or host.endswith(".lan"):
            return {"host": host, "class": "private-lan"}
        return {"host": host, "class": "public"}
    if ip.is_loopback:
        return {"host": host, "class": "loopback"}
    if ip.is_private or ip.is_link_local:
        return {"host": host, "class": "private-lan"}
    if ip.is_global:
        return {"host": host, "class": "public"}
    return {"host": host, "class": "unknown"}


def status_from_text(value: Any) -> str:
    text = clean(value).lower()
    if not text:
        return ""
    if text in PASS_WORDS:
        return "pass"
    if text in HOLD_WORDS:
        return "hold"
    if text in FAIL_WORDS:
        return "fail"
    if "blocked" in text or "not-compatible" in text or "error" in text:
        return "fail"
    if "incomplete" in text or "partial" in text or "hold" in text:
        return "hold"
    if "ready" in text or "pass" in text or "compatible" in text:
        return "pass"
    return ""


def extract_status(data: Any) -> str:
    if isinstance(data, dict):
        for key in ("status", "decision", "result", "verdict", "gate", "outcome"):
            status = status_from_text(data.get(key))
            if status:
                return status
        for value in data.values():
            status = extract_status(value)
            if status:
                return status
    elif isinstance(data, list):
        statuses = [extract_status(item) for item in data]
        statuses = [item for item in statuses if item]
        if "fail" in statuses:
            return "fail"
        if "hold" in statuses:
            return "hold"
        if "pass" in statuses:
            return "pass"
    return ""


def collect_model_ids(data: Any) -> set[str]:
    ids: set[str] = set()
    if isinstance(data, dict):
        for key in ("id", "model", "model_id", "name"):
            value = data.get(key)
            if isinstance(value, str) and value.strip():
                ids.add(value.strip())
        for key in ("data", "models", "model_list"):
            if key in data:
                ids.update(collect_model_ids(data[key]))
        for value in data.values():
            if isinstance(value, (dict, list)):
                ids.update(collect_model_ids(value))
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, str) and item.strip():
                ids.add(item.strip())
            elif isinstance(item, (dict, list)):
                ids.update(collect_model_ids(item))
    return ids


def collect_text(data: Any) -> list[str]:
    texts: list[str] = []
    if isinstance(data, str):
        if data.strip():
            texts.append(data.strip())
    elif isinstance(data, dict):
        for key in ("content", "response", "output", "output_text", "text"):
            value = data.get(key)
            if isinstance(value, str) and value.strip():
                texts.append(value.strip())
        for value in data.values():
            if isinstance(value, (dict, list, str)):
                texts.extend(collect_text(value))
    elif isinstance(data, list):
        for item in data:
            texts.extend(collect_text(item))
    return texts


def read_text_limited(path: Path, limit: int = 2_000_000) -> str:
    data = path.read_bytes()[:limit]
    return data.decode("utf-8", errors="replace")


def scan_secret_file(path: Path) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    text = read_text_limited(path)
    for number, line in enumerate(text.splitlines(), start=1):
        if "redacted" in line.lower() or "<set locally" in line.lower():
            continue
        for name, pattern in SECRET_PATTERNS:
            if pattern.search(line):
                findings.append({"kind": name, "path": str(path), "line": str(number)})
    return findings


def audit_manifest(manifest_path: Path) -> dict[str, Any]:
    manifest_dir = manifest_path.parent
    manifest = load_json(manifest_path)
    run_root = Path(clean(manifest.get("run_root"))).expanduser() if clean(manifest.get("run_root")) else manifest_dir
    vault_root = Path(clean(manifest.get("vault_root"))).expanduser() if clean(manifest.get("vault_root")) else None
    webui = manifest.get("webui") or {}
    provider = manifest.get("provider") or {}
    security = manifest.get("security") or {}
    artifacts = manifest.get("artifacts") or {}
    checks: list[dict[str, Any]] = []

    webui_url = clean(webui.get("base_url"))
    webui_host = clean(webui.get("host")) or webui_url
    webui_class = classify_host(webui_host)
    if not webui_url:
        add_check(checks, "hold", "webui_identity", "Open WebUI base_url is missing")
    else:
        add_check(checks, "pass", "webui_identity", "Open WebUI base_url is recorded", webui_url)
    for field in ("install_method", "image_or_version", "data_path_or_volume", "backup_plan"):
        if nonempty(webui.get(field)):
            add_check(checks, "pass", "webui_identity", f"webui.{field} is recorded", clean(webui.get(field)))
        else:
            add_check(checks, "hold", "webui_identity", f"webui.{field} is missing")

    approval = clean(security.get("non_loopback_approval"))
    if webui_class["class"] == "loopback":
        add_check(checks, "pass", "webui_boundary", "Open WebUI host is loopback", webui_class["host"])
    elif webui_class["class"] in {"private-lan", "public", "unknown", "missing"} and not approval:
        add_check(checks, "fail", "webui_boundary", "Open WebUI host is not loopback and no approval is recorded", json.dumps(webui_class))
    else:
        add_check(checks, "hold", "webui_boundary", "Open WebUI host is non-loopback; approval must be reviewed", json.dumps(webui_class))

    secret_proof = clean(webui.get("secret_key_proof"))
    if secret_proof and re.search(r"(?i)WEBUI_SECRET_KEY", secret_proof) and not re.search(r"(?i)(value not recorded|redacted|not record|secret store)", secret_proof):
        add_check(checks, "hold", "secret_key", "WEBUI_SECRET_KEY proof exists but does not say the value was withheld", secret_proof)
    elif secret_proof:
        add_check(checks, "pass", "secret_key", "WEBUI_SECRET_KEY management proof is recorded without the value", secret_proof)
    else:
        add_check(checks, "hold", "secret_key", "WEBUI_SECRET_KEY management proof is missing")

    provider_url = clean(provider.get("base_url"))
    expected_model = clean(provider.get("expected_model"))
    provider_class = classify_host(provider_url)
    if not provider_url:
        add_check(checks, "hold", "provider_route", "provider.base_url is missing")
    elif provider_class["class"] == "public" and not clean(provider.get("public_provider_approval")):
        add_check(checks, "fail", "provider_route", "provider base URL appears public and has no hybrid/cloud approval", provider_url)
    elif provider_class["class"] in {"loopback", "container-host", "compose-service", "private-lan"}:
        add_check(checks, "pass", "provider_route", "provider route is local or explicitly reachable from the UI boundary", json.dumps(provider_class))
    else:
        add_check(checks, "hold", "provider_route", "provider route class is ambiguous", json.dumps(provider_class))
    if expected_model:
        add_check(checks, "pass", "provider_route", "expected provider model is recorded", expected_model)
    else:
        add_check(checks, "hold", "provider_route", "provider.expected_model is missing")

    required_proofs = {
        "provider_endpoint_proof": "endpoint proof",
        "security_privacy_proof": "security/privacy proof",
    }
    if as_bool(manifest.get("require_application_integration")):
        required_proofs["application_integration_proof"] = "application integration proof"
    if as_bool(manifest.get("require_lifecycle")):
        required_proofs["lifecycle_proof"] = "lifecycle proof"

    for key, label in required_proofs.items():
        path = resolve_artifact(clean(artifacts.get(key)), manifest_dir, run_root, vault_root)
        if not path or not path.exists():
            add_check(checks, "hold", "linked_proof", f"{label} artifact is missing", clean(artifacts.get(key)))
            continue
        status = ""
        if path.suffix.lower() == ".json":
            try:
                status = extract_status(load_json(path))
            except Exception as exc:
                add_check(checks, "hold", "linked_proof", f"{label} JSON could not be parsed: {exc}", str(path))
                continue
        else:
            status = status_from_text(read_text_limited(path, 200_000))
        if status == "pass":
            add_check(checks, "pass", "linked_proof", f"{label} is passing", str(path))
        elif status == "fail":
            add_check(checks, "fail", "linked_proof", f"{label} is failing", str(path))
        else:
            add_check(checks, "hold", "linked_proof", f"{label} is missing a passing decision", str(path))

    connection_path = resolve_artifact(clean(artifacts.get("connection_proof")), manifest_dir, run_root, vault_root)
    if connection_path and connection_path.exists():
        add_check(checks, "pass", "ui_connection", "provider connection proof artifact exists", str(connection_path))
    else:
        add_check(checks, "hold", "ui_connection", "provider connection proof artifact is missing", clean(artifacts.get("connection_proof")))

    model_path = resolve_artifact(clean(artifacts.get("model_visibility_json")), manifest_dir, run_root, vault_root)
    if not model_path or not model_path.exists():
        add_check(checks, "hold", "model_visibility", "model visibility artifact is missing", clean(artifacts.get("model_visibility_json")))
        model_ids: set[str] = set()
    else:
        try:
            model_ids = collect_model_ids(load_json(model_path))
            if expected_model and expected_model in model_ids:
                add_check(checks, "pass", "model_visibility", "expected model is visible in saved model list", expected_model)
            elif expected_model:
                add_check(checks, "fail", "model_visibility", "expected model is absent from saved model list", ", ".join(sorted(model_ids)))
            else:
                add_check(checks, "hold", "model_visibility", "model list exists but expected_model is missing from manifest", str(model_path))
        except Exception as exc:
            model_ids = set()
            add_check(checks, "hold", "model_visibility", f"model visibility JSON could not be parsed: {exc}", str(model_path))

    transcript_path = resolve_artifact(clean(artifacts.get("chat_transcript_json")), manifest_dir, run_root, vault_root)
    expected_text = clean(manifest.get("expected_text")).lower()
    if not transcript_path or not transcript_path.exists():
        add_check(checks, "hold", "chat_transcript", "chat transcript artifact is missing", clean(artifacts.get("chat_transcript_json")))
        transcript_text = ""
    else:
        try:
            if transcript_path.suffix.lower() == ".json":
                transcript_text = "\n".join(collect_text(load_json(transcript_path)))
            else:
                transcript_text = read_text_limited(transcript_path, 500_000)
            if not transcript_text.strip():
                add_check(checks, "hold", "chat_transcript", "chat transcript contains no assistant text", str(transcript_path))
            elif expected_text and expected_text not in transcript_text.lower():
                add_check(checks, "hold", "chat_transcript", "chat transcript exists but expected text was not found", str(transcript_path))
            else:
                add_check(checks, "pass", "chat_transcript", "chat transcript has assistant text from the UI path", str(transcript_path))
        except Exception as exc:
            transcript_text = ""
            add_check(checks, "hold", "chat_transcript", f"chat transcript could not be parsed: {exc}", str(transcript_path))

    for group in ("config_artifacts", "log_artifacts"):
        for raw in iter_artifact_values(artifacts.get(group)):
            path = resolve_artifact(raw, manifest_dir, run_root, vault_root)
            if not path or not path.exists():
                add_check(checks, "hold", "artifact_inventory", f"{group} item is missing", raw)
                continue
            add_check(checks, "pass", "artifact_inventory", f"{group} item exists", str(path))
            if not as_bool(security.get("secrets_allowed_in_files"), False):
                leaks = scan_secret_file(path)
                if leaks:
                    add_check(checks, "fail", "secret_scan", "raw secret-like value found in config/log artifact", json.dumps(leaks))
    process_artifact = resolve_artifact(clean(artifacts.get("container_or_process_artifact")), manifest_dir, run_root, vault_root)
    if process_artifact and process_artifact.exists():
        add_check(checks, "pass", "artifact_inventory", "container or process artifact exists", str(process_artifact))
    else:
        add_check(checks, "hold", "artifact_inventory", "container or process artifact is missing", clean(artifacts.get("container_or_process_artifact")))

    if clean(security.get("export_boundary")).lower() in {"local-only", "local", "offline"}:
        add_check(checks, "pass", "privacy_boundary", "export boundary is local-only", clean(security.get("export_boundary")))
    else:
        add_check(checks, "hold", "privacy_boundary", "export boundary is missing or not local-only", clean(security.get("export_boundary")))
    if clean(security.get("prompt_storage")):
        add_check(checks, "pass", "privacy_boundary", "prompt storage location is recorded", clean(security.get("prompt_storage")))
    else:
        add_check(checks, "hold", "privacy_boundary", "prompt storage location is missing")

    statuses = {item["status"] for item in checks}
    if "fail" in statuses:
        status = "fail"
        decision = "open_webui_provider_blocked"
    elif "hold" in statuses:
        status = "hold"
        decision = "open_webui_provider_incomplete"
    else:
        status = "pass"
        decision = "open_webui_provider_ready"

    return {
        "run_id": clean(manifest.get("run_id")) or manifest_path.stem,
        "generated_at": now_iso(),
        "manifest": str(manifest_path),
        "status": status,
        "decision": decision,
        "webui_host_class": webui_class,
        "provider_host_class": provider_class,
        "expected_model": expected_model,
        "visible_models": sorted(model_ids),
        "checks": checks,
    }


def write_outputs(result: dict[str, Any], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    stem = "open-webui-provider-results"
    write_json(output_dir / f"{stem}.json", result)
    with (output_dir / f"{stem}.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["status", "gate", "message", "evidence"])
        writer.writeheader()
        writer.writerows(result["checks"])
    with (output_dir / f"{stem}.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(result, ensure_ascii=True) + "\n")
    lines = [
        f"# Open WebUI Provider Results: {result['status']} / {result['decision']}",
        "",
        f"- Run id: {result['run_id']}",
        f"- Generated: {result['generated_at']}",
        f"- Expected model: {result.get('expected_model') or ''}",
        f"- Visible models: {', '.join(result.get('visible_models') or [])}",
        "",
        "| Status | Gate | Message | Evidence |",
        "|---|---|---|---|",
    ]
    for item in result["checks"]:
        lines.append(f"| {md_cell(item['status'])} | {md_cell(item['gate'])} | {md_cell(item['message'])} | {md_cell(item.get('evidence', ''))} |")
    (output_dir / f"{stem}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    manifest_path = Path(argv[1]).expanduser() if len(argv) > 1 else Path("open-webui-provider-manifest.json")
    if not manifest_path.exists():
        print(f"Manifest not found: {manifest_path}", file=sys.stderr)
        return 2
    result = audit_manifest(manifest_path)
    output_dir = Path(os.environ.get("OPEN_WEBUI_PROVIDER_OUTPUT_DIR", "")).expanduser() if os.environ.get("OPEN_WEBUI_PROVIDER_OUTPUT_DIR") else manifest_path.parent
    write_outputs(result, output_dir)
    print(json.dumps({"status": result["status"], "decision": result["decision"], "output_dir": str(output_dir)}, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
```

## Verification Fixtures

Use small local fixture files before trusting the runner:

| Fixture | Expected decision |
|---|---|
| Loopback Open WebUI, local provider, passing endpoint/security JSON, expected model in `models.json`, harmless transcript with expected text | `pass/open_webui_provider_ready` |
| Open WebUI bound to `0.0.0.0` or LAN host with no approval | `fail/open_webui_provider_blocked` |
| Missing `WEBUI_SECRET_KEY` proof | `hold/open_webui_provider_incomplete` |
| Expected model absent from model visibility artifact | `fail/open_webui_provider_blocked` |
| Transcript exists but does not contain the expected harmless text | `hold/open_webui_provider_incomplete` |
| Redacted config passes, but raw `WEBUI_SECRET_KEY=` or `OPENAI_API_KEY=` value in a named config/log artifact fails when `secrets_allowed_in_files` is false | `fail/open_webui_provider_blocked` |

## Result Interpretation

If the runner passes, the UI layer can be used as an evidence source for a user-facing local LLM. It still does not prove model quality, benchmark performance, RAG grounding, tool safety, or deployment readiness.

If it holds, fill the missing artifact. Do not change the model, quantization, prompt, or provider until the missing UI proof is clear.

If it fails, fix the failed boundary first. Common fixes are rebinding the UI to loopback, replacing a public provider URL with the intended local route, proving the provider endpoint directly, adding a persistent data volume, recording `WEBUI_SECRET_KEY` management without the value, or redacting config/log artifacts.

## Handoff Map

| Need | Next note |
|---|---|
| Provider endpoint proof | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]] |
| llama.cpp GGUF endpoint proof | [[LLM/Study/Local llama.cpp GGUF Server Runner]] |
| Containerized provider and UI proof | [[LLM/Study/Local LLM Docker GPU Container Serving Lab]] |
| UI/app workflow proof | [[LLM/Study/Local LLM Application Integration Evidence Runner]] |
| Secret, exposure, export, RAG/tool boundary proof | [[LLM/Study/Local LLM Security and Privacy Runner]] |
| Logs, metrics, resource pressure, route state | [[LLM/Study/Local LLM Observability and Operations Runner]] |
| Version pin, backup, upgrade, rollback | [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook]] |
| Final keep/tune/reject/deploy decision | [[LLM/Study/Local LLM Result Synthesis Runner]] |
| End-to-end project | [[LLM/Study/Local LLM Capstone Project Blueprint]] |

## References

- [Open WebUI docs](https://docs.openwebui.com/)
- [Open WebUI quick start](https://docs.openwebui.com/getting-started/quick-start/)
- [OpenAI-compatible provider setup](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-openai-compatible/)
- [Open WebUI environment configuration](https://docs.openwebui.com/reference/env-configuration/)
- [Open WebUI hardening](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)
- [Open WebUI FAQ](https://docs.openwebui.com/faq/)
- [Open WebUI GitHub README](https://github.com/open-webui/open-webui)
