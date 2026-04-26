---
tags: [chunk, llm]
id: "chunk-llm-193"
source: "[[LLM/_raw/raw-llm-049 Universal Adversarial Attacks on Aligned LLMs]]"
source_loc: "What Is This, Chunk Candidates"
topic: "GCG attack algorithm"
claim: "The Greedy Coordinate Gradient (GCG) method automatically optimizes adversarial suffixes — gibberish token sequences appended to prompts — that cause aligned LLMs to comply with harmful requests."
confidence: "verified"
supports:
  - "[[LLM/2023 — Open Models and Agents/2023 — Open Models and Agents]]"
qna_seeds:
  - "Q: What is the GCG attack? A: An algorithm that uses gradient-based optimization to find adversarial suffixes (token sequences) that, when appended to a harmful prompt, cause aligned models to generate harmful responses instead of refusing."
  - "Q: How does GCG optimize the suffix? A: It computes gradients with respect to token embeddings, then greedily substitutes tokens at each position to minimize the loss on the target harmful completion, iterating until a successful suffix is found."
up: "[[LLM/LLM]]"
---

# GCG Generates Adversarial Suffixes to Bypass Alignment

Zou et al. introduced the Greedy Coordinate Gradient (GCG) method for automatically discovering adversarial suffixes that bypass LLM safety alignment. The algorithm appends a sequence of optimizable tokens to a harmful prompt, then uses gradient information with respect to token embeddings to iteratively substitute tokens at each position, greedily minimizing the loss on a target harmful completion. The resulting suffixes are typically nonsensical to humans (e.g., random-looking token strings) but reliably cause aligned models to comply with harmful requests that they would normally refuse. GCG demonstrated that alignment can be systematically circumvented through optimization.
