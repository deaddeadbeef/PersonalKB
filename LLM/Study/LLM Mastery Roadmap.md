---
tags: [study, llm, roadmap, mastery]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [intuition, core, deep-dive, practice]
---

# LLM Mastery Roadmap

> **One-line summary** Mastery means you can explain the field, read the core papers, implement the core mechanisms, evaluate model behavior, and operate a local model with measured trade-offs.

## How to Use This Roadmap

Use this note as the operational definition of "I know LLMs" for this vault. Reading is necessary, but it is not enough. Each level has a knowledge gate, a build gate, and an evaluation gate. Use [[LLM/Study/LLM Mastery Dashboard|LLM Mastery Dashboard]] as the daily home base, and use [[LLM/Study/LLM Mastery Study Cadence|LLM Mastery Study Cadence]] when you need the weekly operating rhythm for turning these gates into recall answers and capstone artifacts.

Move in order:

1. Open [[LLM/Study/LLM Mastery Dashboard|LLM Mastery Dashboard]] and choose today's recall prompt, study route, proof artifact, and evidence destination.
2. Use [[LLM/Study/LLM Daily Mastery Session Run Sheet|LLM Daily Mastery Session Run Sheet]] when you need one saved session artifact tying recall, mechanism, applied proof, and capstone route together.
3. Map the field chronologically with [[LLM/LLM — Learning Path|LLM Learning Path]].
4. Use [[LLM/Study/LLM Architecture Cheatsheet|LLM Architecture Cheatsheet]], [[LLM/Study/LLM Concept Dependency Map|LLM Concept Dependency Map]], [[LLM/Study/LLM Math and Tensor Shape Primer|LLM Math and Tensor Shape Primer]], [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide|LLM Metrics and Evaluation Interpretation Guide]], [[LLM/Study/Local LLM Inference Metrics Field Guide|Local LLM Inference Metrics Field Guide]], [[LLM/Study/LLM Paper Reading Protocol|LLM Paper Reading Protocol]], [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map|LLM 20-Paper Fast Path Synthesis Map]], [[LLM/Study/LLM Paper Claim Ledger|LLM Paper Claim Ledger]], [[LLM/Study/LLM Paper Claim Audit Runner|LLM Paper Claim Audit Runner]], [[LLM/Study/LLM Paper Oral Defense Runner|LLM Paper Oral Defense Runner]], [[LLM/Study/LLM Paper-to-Local Proof Router|LLM Paper-to-Local Proof Router]], [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner|LLM Academic-to-Local Defense Matrix Runner]], [[LLM/Study/LLM Mechanism-to-Inference Bridge Map|LLM Mechanism-to-Inference Bridge Map]], and [[LLM/Study/Local LLM End-to-End Mental Model|Local LLM End-to-End Mental Model]] while reading architecture notes and papers.
5. Use the review drills in [[LLM/Study/LLM Study Index|LLM Study Index]] and the mixed [[LLM/Study/LLM Active Recall Question Bank|LLM Active Recall Question Bank]] for active recall, then use [[LLM/Study/LLM Recall and Remediation Audit Runner|LLM Recall and Remediation Audit Runner]] when scored rows need coverage, remediation, and next-review proof.
6. Use [[LLM/Study/LLM Training Pipeline Map|LLM Training Pipeline Map]] to connect raw data, objectives, pretraining, post-training, adaptation, evaluation, and deployment.
7. Use [[LLM/Study/Tiny Decoder-Only Transformer Training Lab|Tiny Decoder-Only Transformer Training Lab]] to connect attention, next-token loss, gradients, validation, and generation in a toy model.
8. Use [[LLM/Study/Local LLM First Run Readiness Snapshot|Local LLM First Run Readiness Snapshot]], [[LLM/Study/Local LLM Model Store Readiness Snapshot|Local LLM Model Store Readiness Snapshot]], [[LLM/Study/Local LLM Windows Runtime Install Gate|Local LLM Windows Runtime Install Gate]], [[LLM/Study/Local LLM First Model Pull Gate|Local LLM First Model Pull Gate]], [[LLM/Study/Local LLM First Model Pull Runner|Local LLM First Model Pull Runner]], [[LLM/Study/Local LLM First Runtime Health Snapshot|Local LLM First Runtime Health Snapshot]], [[LLM/Study/Local LLM First Runtime Health Runner|Local LLM First Runtime Health Runner]], [[LLM/Study/Local LLM First Smoke Request Runner|Local LLM First Smoke Request Runner]], [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]], [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner|Local LLM First Endpoint Evidence Audit Runner]], [[LLM/Study/Local LLM First Response Debrief Card|Local LLM First Response Debrief Card]], [[LLM/Study/Local LLM First Quality Probe Suite|Local LLM First Quality Probe Suite]], [[LLM/Study/Local LLM First Quality Probe Runner|Local LLM First Quality Probe Runner]], [[LLM/Study/Local LLM Windows First-Run Quickstart|Local LLM Windows First-Run Quickstart]], [[LLM/Study/Local LLM Command Cookbook|Local LLM Command Cookbook]], [[LLM/Study/Local LLM First Inference Evidence Pack|Local LLM First Inference Evidence Pack]], and [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]] to prove local inference competence.

Use [[LLM/Study/Local LLM Hands-On Practicum Sequence|Local LLM Hands-On Practicum Sequence]] as the execution order for the applied local-inference proof. It tells you which artifact to leave behind at each stage instead of treating the labs as disconnected reference pages.

