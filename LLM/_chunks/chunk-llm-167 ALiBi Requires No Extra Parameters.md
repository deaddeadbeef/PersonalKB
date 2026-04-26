---
tags: [chunk, llm]
id: "chunk-llm-167"
source: "[[LLM/_raw/raw-llm-042 ALiBi Train Short Test Long]]"
source_loc: "Why It Matters"
topic: "ALiBi simplicity"
claim: "ALiBi introduces no extra learned parameters and is trivial to implement, requiring only a fixed bias matrix added to attention logits."
confidence: "verified"
supports:
  - "[[LLM/Architecture Variants/Architecture Variants]]"
qna_seeds:
  - "Q: Does ALiBi add parameters to the model? A: No — ALiBi uses fixed, non-learned slopes and a static distance matrix, adding zero trainable parameters compared to learned position embeddings."
  - "Q: How is ALiBi implemented? A: A pre-computed bias matrix (distances times head-specific slopes) is subtracted from attention logits before softmax. It requires only a few lines of code."
up: "[[LLM/LLM]]"
---

# ALiBi Requires No Extra Parameters

ALiBi's design is notable for its extreme simplicity. Unlike learned position embeddings (which add a full embedding table) or RoPE (which applies rotations requiring trigonometric computation), ALiBi uses only a pre-computed static bias matrix derived from fixed slopes and token distances. This adds exactly zero trainable parameters to the model. Implementation requires just adding the bias matrix to attention logits before the softmax, making it trivial to integrate into any Transformer codebase.
