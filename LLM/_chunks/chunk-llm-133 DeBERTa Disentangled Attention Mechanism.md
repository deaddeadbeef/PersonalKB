---
tags: [llm, chunk]
source: "[[raw-llm-034]]"
confidence: high
supports:
  - "[[LLM/2020–2021 — The Scaling Era/Training Infrastructure and Parallelism]]"
  - "[[LLM/2018–2019 — Pretrained Language Models/Encoder-Only Models]]"
qna_seeds:
  - "Q: What is disentangled attention in DeBERTa? A: DeBERTa represents each token with two separate vectors — one for content and one for position — and computes attention using three separate matrices: content-to-content, content-to-position, and position-to-content, rather than combining them into a single embedding."
---

# DeBERTa Disentangled Attention Separates Content and Position

DeBERTa (He et al., 2020) introduced disentangled attention, which represents each token using two separate vectors: one encoding content (semantic meaning) and one encoding relative position. Attention scores are computed as the sum of three interaction terms: content-to-content, content-to-position, and position-to-content. By disentangling these components rather than combining them into a single embedding, the model can learn more nuanced interactions between what a token means and where it appears, improving performance on tasks requiring fine-grained positional reasoning.