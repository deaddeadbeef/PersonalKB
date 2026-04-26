---
tags: [chunk, llm]
id: "chunk-llm-215"
source: "[[LLM/_raw/raw-llm-054 Fast Transformer Decoding One Write-Head MQA]]"
source_loc: "Chunk Candidates"
topic: "MQA quality-speed tradeoff"
claim: "MQA achieves large inference speedups with modest quality degradation, leading to adoption in PaLM, Falcon, and other production models."
confidence: "verified"
supports: ["[[LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants]]"]
qna_seeds:
  - q: "Which major models adopted MQA?"
    a: "Google's PaLM (540B), Technology Innovation Institute's Falcon (40B/180B), and StarCoder all used MQA to achieve faster inference without significant quality regression."
  - q: "What is the typical quality-speed tradeoff with MQA?"
    a: "MQA typically shows less than 1% accuracy degradation on standard benchmarks while providing inference throughput improvements of 2× or more during autoregressive generation, particularly at long sequence lengths."
up: "[[LLM/LLM]]"
---
# MQA Achieves Major Speedups with Modest Quality Cost

Multi-Query Attention delivers inference speedups of 2× or more during autoregressive decoding, with quality degradation typically under 1% on standard language modeling and downstream benchmarks. The speedup scales with sequence length — longer sequences mean larger KV caches, and MQA's reduction factor has proportionally greater impact on memory bandwidth consumption.

This favorable quality-speed tradeoff led to MQA adoption in several high-profile production models: Google's PaLM (540B parameters), Technology Innovation Institute's Falcon (40B and 180B), and StarCoder for code generation. These deployments validated MQA's viability at scale and established the principle that KV cache optimization is a first-class architectural decision, not just a post-hoc inference trick. MQA laid the foundation for the later development of Grouped-Query Attention (GQA).
