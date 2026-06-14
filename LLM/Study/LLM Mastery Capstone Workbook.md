---
tags: [study, llm, capstone, mastery]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [practice]
---

# LLM Mastery Capstone Workbook

> **One-line summary** Mastery becomes credible only when the conceptual, implementation, local inference, RAG, evaluation, and deployment artifacts are linked in one evidence ledger.

Use this with [[LLM/Study/LLM Mastery Roadmap|LLM Mastery Roadmap]]. The roadmap defines the gates; this workbook collects the proof.

## How to Use

Copy the blank ledger into a dated capstone note, or fill the proof links directly here. A gate is complete only when the artifact exists, the evidence is linked, and the pass signal is explicit.

## Evidence Ledger

| Gate | Required artifact | Proof link/path | Pass signal | Status |
|---|---|---|---|---|
| Paper map | One-page map of the 20-paper fast path using [[LLM/Study/LLM Paper Reading Protocol|LLM Paper Reading Protocol]] |  | Can explain architecture, scaling, alignment, RAG, evaluation, and inference links without notes. | Not started |
| Self-assessment | Passed [[LLM/Study/LLM Mastery Self-Assessment Exam|LLM Mastery Self-Assessment Exam]] |  | Overall score is at least 80 percent, no zero in practical sections, and missed-question remediation is linked. | Not started |
| Attention implementation | Implementation output from [[LLM/Study/Attention Implementation Lab|Attention Implementation Lab]] |  | Code or notebook has tensor-shape checks, masking tests, and a plain-language explanation. | Not started |
| Local model endpoint | CLI and HTTP proof from [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]] and [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]] |  | Local endpoint returns a response; model id, runtime, command, and loopback URL are captured. | Not started |
| Benchmark record | Run entry in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] |  | Model, runtime, quantization, hardware, context length, TTFT, tokens/sec, memory, and quality decision are recorded. | Not started |
| Failure diagnosis | Diagnostic row from [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]] |  | At least one failure or explicit no-failure row names the layer, evidence, controlled change, and result. | Not started |
| Local quality gate | Prompt-suite result from [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] |  | Known-answer, schema, RAG/citation, long-context, multi-turn, and workload prompts have scored pass/hold/fail decisions where relevant. | Not started |
| RAG assistant | Local retrieval assistant from [[LLM/Study/Local RAG Assistant Lab|Local RAG Assistant Lab]] |  | Corpus version, chunking policy, index metadata, retrieval evidence, cited answer, and at least one diagnosed failure are captured. | Not started |
| Deployment decision | Deployment decision memo in this workbook |  | Choice between local CPU, local GPU, self-hosted server, or hosted API is justified with workload, quality, latency, memory/cost, privacy, and operational evidence. | Not started |

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

## Local Inference Proof Template

| Evidence item | Link or value |
|---|---|
| Hardware |  |
| Runtime |  |
| Model id |  |
| Quantization |  |
| Context length |  |
| CLI command |  |
| HTTP endpoint |  |
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

## Deployment Decision Memo

Workload:

Decision: local CPU / local GPU / self-hosted server / hosted API

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
- An endpoint without a benchmark.
- A benchmark without quality evidence.
- A RAG answer without citations.
- An LLM judge score without human calibration.
- A deployment choice without a real workload.

## Completion Audit

- [ ] Every gate in the evidence ledger has a proof link.
- [ ] The self-assessment exam is passed or every failed section has a remediation plan.
- [ ] The benchmark and quality-harness decisions agree, or the disagreement is explained.
- [ ] Any local inference failure has a diagnostic row that names the failed layer and controlled next change.
- [ ] The RAG assistant includes at least one diagnosed failure mode.
- [ ] The deployment memo chooses one path and rejects at least one alternative.
- [ ] The vault audit was regenerated after the capstone artifact was added.
- [ ] Any unresolved gaps are explicit in the status column.

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/LLM Mastery Roadmap]]
- [[LLM/Study/LLM Mastery Self-Assessment Exam]]
- [[LLM/Study/LLM Study Index]]
- [[LLM/Study/LLM Paper Reading Protocol]]
- [[LLM/Study/Attention Implementation Lab]]
- [[LLM/Study/Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local RAG Assistant Lab]]
- [[LLM/Study/LLM Architecture Cheatsheet]]
