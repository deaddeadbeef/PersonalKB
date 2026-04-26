---
tags: [chunk, llm]
id: "chunk-llm-116"
source: "[[LLM/_raw/raw-llm-029 Survey of Large Language Models]]"
source_loc: "Key Takeaways 1, Chunk Candidates"
topic: "Model families cluster by architecture"
claim: "Model families cluster by architectural choices: decoder-only dominates generation, encoder-only dominates embeddings, and MoE enables sparse scaling."
confidence: "verified"
supports: ["[[LLM/Architecture Variants/Decoder-Only Models]]"]
up: "[[LLM/LLM]]"
---

# Model Families Cluster by Architectural Choice

## Context
The survey provides a systematic taxonomy of LLM families organized by architectural choices. Decoder-only models (GPT, LLaMA, PaLM) dominate text generation tasks and have become the default architecture for chat and reasoning. Encoder-only models (BERT and its variants) remain the standard for embeddings, classification, and retrieval tasks where bidirectional context is valuable. Encoder-decoder models (T5, BART) excel at seq2seq tasks like summarization and translation. Mixture-of-Experts (MoE) models (Switch Transformer, Mixtral) use sparse activation to scale total parameters while keeping per-token compute constant.

This architectural clustering is not arbitrary — each architecture has structural advantages for its niche. Decoder-only models' autoregressive nature is ideal for open-ended generation. Encoder-only models' bidirectional attention is ideal for understanding tasks. MoE's sparse activation enables parameter counts that would be prohibitively expensive with dense models.

## Why It Matters
Understanding architectural clustering helps practitioners choose the right model family for their task. It also explains the industry trend toward decoder-only architectures for general-purpose assistants: their autoregressive generation capability is the most versatile for open-ended interaction, even if they are not optimal for every specific sub-task.

## QnA Seeds
- Q: Which architecture dominates LLM text generation and why?
  A: Decoder-only (GPT, LLaMA, PaLM) dominates generation because autoregressive next-token prediction naturally produces open-ended text, making it ideal for chat, reasoning, and general-purpose assistants.
- Q: What advantage do Mixture-of-Experts models provide?
  A: MoE enables sparse scaling — increasing total parameter count (and knowledge capacity) while keeping per-token compute constant by activating only a subset of experts for each input.
