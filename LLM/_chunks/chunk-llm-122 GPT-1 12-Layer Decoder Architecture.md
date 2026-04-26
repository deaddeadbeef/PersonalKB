---
tags: [llm, chunk]
source: "[[raw-llm-031]]"
confidence: high
supports:
  - "[[LLM/2018–2019 — Pretrained Language Models/Decoder-Only Models]]"
  - "[[LLM/2018–2019 — Pretrained Language Models/GPT and Decoder-Only Lineage]]"
qna_seeds:
  - "Q: What was the architecture of GPT-1? A: GPT-1 used a 12-layer Transformer decoder with 768-dimensional hidden states, 12 attention heads, and 117M parameters, using byte-pair encoding (BPE) tokenization and learned positional embeddings."
---

# GPT-1 12-Layer Transformer Decoder Architecture

GPT-1 used a 12-layer Transformer decoder with 768-dimensional hidden states, 12 attention heads, and approximately 117 million parameters. It employed byte-pair encoding (BPE) tokenization with a vocabulary of ~40,000 merges and learned positional embeddings rather than sinusoidal ones. This relatively compact architecture demonstrated that decoder-only Transformers could serve as effective general-purpose feature extractors for NLP.