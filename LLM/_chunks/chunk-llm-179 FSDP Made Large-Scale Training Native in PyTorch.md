---
tags: [chunk, llm]
id: "chunk-llm-179"
source: "[[LLM/_raw/raw-llm-045 PyTorch FSDP]]"
source_loc: "Why It Matters"
topic: "FSDP as native PyTorch API"
claim: "FSDP made trillion-parameter-scale training accessible through a native PyTorch API, eliminating the need for external distributed training frameworks for many workloads."
confidence: "verified"
supports:
  - "[[LLM/2020–2021 — The Scaling Era/2020–2021 — The Scaling Era]]"
  - "[[LLM/2024–2025 — Frontier and Efficiency/2024–2025 — Frontier and Efficiency]]"
qna_seeds:
  - "Q: Why is FSDP significant for the PyTorch ecosystem? A: It brought ZeRO-3 style sharding natively into PyTorch, so teams can train very large models without depending on DeepSpeed or custom distributed frameworks."
  - "Q: Is FSDP now the default for LLM training in PyTorch? A: Yes — FSDP (and its successor FSDP2) is the default distributed training strategy for LLM fine-tuning and pre-training in the PyTorch ecosystem."
up: "[[LLM/LLM]]"
---

# FSDP Made Large-Scale Training Native in PyTorch

Before FSDP, training models too large for single-GPU memory in PyTorch required external libraries like DeepSpeed or Megatron-LM. PyTorch FSDP brought ZeRO-3-equivalent sharding into the core framework with a familiar API: wrapping modules with FSDP() is as simple as wrapping with DistributedDataParallel(). This lowered the barrier to large-scale training significantly. FSDP became the default strategy for LLM fine-tuning and pre-training in the PyTorch ecosystem, and Meta's subsequent FSDP2 rewrite further improved composability with tensor parallelism and other advanced parallelism strategies.
