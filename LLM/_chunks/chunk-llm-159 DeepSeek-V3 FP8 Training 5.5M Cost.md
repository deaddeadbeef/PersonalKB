---
tags: [llm, chunk]
source: "[[raw-llm-040]]"
confidence: high
supports:
  - "[[LLM/2024–2025 — Frontier and Efficiency/2024–2025 — Frontier and Efficiency Overview]]"
  - "[[LLM/2022 — Alignment and Chat/Compute Data and Parameter Trade-offs]]"
qna_seeds:
  - "Q: How much did DeepSeek-V3 cost to train? A: DeepSeek-V3 was trained using FP8 mixed-precision on 2,048 NVIDIA H800 GPUs for approximately 2.788 million GPU-hours, at a reported cost of ~.5 million — dramatically lower than comparable frontier models estimated at -100M+."
---

# DeepSeek-V3 Trained for ~\.5M Using FP8 Mixed Precision

DeepSeek-V3 was trained on 14.8 trillion tokens using FP8 mixed-precision training on 2,048 NVIDIA H800 GPUs, consuming approximately 2.788 million GPU-hours at a reported cost of roughly \.5 million. This is dramatically lower than estimated training costs for comparable frontier models (GPT-4 estimated at \-100M+). The FP8 training pipeline — using 8-bit floating point for most matrix multiplications while maintaining critical accumulations in higher precision — was key to this cost efficiency, reducing memory bandwidth and compute requirements without degrading model quality.