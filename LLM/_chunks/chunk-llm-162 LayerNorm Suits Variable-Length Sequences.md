---
tags: [chunk, llm]
id: "chunk-llm-162"
source: "[[LLM/_raw/raw-llm-041 Layer Normalization]]"
source_loc: "Why It Matters, Chunk Candidates"
topic: "LayerNorm for sequences"
claim: "LayerNorm's batch-size independence makes it essential for variable-length sequence models where batch statistics are unreliable."
confidence: "verified"
supports:
  - "[[LLM/Architecture Variants/Architecture Variants]]"
qna_seeds:
  - "Q: Why is LayerNorm preferred over BatchNorm for sequence models? A: Sequences vary in length within a batch, making batch-level statistics unreliable; LayerNorm normalizes per-example so length variation does not affect normalization quality."
  - "Q: What practical benefit does batch-size independence give? A: Models can train with any batch size and sequence length without normalization degradation, which is critical for LLM training on heterogeneous data."
up: "[[LLM/LLM]]"
---

# LayerNorm Suits Variable-Length Sequences

LayerNorm's invariance to batch composition makes it the natural normalization choice for Transformer-based language models. In NLP, batches contain sequences of different lengths, and the padding or truncation needed to form uniform batches makes batch-level statistics unreliable. LayerNorm sidesteps this entirely by computing statistics per example. This property is why virtually every Transformer architecture — from the original 2017 paper onward — adopted LayerNorm rather than BatchNorm.
