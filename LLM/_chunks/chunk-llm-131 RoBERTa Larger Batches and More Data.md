---
tags: [llm, chunk]
source: "[[raw-llm-033]]"
confidence: high
supports:
  - "[[LLM/2018–2019 — Pretrained Language Models/BERT and Encoder Lineage]]"
  - "[[LLM/2022 — Alignment and Chat/Compute Data and Parameter Trade-offs]]"
qna_seeds:
  - "Q: What training methodology changes did RoBERTa make over BERT? A: RoBERTa trained with 8× larger mini-batches (8K sequences), 10× more data (160 GB vs. 16 GB), and for significantly more steps, demonstrating that BERT had been substantially under-trained."
---

# RoBERTa Showed BERT Was Substantially Under-Trained

RoBERTa demonstrated that BERT's original training was significantly under-optimized by scaling up three axes: batch size (from 256 to 8K sequences), data volume (from ~16 GB to ~160 GB across BookCorpus, CC-News, OpenWebText, and Stories), and training duration (substantially more gradient steps). Each axis independently improved performance. This established that training methodology — how long, on how much data, with what batch size — matters as much as model architecture for final quality.