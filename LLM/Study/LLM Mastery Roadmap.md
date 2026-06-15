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
4. Use [[LLM/Study/LLM Architecture Cheatsheet|LLM Architecture Cheatsheet]], [[LLM/Study/LLM Concept Dependency Map|LLM Concept Dependency Map]], [[LLM/Study/LLM Math and Tensor Shape Primer|LLM Math and Tensor Shape Primer]], [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide|LLM Metrics and Evaluation Interpretation Guide]], [[LLM/Study/LLM Paper Reading Protocol|LLM Paper Reading Protocol]], [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map|LLM 20-Paper Fast Path Synthesis Map]], [[LLM/Study/LLM Mechanism-to-Inference Bridge Map|LLM Mechanism-to-Inference Bridge Map]], and [[LLM/Study/Local LLM End-to-End Mental Model|Local LLM End-to-End Mental Model]] while reading architecture notes and papers.
5. Use the review drills in [[LLM/Study/LLM Study Index|LLM Study Index]] and the mixed [[LLM/Study/LLM Active Recall Question Bank|LLM Active Recall Question Bank]] for active recall.
6. Use [[LLM/Study/LLM Training Pipeline Map|LLM Training Pipeline Map]] to connect raw data, objectives, pretraining, post-training, adaptation, evaluation, and deployment.
7. Use [[LLM/Study/Tiny Decoder-Only Transformer Training Lab|Tiny Decoder-Only Transformer Training Lab]] to connect attention, next-token loss, gradients, validation, and generation in a toy model.
8. Use [[LLM/Study/Local LLM First Run Readiness Snapshot|Local LLM First Run Readiness Snapshot]], [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]], [[LLM/Study/Local LLM Windows First-Run Quickstart|Local LLM Windows First-Run Quickstart]], [[LLM/Study/Local LLM Command Cookbook|Local LLM Command Cookbook]], [[LLM/Study/Local LLM First Inference Evidence Pack|Local LLM First Inference Evidence Pack]], and [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]] to prove local inference competence.

Use [[LLM/Study/Local LLM Hands-On Practicum Sequence|Local LLM Hands-On Practicum Sequence]] as the execution order for the applied local-inference proof. It tells you which artifact to leave behind at each stage instead of treating the labs as disconnected reference pages.

