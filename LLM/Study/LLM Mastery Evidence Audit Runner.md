---
tags: [study, llm, mastery, capstone, evidence, audit, local-llm, python]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
---

# LLM Mastery Evidence Audit Runner

> **One-line summary** LLM mastery is not a feeling or a large note collection; it is a linked evidence bundle whose academic, mechanism, implementation, local inference, RAG/tool, safety, operations, deployment, and exam gates can all be audited.

Use this with [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]] when the workbook, capstone folder, or exam attempt should become a repeatable pass, hold, fail, next-route, JSON, Markdown, CSV, and JSONL audit.

Use [[LLM/Study/LLM Mastery Exam Run Sheet|LLM Mastery Exam Run Sheet]] for the human oral/practical attempt. Use this runner after evidence links exist, or during a calibration pass when you need the next missing proof artifact without rereading the whole vault. If the output has many hold/fail rows, use [[LLM/Study/LLM Mastery Gap Triage Runner|LLM Mastery Gap Triage Runner]] to rank them into one next action.

This runner does not prove that an answer is intellectually correct by itself. It proves whether the evidence bundle has the required gates, links, statuses, and critical local-inference artifacts needed before a final human defense can count.

## What This Proves

| Gate family | Evidence checked | Why it matters |
|---|---|---|
| Academic understanding | paper map, paper claim ledger, metric interpretation, training pipeline | prevents local setup from replacing conceptual mastery |
| Mechanism bridge | tensor shapes, attention lab, tiny decoder, mechanism-to-inference rows | ties observed behavior to model internals |
| Local inference | workload, hardware sizing, model selection, custody, runtime, endpoint, client, benchmark, quality | proves you can host and call a local model |
| Extensions | RAG evidence, tool/schema evidence, adaptation decision | proves you can build a system, not only chat with a model |
| Safety and operations | security, privacy, observability, lifecycle, deployment decision | prevents unsafe or unmaintainable local serving |
| Exam and capstone | self-assessment, run sheet, final project note, remediation | proves the knowledge is available without hand-holding |

## Manifest Shape

Minimum manifest:

```json
{
  "run_id": "llm-mastery-audit-001",
  "run_root": "D:/llm-runs/mastery-audit",
  "vault_root": "D:/Vaults/PersonalKB",
  "gates": [
    {
      "gate_id": "academic-paper-map",
      "domain": "academic",
      "required": true,
      "critical": true,
      "status": "pass",
      "proof": "LLM/Study/LLM 20-Paper Fast Path Synthesis Map.md",
      "pass_signal": "Can explain architecture, scaling, alignment, RAG, evaluation, and inference links without notes.",
      "route": "LLM/Study/LLM 20-Paper Fast Path Synthesis Map"
    }
  ]
}
```

`proof` may be an absolute path, a vault-relative path, an Obsidian note path, or an Obsidian link. For a gate that is deliberately out of scope, set `required` to `false` and include `waiver_reason`.

## Default Required Gate Set

If the manifest omits `gates`, the runner uses a default gate list aligned to [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]:

| Domain | Required gates |
|---|---|
| academic | paper map, paper claim ledger, paper claim audit, paper oral defense, academic-to-local defense matrix, metric interpretation, judge calibration, training pipeline |
| mechanism | math/tensor shapes, attention implementation, tiny decoder training, mechanism-to-inference bridge |
| local-inference | workload/model selection, hardware sizing, model custody, artifact custody audit, runtime compatibility runner, first model pull runner, runtime health runner, first smoke request, first response debrief, template/tokenizer compatibility, endpoint, first endpoint evidence audit, API/client, application integration, reasoning budget audit, benchmark, scheduler evidence, evaluation set design, quality evaluation runner |
| system | RAG or tool proof, security/privacy, observability/lifecycle, result synthesis, deployment readiness audit, deployment decision |
| exam | self-assessment, recall/remediation audit, exam run sheet, capstone workbook/final note |

The default gates start in `hold` status. The point is to create a manifest, fill proof links, and rerun until the remaining gaps are explicit.

## Standard-Library Runner

Save the code block as `llm_mastery_evidence_audit_runner.py` or extract it directly from this note.

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


