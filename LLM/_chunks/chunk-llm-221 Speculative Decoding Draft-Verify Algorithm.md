---
tags: [chunk, llm]
id: "chunk-llm-221"
source: "[[LLM/_raw/raw-llm-056 Speculative Sampling for LLM Decoding]]"
source_loc: "What Is This, Chunk Candidates"
topic: "speculative decoding draft-verify algorithm"
claim: "Speculative decoding uses a small draft model to propose multiple tokens, then the large target model verifies them in a single parallel forward pass."
confidence: "verified"
supports: ["[[LLM/2024–2025 — Frontier and Efficiency/Speculative Decoding]]"]
qna_seeds:
  - q: "How does the draft-then-verify algorithm work in speculative decoding?"
    a: "A small, fast draft model autoregressively generates K candidate tokens, then the large target model runs a single forward pass over the entire draft sequence to compute probabilities for all K positions simultaneously and accept or reject each token."
  - q: "Why can the target model verify K tokens in one forward pass?"
    a: "The target model processes the draft tokens using standard causal attention (like processing a prompt), computing the probability of each token given all preceding tokens in parallel — the same cost as generating one token in the prefill phase."
up: "[[LLM/LLM]]"
---
# Speculative Decoding Uses Draft-Then-Verify for Multi-Token Generation

Speculative decoding breaks the one-token-per-forward-pass bottleneck of autoregressive generation by using a two-phase approach. In the draft phase, a small and fast model (e.g., a 68M parameter model for a 70B target) autoregressively generates K candidate tokens. In the verify phase, the large target model processes the entire draft sequence in a single forward pass, computing its probability distribution at each position.

The verification step is computationally equivalent to a prefill operation on K tokens — far cheaper than K separate autoregressive decoding steps with the large model. If all K draft tokens are accepted, the system generates K+1 tokens (K verified plus one new token from the target model's distribution) for the cost of one large-model forward pass plus K small-model passes. This asymmetry between draft and verification cost is the source of the speedup.
