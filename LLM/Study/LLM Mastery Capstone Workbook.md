---
tags: [study, llm, capstone, mastery]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [practice]
---

# LLM Mastery Capstone Workbook

> **One-line summary** Mastery becomes credible only when the conceptual, implementation, local inference, RAG, evaluation, adaptation, and deployment artifacts are linked in one evidence ledger.

Use this with [[LLM/Study/LLM Mastery Roadmap|LLM Mastery Roadmap]]. The roadmap defines the gates; this workbook collects the proof.

## How to Use

Copy the blank ledger into a dated capstone note, or fill the proof links directly here. A gate is complete only when the artifact exists, the evidence is linked, and the pass signal is explicit.

## Evidence Ledger

| Gate | Required artifact | Proof link/path | Pass signal | Status |
|---|---|---|---|---|
| Paper map | One-page map of the 20-paper fast path using [[LLM/Study/LLM Paper Reading Protocol|LLM Paper Reading Protocol]] |  | Can explain architecture, scaling, alignment, RAG, evaluation, and inference links without notes. | Not started |
| Training pipeline map | One capability trace using [[LLM/Study/LLM Training Pipeline Map|LLM Training Pipeline Map]] |  | Can trace raw data, objective, pretraining, post-training, evaluation, adaptation, deployment, and the likely failure owner. | Not started |
| Self-assessment | Passed [[LLM/Study/LLM Mastery Self-Assessment Exam|LLM Mastery Self-Assessment Exam]] |  | Overall score is at least 80 percent, no zero in practical sections, and missed-question remediation is linked. | Not started |
| Attention implementation | Implementation output from [[LLM/Study/Attention Implementation Lab|Attention Implementation Lab]] |  | Code or notebook has tensor-shape checks, masking tests, and a plain-language explanation. | Not started |
| Tiny decoder training | Lab output from [[LLM/Study/Tiny Decoder-Only Transformer Training Lab|Tiny Decoder-Only Transformer Training Lab]] |  | Tiny causal LM has shifted-target example, mask test, train/validation loss, generated samples, and overfitting or undertraining explanation. | Not started |
| Local model endpoint | CLI and HTTP proof from [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]] and [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]] |  | Local endpoint returns a response; model id, runtime, command, and loopback URL are captured. | Not started |
| Model acquisition | Provenance card from [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]] |  | Model card, license, gated access, artifact format, revision/tag/digest, local path, and unsafe-file decision are captured. | Not started |
| Runtime compatibility | Evidence card from [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]] |  | Artifact format, quantization, tokenizer, chat template, runtime, model id, route, and workload contract are captured. | Not started |
| OpenAI-compatible API contract | Contract card from [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] |  | Base URL, route, served model id, non-streaming response, streaming decision, harmless failure, and required feature gaps are captured. | Not started |
| Decoding controls | Sweep from [[LLM/Study/Decoding and Sampling Controls Lab|Decoding and Sampling Controls Lab]] |  | Baseline sampler settings, temperature/filter sweep, penalty test, stop/schema result, and runtime support gaps are captured. | Not started |
| Context/token budget | Budget row from [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]] |  | Runtime context limit, rendered prompt tokens, output reserve, RAG/tool/history tokens, safety margin, and truncation policy are captured. | Not started |
| Benchmark record | Run entry in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] |  | Model, runtime, quantization, hardware, context length, TTFT, tokens/sec, memory, and quality decision are recorded. | Not started |
| Failure diagnosis | Diagnostic row from [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]] |  | At least one failure or explicit no-failure row names the layer, evidence, controlled change, and result. | Not started |
| Local quality gate | Prompt-suite result from [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] |  | Known-answer, schema, RAG/citation, long-context, multi-turn, and workload prompts have scored pass/hold/fail decisions where relevant. | Not started |
| RAG assistant | Local retrieval assistant from [[LLM/Study/Local RAG Assistant Lab|Local RAG Assistant Lab]] and artifact set from [[LLM/Study/Local RAG Minimal Python Harness|Local RAG Minimal Python Harness]] |  | Corpus manifest, chunking policy, index metadata, retrieval evidence, cited answer, unsupported-question refusal, benchmark row, quality row, and at least one diagnosed failure are captured. | Not started |
| Tool loop | Tool-calling proof from [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]] |  | Tool schema, validated arguments, policy check, execution result, injected tool result, bounded loop, and failure rows are captured. | Not started |
| Adaptation decision | Memo using [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide|LLM Adaptation and Fine-Tuning Decision Guide]] |  | Prompting, RAG, SFT, LoRA, QLoRA, DPO, distillation, continued pretraining, or no-train decision is justified from the measured failure mode, data, eval, compute, and rollback evidence. | Not started |
| Deployment decision | Memo using [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]] |  | Choice between local CPU, local GPU, self-hosted server, hosted API, hybrid, or batch inference is justified with workload, quality, latency, memory/cost, privacy, and operational evidence. | Not started |

