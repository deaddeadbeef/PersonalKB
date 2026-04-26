---
tags: [llm, chunk]
source: "[[raw-llm-035]]"
confidence: high
supports:
  - "[[LLM/2018–2019 — Pretrained Language Models/2018–2019 — Pretrained Language Models Overview]]"
qna_seeds:
  - "Q: What noising schemes does BART use for pre-training? A: BART evaluates five corruption strategies: token masking, token deletion, text infilling (replacing spans with a single mask token), sentence permutation, and document rotation. Text infilling with 30% of tokens in Poisson-length spans performed best."
---

# BART Evaluates Five Text Corruption Schemes

BART's pre-training framework supports arbitrary text corruption, and the paper evaluates five schemes: (1) token masking (replacing random tokens with [MASK]), (2) token deletion (removing tokens entirely, forcing the model to decide what's missing), (3) text infilling (replacing variable-length spans with a single [MASK] token, using Poisson-distributed span lengths), (4) sentence permutation (shuffling sentence order), and (5) document rotation (rotating the document at a random token). Text infilling with ~30% of tokens masked in Poisson-length spans (λ=3) yielded the best overall performance across tasks.