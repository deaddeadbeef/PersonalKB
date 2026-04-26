---
tags: [chunk, llm]
id: "chunk-llm-165"
source: "[[LLM/_raw/raw-llm-042 ALiBi Train Short Test Long]]"
source_loc: "What Is This, Chunk Candidates"
topic: "ALiBi linear bias mechanism"
claim: "ALiBi replaces position embeddings with a linear bias subtracted from attention scores, penalizing each key-query pair proportionally to their distance."
confidence: "verified"
supports:
  - "[[LLM/Architecture Variants/Architecture Variants]]"
qna_seeds:
  - "Q: How does ALiBi encode position information? A: It adds a head-specific linear bias to attention scores that penalizes distant key-query pairs — closer tokens receive higher attention by default, with no learned position parameters."
  - "Q: What are the slopes in ALiBi? A: Each attention head gets a different fixed slope (geometric sequence), so some heads attend more locally and others more broadly, providing multi-scale position sensitivity."
up: "[[LLM/LLM]]"
---

# ALiBi Adds Linear Bias Distance Penalty to Attention

ALiBi (Attention with Linear Biases) encodes positional information by adding a static, linear penalty to attention scores based on the distance between query and key positions. Each attention head is assigned a different fixed slope from a geometric sequence, so heads naturally specialize in different attention ranges — some attend locally, others more broadly. This mechanism requires no additional learned parameters and adds negligible computation. The approach is a drop-in replacement for sinusoidal or learned absolute position embeddings.
