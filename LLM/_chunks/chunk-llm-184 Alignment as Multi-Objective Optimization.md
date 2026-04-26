---
tags: [chunk, llm]
id: "chunk-llm-184"
source: "[[LLM/_raw/raw-llm-046 Training a Helpful and Harmless Assistant with RLHF]]"
source_loc: "Why It Matters"
topic: "Multi-objective alignment"
claim: "Bai et al. framed LLM alignment as a multi-objective optimization problem, where helpfulness, harmlessness, and honesty must be balanced rather than optimized independently."
confidence: "verified"
supports:
  - "[[LLM/2022 — Alignment and Chat/2022 — Alignment and Chat]]"
qna_seeds:
  - "Q: Why is alignment framed as multi-objective? A: Because optimizing a single objective (e.g., helpfulness) can degrade others (e.g., harmlessness), so alignment requires finding Pareto-optimal trade-offs across multiple desirable properties."
  - "Q: What are the typical alignment objectives? A: Helpfulness (answering user queries well), harmlessness (avoiding dangerous or toxic outputs), and honesty (providing accurate information and expressing uncertainty)."
up: "[[LLM/LLM]]"
---

# Alignment as Multi-Objective Optimization

The paper's most influential contribution may be its framing of alignment as an inherently multi-objective problem. Rather than treating safety as a constraint or helpfulness as the sole objective, Bai et al. showed that helpfulness, harmlessness, and honesty are distinct axes with complex interactions. Optimizing one can degrade another, and the optimal balance depends on the deployment context. This multi-objective framing influenced Anthropic's subsequent Constitutional AI work and became the standard conceptual framework for alignment research, replacing simpler notions of making the model safe with a richer understanding of competing desiderata.
