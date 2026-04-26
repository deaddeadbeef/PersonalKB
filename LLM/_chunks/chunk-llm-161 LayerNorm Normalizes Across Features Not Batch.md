---
tags: [chunk, llm]
id: "chunk-llm-161"
source: "[[LLM/_raw/raw-llm-041 Layer Normalization]]"
source_loc: "What Is This, Chunk Candidates"
topic: "LayerNorm vs BatchNorm"
claim: "Layer Normalization computes mean and variance across the feature dimension within each example, rather than across the batch dimension as in BatchNorm."
confidence: "verified"
supports:
  - "[[LLM/Architecture Variants/Architecture Variants]]"
qna_seeds:
  - "Q: How does LayerNorm differ from BatchNorm? A: LayerNorm normalizes across features within each training example, while BatchNorm normalizes across the batch for each feature — making LayerNorm independent of batch size."
  - "Q: Why is per-example normalization important? A: It avoids dependence on batch statistics, which are unreliable for variable-length sequences and small batches common in NLP."
up: "[[LLM/LLM]]"
---

# LayerNorm Normalizes Across Features Not Batch

Layer Normalization computes the mean and variance across all features (hidden dimensions) within a single training example, then re-centers and re-scales the activations. This contrasts with Batch Normalization, which computes statistics across the batch dimension for each feature. Because LayerNorm operates entirely within each example, it is independent of batch size and naturally handles variable-length sequences where batch statistics would be unstable. The original 2016 paper by Ba et al. showed that LayerNorm stabilizes hidden-state dynamics in recurrent networks and accelerates training convergence.