DEFAULT_GATES = [
    {
        "gate_id": "academic-paper-map",
        "domain": "academic",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/LLM 20-Paper Fast Path Synthesis Map",
        "pass_signal": "Can explain architecture, scaling, alignment, RAG, evaluation, and inference links without notes.",
    },
    {
        "gate_id": "academic-paper-claim-ledger",
        "domain": "academic",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/LLM Paper Claim Ledger",
        "pass_signal": "Every fast-path paper has claim, evidence, limitation, mechanism, local implication, and follow-up route.",
    },
    {
        "gate_id": "academic-paper-claim-audit",
        "domain": "academic",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/LLM Paper Claim Audit Runner",
        "pass_signal": "Fast-path paper coverage, claim anatomy, source proof, local implication, and follow-up proof routes are audited.",
    },
    {
        "gate_id": "academic-paper-oral-defense",
        "domain": "academic",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/LLM Paper Oral Defense Runner",
        "pass_signal": "Core paper clusters have no-notes answers with claim, evidence, limitation, mechanism, local implication, follow-up route, score, and remediation.",
    },
    {
        "gate_id": "academic-to-local-defense-matrix",
        "domain": "academic",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/LLM Academic-to-Local Defense Matrix Runner",
        "pass_signal": "Paper basis, mechanism, local prediction, artifact, metric, confounder, failure owner, decision, and oral answer are defended together.",
    },
    {
        "gate_id": "academic-metric-interpretation",
        "domain": "academic",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/LLM Metrics and Evaluation Interpretation Guide",
        "pass_signal": "Can classify loss, perplexity, benchmark, preference, calibration, quality, latency, and memory evidence.",
    },
    {
        "gate_id": "academic-judge-calibration",
        "domain": "academic",
        "required": True,
        "critical": False,
        "status": "hold",
        "route": "LLM/Study/Local LLM Judge Calibration Runner",
        "pass_signal": "LLM-as-judge quality evidence has human review, AB/BA order checks, agreement, position-bias, verbosity-bias, and next-route output before supporting repeated decisions.",
    },
    {
        "gate_id": "academic-training-pipeline",
        "domain": "academic",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/LLM Training Pipeline Map",
        "pass_signal": "Can trace one capability from data and objective through post-training, evaluation, adaptation, and deployment.",
    },
    {
        "gate_id": "mechanism-tensor-shapes",
        "domain": "mechanism",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/LLM Math and Tensor Shape Primer",
        "pass_signal": "Can trace token ids, embeddings, logits, loss, attention, weight memory, and KV cache.",
    },
    {
        "gate_id": "mechanism-attention-implementation",
        "domain": "mechanism",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/Attention Implementation Lab",
        "pass_signal": "Attention implementation has tensor-shape checks, masking tests, and a plain-language explanation.",
    },
    {
        "gate_id": "mechanism-tiny-decoder",
        "domain": "mechanism",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/Tiny Decoder-Only Transformer Training Lab",
        "pass_signal": "Tiny causal LM proves shifted targets, causal mask, train/validation loss, and generation.",
    },
    {
        "gate_id": "mechanism-bridge",
        "domain": "mechanism",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/LLM Mechanism-to-Inference Bridge Map",
        "pass_signal": "Local symptoms are tied to mechanisms, controls, evidence, and next decisions.",
    },
    {
        "gate_id": "local-workload-model-selection",
        "domain": "local-inference",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/Local LLM Model Selection Runner",
        "pass_signal": "Workload, hardware, candidate, memory, compatibility, benchmark, and quality facts produce a shortlist.",
    },
    {
        "gate_id": "local-hardware-sizing",
        "domain": "local-inference",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/Local LLM Hardware Sizing Runner",
        "pass_signal": "Candidate weight memory, KV-cache, runtime overhead, active sequences, context target, headroom, fit decision, and next route are captured before model pull or serving.",
    },
    {
        "gate_id": "local-model-custody",
        "domain": "local-inference",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/Local LLM Model Acquisition and Provenance Checklist",
        "pass_signal": "Model card, license, revision, artifact, local path, and unsafe-file risk are recorded.",
    },
    {
        "gate_id": "local-artifact-custody-audit",
        "domain": "local-inference",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/Local LLM Artifact Custody Audit Runner",
        "pass_signal": "Source identity, local bytes or runtime id, inventory, verification, unsafe-file decision, conversion/import proof, runtime handoff, and cleanup plan are audited before serving or deployment evidence depends on the artifact.",
    },
    {
        "gate_id": "local-runtime-compatibility",
        "domain": "local-inference",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/Local LLM Runtime Compatibility Runner",
        "pass_signal": "Architecture, artifact container, quantization, runtime support, tokenizer, chat template, route, model-id visibility, custody proof, sizing proof, compatibility decision, and next route are audited before model pull, health check, smoke test, or benchmark.",
    },
    {
        "gate_id": "local-first-model-pull",
        "domain": "local-inference",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/Local LLM First Model Pull Runner",
        "pass_signal": "Selected model, source check, store decision, runtime install proof, runtime compatibility proof, pull output, CLI/API inventory, show metadata, model visibility, digest check, decision, and next route are audited before runtime health or endpoint smoke.",
    },
    {
        "gate_id": "local-runtime-health",
        "domain": "local-inference",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/Local LLM First Runtime Health Runner",
        "pass_signal": "Listener reachability, native runtime API, installed model ids, running-model or idle state, OpenAI-compatible model ids, expected-model visibility, loopback boundary, decision, missing layer, and next route are audited before the first prompt.",
    },
    {
        "gate_id": "local-first-smoke-request",
        "domain": "local-inference",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/Local LLM First Smoke Request Runner",
        "pass_signal": "Runtime-health JSON, model id, native and OpenAI-compatible base URLs, prompt, expected text, temperature, max token cap, request files, response files, extracted output, route decisions, missing layer, and next action are saved for the first controlled local inference prompt.",
    },
    {
        "gate_id": "local-first-response-debrief",
        "domain": "local-inference",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/Local LLM First Response Debrief Runner",
        "pass_signal": "The saved first response is interpreted into health-bound smoke provenance, route proof, timing conversion, token-rate fields, mechanism owner, quality boundary, missing layer, and next action without sending another request.",
    },
    {
        "gate_id": "local-template-tokenizer-compatibility",
        "domain": "local-inference",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/Chat Template and Tokenizer Compatibility Runner",
        "pass_signal": "Health-bound first-response debrief, model package, tokenizer, chat template, rendered prompt or non-exposure control, route behavior, stop boundary, and downstream decision links are audited.",
    },
    {
        "gate_id": "local-endpoint",
        "domain": "local-inference",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/Local LLM First Endpoint Run Sheet",
        "pass_signal": "Local endpoint returns a response with model id, runtime, command, route, request, response, and timing.",
    },
    {
        "gate_id": "local-first-endpoint-evidence-audit",
        "domain": "local-inference",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/Local LLM First Endpoint Evidence Audit Runner",
        "pass_signal": "The first endpoint run folder has checked run card, preflight, runtime install state, model custody, runtime health, smoke response, pass-state debrief, template/tokenizer compatibility, boundary, and decision gates.",
    },
    {
        "gate_id": "local-api-client",
        "domain": "local-inference",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/Local LLM OpenAI-Compatible API Contract Runner",
        "pass_signal": "Client route, model id, non-streaming or streaming behavior, and harmless failure are saved.",
    },
    {
        "gate_id": "local-application-integration",
        "domain": "local-inference",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/Local LLM Application Integration Evidence Runner",
        "pass_signal": "The local endpoint is wired into an app, CLI, UI, job, RAG assistant, or tool loop with app contract, user flow, response handling, failure behavior, privacy/logging, evaluation, operations, and promotion evidence.",
    },
    {
        "gate_id": "local-reasoning-budget",
        "domain": "local-inference",
        "required": True,
        "critical": False,
        "status": "hold",
        "route": "LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Runner",
        "pass_signal": "Reasoning-capable local runs have fixed controls, parser separation, effort sweep, latency and quality delta, trace policy, selected effort, and retest trigger evidence before quality, runtime, result-synthesis, or deployment decisions depend on reasoning mode.",
    },
    {
        "gate_id": "local-failure-triage",
        "domain": "local-inference",
        "required": True,
        "critical": False,
        "status": "hold",
        "route": "LLM/Study/Local LLM Failure Triage Runner",
        "pass_signal": "Any failed local run has symptom, canonical failed layer, proof, mechanism owner, ruled-out layers, and one controlled next action.",
    },
    {
        "gate_id": "local-benchmark",
        "domain": "local-inference",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/Local LLM Inference Benchmark Log",
        "pass_signal": "TTFT, TPOT, tokens/sec, total latency, memory, quality, and decision are interpreted.",
    },
    {
        "gate_id": "local-scheduler-evidence",
        "domain": "local-inference",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/Local LLM Scheduler Evidence Audit Runner",
        "pass_signal": "Scheduler, KV-cache, queue, long-prompt, tuning, capacity, and decision-card evidence are audited before serving-policy claims.",
    },
    {
        "gate_id": "local-evaluation-set-design",
        "domain": "local-inference",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/Local LLM Evaluation Set Design Runner",
        "pass_signal": "Prompt suite has workload, quality bar, required task classes, held-out/private rows, contamination controls, rubric, pass criteria, refresh plan, and downstream routes before quality scoring.",
    },
    {
        "gate_id": "local-quality",
        "domain": "local-inference",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/Local LLM Quality Evaluation Runner",
        "pass_signal": "Saved prompt-suite cases have prompt and response proof, rubric scores, boundary-specific evidence, and pass/hold/fail runner output.",
    },
    {
        "gate_id": "system-rag-or-tool",
        "domain": "system",
        "required": True,
        "critical": False,
        "status": "hold",
        "route": "LLM/Study/Local RAG Evidence Runner",
        "alternative_routes": ["LLM/Study/Local LLM Tool Calling and Structured Output Runner"],
        "pass_signal": "RAG or tool path has saved evidence, refusal or denial behavior, and failure diagnosis.",
    },
    {
        "gate_id": "system-security-privacy",
        "domain": "system",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/Local LLM Security and Privacy Runner",
        "pass_signal": "Endpoint exposure, logs, RAG/tool/UI/export boundaries, and secrets are checked.",
    },
    {
        "gate_id": "system-operations-lifecycle",
        "domain": "system",
        "required": True,
        "critical": False,
        "status": "hold",
        "route": "LLM/Study/Local LLM Observability and Operations Runner",
        "alternative_routes": ["LLM/Study/Local LLM Service Lifecycle and Upgrade Runner"],
        "pass_signal": "Model state, metrics/logs/resource pressure, restart or lifecycle proof, and next action are saved.",
    },
    {
        "gate_id": "system-result-synthesis",
        "domain": "system",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/Local LLM Result Synthesis Runner",
        "pass_signal": "Endpoint, compatibility, benchmark, eval-set, quality, security, operations, rejected-alternative, and review-trigger evidence are reconciled into a keep/tune/reject/deploy decision.",
    },
    {
        "gate_id": "system-deployment-readiness-audit",
        "domain": "system",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/LLM Deployment Readiness Audit Runner",
        "pass_signal": "Deployment readiness audit checks workload, selected path, model/runtime, endpoint/client, benchmark, quality, security, operations, cost, rejected alternative, and retest proof.",
    },
    {
        "gate_id": "system-deployment-decision",
        "domain": "system",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/LLM Deployment Decision Matrix",
        "pass_signal": "Deployment memo chooses local, self-hosted, hosted, hybrid, or batch with rejected alternatives.",
    },
    {
        "gate_id": "exam-self-assessment",
        "domain": "exam",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/LLM Mastery Self-Assessment Exam",
        "pass_signal": "Overall score is at least 80 percent with no zero in practical sections and linked remediation.",
    },
    {
        "gate_id": "exam-recall-remediation-audit",
        "domain": "exam",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/LLM Recall and Remediation Audit Runner",
        "pass_signal": "Scored recall or exam rows cover required domains, route low-score misses, link remediation artifacts and next reviews, and avoid hard-fail zeroes in applied domains.",
    },
    {
        "gate_id": "exam-run-sheet",
        "domain": "exam",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/LLM Mastery Exam Run Sheet",
        "pass_signal": "One scored attempt has proof links, hard-fail checks, and remediation rows.",
    },
    {
        "gate_id": "exam-capstone-ledger",
        "domain": "exam",
        "required": True,
        "critical": True,
        "status": "hold",
        "route": "LLM/Study/LLM Mastery Capstone Workbook",
        "pass_signal": "Workbook or dated capstone note links every required evidence item and final decision.",
    },
]

