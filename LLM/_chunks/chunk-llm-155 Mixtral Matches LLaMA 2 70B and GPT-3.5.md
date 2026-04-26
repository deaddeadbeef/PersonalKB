---
tags: [llm, chunk]
source: "[[raw-llm-039]]"
confidence: high
supports:
  - "[[LLM/2023 — Open Models and Agents/Open-Weight Model Ecosystem]]"
  - "[[LLM/2020–2021 — The Scaling Era/Mixture-of-Experts Models]]"
qna_seeds:
  - "Q: How does Mixtral compare to LLaMA 2 70B and GPT-3.5? A: Mixtral 8x7B matches or exceeds LLaMA 2 70B on most benchmarks and matches GPT-3.5 on reasoning and code tasks, while using 6× fewer active parameters than LLaMA 2 70B during inference."
---

# Mixtral Matches LLaMA 2 70B and GPT-3.5 Quality

Mixtral 8x7B matches or exceeds LLaMA 2 70B on most evaluated benchmarks including MMLU, HellaSwag, ARC, and GSM8K, while also matching GPT-3.5 Turbo on reasoning and code generation tasks. It achieves this with only 12.9B active parameters per token — roughly 6× fewer than LLaMA 2 70B's dense computation. This demonstrated that open-weight sparse MoE models could compete with both the largest open dense models and proprietary API models at a fraction of the serving cost.