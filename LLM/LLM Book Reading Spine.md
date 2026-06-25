---
tags: [llm, index, book, reading-path, navigation]
up: "[[LLM/LLM]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# LLM Book Reading Spine

> **One-line summary** Read the LLM wiki like a book: a curated narrative path through the main articles first, then the labs, runners, evidence layers, and complete corpus index when you want proof or implementation detail.

This page is the reader-facing spine. [[LLM/LLM Corpus Index|LLM Corpus Index]] is the back-of-book index. [[LLM/Study/LLM Study Index|LLM Study Index]] is the workbook. The era folders are the chapters. The raw notes and chunks are the footnotes.

## How To Read This Wiki Like A Book

Read in passes:

1. **First pass: story.** Read the chapter openers and main articles below. Skip runners, raw notes, chunks, and most implementation proofs.
2. **Second pass: mechanism.** Re-read the same path with [[LLM/Study/LLM Math and Tensor Shape Primer]], [[LLM/Study/Attention Implementation Lab]], and [[LLM/Study/Tiny Decoder-Only Transformer Training Lab]] open beside you.
3. **Third pass: local practice.** Follow the local-hosting chapters from environment preflight through endpoint proof, benchmarking, quality, privacy, operations, and deployment decisions.
4. **Fourth pass: defense.** Use the paper reading, claim ledger, oral defense, and academic-to-local matrix notes to prove you can explain the literature and turn it into local inference decisions.

Do not try to read the whole corpus linearly. Runners are machines for producing evidence. Raw notes are source records. Chunks are footnotes. The book is the ordered path below.

## Prologue: What A Language Model Is

Start with the basic object: a model estimates text probability, turns symbols into vectors, trains against a prediction objective, and is judged by metrics that only partially predict usefulness.

- [[LLM/Pre-2017 — Before Transformers/Language Model Fundamentals|Language Model Fundamentals]]
- [[LLM/Pre-2017 — Before Transformers/Language Modeling Objectives|Language Modeling Objectives]]
- [[LLM/Pre-2017 — Before Transformers/Perplexity and Intrinsic Metrics|Perplexity and Intrinsic Metrics]]
- [[LLM/Pre-2017 — Before Transformers/Tokenization|Tokenization]]
- [[LLM/Pre-2017 — Before Transformers/Embeddings and Representation Geometry|Embeddings and Representation Geometry]]
- [[LLM/Pre-2017 — Before Transformers/Optimizers and Training Stability|Optimizers and Training Stability]]

Reader checkpoint: you should be able to explain tokens, embeddings, logits, loss, perplexity, and why probability is not the same thing as usefulness.

## Book I: Before Transformers

The pre-transformer world teaches the problem that transformers solved. Statistical models counted local patterns. Neural networks learned representations. RNNs gave sequence state but paid for it with serial computation and long-range weakness.

- [[LLM/Pre-2017 — Before Transformers/Pre-2017 — Before Transformers Overview|Pre-2017 — Before Transformers Overview]]
- [[LLM/Pre-2017 — Before Transformers/Pre-LLM Neural Network Foundations|Pre-LLM Neural Network Foundations]]
- [[LLM/Pre-2017 — Before Transformers/Pre-Transformer Foundations|Pre-Transformer Foundations]]

Reader checkpoint: you should be able to say why embeddings, recurrence, gating, encoder-decoder models, and attention were necessary but not sufficient.

## Book II: Attention Becomes Architecture

The transformer turns attention from an encoder-decoder accessory into the main computational substrate. This is the architectural hinge of the whole corpus.

- [[LLM/2017 — The Transformer/2017 — The Transformer Overview|2017 — The Transformer Overview]]
- [[LLM/2017 — The Transformer/Attention Mechanism|Attention Mechanism]]
- [[LLM/2017 — The Transformer/Positional Encoding|Positional Encoding]]
- [[LLM/2017 — The Transformer/Transformer Architecture|Transformer Architecture]]
- [[LLM/2017 — The Transformer/Encoder-Decoder Models|Encoder-Decoder Models]]
- [[LLM/2017 — The Transformer/Transformer Breakthrough and Scaling Era|Transformer Breakthrough and Scaling Era]]

