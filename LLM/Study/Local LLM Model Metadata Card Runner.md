---
tags: [study, llm, inference, local-llm, metadata, tokenizer, architecture, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [core, practice]
last-verified: 2026-06-16
---

# Local LLM Model Metadata Card Runner

> **One-line summary** Turn saved model metadata into a checked model card before architecture, tokenizer, context, custody, runtime-compatibility, or KV-cache-sizing claims depend on it.

Use this after [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]] and [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Local LLM Artifact Download Cache and Conversion Lab]] have identified the artifact, local path, file list, or runtime package. Use it before [[LLM/Study/Local LLM Artifact Custody Audit Runner|Local LLM Artifact Custody Audit Runner]], [[LLM/Study/Local LLM Runtime Compatibility Runner|Local LLM Runtime Compatibility Runner]], [[LLM/Study/Chat Template and Tokenizer Compatibility Runner|Chat Template and Tokenizer Compatibility Runner]], [[LLM/Study/Local LLM Context Window and Token Budgeting Runner|Local LLM Context Window and Token Budgeting Runner]], and [[LLM/Study/Local LLM KV Cache Sizing Runner|Local LLM KV Cache Sizing Runner]] whenever a downstream proof needs architecture, tokenizer, template, context, quantization, license, or file-inventory facts.

This runner does not download a model, call a model, or query a live endpoint. It audits metadata already saved from `config.json`, tokenizer files, a file inventory, or Ollama `POST /api/show` output, then writes a normalized model metadata card.

## What This Proves

| Gate | Evidence checked | Why it matters |
|---|---|---|
| Source identity | model id, source ref, revision, and source proof | prevents floating tags and family guesses from becoming local proof |
| Architecture | model type, layers, hidden size, attention heads, key/value heads, head dimension, context length | feeds KV-cache sizing, hardware sizing, runtime compatibility, and academic tensor-shape explanations |
| Tokenizer and template | tokenizer source, tokenizer class, chat template, special tokens, model max length | prevents role-boundary and stop-token failures from being blamed on model quality |
| Runtime package metadata | Ollama details, quantization level, capabilities, template, parameters, license, and model info | exposes hidden runtime-package facts behind a convenient model tag |
| Artifact inventory | config, tokenizer, weights, license, README, unsafe file hints | catches incomplete downloads, wrong mirrors, and unsafe loading boundaries |
| Downstream handoffs | KV-cache, context-budget, template-tokenizer, custody, and runtime-compatibility candidate fields | keeps later runners from retyping or guessing metadata |

