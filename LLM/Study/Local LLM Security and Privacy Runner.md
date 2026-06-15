---
tags: [study, llm, local-llm, security, privacy, exposure, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice, deep-dive]
last-verified: 2026-06-15
---

# Local LLM Security and Privacy Runner

> **One-line summary** Capture a no-generation security and privacy evidence packet for a local LLM service before trusting logs, RAG data, tools, UI storage, or any non-loopback exposure.

Use this after [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] defines the manual checklist. Use it before exposing Ollama, LM Studio, vLLM, SGLang, llama.cpp, Open WebUI, or a compatible proxy beyond one-person loopback use. If Open WebUI is the UI path, pair it with [[LLM/Study/Local Open WebUI Provider Integration Runner|Local Open WebUI Provider Integration Runner]] so provider routing, persistence, and secret-key proof are checked alongside exposure and export boundaries. If RAG content is untrusted, uploaded, external, private, or tool-adjacent, pair it with [[LLM/Study/Local RAG Prompt Injection and Source Boundary Runner|Local RAG Prompt Injection and Source Boundary Runner]] so the retrieved text cannot silently become instructions. Use it again after a restart, upgrade, cache move, UI change, RAG corpus change, tool integration, reverse proxy change, or tunnel setup.

This runner does not send a generation request. It only checks endpoint shape, host exposure, read-only model-list routes, optional Ollama state routes, config/log evidence, RAG/tool path boundaries, UI/export boundaries, and obvious secret leaks in local files you explicitly name.

Official anchors:

- Ollama binds to `127.0.0.1:11434` by default and uses `OLLAMA_HOST` to change the bind address: [Ollama FAQ](https://docs.ollama.com/faq).
- LM Studio says serving on a non-localhost address exposes the server beyond localhost and recommends authentication: [LM Studio serve on local network](https://lmstudio.ai/docs/developer/core/server/serve-on-network).
- vLLM documents that `--api-key` protects OpenAI-compatible paths but does not secure every sensitive endpoint on the same server: [vLLM security](https://docs.vllm.ai/en/latest/usage/security/).
- Open WebUI uses `WEBUI_SECRET_KEY` for JWT signing and sensitive data encryption, and hardened deployments should protect the data directory and audit logs: [Open WebUI environment reference](https://docs.openwebui.com/reference/env-configuration/) and [Open WebUI hardening](https://docs.openwebui.com/getting-started/advanced-topics/hardening/).
- vLLM warns that allowing local media paths lets requests read server-side media files and should only be used in trusted environments: [vLLM serve CLI](https://docs.vllm.ai/en/v0.19.1/cli/serve/).

## What This Proves

| Evidence | Proves | Does not prove |
|---|---|---|
| Manifest | The intended exposure, model, RAG roots, tool roots, UI data paths, config files, log files, and export boundary are explicit. | That the policy is complete for a production or regulated deployment. |
| Host classification | The configured base URLs are loopback, LAN/private, wildcard, hostname, or public. | That a firewall or reverse proxy is correctly configured. |
| `/v1/models` and optional Ollama routes | The read-only route exposes the expected model id without generation. | That chat completions, tools, streaming, or quality work. |
| Config/log source inventory | Named files exist, have size/hash metadata, and can be scanned locally. | That every relevant file on the machine was discovered. |
| Secret scan | Obvious bearer tokens, API keys, passwords, and WebUI/HF/OpenAI keys are not present in scanned text. | That all secrets or private prompts are absent; scanners are conservative. |
| RAG/tool/UI/export boundaries | Private corpora, allowed tool roots, UI data paths, and export policy are named before use. | That prompt injection, access control, or sandboxing is fully solved. |
| JSON/CSV/Markdown/JSONL output | The decision can feed the capstone workbook, deployment matrix, lifecycle runner, and operations runner. | Long-run incident response, penetration testing, or compliance sign-off. |

Academic bridge: security is part of inference, not a separate afterthought. The model server, prompt assembly, retrieval corpus, tool loop, UI database, logs, and export path all become part of the deployed system. A local model can keep data private only if the endpoint, storage, logs, and tools keep the boundary private too.

## Manifest Contract

Save a manifest such as `security-privacy-manifest.json` next to the runner. Use empty arrays for features that are intentionally not used; leave nothing implicit.

```json
{
  "service": "ollama-local",
  "runtime": "ollama",
  "base_url": "http://127.0.0.1:11434/v1",
  "native_api_url": "http://127.0.0.1:11434/api",
  "expected_model": "qwen3",
  "allowed_hosts": ["127.0.0.1", "localhost", "::1"],
  "intended_exposure": "loopback",
  "authentication_required": false,
  "rag_roots": ["D:\\PrivateCorpus"],
  "tool_allowed_roots": ["D:\\SafeTools"],
  "ui_data_paths": ["D:\\OpenWebUI\\data"],
  "config_paths": ["D:\\LLM-Runs\\compose.yml"],
  "log_paths": ["D:\\LLM-Runs\\server.log"],
  "secrets_allowed_in_files": false,
  "export_boundary": "local-only",
  "notes": "No LAN exposure; no public tunnel; scanned config and log are local copies."
}
```

## Fixed Conditions

Write these before running:

| Field | Value |
|---|---|
| Run folder |  |
| Runtime | Ollama / LM Studio / llama.cpp / vLLM / SGLang / Open WebUI / other |
| Base URL |  |
| Native API URL |  |
| Expected model id |  |
| Intended exposure | loopback / LAN / public / tunnel / unknown |
| Allowed hosts |  |
| Authentication requirement | not needed on loopback / required for LAN / required for public / unknown |
| Config files scanned |  |
| Log files scanned |  |
| RAG corpus roots |  |
| Tool allowed roots |  |
| UI data paths |  |
| Export boundary | local-only / LAN / cloud / unknown |
| Next gate | endpoint smoke / API contract / quality / observability / lifecycle / deployment |

If the intended exposure is LAN, public, tunnel, or shared-host, `LOCAL_LLM_REQUIRE_LOOPBACK=1` should hold or error until the reason, auth, firewall/proxy rule, and logging policy are explicit.

## Standard-Library Runner

Save this as `security-privacy-runner.py` inside the run folder. It uses only Python's standard library.

```python
import csv
import hashlib
import ipaddress
import json
import os
import platform
import re
import socket
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


SECRET_PATTERNS = [
    (
        "authorization_bearer",
        re.compile(r"(?i)(authorization\s*:\s*bearer\s+)([A-Za-z0-9._\-+/=]{8,})"),
    ),
    (
        "named_api_key",
        re.compile(r"(?i)\b([A-Z0-9_]*(?:API|AUTH|ACCESS)[_-]?KEY)\b\s*[:=]\s*([^\s#\"']{8,})"),
    ),
    (
        "hf_or_webui_secret",
        re.compile(
            r"(?i)\b(HF_TOKEN|HUGGING_FACE_HUB_TOKEN|OPENAI_API_KEY|VLLM_API_KEY|WEBUI_SECRET_KEY|WEBUI_JWT_SECRET_KEY|OAUTH_[A-Z0-9_]*KEY)\b\s*[:=]\s*([^\s#\"']{8,})"
        ),
    ),
    (
        "password_or_token",
        re.compile(r"(?i)\b(password|passwd|token|secret)\b\s*[:=]\s*([^\s#\"']{8,})"),
    ),
]

EXPOSURE_LABELS = {"loopback", "lan", "public", "tunnel", "shared-host", "unknown"}


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


def split_semicolon(value):
    if not value:
        return []
    return [item.strip().strip('"') for item in value.split(";") if item.strip()]


def split_csv(value):
    if not value:
        return []
    return [item.strip() for item in value.replace(";", ",").split(",") if item.strip()]


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


def sha256_file(path, max_bytes=50 * 1024 * 1024):
    if path.stat().st_size > max_bytes:
        return ""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def redact_line(line):
    if "<redacted>" in line.lower():
        return line
    redacted = line
    for _name, pattern in SECRET_PATTERNS:
        redacted = pattern.sub(lambda match: f"{match.group(1)}<redacted>", redacted)
    return redacted


def add_finding(findings, severity, area, message, evidence=""):
    findings.append(
        {
            "severity": severity,
            "area": area,
            "message": message,
            "evidence": evidence,
        }
    )


def load_manifest(path, findings):
    if not path:
        return None
    candidate = Path(path).expanduser()
    if not candidate.exists():
        write_manifest_template(candidate)
        add_finding(
            findings,
            "hold",
            "manifest",
            "manifest was missing; a template was written and must be filled before pass",
            str(candidate),
        )
        return None
    try:
        data = json.loads(candidate.read_text(encoding="utf-8"))
    except Exception as exc:
        add_finding(findings, "error", "manifest", f"manifest parse failed: {type(exc).__name__}: {exc}", str(candidate))
        return None
    if not isinstance(data, dict):
        add_finding(findings, "error", "manifest", "manifest must be a JSON object", str(candidate))
        return None
    data["_manifest_path"] = str(candidate.resolve())
    return data


def write_manifest_template(path):
    template = {
        "service": "ollama-local",
        "runtime": "ollama",
        "base_url": "http://127.0.0.1:11434/v1",
        "native_api_url": "http://127.0.0.1:11434/api",
        "expected_model": "qwen3",
        "allowed_hosts": ["127.0.0.1", "localhost", "::1"],
        "intended_exposure": "loopback",
        "authentication_required": False,
        "rag_roots": [],
        "tool_allowed_roots": [],
        "ui_data_paths": [],
        "config_paths": [],
        "log_paths": [],
        "secrets_allowed_in_files": False,
        "export_boundary": "local-only",
        "notes": "Fill this template, then rerun the security/privacy runner.",
    }
    write_json(path, template)


def manifest_list(manifest, key, env_name):
    values = []
    if manifest and key in manifest:
        raw = manifest.get(key)
        if isinstance(raw, list):
            values.extend(str(item) for item in raw)
        elif isinstance(raw, str) and raw.strip():
            values.extend(split_semicolon(raw))
    values.extend(split_semicolon(os.environ.get(env_name, "")))
    seen = set()
    result = []
    for value in values:
        if value and value not in seen:
            seen.add(value)
            result.append(value)
    return result


def manifest_value(manifest, key, env_name, default=""):
    env_value = os.environ.get(env_name)
    if env_value is not None:
        return env_value
    if manifest and manifest.get(key) is not None:
        return str(manifest.get(key))
    return default


def normalize_exposure(value):
    normalized = (value or "unknown").strip().lower()
    return normalized if normalized in EXPOSURE_LABELS else "unknown"


def join_url(base_url, route):
    return f"{base_url.rstrip('/')}/{route.lstrip('/')}"


def derive_native_api_url(base_url):
    if not base_url:
        return ""
    parsed = urllib.parse.urlparse(base_url)
    if parsed.port != 11434:
        return ""
    path = parsed.path.rstrip("/")
    if path.endswith("/v1"):
        return urllib.parse.urlunparse(parsed._replace(path=path[:-3] + "/api"))
    return ""


def classify_host(url):
    parsed = urllib.parse.urlparse(url)
    host = parsed.hostname or ""
    host_display = host
    lowered = host.lower()
    if lowered in {"localhost"}:
        return {"host": host_display, "class": "loopback", "reason": "localhost"}
    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        if lowered in {"0.0.0.0", "::"}:
            return {"host": host_display, "class": "wildcard", "reason": "wildcard bind"}
        return {"host": host_display, "class": "hostname", "reason": "non-IP hostname"}
    if ip.is_unspecified:
        return {"host": host_display, "class": "wildcard", "reason": "unspecified address"}
    if ip.is_loopback:
        return {"host": host_display, "class": "loopback", "reason": "loopback address"}
    if ip.is_private:
        return {"host": host_display, "class": "lan", "reason": "private address"}
    if ip.is_global:
        return {"host": host_display, "class": "public", "reason": "global address"}
    return {"host": host_display, "class": "other", "reason": "special address"}


def auth_headers():
    headers = {"Accept": "application/json, text/plain, */*"}
    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"
    return headers


def fetch_json(source_id, url):
    started = time.perf_counter()
    record = {
        "source_id": source_id,
        "source_type": "endpoint",
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
        elapsed_ms = round((time.perf_counter() - started) * 1000, 3)
        text = raw.decode("utf-8", errors="replace")
        try:
            parsed = json.loads(text)
        except json.JSONDecodeError:
            parsed = None
        extension = "json" if parsed is not None else "txt"
        result_path = OUT_DIR / f"{RUN_ID}-{source_id}.{extension}"
        if parsed is not None:
            write_json(result_path, parsed)
        else:
            write_text(result_path, text)
        record.update(
            {
                "status": str(status_code),
                "ok": 200 <= int(status_code) < 400 and parsed is not None,
                "elapsed_ms": elapsed_ms,
                "bytes": len(raw),
                "result_path": str(result_path),
                "note": "json" if parsed is not None else "non-json response",
                "parsed": parsed,
            }
        )
    except urllib.error.HTTPError as exc:
        raw = exc.read()
        text = raw.decode("utf-8", errors="replace")
        result_path = OUT_DIR / f"{RUN_ID}-{source_id}-error.txt"
        write_text(result_path, redact_line(text))
        record.update(
            {
                "status": f"HTTP {exc.code}",
                "elapsed_ms": round((time.perf_counter() - started) * 1000, 3),
                "bytes": len(raw),
                "result_path": str(result_path),
                "note": redact_line(text[:200]).replace("\n", " "),
            }
        )
    except Exception as exc:
        record.update(
            {
                "status": "error",
                "elapsed_ms": round((time.perf_counter() - started) * 1000, 3),
                "note": f"{type(exc).__name__}: {exc}",
            }
        )
    return record


def extract_model_ids(record):
    parsed = record.get("parsed")
    if not isinstance(parsed, dict):
        return []
    ids = []
    data = parsed.get("data")
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and item.get("id"):
                ids.append(str(item["id"]))
    models = parsed.get("models")
    if isinstance(models, list):
        for item in models:
            if isinstance(item, dict):
                for key in ("name", "model", "id"):
                    if item.get(key):
                        ids.append(str(item[key]))
                        break
    return sorted(set(ids))


def scan_text_for_secrets(text, role, source, findings):
    rows = []
    for index, line in enumerate(text.splitlines(), start=1):
        if "<redacted>" in line.lower():
            continue
        for pattern_name, pattern in SECRET_PATTERNS:
            if pattern.search(line):
                preview = redact_line(line).strip()[:240]
                row = {
                    "severity": "hold",
                    "area": "secret_scan",
                    "pattern": pattern_name,
                    "role": role,
                    "source": source,
                    "line": index,
                    "preview": preview,
                }
                rows.append(row)
                add_finding(findings, "hold", "secret_scan", f"{pattern_name} matched in {role}", f"{source}:{index}")
                break
    return rows


def tail_text(path, line_limit):
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except Exception:
        return ""
    if line_limit > 0:
        lines = lines[-line_limit:]
    return "\n".join(lines)


def inspect_file(path_string, role, findings, secret_rows, tail_lines=None):
    path = Path(path_string).expanduser()
    record = {
        "source_id": f"{role}:{path_string}",
        "source_type": "file",
        "role": role,
        "path": str(path),
        "exists": path.exists(),
        "is_file": path.is_file() if path.exists() else False,
        "is_dir": path.is_dir() if path.exists() else False,
        "size_bytes": "",
        "sha256": "",
        "note": "",
    }
    if not path.exists():
        add_finding(findings, "hold", role, "declared path does not exist", str(path))
        return record
    if path.is_dir():
        record["note"] = "directory boundary only"
        return record
    if not path.is_file():
        record["note"] = "not a regular file"
        add_finding(findings, "warn", role, "declared path is not a regular file", str(path))
        return record
    try:
        record["size_bytes"] = path.stat().st_size
        record["sha256"] = sha256_file(path)
        text = tail_text(path, tail_lines if tail_lines is not None else 0)
        secret_rows.extend(scan_text_for_secrets(text, role, str(path), findings))
        redacted_path = OUT_DIR / f"{RUN_ID}-{role}-{safe_name(path.name)}-redacted.txt"
        write_text(redacted_path, "\n".join(redact_line(line) for line in text.splitlines()) + ("\n" if text else ""))
        record["redacted_excerpt_path"] = str(redacted_path)
    except Exception as exc:
        record["note"] = f"{type(exc).__name__}: {exc}"
        add_finding(findings, "warn", role, "could not read declared file", f"{path}: {exc}")
    return record


def safe_name(name):
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", name)[:80] or "source"


def write_csv(path, rows, fieldnames):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def write_markdown(path, result):
    findings = result["findings"]
    sources = result["sources"]
    model_ids = result["model_ids"]
    lines = [
        f"# Security and Privacy Runner - {RUN_ID}",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Status | {md_cell(result['status'])} |",
        f"| Decision | {md_cell(result['decision'])} |",
        f"| Service | {md_cell(result['service'])} |",
        f"| Runtime | {md_cell(result['runtime'])} |",
        f"| Intended exposure | {md_cell(result['intended_exposure'])} |",
        f"| Require loopback | {md_cell(result['require_loopback'])} |",
        f"| Base URL | {md_cell(result['base_url'])} |",
        f"| Native API URL | {md_cell(result['native_api_url'])} |",
        f"| Expected model | {md_cell(result['expected_model'])} |",
        f"| Model ids seen | {md_cell(', '.join(model_ids))} |",
        f"| Output folder | {md_cell(str(OUT_DIR))} |",
        "",
        "## Findings",
        "",
    ]
    if findings:
        lines.extend(["| Severity | Area | Message | Evidence |", "|---|---|---|---|"])
        for finding in findings:
            lines.append(
                f"| {md_cell(finding.get('severity'))} | {md_cell(finding.get('area'))} | {md_cell(finding.get('message'))} | {md_cell(finding.get('evidence'))} |"
            )
    else:
        lines.append("No findings.")
    lines.extend(["", "## Sources", ""])
    if sources:
        lines.extend(["| Source | Type | Status | Note |", "|---|---|---|---|"])
        for source in sources:
            label = source.get("url") or source.get("path") or source.get("source_id")
            status = source.get("status") or ("exists" if source.get("exists") else "missing")
            lines.append(f"| {md_cell(label)} | {md_cell(source.get('source_type'))} | {md_cell(status)} | {md_cell(source.get('note'))} |")
    else:
        lines.append("No sources checked.")
    lines.append("")
    write_text(path, "\n".join(lines))


def endpoint_exposure_checks(urls, allowed_hosts, intended_exposure, findings):
    rows = []
    for url in urls:
        classification = classify_host(url)
        host = classification["host"]
        host_class = classification["class"]
        rows.append({"url": url, **classification})
        if allowed_hosts and host and host not in allowed_hosts:
            add_finding(findings, "hold", "allowed_hosts", "endpoint host is not in allowed_hosts", f"{host} not in {allowed_hosts}")
        if REQUIRE_LOOPBACK and host_class != "loopback":
            if host_class in {"public", "wildcard"}:
                add_finding(findings, "error", "exposure", "non-loopback public or wildcard endpoint is blocked", url)
            else:
                add_finding(findings, "hold", "exposure", "non-loopback endpoint requires explicit security review", f"{url} classified as {host_class}")
        if intended_exposure in {"lan", "public", "tunnel", "shared-host"} and not AUTH_REQUIRED:
            add_finding(findings, "hold", "authentication", "non-loopback exposure requires authentication evidence", intended_exposure)
    return rows


def boundary_checks(manifest, config_paths, log_paths, findings):
    if not manifest:
        return
    exposure = normalize_exposure(manifest.get("intended_exposure", "unknown"))
    if exposure == "unknown":
        add_finding(findings, "hold", "boundary", "intended_exposure is missing or unknown", "")
    if not str(manifest.get("export_boundary", "")).strip():
        add_finding(findings, "hold", "boundary", "export_boundary is missing", "")
    if "rag_roots" not in manifest:
        add_finding(findings, "warn", "boundary", "rag_roots field is missing; use [] if RAG is not used", "")
    if "tool_allowed_roots" not in manifest:
        add_finding(findings, "warn", "boundary", "tool_allowed_roots field is missing; use [] if tools are not used", "")
    if not config_paths and not log_paths:
        add_finding(findings, "hold", "source_inventory", "no config_paths or log_paths were provided for scan evidence", "")


def decide(findings, route_ok, expected_model, expected_model_present):
    if not route_ok:
        add_finding(findings, "hold", "route", "no read-only model-list route succeeded", "")
    if expected_model and route_ok and not expected_model_present:
        add_finding(findings, "hold", "model", "expected model was not visible in model-list evidence", expected_model)
    severities = {item["severity"] for item in findings}
    if "error" in severities:
        return "error", "public_or_invalid_exposure_blocked"
    if "hold" in severities:
        for item in findings:
            if item["severity"] == "hold":
                return "hold", item["area"]
    return "pass", "loopback_private_ready"


RUN_ID = time.strftime("%Y%m%d-%H%M%S")
RUN_ROOT = Path(os.environ.get("LOCAL_LLM_RUN_ROOT", Path.home() / "Documents" / "local-llm-runs")).expanduser()
OUT_DIR = RUN_ROOT / "security-privacy-runner"
MANIFEST_PATH = os.environ.get("LOCAL_LLM_SECURITY_MANIFEST", str(RUN_ROOT / "security-privacy-manifest.json"))
TIMEOUT_SECONDS = float(os.environ.get("LOCAL_LLM_TIMEOUT_SECONDS", "5"))
LOG_TAIL_LINES = as_int(os.environ.get("LOCAL_LLM_LOG_TAIL_LINES"), 300)
REQUIRE_LOOPBACK = env_bool("LOCAL_LLM_REQUIRE_LOOPBACK", True)
API_KEY = os.environ.get("LOCAL_LLM_API_KEY", "")


def main():
    findings = []
    secret_rows = []
    manifest = load_manifest(MANIFEST_PATH, findings)

    service = manifest_value(manifest, "service", "LOCAL_LLM_SERVICE", "local-llm")
    runtime = manifest_value(manifest, "runtime", "LOCAL_LLM_RUNTIME", "unknown")
    base_url = manifest_value(manifest, "base_url", "LOCAL_LLM_BASE_URL", "")
    native_api_url = manifest_value(manifest, "native_api_url", "LOCAL_LLM_OLLAMA_API_URL", "")
    if not native_api_url:
        native_api_url = derive_native_api_url(base_url)
    expected_model = manifest_value(manifest, "expected_model", "LOCAL_LLM_EXPECTED_MODEL", "")
    intended_exposure = normalize_exposure(manifest_value(manifest, "intended_exposure", "LOCAL_LLM_INTENDED_EXPOSURE", "unknown"))
    allowed_hosts = []
    if manifest and isinstance(manifest.get("allowed_hosts"), list):
        allowed_hosts.extend(str(item) for item in manifest.get("allowed_hosts", []))
    allowed_hosts.extend(split_csv(os.environ.get("LOCAL_LLM_ALLOWED_HOSTS", "")))
    if not allowed_hosts and REQUIRE_LOOPBACK:
        allowed_hosts = ["127.0.0.1", "localhost", "::1"]

    global AUTH_REQUIRED
    AUTH_REQUIRED = env_bool("LOCAL_LLM_AUTHENTICATION_REQUIRED", bool(manifest.get("authentication_required")) if manifest else False)
    secrets_allowed = env_bool("LOCAL_LLM_SECRETS_ALLOWED_IN_FILES", bool(manifest.get("secrets_allowed_in_files")) if manifest else False)

    config_paths = manifest_list(manifest, "config_paths", "LOCAL_LLM_CONFIG_PATHS")
    log_paths = manifest_list(manifest, "log_paths", "LOCAL_LLM_LOG_PATHS")
    rag_roots = manifest_list(manifest, "rag_roots", "LOCAL_LLM_RAG_ROOTS")
    tool_roots = manifest_list(manifest, "tool_allowed_roots", "LOCAL_LLM_TOOL_ALLOWED_ROOTS")
    ui_paths = manifest_list(manifest, "ui_data_paths", "LOCAL_LLM_UI_DATA_PATHS")

    urls = []
    endpoint_specs = []
    if base_url:
        endpoint_specs.append(("openai_models", join_url(base_url, "models")))
        urls.append(base_url)
    if native_api_url:
        endpoint_specs.append(("ollama_tags", join_url(native_api_url, "tags")))
        endpoint_specs.append(("ollama_ps", join_url(native_api_url, "ps")))
        urls.append(native_api_url)

    exposure_rows = endpoint_exposure_checks(urls, allowed_hosts, intended_exposure, findings)
    boundary_checks(manifest, config_paths, log_paths, findings)

    sources = []
    for source_id, url in endpoint_specs:
        record = fetch_json(source_id, url)
        sources.append(record)

    for path in config_paths:
        sources.append(inspect_file(path, "config", findings, secret_rows))
    for path in log_paths:
        sources.append(inspect_file(path, "log", findings, secret_rows, tail_lines=LOG_TAIL_LINES))
    for path in rag_roots:
        sources.append(inspect_file(path, "rag_root", findings, secret_rows))
    for path in tool_roots:
        sources.append(inspect_file(path, "tool_root", findings, secret_rows))
    for path in ui_paths:
        sources.append(inspect_file(path, "ui_data", findings, secret_rows))

    if secret_rows and secrets_allowed:
        for finding in findings:
            if finding.get("area") == "secret_scan" and finding.get("severity") == "hold":
                finding["severity"] = "warn"
        add_finding(findings, "warn", "secret_scan", "secret-like patterns were found but manifest allows them", "")

    model_ids = []
    for source in sources:
        if source.get("source_type") == "endpoint":
            model_ids.extend(extract_model_ids(source))
    model_ids = sorted(set(model_ids))
    route_ok = any(source.get("ok") for source in sources if source.get("source_type") == "endpoint")
    expected_model_present = not expected_model or expected_model in model_ids or any(expected_model in item for item in model_ids)

    status, decision_value = decide(findings, route_ok, expected_model, expected_model_present)

    result = {
        "run_id": RUN_ID,
        "status": status,
        "decision": decision_value,
        "service": service,
        "runtime": runtime,
        "base_url": base_url,
        "native_api_url": native_api_url,
        "expected_model": expected_model,
        "model_ids": model_ids,
        "intended_exposure": intended_exposure,
        "allowed_hosts": allowed_hosts,
        "require_loopback": REQUIRE_LOOPBACK,
        "authentication_required": AUTH_REQUIRED,
        "secrets_allowed_in_files": secrets_allowed,
        "manifest_path": MANIFEST_PATH,
        "run_root": str(RUN_ROOT),
        "out_dir": str(OUT_DIR),
        "platform": {
            "hostname": socket.gethostname(),
            "system": platform.system(),
            "release": platform.release(),
            "python": platform.python_version(),
        },
        "exposure_rows": exposure_rows,
        "sources": sources,
        "secret_rows": secret_rows,
        "findings": findings,
    }

    result_path = OUT_DIR / f"{RUN_ID}-security-results.json"
    markdown_path = OUT_DIR / f"{RUN_ID}-security-results.md"
    sources_csv = OUT_DIR / f"{RUN_ID}-security-sources.csv"
    findings_csv = OUT_DIR / f"{RUN_ID}-security-findings.csv"
    sources_jsonl = OUT_DIR / f"{RUN_ID}-security-sources.jsonl"
    run_log = OUT_DIR / "security-privacy-runs.jsonl"

    write_json(result_path, result)
    write_markdown(markdown_path, result)
    write_csv(
        sources_csv,
        sources,
        ["source_id", "source_type", "role", "url", "path", "exists", "is_file", "is_dir", "status", "ok", "elapsed_ms", "bytes", "size_bytes", "sha256", "result_path", "redacted_excerpt_path", "note"],
    )
    write_csv(findings_csv, findings, ["severity", "area", "message", "evidence"])
    for source in sources:
        append_jsonl(sources_jsonl, source)
    append_jsonl(run_log, {"run_id": RUN_ID, "status": status, "decision": decision_value, "result_path": str(result_path)})

    print(json.dumps({"status": status, "decision": decision_value, "result_path": str(result_path), "markdown_path": str(markdown_path)}, ensure_ascii=True))
    return 0 if status == "pass" else 2


if __name__ == "__main__":
    raise SystemExit(main())
```

## PowerShell Run

```powershell
$RunRoot = Join-Path $HOME ("Documents\local-llm-runs\" + (Get-Date -Format "yyyy-MM-dd-HHmm") + "-security")
New-Item -ItemType Directory -Force -Path $RunRoot | Out-Null

$env:LOCAL_LLM_RUN_ROOT = $RunRoot
$env:LOCAL_LLM_SECURITY_MANIFEST = Join-Path $RunRoot "security-privacy-manifest.json"
$env:LOCAL_LLM_REQUIRE_LOOPBACK = "1"

python .\security-privacy-runner.py
```

First run behavior: if the manifest does not exist, the runner writes a template and returns `hold`. Fill the manifest, then rerun.

## Pass/Hold/Error Interpretation

| Status | Meaning | Next action |
|---|---|---|
| `pass` / `loopback_private_ready` | The route evidence, model visibility, host boundary, manifest, source inventory, and scanned files did not produce blocking findings. | Continue to endpoint smoke, API contract, quality, observability, or lifecycle evidence. |
| `hold` / `exposure` | The endpoint is LAN/private/hostname while loopback is required. | Add explicit auth/firewall/proxy/logging evidence or keep the server on loopback. |
| `hold` / `secret_scan` | A scanned config/log file contains an obvious secret-like pattern. | Rotate if needed, remove from shared artifacts, and keep raw logs local. |
| `hold` / `source_inventory` | No config or log sources were named. | Add config/log paths or explicitly document why no local sources exist. |
| `hold` / `model` | The expected model was not visible in read-only model-list evidence. | Fix model id, served model, or route before smoke testing. |
| `error` / `public_or_invalid_exposure_blocked` | A public or wildcard URL was found while loopback was required, or the manifest is invalid. | Stop and fix exposure or manifest before using the service. |

## Fixture Verification

Use this shape to test the runner without a real LLM. The fake server should expose only read-only model-list routes:

```json
{
  "service": "fixture-local",
  "runtime": "fixture",
  "base_url": "http://127.0.0.1:<port>/v1",
  "native_api_url": "http://127.0.0.1:<port>/api",
  "expected_model": "fixture-model",
  "allowed_hosts": ["127.0.0.1", "localhost", "::1"],
  "intended_exposure": "loopback",
  "authentication_required": false,
  "rag_roots": [],
  "tool_allowed_roots": [],
  "ui_data_paths": [],
  "config_paths": ["<fixture-config>"],
  "log_paths": ["<fixture-log>"],
  "secrets_allowed_in_files": false,
  "export_boundary": "local-only"
}
```

Expected fixture pass: status `pass`, decision `loopback_private_ready`, `/v1/models` reachable, `fixture-model` visible, no secret findings, and no non-loopback exposure finding.

## Capstone Row

| Field | Value |
|---|---|
| Security runner result |  |
| Manifest path |  |
| Status / decision |  |
| Base URL and host class |  |
| Expected model visible |  |
| Config/log sources scanned |  |
| Secret findings | none / fixed / accepted risk |
| RAG roots |  |
| Tool roots |  |
| UI data paths |  |
| Export boundary |  |
| Next action | smoke / API contract / quality / observability / lifecycle / deployment |

## References

- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Observability and Operations Runner]]
- [[LLM/Study/Local Open WebUI Provider Integration Runner]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Runner]]
- [[LLM/Study/Local RAG Minimal Python Harness]]
- [[LLM/Study/Local RAG Prompt Injection and Source Boundary Runner]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
