---
tags: [study, llm, inference, local-llm, ollama, model-acquisition, provenance, first-run, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-16
---

# Local LLM First Model Pull Runner

> **One-line summary** The first model pull counts only when the selected tag, source check, store decision, compatibility proof, pull output, model list, API tags, show metadata, and next route are all saved and agree.

Use this after [[LLM/Study/Local LLM First Model Pull Gate|Local LLM First Model Pull Gate]] when pull artifacts should become repeatable JSON, Markdown, CSV, and JSONL evidence. Use [[LLM/Study/Local LLM First Model Source Recheck Runner|Local LLM First Model Source Recheck Runner]] before pull when the source page needs a machine-checkable dated pass/hold/fail row. Use this runner before [[LLM/Study/Local LLM First Runtime Health Runner|Local LLM First Runtime Health Runner]], [[LLM/Study/Local LLM First Runtime Health Snapshot|Local LLM First Runtime Health Snapshot]], [[LLM/Study/Local LLM First Smoke Request Runner|Local LLM First Smoke Request Runner]], and [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]].

This runner does not run `ollama pull` and does not contact a model registry. It audits saved evidence from the pull gate so a failed or partial download cannot be mistaken for endpoint readiness.

## What This Proves

| Gate | Evidence checked | Why it matters |
|---|---|---|
| Intent before download | selected model, fallback, source check, store decision | prevents "whatever was already installed" from becoming first-run proof |
| Precondition proof | runtime install, model store, compatibility decision | keeps pull evidence tied to the actual machine and runtime path |
| Pull artifact | saved pull output and explicit pull status | separates a completed pull from a partial or failed transfer |
| Runtime inventory | `ollama ls`, `/api/tags`, `/api/show` evidence | proves the selected model is visible through both CLI and local API metadata |
| Handoff | pass/hold/fail and next route | decides whether runtime health, endpoint smoke, smaller model, storage fix, or compatibility triage is next |

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "first-qwen-pull",
  "run_root": "D:/llm-runs/first-model-pull",
  "vault_root": "D:/Vaults/PersonalKB",
  "selected_model": "qwen3.5:4b",
  "fallback_model": "qwen3.5:2b",
  "source_page": "https://ollama.com/library/qwen3.5/tags",
  "source_checked_at": "2026-06-16",
  "source_recheck_output": "D:/llm-runs/first-model-source-recheck/first-model-source-recheck-001-model-source-recheck.json",
  "expected_digest": "2a654d98e6fb",
  "expected_size": "3.4GB",
  "model_store_decision": "default",
  "pull_status": "pass",
  "runtime_install_proof": "LLM/Study/Local LLM Windows Runtime Install Gate",
  "model_store_proof": "LLM/Study/Local LLM Model Store Readiness Snapshot",
  "runtime_compatibility_proof": "LLM/Study/Local LLM Runtime Compatibility Runner",
  "artifacts": {
    "model_pull_decision": "D:/llm-runs/first-model-pull/model-pull-decision.txt",
    "pull_output": "D:/llm-runs/first-model-pull/ollama-pull.txt",
    "ollama_ls_after_pull": "D:/llm-runs/first-model-pull/ollama-ls-after-pull.txt",
    "api_tags_after_pull": "D:/llm-runs/first-model-pull/ollama-api-tags-after-pull.json",
    "api_show_response": "D:/llm-runs/first-model-pull/ollama-show-response.json"
  },
  "next_route": "LLM/Study/Local LLM First Runtime Health Runner"
}
```

Use absolute paths for run artifacts when possible. Vault-relative or manifest-relative paths also work.

## Standard-Library Runner

Save the code block as `local_llm_first_model_pull_runner.py` or extract it directly from this note.

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


REQUIRED_FIELDS = [
    "selected_model",
    "source_page",
    "source_checked_at",
    "model_store_decision",
    "pull_status",
    "runtime_install_proof",
    "model_store_proof",
    "runtime_compatibility_proof",
    "next_route",
]

REQUIRED_ARTIFACTS = [
    "model_pull_decision",
    "pull_output",
    "ollama_ls_after_pull",
    "api_tags_after_pull",
    "api_show_response",
]


def utc_iso() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def slug(value: str) -> str:
    text_value = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return text_value or "local-llm-first-model-pull"


def load_manifest() -> tuple[Path, dict[str, Any]]:
    raw_path = os.environ.get("LOCAL_LLM_FIRST_MODEL_PULL_MANIFEST")
    if len(sys.argv) > 1:
        raw_path = sys.argv[1]
    if not raw_path:
        raise ValueError("Set LOCAL_LLM_FIRST_MODEL_PULL_MANIFEST or pass a manifest path.")
    path = Path(raw_path).expanduser().resolve()
    return path, json.loads(path.read_text(encoding="utf-8"))


def text(value: Any) -> str:
    return str(value or "").strip()


def status_value(value: Any) -> str:
    normalized = text(value).lower().replace("_", "-")
    if normalized in {"pass", "passed", "ready", "complete", "completed", "ok"}:
        return "pass"
    if normalized in {"fail", "failed", "error", "rejected", "partial-failed"}:
        return "fail"
    if normalized in {"hold", "pending", "unknown", "missing", "partial", "incomplete", ""}:
        return "hold"
    return normalized


def wiki_link(route: str) -> str:
    route = text(route)
    if not route:
        return "[[LLM/Study/Local LLM First Model Pull Gate]]"
    if route.startswith("[["):
        return route
    return "[" + "[" + route.removesuffix(".md") + "]" + "]"


def csv_cell(value: Any) -> str:
    if isinstance(value, list):
        return ";".join(str(item) for item in value)
    if value is None:
        return ""
    return str(value)


def md_cell(value: Any) -> str:
    return csv_cell(value).replace("|", "\\|").replace("\n", " ")


def finding(level: str, owner: str, text_value: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "owner": owner,
        "finding": text_value,
        "evidence": evidence,
        "action": action,
    }


def resolve_path(raw_value: Any, manifest_path: Path, run_root: Path, vault_root: Path) -> Path | None:
    raw = text(raw_value)
    if not raw:
        return None
    path = Path(raw).expanduser()
    if path.is_absolute():
        return path
    candidates = [
        run_root / path,
        vault_root / path,
        manifest_path.parent / path,
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]


def read_artifact(path: Path | None) -> tuple[bool, str]:
    if path is None:
        return False, ""
    if not path.exists():
        return False, ""
    if not path.is_file():
        return False, ""
    return True, path.read_text(encoding="utf-8", errors="replace")


def parse_json_or_none(text_value: str) -> Any | None:
    try:
        return json.loads(text_value)
    except json.JSONDecodeError:
        return None


def normalize_model(value: str) -> str:
    return text(value).lower()


def json_contains_model(value: Any, selected_model: str) -> bool:
    needle = normalize_model(selected_model)
    if not needle:
        return False
    if isinstance(value, dict):
        for key, item in value.items():
            key_text = normalize_model(str(key))
            if key_text in {"name", "model", "model_id", "id", "digest"} and needle in normalize_model(str(item)):
                return True
            if json_contains_model(item, selected_model):
                return True
    elif isinstance(value, list):
        return any(json_contains_model(item, selected_model) for item in value)
    elif isinstance(value, str):
        return needle in normalize_model(value)
    return False


def text_contains_model(text_value: str, selected_model: str) -> bool:
    return normalize_model(selected_model) in normalize_model(text_value)


def artifact_has_model(path: Path | None, selected_model: str) -> tuple[bool, bool, str]:
    exists, content = read_artifact(path)
    if not exists:
        return False, False, ""
    parsed = parse_json_or_none(content)
    if parsed is not None:
        return True, json_contains_model(parsed, selected_model), "json"
    return True, text_contains_model(content, selected_model), "text"


def artifact_has_digest(path: Path | None, expected_digest: str) -> tuple[bool, str]:
    if not expected_digest:
        return True, "not required"
    exists, content = read_artifact(path)
    if not exists:
        return False, "missing artifact"
    digest = normalize_model(expected_digest)
    return digest in normalize_model(content), "digest text search"


def evaluate_manifest(manifest: dict[str, Any], manifest_path: Path, run_root: Path, vault_root: Path) -> dict[str, Any]:
    selected_model = text(manifest.get("selected_model"))
    findings: list[dict[str, str]] = []

    for field in REQUIRED_FIELDS:
        if not text(manifest.get(field)):
            findings.append(finding(
                "hold",
                "manifest",
                f"Required field `{field}` is missing.",
                field,
                f"Fill `{field}` from the model pull gate before auditing the first pull.",
            ))

    store_decision = status_value(manifest.get("model_store_decision"))
    if store_decision == "hold":
        findings.append(finding(
            "hold",
            "storage",
            "Model store decision is hold or missing.",
            text(manifest.get("model_store_decision")),
            "Finish the model store readiness snapshot before pulling a model.",
        ))

    pull_status = status_value(manifest.get("pull_status"))
    if pull_status == "fail":
        findings.append(finding(
            "fail",
            "pull",
            "Pull status is explicitly failed.",
            text(manifest.get("pull_status")),
            "Fix the pull failure, choose a smaller fallback, or change the model store decision before endpoint smoke.",
        ))
    elif pull_status != "pass":
        findings.append(finding(
            "hold",
            "pull",
            "Pull status is not pass.",
            text(manifest.get("pull_status")),
            "Record pull_status as pass only after the selected model is visible through CLI and API evidence.",
        ))

    artifacts = manifest.get("artifacts") or {}
    if not isinstance(artifacts, dict):
        artifacts = {}
        findings.append(finding(
            "hold",
            "manifest",
            "Artifacts must be an object.",
            "artifacts",
            "Provide paths for model_pull_decision, pull_output, ollama_ls_after_pull, api_tags_after_pull, and api_show_response.",
        ))

    artifact_rows: list[dict[str, Any]] = []
    resolved_paths: dict[str, Path | None] = {}
    for name in REQUIRED_ARTIFACTS:
        path = resolve_path(artifacts.get(name), manifest_path, run_root, vault_root)
        resolved_paths[name] = path
        exists, content = read_artifact(path)
        row = {
            "artifact": name,
            "path": str(path) if path else "",
            "exists": exists,
            "bytes": len(content.encode("utf-8")) if exists else 0,
            "model_found": None,
        }
        if not exists:
            findings.append(finding(
                "hold",
                "artifact",
                f"Required artifact `{name}` is missing.",
                str(path) if path else name,
                f"Save `{name}` from the first model pull gate before runtime health or endpoint smoke.",
            ))
        artifact_rows.append(row)

    for name in ["model_pull_decision", "pull_output", "ollama_ls_after_pull", "api_tags_after_pull", "api_show_response"]:
        path = resolved_paths.get(name)
        exists, found, mode = artifact_has_model(path, selected_model)
        for row in artifact_rows:
            if row["artifact"] == name:
                row["model_found"] = found if exists else None
                row["mode"] = mode
                break
        if exists and selected_model and not found:
            level = "fail" if name in {"ollama_ls_after_pull", "api_tags_after_pull", "api_show_response"} else "hold"
            findings.append(finding(
                level,
                "inventory",
                f"Selected model `{selected_model}` was not found in `{name}`.",
                str(path),
                "Fix the selected model id, rerun the runtime inventory command, or choose the model actually installed.",
            ))

    digest_ok, digest_method = artifact_has_digest(resolved_paths.get("api_show_response"), text(manifest.get("expected_digest")))
    if not digest_ok:
        findings.append(finding(
            "hold",
            "metadata",
            "Expected digest is not visible in the show response.",
            digest_method,
            "Record the actual digest from `/api/show`, or update the expected digest source check.",
        ))

    fail_count = sum(1 for item in findings if item["level"] == "fail")
    hold_count = sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        status = "fail"
        decision = "first_model_pull_failed"
    elif hold_count:
        status = "hold"
        decision = "first_model_pull_incomplete"
    else:
        status = "pass"
        decision = "first_model_pull_ready"

    next_route = text(manifest.get("next_route"))
    if not next_route:
        next_route = "LLM/Study/Local LLM First Runtime Health Runner" if status == "pass" else "LLM/Study/Local LLM First Model Pull Gate"

    return {
        "selected_model": selected_model,
        "fallback_model": text(manifest.get("fallback_model")),
        "source_page": text(manifest.get("source_page")),
        "source_checked_at": text(manifest.get("source_checked_at")),
        "expected_digest": text(manifest.get("expected_digest")),
        "expected_size": text(manifest.get("expected_size")),
        "model_store_decision": text(manifest.get("model_store_decision")),
        "pull_status": pull_status,
        "status": status,
        "decision": decision,
        "next_route": next_route,
        "next_action": findings[0]["action"] if findings else "Run the first runtime health snapshot before endpoint smoke testing.",
        "artifacts": artifact_rows,
        "findings": findings,
    }


def csv_write(path: Path, artifact_rows: list[dict[str, Any]]) -> None:
    fields = ["artifact", "path", "exists", "bytes", "model_found", "mode"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in artifact_rows:
            writer.writerow({field: csv_cell(row.get(field)) for field in fields})


def render_markdown(record: dict[str, Any]) -> str:
    result = record["result"]
    lines = [
        f"# Local LLM First Model Pull - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Selected model: `{result['selected_model']}`",
        f"- Source checked: `{result['source_checked_at']}`",
        f"- Next route: {wiki_link(result['next_route'])}",
        "",
        "## Artifact Results",
        "",
        "| Artifact | Exists | Bytes | Model found | Path |",
        "|---|---:|---:|---:|---|",
    ]
    for row in result["artifacts"]:
        lines.append(
            "| "
            + " | ".join([
                md_cell(row["artifact"]),
                md_cell(row["exists"]),
                md_cell(row["bytes"]),
                md_cell(row.get("model_found")),
                md_cell(row["path"]),
            ])
            + " |"
        )
    lines.extend(["", "## Findings", ""])
    if result["findings"]:
        for item in result["findings"]:
            lines.append(f"- `{item['level']}` `{item['owner']}`: {item['finding']} -> {item['action']}")
    else:
        lines.append("- Pull evidence is ready for runtime health snapshot.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    manifest_path, manifest = load_manifest()
    run_id = str(manifest.get("run_id") or os.environ.get("LOCAL_LLM_FIRST_MODEL_PULL_RUN_ID") or f"{utc_stamp()}-{slug(manifest_path.stem)}")
    run_root_value = os.environ.get("LOCAL_LLM_FIRST_MODEL_PULL_RUN_ROOT") or manifest.get("run_root", "local-llm-first-model-pull-runs")
    run_root = Path(str(run_root_value)).expanduser()
    if not run_root.is_absolute():
        run_root = manifest_path.parent / run_root
    run_root = run_root.resolve()
    run_dir = run_root / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    vault_root = Path(str(manifest.get("vault_root") or os.environ.get("LOCAL_LLM_FIRST_MODEL_PULL_VAULT_ROOT") or manifest_path.parent)).expanduser()

    result = evaluate_manifest(manifest, manifest_path, run_root, vault_root)
    status = result["status"]
    decision = result["decision"]

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "manifest_path": str(manifest_path),
        "vault_root": str(vault_root),
        "run_root": str(run_root),
        "result": result,
        "outputs": {},
    }

    json_path = run_dir / f"{run_id}-first-model-pull.json"
    markdown_path = run_dir / f"{run_id}-first-model-pull.md"
    csv_path = run_dir / f"{run_id}-first-model-pull-artifacts.csv"
    jsonl_path = run_root / "local-llm-first-model-pull-runs.jsonl"
    record["outputs"] = {
        "json": str(json_path),
        "markdown": str(markdown_path),
        "csv": str(csv_path),
        "jsonl": str(jsonl_path),
    }

    csv_write(csv_path, result["artifacts"])
    json_path.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    markdown_path.write_text(render_markdown(record), encoding="utf-8")
    with jsonl_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(json.dumps({
        "status": status,
        "decision": decision,
        "run_id": run_id,
        "selected_model": result["selected_model"],
        "finding_count": len(result["findings"]),
        "output_dir": str(run_dir),
    }, indent=2))
    return 0 if status == "pass" else 1 if status == "hold" else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(json.dumps({"status": "error", "decision": "runner_exception", "error": str(exc)}, indent=2), file=sys.stderr)
        raise
```

