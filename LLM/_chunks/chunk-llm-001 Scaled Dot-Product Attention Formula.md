---
tags: [chunk, llm]
id: "chunk-llm-001"
source: "[[LLM/_raw/raw-llm-001 Attention Is All You Need]]"
source_loc: "Section 3.2.1"
topic: "attention mechanism"
claim: "Scaled dot-product attention computes softmax(QK^T/√d_k)V"
confidence: "verified"
supports: ["[[LLM/Foundations/Attention Mechanism]]"]
up: "[[LLM/LLM]]"
---

# Scaled Dot-Product Attention Formula

## Context

The core computation in the Transformer architecture is scaled dot-product attention, defined as Attention(Q, K, V) = softmax(QK^T / √d_k)V. The query (Q) and key (K) matrices are multiplied to produce attention scores, which are then scaled by the square root of the key dimension d_k before applying softmax to obtain attention weights. These weights are used to compute a weighted sum of the value (V) vectors.

The scaling factor √d_k is critical: without it, for large d_k the dot products grow large in magnitude, pushing the softmax into regions with extremely small gradients. This scaling ensures stable training regardless of the dimensionality of the key vectors.

## Why It Matters

This formula is the atomic unit of computation in every modern Transformer-based model. Understanding why the scaling factor exists (preventing softmax saturation) and how Q, K, V interact is prerequisite knowledge for grasping multi-head attention, sparse attention variants, and efficient attention approximations like FlashAttention.

## QnA Seeds
- Q: Why is the dot product scaled by √d_k in the attention formula?
  A: Without scaling, large d_k values cause dot products to grow large, pushing softmax into saturated regions with vanishing gradients. Dividing by √d_k keeps the variance of the dot products at approximately 1, ensuring stable gradient flow.
- Q: What are Q, K, and V in the attention formula, and where do they come from?
  A: Q (queries), K (keys), and V (values) are linear projections of the input embeddings. The model learns separate weight matrices W_Q, W_K, and W_V that project the input into these three roles, enabling the attention mechanism to determine which positions to attend to (via Q·K similarity) and what information to aggregate (via V).