## Paper Map Output Template

Use one paragraph per cluster, not one paragraph per paper.

| Axis | Before | After | Lever to explain |
|---|---|---|---|
| Architecture |  |  | Attention, recurrence removal, decoder-only lineage |
| Scaling |  |  | Parameter, data, compute, and inference trade-offs |
| Alignment |  |  | SFT, RLHF, DPO, Constitutional AI, safety evaluation |
| Adaptation |  |  | Prompting, LoRA, QLoRA, distillation, fine-tuning |
| Retrieval and tools |  |  | RAG, embeddings, chunking, function calling, agents |
| Evaluation and serving |  |  | Benchmarks, LLM-as-judge, throughput, latency, KV cache |

## Training Pipeline Proof Template

| Evidence item | Link or value |
|---|---|
| Capability or behavior traced |  |
| Data source likely responsible |  |
| Training objective |  |
| Post-training stage |  |
| Evaluation gate |  |
| Adaptation or RAG layer |  |
| Deployment constraint |  |
| Likely failure owner | data / objective / SFT / preference / RAG / runtime / policy |
| Wrong fix rejected |  |

## Self-Assessment Proof Template

| Evidence item | Link or value |
|---|---|
| Exam date |  |
| Overall score |  |
| Sections below pass threshold |  |
| Local inference practical score |  |
| RAG/evaluation score |  |
| Security/deployment score |  |
| Missed-question remediation links |  |
| Retake date, if needed |  |

## Attention Implementation Proof Template

| Evidence item | Link or value |
|---|---|
| File or notebook |  |
| Input tensor shape |  |
| Q/K/V projection shapes |  |
| Attention score shape |  |
| Mask test |  |
| Softmax sanity check |  |
| Output shape |  |
| Multi-head reshape proof |  |
| Tests run |  |
| Failure fixed |  |

## Tiny Decoder Training Proof Template

| Evidence item | Link or value |
|---|---|
| Corpus/source |  |
| Tokenization/vocabulary |  |
| Train/validation split |  |
| Input/target shift example |  |
| Causal mask test |  |
| Model parameter count |  |
| Training loss samples |  |
| Validation loss samples |  |
| Generated low-temperature sample |  |
| Generated higher-temperature or top-k sample |  |
| Overfitting or undertraining note |  |
| Code/notebook path |  |

## Local Inference Proof Template

| Evidence item | Link or value |
|---|---|
| Hardware |  |
| Acquisition/provenance card |  |
| Runtime |  |
| Compatibility evidence card |  |
| Artifact format |  |
| Tokenizer and chat template |  |
| Model id |  |
| Quantization |  |
| Context length |  |
| Context budget row |  |
| CLI command |  |
| HTTP endpoint |  |
| OpenAI-compatible API contract |  |
| Decoding/sampling preset |  |
| Sampler sweep result |  |
| Truncation/overflow behavior |  |
| Successful response |  |
| Benchmark row |  |
| Quality-harness result |  |
| Serving issue diagnosed |  |
| Failed layer named |  |

## RAG Proof Template

| Evidence item | Link or value |
|---|---|
| Corpus version |  |
| Chunking policy |  |
| Embedding model |  |
| Index location/metadata |  |
| Retriever settings |  |
| Reranker settings |  |
| Top-k evidence example |  |
| Cited answer example |  |
| Retrieval miss diagnosed |  |
| Bad chunk diagnosed |  |
| Hallucination or citation failure diagnosed |  |

## Tool-Calling Proof Template

