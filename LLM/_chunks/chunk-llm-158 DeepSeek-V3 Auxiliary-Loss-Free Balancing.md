---
tags: [llm, chunk]
source: "[[raw-llm-040]]"
confidence: high
supports:
  - "[[LLM/2020–2021 — The Scaling Era/Mixture-of-Experts Models]]"
qna_seeds:
  - "Q: How does DeepSeek-V3 balance expert load without an auxiliary loss? A: DeepSeek-V3 uses a bias-based load balancing strategy that adds a learnable bias term to expert gating scores, dynamically adjusted to equalize expert utilization without the auxiliary balance loss that typically degrades model quality in MoE training."
---

# DeepSeek-V3 Eliminates Auxiliary Loss for Expert Balancing

Traditional MoE models (Switch Transformer, Mixtral) use an auxiliary load-balancing loss added to the training objective to prevent token routing collapse (all tokens going to a few experts). This auxiliary loss degrades model quality because it conflicts with the primary language modeling objective. DeepSeek-V3 replaces this with an auxiliary-loss-free strategy using learnable bias terms added to expert gating scores, dynamically adjusted to equalize expert utilization. This approach achieves balanced routing without sacrificing language modeling performance, contributing to DeepSeek-V3's strong benchmark results.