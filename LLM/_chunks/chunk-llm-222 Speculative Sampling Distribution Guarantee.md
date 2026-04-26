---
tags: [chunk, llm]
id: "chunk-llm-222"
source: "[[LLM/_raw/raw-llm-056 Speculative Sampling for LLM Decoding]]"
source_loc: "Chunk Candidates"
topic: "speculative sampling preserves target distribution"
claim: "Speculative sampling uses a modified rejection sampling scheme that mathematically guarantees the output distribution is identical to the target model's distribution."
confidence: "verified"
supports: ["[[LLM/2024–2025 — Frontier and Efficiency/Speculative Decoding]]"]
qna_seeds:
  - q: "How does speculative decoding guarantee no quality loss?"
    a: "Each draft token is accepted with probability min(1, p_target/p_draft). Rejected tokens trigger resampling from an adjusted distribution (p_target - p_draft), ensuring the final output distribution exactly matches the target model regardless of draft quality."
  - q: "What happens when the draft model disagrees with the target model?"
    a: "The token is rejected with probability proportional to the gap between draft and target probabilities, and a correction token is sampled from the residual distribution, maintaining exact distributional equivalence."
up: "[[LLM/LLM]]"
---
# Speculative Sampling Preserves the Exact Target Distribution

The key theoretical guarantee of speculative decoding is that it produces outputs with exactly the same probability distribution as the target model — zero quality degradation, not merely low degradation. This is achieved through a modified rejection sampling scheme: each draft token at position i is accepted with probability min(1, p_target(x_i) / p_draft(x_i)), where the probabilities are conditioned on all preceding accepted tokens.

When a token is rejected, the algorithm samples a replacement from the adjusted distribution max(0, p_target - p_draft), normalized appropriately. This correction step ensures that the marginalized output distribution is mathematically identical to what the target model would produce through standard autoregressive decoding. The guarantee holds regardless of draft model quality — a worse draft model simply means lower acceptance rates and fewer tokens per step, not different output quality.
