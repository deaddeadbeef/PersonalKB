---
tags: [llm, chunk]
source: "[[raw-llm-032]]"
confidence: high
supports:
  - "[[LLM/2018–2019 — Pretrained Language Models/GPT and Decoder-Only Lineage]]"
  - "[[LLM/2020–2021 — The Scaling Era/In-Context Learning Mechanisms]]"
qna_seeds:
  - "Q: What was GPT-2's key contribution to task transfer? A: GPT-2 demonstrated that a 1.5B parameter language model could perform tasks zero-shot — without any fine-tuning or gradient updates — by simply conditioning on natural language descriptions of the task."
---

# GPT-2 Demonstrated Zero-Shot Task Transfer

GPT-2 (Radford et al., 2019) showed that a language model scaled to 1.5 billion parameters could perform downstream tasks zero-shot, without any fine-tuning or explicit supervision. By conditioning generation on natural language task descriptions (e.g., "TL;DR" for summarization), the model achieved competitive results on reading comprehension, translation, and summarization benchmarks. This was the conceptual leap toward in-context learning that would be fully realized in GPT-3.