---
tags: [chunk, llm]
id: "chunk-llm-002"
source: "[[LLM/_raw/raw-llm-001 Attention Is All You Need]]"
source_loc: "Section 3.2.2"
topic: "attention mechanism"
claim: "Multi-head attention runs h parallel attention operations with different learned projections"
confidence: "verified"
supports: ["[[LLM/Foundations/Attention Mechanism]]"]
up: "[[LLM/LLM]]"
---

# Multi-Head Attention Parallel Projections

## Context

Rather than performing a single attention function with d_model-dimensional keys, values, and queries, multi-head attention projects Q, K, and V h times with different learned linear projections into d_k, d_k, and d_v dimensions respectively. Attention is computed in parallel on each of these h projected versions, producing h output vectors that are concatenated and projected once more to produce the final output.

In the original Transformer, h = 8 heads with d_k = d_v = d_model/h = 64. This means each head operates on a 64-dimensional subspace. Because the projections are learned independently, different heads can specialize in different types of relationships — some may capture positional adjacency, others syntactic dependencies, and others semantic similarity.

## Why It Matters

Multi-head attention is what gives Transformers their representational richness. A single attention head can only compute one attention pattern per position; multiple heads allow the model to jointly attend to information from different representation subspaces at different positions, which is essential for capturing the multi-faceted nature of language.

## QnA Seeds
- Q: Why use multiple attention heads instead of one large attention operation?
  A: A single head computes one attention distribution per position, limiting what relationships it can capture. Multiple heads allow the model to attend to different aspects simultaneously — for example, one head may track syntactic structure while another captures coreference. The total computation cost is similar because each head operates on a reduced dimension (d_model/h).
- Q: How does the output of multi-head attention combine information from all heads?
  A: The outputs from all h heads are concatenated into a single vector of dimension h × d_v = d_model, then multiplied by a learned output projection matrix W_O to produce the final d_model-dimensional output. This projection allows the model to learn how to best combine the information captured by different heads.