9. Use [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]] to prove the machine, runtime boundary, disk, and port before blaming the model.
10. Use [[LLM/Study/Local LLM End-to-End Mental Model|Local LLM End-to-End Mental Model]] to explain the whole path from model artifact and tokenizer through runtime, prefill, decode, route, client, evaluation, and operations before treating command success as mastery.
11. Use [[LLM/Study/Local LLM Runtime Stack Anatomy|Local LLM Runtime Stack Anatomy]] to map the stack from hardware and model bytes through runtime, API route, client/UI, workload, and operations evidence before debugging.
12. Use [[LLM/Study/Local LLM Workload to Model Selection Playbook|Local LLM Workload to Model Selection Playbook]] to define the workload, candidate slots, rejection triggers, and proof ladder before picking a model name.
13. Use [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]] to prove model card, license, gated access, exact artifact, revision, local path, and unsafe-file risk before serving.
14. Use [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Local LLM Artifact Download Cache and Conversion Lab]] to prove the exact downloaded bytes, cache/local path, file list, hash or verification, GGUF/Ollama import, conversion provenance, and cleanup plan.
15. Use [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]] to prove the exact artifact, quantization, tokenizer, chat template, runtime, route, and workload contract fit together. If the path is vLLM or SGLang from Windows, use [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab|Local LLM WSL CUDA vLLM and SGLang Setup Lab]] before comparing serving performance. If the path is containerized vLLM/SGLang or Open WebUI, use [[LLM/Study/Local LLM Docker GPU Container Serving Lab|Local LLM Docker GPU Container Serving Lab]] before treating Docker or Compose as the service contract.
16. Use [[LLM/Study/Local LLM Quantization and GPU Offload Lab|Local LLM Quantization and GPU Offload Lab]] to choose GGUF/AWQ/GPTQ/FP8/INT8, GPU offload, CPU fallback, and KV-cache precision from measured memory, speed, and quality evidence.
17. Use [[LLM/Study/Local LLM Runtime Comparison Lab|Local LLM Runtime Comparison Lab]] when more than one runtime is plausible and the choice needs controlled benchmark, quality, and compatibility evidence.
18. Use [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] to prove the base URL, route, model id, streaming behavior, errors, and feature gaps before client integration.
19. Use [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] to make local endpoint calls reproducible.
20. Use [[LLM/Study/Decoding and Sampling Controls Lab|Decoding and Sampling Controls Lab]] to freeze and tune sampler settings before comparing quality or speed.
21. Use [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Lab|Local LLM Reasoning Budget and Test-Time Compute Lab]] when a local model exposes thinking mode, reasoning effort, reasoning parsers, or trace visibility controls.
22. Use [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]] to prove prompt, history, RAG, tool, output, and margin tokens fit.
23. Use [[LLM/Study/Local LLM Serving Internals and Scheduler Lab|Local LLM Serving Internals and Scheduler Lab]] to explain serving symptoms through prefill, decode, KV cache, PagedAttention, continuous batching, chunked prefill, slots, preemption, queueing, and admission control.
24. Use [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab|Local LLM Concurrency and Batch Throughput Lab]] when the setup must handle more than one active request, a local queue, or batch/offline throughput.
25. Use [[LLM/Study/Local LLM Speculative Decoding Lab|Local LLM Speculative Decoding Lab]] before enabling draft-model, EAGLE, MTP, n-gram, or another speculative decoding path for local generation speed.
26. Use [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]] to capture model state, request timings, logs, runtime metrics, resource pressure, and next controlled action.
27. Use [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook|Local LLM Service Lifecycle and Upgrade Runbook]] when a working endpoint must survive restarts, upgrades, cache movement, UI updates, and rollback.
28. Save benchmark evidence in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]].
29. Use [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] to decide whether local output quality is good enough for the workload.
30. Use [[LLM/Study/Local Embedding and Reranker Hosting Lab|Local Embedding and Reranker Hosting Lab]] before judging a RAG assistant whose retrieval quality depends on local embedding or reranker inference.
31. Use [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide|LLM Adaptation and Fine-Tuning Decision Guide]] when quality gaps require prompting, RAG, SFT, LoRA, QLoRA, DPO, distillation, or a no-train decision.
32. Use [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]] to choose local CPU/GPU, self-hosted, hosted API, hybrid, or batch inference from evidence.
33. Use [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]] to collect proof across the paper, implementation, local inference, RAG, evaluation, adaptation, and deployment gates.
34. Use [[LLM/Study/LLM Mastery Self-Assessment Exam|LLM Mastery Self-Assessment Exam]] and [[LLM/Study/LLM Mastery Exam Run Sheet|LLM Mastery Exam Run Sheet]] to test whether the academic and applied knowledge is available without hand-holding, score the attempt, link proof, and route misses.
35. Build the capstone only after the local inference and evaluation gates are complete.

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
- Prove that pipeline with [[LLM/Study/LLM Inference Request Lifecycle Lab|LLM Inference Request Lifecycle Lab]] by freezing one local request and tracing tokenization, prefill, decode, sampling, stopping, and returned text.
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
- Use [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide|LLM Adaptation and Fine-Tuning Decision Guide]] to decide whether a measured failure should be fixed with prompting, RAG, SFT, LoRA, QLoRA, DPO, continued pretraining, distillation, or no training.
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
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]]

Proof:

