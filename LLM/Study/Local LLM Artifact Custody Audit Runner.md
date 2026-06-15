---
tags: [study, llm, inference, local-llm, artifact, custody, provenance, audit, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM Artifact Custody Audit Runner

> **One-line summary** A local model should not be served until the exact bytes, source, revision, verification evidence, unsafe-file decision, conversion or import trail, runtime handoff, and cleanup plan can be audited.

Use this after [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Local LLM Artifact Download Cache and Conversion Lab]] has produced artifact rows. Use [[LLM/Study/Local LLM Model Acquisition and License Gate Runner|Local LLM Model Acquisition and License Gate Runner]] before or alongside this runner when source, license, gated access, pinning, and unsafe-file posture need machine-checkable acquisition evidence. Use [[LLM/Study/Local LLM Model Metadata Card Runner|Local LLM Model Metadata Card Runner]] before or alongside this runner when file inventory, `config.json`, tokenizer files, GGUF metadata, or Ollama show output need to become normalized architecture/tokenizer/runtime facts. Use this before [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]], [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]], or [[LLM/Study/LLM Deployment Readiness Audit Runner|LLM Deployment Readiness Audit Runner]] when the next decision depends on knowing which model bytes are actually under test.

This runner does not download models, inspect registries, or hash files for you. It audits the evidence you saved: source/provenance card, pinned source identity, local path or runtime id, file inventory, hash or verification result, unsafe-file decision, conversion/import proof, runtime handoff, cleanup plan, and rejected-artifact boundary.

## What This Proves

