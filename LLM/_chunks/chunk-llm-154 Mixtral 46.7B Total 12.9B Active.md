---
tags: [llm, chunk]
source: "[[raw-llm-039]]"
confidence: high
supports:
  - "[[LLM/2020–2021 — The Scaling Era/Mixture-of-Experts Models]]"
  - "[[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]"
qna_seeds:
  - "Q: What is Mixtral's parameter efficiency ratio? A: Mixtral has 46.7B total parameters but activates only 12.9B per forward pass (top-2 of 8 experts), achieving 70B-class quality at roughly the inference cost of a 13B dense model."
---

# Mixtral Activates 12.9B of 46.7B Parameters Per Token

Mixtral contains 46.7 billion total parameters across its 8 experts per layer, but each token activates only 12.9 billion parameters during a forward pass (the 2 selected experts plus shared attention and embedding layers). This means Mixtral achieves the knowledge capacity of a ~47B parameter model while incurring roughly the inference FLOPs of a ~13B dense model. The 3.6× ratio between total and active parameters demonstrates the core efficiency promise of sparse MoE: storing more knowledge than you compute over per token.