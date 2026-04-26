---
tags: [chunk, llm]
id: "chunk-llm-168"
source: "[[LLM/_raw/raw-llm-042 ALiBi Train Short Test Long]]"
source_loc: "Chunk Candidates"
topic: "Position encoding comparison"
claim: "The Transformer position encoding design space includes sinusoidal, learned absolute, relative (T5-style), rotary (RoPE), and linear bias (ALiBi) approaches, each with different extrapolation and efficiency trade-offs."
confidence: "verified"
supports:
  - "[[LLM/Architecture Variants/Architecture Variants]]"
  - "[[LLM/2017 — The Transformer/2017 — The Transformer]]"
qna_seeds:
  - "Q: What are the main position encoding approaches for Transformers? A: Sinusoidal (fixed, original Transformer), learned absolute (GPT-2/BERT), relative (T5), rotary/RoPE (LLaMA, most modern LLMs), and linear bias/ALiBi."
  - "Q: Which position encoding is most popular in modern LLMs? A: RoPE dominates in current models (LLaMA, Mistral, Qwen) due to good extrapolation with NTK-aware scaling, though ALiBi remains used in models like BLOOM and MPT."
up: "[[LLM/LLM]]"
---

# Position Encoding Design Space for Transformers

Transformers require explicit position information since self-attention is permutation-equivariant. The design space has evolved from sinusoidal embeddings (original Transformer) and learned absolute embeddings (GPT-2, BERT) to relative position approaches. T5 introduced learnable relative biases, RoPE applied rotary matrices to encode relative position in the attention dot product, and ALiBi used static linear biases. Each approach has different strengths: RoPE and ALiBi both enable length extrapolation, but RoPE has become dominant in modern LLMs (LLaMA, Mistral, Qwen) due to strong performance with NTK-aware scaling techniques, while ALiBi powers BLOOM and MPT.