- Build a small RAG pipeline with [[LLM/Study/Local RAG Assistant Lab|Local RAG Assistant Lab]], [[LLM/Study/Local Embedding and Reranker Hosting Lab|Local Embedding and Reranker Hosting Lab]], [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab|Local RAG Retrieval Evaluation and Reranking Lab]], and [[LLM/Study/Local RAG Minimal Python Harness|Local RAG Minimal Python Harness]]: corpus manifest, chunk, embedding/reranker service card, index, retrieve, evaluate top-k/rank/reranking, assemble, generate, cite, refuse unsupported claims, and log failures.
- Show one failure caused by retrieval miss, one by bad chunking, and one by generation hallucination.
- Build a simple tool-calling loop with [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]]: tool schema, structured output, validation, policy check, execution, result injection, bounded retry, and failure rows.
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
- [[LLM/Study/Local LLM End-to-End Mental Model|Local LLM End-to-End Mental Model]]
- [[LLM/Study/LLM Concept Dependency Map|LLM Concept Dependency Map]]
- [[LLM/Study/LLM Active Recall Question Bank|LLM Active Recall Question Bank]]
- [[LLM/Study/Local LLM First Run Readiness Snapshot|Local LLM First Run Readiness Snapshot]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM Windows First-Run Quickstart|Local LLM Windows First-Run Quickstart]]
- [[LLM/Study/Local LLM Command Cookbook|Local LLM Command Cookbook]]
- [[LLM/Study/Local LLM First Inference Evidence Pack|Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Local LLM Artifact Download Cache and Conversion Lab]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab|Local LLM WSL CUDA vLLM and SGLang Setup Lab]]
- [[LLM/Study/Local LLM Docker GPU Container Serving Lab|Local LLM Docker GPU Container Serving Lab]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Lab|Local LLM Quantization and GPU Offload Lab]]
- [[LLM/Study/Local LLM Runtime Comparison Lab|Local LLM Runtime Comparison Lab]]
- [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]]
- [[LLM/Study/Decoding and Sampling Controls Lab|Decoding and Sampling Controls Lab]]
- [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Lab|Local LLM Reasoning Budget and Test-Time Compute Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab|Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab|Local LLM Concurrency and Batch Throughput Lab]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab|Local LLM Prompt Cache and KV Reuse Lab]]
- [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook|Local LLM Service Lifecycle and Upgrade Runbook]]
- [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]]
- [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]]

Proof:

- Run one local model through a CLI and one local HTTP API.
- If the first run is on Windows, use [[LLM/Study/Local LLM First Run Readiness Snapshot|Local LLM First Run Readiness Snapshot]] before installing anything, then use [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]] and [[LLM/Study/Local LLM Windows First-Run Quickstart|Local LLM Windows First-Run Quickstart]] to capture preflight, model id, smoke response, listener boundary, and quality mini-suite before moving to broader serving work.
- Use [[LLM/Study/Local LLM Command Cookbook|Local LLM Command Cookbook]] when you need copyable startup, `/v1/models`, `/v1/chat/completions`, Python client, streaming, benchmark, and teardown commands for the chosen runtime.
- Use [[LLM/Study/Local LLM End-to-End Mental Model|Local LLM End-to-End Mental Model]] when you can execute a command but cannot yet explain the artifact, tokenizer, runtime, prefill, decode, route, client, evaluation, and operations chain.
- Capture a machine/runtime preflight with [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]] before diagnosing quality or speed.
- Record acquisition provenance with [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]] before serving downloaded, gated, converted, or internal model artifacts.
- Prove the actual local artifact with [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Local LLM Artifact Download Cache and Conversion Lab]] before treating a cache path, GGUF file, Ollama package, or converted derivative as the model under test.
- Use [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] to keep the endpoint loopback-only until exposure, authentication, logs, RAG data, and tools are understood.
- Confirm the local endpoint is using the intended tokenizer, chat template, special tokens, and stop policy.
- Estimate weight memory and KV-cache risk with [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]] before choosing the model/runtime pair.
- Fill a compatibility evidence card with [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]] before treating load errors or strange behavior as model-quality failures.
- If vLLM or SGLang runs under WSL from Windows, complete [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab|Local LLM WSL CUDA vLLM and SGLang Setup Lab]] before runtime comparison, scheduler tuning, or throughput claims.
- If vLLM, SGLang, or Open WebUI runs in Docker, complete [[LLM/Study/Local LLM Docker GPU Container Serving Lab|Local LLM Docker GPU Container Serving Lab]] before accepting Docker, Compose, or UI routing as production-style evidence.
- Use [[LLM/Study/Local LLM Quantization and GPU Offload Lab|Local LLM Quantization and GPU Offload Lab]] before accepting a lower-bit artifact, GPU-offload setting, CPU/GPU split, or KV-cache precision as the local baseline.
- Compare at least two plausible runtimes with [[LLM/Study/Local LLM Runtime Comparison Lab|Local LLM Runtime Comparison Lab]] before claiming the runtime choice is understood.
- Use [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]] to prove the endpoint with a smoke test and diagnose any serving failures.
- Use [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] to prove whether generic OpenAI-compatible clients can rely on the local route, streaming path, error shape, and required feature set.
- Use [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]] to name the failed layer before changing model, runtime, prompt, or hardware.
- Use [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] to log repeatable non-streaming, streaming, error, and benchmark rows from the same client.
- Use [[LLM/Study/Decoding and Sampling Controls Lab|Decoding and Sampling Controls Lab]] to freeze temperature, candidate filters, penalties, seed behavior, stop rules, and output caps before benchmark or quality comparisons.
- Use [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Lab|Local LLM Reasoning Budget and Test-Time Compute Lab]] when a local model exposes thinking mode, reasoning effort, reasoning parsers, or trace visibility controls.
- Use [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]] to prove the rendered prompt, retrieved context, tool schemas, history, output reserve, and safety margin fit the runtime context limit.
- Use [[LLM/Study/Local LLM Serving Internals and Scheduler Lab|Local LLM Serving Internals and Scheduler Lab]] before tuning concurrency or throughput settings so scheduler, prefill, decode, KV-cache, preemption, and queue symptoms have a named owner.
- Use [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab|Local LLM Concurrency and Batch Throughput Lab]] before claiming a setup can handle shared local use, batch/offline work, or multi-client traffic.
- Use [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab|Local LLM Prompt Cache and KV Reuse Lab]] before claiming repeated system prompts, documents, examples, RAG context, tool protocols, or chat history reduce prefill or TTFT.
- Use [[LLM/Study/Local LLM Speculative Decoding Lab|Local LLM Speculative Decoding Lab]] before claiming draft decoding, EAGLE, MTP, or n-gram speculation improves local generation speed.
- Use [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]] before interpreting latency, throughput, memory, or error symptoms; capture model state, route, request timings, logs, metrics, resource pressure, and one next controlled action.
- Use [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook|Local LLM Service Lifecycle and Upgrade Runbook]] before changing runtime version, model revision, cache path, startup mode, UI container, driver stack, or client contract for a maintained local setup.
- Record model, runtime, quantization, hardware, context length, time to first token, tokens/sec, and peak memory in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]].
- Use [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] to score known-answer, schema, RAG/citation, long-context, multi-turn, and workload-specific prompts.
- Use [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]] when local inference depends on function calling, structured output, tools, or agent loops.
- Use [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide|LLM Adaptation and Fine-Tuning Decision Guide]] before fine-tuning a model to fix a local quality gap.
- Use [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]] to convert benchmark, quality, security, cost, and ops evidence into a deployment choice.
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

- For a new paper, use [[LLM/Study/LLM Paper Reading Protocol|LLM Paper Reading Protocol]] to identify the problem, baseline, method, evaluation, claimed improvement, and deployment implication.
- Separate model-scale gains from data, inference-time compute, tool use, retrieval, and evaluation effects.
- Explain what would make the result fail to transfer to a local deployment.

## Capstone Sequence

Complete these in order:

1. **Paper and dependency map:** use [[LLM/Study/LLM Concept Dependency Map|LLM Concept Dependency Map]], [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map|LLM 20-Paper Fast Path Synthesis Map]], [[LLM/Study/LLM Mechanism-to-Inference Bridge Map|LLM Mechanism-to-Inference Bridge Map]], and [[LLM/Study/Local LLM End-to-End Mental Model|Local LLM End-to-End Mental Model]] to explain the 20-paper fast path from [[LLM/Study/LLM Study Index|LLM Study Index]], translate at least five mechanisms into local inference controls, and narrate one local request from artifact to operations decision; then use [[LLM/Study/LLM Paper Reading Protocol|LLM Paper Reading Protocol]] to remediate any paper you cannot explain.
2. **Training pipeline map:** use [[LLM/Study/LLM Training Pipeline Map|LLM Training Pipeline Map]] to trace one capability from data and objective through post-training, evaluation, adaptation, and deployment.
3. **Attention implementation:** complete [[LLM/Study/Attention Implementation Lab|Attention Implementation Lab]] and explain the tensor shapes.
4. **Tiny decoder training:** complete [[LLM/Study/Tiny Decoder-Only Transformer Training Lab|Tiny Decoder-Only Transformer Training Lab]] and explain next-token loss, causal masking, validation loss, and generation.
5. **Local inference report:** complete [[LLM/Study/Local LLM First Inference Evidence Pack|Local LLM First Inference Evidence Pack]] and [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]], use [[LLM/Study/Local LLM Command Cookbook|Local LLM Command Cookbook]] for the copyable server, route, client, streaming, benchmark, and teardown commands, prove artifact custody with [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab|Local LLM Artifact Download Cache and Conversion Lab]], fill compatibility cards from [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]] and [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]], prove WSL CUDA setup with [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab|Local LLM WSL CUDA vLLM and SGLang Setup Lab]] when using vLLM or SGLang from Windows, prove Docker GPU serving with [[LLM/Study/Local LLM Docker GPU Container Serving Lab|Local LLM Docker GPU Container Serving Lab]] when using containers or Open WebUI, choose the accepted quantization/offload/KV-cache setting with [[LLM/Study/Local LLM Quantization and GPU Offload Lab|Local LLM Quantization and GPU Offload Lab]], compare plausible runtimes with [[LLM/Study/Local LLM Runtime Comparison Lab|Local LLM Runtime Comparison Lab]], prove the context budget with [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]], identify scheduler and KV-cache bottlenecks with [[LLM/Study/Local LLM Serving Internals and Scheduler Lab|Local LLM Serving Internals and Scheduler Lab]], test repeated-prefix reuse with [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab|Local LLM Prompt Cache and KV Reuse Lab]], capture operations evidence with [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]], record lifecycle and rollback proof with [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook|Local LLM Service Lifecycle and Upgrade Runbook]], and save the benchmark table in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]].
6. **RAG assistant:** build document ingestion, chunking, embedding, embedding/reranker service proof, retrieval evaluation, reranking, generation, citation output, unsupported-question refusal, and failure logging with [[LLM/Study/Local RAG Assistant Lab|Local RAG Assistant Lab]], [[LLM/Study/Local Embedding and Reranker Hosting Lab|Local Embedding and Reranker Hosting Lab]], [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab|Local RAG Retrieval Evaluation and Reranking Lab]], and [[LLM/Study/Local RAG Minimal Python Harness|Local RAG Minimal Python Harness]].
7. **Tool loop:** build a harmless local tool-calling loop with [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]], including schema validation, policy checks, result injection, and one denied unsafe action.
8. **Evaluation harness:** evaluate the RAG/tool assistant with [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]], including at least one human rubric and one LLM-as-judge rubric.
9. **Self-assessment:** use [[LLM/Study/LLM Active Recall Question Bank|LLM Active Recall Question Bank]] for mixed retrieval practice, then pass [[LLM/Study/LLM Mastery Self-Assessment Exam|LLM Mastery Self-Assessment Exam]] with [[LLM/Study/LLM Mastery Exam Run Sheet|LLM Mastery Exam Run Sheet]] and link missed-question remediation.
10. **Adaptation decision:** use [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide|LLM Adaptation and Fine-Tuning Decision Guide]] to decide whether the workload needs prompting, RAG, SFT, LoRA/QLoRA, DPO, distillation, continued pretraining, or no training.
11. **Deployment decision:** use [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]] to write a trade-off memo choosing hosted API, local CPU/GPU, self-hosted serving, hybrid, or batch inference for one real workload.