Reader checkpoint: you should be able to draw scaled dot-product attention, explain why position is external to attention, and explain why parallelism mattered.

## Book III: Pretraining Becomes The Product

The next step is not just a better model shape. It is a new workflow: pretrain broadly, adapt narrowly, and split the model family into encoder, decoder, and encoder-decoder use cases.

- [[LLM/2018–2019 — Pretrained Language Models/2018–2019 — Pretrained Language Models Overview|2018–2019 — Pretrained Language Models Overview]]
- [[LLM/2018–2019 — Pretrained Language Models/BERT and Encoder Lineage|BERT and Encoder Lineage]]
- [[LLM/2018–2019 — Pretrained Language Models/GPT and Decoder-Only Lineage|GPT and Decoder-Only Lineage]]
- [[LLM/2018–2019 — Pretrained Language Models/Encoder-Only Models|Encoder-Only Models]]
- [[LLM/2018–2019 — Pretrained Language Models/Decoder-Only Models|Decoder-Only Models]]
- [[LLM/2018–2019 — Pretrained Language Models/Supervised Fine-Tuning|Supervised Fine-Tuning]]
- [[LLM/2018–2019 — Pretrained Language Models/Domain Adaptation|Domain Adaptation]]
- [[LLM/2018–2019 — Pretrained Language Models/Distillation and Model Compression|Distillation and Model Compression]]
- [[LLM/2018–2019 — Pretrained Language Models/Data Curation and Deduplication|Data Curation and Deduplication]]
- [[LLM/2018–2019 — Pretrained Language Models/Knowledge and Reasoning Benchmarks|Knowledge and Reasoning Benchmarks]]

Reader checkpoint: you should be able to choose encoder-only, decoder-only, or encoder-decoder architectures from workload needs.

## Book IV: Scale Becomes A Method

Scaling changes the field from architecture invention to systems strategy. Data, compute, parameters, infrastructure, and adaptation methods become first-class levers.

- [[LLM/2020–2021 — The Scaling Era/2020–2021 — The Scaling Era Overview|2020–2021 — The Scaling Era Overview]]
- [[LLM/2020–2021 — The Scaling Era/Scaling Laws|Scaling Laws]]
- [[LLM/2022 — Alignment and Chat/Compute Data and Parameter Trade-offs|Compute Data and Parameter Trade-offs]]
- [[LLM/2020–2021 — The Scaling Era/Training Infrastructure and Parallelism|Training Infrastructure and Parallelism]]
- [[LLM/2020–2021 — The Scaling Era/Few-Shot Prompting|Few-Shot Prompting]]
- [[LLM/2020–2021 — The Scaling Era/In-Context Learning Mechanisms|In-Context Learning Mechanisms]]
- [[LLM/2020–2021 — The Scaling Era/Parameter-Efficient Fine-Tuning|Parameter-Efficient Fine-Tuning]]
- [[LLM/2020–2021 — The Scaling Era/LoRA and QLoRA|LoRA and QLoRA]]
- [[LLM/2020–2021 — The Scaling Era/Mixture-of-Experts Models|Mixture-of-Experts Models]]
- [[LLM/2020–2021 — The Scaling Era/Retrieval Pipelines and Context Assembly|Retrieval Pipelines and Context Assembly]]
- [[LLM/2020–2021 — The Scaling Era/Contamination and Data Leakage|Contamination and Data Leakage]]
- [[LLM/2020–2021 — The Scaling Era/Continual Fine-Tuning and Catastrophic Forgetting|Continual Fine-Tuning and Catastrophic Forgetting]]
- [[LLM/2020–2021 — The Scaling Era/Vision-Language Models|Vision-Language Models]]

Reader checkpoint: you should be able to explain why more parameters alone are not enough: data quality, compute allocation, evaluation contamination, and serving cost all matter.