STATUS_VALUES = {
    "pass": "pass",
    "passed": "pass",
    "complete": "pass",
    "ready": "pass",
    "hold": "hold",
    "blocked": "hold",
    "gap": "hold",
    "missing": "hold",
    "not-started": "hold",
    "not started": "hold",
    "in-progress": "hold",
    "in progress": "hold",
    "fail": "fail",
    "failed": "fail",
    "rejected": "fail",
    "unsafe": "fail",
}

STATUS_RANK = {"pass": 0, "hold": 1, "fail": 2}
DOMAIN_ORDER = {"academic": 0, "mechanism": 1, "local-inference": 2, "system": 3, "exam": 4}
LINK_OPEN = "[" + "["
LINK_CLOSE = "]" + "]"


def utc_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def slug(value: Any) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value or "").strip().lower())
    return text.strip("-") or "llm-mastery-audit"


def norm(value: Any) -> str:
    return str(value or "").strip().lower()


def status_value(value: Any) -> str:
    return STATUS_VALUES.get(norm(value).replace("_", "-"), "hold")


def bool_value(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if value in (None, ""):
        return default
    text = norm(value).replace("_", "-").replace(" ", "-")
    if text in {"true", "yes", "y", "1", "required", "critical"}:
        return True
    if text in {"false", "no", "n", "0", "optional", "waived", "not-required"}:
        return False
    return default


def list_value(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, tuple):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str):
        stripped = value.strip()
        if not stripped:
            return []
        if stripped.startswith("["):
            try:
                parsed = json.loads(stripped)
                if isinstance(parsed, list):
                    return [str(item).strip() for item in parsed if str(item).strip()]
            except json.JSONDecodeError:
                pass
        return [part.strip() for part in stripped.split(",") if part.strip()]
    return [str(value).strip()] if str(value).strip() else []


