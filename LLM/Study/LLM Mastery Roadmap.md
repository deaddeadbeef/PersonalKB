---
tags: [study, llm, roadmap, mastery]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [intuition, core, deep-dive, practice]
---

# LLM Mastery Roadmap

> **One-line summary** Mastery means you can explain the field, read the core papers, implement the core mechanisms, evaluate model behavior, and operate a local model with measured trade-offs.

## How to Use This Roadmap

Use this note as the operational definition of "I know LLMs" for this vault. Reading is necessary, but it is not enough. Each level has a knowledge gate, a build gate, and an evaluation gate.

Move in order:

1. Map the field chronologically with [[LLM/LLM — Learning Path|LLM Learning Path]].
2. Use [[LLM/Study/LLM Architecture Cheatsheet|LLM Architecture Cheatsheet]] and [[LLM/Study/LLM Paper Reading Protocol|LLM Paper Reading Protocol]] while reading architecture notes and papers.
3. Use the review drills in [[LLM/Study/LLM Study Index|LLM Study Index]] for active recall.
4. Use [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]] to prove local inference competence.
5. Use [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]] to prove the machine, runtime boundary, disk, and port before blaming the model.
6. Use [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] to make local endpoint calls reproducible.
7. Save benchmark evidence in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]].
8. Use [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] to decide whether local output quality is good enough for the workload.
9. Use [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]] to collect proof across the paper, implementation, local inference, RAG, evaluation, and deployment gates.
10. Use [[LLM/Study/LLM Mastery Self-Assessment Exam|LLM Mastery Self-Assessment Exam]] to test whether the academic and applied knowledge is available without hand-holding.
11. Build the capstone only after the local inference and evaluation gates are complete.

## Level 1: Field Map

**Goal:** Explain what changed from n-gram language models to transformer-based assistants.

Read:

- [[LLM/Pre-2017 — Before Transformers/Language Model Fundamentals|Language Model Fundamentals]]
- [[LLM/Pre-2017 — Before Transformers/Tokenization|Tokenization]]
- [[LLM/2017 — The Transformer/Attention Mechanism|Attention Mechanism]]
- [[LLM/2017 — The Transformer/Transformer Architecture|Transformer Architecture]]
- [[LLM/Study/Attention Implementation Lab|Attention Implementation Lab]]
- [[LLM/2018–2019 — Pretrained Language Models/GPT and Decoder-Only Lineage|GPT and Decoder-Only Lineage]]

Proof:

- Draw the pipeline from text to tokens to logits to next-token sampling.
- Prove that pipeline with [[LLM/Study/LLM Inference Request Lifecycle Lab|LLM Inference Request Lifecycle Lab]] by freezing one local request and tracing tokenization, prefill, decode, sampling, stopping, and returned text.
- Verify tokenizer and chat-template compatibility with [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat Template and Tokenizer Compatibility Lab]] before blaming the model for instruction-following failures.
- Implement scaled dot-product attention with [[LLM/Study/Attention Implementation Lab|Attention Implementation Lab]] and explain the tensor shapes.
- Explain why decoder-only transformers became the dominant general assistant architecture.
- Define perplexity, tokenization, context window, embedding, attention head, and pretraining.

## Level 2: Architecture and Training

**Goal:** Understand the mechanisms that make modern LLMs trainable and scalable.

Read:

- [[LLM/2020–2021 — The Scaling Era/Scaling Laws|Scaling Laws]]
- [[LLM/2020–2021 — The Scaling Era/Training Infrastructure and Parallelism|Training Infrastructure and Parallelism]]
- [[LLM/2020–2021 — The Scaling Era/Mixture-of-Experts Models|Mixture-of-Experts Models]]
- [[LLM/2020–2021 — The Scaling Era/LoRA and QLoRA|LoRA and QLoRA]]
- [[LLM/2022 — Alignment and Chat/Compute Data and Parameter Trade-offs|Compute Data and Parameter Trade-offs]]

Proof:

- Reproduce the main scaling-law intuition: model size, data, and compute are coupled.
- Explain why overtraining a smaller model can be rational when inference cost matters.
- Compare full fine-tuning, LoRA, QLoRA, distillation, and prompt-only adaptation.
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

