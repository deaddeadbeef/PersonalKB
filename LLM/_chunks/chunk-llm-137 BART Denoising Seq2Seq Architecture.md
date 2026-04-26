---
tags: [llm, chunk]
source: "[[raw-llm-035]]"
confidence: high
supports:
  - "[[LLM/2018–2019 — Pretrained Language Models/2018–2019 — Pretrained Language Models Overview]]"
qna_seeds:
  - "Q: What is BART's architecture? A: BART combines a bidirectional encoder (like BERT) with a left-to-right autoregressive decoder (like GPT) in an encoder-decoder Transformer, pre-trained by corrupting text with arbitrary noising functions and learning to reconstruct the original."
---

# BART Combines Bidirectional Encoder with Autoregressive Decoder

BART (Lewis et al., 2019) uses an encoder-decoder Transformer architecture where the encoder is bidirectional (like BERT) and the decoder is autoregressive left-to-right (like GPT). It is pre-trained as a denoising autoencoder: text is corrupted with arbitrary noising functions, and the model learns to reconstruct the original undamaged input. This hybrid design unifies the strengths of encoder-only models (rich bidirectional representations) and decoder-only models (strong generation) in a single framework.