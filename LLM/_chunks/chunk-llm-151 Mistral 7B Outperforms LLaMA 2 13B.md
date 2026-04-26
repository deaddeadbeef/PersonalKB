---
tags: [llm, chunk]
source: "[[raw-llm-038]]"
confidence: high
supports:
  - "[[LLM/2023 — Open Models and Agents/Open-Weight Model Ecosystem]]"
qna_seeds:
  - "Q: How does Mistral 7B compare to LLaMA 2? A: Mistral 7B (7.3B parameters) outperforms LLaMA 2 13B on all evaluated benchmarks and matches LLaMA 1 34B on many, demonstrating that careful architecture and training at 7B scale can match much larger models."
---

# Mistral 7B Outperforms LLaMA 2 13B on All Benchmarks

Despite having only 7.3 billion parameters, Mistral 7B outperformed LLaMA 2 13B on all evaluated benchmarks including commonsense reasoning, reading comprehension, math, and code generation. It also matched or exceeded LLaMA 1 34B on many tasks. This demonstrated that careful architectural choices (sliding window attention, GQA) and training optimization at a smaller scale can match models with nearly 2× or 5× more parameters, making the efficiency-per-parameter ratio as important as raw scale.