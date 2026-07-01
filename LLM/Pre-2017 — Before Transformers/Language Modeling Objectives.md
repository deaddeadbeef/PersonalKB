---
tags: [llm, pretraining]
up: "[[Pre-2017 — Before Transformers Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---

# Language Modeling Objectives

> **One-line summary** Pretraining objectives teach models by turning raw text into prediction tasks that force them to learn structure, semantics, and usable world knowledge.

## 🎯 Intuition
**The Core Idea:** Language modeling objectives work by creating prediction tasks over unlabeled text that force models to internalize language structure, semantics, and knowledge.

**Analogy:** A pretraining objective is like choosing the drills for an athlete: one drill teaches pure continuation, another teaches filling in blanks, and another teaches reconstruction after corruption, so the skill the model develops depends on the practice format.

**Why It Matters:** The choice of pretraining objective fundamentally shapes what a model learns and how it can be used. Next-token prediction has emerged as the dominant paradigm for foundation models because it scales seamlessly to generation, aligns naturally with human text production, and teaches surprisingly general capabilities. The universality of causal LM — that predicting the next token end-to-end captures so much of intelligence — is one of the field's key empirical discoveries, even though specialized objectives still matter in domains like code infilling.

---

## ⚙️ Core Mechanics
### How It Works
- The most dominant objective is **next-token prediction** (causal or autoregressive language modeling), where given a sequence of tokens `x₁, x₂, ..., xₜ`, the model predicts `xₜ₊₁`.
- **Next-token prediction (causal LM)**: `P(x) = ∏ P(xₜ | x<ₜ)`; uses causal attention mask; loss on all positions.
- **Masked LM (MLM)**: mask ~15% of tokens with `[MASK]`, random tokens, or unchanged; predict masked tokens; bidirectional attention.
- **Prefix LM**: bidirectional attention on prefix tokens, causal on suffix; combines comprehension and generation.
- **Span corruption (T5)**: mask spans of mean length 3; replace with sentinel tokens; generate corrupted spans autoregressively.
- **Fill-in-the-middle (FIM)**: reorder as prefix-suffix-middle or suffix-prefix-middle with special delimiters; predict middle portion.
- **Denoising**: apply noise (deletion, masking, permutation); reconstruct original sequence.
- All objectives share the underlying principle: create a prediction task that requires understanding language structure.

### Key Specifications

| Objective | Attention | Use Case | Example Models |
|-----------|-----------|----------|----------------|
| Causal LM | Unidirectional (left-to-right) | Generation, foundation models | GPT-3, LLaMA, PaLM |
| Masked LM | Bidirectional | Classification, embeddings | BERT, RoBERTa |
| Prefix LM | Hybrid (bi on prefix, causal on suffix) | Both comprehension and generation | PaLM (variant) |
| Span corruption | Encoder-decoder | Seq2seq tasks | T5, UL2 |
| Fill-in-the-middle | Causal with reordering | Code infilling | CodeGen, StarCoder |

### Key Facts
- Causal LM is naturally suited to generation because the model only attends left-to-right.
- MLM gives richer bidirectional representations but makes pure generation awkward.
- Prefix LM mixes bidirectional understanding with causal generation.
- Span corruption and denoising train models to reconstruct missing or corrupted content.
- Fill-in-the-middle is especially important for code models that must infill, not just continue.

---

## 🔬 Deep Dive
### Technical Details
The most dominant objective is **next-token prediction** (causal or autoregressive language modeling), where given a sequence of tokens `x₁, x₂, ..., xₜ`, the model predicts `xₜ₊₁`. This is formalized as maximizing the log-likelihood: `L = Σ log P(xₜ | x₁, ..., xₜ₋₁)`. The model can only attend to previous tokens (left-to-right), making it naturally suited for text generation. What is remarkable is that this seemingly simple objective — predict the next word — turns out to be surprisingly universal, teaching models grammar, facts, reasoning patterns, and even some degree of common sense.

**Masked language modeling** (MLM), popularized by BERT, randomly masks 15% of tokens and trains the model to predict them using bidirectional context. The loss is only computed on masked positions: `L = Σ log P(xᵢ | x₋ᵢ)` where `x₋ᵢ` denotes all tokens except `i`. This bidirectional attention allows richer representations but makes pure generation awkward. **Prefix LM** is a hybrid: bidirectional attention on a prefix, then causal on the suffix, used by models like PaLM to get benefits of both approaches.

**Span corruption** (T5) masks contiguous spans of tokens and trains the model to generate them. **Denoising** objectives corrupt the input in various ways (token deletion, masking, permutation) and train the model to reconstruct the original. **Fill-in-the-middle** (FIM), used in code models like CodeGen, splits sequences into prefix-suffix-middle and trains the model to generate the middle given prefix and suffix, teaching it to work with incomplete contexts — critical for code infilling.

### Limitations and Criticisms
- Causal LM is highly general, but it is not always the most natural objective for tasks like infilling or bidirectional understanding.
- MLM provides stronger bidirectional context during pretraining, but pure generation is awkward because the training setup is not naturally sequential.
- Specialized objectives improve domain fit, but they also fragment architectures and can lose the simplicity-and-scaling advantage that made decoder-only causal LM dominant.

### Impact and Legacy
The debate between causal and masked objectives influenced architecture choices for years, with encoder-decoder models like T5 and decoder-only models like GPT representing different philosophical bets. The trend has clearly moved toward decoder-only models with causal LM, validated by GPT-3, PaLM, LLaMA, and others showing that simplicity and scaling win. At the same time, objectives like fill-in-the-middle remain crucial in specialized settings such as code completion and infilling.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why does causal language modeling fit text generation more naturally than masked language modeling?
2. What extra capability does fill-in-the-middle add for code models?
3. How does prefix LM combine benefits of causal and masked-style training?

### Core Problems
1. Compare causal LM, MLM, and span corruption in terms of attention pattern, loss computation, and the types of downstream behavior each objective encourages.
2. Explain why a team building a code assistant might choose FIM over pure next-token prediction for some training data.

### Challenge
1. Propose a hybrid pretraining objective for a future model that must excel at both long-form generation and precise infilling, and explain what trade-offs it makes relative to causal LM and MLM.

*See also:*
- [[LLM/2018–2019 — Pretrained Language Models/BERT and Encoder Lineage|BERT]]
- [[LLM/2017 — The Transformer/Encoder-Decoder Models|T5]]
- [[Decoder-Only Models]]
- [[LLM/2018–2019 — Pretrained Language Models/Domain Adaptation|Code Models]]
- [[LLM/2020–2021 — The Scaling Era/Scaling Laws|PaLM]]
- [[LLM/Study/Tiny Decoder-Only Transformer Training Lab|Tiny Decoder-Only Transformer Training Lab]] — make the causal LM objective concrete with shifted targets and cross-entropy loss

## References
### Supporting Chunks
- Evidence chunks and raw source notes are reachable through [[LLM/LLM Corpus Index|LLM Corpus Index]] and [[LLM/Sources/Sources Index|LLM Sources Index]].

### References
- [[LLM/Sources/Sources Index]]