## PowerShell Run

```powershell
$env:LOCAL_LLM_FIRST_MODEL_PULL_MANIFEST = "D:\llm-runs\first-model-pull\first-model-pull-manifest.json"
$env:LOCAL_LLM_FIRST_MODEL_PULL_RUN_ROOT = "D:\llm-runs\first-model-pull"
$env:LOCAL_LLM_FIRST_MODEL_PULL_VAULT_ROOT = "D:\Vaults\PersonalKB"
python .\local_llm_first_model_pull_runner.py
```

## Reading The Result

| Runner status | Meaning | Next route |
|---|---|---|
| `pass/first_model_pull_ready` | selected model, source check, store decision, preconditions, pull output, CLI list, API tags, and show metadata agree | [[LLM/Study/Local LLM First Runtime Health Runner]] |
| `hold/first_model_pull_incomplete` | pull artifacts, source check, store decision, compatibility proof, digest, or explicit status is missing | [[LLM/Study/Local LLM First Model Pull Gate]] |
| `fail/first_model_pull_failed` | pull failed or runtime inventory contradicts the selected model | fix pull/storage/tag mismatch before runtime health or endpoint smoke |

A `pass` result does not prove inference. It only says the model artifact is visible enough to move to a no-generation runtime health snapshot.

## Capstone Row

