---
tags: [llm, chunk]
source: "[[raw-llm-032]]"
confidence: high
supports:
  - "[[LLM/2020–2021 — The Scaling Era/Scaling Laws]]"
  - "[[LLM/2018–2019 — Pretrained Language Models/GPT and Decoder-Only Lineage]]"
qna_seeds:
  - "Q: How did GPT-2 demonstrate scaling effects? A: GPT-2 was released in four sizes (117M, 345M, 762M, 1.5B parameters), and performance on every benchmark improved log-linearly with model size — providing early empirical evidence for the scaling hypothesis."
---

# GPT-2 Scaling from 117M to 1.5B Showed Log-Linear Improvement

GPT-2 was released in four model sizes: 117M, 345M, 762M, and 1.5B parameters. Performance on every evaluated benchmark improved log-linearly with parameter count, with the largest model achieving the best zero-shot results on 7 out of 8 language modeling datasets. This systematic scaling study provided early empirical evidence for the scaling hypothesis — that simply making language models larger yields predictable performance gains — later formalized by Kaplan et al.'s scaling laws.