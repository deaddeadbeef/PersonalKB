---
tags: [llm, moc]
up: "[[Welcome]]"
---

# Large Language Models — A Chronicle

> From statistical n-grams to autonomous agents: the story of how machines learned to speak.

> 📚 **New here?** Start with the [[LLM — Learning Path|Learning Path]] for a guided, progressive tour.

## The Timeline

### [[Pre-2017 — Before Transformers Overview|Pre-2017 — Before Transformers]]
N-grams, RNNs, word embeddings, and the foundations that made everything possible.
*7 pages — Language modeling, tokenization, embeddings, optimization*

### [[2017 — The Transformer Overview|2017 — The Transformer]]
"Attention Is All You Need" — one paper replaces recurrence and launches the modern era.
*5 pages — Self-attention, positional encoding, the full architecture*

### [[2018–2019 — Pretrained Language Models Overview|2018–2019 — Pretrained Language Models]]
BERT and GPT split the world into encoder and decoder paths. Pretrain-then-fine-tune becomes the paradigm.
*9 pages — BERT, GPT-1/2, fine-tuning, benchmarks, distillation*

### [[2020–2021 — The Scaling Era Overview|2020–2021 — The Scaling Era]]
GPT-3 proves scale is a strategy. Few-shot learning, LoRA, CLIP, and distributed training rewrite the rules.
*11 pages — Scaling laws, in-context learning, PEFT, MoE, RAG origins*

### [[2022 — Alignment and Chat Overview|2022 — Alignment and Chat]]
RLHF, InstructGPT, chain-of-thought, and ChatGPT transform raw models into usable assistants.
*12 pages — Alignment, DPO, Constitutional AI, instruction tuning, quantization*

### [[2023 — Open Models and Agents Overview|2023 — Open Models and Agents]]
LLaMA breaks open the field. RAG matures, agents learn to use tools, and structured output goes production.
*14 pages — Open models, RAG stack, function calling, tool use, LLM-as-Judge*

### [[2024–2025 — Frontier and Efficiency Overview|2024–2025 — Frontier and Efficiency]]
SSMs challenge attention, context windows hit 1M tokens, and autonomous agents write code.
*14 pages — Mamba, speculative decoding, serving infra, multi-agent, multimodal frontier*

### [[2026 — Reasoning and Agents Overview|2026 — Reasoning and Agents]]
LLMs learn to think longer and act autonomously. Reasoning models, coding agents, and new inference paradigms.
*8 pages — Test-time compute, DeepSeek R1, frontier models, agentic coding, computer use, MCP*

---

## Study Materials
- [[LLM/Study/LLM Study Index|LLM Study Index]] — Review drills, cheatsheet, 20-paper fast path
- [[LLM/Study/LLM Mastery Roadmap|LLM Mastery Roadmap]] — Competency gates from field map to local inference and capstone
- [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]] — Evidence ledger for paper, implementation, inference, RAG, evaluation, and deployment proof
- [[LLM/Study/LLM Paper Reading Protocol|LLM Paper Reading Protocol]] — Method for extracting claims, evidence, limitations, and deployment implications from papers
- [[LLM/Study/LLM Architecture Cheatsheet|LLM Architecture Cheatsheet]] — Quick-reference tables
- [[LLM/Study/Attention Implementation Lab|Attention Implementation Lab]] — Scaled dot-product attention, masking, multi-head tensor shapes, and KV-cache implications
- [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]] — Practical path to run, serve, and benchmark local models
- [[LLM/Study/LLM Inference Request Lifecycle Lab|LLM Inference Request Lifecycle Lab]] — Request-level path from prompt assembly to tokens, prefill, decode, sampling, stopping, streaming, and measurement
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]] — Memory, context, quantization, and runtime sizing decisions
- [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] — Reproducible run log for local model/runtime comparisons
- [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] — Workload-specific prompt suites, rubrics, pairwise comparison, and RAG/citation gates
- [[LLM/Study/Local RAG Assistant Lab|Local RAG Assistant Lab]] — End-to-end local retrieval, citation, and grounded-answer workflow
- [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]] — Endpoint smoke tests and failure triage for local model servers

## Infrastructure
- [[LLM/Sources/Sources Index|Sources Index]] — Paper bibliography
- [[LLM/_queries/QnA - Chunk Coverage Map|QnA — Chunk Coverage Map]] — Chunk backing dashboard
- [[LLM/_queries/QnA System Roadmap|QnA — System Roadmap]] — Build progress tracker
