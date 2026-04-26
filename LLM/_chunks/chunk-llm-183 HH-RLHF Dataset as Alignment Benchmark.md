---
tags: [chunk, llm]
id: "chunk-llm-183"
source: "[[LLM/_raw/raw-llm-046 Training a Helpful and Harmless Assistant with RLHF]]"
source_loc: "Why It Matters, Chunk Candidates"
topic: "HH-RLHF dataset"
claim: "The HH-RLHF dataset of human preference comparisons for helpfulness and harmlessness became a standard benchmark for alignment research and reward model training."
confidence: "verified"
supports:
  - "[[LLM/2022 — Alignment and Chat/2022 — Alignment and Chat]]"
qna_seeds:
  - "Q: What is the HH-RLHF dataset? A: A public dataset of human preference comparisons where annotators chose between model response pairs along helpfulness and harmlessness dimensions, released by Anthropic."
  - "Q: How is the HH-RLHF dataset used? A: As a standard benchmark for training and evaluating reward models, and for testing new alignment algorithms like DPO, RLAIF, and Constitutional AI."
up: "[[LLM/LLM]]"
---

# HH-RLHF Dataset as Alignment Benchmark

Anthropic released the HH-RLHF (Helpful and Harmless) dataset, containing thousands of human preference comparisons between model response pairs. Each comparison is labeled along helpfulness and harmlessness dimensions, providing separate training signals for each objective. The dataset became a standard benchmark in alignment research — used to train and evaluate reward models, test new alignment algorithms (DPO, RLAIF, Constitutional AI), and compare different approaches to the helpfulness-harmlessness trade-off. Its public availability accelerated open-source alignment research significantly.
