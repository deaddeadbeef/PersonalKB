---
tags: [chunk, llm]
id: "chunk-llm-223"
source: "[[LLM/_raw/raw-llm-056 Speculative Sampling for LLM Decoding]]"
source_loc: "Chunk Candidates"
topic: "speculative decoding speedup analysis"
claim: "Speculative decoding speedup depends on draft model acceptance rate, which is governed by the alignment between draft and target distributions."
confidence: "verified"
supports: ["[[LLM/2024–2025 — Frontier and Efficiency/Speculative Decoding]]", "[[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]"]
qna_seeds:
  - q: "What determines the speedup of speculative decoding?"
    a: "The expected tokens per verification step is 1/(1-α) where α is the mean acceptance rate. With α=0.7 and K=5 draft tokens, the expected accepted tokens per step is approximately 3.3, yielding 2-3× wall-clock speedup after accounting for draft model overhead."
  - q: "What properties should a good draft model have?"
    a: "A good draft model closely approximates the target's distribution (high acceptance rate) while being small enough that K draft forward passes cost much less than one target forward pass. Typical size ratios are 10-100× smaller than the target."
up: "[[LLM/LLM]]"
---
# Speculative Decoding Speedup Depends on Draft-Target Alignment

The practical speedup of speculative decoding is governed by the acceptance rate α — the probability that a draft token matches the target model's distribution well enough to be accepted. The expected number of tokens generated per verification step is approximately 1/(1-α), meaning an acceptance rate of 0.7 yields ~3.3 tokens per step, and 0.8 yields ~5 tokens per step.

The net wall-clock speedup must account for the cost of draft generation. If the draft model is 100× smaller than the target, K draft steps cost roughly K/100 of one target step, making draft overhead negligible. In practice, speculative decoding achieves 2–3× speedup for well-matched draft-target pairs, with the exact factor depending on task difficulty (easier tasks have higher acceptance rates), draft model quality, and the number of speculative tokens K. Production systems typically use K=4–8.
