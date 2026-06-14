---
tags: [llm, learning-path]
---
# LLM — Learning Path

> A guided, progressive tour through the history and technology of large language models. Four passes, each building on the last.

## How to Use This Path

| Pass | Focus | Read | Time |
|------|-------|------|------|
| 1 — Intuition | Build mental map | 🎯 sections only | ~2 hrs |
| 2 — Core | Understand mechanics | ⚙️ sections + Warm-Up | ~8 hrs |
| 3 — Deep Dive | Master details | 🔬 sections (selective) | ~15 hrs |
| 4 — Practice | Build skill | 🏋️ sections + drills | Ongoing |

For proof-based progress, use [[LLM/Study/LLM Mastery Roadmap|LLM Mastery Roadmap]] alongside this chronological path. The learning path tells you what to read; the roadmap tells you what you must be able to explain, build, benchmark, and evaluate.

Use [[LLM/Study/LLM Mastery Self-Assessment Exam|LLM Mastery Self-Assessment Exam]] after each pass when you want a stricter oral/practical check across academic concepts and local inference operations.

---

## Pass 1 — Intuition (~2 hours)

Read ONLY the 🎯 Intuition section of each page. Build a chronological mental map of how language models evolved.

### Pre-2017 — Before Transformers
1. [[Pre-2017 — Before Transformers Overview]] — the pre-transformer era hub
2. [[Language Model Fundamentals]] — what a language model is and why it matters
3. [[Pre-Transformer Foundations]] — RNNs, LSTMs, seq2seq, attention origins
4. [[Embeddings and Representation Geometry]] — Word2Vec, GloVe, and distributed representations
5. [[Tokenization]] — BPE, WordPiece, SentencePiece
6. [[Language Modeling Objectives]] — next-token prediction, masked LM
7. [[Optimizers and Training Stability]] — SGD, Adam, learning rate schedules
8. [[Perplexity and Intrinsic Metrics]] — measuring language model quality

### 2017 — The Transformer
9. [[2017 — The Transformer Overview]] — the transformer era hub
10. [[Attention Mechanism]] — scaled dot-product attention, multi-head attention
11. [[Positional Encoding]] — sinusoidal, learned, rotary (RoPE)
12. [[Transformer Architecture]] — encoder-decoder, the original design
13. [[Encoder-Decoder Models]] — T5, BART, and the full architecture
14. [[Transformer Breakthrough and Scaling Era]] — why attention replaced recurrence

### 2018–2019 — Pretrained Language Models
15. [[2018–2019 — Pretrained Language Models Overview]] — the pretraining era hub
16. [[BERT and Encoder Lineage]] — masked LM, bidirectional context
17. [[GPT and Decoder-Only Lineage]] — autoregressive pretraining, GPT-1/2
18. [[Decoder-Only Models]] — the architecture that won
19. [[Encoder-Only Models]] — BERT, RoBERTa, classification workhorses
20. [[Supervised Fine-Tuning]] — adapting pretrained models to tasks
21. [[Knowledge and Reasoning Benchmarks]] — GLUE, SuperGLUE, and beyond
22. [[Distillation and Model Compression]] — DistilBERT, knowledge transfer
23. [[Data Curation and Deduplication]] — training data quality matters
24. [[Domain Adaptation]] — adapting models to specific fields

### 2020–2021 — The Scaling Era
25. [[2020–2021 — The Scaling Era Overview]] — the scaling era hub
26. [[Scaling Laws]] — Chinchilla, Kaplan — how scale predicts performance
27. [[In-Context Learning Mechanisms]] — GPT-3's emergent few-shot ability
28. [[Few-Shot Prompting]] — task specification through examples
29. [[Parameter-Efficient Fine-Tuning]] — adapters, prefix tuning
30. [[LoRA and QLoRA]] — low-rank adaptation for efficient fine-tuning
31. [[Mixture-of-Experts Models]] — sparse activation, Switch Transformer
32. [[Training Infrastructure and Parallelism]] — data/model/pipeline parallelism
33. [[Vision-Language Models]] — CLIP, connecting vision and language
34. [[Retrieval Pipelines and Context Assembly]] — early RAG foundations
35. [[Contamination and Data Leakage]] — benchmark validity concerns
36. [[Continual Fine-Tuning and Catastrophic Forgetting]] — stability-plasticity trade-off