| Evidence item | Link or value |
|---|---|
| Tool contract card |  |
| Structured-output baseline |  |
| Runtime route and tool-choice mode |  |
| Tool schema version |  |
| Tool call observed |  |
| Argument validation result |  |
| Policy allow/deny result |  |
| Tool execution result |  |
| Tool-result injection proof |  |
| Bounded loop settings |  |
| Wrong-tool or bad-argument failure |  |
| Unsafe-action denial |  |
| Quality harness tool row |  |

## Evaluation Proof Template

| Evidence item | Link or value |
|---|---|
| Prompt suite |  |
| Scoring rubric |  |
| Thresholds |  |
| Human calibration notes |  |
| LLM-as-judge notes |  |
| Pass decisions |  |
| Hold decisions |  |
| Fail decisions |  |
| Changes made after evaluation |  |

## Adaptation Decision Memo

Use [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide|LLM Adaptation and Fine-Tuning Decision Guide]] before training or deciding not to train.

Workload:

Baseline failure:

Decision: prompt / examples / RAG / model swap / SFT / LoRA / QLoRA / DPO / continued pretraining / distillation / no training

Data boundary:

Held-out evaluation:

Rejected alternatives:

Deployment impact:

Rollback:

## Deployment Decision Memo

Use [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]] before filling this out.

Workload:

Decision: local CPU / local GPU / self-hosted server / hosted API / hybrid / batch

Evidence:

Quality:

Latency:

Memory/cost:

Privacy:

Operational risk:

Rejected alternatives:

Next run:

## What Does Not Count

- Reading without recall.
- A training-stage explanation without data, objective, evaluation, and failure-owner evidence.
- A training-loop claim without shifted targets, causal mask evidence, train/validation loss, and generated samples.
- A local run that records model size but not artifact, tokenizer, chat template, runtime, route compatibility, and API contract.
- A local model download without model card, license, revision/tag/digest, and local path evidence.
- A long-context, RAG, tool, or multi-turn run without a counted context budget and output reserve.
- A tool-using run where the model-selected action executes without schema validation, policy check, bounded loop control, and failure rows.
- A benchmark that changes temperature, filters, penalties, seeds, stops, or output caps without saying so.
- An endpoint without a benchmark.
- A benchmark without quality evidence.
- A RAG answer without citations.
- An LLM judge score without human calibration.
- A fine-tune decision without a baseline failure, held-out eval, and rollback plan.
- A deployment choice without a real workload.

## Completion Audit

- [ ] Every gate in the evidence ledger has a proof link.
- [ ] The training pipeline map explains one capability from data through deployment.
- [ ] The tiny decoder training lab proves next-token loss, causal masking, validation loss, and generation.
- [ ] The self-assessment exam is passed or every failed section has a remediation plan.
- [ ] The benchmark and quality-harness decisions agree, or the disagreement is explained.
- [ ] The local model artifact has an acquisition/provenance card.
- [ ] The local model endpoint has a runtime compatibility evidence card.
- [ ] Any generic client integration has an OpenAI-compatible API contract card.
- [ ] Sampler settings are frozen or intentionally varied with a decoding-controls note.
- [ ] Any long-context, RAG, tool, or multi-turn run has a context-budget row.
- [ ] Any tool-using run has schema validation, policy decision, execution result, and bounded-loop proof.
- [ ] The adaptation memo either justifies no training or proves the selected adaptation method against held-out evidence.
- [ ] Any local inference failure has a diagnostic row that names the failed layer and controlled next change.
- [ ] The RAG assistant includes a manifest, chunk records, retrieval evidence, cited answer, unsupported-question refusal, and at least one diagnosed failure mode.
- [ ] The deployment memo chooses one path and rejects at least one alternative.
- [ ] The vault audit was regenerated after the capstone artifact was added.
- [ ] Any unresolved gaps are explicit in the status column.

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/LLM Mastery Roadmap]]
- [[LLM/Study/LLM Mastery Self-Assessment Exam]]
- [[LLM/Study/LLM Training Pipeline Map]]
- [[LLM/Study/Tiny Decoder-Only Transformer Training Lab]]
- [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/Study/LLM Study Index]]
- [[LLM/Study/LLM Paper Reading Protocol]]
- [[LLM/Study/Attention Implementation Lab]]
- [[LLM/Study/Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Decoding and Sampling Controls Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local RAG Assistant Lab]]
- [[LLM/Study/Local RAG Minimal Python Harness]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/Study/LLM Architecture Cheatsheet]]