Academic bridge: the local hosting question "will it run?" depends on the same variables used in the architecture notes: layers, width, attention heads, key/value heads, context length, tokenizer, and generation boundary. A metadata card is the checkpoint where those paper-level concepts become local evidence.

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "model-metadata-qwen-baseline",
  "run_root": "D:/llm-runs/model-metadata",
  "vault_root": "D:/Vaults/PersonalKB",
  "model_id": "example-local-model",
  "expected_model_id": "example-local-model",
  "source_ref": "hf.co/org/repo@commit-or-ollama-tag",
  "source_proof": "LLM/Study/Local LLM Model Acquisition and Provenance Checklist",
  "revision_or_file": "commit, tag, digest, or file name",
  "required_downstreams": [
    "kv_cache_sizing",
    "runtime_compatibility",
    "template_tokenizer",
    "context_budget",
    "artifact_custody"
  ],
  "decisions": {
    "unsafe_file_decision": "none",
    "trust_remote_code": "no"
  },
  "metadata": {
    "config_json": "model/config.json",
    "tokenizer_config_json": "model/tokenizer_config.json",
    "special_tokens_map_json": "model/special_tokens_map.json",
    "generation_config_json": "model/generation_config.json",
    "ollama_show_json": "ollama-show.json",
    "file_inventory": "file-list.txt"
  }
}
```

Use only the files you have. Hugging Face-style snapshots usually provide `config.json` and tokenizer files. Ollama packages usually provide `ollama show` or `/api/show` output with `details`, `template`, `parameters`, `license`, `capabilities`, and `model_info`.

## Evidence Sources

| Source | Useful fields | Notes |
|---|---|---|
| `config.json` | `model_type`, `architectures`, `hidden_size`, `num_attention_heads`, `num_hidden_layers`, `vocab_size`, `max_position_embeddings`, `num_key_value_heads`, `rope_scaling`, `torch_dtype`, `quantization_config` | Hugging Face Transformers documents common config fields such as `hidden_size`, `num_attention_heads`, `num_hidden_layers`, and `vocab_size`. |
| `tokenizer_config.json` | tokenizer class, chat template, model max length, BOS/EOS/PAD tokens | Chat-template presence is a compatibility fact, not a quality score. |
| `special_tokens_map.json` | special-token names and strings | Use this to catch stop/EOS/PAD ambiguity before prompt testing. |
| `generation_config.json` | EOS/PAD ids, max tokens, sampling defaults | Treat generation defaults as a baseline, not as workload policy. |
| Ollama `/api/show` | `details`, `model_info`, `template`, `parameters`, `license`, `capabilities` | The show endpoint exposes model metadata behind a local tag. |
| File inventory | config/tokenizer/weights/license/README presence and unsafe extensions | Required when custody or cache evidence depends on local bytes. |

## Output Contract

The runner writes:

| File | Purpose |
|---|---|
| `<run_id>-metadata-card.json` | full normalized record for downstream runners |
| `<run_id>-metadata-card.md` | human-readable Obsidian evidence card |
| `<run_id>-metadata-findings.csv` | one row per pass/hold/fail finding |
| `<run_id>-metadata-findings.jsonl` | machine-readable findings plus summary row |

Status meanings:

| Status | Meaning |
|---|---|
| `pass` | required source, architecture, tokenizer/template, inventory, and downstream handoff fields are complete enough for the requested routes |
| `hold` | evidence is incomplete but not contradictory; gather the missing metadata before serving, benchmarking, or sizing |
| `fail` | metadata contradicts itself or the artifact is blocked by a stated unsafe-file decision |

Hard failures include `num_key_value_heads > num_attention_heads`, `hidden_size` not divisible by `num_attention_heads`, expected model id mismatch, or an unsafe-file decision marked blocked.

## Standard-Library Runner

Save this as `local_llm_model_metadata_card_runner.py` inside the run folder, or extract it from this note. It uses only Python's standard library.

```python
from __future__ import annotations

import csv
import datetime as dt
import json
import os
import sys
from pathlib import Path
from typing import Any


ARCHITECTURE_ALIASES = {
    "model_type": ["model_type", "general.architecture", "architecture"],
    "layers": ["num_hidden_layers", "n_layer", "n_layers", "num_layers", "block_count"],
    "hidden_size": ["hidden_size", "n_embd", "d_model", "embedding_length"],
    "num_attention_heads": ["num_attention_heads", "n_head", "num_heads", "attention.head_count", "head_count"],
    "num_key_value_heads": [
        "num_key_value_heads",
        "num_kv_heads",
        "n_head_kv",
        "attention.head_count_kv",
        "head_count_kv",
    ],
    "vocab_size": ["vocab_size", "vocabulary_size", "tokenizer.ggml.tokens"],
    "context_window": ["max_position_embeddings", "n_positions", "seq_length", "model_max_length", "context_length"],
}

TEXT_WEIGHT_EXTENSIONS = {".safetensors", ".gguf", ".bin", ".pt", ".pth", ".onnx", ".ckpt"}
UNSAFE_EXTENSIONS = {".bin", ".pt", ".pth", ".pkl", ".pickle"}
CUSTOM_CODE_EXTENSIONS = {".py"}
DEFAULT_REQUIRED_DOWNSTREAMS = [
    "artifact_custody",
    "runtime_compatibility",
    "template_tokenizer",
    "context_budget",
    "kv_cache_sizing",
]


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def clean_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def to_int(value: Any) -> int | None:
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    if isinstance(value, str):
        stripped = value.strip().replace(",", "")
        if stripped.isdigit():
            return int(stripped)
    return None


def nonempty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, set, dict)):
        return bool(value)
    return True