def load_manifest() -> tuple[Path, dict[str, Any]]:
    manifest_path = os.environ.get("LLM_MASTERY_AUDIT_MANIFEST")
    if not manifest_path:
        raise ValueError("Set LLM_MASTERY_AUDIT_MANIFEST to a JSON manifest path.")
    path = Path(manifest_path).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"Manifest path does not exist: {path}")
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError("Manifest must be a JSON object.")
    return path, data


def strip_obsidian_link(value: str) -> str:
    text = value.strip()
    if text.startswith(LINK_OPEN) and text.endswith(LINK_CLOSE):
        inner = text[2:-2]
        return inner.split("|", 1)[0].split("#", 1)[0].strip()
    return text


def proof_candidates(vault_root: Path, proof: str) -> list[Path]:
    proof_text = strip_obsidian_link(proof)
    if not proof_text:
        return []
    path = Path(proof_text).expanduser()
    candidates: list[Path] = []
    if path.is_absolute():
        candidates.append(path)
        if path.suffix == "":
            candidates.append(path.with_suffix(".md"))
    else:
        candidates.append(vault_root / path)
        if path.suffix == "":
            candidates.append((vault_root / path).with_suffix(".md"))
    return [candidate.resolve() for candidate in candidates]


def proof_exists(vault_root: Path, proof: str) -> tuple[bool, str]:
    if not proof.strip():
        return False, ""
    for candidate in proof_candidates(vault_root, proof):
        if candidate.exists():
            return True, str(candidate)
    return False, str(proof_candidates(vault_root, proof)[0]) if proof_candidates(vault_root, proof) else proof


