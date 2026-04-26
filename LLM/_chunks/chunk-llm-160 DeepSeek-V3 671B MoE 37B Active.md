---
tags: [llm, chunk]
source: "[[raw-llm-040]]"
confidence: high
supports:
  - "[[LLM/2020–2021 — The Scaling Era/Mixture-of-Experts Models]]"
  - "[[LLM/2024–2025 — Frontier and Efficiency/2024–2025 — Frontier and Efficiency Overview]]"
qna_seeds:
  - "Q: What are DeepSeek-V3's scale and performance characteristics? A: DeepSeek-V3 is a 671B total parameter MoE model with 37B active parameters per token, trained on 14.8T tokens. It matches GPT-4o and Claude 3.5 Sonnet on most benchmarks, demonstrating that architectural innovation can close the gap with frontier labs at a fraction of the cost."
---

# DeepSeek-V3 671B MoE Matches Frontier at Fraction of Cost

DeepSeek-V3 is a 671-billion parameter Mixture-of-Experts model that activates 37 billion parameters per forward pass, trained on 14.8 trillion tokens. It matches or approaches GPT-4o and Claude 3.5 Sonnet performance on most major benchmarks including MMLU, HumanEval, MATH, and GSM8K. Achieving frontier-class quality at a reported training cost of ~\.5M demonstrated that architectural innovation (MLA, auxiliary-loss-free balancing) and training efficiency (FP8) can substantially close the gap with well-resourced frontier labs, challenging the assumption that only \+ budgets can produce top-tier models.