Proof:

- Build a small RAG pipeline with [[LLM/Study/Local RAG Assistant Lab|Local RAG Assistant Lab]]: chunk, embed, retrieve, rerank, generate, cite.
- Show one failure caused by retrieval miss, one by bad chunking, and one by generation hallucination.
- Build a simple tool-calling loop with schema validation and error handling.
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
- [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]]

Proof:

- Run one local model through a CLI and one local HTTP API.
- Capture a machine/runtime preflight with [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]] before diagnosing quality or speed.
- Use [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] to keep the endpoint loopback-only until exposure, authentication, logs, RAG data, and tools are understood.
- Confirm the local endpoint is using the intended tokenizer, chat template, special tokens, and stop policy.
- Estimate weight memory and KV-cache risk with [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]] before choosing the model/runtime pair.
- Use [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]] to prove the endpoint with a smoke test and diagnose any serving failures.
- Use [[LLM/Study/Local LLM Troubleshooting Decision Tree|Local LLM Troubleshooting Decision Tree]] to name the failed layer before changing model, runtime, prompt, or hardware.
- Use [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] to log repeatable non-streaming, streaming, error, and benchmark rows from the same client.
- Record model, runtime, quantization, hardware, context length, time to first token, tokens/sec, and peak memory in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]].
- Use [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] to score known-answer, schema, RAG/citation, long-context, multi-turn, and workload-specific prompts.
- Explain why KV cache, quantization, batch size, and context length change latency and throughput.
- Compare at least two runtimes, such as Ollama versus llama.cpp, or llama.cpp versus vLLM.

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

1. **Paper map:** write a one-page map of the 20-paper fast path from [[LLM/Study/LLM Study Index|LLM Study Index]] using [[LLM/Study/LLM Paper Reading Protocol|LLM Paper Reading Protocol]].
2. **Attention implementation:** complete [[LLM/Study/Attention Implementation Lab|Attention Implementation Lab]] and explain the tensor shapes.
3. **Local inference report:** complete [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]] and save the benchmark table in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]].
4. **RAG assistant:** build document ingestion, chunking, embedding, retrieval, reranking, generation, and citation output with [[LLM/Study/Local RAG Assistant Lab|Local RAG Assistant Lab]].
5. **Evaluation harness:** evaluate the RAG assistant with [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]], including at least one human rubric and one LLM-as-judge rubric.
6. **Self-assessment:** pass [[LLM/Study/LLM Mastery Self-Assessment Exam|LLM Mastery Self-Assessment Exam]] and link missed-question remediation.
7. **Deployment decision:** write a trade-off memo choosing hosted API, local CPU/GPU, or production serving for one real workload.

Track the proof links and pass signals in [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]] as each capstone step is completed.

## Completion Checklist

- [ ] I can explain the historical timeline without notes.
- [ ] I can derive the attention computation and name each tensor.
- [ ] I can explain pretraining, SFT, RLHF, DPO, LoRA, QLoRA, RAG, function calling, and LLM-as-judge.
- [ ] I can identify when a problem is a retrieval issue, prompt issue, model capability issue, or evaluation issue.
- [ ] I can host a local model, call its API, and record latency/throughput/memory metrics.
- [ ] I can explain the security and privacy boundary of a local model server before exposing it beyond loopback.
- [ ] I can run a local quality harness and explain pass/hold/fail decisions from rubric evidence.
- [ ] I can justify a model/runtime/quantization choice for my hardware and workload.
- [ ] I can read a new LLM paper and place it in the field map.
- [ ] I can build and evaluate a small LLM application end to end.

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/LLM — Learning Path]]
- [[LLM/Study/LLM Study Index]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Mastery Self-Assessment Exam]]
- [[LLM/Study/LLM Architecture Cheatsheet]]
- [[LLM/Study/LLM Paper Reading Protocol]]
- [[LLM/Study/Attention Implementation Lab]]
- [[LLM/Study/Local LLM Hosting and Inference Lab]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local RAG Assistant Lab]]
