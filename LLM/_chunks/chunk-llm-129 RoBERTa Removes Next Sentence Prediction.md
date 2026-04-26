---
tags: [llm, chunk]
source: "[[raw-llm-033]]"
confidence: high
supports:
  - "[[LLM/2018–2019 — Pretrained Language Models/BERT and Encoder Lineage]]"
  - "[[LLM/2018–2019 — Pretrained Language Models/Encoder-Only Models]]"
qna_seeds:
  - "Q: What did RoBERTa find about BERT's Next Sentence Prediction objective? A: RoBERTa showed that removing BERT's Next Sentence Prediction (NSP) loss either matched or improved downstream performance, demonstrating NSP was unnecessary and potentially harmful to representation quality."
---

# RoBERTa Proved BERT's Next Sentence Prediction Was Unnecessary

RoBERTa (Liu et al., 2019) systematically ablated BERT's training objectives and found that removing the Next Sentence Prediction (NSP) loss either matched or improved downstream task performance. Training with full-length sequences from a single document without NSP yielded the best results. This finding changed the default recipe for encoder pre-training — subsequent models like ALBERT and DeBERTa dropped NSP, and the result demonstrated that careful ablation of training choices can matter as much as architectural innovation.