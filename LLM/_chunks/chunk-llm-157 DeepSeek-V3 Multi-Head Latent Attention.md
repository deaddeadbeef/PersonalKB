---
tags: [llm, chunk]
source: "[[raw-llm-040]]"
confidence: high
supports:
  - "[[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]"
  - "[[LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants]]"
qna_seeds:
  - "Q: What is Multi-head Latent Attention (MLA) in DeepSeek-V3? A: MLA compresses key-value representations into a low-dimensional latent space before storing them in the KV cache, dramatically reducing cache memory per token while preserving full multi-head attention expressiveness through learned up-projections at query time."
---

# DeepSeek-V3 Uses Multi-Head Latent Attention for KV Compression

DeepSeek-V3 introduces Multi-head Latent Attention (MLA), which compresses key-value representations into a low-dimensional latent vector before caching. Rather than storing full-dimensional K and V tensors for each attention head, MLA stores a single compressed latent per token and reconstructs the full KV representations via learned up-projection matrices at attention computation time. This reduces KV cache memory by a large factor compared to standard multi-head attention, enabling longer contexts and higher batch sizes during serving while maintaining the expressiveness of multi-head attention.