---
tags: [chunk, llm]
id: "chunk-llm-003"
source: "[[LLM/_raw/raw-llm-001 Attention Is All You Need]]"
source_loc: "Section 3.5"
topic: "positional encoding"
claim: "Positional encoding is needed because self-attention is permutation-invariant; original Transformer used sinusoidal encoding"
confidence: "verified"
supports: ["[[LLM/Foundations/Positional Encoding]]"]
up: "[[LLM/LLM]]"
---

# Positional Encoding for Permutation-Invariant Attention

## Context

Self-attention treats its input as a set, not a sequence — if you permute the input tokens, the attention scores permute identically without any change in the computed relationships. This permutation invariance means that without additional information, the model cannot distinguish "the cat sat on the mat" from "mat the on sat cat the." Positional encoding injects sequence order information into the model.

The original Transformer used fixed sinusoidal positional encodings: PE(pos, 2i) = sin(pos / 10000^(2i/d_model)) and PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model)). These encodings are added directly to the input embeddings. The sinusoidal design was chosen because it allows the model to learn relative positions (since PE(pos+k) can be expressed as a linear function of PE(pos)) and generalizes to sequence lengths longer than those seen in training.

## Why It Matters

Positional encoding is a foundational design choice that impacts every downstream capability of a Transformer. The original sinusoidal approach has since been largely superseded by learned encodings (GPT-2), rotary position embeddings (RoPE in LLaMA), and ALiBi, each with different trade-offs for length generalization and computational efficiency.

## QnA Seeds
- Q: Why does self-attention need positional encoding at all?
  A: Self-attention computes the same output regardless of input order (it is permutation-equivariant). Without positional encoding, the model has no way to distinguish word order, making it unable to differentiate "dog bites man" from "man bites dog." Positional encodings inject position information so the model can reason about sequence structure.
- Q: What advantage did sinusoidal encoding have over learned positional embeddings?
  A: Sinusoidal encodings allow the model to extrapolate to sequence lengths not seen during training, since they are defined by a continuous mathematical function. They also encode relative position information — the offset between any two positions can be represented as a linear transformation of their encodings. Learned embeddings, by contrast, are fixed to the maximum training length.
