---
tags: [study, llm, local-llm, model-acquisition, license, provenance, safety, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice]
last-verified: 2026-06-16
---

# Local LLM Model Acquisition and License Gate Runner

> **One-line summary** Audit a candidate model's source, model card, license, gated-access state, exact artifact, unsafe-file posture, and requested use before downloading, serving, benchmarking, or deploying it locally.

Use this after [[LLM/Study/Local LLM Workload to Model Selection Playbook|Local LLM Workload to Model Selection Playbook]] identifies a candidate and before [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Local LLM Artifact Download Cache and Conversion Lab]], [[LLM/Study/Local LLM Model Metadata Card Runner|Local LLM Model Metadata Card Runner]], [[LLM/Study/Local LLM Artifact Custody Audit Runner|Local LLM Artifact Custody Audit Runner]], [[LLM/Study/Local LLM Runtime Compatibility Runner|Local LLM Runtime Compatibility Runner]], or [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]] relies on that model.

This runner does not scrape a model registry, download model files, interpret a license as legal advice, or decide whether a model is morally acceptable. It audits evidence you already saved: model card capture, license capture, gated-access proof, intended-use decision, exact revision/tag/file, artifact format, unsafe-file review, scan status, cache plan, and requested local use.

## Official Anchors

- Hugging Face model cards are `README.md` files with metadata and descriptions; the docs say they should describe the model, intended uses, limitations, training data, and evaluation results: [Hugging Face model cards](https://huggingface.co/docs/hub/en/model-cards).
- Hugging Face gated models grant access to individual users, and users may need to share account/contact information or satisfy additional author fields before accessing files: [Hugging Face gated models](https://huggingface.co/docs/hub/en/models-gated).
- Hugging Face runs repository files through malware scanning at each commit, while a missing badge can mean pending or errored scanning rather than safety: [Hugging Face malware scanning](https://huggingface.co/docs/hub/en/security-malware).
- Hugging Face warns that pickle files can execute arbitrary code and recommends loading models from trusted users/organizations or safer formats: [Hugging Face pickle scanning](https://huggingface.co/docs/hub/en/security-pickle).
- Safetensors is documented as a simple tensor format designed for safe storage compared with pickle: [Hugging Face Safetensors](https://huggingface.co/docs/safetensors/index).
- SPDX license identifiers provide standardized short identifiers and canonical license URLs for efficient license identification: [SPDX license list](https://spdx.github.io/spdx-spec/v2.3/SPDX-license-list/).
- The Open Source AI Definition distinguishes open-source AI from merely available weights and requires freedoms to use, study, modify, share, plus preferred modification forms such as data information, code, and parameters: [Open Source AI Definition 1.0](https://opensource.org/ai/open-source-ai-definition).

## What This Proves

| Gate | Evidence checked | Why it matters |
|---|---|---|
| Workload and data boundary | workload, requested use, data sensitivity | a technically runnable model may still be wrong for private, commercial, shared, or service use |
| Source identity | registry or URL, model id, model card capture, date checked | prevents a model name from becoming timeless proof |
| License and terms | license id, URL/text capture, extra terms, allowed requested scopes | catches learning-only, non-commercial, gated, no-redistribution, or service-restricted candidates before serving |
| Gated access | none/accepted/pending/denied plus proof when accepted | avoids mirroring or using artifacts before terms are accepted by the actual user/account |
| Artifact pinning | artifact format, exact revision/tag/file/digest, reproducibility requirement | keeps benchmarks and quality rows tied to a concrete candidate |
| Unsafe-file posture | safe format, pickle-like files, custom code, `trust_remote_code`, scan status | prevents code-execution risk from slipping into local serving |
| Handoff | acquisition decision, next route, cache/download plan | routes pass/hold/fail into artifact download, custody, metadata, or rejection |

Academic bridge: "open weights" is not the same thing as "open source AI," and "can load locally" is not the same thing as "allowed and safe to use." The model artifact is part of the experimental method. License, provenance, revision, serialization format, and source trust are variables in the local inference setup.

## Manifest Shape

Save `model-acquisition-license-manifest.json` next to the runner:

```json
{
  "run_id": "model-acquisition-qwen-baseline",
  "run_root": "D:/llm-runs/model-acquisition",
  "vault_root": "D:/Vaults/PersonalKB",
  "candidate": {
    "model_id": "org/model",
    "workload": "private local assistant",
    "data_boundary": "personal",
    "requested_use": ["local_personal", "benchmark", "rag"],
    "source_registry": "Hugging Face Hub",
    "source_url": "https://huggingface.co/org/model",
    "model_card_url": "https://huggingface.co/org/model/blob/<rev>/README.md",
    "model_card_reviewed": true,
    "model_card_date_checked": "2026-06-16",
    "intended_use_matches": "yes",
    "limitations_recorded": true,
    "training_data_recorded": "summary",
    "claims_open_source": false,
    "open_source_basis": "open weights, not full OSAI evidence"
  },
  "license": {
    "license_id": "apache-2.0",
    "license_url": "https://www.apache.org/licenses/LICENSE-2.0",
    "license_text_captured": true,
    "extra_terms": "",
    "local_personal_allowed": true,
    "benchmark_allowed": true,
    "commercial_allowed": true,
    "redistribution_allowed": true,
    "derivative_allowed": true,
    "service_allowed": true,
    "requires_attribution": true,
    "requires_share_alike": false
  },
  "access": {
    "gated_access": "none",
    "access_status": "not_required",
    "terms_accepted_by": "",
    "access_proof": ""
  },
  "artifact": {
    "artifact_format": "safetensors",
    "artifact_ref": "model.safetensors shards",
    "revision_or_tag": "<commit hash or immutable tag>",
    "reproducibility_required": true,
    "digest_or_revision_proof": "<commit hash, digest, or hash artifact>",
    "download_method": "hf download --revision <rev>",
    "cache_plan": "D:/Models/hf/org-model/<rev>",
    "unsafe_file_types": [],
    "trust_remote_code": "no",
    "malware_scan_status": "ok",
    "pickle_scan_status": "not_applicable",
    "preferred_safe_format_available": true,
    "unsafe_review_artifact": ""
  },
  "artifacts": {
    "model_card_capture": "model-card.md",
    "license_capture": "license.txt",
    "gated_access_proof": "",
    "source_snapshot_proof": "source-snapshot.json",
    "review_note": "acquisition-review.md"
  }
}
```

Status meanings:

| Status | Meaning |
|---|---|
| `pass/acquisition_ready` | evidence supports acquiring this artifact for the requested local use and next route |
| `hold/acquisition_incomplete` | evidence is missing or ambiguous; gather proof before download/serve |
| `fail/acquisition_blocked` | requested use contradicts license/access/safety evidence, or the artifact should not be loaded |

## Standard-Library Runner

Save this as `local_llm_model_acquisition_license_gate_runner.py` inside the run folder, or extract it from this note. It uses only Python's standard library.

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


SAFE_FORMATS = {"safetensors", "gguf", "ollama_package", "onnx", "mlx", "flax", "tensorflow"}
UNSAFE_FORMATS = {"pickle", "pytorch_bin", "bin", "pt", "pth", "ckpt", "custom_code", "unknown"}
FLOATING_REVISIONS = {"", "main", "master", "latest", "dev", "nightly", "head"}
ACCESS_PASS = {"none", "not_required", "accepted", "approved", "granted"}
ACCESS_HOLD = {"pending", "requested", "manual_review", "unknown", ""}
ACCESS_FAIL = {"denied", "rejected", "blocked", "not_allowed"}
SCAN_FAIL = {"infected", "unsafe", "suspicious", "malware", "blocked", "fail", "failed"}
SCAN_HOLD = {"pending", "unknown", "missing", "errored", "error", ""}
REQUEST_SCOPE_TO_LICENSE_FLAG = {
    "local_personal": "local_personal_allowed",
    "personal": "local_personal_allowed",
    "benchmark": "benchmark_allowed",
    "research": "benchmark_allowed",
    "commercial": "commercial_allowed",
    "redistribution": "redistribution_allowed",
    "share": "redistribution_allowed",
    "derivative": "derivative_allowed",
    "fine_tune": "derivative_allowed",
    "adapter": "derivative_allowed",
    "service": "service_allowed",
    "shared_service": "service_allowed",
    "rag": "local_personal_allowed",
}


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def clean(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def norm(value: Any) -> str:
    return clean(value).lower().replace(" ", "_").replace("-", "_")


def as_bool(value: Any, default: bool | None = False) -> bool | None:
    if value is None or value == "":
        return default
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    text = norm(value)
    if text in {"1", "true", "yes", "y", "pass", "allowed", "accepted", "ok"}:
        return True
    if text in {"0", "false", "no", "n", "fail", "blocked", "denied", "not_allowed"}:
        return False
    return default


def list_value(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [clean(item) for item in value if clean(item)]
    if isinstance(value, tuple):
        return [clean(item) for item in value if clean(item)]
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return []
        if text.startswith("["):
            try:
                parsed = json.loads(text)
                if isinstance(parsed, list):
                    return [clean(item) for item in parsed if clean(item)]
            except json.JSONDecodeError:
                pass
        return [part.strip() for part in re.split(r"[,;]", text) if part.strip()]
    return [clean(value)] if clean(value) else []


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


def resolve_artifact(raw: Any, manifest_dir: Path, run_root: Path | None, vault_root: Path | None) -> Path | None:
    text = clean(raw)
    if not text:
        return None
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


def artifact_exists(raw: Any, manifest_dir: Path, run_root: Path | None, vault_root: Path | None) -> tuple[bool, str]:
    path = resolve_artifact(raw, manifest_dir, run_root, vault_root)
    if not path:
        return False, ""
    return path.exists(), str(path)


def check_required_text(checks: list[dict[str, Any]], group: dict[str, Any], gate: str, fields: list[str]) -> None:
    for field in fields:
        if clean(group.get(field)):
            add_check(checks, "pass", gate, f"{field} is recorded", clean(group.get(field)))
        else:
            add_check(checks, "hold", gate, f"{field} is missing")


def check_artifacts(
    checks: list[dict[str, Any]],
    artifacts: dict[str, Any],
    manifest_dir: Path,
    run_root: Path | None,
    vault_root: Path | None,
) -> None:
    for key in ("model_card_capture", "license_capture", "source_snapshot_proof", "review_note"):
        exists, path = artifact_exists(artifacts.get(key), manifest_dir, run_root, vault_root)
        if exists:
            add_check(checks, "pass", "artifact_inventory", f"{key} exists", path)
        else:
            add_check(checks, "hold", "artifact_inventory", f"{key} is missing", clean(artifacts.get(key)))
    if clean(artifacts.get("gated_access_proof")):
        exists, path = artifact_exists(artifacts.get("gated_access_proof"), manifest_dir, run_root, vault_root)
        add_check(checks, "pass" if exists else "hold", "artifact_inventory", "gated_access_proof checked", path or clean(artifacts.get("gated_access_proof")))


def check_license(checks: list[dict[str, Any]], candidate: dict[str, Any], license_info: dict[str, Any]) -> None:
    license_id = clean(license_info.get("license_id"))
    if license_id:
        add_check(checks, "pass", "license", "license id is recorded", license_id)
    else:
        add_check(checks, "hold", "license", "license id is missing")
    if clean(license_info.get("license_url")) or as_bool(license_info.get("license_text_captured"), False):
        add_check(checks, "pass", "license", "license URL or captured text is recorded", clean(license_info.get("license_url")))
    else:
        add_check(checks, "hold", "license", "license URL/text capture is missing")

    requested = [norm(item) for item in list_value(candidate.get("requested_use"))]
    if not requested:
        add_check(checks, "hold", "license", "requested_use is missing")
    for scope in requested:
        flag = REQUEST_SCOPE_TO_LICENSE_FLAG.get(scope)
        if not flag:
            add_check(checks, "hold", "license", f"requested use scope is not mapped to a license flag: {scope}")
            continue
        allowed = as_bool(license_info.get(flag), None)
        if allowed is True:
            add_check(checks, "pass", "license", f"requested use is allowed by recorded license flag", f"{scope} -> {flag}")
        elif allowed is False:
            add_check(checks, "fail", "license", f"requested use is blocked by recorded license flag", f"{scope} -> {flag}=false")
        else:
            add_check(checks, "hold", "license", f"requested use lacks license flag evidence", f"{scope} -> {flag}")

    license_norm = norm(license_id)
    if license_norm and license_norm not in {"apache_2.0", "mit", "bsd_3_clause", "bsd_2_clause", "cc_by_4.0"}:
        if clean(license_info.get("extra_terms")) or as_bool(license_info.get("license_text_captured"), False):
            add_check(checks, "pass", "license", "non-simple or custom license has extra terms/text evidence", clean(license_info.get("extra_terms")))
        else:
            add_check(checks, "hold", "license", "non-simple or custom license needs captured terms", license_id)


def check_access(checks: list[dict[str, Any]], access: dict[str, Any], artifacts: dict[str, Any], manifest_dir: Path, run_root: Path | None, vault_root: Path | None) -> None:
    gated = norm(access.get("gated_access"))
    status = norm(access.get("access_status"))
    if gated in {"none", "not_required", "no"}:
        add_check(checks, "pass", "gated_access", "gated access is not required", gated)
        return
    if status in ACCESS_FAIL:
        add_check(checks, "fail", "gated_access", "gated access status blocks acquisition", status)
        return
    if status in ACCESS_HOLD:
        add_check(checks, "hold", "gated_access", "gated access is not accepted yet", status)
        return
    if status in ACCESS_PASS:
        proof = clean(access.get("access_proof")) or clean(artifacts.get("gated_access_proof"))
        exists, path = artifact_exists(proof, manifest_dir, run_root, vault_root)
        if proof and exists:
            add_check(checks, "pass", "gated_access", "gated access acceptance proof exists", path)
        elif proof:
            add_check(checks, "hold", "gated_access", "gated access proof path is recorded but missing", proof)
        else:
            add_check(checks, "hold", "gated_access", "gated model needs acceptance proof")
        return
    add_check(checks, "hold", "gated_access", "gated access status is ambiguous", status)


def check_artifact_safety(checks: list[dict[str, Any]], artifact: dict[str, Any]) -> None:
    fmt = norm(artifact.get("artifact_format"))
    unsafe_types = {norm(item) for item in list_value(artifact.get("unsafe_file_types"))}
    trust_remote_code = norm(artifact.get("trust_remote_code"))
    if fmt in SAFE_FORMATS:
        add_check(checks, "pass", "artifact_safety", "artifact format is in the safe/preferred set", fmt)
    elif fmt in UNSAFE_FORMATS or not fmt:
        add_check(checks, "hold", "artifact_safety", "artifact format is unsafe or unknown", fmt)
    else:
        add_check(checks, "hold", "artifact_safety", "artifact format needs explicit review", fmt)

    if unsafe_types:
        if clean(artifact.get("unsafe_review_artifact")):
            add_check(checks, "hold", "artifact_safety", "unsafe file types are present with review artifact; manual review still required", ",".join(sorted(unsafe_types)))
        else:
            add_check(checks, "fail", "artifact_safety", "unsafe file types are present without review artifact", ",".join(sorted(unsafe_types)))
    else:
        add_check(checks, "pass", "artifact_safety", "no unsafe file types recorded")

    if trust_remote_code in {"yes", "true", "required"}:
        if clean(artifact.get("unsafe_review_artifact")):
            add_check(checks, "hold", "artifact_safety", "trust_remote_code is required and has a review artifact", clean(artifact.get("unsafe_review_artifact")))
        else:
            add_check(checks, "fail", "artifact_safety", "trust_remote_code is required without review artifact")
    elif trust_remote_code:
        add_check(checks, "pass", "artifact_safety", "trust_remote_code is not required", trust_remote_code)
    else:
        add_check(checks, "hold", "artifact_safety", "trust_remote_code decision is missing")

    for key in ("malware_scan_status", "pickle_scan_status"):
        status = norm(artifact.get(key))
        if status in SCAN_FAIL:
            add_check(checks, "fail", "artifact_safety", f"{key} blocks acquisition", status)
        elif status in SCAN_HOLD:
            add_check(checks, "hold", "artifact_safety", f"{key} is missing, pending, or errored", status)
        else:
            add_check(checks, "pass", "artifact_safety", f"{key} is acceptable or not applicable", status)


def check_pinning(checks: list[dict[str, Any]], artifact: dict[str, Any]) -> None:
    check_required_text(checks, artifact, "artifact_identity", ["artifact_format", "artifact_ref", "revision_or_tag", "download_method", "cache_plan"])
    revision = clean(artifact.get("revision_or_tag"))
    if as_bool(artifact.get("reproducibility_required"), True):
        if norm(revision) in FLOATING_REVISIONS:
            add_check(checks, "fail", "artifact_identity", "reproducibility is required but revision/tag is floating", revision)
        elif clean(artifact.get("digest_or_revision_proof")):
            add_check(checks, "pass", "artifact_identity", "digest or revision proof is recorded", clean(artifact.get("digest_or_revision_proof")))
        else:
            add_check(checks, "hold", "artifact_identity", "digest or revision proof is missing")
    else:
        add_check(checks, "hold", "artifact_identity", "reproducibility is marked not required; downstream benchmarks should not rely on exact bytes", revision)


def check_open_source_claim(checks: list[dict[str, Any]], candidate: dict[str, Any]) -> None:
    if not as_bool(candidate.get("claims_open_source"), False):
        add_check(checks, "pass", "open_source_claim", "candidate is not claiming open-source AI status")
        return
    basis = clean(candidate.get("open_source_basis"))
    if not basis:
        add_check(checks, "hold", "open_source_claim", "open-source AI claim lacks basis")
    elif "open weights" in basis.lower() and "not" in basis.lower():
        add_check(checks, "hold", "open_source_claim", "basis distinguishes open weights from open-source AI", basis)
    elif "osi" in basis.lower() or "data information" in basis.lower():
        add_check(checks, "pass", "open_source_claim", "open-source AI basis is recorded", basis)
    else:
        add_check(checks, "hold", "open_source_claim", "open-source AI basis needs review", basis)


def audit_manifest(manifest_path: Path) -> dict[str, Any]:
    manifest_dir = manifest_path.parent
    manifest = load_json(manifest_path)
    run_root = Path(clean(manifest.get("run_root"))).expanduser() if clean(manifest.get("run_root")) else manifest_dir
    vault_root = Path(clean(manifest.get("vault_root"))).expanduser() if clean(manifest.get("vault_root")) else None
    candidate = manifest.get("candidate") if isinstance(manifest.get("candidate"), dict) else {}
    license_info = manifest.get("license") if isinstance(manifest.get("license"), dict) else {}
    access = manifest.get("access") if isinstance(manifest.get("access"), dict) else {}
    artifact = manifest.get("artifact") if isinstance(manifest.get("artifact"), dict) else {}
    artifacts = manifest.get("artifacts") if isinstance(manifest.get("artifacts"), dict) else {}
    checks: list[dict[str, Any]] = []

    check_required_text(
        checks,
        candidate,
        "candidate_identity",
        ["model_id", "workload", "data_boundary", "source_registry", "source_url", "model_card_url", "model_card_date_checked"],
    )
    if as_bool(candidate.get("model_card_reviewed"), False):
        add_check(checks, "pass", "candidate_identity", "model card was reviewed")
    else:
        add_check(checks, "hold", "candidate_identity", "model card reviewed flag is missing or false")
    if norm(candidate.get("intended_use_matches")) in {"yes", "pass", "matches"}:
        add_check(checks, "pass", "candidate_identity", "intended use matches workload", clean(candidate.get("intended_use_matches")))
    elif norm(candidate.get("intended_use_matches")) in {"no", "false", "mismatch"}:
        add_check(checks, "fail", "candidate_identity", "intended use does not match workload", clean(candidate.get("intended_use_matches")))
    else:
        add_check(checks, "hold", "candidate_identity", "intended use match is partial or unknown", clean(candidate.get("intended_use_matches")))
    if as_bool(candidate.get("limitations_recorded"), False):
        add_check(checks, "pass", "candidate_identity", "limitations were recorded")
    else:
        add_check(checks, "hold", "candidate_identity", "limitations are not recorded")
    if clean(candidate.get("training_data_recorded")):
        add_check(checks, "pass", "candidate_identity", "training data disclosure state is recorded", clean(candidate.get("training_data_recorded")))
    else:
        add_check(checks, "hold", "candidate_identity", "training data disclosure state is missing")

    check_open_source_claim(checks, candidate)
    check_license(checks, candidate, license_info)
    check_access(checks, access, artifacts, manifest_dir, run_root, vault_root)
    check_pinning(checks, artifact)
    check_artifact_safety(checks, artifact)
    check_artifacts(checks, artifacts, manifest_dir, run_root, vault_root)

    statuses = {check["status"] for check in checks}
    if "fail" in statuses:
        status = "fail"
        decision = "acquisition_blocked"
        next_route = "Reject or repair source/license/access/safety before download."
    elif "hold" in statuses:
        status = "hold"
        decision = "acquisition_incomplete"
        next_route = "Collect missing model-card, license, gated-access, revision, or safety proof."
    else:
        status = "pass"
        decision = "acquisition_ready"
        next_route = "Proceed to artifact download/cache/conversion and custody audit."

    return {
        "run_id": clean(manifest.get("run_id")) or manifest_path.stem,
        "generated_at": now_iso(),
        "manifest": str(manifest_path),
        "status": status,
        "decision": decision,
        "next_route": next_route,
        "model_id": clean(candidate.get("model_id")),
        "requested_use": list_value(candidate.get("requested_use")),
        "checks": checks,
    }


def write_outputs(result: dict[str, Any], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    stem = "model-acquisition-license-results"
    write_json(output_dir / f"{stem}.json", result)
    with (output_dir / f"{stem}.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["status", "gate", "message", "evidence"])
        writer.writeheader()
        writer.writerows(result["checks"])
    with (output_dir / f"{stem}.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(result, ensure_ascii=True) + "\n")
    lines = [
        f"# Model Acquisition License Gate: {result['status']} / {result['decision']}",
        "",
        f"- Run id: {result['run_id']}",
        f"- Generated: {result['generated_at']}",
        f"- Model id: {result.get('model_id') or ''}",
        f"- Requested use: {', '.join(result.get('requested_use') or [])}",
        f"- Next route: {result['next_route']}",
        "",
        "| Status | Gate | Message | Evidence |",
        "|---|---|---|---|",
    ]
    for check in result["checks"]:
        lines.append(f"| {md_cell(check['status'])} | {md_cell(check['gate'])} | {md_cell(check['message'])} | {md_cell(check.get('evidence', ''))} |")
    (output_dir / f"{stem}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    manifest_path = Path(argv[1]).expanduser() if len(argv) > 1 else Path(os.environ.get("LOCAL_LLM_ACQUISITION_MANIFEST", "model-acquisition-license-manifest.json")).expanduser()
    if not manifest_path.exists():
        print(f"Manifest not found: {manifest_path}", file=sys.stderr)
        return 2
    result = audit_manifest(manifest_path)
    output_dir = Path(os.environ.get("LOCAL_LLM_ACQUISITION_OUTPUT_DIR", "")).expanduser() if os.environ.get("LOCAL_LLM_ACQUISITION_OUTPUT_DIR") else manifest_path.parent
    write_outputs(result, output_dir)
    print(json.dumps({"status": result["status"], "decision": result["decision"], "output_dir": str(output_dir)}, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
```

## Verification Fixtures

Use local fixtures before trusting the runner on a real candidate:

| Fixture | Expected decision |
|---|---|
| Reviewed model card, license capture, accepted requested use, no gate, pinned revision, safetensors/GGUF/Ollama package, scan ok, source artifacts present | `pass/acquisition_ready` |
| Requested commercial use with `commercial_allowed: false` | `fail/acquisition_blocked` |
| Gated model with `access_status: pending` | `hold/acquisition_incomplete` |
| Gated model with `access_status: denied` | `fail/acquisition_blocked` |
| Reproducibility required but revision is `main` or `latest` | `fail/acquisition_blocked` |
| Unsafe pickle/PyTorch files with no review artifact | `fail/acquisition_blocked` |
| Malware or pickle scan marked unsafe/suspicious/infected | `fail/acquisition_blocked` |
| Open-source AI claim with only "open weights" evidence | `hold/acquisition_incomplete` |

## Handoff Map

| Need | Next note |
|---|---|
| Candidate choice from workload | [[LLM/Study/Local LLM Workload to Model Selection Playbook]] |
| Manual acquisition checklist | [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]] |
| File download/cache/conversion proof | [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab]] |
| Normalized metadata | [[LLM/Study/Local LLM Model Metadata Card Runner]] |
| Local byte custody | [[LLM/Study/Local LLM Artifact Custody Audit Runner]] |
| Runtime compatibility | [[LLM/Study/Local LLM Runtime Compatibility Runner]] |
| Serving path | [[LLM/Study/Local LLM Serving Runbook]] |
| Security/privacy route | [[LLM/Study/Local LLM Security and Privacy Runner]] |

## References

- [Hugging Face model cards](https://huggingface.co/docs/hub/en/model-cards)
- [Hugging Face gated models](https://huggingface.co/docs/hub/en/models-gated)
- [Hugging Face malware scanning](https://huggingface.co/docs/hub/en/security-malware)
- [Hugging Face pickle scanning](https://huggingface.co/docs/hub/en/security-pickle)
- [Hugging Face Safetensors](https://huggingface.co/docs/safetensors/index)
- [SPDX license list](https://spdx.github.io/spdx-spec/v2.3/SPDX-license-list/)
- [Open Source AI Definition 1.0](https://opensource.org/ai/open-source-ai-definition)