## Book V: Alignment Turns Models Into Assistants

This is where a model that predicts text becomes an assistant that follows instructions, uses role conditioning, and is judged by human preference and safety behavior.

- [[LLM/2022 — Alignment and Chat/2022 — Alignment and Chat Overview|2022 — Alignment and Chat Overview]]
- [[LLM/2022 — Alignment and Chat/Instruction Tuning|Instruction Tuning]]
- [[LLM/2022 — Alignment and Chat/Reinforcement Learning from Human Feedback|Reinforcement Learning from Human Feedback]]
- [[LLM/2022 — Alignment and Chat/Direct Preference Optimization|Direct Preference Optimization]]
- [[LLM/2022 — Alignment and Chat/Constitutional AI|Constitutional AI]]
- [[LLM/2022 — Alignment and Chat/System Prompts and Role Conditioning|System Prompts and Role Conditioning]]
- [[LLM/2022 — Alignment and Chat/Chain-of-Thought Prompting|Chain-of-Thought Prompting]]
- [[LLM/2022 — Alignment and Chat/Human Evaluation and Preference Studies|Human Evaluation and Preference Studies]]
- [[LLM/2022 — Alignment and Chat/Alignment Objectives and Failure Modes|Alignment Objectives and Failure Modes]]
- [[LLM/2022 — Alignment and Chat/Red-Teaming and Safety Evaluations|Red-Teaming and Safety Evaluations]]
- [[LLM/2022 — Alignment and Chat/Mechanistic Interpretability|Mechanistic Interpretability]]
- [[LLM/2022 — Alignment and Chat/Quantization|Quantization]]

Reader checkpoint: you should be able to separate base-model capability, instruction following, preference alignment, safety evaluation, and deployment constraint.

## Book VI: Open Models, Retrieval, And Tools

The field becomes practical and modular: open weights, vector databases, RAG, reranking, structured output, function calling, and tool loops turn language models into systems.

- [[LLM/2023 — Open Models and Agents/2023 — Open Models and Agents Overview|2023 — Open Models and Agents Overview]]
- [[LLM/2023 — Open Models and Agents/Open-Weight Model Ecosystem|Open-Weight Model Ecosystem]]
- [[LLM/2023 — Open Models and Agents/Frontier Labs and Open vs Closed Models|Frontier Labs and Open vs Closed Models]]
- [[LLM/2023 — Open Models and Agents/Embeddings and Vector Databases|Embeddings and Vector Databases]]
- [[LLM/2023 — Open Models and Agents/Chunking Strategies|Chunking Strategies]]
- [[LLM/2023 — Open Models and Agents/Hybrid Search|Hybrid Search]]
- [[LLM/2023 — Open Models and Agents/Reranking|Reranking]]
- [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes|RAG Evaluation and Failure Modes]]
- [[LLM/2023 — Open Models and Agents/Function Calling|Function Calling]]
- [[LLM/2023 — Open Models and Agents/Tool-Augmented Prompting|Tool-Augmented Prompting]]
- [[LLM/2023 — Open Models and Agents/Tool Selection and Execution Loops|Tool Selection and Execution Loops]]
- [[LLM/2023 — Open Models and Agents/Structured Output and Constrained Generation|Structured Output and Constrained Generation]]
- [[LLM/2023 — Open Models and Agents/Planning and Task Decomposition|Planning and Task Decomposition]]
- [[LLM/2023 — Open Models and Agents/LLM-as-Judge|LLM-as-Judge]]
- [[LLM/2023 — Open Models and Agents/Multimodal Tokenization and Fusion|Multimodal Tokenization and Fusion]]

Reader checkpoint: you should be able to design a RAG/tool system without confusing retrieval quality, generation quality, citation quality, and tool safety.

## Book VII: Frontier Systems And Efficiency

Now the bottleneck is not only intelligence. It is serving. Context windows, KV cache, batching, speculative decoding, long-context attention, and multimodal input shape what you can host and what it costs.