### 2022 — Alignment and Chat
37. [[2022 — Alignment and Chat Overview]] — the alignment era hub
38. [[Reinforcement Learning from Human Feedback]] — RLHF pipeline
39. [[Instruction Tuning]] — teaching models to follow instructions
40. [[Chain-of-Thought Prompting]] — eliciting step-by-step reasoning
41. [[Direct Preference Optimization]] — RLHF without the RL
42. [[Constitutional AI]] — AI self-critique and improvement
43. [[Alignment Objectives and Failure Modes]] — helpful, harmless, honest
44. [[Quantization]] — INT8, INT4, GPTQ, AWQ
45. [[System Prompts and Role Conditioning]] — steering model behavior
46. [[Mechanistic Interpretability]] — understanding what's inside
47. [[Red-Teaming and Safety Evaluations]] — adversarial testing
48. [[Human Evaluation and Preference Studies]] — measuring alignment
49. [[Compute Data and Parameter Trade-offs]] — optimal allocation

### 2023 — Open Models and Agents
50. [[2023 — Open Models and Agents Overview]] — the open-models era hub
51. [[Open-Weight Model Ecosystem]] — LLaMA, Mistral, and the open revolution
52. [[Frontier Labs and Open vs Closed Models]] — OpenAI, Anthropic, Google, Meta
53. [[Embeddings and Vector Databases]] — dense retrieval infrastructure
54. [[Chunking Strategies]] — splitting documents for retrieval
55. [[Hybrid Search]] — combining dense and sparse retrieval
56. [[Reranking]] — cross-encoder reranking for precision
57. [[RAG Evaluation and Failure Modes]] — measuring retrieval-augmented generation
58. [[Function Calling]] — structured tool invocation
59. [[Tool-Augmented Prompting]] — ReAct, Toolformer patterns
60. [[Tool Selection and Execution Loops]] — agent tool-use cycles
61. [[Planning and Task Decomposition]] — breaking complex tasks into steps
62. [[Structured Output and Constrained Generation]] — JSON mode, grammar-constrained decoding
63. [[LLM-as-Judge]] — using LLMs to evaluate LLM outputs
64. [[Multimodal Tokenization and Fusion]] — processing images and text together

### 2024–2025 — Frontier and Efficiency
65. [[2024–2025 — Frontier and Efficiency Overview]] — the frontier era hub
66. [[State Space Models and Mamba]] — alternatives to attention
67. [[Efficient Attention and Long-Context Variants]] — 1M+ token contexts
68. [[Speculative Decoding]] — draft-verify acceleration
69. [[KV Cache and Context Reuse]] — memory optimization for inference
70. [[Batching and Continuous Batching]] — throughput optimization
71. [[Serving Architectures and Throughput-Latency Trade-offs]] — vLLM, TGI, production serving
72. [[Code Generation Agents]] — Copilot, Cursor, agentic coding
73. [[Multi-Agent Systems]] — orchestrating multiple LLM agents
74. [[Memory and State Management]] — long-term agent memory
75. [[Speech-Language Models]] — audio-native LLMs
76. [[Video Understanding Models]] — temporal visual reasoning
77. [[OCR Documents and UI Understanding]] — document and screen comprehension
78. [[Code and Agentic Benchmarks]] — SWE-bench, HumanEval
79. [[Multimodal Evaluation and Safety]] — evaluating beyond text

### 2026 — Reasoning and Agents
80. [[2026 — Reasoning and Agents Overview]] — the reasoning era hub
81. [[Reasoning Models and Test-Time Compute]] — thinking longer at inference
82. [[DeepSeek R1 and Open Reasoning]] — open-source reasoning breakthroughs
83. [[Frontier Models 2025-2026]] — Claude, GPT, Gemini frontier
84. [[Agentic Coding Systems]] — autonomous software engineering
85. [[Computer Use and GUI Agents]] — LLMs controlling screens
86. [[Model Context Protocol]] — standardized tool integration
87. [[Prompt Caching and Inference Infrastructure]] — efficient serving at scale
88. [[Reasoning Distillation]] — transferring reasoning to smaller models

