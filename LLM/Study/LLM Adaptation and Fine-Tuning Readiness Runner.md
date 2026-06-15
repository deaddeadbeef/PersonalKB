---
tags: [study, llm, adaptation, fine-tuning, sft, peft, lora, qlora, dpo, dataset, evaluation, evidence, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [deep-dive, practice]
last-verified: 2026-06-16
---

# LLM Adaptation and Fine-Tuning Readiness Runner

> **One-line summary** Audit whether a measured quality gap is ready for prompting, RAG, model swap, SFT, LoRA, QLoRA, DPO, distillation, continued pretraining, or a no-train decision before changing weights or shipping an adapter.

Use this after [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide|LLM Adaptation and Fine-Tuning Decision Guide]] and after [[LLM/Study/Local LLM Quality Evaluation Runner|Local LLM Quality Evaluation Runner]] or another quality gate has produced a reproducible baseline failure. Use it before training an adapter, merging a model, writing the adaptation memo in [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]], feeding evidence into [[LLM/Study/Local LLM Result Synthesis Runner|Local LLM Result Synthesis Runner]], or accepting a deployment path in [[LLM/Study/LLM Deployment Readiness Audit Runner|LLM Deployment Readiness Audit Runner]].

This runner does not train a model, inspect private data, call a hosted provider, or decide that fine-tuning is always desirable. It audits the evidence you saved: baseline failure, chosen adaptation method, rejected alternatives, dataset shape, held-out split, contamination and privacy checks, tokenizer/chat-template proof, method-specific config, compute boundary, deployment plan, rollback plan, and post-adaptation evaluation route.

## Official Anchors

