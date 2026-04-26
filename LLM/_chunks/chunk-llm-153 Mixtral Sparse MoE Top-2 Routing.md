---
tags: [llm, chunk]
source: "[[raw-llm-039]]"
confidence: high
supports:
  - "[[LLM/2020–2021 — The Scaling Era/Mixture-of-Experts Models]]"
qna_seeds:
  - "Q: How does Mixtral's expert routing work? A: Mixtral uses 8 expert FFN blocks per layer with a top-2 routing mechanism — for each token, a learned gating network selects the 2 most relevant experts, and only those 2 are activated, leaving the other 6 idle for that token."
---

# Mixtral Uses Top-2 Routing Across 8 Experts Per Layer

Mixtral (Jiang et al., 2024) implements a sparse Mixture-of-Experts architecture with 8 expert feed-forward network blocks per Transformer layer. For each input token, a learned gating network computes routing probabilities and selects the top 2 experts with the highest scores. Only these 2 experts are activated and their outputs are combined weighted by the gating scores; the remaining 6 experts perform no computation for that token. This sparse activation pattern means each token uses only a fraction of the model's total parameters, dramatically reducing inference compute.