| Evidence | Output |
|---|---|
| First model pull runner | `<run-id>-first-model-pull.json`, `<run-id>-first-model-pull.md`, `<run-id>-first-model-pull-artifacts.csv`, and one `local-llm-first-model-pull-runs.jsonl` row |

## Completion Gate

This runner is useful when:

- [ ] the selected model, fallback, source page, source check date, expected size, and expected digest are recorded
- [ ] source recheck output is linked when the current page facts were machine-checked before pull
- [ ] runtime install, model store, and runtime compatibility proof links exist
- [ ] model store decision is not hold
- [ ] pull output is saved and pull status is explicit
- [ ] `ollama ls`, `/api/tags`, and `/api/show` evidence all include the selected model
- [ ] digest mismatch is explained before endpoint smoke
- [ ] output JSON, Markdown, CSV, and JSONL artifacts are saved before runtime health or inference

## References

- [[LLM/Study/Local LLM First Model Pull Gate]]
- [[LLM/Study/Local LLM First Model Source Recheck Runner]]
- [[LLM/Study/Local LLM Model Store Readiness Snapshot]]
- [[LLM/Study/Local LLM Windows Runtime Install Gate]]
- [[LLM/Study/Local LLM Runtime Compatibility Runner]]
- [[LLM/Study/Local LLM Artifact Custody Audit Runner]]
- [[LLM/Study/Local LLM First Runtime Health Snapshot]]
- [[LLM/Study/Local LLM First Runtime Health Runner]]
- [[LLM/Study/Local LLM First Smoke Request Runner]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