| Evidence family | Checks | Why it matters |
|---|---|---|
| Source identity | model source, artifact form, revision, tag, filename, or digest are recorded | avoids benchmarking a floating or ambiguous model |
| Local bytes | cache path, local mirror, GGUF path, runtime id, or derived output is linked | ties the runtime to a concrete artifact |
| File inventory | shard list, file list, metadata, or runtime show output exists | catches wrong downloads, missing tokenizer files, and hidden package details |
| Verification | hash, digest, `hf cache verify`, scanner result, or partial-verification note is explicit | separates reproducible proof from best-effort learning evidence |
| Unsafe boundary | pickle-like files, custom code, and `trust_remote_code` have a decision and review artifact | prevents silent code-execution risk from entering serving evidence |
| Conversion/import | GGUF conversion, Ollama import, or runtime package handoff has command output and resulting id/hash | treats derived artifacts as new evidence, not neutral copies |
| Cleanup | accepted and rejected artifacts have a removal or retention plan | prevents stale caches from becoming future model identity confusion |

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "artifact-custody-2026-06-15",
  "run_root": "D:/llm-runs/artifact-custody",
  "vault_root": "D:/Vaults/PersonalKB",
  "artifacts": [
    {
      "artifact_id": "qwen2.5-7b-instruct-q4",
      "artifact_form": "gguf",
      "source_ref": "hf.co/org/repo",
      "revision_or_file": "model-q4_k_m.gguf",
      "provenance_artifact": "LLM/Study/Local LLM Model Acquisition and License Gate Runner",
      "local_path": "D:/Models/gguf/model-q4_k_m.gguf",
      "file_inventory_artifact": "D:/llm-runs/artifact-custody/file-list.txt",
      "verification_method": "sha256",
      "hash_or_digest": "sha256:...",
      "verification_artifact": "D:/llm-runs/artifact-custody/hash.txt",
      "unsafe_file_decision": "none",
      "conversion_or_import": "none",
      "runtime_handoff_artifact": "LLM/Study/Local LLM Runtime and Model Compatibility Matrix",
      "cleanup_plan": "Keep accepted GGUF; remove rejected dry-run cache with reviewed command."
    }
  ]
}
```

`provenance_artifact`, `local_path`, `file_inventory_artifact`, `verification_artifact`, `conversion_artifact`, `runtime_handoff_artifact`, and `review_artifact` may be absolute paths, vault-relative paths, Obsidian note paths, or Obsidian links.

## Row Contract

| Field | Required when | Meaning |
|---|---|---|
| `artifact_id` | always | stable id for this model artifact or runtime package |
| `artifact_form` | always | `hf_snapshot`, `local_dir`, `gguf`, `ollama_package`, `converted_derivative`, `adapter`, or custom |
| `source_ref` | always | registry, URL, internal source, or runtime package source |
| `revision_or_file` | always | commit, tag, filename, package tag, or digest |
| `provenance_artifact` | always | model acquisition card, source/provenance note, or [[LLM/Study/Local LLM Model Acquisition and License Gate Runner|model acquisition/license gate output]] |
| `local_path` or `runtime_model_id` | always | concrete local bytes or runtime-visible package id |
| `file_inventory_artifact` | always | file list, shard list, runtime show output, or metadata output |
| `model_metadata_card` | compatibility, tokenizer, context, or KV-cache handoffs | output from [[LLM/Study/Local LLM Model Metadata Card Runner|Local LLM Model Metadata Card Runner]] when normalized model facts support downstream evidence |
| `verification_method` | always | `sha256`, `digest`, `hf_cache_verify`, `runtime_show`, `scanner`, `partial`, or similar |
| `hash_or_digest` or `verification_artifact` | always | actual verification value or output file |
| `unsafe_file_decision` | always | `none`, `reviewed`, `sandboxed`, `learning-only`, `blocked`, or equivalent |
| `review_artifact` | unsafe/custom-code rows | review note, scanner output, or sandbox record |
| `conversion_or_import` | always | `none`, `ollama_import`, `ollama_hf_shortcut`, `gguf_conversion`, `quantization`, or equivalent |
| `conversion_artifact` | conversion/import rows | Modelfile, command log, converter command, runtime show, or output hash record |
| `derived_output_hash` | converted derivative rows | hash or digest of the converted output |
| `runtime_handoff_artifact` | always | compatibility card, serving run sheet, or runtime show evidence |
| `cleanup_plan` | always | keep/remove/prune/rollback plan for accepted and rejected artifacts |

## Standard-Library Runner

Save this as `local_llm_artifact_custody_audit_runner.py` inside the run folder. It uses only Python's standard library.

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


ARTIFACT_FORM_ALIASES = {
    "hf snapshot": "hf_snapshot",
    "huggingface_snapshot": "hf_snapshot",
    "hugging-face-snapshot": "hf_snapshot",
    "local directory": "local_dir",
    "local-dir": "local_dir",
    "ollama package": "ollama_package",
    "ollama-tag": "ollama_package",
    "converted": "converted_derivative",
    "converted-derivative": "converted_derivative",
}

CONVERSION_VALUES_REQUIRING_PROOF = {
    "ollama_import",
    "ollama-hf-shortcut",
    "ollama_hf_shortcut",
    "gguf_conversion",
    "gguf-conversion",
    "quantization",
    "adapter_merge",
    "adapter-merge",
    "conversion",
    "import",
}

UNSAFE_MARKERS = {"pickle", "bin", "pt", "pth", "custom_code", "trust_remote_code", "unknown", "unsafe"}
BLOCKING_DECISIONS = {"blocked", "reject", "rejected", "do_not_load", "do-not-load", "fail"}


def utc_iso() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def slug(value: str) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value).strip().lower())
    return text.strip("-") or "artifact-custody"


def display(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value).strip()


def md_cell(value: Any) -> str:
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=True)
    return display(value).replace("|", "\\|").replace("\n", " ")


def list_value(value: Any) -> list[Any]:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return value
    return [value]


def norm_token(value: Any) -> str:
    text = display(value).lower().replace(" ", "_").replace("-", "_")
    return text


def norm_form(value: Any) -> str:
    text = display(value).lower().strip()
    text = ARTIFACT_FORM_ALIASES.get(text, text)
    return text.replace(" ", "_").replace("-", "_")


def bool_value(value: Any, default: bool = False) -> bool:
    if value is None or value == "":
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y", "pass", "present", "required"}


def unwrap_link(value: Any) -> str:
    text = display(value)
    open_link = "[" * 2
    close_link = "]" * 2
    if text.startswith(open_link) and text.endswith(close_link):
        text = text[2:-2]
        if "|" in text:
            text = text.split("|", 1)[0]
    if "#" in text:
        text = text.split("#", 1)[0]
    return text.strip()


def proof_exists(vault_root: Path, value: Any) -> tuple[bool, str]:
    proof = unwrap_link(value)
    if not proof:
        return False, ""
    if proof.startswith(("http://", "https://")):
        return True, proof
    path_text = proof.replace("/", "\\")
    path = Path(path_text).expanduser()
    candidates: list[Path] = []
    if path.is_absolute():
        candidates.append(path)
    else:
        candidates.append(vault_root / path)
    if not path.suffix:
        candidates.extend(candidate.with_suffix(".md") for candidate in list(candidates))
    for candidate in candidates:
        if candidate.exists():
            return True, str(candidate)
    if "\\" not in path_text and "/" not in proof:
        matches = list(vault_root.rglob(path_text + ".md"))
        if matches:
            return True, str(matches[0])
    return False, proof


def finding(level: str, artifact_id: str, text: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "artifact_id": artifact_id,
        "finding": text,
        "evidence": evidence,
        "action": action,
    }


def first_text(row: dict[str, Any], keys: list[str]) -> str:
    for key in keys:
        value = display(row.get(key))
        if value:
            return value
    return ""


def row_proof(row: dict[str, Any], keys: list[str], vault_root: Path) -> tuple[bool, str]:
    value = first_text(row, keys)
    return proof_exists(vault_root, value)


def has_unsafe_marker(row: dict[str, Any]) -> bool:
    if bool_value(row.get("unsafe_files_present")) or bool_value(row.get("trust_remote_code")) or bool_value(row.get("custom_code_present")):
        return True
    unsafe_value = " ".join(display(item).lower() for item in list_value(row.get("unsafe_file_types") or row.get("unsafe_files")))
    return any(marker in unsafe_value for marker in UNSAFE_MARKERS)


def requires_conversion_proof(row: dict[str, Any], artifact_form: str) -> bool:
    conversion = norm_token(row.get("conversion_or_import") or row.get("conversion") or row.get("import_method"))
    if artifact_form == "converted_derivative":
        return True
    if not conversion or conversion in {"none", "no", "n_a", "na"}:
        return False
    return conversion in {value.replace("-", "_") for value in CONVERSION_VALUES_REQUIRING_PROOF}


def evaluate_artifact(row: dict[str, Any], vault_root: Path) -> dict[str, Any]:
    artifact_id = display(row.get("artifact_id") or row.get("id") or row.get("model_id") or row.get("name"))
    artifact_form = norm_form(row.get("artifact_form") or row.get("form") or row.get("kind"))
    findings: list[dict[str, str]] = []

    if not artifact_id:
        artifact_id = "(missing)"
        findings.append(finding("hold", artifact_id, "Artifact id is missing.", json.dumps(row, ensure_ascii=True)[:160], "Give the artifact a stable artifact_id."))
    if not artifact_form:
        artifact_form = "(missing)"
        findings.append(finding("hold", artifact_id, "Artifact form is missing.", artifact_id, "Set artifact_form to hf_snapshot, local_dir, gguf, ollama_package, converted_derivative, adapter, or a custom value."))

    if not first_text(row, ["source_ref", "source", "repo", "url", "registry"]):
        findings.append(finding("hold", artifact_id, "Source reference is missing.", artifact_id, "Record the registry, URL, internal source, or runtime package source."))
    if not first_text(row, ["revision_or_file", "revision", "tag", "filename", "digest"]):
        findings.append(finding("hold", artifact_id, "Pinned revision, tag, filename, or digest is missing.", artifact_id, "Record the exact source identity used for this artifact."))

    provenance_exists, provenance_resolved = row_proof(row, ["provenance_artifact", "source_card", "acquisition_card"], vault_root)
    if not provenance_exists:
        findings.append(finding("hold", artifact_id, "Provenance artifact does not resolve.", provenance_resolved or "(missing provenance_artifact)", "Link the model acquisition/provenance card."))

    local_identity = first_text(row, ["local_path", "artifact_path", "cache_path", "snapshot_path", "gguf_path", "runtime_model_id"])
    if not local_identity:
        findings.append(finding("hold", artifact_id, "Local path or runtime model id is missing.", artifact_id, "Record the cache path, local file, snapshot directory, GGUF path, or runtime-visible model id."))
    elif first_text(row, ["local_path", "artifact_path", "cache_path", "snapshot_path", "gguf_path"]):
        local_ok, local_resolved = row_proof(row, ["local_path", "artifact_path", "cache_path", "snapshot_path", "gguf_path"], vault_root)
        if not local_ok:
            findings.append(finding("hold", artifact_id, "Local artifact path does not resolve.", local_resolved, "Fix the artifact path or link a runtime-show artifact instead."))

    inventory_exists, inventory_resolved = row_proof(row, ["file_inventory_artifact", "inventory_artifact", "file_list", "metadata_artifact", "runtime_show_artifact"], vault_root)
    if not inventory_exists:
        findings.append(finding("hold", artifact_id, "File inventory or runtime metadata artifact does not resolve.", inventory_resolved or "(missing file_inventory_artifact)", "Link a file list, shard list, GGUF metadata output, or runtime show output."))

    verification_method = norm_token(row.get("verification_method") or row.get("verification") or row.get("hash_method"))
    if not verification_method:
        findings.append(finding("hold", artifact_id, "Verification method is missing.", artifact_id, "Record sha256, digest, hf_cache_verify, runtime_show, scanner, or partial."))
    verification_value = first_text(row, ["hash_or_digest", "sha256", "digest", "checksum"])
    verification_exists, verification_resolved = row_proof(row, ["verification_artifact", "hash_artifact", "digest_artifact", "scanner_artifact"], vault_root)
    if not verification_value and not verification_exists:
        findings.append(finding("hold", artifact_id, "Verification value or artifact is missing.", verification_resolved or "(missing verification evidence)", "Record a hash/digest or link verification output."))
    if verification_method in {"partial", "best_effort", "unknown"} and not first_text(row, ["partial_verification_reason", "verification_limitation", "waiver_reason"]):
        findings.append(finding("hold", artifact_id, "Partial verification has no limitation note.", verification_method, "Explain why full verification is unavailable and what risk remains."))

    unsafe_decision = norm_token(row.get("unsafe_file_decision") or row.get("unsafe_decision") or row.get("trust_decision"))
    if not unsafe_decision:
        findings.append(finding("hold", artifact_id, "Unsafe-file decision is missing.", artifact_id, "Record none, reviewed, sandboxed, learning-only, blocked, or equivalent."))
    if unsafe_decision in BLOCKING_DECISIONS:
        findings.append(finding("fail", artifact_id, "Artifact is marked blocked or rejected.", unsafe_decision, "Do not use this artifact as serving or deployment evidence."))
    if has_unsafe_marker(row):
        review_exists, review_resolved = row_proof(row, ["review_artifact", "scanner_artifact", "sandbox_artifact", "unsafe_review_artifact"], vault_root)
        if not review_exists:
            findings.append(finding("hold", artifact_id, "Unsafe or custom-code artifact has no review evidence.", review_resolved or "(missing review_artifact)", "Link scanner output, code review, sandbox notes, or choose a safer artifact."))
        if unsafe_decision in {"none", "no", "n_a", "na"}:
            findings.append(finding("hold", artifact_id, "Unsafe marker conflicts with a 'none' decision.", unsafe_decision, "Record a real review, sandbox, learning-only, or blocked decision."))

    conversion_needed = requires_conversion_proof(row, artifact_form)
    conversion_value = norm_token(row.get("conversion_or_import") or row.get("conversion") or row.get("import_method"))
    if not conversion_value:
        findings.append(finding("hold", artifact_id, "Conversion/import decision is missing.", artifact_id, "Record none, ollama_import, ollama_hf_shortcut, gguf_conversion, quantization, or another explicit decision."))
    if conversion_needed:
        conversion_exists, conversion_resolved = row_proof(row, ["conversion_artifact", "import_artifact", "modelfile", "converter_log", "command_artifact"], vault_root)
        if not conversion_exists:
            findings.append(finding("hold", artifact_id, "Conversion or import proof does not resolve.", conversion_resolved or "(missing conversion_artifact)", "Link Modelfile, command output, converter log, runtime show output, or import proof."))
        if artifact_form == "converted_derivative" and not first_text(row, ["derived_output_hash", "output_hash", "converted_hash"]):
            findings.append(finding("hold", artifact_id, "Converted derivative has no output hash.", artifact_id, "Record a hash or digest for the derived artifact."))

    handoff_exists, handoff_resolved = row_proof(row, ["runtime_handoff_artifact", "compatibility_artifact", "serving_handoff_artifact", "runtime_show_artifact"], vault_root)
    if not handoff_exists:
        findings.append(finding("hold", artifact_id, "Runtime handoff artifact does not resolve.", handoff_resolved or "(missing runtime_handoff_artifact)", "Link the runtime compatibility card, serving run sheet, or runtime show output."))

    if not first_text(row, ["cleanup_plan", "rollback_plan", "retention_plan"]):
        findings.append(finding("hold", artifact_id, "Cleanup or retention plan is missing.", artifact_id, "Record how accepted and rejected artifacts will be kept, pruned, removed, or reacquired."))

    if bool_value(row.get("rejected")) or bool_value(row.get("failed")):
        findings.append(finding("fail", artifact_id, "Artifact is explicitly rejected or failed.", artifact_id, "Keep it out of compatibility, benchmark, and deployment evidence."))

    if any(item["level"] == "fail" for item in findings):
        status = "fail"
        decision = "artifact_custody_failed"
    elif findings:
        status = "hold"
        decision = "artifact_custody_incomplete"
    else:
        status = "pass"
        decision = "artifact_custody_ready"

    return {
        "artifact_id": artifact_id,
        "artifact_form": artifact_form,
        "status": status,
        "decision": decision,
        "source_ref": first_text(row, ["source_ref", "source", "repo", "url", "registry"]),
        "revision_or_file": first_text(row, ["revision_or_file", "revision", "tag", "filename", "digest"]),
        "local_identity": local_identity,
        "verification_method": verification_method,
        "conversion_or_import": conversion_value,
        "next_action": findings[0]["action"] if findings else "Use this artifact custody output as the handoff to compatibility and serving evidence.",
        "findings": findings,
    }


def csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = [
        "artifact_id",
        "artifact_form",
        "status",
        "decision",
        "source_ref",
        "revision_or_file",
        "local_identity",
        "verification_method",
        "conversion_or_import",
        "next_action",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def render_markdown(record: dict[str, Any]) -> str:
    lines = [
        f"# Local LLM Artifact Custody Audit - {record['run_id']}",
        "",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Artifacts: `{record['artifact_count']}`",
        f"- Pass/Hold/Fail: `{record['pass_count']}` / `{record['hold_count']}` / `{record['fail_count']}`",
        f"- Findings: `{record['finding_count']}`",
        f"- Next action: {record['next_action']}",
        "",
        "## Artifacts",
        "",
        "| Artifact | Form | Status | Source | Revision/File | Verification | Conversion/Import | Next action |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for row in record["artifacts"]:
        lines.append(
            "| "
            + " | ".join([
                md_cell(row["artifact_id"]),
                md_cell(row["artifact_form"]),
                md_cell(row["status"]),
                md_cell(row["source_ref"]),
                md_cell(row["revision_or_file"]),
                md_cell(row["verification_method"]),
                md_cell(row["conversion_or_import"]),
                md_cell(row["next_action"]),
            ])
            + " |"
        )
    lines.extend(["", "## Findings", ""])
    if record["findings"]:
        lines.append("| Level | Artifact | Finding | Evidence | Action |")
        lines.append("|---|---|---|---|---|")
        for item in record["findings"]:
            lines.append(
                "| "
                + " | ".join([
                    md_cell(item["level"]),
                    md_cell(item["artifact_id"]),
                    md_cell(item["finding"]),
                    md_cell(item["evidence"]),
                    md_cell(item["action"]),
                ])
                + " |"
            )
    else:
        lines.append("No findings.")
    return "\n".join(lines) + "\n"


def load_manifest() -> tuple[Path, dict[str, Any]]:
    manifest_value = os.environ.get("LOCAL_LLM_ARTIFACT_CUSTODY_AUDIT_MANIFEST")
    if not manifest_value:
        raise ValueError("Set LOCAL_LLM_ARTIFACT_CUSTODY_AUDIT_MANIFEST to a JSON manifest path.")
    manifest_path = Path(manifest_value).expanduser().resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict):
        raise ValueError("Manifest must be a JSON object.")
    return manifest_path, manifest


def main() -> int:
    manifest_path, manifest = load_manifest()
    base_for_relative = manifest_path.parent
    run_root_value = os.environ.get("LOCAL_LLM_ARTIFACT_CUSTODY_AUDIT_RUN_ROOT") or manifest.get("run_root") or base_for_relative
    run_root = Path(str(run_root_value)).expanduser()
    if not run_root.is_absolute():
        run_root = base_for_relative / run_root
    run_root = run_root.resolve()

    vault_root_value = manifest.get("vault_root") or os.environ.get("LOCAL_LLM_ARTIFACT_CUSTODY_AUDIT_VAULT_ROOT") or "."
    vault_root = Path(str(vault_root_value)).expanduser()
    if not vault_root.is_absolute():
        vault_root = base_for_relative / vault_root
    vault_root = vault_root.resolve()

    run_id = display(manifest.get("run_id") or os.environ.get("LOCAL_LLM_ARTIFACT_CUSTODY_AUDIT_RUN_ID") or f"{utc_stamp()}-{slug(run_root.name)}")
    output_root_value = manifest.get("output_root") or os.environ.get("LOCAL_LLM_ARTIFACT_CUSTODY_AUDIT_OUTPUT_ROOT") or "artifact-custody-audits"
    output_root = Path(str(output_root_value)).expanduser()
    if not output_root.is_absolute():
        output_root = run_root / output_root
    output_root = output_root.resolve()
    output_dir = output_root / run_id
    output_dir.mkdir(parents=True, exist_ok=True)

    artifacts = manifest.get("artifacts") or manifest.get("rows") or []
    if not isinstance(artifacts, list) or not all(isinstance(row, dict) for row in artifacts):
        raise ValueError("Manifest artifacts must be a list of objects.")

    evaluated = [evaluate_artifact(dict(row), vault_root) for row in artifacts]
    findings = [item for row in evaluated for item in row["findings"]]
    if not evaluated:
        findings.append(finding("hold", "(manifest)", "Manifest has no artifacts.", str(manifest_path), "Add at least one artifact custody row."))

    fail_findings = sum(1 for item in findings if item["level"] == "fail")
    hold_findings = sum(1 for item in findings if item["level"] == "hold")
    pass_count = sum(1 for row in evaluated if row["status"] == "pass")
    hold_count = sum(1 for row in evaluated if row["status"] == "hold")
    fail_count = sum(1 for row in evaluated if row["status"] == "fail")

    if fail_findings:
        status = "fail"
        decision = "artifact_custody_failed"
        next_action = "Reject or quarantine the failed artifact before compatibility, serving, benchmark, or deployment evidence depends on it."
    elif hold_findings:
        status = "hold"
        decision = "artifact_custody_incomplete"
        next_action = "Complete the first missing source, verification, unsafe-file, conversion/import, handoff, or cleanup field."
    else:
        status = "pass"
        decision = "artifact_custody_ready"
        next_action = "Link this audit output from runtime compatibility, first endpoint, and deployment readiness evidence."

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "next_action": next_action,
        "manifest_path": str(manifest_path),
        "run_root": str(run_root),
        "vault_root": str(vault_root),
        "artifact_count": len(evaluated),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "finding_count": len(findings),
        "artifacts": evaluated,
        "findings": findings,
        "outputs": {},
    }

    json_path = output_dir / f"{run_id}-artifact-custody-audit.json"
    markdown_path = output_dir / f"{run_id}-artifact-custody-audit.md"
    csv_path = output_dir / f"{run_id}-artifact-custody-audit.csv"
    jsonl_path = output_root / "artifact-custody-audits.jsonl"
    record["outputs"] = {
        "json": str(json_path),
        "markdown": str(markdown_path),
        "csv": str(csv_path),
        "jsonl": str(jsonl_path),
    }

    csv_write(csv_path, evaluated)
    json_path.write_text(json.dumps(record, indent=2, ensure_ascii=True), encoding="utf-8")
    markdown_path.write_text(render_markdown(record), encoding="utf-8")
    with jsonl_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=True) + "\n")

    print(json.dumps({
        "status": status,
        "decision": decision,
        "run_id": run_id,
        "artifact_count": record["artifact_count"],
        "pass_count": record["pass_count"],
        "hold_count": record["hold_count"],
        "fail_count": record["fail_count"],
        "finding_count": record["finding_count"],
        "output_dir": str(output_dir),
    }, indent=2))
    return 0 if status == "pass" else 1 if status == "hold" else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(json.dumps({"status": "error", "decision": "runner_exception", "error": str(exc)}, indent=2), file=sys.stderr)
        raise SystemExit(3)
```