def wiki_link(route: str) -> str:
    return LINK_OPEN + route + LINK_CLOSE


def route_for_gate(gate: dict[str, Any]) -> str:
    route = str(gate.get("route") or gate.get("proof") or "")
    if route:
        return strip_obsidian_link(route).removesuffix(".md")
    alternatives = list_value(gate.get("alternative_routes"))
    if alternatives:
        return strip_obsidian_link(alternatives[0]).removesuffix(".md")
    return "LLM/Study/LLM Mastery Dashboard"


def finding(level: str, owner: str, text: str, evidence: str, action: str) -> dict[str, str]:
    return {
        "level": level,
        "owner": owner,
        "finding": text,
        "evidence": evidence,
        "action": action,
    }


def evaluate_gate(gate: dict[str, Any], vault_root: Path) -> dict[str, Any]:
    gate_id = str(gate.get("gate_id") or gate.get("id") or gate.get("name") or "")
    domain = str(gate.get("domain") or "unspecified")
    required = bool_value(gate.get("required"), True)
    critical = bool_value(gate.get("critical"), False)
    declared_status = status_value(gate.get("status"))
    proof = str(gate.get("proof") or gate.get("proof_path") or gate.get("evidence") or "")
    pass_signal = str(gate.get("pass_signal") or "")
    waiver_reason = str(gate.get("waiver_reason") or "")
    findings: list[dict[str, str]] = []

    if not gate_id:
        findings.append(finding(
            "hold",
            domain,
            "Gate id is missing.",
            str(gate),
            "Give every gate a stable id or gate_id before auditing.",
        ))

    if not required:
        if not waiver_reason:
            findings.append(finding(
                "hold",
                domain,
                "Optional or out-of-scope gate has no waiver reason.",
                gate_id,
                "Record why this gate is not required for the current capstone.",
            ))
        elif declared_status == "fail":
            findings.append(finding(
                "fail",
                domain,
                "Waived gate is marked failed.",
                gate_id,
                "Either remove the waiver or resolve the failure.",
            ))
        status = "hold" if findings else "pass"
        decision = "waiver_needs_reason" if findings else "waived_with_reason"
        next_route = route_for_gate(gate)
        return {
            "gate_id": gate_id,
            "domain": domain,
            "required": required,
            "critical": critical,
            "declared_status": declared_status,
            "status": status,
            "decision": decision,
            "proof": proof,
            "proof_resolved": "",
            "proof_exists": False,
            "pass_signal": pass_signal,
            "next_route": next_route,
            "next_action": findings[0]["action"] if findings else "Keep waiver with reason in the capstone ledger.",
            "findings": findings,
        }

    if declared_status == "fail":
        findings.append(finding(
            "fail",
            domain,
            "Gate is explicitly marked fail.",
            gate_id,
            "Resolve the failed evidence before claiming mastery.",
        ))
    elif declared_status != "pass":
        findings.append(finding(
            "hold",
            domain,
            "Gate is not marked pass.",
            declared_status,
            "Complete the evidence route and set status to pass only after the pass signal is met.",
        ))

    exists = False
    proof_resolved = ""
    if proof:
        exists, proof_resolved = proof_exists(vault_root, proof)
        if not exists:
            findings.append(finding(
                "hold",
                domain,
                "Proof link or path does not resolve in the vault.",
                proof_resolved,
                "Fix the proof path or create the linked evidence artifact.",
            ))
    else:
        findings.append(finding(
            "hold",
            domain,
            "Required gate has no proof link or path.",
            gate_id,
            "Add a proof link to the capstone workbook or manifest.",
        ))

    if not pass_signal:
        findings.append(finding(
            "hold",
            domain,
            "Gate has no explicit pass signal.",
            gate_id,
            "Write the observable evidence condition that makes this gate pass.",
        ))

    if critical and declared_status == "pass" and not proof:
        findings.append(finding(
            "fail",
            domain,
            "Critical gate is marked pass without proof.",
            gate_id,
            "A critical mastery gate needs linked evidence, not only status text.",
        ))

    fail_count = sum(1 for item in findings if item["level"] == "fail")
    hold_count = sum(1 for item in findings if item["level"] == "hold")
    if fail_count:
        status = "fail"
        decision = "gate_failed"
    elif hold_count:
        status = "hold"
        decision = "gate_incomplete"
    else:
        status = "pass"
        decision = "gate_ready"

    next_route = route_for_gate(gate)
    next_action = findings[0]["action"] if findings else "Keep this proof linked in the capstone ledger."
    return {
        "gate_id": gate_id,
        "domain": domain,
        "required": required,
        "critical": critical,
        "declared_status": declared_status,
        "status": status,
        "decision": decision,
        "proof": proof,
        "proof_resolved": proof_resolved,
        "proof_exists": exists,
        "pass_signal": pass_signal,
        "next_route": next_route,
        "next_action": next_action,
        "findings": findings,
    }