9. Use [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]] to prove the machine, runtime boundary, disk, and port before blaming the model.
10. Use [[LLM/Study/Local LLM End-to-End Mental Model|Local LLM End-to-End Mental Model]] to explain the whole path from model artifact and tokenizer through runtime, prefill, decode, route, client, evaluation, and operations before treating command success as mastery.
11. Use [[LLM/Study/Local LLM Inference Metrics Field Guide|Local LLM Inference Metrics Field Guide]] to interpret TTFT, TPOT, throughput, memory, queue, concurrency, and quality numbers before tuning the serving stack; then use [[LLM/Study/Local LLM Benchmark Evidence Audit Runner|Local LLM Benchmark Evidence Audit Runner]] before those numbers support comparison, synthesis, or deployment.
12. Use [[LLM/Study/Local LLM Runtime Stack Anatomy|Local LLM Runtime Stack Anatomy]] to map the stack from hardware and model bytes through runtime, API route, client/UI, workload, and operations evidence before debugging.
13. Use [[LLM/Study/Local LLM Workload to Model Selection Playbook|Local LLM Workload to Model Selection Playbook]] to define the workload, candidate slots, rejection triggers, and proof ladder before picking a model name.
14. Use [[LLM/Study/Local LLM Hardware Sizing Runner|Local LLM Hardware Sizing Runner]] when weight memory, KV-cache, runtime overhead, active sequences, context, and headroom must become repeatable pass/hold/fail fit evidence; then use [[LLM/Study/Local LLM Model Selection Runner|Local LLM Model Selection Runner]] when the workload, hardware, candidate, memory, compatibility, benchmark, and quality facts should become a repeatable shortlist before download or deployment.
15. Use [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]] to prove model card, license, gated access, exact artifact, revision, local path, and unsafe-file risk before serving.
16. Use [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Local LLM Artifact Download Cache and Conversion Lab]] to prove the exact downloaded bytes, cache/local path, file list, hash or verification, GGUF/Ollama import, conversion provenance, and cleanup plan.
17. Use [[LLM/Study/Local LLM Artifact Custody Audit Runner|Local LLM Artifact Custody Audit Runner]] before compatibility, serving, benchmark, or deployment evidence depends on those local bytes.
18. Use [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]] to prove the exact artifact, quantization, tokenizer, chat template, runtime, route, and workload contract fit together, then use [[LLM/Study/Local LLM Runtime Compatibility Runner|Local LLM Runtime Compatibility Runner]] when that compatibility decision must become repeatable pass/hold/fail evidence before model pull, runtime health, smoke testing, benchmark, or deployment. Use [[LLM/Study/Chat Template and Tokenizer Compatibility Runner|Chat Template and Tokenizer Compatibility Runner]] when template/tokenizer evidence must be repeatable before quality, benchmark, or deployment decisions. If the path is vLLM or SGLang from Windows, use [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab|Local LLM WSL CUDA vLLM and SGLang Setup Lab]] before comparing serving performance. If the path is containerized vLLM/SGLang or Open WebUI, use [[LLM/Study/Local LLM Docker GPU Container Serving Lab|Local LLM Docker GPU Container Serving Lab]] before treating Docker or Compose as the service contract.
19. Use [[LLM/Study/Local LLM Quantization and GPU Offload Lab|Local LLM Quantization and GPU Offload Lab]] to choose GGUF/AWQ/GPTQ/FP8/INT8, GPU offload, CPU fallback, and KV-cache precision from measured memory, speed, and quality evidence, then use [[LLM/Study/Local LLM Quantization and GPU Offload Evidence Runner|Local LLM Quantization and GPU Offload Evidence Runner]] before result synthesis depends on that setting.
20. Use [[LLM/Study/Local LLM Runtime Comparison Lab|Local LLM Runtime Comparison Lab]] when more than one runtime is plausible and the choice needs controlled benchmark, quality, and compatibility evidence.
21. Use [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] to prove the base URL, route, model id, streaming behavior, errors, and feature gaps before client integration, then use [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner|Local LLM OpenAI-Compatible API Contract Runner]] to save repeatable `/v1/models`, chat, stream, wrong-model failure, and JSONL handoff evidence.
22. Use [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] to make local endpoint calls reproducible, then use [[LLM/Study/Local LLM Application Integration Evidence Runner|Local LLM Application Integration Evidence Runner]] before treating an app, CLI, UI, job, RAG assistant, or tool loop as real integration evidence.
23. Use [[LLM/Study/Decoding and Sampling Controls Lab|Decoding and Sampling Controls Lab]] to freeze and tune sampler settings before comparing quality or speed, then use [[LLM/Study/Decoding and Sampling Controls Runner|Decoding and Sampling Controls Runner]] to save baseline, temperature, seed, stop-string, output-cap, CSV, Markdown, and JSONL evidence.
24. Use [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Lab|Local LLM Reasoning Budget and Test-Time Compute Lab]] when a local model exposes thinking mode, reasoning effort, reasoning parsers, or trace visibility controls, then use [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Runner|Local LLM Reasoning Budget and Test-Time Compute Runner]] when the saved effort sweep needs auditable parser, latency, quality, trace-policy, and decision proof.
25. Use [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]] to prove prompt, history, RAG, tool, output, and margin tokens fit, then use [[LLM/Study/Local LLM Context Window and Token Budgeting Runner|Local LLM Context Window and Token Budgeting Runner]] to save manifest, component-token, reserve, margin, drop-plan, and JSONL evidence.
26. Use [[LLM/Study/Local LLM Serving Internals and Scheduler Lab|Local LLM Serving Internals and Scheduler Lab]] to explain serving symptoms through prefill, decode, KV cache, PagedAttention, continuous batching, chunked prefill, slots, preemption, queueing, and admission control, then use [[LLM/Study/Local LLM Scheduler Evidence Audit Runner|Local LLM Scheduler Evidence Audit Runner]] to audit the saved scheduler evidence before changing concurrency, queue, cache, or deployment policy.
27. Use [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab|Local LLM Concurrency and Batch Throughput Lab]] when the setup must handle more than one active request, a local queue, or batch/offline throughput, then use [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner|Local LLM Concurrency and Batch Throughput Runner]] when that claim needs JSON, CSV, Markdown, and JSONL evidence.
28. Use [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab|Local LLM Prompt Cache and KV Reuse Lab]] before claiming repeated-prefix speedups, then use [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner|Local LLM Prompt Cache and KV Reuse Runner]] when the result needs shared-prefix, changed-prefix, TTFT, metrics, CSV, Markdown, and JSONL evidence.
29. Use [[LLM/Study/Local LLM Speculative Decoding Lab|Local LLM Speculative Decoding Lab]] before enabling draft-model, EAGLE, MTP, n-gram, or another speculative decoding path for local generation speed, then use [[LLM/Study/Local LLM Speculative Decoding Runner|Local LLM Speculative Decoding Runner]] when the result needs no-spec/spec profile, TTFT, decode-rate, accepted-token signal, quality, CSV, Markdown, and JSONL evidence.
30. Use [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]] to capture model state, request timings, logs, runtime metrics, resource pressure, and next controlled action, then use [[LLM/Study/Local LLM Observability and Operations Runner|Local LLM Observability and Operations Runner]] when the service-state claim needs repeatable JSON, CSV, Markdown, and JSONL evidence.
31. Use [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook|Local LLM Service Lifecycle and Upgrade Runbook]] when a working endpoint must survive restarts, upgrades, cache movement, UI updates, and rollback, then use [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner|Local LLM Service Lifecycle and Upgrade Runner]] when the change needs a validated before/after/rollback evidence package.
32. Use [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] before any non-loopback use, then use [[LLM/Study/Local LLM Security and Privacy Runner|Local LLM Security and Privacy Runner]] when endpoint exposure, config/log secrets, RAG/tool/UI storage, export boundary, and model-list evidence need repeatable JSON, CSV, Markdown, and JSONL proof.
33. Save benchmark evidence in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]].
34. Use [[LLM/Study/Local LLM First Quality Probe Suite|Local LLM First Quality Probe Suite]] or [[LLM/Study/Local LLM First Quality Probe Runner|Local LLM First Quality Probe Runner]] for the first private quality signal after smoke output, then use [[LLM/Study/Local LLM Evaluation Set Design Runner|Local LLM Evaluation Set Design Runner]] before the full prompt suite supports repeated model, runtime, RAG, tool, or deployment decisions. Use [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] only after the suite has workload, held-out/private, contamination, rubric, and pass-criteria proof, then use [[LLM/Study/Local LLM Quality Evaluation Runner|Local LLM Quality Evaluation Runner]] when the scored prompt-suite rows should become machine-checkable quality evidence. Use [[LLM/Study/Local LLM Judge Calibration Runner|Local LLM Judge Calibration Runner]] before any LLM-as-judge row supports repeated model, runtime, RAG, tool, or deployment decisions.
35. Use [[LLM/Study/Local Embedding and Reranker Hosting Lab|Local Embedding and Reranker Hosting Lab]] before judging a RAG assistant whose retrieval quality depends on local embedding or reranker inference.
36. Use [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide|LLM Adaptation and Fine-Tuning Decision Guide]] when quality gaps require prompting, RAG, SFT, LoRA, QLoRA, DPO, distillation, or a no-train decision, then use [[LLM/Study/LLM Adaptation and Fine-Tuning Readiness Runner|LLM Adaptation and Fine-Tuning Readiness Runner]] before training, adapter serving, result synthesis, or capstone evidence depends on that decision.
37. Use [[LLM/Study/Local LLM Result Synthesis Runner|Local LLM Result Synthesis Runner]] to reconcile endpoint, benchmark, eval-set, quality, security, operations, and rejected-alternative evidence into keep, tune, reject, rerun, or deployment-memo readiness; then use [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]] to choose local CPU/GPU, self-hosted, hosted API, hybrid, or batch inference from evidence.
38. Use [[LLM/Study/LLM Deployment Readiness Audit Runner|LLM Deployment Readiness Audit Runner]] to check whether the workload, selected path, model/runtime, artifact custody, endpoint, application integration, benchmark, quality, privacy, operations, cost, rejected alternative, and retest proof are ready before accepting the deployment memo.
39. Use [[LLM/Study/Local LLM Capstone Project Blueprint|Local LLM Capstone Project Blueprint]] to turn the academic and applied proof path into one buildable local assistant project.
40. Use [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]] to collect proof across the paper, implementation, local inference, RAG, evaluation, adaptation, and deployment gates.
41. Use [[LLM/Study/LLM Paper Oral Defense Runner|LLM Paper Oral Defense Runner]], [[LLM/Study/LLM Mastery Self-Assessment Exam|LLM Mastery Self-Assessment Exam]], and [[LLM/Study/LLM Mastery Exam Run Sheet|LLM Mastery Exam Run Sheet]] to test whether the academic and applied knowledge is available without hand-holding, score the attempt, link proof, route misses, and validate the scored rows with [[LLM/Study/LLM Recall and Remediation Audit Runner|LLM Recall and Remediation Audit Runner]].
42. Use [[LLM/Study/LLM Mastery Evidence Audit Runner|LLM Mastery Evidence Audit Runner]] to check whether the academic, mechanism, local-inference, system, and exam proof bundle has critical gaps before final defense, then use [[LLM/Study/LLM Mastery Gap Triage Runner|LLM Mastery Gap Triage Runner]] when the output has multiple hold/fail gates and you need one top next action.
43. Build the capstone only after the local inference and evaluation gates are complete.

