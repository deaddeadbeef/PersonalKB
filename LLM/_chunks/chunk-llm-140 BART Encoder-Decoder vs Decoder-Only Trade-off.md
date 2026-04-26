---
tags: [llm, chunk]
source: "[[raw-llm-035]]"
confidence: high
supports:
  - "[[LLM/2018–2019 — Pretrained Language Models/Decoder-Only Models]]"
  - "[[LLM/2018–2019 — Pretrained Language Models/Encoder-Only Models]]"
qna_seeds:
  - "Q: How does BART compare to decoder-only and encoder-only models? A: BART matches BERT on comprehension tasks (SQuAD, GLUE) while significantly outperforming it on generation tasks, and matches GPT on generation while outperforming it on comprehension — validating the encoder-decoder as a unified architecture for both paradigms."
---

# BART Validates Encoder-Decoder as Unified Architecture

BART demonstrated that encoder-decoder models can match encoder-only models (BERT) on comprehension tasks like SQuAD and GLUE, while simultaneously matching or exceeding decoder-only models (GPT) on generation tasks like summarization and dialogue. This validated the encoder-decoder Transformer as a viable unified architecture for both understanding and generation. However, the field ultimately converged on decoder-only models at scale due to their simpler training recipe and strong performance when sufficiently scaled.