def domain_summary(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    domains = sorted({row["domain"] for row in rows}, key=lambda item: (DOMAIN_ORDER.get(item, 99), item))
    summary: list[dict[str, Any]] = []
    for domain in domains:
        subset = [row for row in rows if row["domain"] == domain]
        summary.append({
            "domain": domain,
            "gate_count": len(subset),
            "pass_count": sum(1 for row in subset if row["status"] == "pass"),
            "hold_count": sum(1 for row in subset if row["status"] == "hold"),
            "fail_count": sum(1 for row in subset if row["status"] == "fail"),
            "critical_missing": sum(1 for row in subset if row["critical"] and row["status"] != "pass"),
        })
    return summary


def missing_domain_gate(domain: str) -> dict[str, Any]:
    return {
        "gate_id": f"domain-{domain}-coverage",
        "domain": domain,
        "required": True,
        "critical": True,
        "declared_status": "hold",
        "status": "hold",
        "decision": "domain_missing",
        "proof": "",
        "proof_resolved": "",
        "proof_exists": False,
        "pass_signal": f"Manifest includes at least one {domain} gate.",
        "next_route": "LLM/Study/LLM Mastery Capstone Workbook",
        "next_action": f"Add at least one {domain} evidence gate to the mastery audit manifest.",
        "findings": [finding(
            "hold",
            domain,
            "Required evidence domain is missing from the manifest.",
            domain,
            f"Add at least one {domain} gate before using the audit as mastery evidence.",
        )],
    }


def csv_cell(value: Any) -> str:
    if isinstance(value, list):
        return ";".join(str(item) for item in value)
    if value is None:
        return ""
    return str(value)


def csv_write(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "gate_id",
        "domain",
        "required",
        "critical",
        "declared_status",
        "status",
        "decision",
        "proof",
        "proof_exists",
        "pass_signal",
        "next_route",
        "next_action",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: csv_cell(row.get(field)) for field in fields})


def md_cell(value: Any) -> str:
    return csv_cell(value).replace("|", "\\|").replace("\n", " ")