## Level 1: Field Map

**Goal:** Explain what changed from n-gram language models to transformer-based assistants.

Read:

- [[LLM/Pre-2017 — Before Transformers/Language Model Fundamentals|Language Model Fundamentals]]
- [[LLM/Pre-2017 — Before Transformers/Tokenization|Tokenization]]
- [[LLM/Study/LLM Math and Tensor Shape Primer|LLM Math and Tensor Shape Primer]]
- [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide|LLM Metrics and Evaluation Interpretation Guide]]
- [[LLM/2017 — The Transformer/Attention Mechanism|Attention Mechanism]]
- [[LLM/2017 — The Transformer/Transformer Architecture|Transformer Architecture]]
- [[LLM/Study/Attention Implementation Lab|Attention Implementation Lab]]
- [[LLM/2018–2019 — Pretrained Language Models/GPT and Decoder-Only Lineage|GPT and Decoder-Only Lineage]]

Proof:

- Draw the pipeline from text to tokens to embeddings to hidden states to logits to probabilities to next-token sampling.
- Prove that pipeline with [[LLM/Study/LLM Inference Request Lifecycle Lab|LLM Inference Request Lifecycle Lab]] by freezing one local request and tracing tokenization, prefill, decode, sampling, stopping, and returned text. When request/response files exist, use [[LLM/Study/LLM Inference Request Lifecycle Runner|LLM Inference Request Lifecycle Runner]] to convert the trace into phase rows and findings.
- Verify tokenizer and chat-template compatibility with [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat Template and Tokenizer Compatibility Lab]] before blaming the model for instruction-following failures.
- Implement scaled dot-product attention with [[LLM/Study/Attention Implementation Lab|Attention Implementation Lab]] and explain the tensor shapes.
- Explain why decoder-only transformers became the dominant general assistant architecture.
- Define perplexity, tokenization, context window, embedding, attention head, and pretraining.

## Level 2: Architecture and Training

**Goal:** Understand the mechanisms that make modern LLMs trainable and scalable.

Read:

- [[LLM/2020–2021 — The Scaling Era/Scaling Laws|Scaling Laws]]
- [[LLM/Study/LLM Math and Tensor Shape Primer|LLM Math and Tensor Shape Primer]]
- [[LLM/Study/LLM Training Pipeline Map|LLM Training Pipeline Map]]
- [[LLM/Study/Tiny Decoder-Only Transformer Training Lab|Tiny Decoder-Only Transformer Training Lab]]
- [[LLM/2020–2021 — The Scaling Era/Training Infrastructure and Parallelism|Training Infrastructure and Parallelism]]
- [[LLM/2020–2021 — The Scaling Era/Mixture-of-Experts Models|Mixture-of-Experts Models]]
- [[LLM/2020–2021 — The Scaling Era/LoRA and QLoRA|LoRA and QLoRA]]
- [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide|LLM Adaptation and Fine-Tuning Decision Guide]]
- [[LLM/2022 — Alignment and Chat/Compute Data and Parameter Trade-offs|Compute Data and Parameter Trade-offs]]

Proof:

- Reproduce the main scaling-law intuition: model size, data, and compute are coupled.
- Trace data curation, tokenization, pretraining objective, distributed training, SFT, preference optimization, adaptation, and deployment with [[LLM/Study/LLM Training Pipeline Map|LLM Training Pipeline Map]].
- Train a tiny decoder-only model with [[LLM/Study/Tiny Decoder-Only Transformer Training Lab|Tiny Decoder-Only Transformer Training Lab]] and explain shifted targets, cross-entropy loss, train/validation loss, overfitting, and autoregressive generation.
- Explain why overtraining a smaller model can be rational when inference cost matters.
- Compare full fine-tuning, LoRA, QLoRA, distillation, and prompt-only adaptation.
- Use [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide|LLM Adaptation and Fine-Tuning Decision Guide]] to decide whether a measured failure should be fixed with prompting, RAG, SFT, LoRA, QLoRA, DPO, continued pretraining, distillation, or no training, then audit the decision with [[LLM/Study/LLM Adaptation and Fine-Tuning Readiness Runner|LLM Adaptation and Fine-Tuning Readiness Runner]].
- Explain data parallelism, tensor parallelism, pipeline parallelism, ZeRO/FSDP, and MoE routing at a high level.

## Level 3: Alignment, Prompting, and Evaluation

**Goal:** Understand how raw pretrained models become useful assistants and how their behavior is measured.

Read:

- [[LLM/2022 — Alignment and Chat/Instruction Tuning|Instruction Tuning]]
- [[LLM/2022 — Alignment and Chat/Reinforcement Learning from Human Feedback|Reinforcement Learning from Human Feedback]]
- [[LLM/2022 — Alignment and Chat/Direct Preference Optimization|Direct Preference Optimization]]
- [[LLM/2022 — Alignment and Chat/Chain-of-Thought Prompting|Chain-of-Thought Prompting]]
- [[LLM/2023 — Open Models and Agents/LLM-as-Judge|LLM-as-Judge]]
- [[LLM/2022 — Alignment and Chat/Red-Teaming and Safety Evaluations|Red-Teaming and Safety Evaluations]]

Proof:

- Trace the SFT -> reward model -> policy optimization alignment pipeline.
- Compare RLHF, DPO, and Constitutional AI as post-training stages in [[LLM/Study/LLM Training Pipeline Map|LLM Training Pipeline Map]].
- Contrast RLHF, DPO, Constitutional AI, and instruction tuning.
- Write an evaluation rubric, then compare human preference, benchmark score, and LLM-as-judge evaluation.
- Explain position bias, verbosity bias, contamination, and why static benchmarks saturate.

## Level 4: Retrieval, Tools, and Agents

**Goal:** Build systems around a model instead of treating the model as the whole product.

Read:

- [[LLM/2020–2021 — The Scaling Era/Retrieval Pipelines and Context Assembly|Retrieval Pipelines and Context Assembly]]
- [[LLM/2023 — Open Models and Agents/Embeddings and Vector Databases|Embeddings and Vector Databases]]
- [[LLM/2023 — Open Models and Agents/Chunking Strategies|Chunking Strategies]]
- [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes|RAG Evaluation and Failure Modes]]
- [[LLM/2023 — Open Models and Agents/Function Calling|Function Calling]]
- [[LLM/2023 — Open Models and Agents/Tool Selection and Execution Loops|Tool Selection and Execution Loops]]
- [[LLM/Study/Local RAG Assistant Lab|Local RAG Assistant Lab]]
- [[LLM/Study/Local Embedding and Reranker Hosting Lab|Local Embedding and Reranker Hosting Lab]]
- [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab|Local RAG Retrieval Evaluation and Reranking Lab]]
- [[LLM/Study/Local RAG Minimal Python Harness|Local RAG Minimal Python Harness]]
- [[LLM/Study/Local RAG Evidence Runner|Local RAG Evidence Runner]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Runner|Local LLM Tool Calling and Structured Output Runner]]

Proof:

- Build a small RAG pipeline with [[LLM/Study/Local RAG Assistant Lab|Local RAG Assistant Lab]], [[LLM/Study/Local Embedding and Reranker Hosting Lab|Local Embedding and Reranker Hosting Lab]], [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab|Local RAG Retrieval Evaluation and Reranking Lab]], [[LLM/Study/Local RAG Minimal Python Harness|Local RAG Minimal Python Harness]], and [[LLM/Study/Local RAG Evidence Runner|Local RAG Evidence Runner]]: corpus manifest, chunk, embedding/reranker service card, index, retrieve, evaluate top-k/rank/reranking, assemble, generate, cite, refuse unsupported claims, log failures, and save the evidence packet.
- Show one failure caused by retrieval miss, one by bad chunking, and one by generation hallucination.
- Build a simple tool-calling loop with [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]], then save repeatable evidence with [[LLM/Study/Local LLM Tool Calling and Structured Output Runner|Local LLM Tool Calling and Structured Output Runner]]: tool schema, structured output, validation, policy check, execution, result injection, bounded retry, and failure rows.
- Explain why context assembly and evaluation matter as much as the base model.

## Level 5: Inference and Local Hosting

**Goal:** Host a local model, call it through an API, and explain the performance bottlenecks.

Read:

- [[LLM/2022 — Alignment and Chat/Quantization|Quantization]]
- [[LLM/2023 — Open Models and Agents/Open-Weight Model Ecosystem|Open-Weight Model Ecosystem]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse|KV Cache and Context Reuse]]
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching|Batching and Continuous Batching]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs|Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/2024–2025 — Frontier and Efficiency/Speculative Decoding|Speculative Decoding]]
- [[LLM/2026 — Reasoning and Agents/Prompt Caching and Inference Infrastructure|Prompt Caching and Inference Infrastructure]]
- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map|LLM Mechanism-to-Inference Bridge Map]]
- [[LLM/Study/LLM Paper Claim Ledger|LLM Paper Claim Ledger]]
- [[LLM/Study/LLM Paper-to-Local Proof Router|LLM Paper-to-Local Proof Router]]
- [[LLM/Study/Local LLM End-to-End Mental Model|Local LLM End-to-End Mental Model]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide|Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/Local LLM Benchmark Evidence Audit Runner|Local LLM Benchmark Evidence Audit Runner]]
- [[LLM/Study/LLM Concept Dependency Map|LLM Concept Dependency Map]]
- [[LLM/Study/LLM Active Recall Question Bank|LLM Active Recall Question Bank]]
- [[LLM/Study/Local LLM First Run Readiness Snapshot|Local LLM First Run Readiness Snapshot]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM Windows First-Run Quickstart|Local LLM Windows First-Run Quickstart]]
- [[LLM/Study/Local LLM Command Cookbook|Local LLM Command Cookbook]]
- [[LLM/Study/Local LLM First Inference Evidence Pack|Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab|LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/LLM Inference Request Lifecycle Runner|LLM Inference Request Lifecycle Runner]]
- [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Local LLM Artifact Download Cache and Conversion Lab]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab|Local LLM WSL CUDA vLLM and SGLang Setup Lab]]
- [[LLM/Study/Local LLM Docker GPU Container Serving Lab|Local LLM Docker GPU Container Serving Lab]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Lab|Local LLM Quantization and GPU Offload Lab]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Evidence Runner|Local LLM Quantization and GPU Offload Evidence Runner]]
- [[LLM/Study/Local LLM Runtime Comparison Lab|Local LLM Runtime Comparison Lab]]
- [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner|Local LLM OpenAI-Compatible API Contract Runner]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Application Integration Evidence Runner|Local LLM Application Integration Evidence Runner]]
- [[LLM/Study/Decoding and Sampling Controls Lab|Decoding and Sampling Controls Lab]]
- [[LLM/Study/Decoding and Sampling Controls Runner|Decoding and Sampling Controls Runner]]
- [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Lab|Local LLM Reasoning Budget and Test-Time Compute Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Runner|Local LLM Context Window and Token Budgeting Runner]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab|Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM Scheduler Evidence Audit Runner|Local LLM Scheduler Evidence Audit Runner]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab|Local LLM Concurrency and Batch Throughput Lab]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner|Local LLM Concurrency and Batch Throughput Runner]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab|Local LLM Prompt Cache and KV Reuse Lab]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner|Local LLM Prompt Cache and KV Reuse Runner]]
- [[LLM/Study/Local LLM Speculative Decoding Runner|Local LLM Speculative Decoding Runner]]
- [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook|Local LLM Service Lifecycle and Upgrade Runbook]]
- [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Security and Privacy Runner|Local LLM Security and Privacy Runner]]
- [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]]
- [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]]
- [[LLM/Study/LLM Deployment Readiness Audit Runner|LLM Deployment Readiness Audit Runner]]

Proof:

- Run one local model through a CLI and one local HTTP API.
- If the first run is on Windows, use [[LLM/Study/Local LLM First Run Readiness Snapshot|Local LLM First Run Readiness Snapshot]] before installing anything, then use [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]], [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner|Local LLM First Endpoint Evidence Audit Runner]], [[LLM/Study/Local LLM First Response Debrief Card|Local LLM First Response Debrief Card]], [[LLM/Study/Local LLM First Quality Probe Suite|Local LLM First Quality Probe Suite]], and [[LLM/Study/Local LLM Windows First-Run Quickstart|Local LLM Windows First-Run Quickstart]] to capture preflight, model id, smoke response, listener boundary, endpoint evidence audit, and quality mini-suite before moving to broader serving work.
- Use [[LLM/Study/Local LLM Command Cookbook|Local LLM Command Cookbook]] when you need copyable startup, `/v1/models`, `/v1/chat/completions`, Python client, streaming, benchmark, and teardown commands for the chosen runtime.
- Use [[LLM/Study/Local LLM End-to-End Mental Model|Local LLM End-to-End Mental Model]] when you can execute a command but cannot yet explain the artifact, tokenizer, runtime, prefill, decode, route, client, evaluation, and operations chain.
- Use [[LLM/Study/Local LLM Inference Metrics Field Guide|Local LLM Inference Metrics Field Guide]] before acting on TTFT, TPOT, output tokens/sec, memory, queue, or quality numbers; use [[LLM/Study/Local LLM Benchmark Evidence Audit Runner|Local LLM Benchmark Evidence Audit Runner]] before turning saved benchmark rows into comparison, result-synthesis, or deployment evidence.
- Capture a machine/runtime preflight with [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]] before diagnosing quality or speed.
- Record acquisition provenance with [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]] before serving downloaded, gated, converted, or internal model artifacts.
- Prove the actual local artifact with [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Local LLM Artifact Download Cache and Conversion Lab]], then audit it with [[LLM/Study/Local LLM Artifact Custody Audit Runner|Local LLM Artifact Custody Audit Runner]] before treating a cache path, GGUF file, Ollama package, or converted derivative as the model under test.
- Use [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] to keep the endpoint loopback-only until exposure, authentication, logs, RAG data, and tools are understood. Use [[LLM/Study/Local LLM Security and Privacy Runner|Local LLM Security and Privacy Runner]] when the boundary needs repeatable exposure, model-list, config/log secret-scan, RAG/tool/UI/export, and pass/hold/error evidence.
- Confirm the local endpoint is using the intended tokenizer, chat template, special tokens, and stop policy.
- Use [[LLM/Study/Chat Template and Tokenizer Compatibility Runner|Chat Template and Tokenizer Compatibility Runner]] before treating role-marker leakage, ignored system prompts, malformed JSON/tool output, or prompt-continuation behavior as model-quality evidence.
- Estimate weight memory and KV-cache risk with [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]] before choosing the model/runtime pair.
- Fill a compatibility evidence card with [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]] before treating load errors or strange behavior as model-quality failures.
- If vLLM or SGLang runs under WSL from Windows, complete [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab|Local LLM WSL CUDA vLLM and SGLang Setup Lab]] before runtime comparison, scheduler tuning, or throughput claims.
- If vLLM, SGLang, or Open WebUI runs in Docker, complete [[LLM/Study/Local LLM Docker GPU Container Serving Lab|Local LLM Docker GPU Container Serving Lab]] before accepting Docker, Compose, or UI routing as production-style evidence.
- Use [[LLM/Study/Local LLM Quantization and GPU Offload Lab|Local LLM Quantization and GPU Offload Lab]] before accepting a lower-bit artifact, GPU-offload setting, CPU/GPU split, or KV-cache precision as the local baseline, then audit the rows with [[LLM/Study/Local LLM Quantization and GPU Offload Evidence Runner|Local LLM Quantization and GPU Offload Evidence Runner]].
- Compare at least two plausible runtimes with [[LLM/Study/Local LLM Runtime Comparison Lab|Local LLM Runtime Comparison Lab]] before claiming the runtime choice is understood.
- Use [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]] to prove the endpoint with a smoke test and diagnose any serving failures.
- Use [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] to prove whether generic OpenAI-compatible clients can rely on the local route, streaming path, error shape, and required feature set, then use [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner|Local LLM OpenAI-Compatible API Contract Runner]] to capture the repeatable contract evidence.
- Use [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]] to name the failed layer before changing model, runtime, prompt, or hardware. When the failure affects benchmark, quality, operations, or deployment evidence, use [[LLM/Study/Local LLM Failure Triage Runner|Local LLM Failure Triage Runner]] to save the symptom, proof, mechanism owner, ruled-out layers, and one controlled next action.
- Use [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] to log repeatable non-streaming, streaming, error, and benchmark rows from the same client.
- Use [[LLM/Study/Local LLM Application Integration Evidence Runner|Local LLM Application Integration Evidence Runner]] when the local client is wired into a real app boundary and needs app contract, user flow, response handling, failure behavior, privacy/logging, evaluation, operations, and promotion proof.
- Use [[LLM/Study/LLM Inference Request Lifecycle Runner|LLM Inference Request Lifecycle Runner]] when a saved local request/response pair needs client request, prompt assembly, tokenization, prefill, decode, stop, parse, and application-handling evidence before benchmark or capstone claims.
- Use [[LLM/Study/Decoding and Sampling Controls Lab|Decoding and Sampling Controls Lab]] to freeze temperature, candidate filters, penalties, seed behavior, stop rules, and output caps before benchmark or quality comparisons, then use [[LLM/Study/Decoding and Sampling Controls Runner|Decoding and Sampling Controls Runner]] when those controls need repeatable run evidence.
- Use [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Lab|Local LLM Reasoning Budget and Test-Time Compute Lab]] when a local model exposes thinking mode, reasoning effort, reasoning parsers, or trace visibility controls, then audit the saved effort sweep with [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Runner|Local LLM Reasoning Budget and Test-Time Compute Runner]] before quality, runtime, result-synthesis, or deployment decisions depend on reasoning mode.
- Use [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]] to prove the rendered prompt, retrieved context, tool schemas, history, output reserve, and safety margin fit the runtime context limit, then use [[LLM/Study/Local LLM Context Window and Token Budgeting Runner|Local LLM Context Window and Token Budgeting Runner]] when the budget needs repeatable run evidence.
- Use [[LLM/Study/Local LLM Serving Internals and Scheduler Lab|Local LLM Serving Internals and Scheduler Lab]] before tuning concurrency or throughput settings so scheduler, prefill, decode, KV-cache, preemption, and queue symptoms have a named owner; use [[LLM/Study/Local LLM Scheduler Evidence Audit Runner|Local LLM Scheduler Evidence Audit Runner]] when the scheduler decision needs pass/hold/fail proof links.
- Use [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab|Local LLM Concurrency and Batch Throughput Lab]] before claiming a setup can handle shared local use, batch/offline work, or multi-client traffic; use [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner|Local LLM Concurrency and Batch Throughput Runner]] when the result needs repeatable run artifacts.
- Use [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab|Local LLM Prompt Cache and KV Reuse Lab]] before claiming repeated system prompts, documents, examples, RAG context, tool protocols, or chat history reduce prefill or TTFT; use [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner|Local LLM Prompt Cache and KV Reuse Runner]] when the result needs repeatable run artifacts.
- Use [[LLM/Study/Local LLM Speculative Decoding Lab|Local LLM Speculative Decoding Lab]] before claiming draft decoding, EAGLE, MTP, or n-gram speculation improves local generation speed; use [[LLM/Study/Local LLM Speculative Decoding Runner|Local LLM Speculative Decoding Runner]] when the result needs repeatable run artifacts.
- Use [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]] before interpreting latency, throughput, memory, or error symptoms; use [[LLM/Study/Local LLM Observability and Operations Runner|Local LLM Observability and Operations Runner]] when the result needs repeatable route, loaded-model, metrics, slots, resource, log-tail, privacy, and next-action evidence.
- Use [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook|Local LLM Service Lifecycle and Upgrade Runbook]] before changing runtime version, model revision, cache path, startup mode, UI container, driver stack, or client contract for a maintained local setup; use [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner|Local LLM Service Lifecycle and Upgrade Runner]] when the freeze card, artifacts, backup, rollback route, and post-change validation need repeatable run evidence.
- Record model, runtime, quantization, hardware, context length, time to first token, tokens/sec, and peak memory in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]], then audit the row with [[LLM/Study/Local LLM Benchmark Evidence Audit Runner|Local LLM Benchmark Evidence Audit Runner]] before comparing or promoting it.
- Use [[LLM/Study/Local LLM First Quality Probe Suite|Local LLM First Quality Probe Suite]] or [[LLM/Study/Local LLM First Quality Probe Runner|Local LLM First Quality Probe Runner]] before the full harness when the first endpoint has no quality rows. Use [[LLM/Study/Local LLM Evaluation Set Design Runner|Local LLM Evaluation Set Design Runner]] before repeated quality decisions so the suite has workload fit, held-out/private coverage, contamination controls, rubric, and refresh proof. Then use [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] to score known-answer, schema, RAG/citation, long-context, multi-turn, and workload-specific prompts, and use [[LLM/Study/Local LLM Quality Evaluation Runner|Local LLM Quality Evaluation Runner]] to audit the saved prompt/response artifacts, rubric scores, boundary-specific proof, and pass/hold/fail status. If an LLM judge contributes to the decision, run [[LLM/Study/Local LLM Judge Calibration Runner|Local LLM Judge Calibration Runner]] before treating the score as evidence.
- Use [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]] when local inference depends on function calling, structured output, tools, or agent loops, then use [[LLM/Study/Local LLM Tool Calling and Structured Output Runner|Local LLM Tool Calling and Structured Output Runner]] when the result needs JSON, CSV, Markdown, and JSONL proof.
- Use [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide|LLM Adaptation and Fine-Tuning Decision Guide]] before fine-tuning a model to fix a local quality gap, then run [[LLM/Study/LLM Adaptation and Fine-Tuning Readiness Runner|LLM Adaptation and Fine-Tuning Readiness Runner]] before accepting training or no-training evidence.
- Use [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]] to convert benchmark, quality, security, cost, and ops evidence into a deployment choice, then use [[LLM/Study/LLM Deployment Readiness Audit Runner|LLM Deployment Readiness Audit Runner]] to check whether the proof bundle is ready.
- Explain why KV cache, quantization, batch size, and context length change latency and throughput.
- Compare at least two runtimes, such as Ollama versus LM Studio, Ollama versus llama.cpp, llama.cpp versus vLLM, or vLLM versus SGLang, with fixed prompts, sampler settings, context target, output cap, benchmark rows, concurrency evidence when relevant, and quality rows.

