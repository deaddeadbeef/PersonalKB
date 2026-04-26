---
tags: [chunk, llm]
id: "chunk-llm-218"
source: "[[LLM/_raw/raw-llm-055 GQA Training Generalized Multi-Query Transformer Models]]"
source_loc: "Chunk Candidates"
topic: "GQA uptraining recipe"
claim: "GQA provides an uptraining recipe to convert existing MHA checkpoints to GQA by mean-pooling KV heads within groups and fine-tuning for a small fraction of original training compute."
confidence: "verified"
supports: ["[[LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants]]"]
qna_seeds:
  - q: "How does the GQA uptraining recipe convert MHA to GQA?"
    a: "KV head weights within each group are initialized by mean-pooling the original MHA KV heads, then the model is fine-tuned for approximately 5% of the original pre-training compute to recover quality."
  - q: "Why is uptraining important for GQA adoption?"
    a: "It allows organizations to convert existing expensive MHA checkpoints to GQA without retraining from scratch, making GQA adoption a fine-tuning cost rather than a pre-training cost."
up: "[[LLM/LLM]]"
---
# GQA Uptraining Converts MHA Checkpoints with Minimal Compute

A key practical contribution of the GQA paper is the uptraining recipe for converting existing Multi-Head Attention checkpoints to Grouped-Query Attention. The process initializes each GQA key-value group by mean-pooling the corresponding MHA key-value heads, then fine-tunes the model for approximately 5% of the original pre-training compute (α proportion of the original training steps).

This recipe is crucial for adoption because pre-training large language models costs millions of dollars. Rather than requiring organizations to retrain from scratch with GQA architecture, uptraining allows converting an existing MHA checkpoint — preserving the investment in pre-training — while gaining GQA's inference speed benefits. The LLaMA 2 70B model used this approach, converting from an MHA base to GQA with 8 KV groups.