---

## Pass 2 — Core Mechanics (~8 hours)

Re-read each page's ⚙️ Core Mechanics and 🏋️ Warm-Up sections. Understand *how* each breakthrough works.

### Suggested order
Follow the same chronological sequence as Pass 1. Spend extra time on:
- **Attention mechanism** — trace Q, K, V matrices through a self-attention step
- **Scaling laws** — understand the Chinchilla-optimal compute/data ratio
- **RLHF pipeline** — trace reward model → PPO → aligned model
- **RAG stack** — follow a query through embed → retrieve → rerank → generate
- **LoRA** — understand low-rank decomposition of weight updates

### Checkpoints
After this pass you should be able to:
- [ ] Explain self-attention with matrix operations
- [ ] Describe the BERT vs GPT architectural split and why decoders won
- [ ] Trace the RLHF training pipeline end to end
- [ ] Explain scaling laws and compute-optimal training
- [ ] Describe a complete RAG pipeline from query to answer

---

## Pass 3 — Deep Dive (selective, ~15 hours)

Read the 🔬 Deep Dive sections for areas you want to master.

### Track A — Architecture & Training
- [[Attention Mechanism]] — multi-query attention, grouped-query attention
- [[Scaling Laws]] — emergent abilities, phase transitions
- [[Mixture-of-Experts Models]] — routing, load balancing, expert specialization
- [[Training Infrastructure and Parallelism]] — ZeRO, FSDP, tensor parallelism
- [[State Space Models and Mamba]] — S4, Mamba-2, linear attention alternatives

### Track B — Alignment & Safety
- [[Reinforcement Learning from Human Feedback]] — reward hacking, KL penalty
- [[Direct Preference Optimization]] — derivation from RLHF objective
- [[Constitutional AI]] — recursive self-improvement
- [[Red-Teaming and Safety Evaluations]] — jailbreaks, robustness testing
- [[Alignment Objectives and Failure Modes]] — deceptive alignment, reward misspecification

### Track C — Retrieval & Agents
- [[Embeddings and Vector Databases]] — ANN algorithms, embedding fine-tuning
- [[Chunking Strategies]] — semantic chunking, parent-child strategies
- [[Function Calling]] — parallel tool use, structured schemas
- [[Planning and Task Decomposition]] — tree-of-thought, self-reflection
- [[Multi-Agent Systems]] — orchestration patterns, debate, specialization

### Track D — Inference & Efficiency
- [[Quantization]] — GPTQ, AWQ, GGUF formats
- [[Speculative Decoding]] — draft model selection, acceptance rates
- [[KV Cache and Context Reuse]] — paged attention, prefix caching
- [[Efficient Attention and Long-Context Variants]] — ring attention, flash attention
- [[Serving Architectures and Throughput-Latency Trade-offs]] — batching strategies

---

## Pass 4 — Practice (ongoing)

Build active-recall skill through drills and hands-on experimentation.

### Drills
- [[LLM Study Index]] — full study plan, review drills, 20-paper fast path
- [[LLM/Study/LLM Mastery Roadmap|LLM Mastery Roadmap]] — competency gates and capstone sequence
- [[LLM/Study/LLM Mastery Self-Assessment Exam|LLM Mastery Self-Assessment Exam]] — oral and practical gate before claiming mastery
- [[LLM Architecture Cheatsheet]] — quick-reference tables

### Hands-On Exercises
1. **Fine-tune a model** — LoRA fine-tune an open model on a custom dataset
2. **Build a RAG pipeline** — embed, chunk, retrieve, rerank, generate
3. **Implement attention** — code scaled dot-product attention from scratch
4. **Prompt engineering** — compare zero-shot, few-shot, and chain-of-thought on the same task
5. **Deploy and serve** — complete [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]], use [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]] to expose an endpoint, quantize a model, serve with vLLM or llama.cpp, measure latency/throughput
6. **Build an agent** — function-calling agent with tool use and planning

### Capstone
Build a complete RAG-powered assistant: document ingestion → chunking → embedding → vector store → retrieval → reranking → generation → evaluation with LLM-as-Judge.