Track the proof links and pass signals in [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]] as each capstone step is completed.

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
- [ ] I can build a local tool-calling loop with schema validation, policy checks, bounded retries, and tool-result evaluation.
- [ ] I can host a local model, call its API, tune decoding controls, and record latency/throughput/memory metrics.
- [ ] I can decide when local reasoning effort is worth the latency, token budget, parser, and trace-retention cost.
- [ ] I can explain whether a local serving bottleneck belongs to queueing, prefill, decode, KV cache, slots, continuous batching, chunked prefill, preemption, or admission control.
- [ ] I can run a small concurrency ladder and identify the saturation point, queue policy, and backpressure decision for local serving.
- [ ] I can capture model state, request timing, runtime metrics/logs, resource pressure, and next controlled action for a local LLM server.
- [ ] I can pin, restart, upgrade, back up, roll back, and post-validate a maintained local LLM service without guessing.
- [ ] I can budget a local request across template, prompt, history, RAG, tools, output reserve, and safety margin.
- [ ] I can prove whether a local endpoint is OpenAI-compatible enough for a given client and workload.
- [ ] I can explain the security and privacy boundary of a local model server before exposing it beyond loopback.
- [ ] I can run a local quality harness and explain pass/hold/fail decisions from rubric evidence.
- [ ] I can justify a model/runtime/quantization choice for my hardware and workload, including source, license, artifact format, tokenizer, template, and API-route compatibility.
- [ ] I can prove the Windows-to-WSL CUDA path for vLLM or SGLang before interpreting runtime, scheduler, or throughput results.
- [ ] I can prove the Docker GPU container path for vLLM, SGLang, Compose, and Open WebUI before treating a container as a local service.
- [ ] I can prove which local bytes were downloaded, cached, imported, converted, verified, served, and cleaned up or retained.
- [ ] I can compare two local runtimes with fixed prompts, sampler settings, context target, output cap, benchmark rows, quality rows, and a rejected alternative.
- [ ] I can explain why loss, perplexity, benchmark, preference, calibration, quality, latency, and memory metrics prove different claims.
- [ ] I can read a new LLM paper and place it in the field map.
- [ ] I can build and evaluate a small LLM application end to end.

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/LLM — Learning Path]]
- [[LLM/Study/LLM Study Index]]
- [[LLM/Study/LLM Mastery Study Cadence]]
- [[LLM/Study/LLM Daily Mastery Session Run Sheet]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Mastery Self-Assessment Exam]]
- [[LLM/Study/LLM Architecture Cheatsheet]]
- [[LLM/Study/LLM Concept Dependency Map]]
- [[LLM/Study/LLM Active Recall Question Bank]]
- [[LLM/Study/LLM Mastery Exam Run Sheet]]
- [[LLM/Study/LLM Math and Tensor Shape Primer]]
- [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]]
- [[LLM/Study/LLM Paper Reading Protocol]]
- [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map]]
- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]]
- [[LLM/Study/LLM Training Pipeline Map]]
- [[LLM/Study/Attention Implementation Lab]]
- [[LLM/Study/Tiny Decoder-Only Transformer Training Lab]]
- [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide]]
- [[LLM/Study/Local LLM First Run Readiness Snapshot]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM Windows First-Run Quickstart]]
- [[LLM/Study/Local LLM First Inference Evidence Pack]]
- [[LLM/Study/Local LLM Hands-On Practicum Sequence]]
- [[LLM/Study/Local LLM Workload to Model Selection Playbook]]
- [[LLM/Study/Local LLM Runtime Stack Anatomy]]
- [[LLM/Study/Local LLM Hosting and Inference Lab]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Artifact Download Cache and Conversion Lab]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab]]
- [[LLM/Study/Local LLM Docker GPU Container Serving Lab]]
- [[LLM/Study/Local LLM Runtime Comparison Lab]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Decoding and Sampling Controls Lab]]
- [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab]]
- [[LLM/Study/Local LLM Speculative Decoding Lab]]
- [[LLM/Study/Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/Study/Local RAG Assistant Lab]]
- [[LLM/Study/Local Embedding and Reranker Hosting Lab]]
- [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab]]
- [[LLM/Study/Local RAG Minimal Python Harness]]