- [[LLM/2024–2025 — Frontier and Efficiency/2024–2025 — Frontier and Efficiency Overview|2024–2025 — Frontier and Efficiency Overview]]
- [[LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants|Efficient Attention and Long-Context Variants]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse|KV Cache and Context Reuse]]
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching|Batching and Continuous Batching]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs|Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/2024–2025 — Frontier and Efficiency/Speculative Decoding|Speculative Decoding]]
- [[LLM/2024–2025 — Frontier and Efficiency/State Space Models and Mamba|State Space Models and Mamba]]
- [[LLM/2024–2025 — Frontier and Efficiency/Memory and State Management|Memory and State Management]]
- [[LLM/2024–2025 — Frontier and Efficiency/Code Generation Agents|Code Generation Agents]]
- [[LLM/2024–2025 — Frontier and Efficiency/Code and Agentic Benchmarks|Code and Agentic Benchmarks]]
- [[LLM/2024–2025 — Frontier and Efficiency/Multi-Agent Systems|Multi-Agent Systems]]
- [[LLM/2024–2025 — Frontier and Efficiency/OCR Documents and UI Understanding|OCR Documents and UI Understanding]]
- [[LLM/2024–2025 — Frontier and Efficiency/Speech-Language Models|Speech-Language Models]]
- [[LLM/2024–2025 — Frontier and Efficiency/Video Understanding Models|Video Understanding Models]]
- [[LLM/2024–2025 — Frontier and Efficiency/Multimodal Evaluation and Safety|Multimodal Evaluation and Safety]]

Reader checkpoint: you should be able to explain why a local model can be "small enough to load" but still fail latency, context, memory, or quality requirements.

## Book VIII: Reasoning And Agents

The latest era adds test-time compute, reasoning distillation, GUI control, coding agents, prompt caching, and common tool protocols. Read this last so the claims sit on top of the full stack rather than floating as product hype.

- [[LLM/2026 — Reasoning and Agents/2026 — Reasoning and Agents Overview|2026 — Reasoning and Agents Overview]]
- [[LLM/2026 — Reasoning and Agents/Reasoning Models and Test-Time Compute|Reasoning Models and Test-Time Compute]]
- [[LLM/2026 — Reasoning and Agents/DeepSeek R1 and Open Reasoning|DeepSeek R1 and Open Reasoning]]
- [[LLM/2026 — Reasoning and Agents/Reasoning Distillation|Reasoning Distillation]]
- [[LLM/2026 — Reasoning and Agents/Prompt Caching and Inference Infrastructure|Prompt Caching and Inference Infrastructure]]
- [[LLM/2026 — Reasoning and Agents/Model Context Protocol|Model Context Protocol]]
- [[LLM/2026 — Reasoning and Agents/Agentic Coding Systems|Agentic Coding Systems]]
- [[LLM/2026 — Reasoning and Agents/Computer Use and GUI Agents|Computer Use and GUI Agents]]
- [[LLM/2026 — Reasoning and Agents/Frontier Models 2025-2026|Frontier Models 2025-2026]]

Reader checkpoint: you should be able to separate model reasoning, tool execution, agent orchestration, context protocol, and serving infrastructure.

## Book IX: The Local LLM Practicum

This is the practical book inside the book. It turns the academic spine into a local system you can run, measure, debug, and either accept or reject.

### First Endpoint

- [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM First Run Readiness Snapshot|Local LLM First Run Readiness Snapshot]]
- [[LLM/Study/Local LLM First Model Candidate Ladder|Local LLM First Model Candidate Ladder]]
- [[LLM/Study/Local LLM Windows Model Store and Cache Plan|Local LLM Windows Model Store and Cache Plan]]
- [[LLM/Study/Local LLM Windows Runtime Install Gate|Local LLM Windows Runtime Install Gate]]
- [[LLM/Study/Local LLM First Model Pull Gate|Local LLM First Model Pull Gate]]
- [[LLM/Study/Local LLM First Runtime Health Snapshot|Local LLM First Runtime Health Snapshot]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet|Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM First Inference Proof - 2026-06-16|Local LLM First Inference Proof - 2026-06-16]]

