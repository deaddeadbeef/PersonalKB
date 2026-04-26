---
tags: [chunk, llm]
id: "chunk-llm-012"
source: "[[LLM/_raw/raw-llm-003 BERT Pre-training of Deep Bidirectional Transformers]]"
source_loc: "Section 1, Section 3"
topic: "bidirectional context"
claim: "Bidirectional context from MLM produces richer representations than left-to-right models for understanding tasks"
confidence: "verified"
supports: ["[[LLM/Foundations/Language Model Fundamentals]]"]
up: "[[LLM/LLM]]"
---

# Bidirectional Context Produces Richer Representations

## Context

Before BERT, pre-trained language models like GPT used left-to-right (autoregressive) training, where each token can only attend to preceding tokens. This is natural for generation but limits the representations available for understanding tasks. BERT's key insight was that Masked Language Modeling allows bidirectional pre-training: when predicting a masked token, the model can attend to both left and right context simultaneously, producing richer representations.

The difference is striking: to predict the meaning of "bank" in "I went to the bank to deposit money," a left-to-right model only sees "I went to the" — insufficient for disambiguation. BERT sees the entire sentence, including "deposit money," which clearly resolves the ambiguity. Empirically, BERT dominated understanding benchmarks (GLUE, SQuAD, NER) upon release, outperforming GPT-1 and ELMo by large margins on tasks requiring full-context comprehension.

## Why It Matters

The bidirectional vs. unidirectional distinction became the fundamental axis differentiating encoder models (BERT family, for understanding) from decoder models (GPT family, for generation). Understanding this trade-off is essential for choosing the right model class: encoders for classification, extraction, and retrieval; decoders for generation and reasoning. Modern encoder-decoder models (T5, BART) attempt to get the best of both worlds.

## QnA Seeds
- Q: Why can't autoregressive models achieve bidirectional context?
  A: Autoregressive models are trained to predict the next token, so they must not "see" future tokens during training — this would be information leakage. The causal attention mask enforces this constraint. While bidirectional attention would produce richer representations, it would break the generative training objective. BERT solved this by using a different objective (MLM) that doesn't require left-to-right generation.
- Q: If bidirectional context is superior for understanding, why do most modern LLMs use decoder-only architectures?
  A: Decoder-only models can perform both generation and understanding (by generating answers to understanding questions), while encoder-only models cannot easily generate open-ended text. At sufficient scale, decoder models achieve competitive understanding performance through in-context learning and chain-of-thought reasoning. The versatility of generation plus the simplicity of a single architecture has made decoder-only the dominant paradigm.
