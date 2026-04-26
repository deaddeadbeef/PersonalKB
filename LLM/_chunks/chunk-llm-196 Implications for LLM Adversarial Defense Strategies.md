---
tags: [chunk, llm]
id: "chunk-llm-196"
source: "[[LLM/_raw/raw-llm-049 Universal Adversarial Attacks on Aligned LLMs]]"
source_loc: "Why It Matters, Chunk Candidates"
topic: "Adversarial defense for LLMs"
claim: "GCG attacks prompted research into adversarial defenses for LLMs, including perplexity filtering, input preprocessing, and adversarial training against suffix-based attacks."
confidence: "verified"
supports:
  - "[[LLM/2023 — Open Models and Agents/2023 — Open Models and Agents]]"
qna_seeds:
  - "Q: What defenses have been proposed against adversarial suffix attacks? A: Perplexity-based input filtering (detecting gibberish suffixes), input preprocessing/paraphrasing, adversarial training that includes GCG-style attacks in safety data, and output filtering."
  - "Q: Are current defenses effective against GCG-style attacks? A: Partially — perplexity filtering catches obvious gibberish suffixes but can be evaded by optimizing for natural-looking adversarial text. No fully robust defense exists yet."
up: "[[LLM/LLM]]"
---

# Implications for LLM Adversarial Defense Strategies

The GCG attack catalyzed research into adversarial defenses for deployed LLMs. Proposed defenses include perplexity-based input filtering (rejecting prompts with gibberish suffixes that have abnormally high perplexity), input paraphrasing (rewriting prompts to neutralize adversarial perturbations), adversarial training (including GCG-generated attacks in the safety training data), and output classifiers that detect harmful generations post-hoc. However, each defense has limitations: perplexity filters can be evaded by optimizing for natural-looking adversarial text, and adversarial training with specific attacks may not generalize. The cat-and-mouse dynamic between attacks and defenses remains an open research problem.