### Client, Timing, And Benchmarking

- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible Streaming Timing Proof - 2026-06-16|Local LLM OpenAI-Compatible Streaming Timing Proof - 2026-06-16]]
- [[LLM/Study/Local LLM First Benchmark Row Proof - 2026-06-16|Local LLM First Benchmark Row Proof - 2026-06-16]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide|Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]]

### Quality, Safety, And Operations

- [[LLM/Study/Local LLM First Endpoint Audit and Quality Probe - 2026-06-16|Local LLM First Endpoint Audit and Quality Probe - 2026-06-16]]
- [[LLM/Study/Local LLM Quality Remediation Probe - 2026-06-16|Local LLM Quality Remediation Probe - 2026-06-16]]
- [[LLM/Study/Local LLM Calculator Tool Remediation Proof - 2026-06-16|Local LLM Calculator Tool Remediation Proof - 2026-06-16]]
- [[LLM/Study/Local LLM Structured Format Remediation Proof - 2026-06-16|Local LLM Structured Format Remediation Proof - 2026-06-16]]
- [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Security and Privacy Proof - 2026-06-16|Local LLM Security and Privacy Proof - 2026-06-16]]
- [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook|Local LLM Service Lifecycle and Upgrade Runbook]]

### Selection, Deployment, And Extension

- [[LLM/Study/Local LLM Workload to Model Selection Playbook|Local LLM Workload to Model Selection Playbook]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM Runtime Stack Anatomy|Local LLM Runtime Stack Anatomy]]
- [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]]
- [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Hands-On Practicum Sequence|Local LLM Hands-On Practicum Sequence]]
- [[LLM/Study/Local RAG Assistant Lab|Local RAG Assistant Lab]]

Reader checkpoint: you should be able to host a local endpoint, call it through an OpenAI-compatible client, measure latency and tokens, evaluate quality, keep it private, and decide whether it is good enough for a specific workload.

## Book X: Defense, Papers, And Mastery

The final book is not more reading. It is proving that you can explain the field without hand-waving and connect papers to local decisions.

- [[LLM/Study/LLM Paper Reading Protocol|LLM Paper Reading Protocol]]
- [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map|LLM 20-Paper Fast Path Synthesis Map]]
- [[LLM/Study/LLM Paper Claim Ledger|LLM Paper Claim Ledger]]
- [[LLM/Study/LLM Paper Claim Audit Runner|LLM Paper Claim Audit Runner]]
- [[LLM/Study/LLM Paper Oral Defense Runner|LLM Paper Oral Defense Runner]]
- [[LLM/Study/LLM Paper-to-Local Proof Router|LLM Paper-to-Local Proof Router]]
- [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner|LLM Academic-to-Local Defense Matrix Runner]]
- [[LLM/Study/LLM Mastery Roadmap|LLM Mastery Roadmap]]
- [[LLM/Study/LLM Mastery Self-Assessment Exam|LLM Mastery Self-Assessment Exam]]
- [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]
- [[LLM/Study/Local LLM Capstone Project Blueprint|Local LLM Capstone Project Blueprint]]

Reader checkpoint: you should be able to defend a paper claim, name the evidence, state the limitation, predict the local implication, and route the next proof artifact.

## Appendices

Use these when the book path is not enough:

- [[LLM/LLM Corpus Index|LLM Corpus Index]] — complete all-links map.
- [[LLM/Sources/Sources Index|Sources Index]] — source bibliography.
- [[LLM/Study/LLM Study Index|LLM Study Index]] — all study notes, labs, runners, and drills.
- [[LLM/Study/LLM Active Recall Question Bank|LLM Active Recall Question Bank]] — recall prompts after reading.
- [[LLM/Study/LLM Mastery Dashboard|LLM Mastery Dashboard]] — daily next action and evidence routing.

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/LLM Corpus Index]]
- [[LLM/Study/LLM Study Index]]