## Level 6: Frontier and Research Literacy

**Goal:** Read current LLM research without losing the stable conceptual map.

Read:

- [[LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants|Efficient Attention and Long-Context Variants]]
- [[LLM/2024–2025 — Frontier and Efficiency/State Space Models and Mamba|State Space Models and Mamba]]
- [[LLM/2026 — Reasoning and Agents/Reasoning Models and Test-Time Compute|Reasoning Models and Test-Time Compute]]
- [[LLM/2026 — Reasoning and Agents/DeepSeek R1 and Open Reasoning|DeepSeek R1 and Open Reasoning]]
- [[LLM/2026 — Reasoning and Agents/Reasoning Distillation|Reasoning Distillation]]
- [[LLM/2026 — Reasoning and Agents/Agentic Coding Systems|Agentic Coding Systems]]
- [[LLM/2026 — Reasoning and Agents/Model Context Protocol|Model Context Protocol]]
- [[LLM/Study/LLM Paper Reading Protocol|LLM Paper Reading Protocol]]

Proof:

- For a new paper, use [[LLM/Study/LLM Paper Reading Protocol|LLM Paper Reading Protocol]] to identify the problem, baseline, method, evaluation, claimed improvement, and deployment implication, use [[LLM/Study/LLM Paper Oral Defense Runner|LLM Paper Oral Defense Runner]] when the answer must be proven without notes, then use [[LLM/Study/LLM Paper-to-Local Proof Router|LLM Paper-to-Local Proof Router]] when the claim needs an actionable local proof route and [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner|LLM Academic-to-Local Defense Matrix Runner]] when the local artifact, metric, failure owner, and decision need to be defended together.
- Separate model-scale gains from data, inference-time compute, tool use, retrieval, and evaluation effects.
- Explain what would make the result fail to transfer to a local deployment.

## Capstone Sequence

Complete these in order:

