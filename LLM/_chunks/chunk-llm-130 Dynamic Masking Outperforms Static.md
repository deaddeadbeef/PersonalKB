---
tags: [llm, chunk]
source: "[[raw-llm-033]]"
confidence: high
supports:
  - "[[LLM/2018–2019 — Pretrained Language Models/BERT and Encoder Lineage]]"
qna_seeds:
  - "Q: What is dynamic masking and why is it better than static masking? A: Dynamic masking generates a new random mask pattern each time a sequence is fed to the model during training, rather than using a fixed mask determined during preprocessing. RoBERTa showed this prevents the model from memorizing specific mask patterns and slightly improves performance."
---

# Dynamic Masking Outperforms Static Masking in MLM

BERT's original implementation used static masking — mask patterns were determined once during data preprocessing and reused across epochs. RoBERTa showed that dynamic masking, where a new random mask is generated each time a sequence is presented to the model, produces comparable or slightly better results. Dynamic masking prevents the model from seeing the same masked version of each sentence repeatedly, effectively increasing training data diversity without collecting additional text.