---
tags: [chunk, llm]
id: "chunk-llm-018"
source: "[[LLM/_raw/raw-llm-005 Training Compute-Optimal LLMs (Chinchilla)]]"
source_loc: "Section 4, Table 2"
topic: "scaling laws"
claim: "Chinchilla (70B, 1.4T tokens) outperformed Gopher (280B, 300B tokens) with 4× fewer parameters, proving most models were undertrained on data"
confidence: "verified"
supports: ["[[LLM/Pretraining/Scaling Laws]]"]
up: "[[LLM/LLM]]"
---

# Chinchilla Outperforms Gopher with 4× Fewer Parameters

## Context

The most dramatic empirical result in the Chinchilla paper was the head-to-head comparison: Chinchilla (70B parameters, 1.4T training tokens) outperformed Gopher (280B parameters, 300B training tokens) on the majority of evaluation benchmarks, despite having only one-quarter the parameters. Both models used approximately the same total compute budget. The difference was entirely in allocation: Chinchilla invested in data where Gopher invested in parameters.

Gopher followed the Kaplan scaling recommendations, which suggested scaling parameters faster than data. By instead following compute-optimal ratios, Chinchilla achieved lower language modeling loss and higher downstream accuracy. The improvement was consistent across MMLU, reading comprehension, common sense reasoning, and language modeling benchmarks, with Chinchilla matching or exceeding Gopher on 70%+ of tasks.

## Why It Matters

This result was a paradigm shift. It proved that the prevailing "bigger model = better model" strategy was suboptimal — the industry had been systematically under-investing in training data. The practical implications were enormous: a model with 4× fewer parameters is 4× cheaper to serve at inference time, while being equally or more capable. This finding directly inspired the LLaMA training philosophy and reshaped how every major lab allocated training budgets.

## QnA Seeds
- Q: How could a 70B model outperform a 280B model that used the same compute?
  A: With the same compute budget, Chinchilla allocated more FLOPs to processing training data (1.4T tokens vs 300B), while Gopher allocated more FLOPs to forward/backward passes through a larger model. The 280B Gopher had more capacity but was starved for data — it couldn't fully utilize its parameters. Chinchilla's smaller model was fully trained, meaning its parameters were efficiently utilized.
- Q: What does "undertrained" mean in the context of large language models?
  A: A model is undertrained when it has not seen enough training data to fully utilize its parameter capacity. The model's representations are underdeveloped relative to what the architecture could support with more data. Symptoms include: (1) training loss hasn't plateaued, (2) a smaller model trained on more data outperforms it, and (3) the token-to-parameter ratio is well below the compute-optimal 20:1.