def render_markdown(record: dict[str, Any]) -> str:
    lines = [
        f"# LLM Mastery Evidence Audit - {record['run_id']}",
        "",
        f"- Created: `{record['created_at']}`",
        f"- Status: `{record['status']}`",
        f"- Decision: `{record['decision']}`",
        f"- Vault root: `{record['vault_root']}`",
        f"- Gates: `{record['gate_count']}`",
        f"- Pass/Hold/Fail: `{record['pass_count']}` / `{record['hold_count']}` / `{record['fail_count']}`",
        f"- Critical gaps: `{record['critical_gap_count']}`",
        "",
        "## Domain Summary",
        "",
        "| Domain | Gates | Pass | Hold | Fail | Critical gaps |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in record["domains"]:
        lines.append(
            "| "
            + " | ".join([
                md_cell(row["domain"]),
                md_cell(row["gate_count"]),
                md_cell(row["pass_count"]),
                md_cell(row["hold_count"]),
                md_cell(row["fail_count"]),
                md_cell(row["critical_missing"]),
            ])
            + " |"
        )
    lines.extend([
        "",
        "## Gate Results",
        "",
        "| Gate | Domain | Critical | Status | Proof exists | Next route |",
        "|---|---|---:|---|---:|---|",
    ])
    for row in record["gates"]:
        lines.append(
            "| "
            + " | ".join([
                md_cell(row["gate_id"]),
                md_cell(row["domain"]),
                md_cell(row["critical"]),
                md_cell(row["status"]),
                md_cell(row["proof_exists"]),
                md_cell(wiki_link(row["next_route"])),
            ])
            + " |"
        )
    lines.extend([
        "",
        "## Next Actions",
        "",
    ])
    incomplete = [row for row in record["gates"] if row["status"] != "pass"]
    for row in incomplete:
        lines.append(f"- `{row['gate_id']}` -> {wiki_link(row['next_route'])}: {row['next_action']}")
    if not incomplete:
        lines.append("- Evidence gates are ready for a human oral/practical defense.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    manifest_path, manifest = load_manifest()
    vault_root = Path(manifest.get("vault_root") or os.environ.get("LLM_MASTERY_AUDIT_VAULT_ROOT") or manifest_path.parent).expanduser().resolve()
    run_id = str(manifest.get("run_id") or os.environ.get("LLM_MASTERY_AUDIT_RUN_ID") or f"{utc_stamp()}-{slug(manifest_path.stem)}")
    run_root_value = os.environ.get("LLM_MASTERY_AUDIT_RUN_ROOT") or manifest.get("run_root", "llm-mastery-audit-runs")
    run_root = Path(str(run_root_value)).expanduser()
    if not run_root.is_absolute():
        run_root = manifest_path.parent / run_root
    run_root = run_root.resolve()
    run_dir = run_root / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    gates = manifest.get("gates")
    if gates is None:
        gates = DEFAULT_GATES
    if not isinstance(gates, list) or not all(isinstance(row, dict) for row in gates):
        raise ValueError("Manifest gates must be a list of objects.")

    evaluated = [evaluate_gate(dict(gate), vault_root) for gate in gates]
    required_domains = list_value(manifest.get("required_domains")) or ["academic", "mechanism", "local-inference", "system", "exam"]
    present_domains = {row["domain"] for row in evaluated}
    for domain in required_domains:
        if domain not in present_domains:
            evaluated.append(missing_domain_gate(domain))

    evaluated.sort(key=lambda row: (
        STATUS_RANK.get(row["status"], 3),
        DOMAIN_ORDER.get(row["domain"], 99),
        row["gate_id"],
    ))

    pass_count = sum(1 for row in evaluated if row["status"] == "pass")
    hold_count = sum(1 for row in evaluated if row["status"] == "hold")
    fail_count = sum(1 for row in evaluated if row["status"] == "fail")
    critical_gap_count = sum(1 for row in evaluated if row["critical"] and row["status"] != "pass")

    domain_rows = domain_summary(evaluated)
    if fail_count:
        status = "fail"
        decision = "mastery_evidence_failed"
    elif hold_count or critical_gap_count:
        status = "hold"
        decision = "mastery_evidence_incomplete"
    else:
        status = "pass"
        decision = "mastery_evidence_ready_for_defense"

    record = {
        "run_id": run_id,
        "created_at": utc_iso(),
        "status": status,
        "decision": decision,
        "manifest_path": str(manifest_path),
        "vault_root": str(vault_root),
        "gate_count": len(evaluated),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "critical_gap_count": critical_gap_count,
        "domains": domain_rows,
        "gates": evaluated,
        "outputs": {},
    }

    json_path = run_dir / f"{run_id}-mastery-audit.json"
    markdown_path = run_dir / f"{run_id}-mastery-audit.md"
    csv_path = run_dir / f"{run_id}-mastery-audit.csv"
    jsonl_path = run_root / "llm-mastery-audit-runs.jsonl"
    record["outputs"] = {
        "json": str(json_path),
        "markdown": str(markdown_path),
        "csv": str(csv_path),
        "jsonl": str(jsonl_path),
    }

    csv_write(csv_path, evaluated)
    json_path.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    markdown_path.write_text(render_markdown(record), encoding="utf-8")
    with jsonl_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(json.dumps({
        "status": status,
        "decision": decision,
        "run_id": run_id,
        "gate_count": len(evaluated),
        "pass_count": pass_count,
        "hold_count": hold_count,
        "fail_count": fail_count,
        "critical_gap_count": critical_gap_count,
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
$env:LLM_MASTERY_AUDIT_MANIFEST = "D:\llm-runs\mastery-audit\mastery-audit-manifest.json"
$env:LLM_MASTERY_AUDIT_VAULT_ROOT = "D:\Vaults\PersonalKB"
$env:LLM_MASTERY_AUDIT_RUN_ROOT = "D:\llm-runs\mastery-audit"
python .\llm_mastery_evidence_audit_runner.py
```

## Reading The Result

| Runner status | Meaning | Next route |
|---|---|---|
| `pass/mastery_evidence_ready_for_defense` | every required gate is pass, proof links resolve, critical gates have evidence, and waived gates have reasons | take the oral/practical defense using [[LLM/Study/LLM Mastery Exam Run Sheet]] |
| `hold/mastery_evidence_incomplete` | required evidence, proof link, pass signal, or critical gate is missing | use [[LLM/Study/LLM Mastery Gap Triage Runner|LLM Mastery Gap Triage Runner]] when more than one gate is held, otherwise follow the held gate's `next_route` |
| `fail/mastery_evidence_failed` | a gate is explicitly failed, unsafe, or rejected | fix the failed gate before claiming mastery |

This runner can pass only the evidence bundle. The final mastery claim still needs the human exam and capstone defense.

## Capstone Row

| Evidence | Output |
|---|---|
| Mastery evidence audit runner | `<run-id>-mastery-audit.json`, `<run-id>-mastery-audit.md`, `<run-id>-mastery-audit.csv`, and one `llm-mastery-audit-runs.jsonl` row |

## Completion Gate

This runner is useful when:

- [ ] the manifest includes academic, mechanism, local-inference, system, and exam gates
- [ ] every required gate has a proof link or path
- [ ] critical gates cannot pass without proof
- [ ] waived optional gates include a reason
- [ ] output JSON, Markdown, CSV, and JSONL artifacts are saved
- [ ] incomplete gates route to the lowest next proof artifact
- [ ] if multiple critical gates are incomplete, a gap triage output names the top next action

## References

- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Mastery Dashboard]]
- [[LLM/Study/LLM Mastery Roadmap]]
- [[LLM/Study/LLM Mastery Gap Triage Runner]]
- [[LLM/Study/LLM Mastery Self-Assessment Exam]]
- [[LLM/Study/LLM Mastery Exam Run Sheet]]
- [[LLM/Study/LLM Recall and Remediation Audit Runner]]
- [[LLM/Study/Local LLM Capstone Project Blueprint]]
- [[LLM/Study/LLM Paper Claim Ledger]]
- [[LLM/Study/LLM Paper Claim Audit Runner]]
- [[LLM/Study/LLM Paper Oral Defense Runner]]
- [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner]]
- [[LLM/Study/Local LLM Judge Calibration Runner]]
- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]]
- [[LLM/Study/Local LLM Hardware Sizing Runner]]
- [[LLM/Study/Local LLM Model Selection Runner]]
- [[LLM/Study/Local LLM Artifact Custody Audit Runner]]
- [[LLM/Study/Local LLM Runtime Compatibility Runner]]
- [[LLM/Study/Local LLM First Model Pull Runner]]
- [[LLM/Study/Local LLM First Runtime Health Runner]]
- [[LLM/Study/Local LLM First Smoke Request Runner]]
- [[LLM/Study/Local LLM First Response Debrief Runner]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Runner]]
- [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner]]
- [[LLM/Study/Local LLM Application Integration Evidence Runner]]
- [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Runner]]
- [[LLM/Study/Local LLM Failure Triage Runner]]
- [[LLM/Study/Local LLM Scheduler Evidence Audit Runner]]
- [[LLM/Study/Local LLM Evaluation Set Design Runner]]
- [[LLM/Study/Local LLM Quality Evaluation Runner]]
- [[LLM/Study/Local RAG Evidence Runner]]
- [[LLM/Study/Local LLM Security and Privacy Runner]]
- [[LLM/Study/Local LLM Result Synthesis Runner]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/Study/LLM Deployment Readiness Audit Runner]]
