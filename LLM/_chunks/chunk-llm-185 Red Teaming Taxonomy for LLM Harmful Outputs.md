---
tags: [chunk, llm]
id: "chunk-llm-185"
source: "[[LLM/_raw/raw-llm-047 Red Teaming Language Models to Reduce Harms]]"
source_loc: "What Is This, Chunk Candidates"
topic: "Red teaming attack taxonomy"
claim: "Ganguli et al. cataloged a taxonomy of harmful LLM outputs from red teaming, including categories like discrimination, violence, illegal activities, and manipulation."
confidence: "verified"
supports:
  - "[[LLM/2022 — Alignment and Chat/2022 — Alignment and Chat]]"
qna_seeds:
  - "Q: What categories of harm were identified in LLM red teaming? A: Discrimination and bias, violence and threats, illegal activity instructions, manipulation and deception, sexual content, privacy violations, and self-harm content, among others."
  - "Q: Why is a harm taxonomy important for red teaming? A: It ensures systematic coverage — without a taxonomy, red teamers may cluster around obvious attack types and miss less intuitive but equally dangerous failure modes."
up: "[[LLM/LLM]]"
---

# Red Teaming Taxonomy for LLM Harmful Outputs

Ganguli et al. developed a structured taxonomy of harmful outputs discovered through systematic red teaming of language models. Categories include discrimination and stereotyping, violent and threatening content, instructions for illegal activities, manipulation and social engineering, explicit sexual content, privacy violations, and encouragement of self-harm. The taxonomy ensures comprehensive coverage during safety evaluation — without structured categories, red teamers tend to cluster around obvious attack types. This categorization became a reference for subsequent safety evaluation efforts and informed the development of automated red teaming benchmarks.