def load_json_file(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def path_candidates(ref: str, manifest_path: Path, manifest: dict[str, Any]) -> list[Path]:
    raw = Path(os.path.expandvars(ref))
    if raw.is_absolute():
        return [raw]
    roots = [manifest_path.parent]
    for key in ("run_root", "vault_root"):
        value = clean_text(manifest.get(key))
        if value:
            roots.append(Path(os.path.expandvars(value)))
    return [root / raw for root in roots]


def resolve_existing_path(ref: Any, manifest_path: Path, manifest: dict[str, Any]) -> Path | None:
    value = clean_text(ref)
    if not value:
        return None
    for candidate in path_candidates(value, manifest_path, manifest):
        if candidate.exists():
            return candidate
    return None


def load_optional_json(ref: Any, manifest_path: Path, manifest: dict[str, Any], label: str, findings: list[dict[str, Any]]) -> Any:
    value = clean_text(ref)
    if not value:
        return None
    path = resolve_existing_path(value, manifest_path, manifest)
    if path is None:
        findings.append(finding("hold", label, f"Metadata file is missing: {value}", "metadata", "Save the file or remove it from the manifest."))
        return None
    try:
        return load_json_file(path)
    except json.JSONDecodeError as exc:
        findings.append(finding("fail", label, f"Metadata file is not valid JSON: {path} ({exc})", "metadata", "Regenerate or repair the artifact."))
        return None


def load_inventory(ref: Any, manifest_path: Path, manifest: dict[str, Any], findings: list[dict[str, Any]]) -> list[str]:
    value = clean_text(ref)
    if not value:
        return []
    path = resolve_existing_path(value, manifest_path, manifest)
    if path is None:
        findings.append(finding("hold", "file_inventory", f"File inventory is missing: {value}", "inventory", "Save a file list from the artifact directory or runtime package."))
        return []
    try:
        if path.suffix.lower() == ".json":
            data = load_json_file(path)
            if isinstance(data, dict):
                items = data.get("files") or data.get("items") or data.get("paths") or []
            else:
                items = data
            results = []
            for item in as_list(items):
                if isinstance(item, dict):
                    results.append(clean_text(item.get("path") or item.get("name") or item.get("file")))
                else:
                    results.append(clean_text(item))
            return [item for item in results if item]
        return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    except Exception as exc:
        findings.append(finding("fail", "file_inventory", f"Could not read file inventory: {path} ({exc})", "inventory", "Regenerate the file inventory."))
        return []


def flatten(value: Any, prefix: str = "") -> dict[str, Any]:
    out: dict[str, Any] = {}
    if isinstance(value, dict):
        for key, nested in value.items():
            text_key = str(key)
            path = f"{prefix}.{text_key}" if prefix else text_key
            out[path] = nested
            out.update(flatten(nested, path))
    return out


def key_score(key: str) -> tuple[int, int, str]:
    lowered = key.lower()
    penalty = 0
    for avoid in (".audio.", ".vision.", ".projector.", ".text_config.", ".encoder."):
        if avoid in f".{lowered}.":
            penalty += 10
    return (penalty, len(key), key)


def find_value(sources: list[dict[str, Any]], aliases: list[str]) -> tuple[Any, str]:
    lowered_aliases = [alias.lower() for alias in aliases]
    for source in sources:
        lowered_keys = {key.lower(): key for key in source.keys()}
        for alias in lowered_aliases:
            if alias in lowered_keys:
                actual = lowered_keys[alias]
                return source[actual], actual
    suffix_matches: list[tuple[tuple[int, int, str], Any, str]] = []
    for source in sources:
        for key, value in source.items():
            lowered = key.lower()
            for alias in lowered_aliases:
                if lowered.endswith("." + alias) or lowered.endswith("_" + alias):
                    suffix_matches.append((key_score(key), value, key))
    if suffix_matches:
        _, value, key = sorted(suffix_matches, key=lambda item: item[0])[0]
        return value, key
    return None, ""


def summarize_inventory(files: list[str]) -> dict[str, Any]:
    basenames = [Path(item.replace("\\", "/")).name.lower() for item in files]
    suffixes = [Path(name).suffix.lower() for name in basenames]
    unsafe = sorted({name for name in basenames if Path(name).suffix.lower() in UNSAFE_EXTENSIONS})
    custom_code = sorted({name for name in basenames if Path(name).suffix.lower() in CUSTOM_CODE_EXTENSIONS})
    weights = sorted({name for name in basenames if Path(name).suffix.lower() in TEXT_WEIGHT_EXTENSIONS})
    return {
        "file_count": len(files),
        "config_present": "config.json" in basenames,
        "tokenizer_present": any(name in basenames for name in ("tokenizer.json", "tokenizer.model", "tokenizer_config.json")),
        "special_tokens_present": "special_tokens_map.json" in basenames,
        "generation_config_present": "generation_config.json" in basenames,
        "weights_present": bool(weights),
        "weight_files": weights[:25],
        "license_present": any(name.startswith("license") or name == "license" for name in basenames),
        "readme_present": any(name.startswith("readme") for name in basenames),
        "unsafe_file_hints": unsafe,
        "custom_code_hints": custom_code,
        "extensions": sorted(set(suffix for suffix in suffixes if suffix)),
    }


def normalize_architecture(config: dict[str, Any], ollama_show: dict[str, Any]) -> dict[str, Any]:
    details = ollama_show.get("details") if isinstance(ollama_show.get("details"), dict) else {}
    model_info = ollama_show.get("model_info") if isinstance(ollama_show.get("model_info"), dict) else {}
    sources = [flatten(config), flatten(model_info), flatten(details)]
    output: dict[str, Any] = {}
    source_keys: dict[str, str] = {}
    for field, aliases in ARCHITECTURE_ALIASES.items():
        value, source_key = find_value(sources, aliases)
        if field in {"layers", "hidden_size", "num_attention_heads", "num_key_value_heads", "vocab_size", "context_window"}:
            value = to_int(value)
        if nonempty(value):
            output[field] = value
            source_keys[field] = source_key
    if "architectures" in config:
        output["architectures"] = as_list(config.get("architectures"))
        source_keys["architectures"] = "config.architectures"
    if "torch_dtype" in config:
        output["torch_dtype"] = config.get("torch_dtype")
        source_keys["torch_dtype"] = "config.torch_dtype"
    if "quantization_config" in config:
        output["quantization_config"] = config.get("quantization_config")
        source_keys["quantization_config"] = "config.quantization_config"
    if "rope_scaling" in config:
        output["rope_scaling"] = config.get("rope_scaling")
        source_keys["rope_scaling"] = "config.rope_scaling"
    if details:
        output["ollama_family"] = details.get("family")
        output["ollama_format"] = details.get("format")
        output["ollama_parameter_size"] = details.get("parameter_size")
        output["ollama_quantization_level"] = details.get("quantization_level")
    hidden_size = to_int(output.get("hidden_size"))
    heads = to_int(output.get("num_attention_heads"))
    if hidden_size and heads and hidden_size % heads == 0:
        output["head_dim"] = hidden_size // heads
    output["source_keys"] = source_keys
    return output


def normalize_tokenizer(tokenizer_config: dict[str, Any], special_tokens: dict[str, Any], ollama_show: dict[str, Any], inventory: dict[str, Any]) -> dict[str, Any]:
    has_chat_template = bool(clean_text(tokenizer_config.get("chat_template")) or clean_text(ollama_show.get("template")))
    token_fields = {}
    for name in ("bos_token", "eos_token", "pad_token", "unk_token", "sep_token", "cls_token"):
        token_fields[name] = tokenizer_config.get(name) or special_tokens.get(name)
    return {
        "tokenizer_class": tokenizer_config.get("tokenizer_class"),
        "tokenizer_source": "tokenizer_config.json" if tokenizer_config else ("file_inventory" if inventory.get("tokenizer_present") else ""),
        "tokenizer_present": bool(tokenizer_config or inventory.get("tokenizer_present")),
        "chat_template_present": has_chat_template,
        "chat_template_source": "tokenizer_config.json" if clean_text(tokenizer_config.get("chat_template")) else ("ollama_show" if clean_text(ollama_show.get("template")) else ""),
        "model_max_length": to_int(tokenizer_config.get("model_max_length")),
        "special_tokens": {key: value for key, value in token_fields.items() if nonempty(value)},
    }


def normalize_ollama_show(ollama_show: dict[str, Any]) -> dict[str, Any]:
    details = ollama_show.get("details") if isinstance(ollama_show.get("details"), dict) else {}
    model_info = ollama_show.get("model_info") if isinstance(ollama_show.get("model_info"), dict) else {}
    return {
        "details": details,
        "capabilities": as_list(ollama_show.get("capabilities")),
        "template_present": bool(clean_text(ollama_show.get("template"))),
        "parameters_present": bool(clean_text(ollama_show.get("parameters"))),
        "license_present": bool(clean_text(ollama_show.get("license"))),
        "model_info_key_count": len(model_info),
    }


def finding(status: str, field: str, message: str, owner: str, next_action: str) -> dict[str, Any]:
    return {
        "status": status,
        "field": field,
        "message": message,
        "owner": owner,
        "next_action": next_action,
    }


def add_required(findings: list[dict[str, Any]], field: str, value: Any, owner: str, next_action: str) -> None:
    if not nonempty(value):
        findings.append(finding("hold", field, f"Missing required evidence: {field}.", owner, next_action))


def first_missing_for_route(route: str, architecture: dict[str, Any], tokenizer: dict[str, Any], inventory: dict[str, Any], manifest: dict[str, Any]) -> str:
    if route == "kv_cache_sizing":
        for field in ("layers", "hidden_size", "num_attention_heads", "num_key_value_heads"):
            if not nonempty(architecture.get(field)):
                return field
    if route == "template_tokenizer":
        if not tokenizer.get("tokenizer_present"):
            return "tokenizer_source"
        if not tokenizer.get("chat_template_present"):
            return "chat_template"
    if route == "context_budget":
        if not nonempty(architecture.get("context_window")) and not nonempty(tokenizer.get("model_max_length")):
            return "context_window"
    if route == "artifact_custody":
        if not inventory.get("file_count") and not nonempty(manifest.get("runtime_model_id")):
            return "file_inventory"
    if route == "runtime_compatibility":
        if not nonempty(architecture.get("model_type")) and not nonempty(architecture.get("architectures")):
            return "architecture"
        if not tokenizer.get("tokenizer_present") and not tokenizer.get("chat_template_present"):
            return "tokenizer_or_template"
    return ""


def validate_record(record: dict[str, Any]) -> None:
    manifest = record["manifest"]
    architecture = record["architecture"]
    tokenizer = record["tokenizer"]
    inventory = record["inventory"]
    findings = record["findings"]
    decisions = manifest.get("decisions") if isinstance(manifest.get("decisions"), dict) else {}

    add_required(findings, "model_id", manifest.get("model_id"), "source", "Name the exact local/runtime model id being audited.")
    add_required(findings, "source_ref", manifest.get("source_ref"), "source", "Record the Hub repo/revision, Ollama tag, GGUF URL, or internal source.")
    add_required(findings, "source_proof", manifest.get("source_proof"), "source", "Link the acquisition card or source proof.")

    expected = clean_text(manifest.get("expected_model_id"))
    actual = clean_text(manifest.get("model_id") or manifest.get("runtime_model_id"))
    if expected and actual and expected != actual:
        findings.append(finding("fail", "expected_model_id", f"Expected model id {expected!r} does not match manifest model id {actual!r}.", "source", "Fix the manifest or audit the correct model."))

    heads = to_int(architecture.get("num_attention_heads"))
    kv_heads = to_int(architecture.get("num_key_value_heads"))
    hidden_size = to_int(architecture.get("hidden_size"))
    if heads and kv_heads and kv_heads > heads:
        findings.append(finding("fail", "num_key_value_heads", "Key/value heads exceed attention heads.", "architecture", "Recheck config.json or runtime model_info."))
    if hidden_size and heads and hidden_size % heads != 0:
        findings.append(finding("fail", "hidden_size", "Hidden size is not divisible by attention heads.", "architecture", "Recheck hidden size and attention-head fields."))

    required_downstreams = [clean_text(item) for item in as_list(manifest.get("required_downstreams") or DEFAULT_REQUIRED_DOWNSTREAMS) if clean_text(item)]
    for route in required_downstreams:
        missing = first_missing_for_route(route, architecture, tokenizer, inventory, manifest)
        if missing:
            findings.append(finding("hold", route, f"Downstream route {route} is missing {missing}.", route, "Capture the missing metadata before running this downstream proof."))

    unsafe_decision = clean_text(decisions.get("unsafe_file_decision") or manifest.get("unsafe_file_decision")).lower()
    trust_remote_code = clean_text(decisions.get("trust_remote_code") or manifest.get("trust_remote_code")).lower()
    if inventory.get("unsafe_file_hints") and not unsafe_decision:
        findings.append(finding("hold", "unsafe_file_decision", "Unsafe or pickle-style file hints are present but no decision is recorded.", "artifact", "Record reviewed, sandboxed, learning-only, blocked, or none."))
    if inventory.get("custom_code_hints") and trust_remote_code not in {"no", "false", "not needed", "reviewed", "sandboxed"}:
        findings.append(finding("hold", "trust_remote_code", "Python/custom-code hints are present and trust_remote_code policy is unclear.", "artifact", "Record no/reviewed/sandboxed/blocked before loading."))
    if unsafe_decision == "blocked" or trust_remote_code == "blocked":
        findings.append(finding("fail", "unsafe_file_decision", "Manifest marks the artifact as blocked by unsafe-file or custom-code policy.", "artifact", "Reject or replace the artifact."))

    if not findings:
        findings.append(finding("pass", "metadata_card", "Metadata card is ready for requested downstream routes.", "metadata", "Use the generated handoff fields in the next runner."))


def build_handoffs(record: dict[str, Any]) -> dict[str, Any]:
    manifest = record["manifest"]
    architecture = record["architecture"]
    tokenizer = record["tokenizer"]
    inventory = record["inventory"]
    ollama = record["ollama"]
    model_id = manifest.get("model_id") or manifest.get("runtime_model_id")
    source = manifest.get("source_ref")
    handoffs: dict[str, Any] = {
        "artifact_custody_fields": {
            "artifact_id": model_id,
            "source_ref": source,
            "revision_or_file": manifest.get("revision_or_file"),
            "file_inventory_artifact": manifest.get("metadata", {}).get("file_inventory") if isinstance(manifest.get("metadata"), dict) else "",
            "unsafe_file_decision": (manifest.get("decisions") or {}).get("unsafe_file_decision") if isinstance(manifest.get("decisions"), dict) else manifest.get("unsafe_file_decision"),
            "inventory_summary": inventory,
        },
        "runtime_compatibility_candidate": {
            "candidate_id": model_id,
            "model_id": model_id,
            "source": source,
            "architecture": architecture.get("model_type") or ", ".join(str(item) for item in as_list(architecture.get("architectures"))),
            "artifact_container": architecture.get("ollama_format") or manifest.get("artifact_container"),
            "quantization": architecture.get("ollama_quantization_level") or manifest.get("quantization"),
            "tokenizer_source": tokenizer.get("tokenizer_source"),
            "chat_template_source": tokenizer.get("chat_template_source"),
        },
        "template_tokenizer_candidate": {
            "model_id": model_id,
            "tokenizer_source": tokenizer.get("tokenizer_source"),
            "chat_template_source": tokenizer.get("chat_template_source"),
            "special_tokens": tokenizer.get("special_tokens"),
        },
        "context_budget_candidate": {
            "model_id": model_id,
            "context_window": architecture.get("context_window") or tokenizer.get("model_max_length"),
            "context_source": architecture.get("source_keys", {}).get("context_window") or ("tokenizer_config.model_max_length" if tokenizer.get("model_max_length") else ""),
        },
        "ollama_runtime_metadata": ollama,
    }
    kv_fields = ("layers", "hidden_size", "num_attention_heads", "num_key_value_heads", "head_dim")
    if any(nonempty(architecture.get(field)) for field in kv_fields):
        handoffs["kv_cache_sizing_candidate"] = {
            "candidate_id": model_id,
            "layers": architecture.get("layers"),
            "hidden_size": architecture.get("hidden_size"),
            "num_attention_heads": architecture.get("num_attention_heads"),
            "num_key_value_heads": architecture.get("num_key_value_heads"),
            "head_dim": architecture.get("head_dim"),
            "source": "Local LLM Model Metadata Card Runner",
            "next_route": "LLM/Study/Local LLM KV Cache Sizing Runner",
        }
    return handoffs


def status_from_findings(findings: list[dict[str, Any]]) -> tuple[str, str]:
    statuses = {item["status"] for item in findings}
    if "fail" in statuses:
        return "fail", "metadata_conflict"
    if "hold" in statuses:
        return "hold", "metadata_incomplete"
    return "pass", "model_metadata_ready"


def build_record(manifest_path: Path) -> dict[str, Any]:
    manifest = load_json_file(manifest_path)
    findings: list[dict[str, Any]] = []
    metadata = manifest.get("metadata") if isinstance(manifest.get("metadata"), dict) else {}

    config = load_optional_json(metadata.get("config_json"), manifest_path, manifest, "config_json", findings) or {}
    tokenizer_config = load_optional_json(metadata.get("tokenizer_config_json"), manifest_path, manifest, "tokenizer_config_json", findings) or {}
    special_tokens = load_optional_json(metadata.get("special_tokens_map_json"), manifest_path, manifest, "special_tokens_map_json", findings) or {}
    generation_config = load_optional_json(metadata.get("generation_config_json"), manifest_path, manifest, "generation_config_json", findings) or {}
    ollama_show = load_optional_json(metadata.get("ollama_show_json"), manifest_path, manifest, "ollama_show_json", findings) or {}
    inventory_files = load_inventory(metadata.get("file_inventory"), manifest_path, manifest, findings)

    inventory = summarize_inventory(inventory_files)
    architecture = normalize_architecture(config, ollama_show)
    tokenizer = normalize_tokenizer(tokenizer_config, special_tokens, ollama_show, inventory)
    ollama = normalize_ollama_show(ollama_show)

    record: dict[str, Any] = {
        "run_id": manifest.get("run_id") or manifest_path.stem,
        "generated_at": now_iso(),
        "manifest_path": str(manifest_path),
        "manifest": manifest,
        "metadata_inputs": {
            "config_json": bool(config),
            "tokenizer_config_json": bool(tokenizer_config),
            "special_tokens_map_json": bool(special_tokens),
            "generation_config_json": bool(generation_config),
            "ollama_show_json": bool(ollama_show),
            "file_inventory": bool(inventory_files),
        },
        "architecture": architecture,
        "tokenizer": tokenizer,
        "generation_config": generation_config,
        "ollama": ollama,
        "inventory": inventory,
        "findings": findings,
    }
    validate_record(record)
    record["handoffs"] = build_handoffs(record)
    record["status"], record["decision"] = status_from_findings(record["findings"])
    record["next_route"] = choose_next_route(record)
    return record


def choose_next_route(record: dict[str, Any]) -> str:
    if record["status"] == "fail":
        return "LLM/Study/Local LLM Artifact Download Cache and Conversion Lab"
    if record["status"] == "hold":
        first_hold = next((item for item in record["findings"] if item["status"] == "hold"), None)
        if first_hold and first_hold["owner"] == "source":
            return "LLM/Study/Local LLM Model Acquisition and Provenance Checklist"
        if first_hold and first_hold["owner"] in {"metadata", "inventory", "artifact"}:
            return "LLM/Study/Local LLM Artifact Download Cache and Conversion Lab"
        if first_hold and first_hold["owner"] == "kv_cache_sizing":
            return "LLM/Study/Local LLM KV Cache Sizing Runner"
        if first_hold and first_hold["owner"] == "template_tokenizer":
            return "LLM/Study/Chat Template and Tokenizer Compatibility Runner"
        if first_hold and first_hold["owner"] == "context_budget":
            return "LLM/Study/Local LLM Context Window and Token Budgeting Runner"
        return "LLM/Study/Local LLM Runtime Compatibility Runner"
    return "LLM/Study/Local LLM Runtime Compatibility Runner"


def obsidian_link(target: str) -> str:
    return ("[" * 2) + target + ("]" * 2)


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_markdown(path: Path, record: dict[str, Any]) -> None:
    architecture = record["architecture"]
    tokenizer = record["tokenizer"]
    inventory = record["inventory"]
    lines = [
        f"# Local LLM Model Metadata Card - {record['run_id']}",
        "",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Model: `{record['manifest'].get('model_id', '')}`",
        f"- Source: `{record['manifest'].get('source_ref', '')}`",
        f"- Next route: {obsidian_link(record['next_route'])}",
        "",
        "## Architecture",
        "",
        "| Field | Value |",
        "|---|---|",
    ]
    for key in ("model_type", "architectures", "layers", "hidden_size", "num_attention_heads", "num_key_value_heads", "head_dim", "vocab_size", "context_window", "torch_dtype", "ollama_quantization_level"):
        value = architecture.get(key)
        lines.append(f"| {key} | `{json.dumps(value, ensure_ascii=False)}` |" if nonempty(value) else f"| {key} |  |")
    lines.extend([
        "",
        "## Tokenizer And Template",
        "",
        "| Field | Value |",
        "|---|---|",
    ])
    for key in ("tokenizer_source", "tokenizer_class", "tokenizer_present", "chat_template_present", "chat_template_source", "model_max_length", "special_tokens"):
        value = tokenizer.get(key)
        lines.append(f"| {key} | `{json.dumps(value, ensure_ascii=False)}` |" if nonempty(value) else f"| {key} |  |")
    lines.extend([
        "",
        "## Inventory",
        "",
        "| Field | Value |",
        "|---|---|",
    ])
    for key in ("file_count", "config_present", "tokenizer_present", "weights_present", "license_present", "readme_present", "unsafe_file_hints", "custom_code_hints"):
        lines.append(f"| {key} | `{json.dumps(inventory.get(key), ensure_ascii=False)}` |")
    lines.extend([
        "",
        "## Findings",
        "",
        "| Status | Field | Message | Owner | Next action |",
        "|---|---|---|---|---|",
    ])
    for item in record["findings"]:
        lines.append(f"| `{item['status']}` | `{item['field']}` | {item['message']} | `{item['owner']}` | {item['next_action']} |")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_csv(path: Path, findings: list[dict[str, Any]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["status", "field", "message", "owner", "next_action"])
        writer.writeheader()
        for item in findings:
            writer.writerow(item)


def write_jsonl(path: Path, record: dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        handle.write(json.dumps({"type": "summary", "run_id": record["run_id"], "status": record["status"], "decision": record["decision"], "next_route": record["next_route"]}, sort_keys=True) + "\n")
        for item in record["findings"]:
            handle.write(json.dumps({"type": "finding", "run_id": record["run_id"], **item}, sort_keys=True) + "\n")


def write_outputs(record: dict[str, Any], out_dir: Path) -> dict[str, str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = record["run_id"]
    paths = {
        "json": out_dir / f"{stem}-metadata-card.json",
        "markdown": out_dir / f"{stem}-metadata-card.md",
        "csv": out_dir / f"{stem}-metadata-findings.csv",
        "jsonl": out_dir / f"{stem}-metadata-findings.jsonl",
    }
    write_json(paths["json"], record)
    write_markdown(paths["markdown"], record)
    write_csv(paths["csv"], record["findings"])
    write_jsonl(paths["jsonl"], record)
    return {key: str(path) for key, path in paths.items()}


def main(argv: list[str]) -> int:
    if len(argv) not in {2, 3}:
        print("Usage: python local_llm_model_metadata_card_runner.py <manifest.json> [output_dir]", file=sys.stderr)
        return 2
    manifest_path = Path(argv[1]).resolve()
    if not manifest_path.exists():
        print(f"Manifest not found: {manifest_path}", file=sys.stderr)
        return 2
    record = build_record(manifest_path)
    out_dir = Path(argv[2]).resolve() if len(argv) == 3 else manifest_path.parent / "metadata-card-results"
    outputs = write_outputs(record, out_dir)
    print(json.dumps({"status": record["status"], "decision": record["decision"], "next_route": record["next_route"], "outputs": outputs}, indent=2, sort_keys=True))
    return 1 if record["status"] == "fail" else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
```

## Fixture Checks

Use these before trusting an edited copy:

| Fixture | Expected status | Why |
|---|---|---|
| Hugging Face-style config, tokenizer config, special tokens, and inventory | `pass` | Architecture, tokenizer, context, file inventory, and source proof are complete. |
| Config lacks `num_key_value_heads` while `kv_cache_sizing` is required | `hold` | The KV-cache runner should not guess GQA/MQA/MHA geometry. |
| `num_key_value_heads` exceeds `num_attention_heads` | `fail` | The metadata contradicts attention geometry. |
| Ollama show output has quantization/template/license but no attention geometry | `hold` | Good runtime package facts are not enough for head-aware cache sizing. |

## Completion Gate

This runner is complete when you have:

- [ ] source ref, source proof, model id, and revision/tag/file recorded
- [ ] at least one metadata source saved: `config.json`, tokenizer files, Ollama `/api/show`, or inventory
- [ ] architecture fields captured or explicit hold reason recorded
- [ ] tokenizer/template fields captured or explicit hold reason recorded
- [ ] context-window source captured or explicit hold reason recorded
- [ ] unsafe-file and custom-code decisions recorded when inventory shows risky files
- [ ] JSON, Markdown, CSV, and JSONL outputs saved
- [ ] handoff fields copied into the next custody, compatibility, tokenizer, context, or KV-cache runner

## References

Internal:

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab]]
- [[LLM/Study/Local LLM Artifact Custody Audit Runner]]
- [[LLM/Study/Local LLM Runtime Compatibility Runner]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Runner]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]]
- [[LLM/Study/Local LLM KV Cache Sizing Runner]]
- [[LLM/Study/LLM Math and Tensor Shape Primer]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]

Current external docs checked 2026-06-16:

- [Hugging Face Hub download guide](https://huggingface.co/docs/huggingface_hub/guides/download)
- [Hugging Face Transformers configuration](https://huggingface.co/docs/transformers/main_classes/configuration)
- [Ollama show model details API](https://docs.ollama.com/api-reference/show-model-details)
- [Ollama Modelfile reference](https://docs.ollama.com/modelfile)
- [Ollama context length](https://docs.ollama.com/context-length)
