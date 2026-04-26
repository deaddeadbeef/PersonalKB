---
tags: [llm, architecture]
up: "[[2017 — The Transformer Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Encoder-Decoder Models

> **One-line summary** Encoder-decoder transformers read the full input with an encoder, then generate outputs step by step with a decoder that cross-attends back to the encoded representation.

## 🎯 Intuition
**The Core Idea:** An encoder-decoder model separates understanding the input from generating the output, connecting them through cross-attention.
**Analogy:** Like a translator who first reads and understands the whole sentence, then writes the translation word by word while repeatedly glancing back at the source.
**Why It Matters:** Encoder-decoder models use separate stacks for processing input and generating output, making them especially strong when there is a clear input-output mapping. While decoder-only models dominate general chat and open-ended generation, encoder-decoder models remain especially effective for translation, summarization, and structured generation. The text-to-text framing popularized by T5 also showed that one architecture could handle many NLP tasks through a unified interface.

---

## ⚙️ Core Mechanics
### How It Works
- The encoder-decoder architecture mirrors the original transformer design: the encoder processes the full input bidirectionally, producing rich contextual representations.
- The decoder then generates the output autoregressively, using cross-attention to "look at" the encoder's representations at each step.
- **Encoder**: bidirectional self-attention, processes full input
- **Decoder**: causal self-attention + cross-attention to encoder output
- **Cross-attention**: decoder queries attend to encoder key/value representations
- **T5 span corruption**: replace random spans with sentinel tokens, predict the replaced spans
- **BART denoising**: reconstruct original from corrupted input (multiple corruption strategies)
- **Text-to-text framing**: every task becomes sequence-to-sequence with task-specific prefixes

### Key Specifications

| Model | Year | Pretraining | Key Use |
|-------|------|------------|---------|
| T5 | 2019 | Span corruption | Multi-task NLP |
| BART | 2019 | Denoising autoencoder | Summarization, generation |
| UL2 | 2022 | Mixed objectives (MoD) | Unified pretraining |

### Key Facts
- Encoder-decoder models use separate stacks for processing input and generating output.
- The encoder is bidirectional, while the decoder is autoregressive.
- Cross-attention is the bridge that lets the decoder access encoded input representations.
- T5, BART, and UL2 are key examples of the paradigm.

---

## 🔬 Deep Dive
### Technical Details
The encoder processes the full input bidirectionally and produces rich contextual representations. The decoder then generates the output autoregressively, using cross-attention to attend to the encoder states at each generation step. T5 (Raffel et al. 2019) established the "text-to-text" framework, where every NLP task is framed as text input → text output: translation becomes a prefixed instruction followed by translated text, summarization becomes a summarization prompt followed by a summary, and classification becomes a prompt whose output is a label like "positive." BART (Lewis et al. 2019) used a denoising objective by corrupting the input through masking, deletion, permutation, and rotation, then training the model to reconstruct the original. UL2 (Tay et al. 2022) extended the pattern by unifying multiple pretraining objectives, including causal, prefix, and span corruption, with mode-switching tokens.

### Limitations and Criticisms
- Encoder-decoder models are often less favored than decoder-only models for general-purpose chat and open-ended generation.
- Maintaining both encoder and decoder stacks can make the architecture more complex than single-stack alternatives.
- Their strengths are clearest when tasks have explicit input-output separation, so they may be less naturally aligned with purely next-token-style deployment settings.

### Impact and Legacy
The architecture preserved the original transformer seq2seq design and proved that a single sequence-to-sequence framework could support many NLP tasks. T5 strongly influenced prompt-style task framing, BART became a major reference for denoising-based generation and summarization, and UL2 pushed toward unified pretraining over multiple objectives. Encoder-only and decoder-only families can also be understood as specializing one half of the broader encoder-decoder blueprint.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What role does the encoder play that the decoder does not?
2. Why is cross-attention essential in encoder-decoder models?
3. Why are encoder-decoder models especially natural for translation and summarization?

### Core Problems
1. Compare T5, BART, and UL2 in terms of their pretraining objectives and explain how each objective shapes downstream behavior.
2. Design a text-to-text prompt formulation for a classification or extraction task and explain how an encoder-decoder model would process it.

### Challenge
1. Analyze when an encoder-decoder architecture should outperform a decoder-only model, and identify where the extra encoder stack yields enough benefit to justify its cost.

---

*See also:* [[Language Model Fundamentals]] — seq2seq foundations before the transformer era; [[Encoder-Only Models]] — BERT derives from the encoder half of the architecture; [[Decoder-Only Models]] — GPT derives from the decoder half of the architecture; [[Supervised Fine-Tuning]] — fine-tuning encoder-decoder models like T5; [[Scaling Laws]] — scaling encoder-decoder vs decoder-only architectures

## Supporting Chunks / References
*(To be populated as chunks are created)*

- [[LLM/Sources/Sources Index]]