- TRL `SFTTrainer` supports language-modeling and prompt-completion datasets in standard or conversational formats, and conversational datasets can have chat templates applied automatically: [Hugging Face TRL SFTTrainer](https://huggingface.co/docs/trl/en/sft_trainer).
- TRL `DPOTrainer` requires preference data and supports standard or conversational prompt/chosen/rejected formats: [Hugging Face TRL DPOTrainer](https://huggingface.co/docs/trl/en/dpo_trainer).
- TRL dataset-format docs distinguish dataset format from dataset type and list prompt-only, prompt-completion, preference, unpaired-preference, and stepwise-supervision shapes: [Hugging Face TRL dataset formats](https://huggingface.co/docs/trl/en/dataset_formats).
- Hugging Face PEFT documents LoRA as low-rank matrices that reduce the number of parameters that need fine-tuning, with `LoraConfig` fields such as rank, target modules, alpha, dropout, and initialization: [Hugging Face PEFT LoRA](https://huggingface.co/docs/peft/package_reference/lora).
- Transformers chat-template docs emphasize that chat-tuned causal LMs expect model-specific control tokens and that using the wrong format can severely degrade behavior: [Hugging Face Transformers chat templates](https://huggingface.co/docs/transformers/en/chat_templating).
- LoRA freezes pretrained weights and trains low-rank update matrices, reducing trainable parameters and avoiding extra inference latency after merge: [Hu et al. 2021](https://arxiv.org/abs/2106.09685).
- QLoRA backpropagates through a frozen 4-bit quantized base model into LoRA adapters and uses NF4, double quantization, and paged optimizers to reduce memory: [Dettmers et al. 2023](https://arxiv.org/abs/2305.14314).
- DPO trains directly on preference pairs without a separate reward model or PPO loop, but still depends on preference-data support and a reference-policy comparison: [Rafailov et al. 2023](https://arxiv.org/abs/2305.18290).

## What This Proves

| Gate | Evidence checked | Why it matters |
|---|---|---|
| Baseline failure | failing quality row, failure mode, selected workload | prevents training to fix an unmeasured or already-passing behavior |
| Method fit | selected method, rejected alternatives, method-match justification | keeps SFT/LoRA/DPO from becoming the default answer to every bad response |
| Dataset shape | SFT prompt-completion, chat messages, DPO preference pairs, raw domain corpus, teacher outputs | maps the data to the actual training or no-training method |
| Split hygiene | train/validation/held-out counts, overlap, duplicates, contamination check | protects evaluation from leakage and overfitting |
| Privacy and rights | private-data boundary, data egress, source license/consent review, secrets scan | stops accidental provider upload or unsafe retention before adaptation |
| Tokenizer/template | chat-template proof and role/stop-token compatibility | prevents training or evaluation with the wrong conversation format |
| Method config | LoRA rank/modules, QLoRA quantized base plan, DPO reference model, distillation teacher | makes the adaptation plan reproducible enough to audit |
| Deployment and rollback | adapter/merge/index/prompt path, runtime target, rollback plan | ensures the adapted artifact can be served and removed safely |
| Evaluation handoff | held-out eval, regression suite, pass criteria, rerun route | makes the final claim compare against the original failure, not vibes |

Academic bridge: adaptation is an experiment. The independent variable is not only "fine-tune or not"; it is the method, data distribution, tokenizer format, frozen or trainable parameters, preference objective, privacy boundary, and deployment artifact. A correct no-train decision can be stronger evidence than an ungrounded LoRA run.

## Manifest Shape

Save `adaptation-readiness-manifest.json` next to the runner:

```json
{
  "run_id": "adaptation-readiness-001",
  "run_root": "D:/llm-runs/adaptation-readiness",
  "vault_root": "D:/Vaults/PersonalKB",
  "decision": {
    "workload": "private local extraction assistant",
    "baseline_model": "local-model-id",
    "failure_mode": "format",
    "selected_method": "lora",
    "method_matches_failure_mode": true,
    "rejected_methods": ["rag", "dpo"],
    "rejection_reason": "failure is repeated output schema behavior, not missing source facts or subjective preference",
    "final_intent": "train_adapter"
  },
  "dataset": {
    "dataset_format": "conversational_prompt_completion",
    "train_examples": 1200,
    "validation_examples": 120,
    "heldout_examples": 120,
    "preference_pairs": 0,
    "duplicate_check": true,
    "near_duplicate_check": true,
    "train_heldout_overlap_count": 0,
    "benchmark_contamination_check": true,
    "secrets_scan": true,
    "private_data_boundary": "local_only",
    "data_leaves_machine": false,
    "provider_egress_approved": false,
    "source_license_reviewed": true,
    "data_version_or_hash": "dataset-v1-sha256"
  },
  "method": {
    "lora_rank": 16,
    "lora_alpha": 32,
    "target_modules": ["q_proj", "v_proj"],
    "quantized_base_plan": "",
    "reference_model": "",
    "teacher_model": "",
    "adapter_or_merge_plan": "serve base model plus adapter; do not merge until regression passes",
    "no_train_reason": ""
  },
  "evaluation": {
    "baseline_status": "fail",
    "heldout_eval_ready": true,
    "regression_suite_ready": true,
    "safety_regression_ready": true,
    "format_regression_ready": true,
    "pass_criteria": "held-out schema pass rate improves by 20 points with no safety regression",
    "rerun_route": "LLM/Study/Local LLM Quality Evaluation Runner"
  },
  "deployment": {
    "training_location": "local_gpu",
    "gpu_memory_gb": 12,
    "memory_plan": "adapter training only; no full fine-tune",
    "runtime_target": "Ollama adapter import or vLLM LoRA serving",
    "rollback_plan": "remove adapter and restore baseline prompt",
    "retention_policy": "keep dataset manifest and hashed examples; delete temp shards"
  },
  "artifacts": {
    "baseline_failure_artifact": "quality-baseline.md",
    "evaluation_set_artifact": "eval-set-design.json",
    "dataset_manifest": "dataset-manifest.json",
    "heldout_manifest": "heldout-manifest.json",
    "chat_template_proof": "chat-template-proof.md",
    "privacy_review": "privacy-review.md",
    "rollback_plan": "rollback-plan.md"
  }
}
```

Status meanings:

| Status | Meaning |
|---|---|
| `pass/adaptation_ready` | method, data, evaluation, privacy, compute, deployment, and rollback evidence support the selected adaptation or no-train decision |
| `hold/adaptation_incomplete` | evidence is missing or ambiguous; collect proof before training or accepting no-train |
| `fail/adaptation_blocked` | baseline, data, privacy, leakage, method, or deployment evidence contradicts the proposed adaptation |

## Standard-Library Runner

Save this as `llm_adaptation_fine_tuning_readiness_runner.py` inside the run folder, or extract it from this note. It uses only Python's standard library.

```python
from __future__ import annotations

import csv
import datetime as dt
import json
import os
import sys
from pathlib import Path
from typing import Any


TRAINING_METHODS = {"sft", "lora", "qlora", "dpo", "distillation", "continued_pretraining"}
NO_DATA_METHODS = {"prompt", "few_shot", "rag", "model_swap", "no_train", "tool_policy", "quantization"}
METHOD_ALIASES = {
    "fine_tune": "sft",
    "finetune": "sft",
    "fine_tuning": "sft",
    "adapter": "lora",
    "peft": "lora",
    "no_training": "no_train",
    "do_not_train": "no_train",
    "continued_pre_train": "continued_pretraining",
    "continued_pretraining": "continued_pretraining",
}
FORMAT_BY_METHOD = {
    "sft": {"prompt_completion", "conversational_prompt_completion", "messages", "conversational"},
    "lora": {"prompt_completion", "conversational_prompt_completion", "messages", "conversational"},
    "qlora": {"prompt_completion", "conversational_prompt_completion", "messages", "conversational"},
    "dpo": {"preference", "conversational_preference", "chosen_rejected"},
    "distillation": {"teacher_outputs", "prompt_completion", "conversational_prompt_completion", "messages"},
    "continued_pretraining": {"raw_text", "domain_corpus", "language_modeling", "text"},
}
CHAT_TEMPLATE_METHODS = {"sft", "lora", "qlora", "dpo", "distillation"}


def clean(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def norm(value: Any) -> str:
    return clean(value).lower().replace(" ", "_").replace("-", "_")


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def as_bool(value: Any, default: bool | None = False) -> bool | None:
    if value is None or value == "":
        return default
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    text = norm(value)
    if text in {"1", "true", "yes", "y", "pass", "passed", "ok", "ready"}:
        return True
    if text in {"0", "false", "no", "n", "fail", "failed", "blocked"}:
        return False
    return default


def number(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def list_value(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [clean(item) for item in value if clean(item)]
    if isinstance(value, tuple):
        return [clean(item) for item in value if clean(item)]
    text = clean(value)
    if not text:
        return []
    if text.startswith("["):
        try:
            parsed = json.loads(text)
            if isinstance(parsed, list):
                return [clean(item) for item in parsed if clean(item)]
        except json.JSONDecodeError:
            pass
    return [part.strip() for part in text.replace(";", ",").split(",") if part.strip()]


def method_name(value: Any) -> str:
    method = norm(value)
    return METHOD_ALIASES.get(method, method)


def add(checks: list[dict[str, Any]], status: str, gate: str, message: str, evidence: Any = "") -> None:
    checks.append({"status": status, "gate": gate, "message": message, "evidence": clean(evidence)})


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8-sig") as handle:
        return json.load(handle)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def md_cell(value: Any) -> str:
    if isinstance(value, (list, dict)):
        value = json.dumps(value, ensure_ascii=True)
    return clean(value).replace("|", "\\|").replace("\n", " ")


def resolve_artifact(raw: Any, manifest_dir: Path, run_root: Path, vault_root: Path | None) -> Path | None:
    text = clean(raw)
    if not text:
        return None
    text = text.strip("[]")
    if "|" in text and "/" in text:
        text = text.split("|", 1)[0]
    candidate = Path(text.replace("\\", os.sep).replace("/", os.sep)).expanduser()
    candidates = [candidate] if candidate.is_absolute() else [manifest_dir / candidate, run_root / candidate]
    if vault_root and not candidate.is_absolute():
        candidates.append(vault_root / candidate)
    for item in candidates:
        if item.exists():
            return item
    return candidates[0] if candidates else None


def artifact_exists(raw: Any, manifest_dir: Path, run_root: Path, vault_root: Path | None) -> tuple[bool, str]:
    path = resolve_artifact(raw, manifest_dir, run_root, vault_root)
    if not path:
        return False, ""
    return path.exists(), str(path)


def check_required_text(checks: list[dict[str, Any]], group: dict[str, Any], gate: str, fields: list[str]) -> None:
    for field in fields:
        value = clean(group.get(field))
        if value:
            add(checks, "pass", gate, f"{field} is recorded", value)
        else:
            add(checks, "hold", gate, f"{field} is missing")


def check_artifacts(checks: list[dict[str, Any]], artifacts: dict[str, Any], manifest_dir: Path, run_root: Path, vault_root: Path | None, method: str) -> None:
    required = ["baseline_failure_artifact", "evaluation_set_artifact", "rollback_plan"]
    if method in TRAINING_METHODS:
        required.extend(["dataset_manifest", "heldout_manifest"])
    if method in CHAT_TEMPLATE_METHODS:
        required.append("chat_template_proof")
    if norm(artifacts.get("privacy_review")):
        required.append("privacy_review")
    for key in dict.fromkeys(required):
        exists, path = artifact_exists(artifacts.get(key), manifest_dir, run_root, vault_root)
        if exists:
            add(checks, "pass", "artifact_inventory", f"{key} exists", path)
        else:
            add(checks, "hold", "artifact_inventory", f"{key} is missing", artifacts.get(key, ""))


def check_decision(checks: list[dict[str, Any]], decision: dict[str, Any], evaluation: dict[str, Any], method: str) -> None:
    check_required_text(checks, decision, "decision", ["workload", "baseline_model", "failure_mode", "selected_method", "final_intent"])
    baseline_status = norm(evaluation.get("baseline_status"))
    if method in TRAINING_METHODS and baseline_status in {"pass", "passed", "green", "ready"}:
        add(checks, "fail", "baseline_failure", "training method is selected but baseline is recorded as passing", baseline_status)
    elif baseline_status in {"fail", "failed", "hold", "blocked", "incomplete"}:
        add(checks, "pass", "baseline_failure", "baseline gap is reproducible", baseline_status)
    else:
        add(checks, "hold", "baseline_failure", "baseline status is missing or ambiguous", baseline_status)
    match = as_bool(decision.get("method_matches_failure_mode"), None)
    if match is True:
        add(checks, "pass", "method_fit", "selected method is justified for the failure mode")
    elif match is False:
        add(checks, "fail", "method_fit", "selected method is recorded as not matching the failure mode")
    else:
        add(checks, "hold", "method_fit", "method_matches_failure_mode is missing")
    if list_value(decision.get("rejected_methods")) and clean(decision.get("rejection_reason")):
        add(checks, "pass", "method_fit", "rejected alternatives are recorded", ", ".join(list_value(decision.get("rejected_methods"))))
    else:
        add(checks, "hold", "method_fit", "rejected alternatives or rejection reason are missing")


def check_dataset(checks: list[dict[str, Any]], dataset: dict[str, Any], method: str) -> None:
    fmt = method_name(dataset.get("dataset_format"))
    if method in NO_DATA_METHODS:
        add(checks, "pass", "dataset_shape", "selected method does not require training data", method)
        return
    allowed = FORMAT_BY_METHOD.get(method, set())
    if fmt in allowed:
        add(checks, "pass", "dataset_shape", "dataset format matches selected method", fmt)
    else:
        add(checks, "fail", "dataset_shape", "dataset format does not match selected method", f"{fmt} for {method}")
    train = number(dataset.get("train_examples"))
    val = number(dataset.get("validation_examples"))
    heldout = number(dataset.get("heldout_examples"))
    if method == "dpo":
        pairs = number(dataset.get("preference_pairs"))
        if pairs > 0:
            add(checks, "pass", "dataset_shape", "preference pairs are recorded", int(pairs))
        else:
            add(checks, "fail", "dataset_shape", "DPO requires preference pairs")
    else:
        if train > 0:
            add(checks, "pass", "dataset_shape", "training example count is recorded", int(train))
        else:
            add(checks, "hold", "dataset_shape", "training example count is missing")
        if val > 0:
            add(checks, "pass", "dataset_shape", "validation example count is recorded", int(val))
        else:
            add(checks, "hold", "dataset_shape", "validation example count is missing")
    if heldout > 0:
        add(checks, "pass", "dataset_split", "held-out example count is recorded", int(heldout))
    else:
        add(checks, "fail", "dataset_split", "held-out examples are required before adaptation")


def check_hygiene(checks: list[dict[str, Any]], dataset: dict[str, Any], method: str) -> None:
    if method in NO_DATA_METHODS and not clean(dataset.get("dataset_format")):
        add(checks, "pass", "dataset_hygiene", "training-dataset hygiene is not required for this no-training method", method)
        if clean(dataset.get("private_data_boundary")):
            add(checks, "pass", "privacy", "privacy boundary is recorded", dataset.get("private_data_boundary"))
        else:
            add(checks, "hold", "privacy", "private_data_boundary is missing")
        return
    for key in ("duplicate_check", "near_duplicate_check", "benchmark_contamination_check", "secrets_scan", "source_license_reviewed"):
        if as_bool(dataset.get(key), False):
            add(checks, "pass", "dataset_hygiene", f"{key} passed or is recorded")
        else:
            add(checks, "hold", "dataset_hygiene", f"{key} is missing or false")
    overlap = number(dataset.get("train_heldout_overlap_count"))
    if overlap > 0:
        add(checks, "fail", "dataset_hygiene", "train/held-out overlap is nonzero", int(overlap))
    else:
        add(checks, "pass", "dataset_hygiene", "train/held-out overlap is zero")
    boundary = norm(dataset.get("private_data_boundary"))
    if not boundary:
        add(checks, "hold", "privacy", "private_data_boundary is missing")
    elif boundary in {"local_only", "private", "regulated", "secret"} and as_bool(dataset.get("data_leaves_machine"), False) and not as_bool(dataset.get("provider_egress_approved"), False):
        add(checks, "fail", "privacy", "private data is configured to leave the machine without approval", boundary)
    else:
        add(checks, "pass", "privacy", "privacy boundary is recorded", boundary)
    if clean(dataset.get("data_version_or_hash")):
        add(checks, "pass", "dataset_hygiene", "data version or hash is recorded", dataset.get("data_version_or_hash"))
    else:
        add(checks, "hold", "dataset_hygiene", "data version or hash is missing")


def check_method_config(checks: list[dict[str, Any]], method_info: dict[str, Any], method: str) -> None:
    if method in {"lora", "qlora"}:
        rank = number(method_info.get("lora_rank"))
        if rank > 0:
            add(checks, "pass", "method_config", "LoRA rank is recorded", int(rank))
        else:
            add(checks, "hold", "method_config", "LoRA rank is missing")
        if list_value(method_info.get("target_modules")):
            add(checks, "pass", "method_config", "LoRA target modules are recorded", ", ".join(list_value(method_info.get("target_modules"))))
        else:
            add(checks, "hold", "method_config", "LoRA target modules are missing")
    if method == "qlora":
        if clean(method_info.get("quantized_base_plan")):
            add(checks, "pass", "method_config", "QLoRA quantized base plan is recorded", method_info.get("quantized_base_plan"))
        else:
            add(checks, "hold", "method_config", "QLoRA quantized base plan is missing")
    if method == "dpo":
        if clean(method_info.get("reference_model")):
            add(checks, "pass", "method_config", "DPO reference model is recorded", method_info.get("reference_model"))
        else:
            add(checks, "fail", "method_config", "DPO requires a reference model")
    if method == "distillation":
        if clean(method_info.get("teacher_model")):
            add(checks, "pass", "method_config", "distillation teacher model is recorded", method_info.get("teacher_model"))
        else:
            add(checks, "fail", "method_config", "distillation requires a teacher model")
    if method == "no_train":
        if clean(method_info.get("no_train_reason")):
            add(checks, "pass", "method_config", "no-train reason is recorded", method_info.get("no_train_reason"))
        else:
            add(checks, "hold", "method_config", "no-train decision needs a reason")
    if method in TRAINING_METHODS and clean(method_info.get("adapter_or_merge_plan")):
        add(checks, "pass", "method_config", "adapter, merge, or artifact plan is recorded", method_info.get("adapter_or_merge_plan"))
    elif method in TRAINING_METHODS:
        add(checks, "hold", "method_config", "adapter, merge, or artifact plan is missing")


def check_evaluation(checks: list[dict[str, Any]], evaluation: dict[str, Any], method: str) -> None:
    for key in ("heldout_eval_ready", "regression_suite_ready", "safety_regression_ready", "format_regression_ready"):
        if as_bool(evaluation.get(key), False):
            add(checks, "pass", "evaluation", f"{key} is ready")
        else:
            add(checks, "hold", "evaluation", f"{key} is missing or false")
    if clean(evaluation.get("pass_criteria")):
        add(checks, "pass", "evaluation", "pass criteria are recorded", evaluation.get("pass_criteria"))
    else:
        add(checks, "hold", "evaluation", "pass criteria are missing")
    if clean(evaluation.get("rerun_route")):
        add(checks, "pass", "evaluation", "post-adaptation rerun route is recorded", evaluation.get("rerun_route"))
    else:
        add(checks, "hold", "evaluation", "post-adaptation rerun route is missing")


def check_deployment(checks: list[dict[str, Any]], deployment: dict[str, Any], method: str) -> None:
    check_required_text(checks, deployment, "deployment", ["training_location", "runtime_target", "rollback_plan"])
    if method in {"qlora", "continued_pretraining"} and not clean(deployment.get("memory_plan")):
        add(checks, "hold", "deployment", "memory plan is required for this method")
    elif clean(deployment.get("memory_plan")):
        add(checks, "pass", "deployment", "memory plan is recorded", deployment.get("memory_plan"))
    if clean(deployment.get("retention_policy")):
        add(checks, "pass", "deployment", "retention policy is recorded", deployment.get("retention_policy"))
    else:
        add(checks, "hold", "deployment", "retention policy is missing")


def audit_manifest(path: Path) -> dict[str, Any]:
    manifest = load_json(path)
    manifest_dir = path.parent
    run_root = Path(clean(manifest.get("run_root"))).expanduser() if clean(manifest.get("run_root")) else manifest_dir
    vault_root = Path(clean(manifest.get("vault_root"))).expanduser() if clean(manifest.get("vault_root")) else None
    decision = manifest.get("decision") if isinstance(manifest.get("decision"), dict) else {}
    dataset = manifest.get("dataset") if isinstance(manifest.get("dataset"), dict) else {}
    method_info = manifest.get("method") if isinstance(manifest.get("method"), dict) else {}
    evaluation = manifest.get("evaluation") if isinstance(manifest.get("evaluation"), dict) else {}
    deployment = manifest.get("deployment") if isinstance(manifest.get("deployment"), dict) else {}
    artifacts = manifest.get("artifacts") if isinstance(manifest.get("artifacts"), dict) else {}
    method = method_name(decision.get("selected_method"))
    checks: list[dict[str, Any]] = []

    if method in TRAINING_METHODS or method in NO_DATA_METHODS:
        add(checks, "pass", "method", "selected method is recognized", method)
    else:
        add(checks, "fail", "method", "selected method is not recognized", method)

    check_decision(checks, decision, evaluation, method)
    check_dataset(checks, dataset, method)
    check_hygiene(checks, dataset, method)
    check_method_config(checks, method_info, method)
    check_evaluation(checks, evaluation, method)
    check_deployment(checks, deployment, method)
    check_artifacts(checks, artifacts, manifest_dir, run_root, vault_root, method)

    statuses = {check["status"] for check in checks}
    if "fail" in statuses:
        status = "fail"
        decision_status = "adaptation_blocked"
        next_route = "Repair baseline, method, privacy, split, or method-specific evidence before training or accepting the decision."
    elif "hold" in statuses:
        status = "hold"
        decision_status = "adaptation_incomplete"
        next_route = "Collect missing dataset, evaluation, tokenizer, privacy, compute, or rollback evidence."
    else:
        status = "pass"
        decision_status = "adaptation_ready"
        next_route = "Proceed to training/no-train memo, then rerun held-out evaluation and result synthesis."

    return {
        "run_id": clean(manifest.get("run_id")) or path.stem,
        "generated_at": now_iso(),
        "manifest": str(path),
        "status": status,
        "decision": decision_status,
        "next_route": next_route,
        "selected_method": method,
        "workload": clean(decision.get("workload")),
        "checks": checks,
    }


def write_outputs(result: dict[str, Any], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    stem = "adaptation-readiness-results"
    write_json(output_dir / f"{stem}.json", result)
    with (output_dir / f"{stem}.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["status", "gate", "message", "evidence"])
        writer.writeheader()
        writer.writerows(result["checks"])
    with (output_dir / f"{stem}.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(result, ensure_ascii=True) + "\n")
    lines = [
        f"# Adaptation Readiness: {result['status']} / {result['decision']}",
        "",
        f"- Run id: {result['run_id']}",
        f"- Generated: {result['generated_at']}",
        f"- Workload: {result.get('workload', '')}",
        f"- Selected method: {result.get('selected_method', '')}",
        f"- Next route: {result['next_route']}",
        "",
        "| Status | Gate | Message | Evidence |",
        "|---|---|---|---|",
    ]
    for check in result["checks"]:
        lines.append(f"| {md_cell(check['status'])} | {md_cell(check['gate'])} | {md_cell(check['message'])} | {md_cell(check.get('evidence', ''))} |")
    (output_dir / f"{stem}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    manifest_path = Path(argv[1]).expanduser() if len(argv) > 1 else Path(os.environ.get("LLM_ADAPTATION_READINESS_MANIFEST", "adaptation-readiness-manifest.json")).expanduser()
    if not manifest_path.exists():
        print(f"Manifest not found: {manifest_path}", file=sys.stderr)
        return 2
    result = audit_manifest(manifest_path)
    output_dir = Path(os.environ.get("LLM_ADAPTATION_READINESS_OUTPUT_DIR", "")).expanduser() if os.environ.get("LLM_ADAPTATION_READINESS_OUTPUT_DIR") else manifest_path.parent
    write_outputs(result, output_dir)
    print(json.dumps({"status": result["status"], "decision": result["decision"], "output_dir": str(output_dir)}, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
```

## Verification Fixtures

Use local fixtures before trusting the runner on a real adaptation decision:

| Fixture | Expected decision |
|---|---|
| LoRA plan with failing baseline, prompt-completion/chat data, held-out split, hygiene checks, LoRA config, eval route, local training boundary, and rollback artifacts | `pass/adaptation_ready` |
| SFT or LoRA selected while the baseline is recorded as already passing | `fail/adaptation_blocked` |
| DPO selected with prompt-completion data instead of preference pairs | `fail/adaptation_blocked` |
| Nonzero train/held-out overlap | `fail/adaptation_blocked` |
| Held-out eval or regression suite missing | `hold/adaptation_incomplete` |
| Private data leaves the machine without provider egress approval | `fail/adaptation_blocked` |
| QLoRA selected without quantized-base or memory plan | `hold/adaptation_incomplete` |
| No-train decision without a reason | `hold/adaptation_incomplete` |

## Handoff Map

| Need | Next note |
|---|---|
| Method choice before runner manifest | [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide]] |
| Baseline quality proof | [[LLM/Study/Local LLM Quality Evaluation Runner]] |
| Evaluation set design | [[LLM/Study/Local LLM Evaluation Set Design Runner]] |
| Tokenizer/template proof | [[LLM/Study/Chat Template and Tokenizer Compatibility Runner]] |
| RAG instead of training | [[LLM/Study/Local RAG Evidence Runner]] |
| Result synthesis after adaptation/no-train | [[LLM/Study/Local LLM Result Synthesis Runner]] |
| Deployment acceptance | [[LLM/Study/LLM Deployment Readiness Audit Runner]] |
| Capstone evidence | [[LLM/Study/LLM Mastery Capstone Workbook]] |

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide]]
- [[LLM/Study/Local LLM Quality Evaluation Runner]]
- [[LLM/Study/Local LLM Evaluation Set Design Runner]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Runner]]
- [[LLM/Study/Local LLM Result Synthesis Runner]]
- [[LLM/Study/LLM Deployment Readiness Audit Runner]]
- [[LLM/2018–2019 — Pretrained Language Models/Supervised Fine-Tuning]]
- [[LLM/2018–2019 — Pretrained Language Models/Data Curation and Deduplication]]
- [[LLM/2020–2021 — The Scaling Era/Parameter-Efficient Fine-Tuning]]
- [[LLM/2020–2021 — The Scaling Era/LoRA and QLoRA]]
- [[LLM/2022 — Alignment and Chat/Direct Preference Optimization]]
- [Hugging Face TRL SFTTrainer](https://huggingface.co/docs/trl/en/sft_trainer)
- [Hugging Face TRL DPOTrainer](https://huggingface.co/docs/trl/en/dpo_trainer)
- [Hugging Face TRL dataset formats](https://huggingface.co/docs/trl/en/dataset_formats)
- [Hugging Face PEFT LoRA](https://huggingface.co/docs/peft/package_reference/lora)
- [Hugging Face Transformers chat templates](https://huggingface.co/docs/transformers/en/chat_templating)
- [Hu et al. 2021, LoRA](https://arxiv.org/abs/2106.09685)
- [Dettmers et al. 2023, QLoRA](https://arxiv.org/abs/2305.14314)
- [Rafailov et al. 2023, DPO](https://arxiv.org/abs/2305.18290)
