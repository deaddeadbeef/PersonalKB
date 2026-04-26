---
tags: [llm, chunk]
source: "[[raw-llm-033]]"
confidence: high
supports:
  - "[[LLM/2018–2019 — Pretrained Language Models/Knowledge and Reasoning Benchmarks]]"
  - "[[LLM/2018–2019 — Pretrained Language Models/BERT and Encoder Lineage]]"
qna_seeds:
  - "Q: How did RoBERTa perform compared to XLNet? A: RoBERTa matched or exceeded XLNet on GLUE, SQuAD 2.0, and RACE benchmarks using BERT's exact architecture with no modifications — only improved training methodology."
---

# RoBERTa Achieved SOTA on GLUE and SQuAD Without Architectural Changes

Using the exact same Transformer encoder architecture as BERT (no architectural modifications), RoBERTa achieved state-of-the-art results on GLUE (88.5), SQuAD 1.1/2.0, and RACE, matching or exceeding XLNet which had introduced a more complex permutation-based training objective. This was a powerful demonstration that training recipe optimization — data, compute, and hyperparameter tuning — can be more impactful than novel architecture design.