## PowerShell Run

```powershell
$env:LOCAL_LLM_ARTIFACT_CUSTODY_AUDIT_MANIFEST = "D:\llm-runs\artifact-custody\artifact-custody-manifest.json"
$env:LOCAL_LLM_ARTIFACT_CUSTODY_AUDIT_VAULT_ROOT = "D:\Vaults\PersonalKB"
python .\local_llm_artifact_custody_audit_runner.py
```

## Reading The Result

| Runner status | Meaning | Next route |
|---|---|---|
| `pass/artifact_custody_ready` | every artifact row has source identity, local bytes or runtime id, inventory, verification, unsafe-file decision, conversion/import decision, runtime handoff, and cleanup plan | link the output in [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]] and [[LLM/Study/LLM Deployment Readiness Audit Runner|LLM Deployment Readiness Audit Runner]] |
| `hold/artifact_custody_incomplete` | at least one field or proof artifact is missing, partial, or unresolved | complete the first missing evidence row before serving or benchmarking |
| `fail/artifact_custody_failed` | the artifact is rejected, blocked, unsafe without an acceptable decision, or explicitly failed | quarantine or replace the artifact before using downstream evidence |

## Completion Gate

This runner is complete for one artifact custody pass when:

- [ ] every accepted artifact has source, revision/tag/file/digest, artifact form, and provenance artifact
- [ ] every accepted artifact has local path or runtime model id plus inventory or metadata proof
- [ ] every accepted artifact has verification method plus hash/digest or verification artifact
- [ ] unsafe files, custom code, and `trust_remote_code` have review evidence and a decision
- [ ] conversion or import rows have command, Modelfile, converter log, runtime show, or output hash proof
- [ ] converted derivatives have a derived output hash
- [ ] runtime compatibility or serving handoff is linked
- [ ] cleanup or retention plan is explicit
- [ ] output JSON, Markdown, CSV, and JSONL files are linked from compatibility, endpoint, or deployment evidence

## References

- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Model Acquisition and License Gate Runner]]
- [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab]]
- [[LLM/Study/Local LLM Model Metadata Card Runner]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM First Model Pull Gate]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner]]
- [[LLM/Study/LLM Deployment Readiness Audit Runner]]
- [[LLM/Study/LLM Mastery Evidence Audit Runner]]
- [[LLM/Study/Local LLM Security and Privacy Runner]]
