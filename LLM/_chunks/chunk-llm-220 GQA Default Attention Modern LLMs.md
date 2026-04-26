---
tags: [chunk, llm]
id: "chunk-llm-220"
source: "[[LLM/_raw/raw-llm-055 GQA Training Generalized Multi-Query Transformer Models]]"
source_loc: "Why It Matters"
topic: "GQA default attention modern LLMs"
claim: "GQA was adopted as the default attention mechanism by LLaMA 2 70B, Mistral, Mixtral, and most subsequent large language models."
confidence: "verified"
supports: ["[[LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants]]"]
qna_seeds:
  - q: "Which major models use GQA as their default attention mechanism?"
    a: "LLaMA 2 70B, LLaMA 3 (all sizes), Mistral 7B, Mixtral 8x7B, Gemma, and most other models released after mid-2023 use GQA."
  - q: "Why did GQA become the industry default so quickly?"
    a: "The combination of Pareto-optimal quality-speed tradeoff, simple uptraining recipe for existing checkpoints, and validated production deployments at Meta and Google made GQA the obvious choice for any new model architecture."
up: "[[LLM/LLM]]"
---
# GQA Became the Default Attention for Modern LLMs

Following its introduction, Grouped-Query Attention rapidly became the standard attention configuration for large language models. LLaMA 2 70B was the first major model to adopt GQA, and the entire LLaMA 3 family (8B, 70B, 405B) followed. Mistral 7B, Mixtral 8x7B, Google's Gemma, and virtually every significant model released after mid-2023 uses GQA rather than full MHA or MQA.

GQA's rapid standardization resulted from multiple converging factors: the Pareto-optimal speed-quality tradeoff left little reason to choose alternatives, the uptraining recipe minimized adoption cost for existing checkpoints, and early validation by Meta (LLaMA 2) and Google (T5 experiments) gave the community confidence. Today, choosing GQA over MHA is considered a baseline architectural decision rather than an optimization — defaulting to full MHA in a new architecture would require justification.
