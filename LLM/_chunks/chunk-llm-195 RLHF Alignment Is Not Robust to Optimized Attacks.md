---
tags: [chunk, llm]
id: "chunk-llm-195"
source: "[[LLM/_raw/raw-llm-049 Universal Adversarial Attacks on Aligned LLMs]]"
source_loc: "Why It Matters, Chunk Candidates"
topic: "RLHF alignment fragility"
claim: "RLHF-based alignment is fundamentally brittle against gradient-optimized adversarial attacks, indicating that current safety training is a behavioral veneer rather than a deep capability restriction."
confidence: "verified"
supports:
  - "[[LLM/2022 — Alignment and Chat/2022 — Alignment and Chat]]"
  - "[[LLM/2023 — Open Models and Agents/2023 — Open Models and Agents]]"
qna_seeds:
  - "Q: What does GCG reveal about RLHF alignment robustness? A: That RLHF-trained refusal behavior can be bypassed by optimized adversarial inputs, suggesting alignment modifies the model's surface behavior (when to refuse) but does not remove the underlying capability to generate harmful content."
  - "Q: Is this a fundamental limitation of RLHF? A: Possibly — since RLHF trains the model to refuse based on input patterns, adversarial optimization can always find input patterns that evade the learned refusal boundary while still triggering harmful generation."
up: "[[LLM/LLM]]"
---

# RLHF Alignment Is Not Robust to Optimized Attacks

The GCG results revealed that RLHF alignment is a relatively shallow behavioral modification rather than a fundamental capability restriction. Aligned models retain the full ability to generate harmful content — RLHF merely teaches them to refuse when the input matches patterns seen during safety training. Adversarial suffix optimization finds inputs outside the safety training distribution that still trigger harmful generations. This brittleness is a structural property: any alignment method that operates by training refusal patterns on a finite distribution of harmful prompts is vulnerable to optimized out-of-distribution inputs. The finding sparked urgent research into more robust alignment approaches and adversarial defenses.