1. **Paper and dependency map:** use [[LLM/Study/LLM Concept Dependency Map|LLM Concept Dependency Map]], [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map|LLM 20-Paper Fast Path Synthesis Map]], [[LLM/Study/LLM Paper Claim Ledger|LLM Paper Claim Ledger]], [[LLM/Study/LLM Paper Claim Audit Runner|LLM Paper Claim Audit Runner]], [[LLM/Study/LLM Paper Oral Defense Runner|LLM Paper Oral Defense Runner]], [[LLM/Study/LLM Paper-to-Local Proof Router|LLM Paper-to-Local Proof Router]], [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner|LLM Academic-to-Local Defense Matrix Runner]], [[LLM/Study/LLM Mechanism-to-Inference Bridge Map|LLM Mechanism-to-Inference Bridge Map]], [[LLM/Study/Local LLM End-to-End Mental Model|Local LLM End-to-End Mental Model]], and [[LLM/Study/Local LLM Inference Metrics Field Guide|Local LLM Inference Metrics Field Guide]] to explain the 20-paper fast path from [[LLM/Study/LLM Study Index|LLM Study Index]], defend claim/evidence/limitation rows, audit paper coverage and source proof, prove no-notes paper answers, route paper claims to local proof artifacts, validate paper-to-local defense rows, translate at least five mechanisms into local inference controls, narrate one local request from artifact to operations decision, and interpret one benchmark row; then use [[LLM/Study/LLM Paper Reading Protocol|LLM Paper Reading Protocol]] to remediate any paper you cannot explain.
2. **Training pipeline map:** use [[LLM/Study/LLM Training Pipeline Map|LLM Training Pipeline Map]] to trace one capability from data and objective through post-training, evaluation, adaptation, and deployment.
3. **Attention implementation:** complete [[LLM/Study/Attention Implementation Lab|Attention Implementation Lab]] and explain the tensor shapes.
4. **Tiny decoder training:** complete [[LLM/Study/Tiny Decoder-Only Transformer Training Lab|Tiny Decoder-Only Transformer Training Lab]] and explain next-token loss, causal masking, validation loss, and generation.
5. **Local inference report:** complete the Windows first-run chain with [[LLM/Study/Local LLM Model Store Readiness Snapshot|Local LLM Model Store Readiness Snapshot]], [[LLM/Study/Local LLM Hardware Sizing Runner|Local LLM Hardware Sizing Runner]], [[LLM/Study/Local LLM Windows Runtime Install Gate|Local LLM Windows Runtime Install Gate]], [[LLM/Study/Local LLM First Model Pull Gate|Local LLM First Model Pull Gate]], [[LLM/Study/Local LLM First Model Pull Runner|Local LLM First Model Pull Runner]], [[LLM/Study/Local LLM First Runtime Health Snapshot|Local LLM First Runtime Health Snapshot]], [[LLM/Study/Local LLM First Runtime Health Runner|Local LLM First Runtime Health Runner]], [[LLM/Study/Local LLM First Smoke Request Runner|Local LLM First Smoke Request Runner]], [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]], [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner|Local LLM First Endpoint Evidence Audit Runner]], and [[LLM/Study/Local LLM First Inference Evidence Pack|Local LLM First Inference Evidence Pack]], then use [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]] and [[LLM/Study/Local LLM Command Cookbook|Local LLM Command Cookbook]] for the copyable server, route, client, streaming, benchmark, and teardown commands, prove artifact custody with [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Local LLM Artifact Download Cache and Conversion Lab]] and [[LLM/Study/Local LLM Artifact Custody Audit Runner|Local LLM Artifact Custody Audit Runner]], fill compatibility cards from [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]] and audit them with [[LLM/Study/Local LLM Runtime Compatibility Runner|Local LLM Runtime Compatibility Runner]], prove API shape with [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] and [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner|Local LLM OpenAI-Compatible API Contract Runner]], prove WSL CUDA setup with [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab|Local LLM WSL CUDA vLLM and SGLang Setup Lab]] when using vLLM or SGLang from Windows, prove Docker GPU serving with [[LLM/Study/Local LLM Docker GPU Container Serving Lab|Local LLM Docker GPU Container Serving Lab]] when using containers or Open WebUI, choose the accepted quantization/offload/KV-cache setting with [[LLM/Study/Local LLM Quantization and GPU Offload Lab|Local LLM Quantization and GPU Offload Lab]], compare plausible runtimes with [[LLM/Study/Local LLM Runtime Comparison Lab|Local LLM Runtime Comparison Lab]], prove the context budget with [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]] and [[LLM/Study/Local LLM Context Window and Token Budgeting Runner|Local LLM Context Window and Token Budgeting Runner]], identify scheduler and KV-cache bottlenecks with [[LLM/Study/Local LLM Serving Internals and Scheduler Lab|Local LLM Serving Internals and Scheduler Lab]], audit scheduler evidence with [[LLM/Study/Local LLM Scheduler Evidence Audit Runner|Local LLM Scheduler Evidence Audit Runner]], test repeated-prefix reuse with [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab|Local LLM Prompt Cache and KV Reuse Lab]], capture operations evidence with [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]] and [[LLM/Study/Local LLM Observability and Operations Runner|Local LLM Observability and Operations Runner]], record lifecycle and rollback proof with [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook|Local LLM Service Lifecycle and Upgrade Runbook]] and [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner|Local LLM Service Lifecycle and Upgrade Runner]], save the benchmark table in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]], and shape the final application deliverable with [[LLM/Study/Local LLM Capstone Project Blueprint|Local LLM Capstone Project Blueprint]].
6. **RAG assistant:** build document ingestion, chunking, embedding, embedding/reranker service proof, retrieval evaluation, reranking, generation, citation output, unsupported-question refusal, failure logging, and saved evidence packet with [[LLM/Study/Local RAG Assistant Lab|Local RAG Assistant Lab]], [[LLM/Study/Local Embedding and Reranker Hosting Lab|Local Embedding and Reranker Hosting Lab]], [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab|Local RAG Retrieval Evaluation and Reranking Lab]], [[LLM/Study/Local RAG Minimal Python Harness|Local RAG Minimal Python Harness]], and [[LLM/Study/Local RAG Evidence Runner|Local RAG Evidence Runner]].
7. **Tool loop:** build a harmless local tool-calling loop with [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]] and [[LLM/Study/Local LLM Tool Calling and Structured Output Runner|Local LLM Tool Calling and Structured Output Runner]], including schema validation, policy checks, result injection, and one denied unsafe action.
8. **Evaluation harness:** audit the prompt suite with [[LLM/Study/Local LLM Evaluation Set Design Runner|Local LLM Evaluation Set Design Runner]], evaluate the RAG/tool assistant with [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]], then audit the saved quality rows with [[LLM/Study/Local LLM Quality Evaluation Runner|Local LLM Quality Evaluation Runner]], including at least one human rubric and one LLM-as-judge rubric; run [[LLM/Study/Local LLM Judge Calibration Runner|Local LLM Judge Calibration Runner]] before the judge score can support a keep/hold/reject decision.
9. **Self-assessment:** use [[LLM/Study/LLM Active Recall Question Bank|LLM Active Recall Question Bank]] for mixed retrieval practice, then pass [[LLM/Study/LLM Mastery Self-Assessment Exam|LLM Mastery Self-Assessment Exam]] with [[LLM/Study/LLM Mastery Exam Run Sheet|LLM Mastery Exam Run Sheet]], run [[LLM/Study/LLM Recall and Remediation Audit Runner|LLM Recall and Remediation Audit Runner]], run [[LLM/Study/LLM Mastery Evidence Audit Runner|LLM Mastery Evidence Audit Runner]], run [[LLM/Study/LLM Mastery Gap Triage Runner|LLM Mastery Gap Triage Runner]] if there is more than one hold/fail row, and link missed-question remediation.
10. **Adaptation decision:** use [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide|LLM Adaptation and Fine-Tuning Decision Guide]] and [[LLM/Study/LLM Adaptation and Fine-Tuning Readiness Runner|LLM Adaptation and Fine-Tuning Readiness Runner]] to decide whether the workload needs prompting, RAG, SFT, LoRA/QLoRA, DPO, distillation, continued pretraining, or no training, and to prove baseline failure, data split, privacy, eval, deployment, and rollback.
11. **Deployment decision:** use [[LLM/Study/Local LLM Result Synthesis Runner|Local LLM Result Synthesis Runner]] to reconcile local-run evidence into keep, tune, reject, rerun, or deployment-memo readiness; use [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]] to write a trade-off memo choosing hosted API, local CPU/GPU, self-hosted serving, hybrid, or batch inference for one real workload; then use [[LLM/Study/LLM Deployment Readiness Audit Runner|LLM Deployment Readiness Audit Runner]] to audit the proof bundle, including application integration evidence when relevant, before accepting the memo.

Track the proof links and pass signals in [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]] as each capstone step is completed. Use [[LLM/Study/Local LLM Capstone Project Blueprint|Local LLM Capstone Project Blueprint]] as the final project spec before writing the deployment memo, use [[LLM/Study/LLM Deployment Readiness Audit Runner|LLM Deployment Readiness Audit Runner]] before accepting that memo, then use [[LLM/Study/LLM Mastery Evidence Audit Runner|LLM Mastery Evidence Audit Runner]] to find any critical gaps before final defense.

## Completion Checklist

