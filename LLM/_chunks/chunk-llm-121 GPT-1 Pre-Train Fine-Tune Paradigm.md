---
tags: [llm, chunk]
source: "[[raw-llm-031]]"
confidence: high
supports:
  - "[[LLM/2018–2019 — Pretrained Language Models/GPT and Decoder-Only Lineage]]"
  - "[[LLM/2018–2019 — Pretrained Language Models/Supervised Fine-Tuning]]"
qna_seeds:
  - "Q: What training paradigm did GPT-1 establish? A: GPT-1 introduced the pre-train on unlabeled text then fine-tune on downstream tasks paradigm, where a generative (left-to-right) language model is first trained unsupervised and then adapted with task-specific labeled data."
---

# GPT-1 Established the Pre-Train → Fine-Tune Paradigm

GPT-1 (Radford et al., 2018) introduced the two-stage recipe of generative pre-training on unlabeled text followed by discriminative fine-tuning on downstream tasks. The model was pre-trained with a standard language modeling objective on the BooksCorpus (~7,000 unpublished books), then fine-tuned with task-specific heads. This pre-train → fine-tune paradigm became the default recipe for NLP and set the stage for GPT-2, GPT-3, and the entire decoder-only lineage.