- [ ] I can explain the historical timeline without notes.
- [ ] I can explain token IDs, embeddings, hidden states, logits, probabilities, cross-entropy, attention shapes, and KV-cache arithmetic.
- [ ] I can derive the attention computation and name each tensor.
- [ ] I can train a tiny decoder-only language model and explain shifted targets, cross-entropy loss, validation loss, and generation.
- [ ] I can explain pretraining, SFT, RLHF, DPO, LoRA, QLoRA, RAG, function calling, and LLM-as-judge.
- [ ] I can trace one capability from corpus choice and training objective through post-training, evaluation, adaptation, and deployment.
- [ ] I can identify when a problem is a retrieval issue, prompt issue, model capability issue, or evaluation issue.
- [ ] I can translate a local inference symptom into the academic mechanism, local control, evidence artifact, and next decision.
- [ ] I can explain one local request from model artifact and tokenizer through runtime, prefill, decode, route, client, quality gate, and operations decision.
- [ ] I can interpret TTFT, TPOT, output tokens/sec, total latency, memory, queue, and quality numbers as request-phase evidence with confounders and next actions.
- [ ] I can build a local tool-calling loop with schema validation, policy checks, bounded retries, and tool-result evaluation.
- [ ] I can host a local model, call its API, tune decoding controls, and record latency/throughput/memory metrics.
- [ ] I can compute and audit weight memory, KV-cache memory, runtime overhead, context, active sequences, and headroom before pulling or serving a model.
- [ ] I can audit a first model pull from saved source, store, compatibility, pull, list, tags, show, digest, and next-route evidence before endpoint smoke.
- [ ] I can audit runtime health from listener, native API, model-list, running-model, OpenAI-compatible model-list, expected-model, boundary, missing-layer, and next-route evidence before the first prompt.
- [ ] I can bind the first smoke request to runtime-health JSON, save native and OpenAI-compatible request/response/output files, and debrief the first response before making quality claims.
- [ ] I can decide when local reasoning effort is worth the latency, token budget, parser, and trace-retention cost, and I can audit that decision with a reasoning-budget runner output.
- [ ] I can turn scored local prompt-suite rows into quality-evaluation runner output with saved prompt/response artifacts, rubric scores, boundary proof, and pass/hold/fail status.
- [ ] I can explain whether a local serving bottleneck belongs to queueing, prefill, decode, KV cache, slots, continuous batching, chunked prefill, preemption, or admission control.
- [ ] I can run a small concurrency ladder and identify the saturation point, queue policy, and backpressure decision for local serving.
- [ ] I can capture model state, request timing, runtime metrics/logs, resource pressure, and next controlled action for a local LLM server, including a repeatable no-generation observability runner output.
- [ ] I can pin, restart, upgrade, back up, roll back, and post-validate a maintained local LLM service without guessing, including a repeatable lifecycle runner output.
- [ ] I can budget a local request across template, prompt, history, RAG, tools, output reserve, and safety margin.
- [ ] I can prove whether a local endpoint is OpenAI-compatible enough for a given client and workload.
- [ ] I can audit model package, tokenizer, chat template, rendered prompt or non-exposure control, route behavior, stop boundary, and downstream benchmark/quality links before blaming model quality.
- [ ] I can turn a local inference failure into a machine-checkable triage row with symptom, failed layer, proof, mechanism owner, ruled-out layers, and one controlled next action.
- [ ] I can explain the security and privacy boundary of a local model server before exposing it beyond loopback.
- [ ] I can design a held-out/private, contamination-aware prompt suite before scoring model quality.
- [ ] I can run a local quality harness and explain pass/hold/fail decisions from rubric evidence.
- [ ] I can calibrate an LLM-as-judge result against human review, AB/BA order stability, position bias, verbosity bias, and linked proof before using it for repeated local decisions.
- [ ] I can justify a model/runtime/quantization choice for my hardware and workload, including source, license, artifact format, tokenizer, template, and API-route compatibility.
- [ ] I can audit runtime compatibility into pass/hold/fail evidence before model pull, runtime health, smoke testing, benchmark, or deployment.
- [ ] I can prove the Windows-to-WSL CUDA path for vLLM or SGLang before interpreting runtime, scheduler, or throughput results.
- [ ] I can prove the Docker GPU container path for vLLM, SGLang, Compose, and Open WebUI before treating a container as a local service.
- [ ] I can prove which local bytes were downloaded, cached, imported, converted, verified, served, and cleaned up or retained.
- [ ] I can compare two local runtimes with fixed prompts, sampler settings, context target, output cap, benchmark rows, quality rows, and a rejected alternative.
- [ ] I can synthesize local-run evidence into keep, tune, reject, rerun, or deployment-memo readiness without hand-waving.
- [ ] I can explain why loss, perplexity, benchmark, preference, calibration, quality, latency, and memory metrics prove different claims.
- [ ] I can read a new LLM paper and place it in the field map.
- [ ] I can reduce a paper to claim, evidence, limitation, mechanism, local implication, and follow-up proof.
- [ ] I can audit a paper claim set for fast-path coverage, source proof, local implications, and follow-up proof routes.
- [ ] I can answer core paper oral prompts without notes and tie each answer to mechanism, evidence, limitation, local implication, route, score, and remediation.
- [ ] I can defend a paper-to-local matrix row by naming the paper basis, mechanism, local prediction, artifact, metric, confounder, failure owner, and decision.
- [ ] I can build and evaluate a small LLM application end to end.
- [ ] I can defend one local LLM capstone project from paper claims through endpoint, client, RAG/tool extension, evaluation, security, operations, and deployment decision.
- [ ] I can audit whether a deployment decision is ready by checking workload, selected path, model/runtime, endpoint, benchmark, quality, privacy, operations, cost, rejected alternative, and retest proof.

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/LLM — Learning Path]]
- [[LLM/Study/LLM Study Index]]
- [[LLM/Study/LLM Mastery Study Cadence]]
- [[LLM/Study/LLM Daily Mastery Session Run Sheet]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Mastery Self-Assessment Exam]]
- [[LLM/Study/LLM Mastery Evidence Audit Runner]]
- [[LLM/Study/LLM Mastery Gap Triage Runner]]
- [[LLM/Study/LLM Deployment Readiness Audit Runner]]
- [[LLM/Study/LLM Architecture Cheatsheet]]
- [[LLM/Study/LLM Concept Dependency Map]]
- [[LLM/Study/LLM Active Recall Question Bank]]
- [[LLM/Study/LLM Mastery Exam Run Sheet]]
- [[LLM/Study/LLM Recall and Remediation Audit Runner]]
- [[LLM/Study/LLM Math and Tensor Shape Primer]]
- [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]]
- [[LLM/Study/Local LLM Evaluation Set Design Runner]]
- [[LLM/Study/Local LLM Judge Calibration Runner]]
- [[LLM/Study/Local LLM Result Synthesis Runner]]
- [[LLM/Study/LLM Paper Reading Protocol]]
- [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map]]
- [[LLM/Study/LLM Paper Claim Audit Runner]]
- [[LLM/Study/LLM Paper Oral Defense Runner]]
- [[LLM/Study/LLM Paper-to-Local Proof Router]]
- [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner]]
- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]]
- [[LLM/Study/LLM Training Pipeline Map]]
- [[LLM/Study/Attention Implementation Lab]]
- [[LLM/Study/Tiny Decoder-Only Transformer Training Lab]]
- [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide]]
- [[LLM/Study/LLM Adaptation and Fine-Tuning Readiness Runner]]
- [[LLM/Study/Local LLM First Run Readiness Snapshot]]
- [[LLM/Study/Local LLM Model Store Readiness Snapshot]]
- [[LLM/Study/Local LLM Windows Runtime Install Gate]]
- [[LLM/Study/Local LLM First Model Pull Gate]]
- [[LLM/Study/Local LLM First Model Pull Runner]]
- [[LLM/Study/Local LLM First Runtime Health Snapshot]]
- [[LLM/Study/Local LLM First Runtime Health Runner]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner]]
- [[LLM/Study/Local LLM First Response Debrief Card]]
- [[LLM/Study/Local LLM First Quality Probe Suite]]
- [[LLM/Study/Local LLM First Quality Probe Runner]]
- [[LLM/Study/Local LLM Windows First-Run Quickstart]]
- [[LLM/Study/Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM Hands-On Practicum Sequence]]
- [[LLM/Study/Local LLM Workload to Model Selection Playbook]]
- [[LLM/Study/Local LLM Model Selection Runner]]
- [[LLM/Study/Local LLM Runtime Stack Anatomy]]
- [[LLM/Study/Local LLM Hosting and Inference Lab]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/LLM Inference Request Lifecycle Runner]]
- [[LLM/Study/Local LLM Failure Triage Runner]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Runner]]
- [[LLM/Study/Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab]]
- [[LLM/Study/Local LLM Artifact Custody Audit Runner]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Hardware Sizing Runner]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM Runtime Compatibility Runner]]
- [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab]]
- [[LLM/Study/Local LLM Docker GPU Container Serving Lab]]
- [[LLM/Study/Local LLM Runtime Comparison Lab]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Lab]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Evidence Runner]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Application Integration Evidence Runner]]
- [[LLM/Study/Decoding and Sampling Controls Lab]]
- [[LLM/Study/Decoding and Sampling Controls Runner]]
- [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Lab]]
- [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Runner]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM Scheduler Evidence Audit Runner]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner]]
- [[LLM/Study/Local LLM Speculative Decoding Lab]]
- [[LLM/Study/Local LLM Speculative Decoding Runner]]
- [[LLM/Study/Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM Observability and Operations Runner]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runner]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Runner]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Quality Evaluation Runner]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/Study/LLM Deployment Readiness Audit Runner]]
- [[LLM/Study/Local RAG Assistant Lab]]
- [[LLM/Study/Local Embedding and Reranker Hosting Lab]]
- [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab]]
- [[LLM/Study/Local RAG Minimal Python Harness]]
- [[LLM/Study/Local RAG Evidence Runner]]
