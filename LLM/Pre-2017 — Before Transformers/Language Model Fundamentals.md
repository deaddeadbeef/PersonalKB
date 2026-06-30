---
tags: [llm, foundations]
up: "[[Pre-2017 — Before Transformers Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Language Model Fundamentals

> **One-line summary** A language model learns to assign probabilities to token sequences, usually by predicting what token comes next.

## 🎯 Intuition
**The Core Idea:** A language model estimates a probability distribution over the vocabulary at each position so it can predict the next token from prior context.

**Analogy:** A language model is like an ultra-fast autocomplete engine that keeps a weighted shortlist of what could plausibly come next, updating that shortlist after every new token it sees.

**Why It Matters:** Next-token prediction is the foundation of modern AI's most capable systems. The surprising insight from the scaling era is that optimizing this deceptively simple and seemingly narrow objective at sufficient scale produces models that can reason, translate, follow instructions, write code, and engage in complex multi-turn conversations. Understanding why this works — compression as intelligence, and the connection between prediction and understanding — remains one of the field's deepest open questions.

---

## ⚙️ Core Mechanics
### How It Works
- A language model assigns probabilities to sequences of tokens — at its core, it answers “what word comes next?”
- **Next-token prediction**: `P(x_t | x_{<t})` via softmax over vocabulary logits.
- **Cross-entropy loss**: `L = -1/N × Σ log P(x_i | x_{<i})`.
- **Perplexity**: `PPL = exp(L)`, lower is better.
- **Teacher forcing**: during training, feed ground-truth tokens rather than model predictions.
- **Autoregressive generation**: at inference, sample from the predicted distribution, append the token, and repeat.
- **Temperature**: scales logits before softmax; lower = more deterministic, higher = more random.
- **Top-k / top-p (nucleus) sampling**: truncate the distribution to the most likely tokens for higher-quality generation.

### Key Specifications

| Aspect | Autoregressive (Causal) | Masked Language Model |
|--------|------------------------|----------------------|
| Direction | Left-to-right only | Bidirectional |
| Training | Predict next token | Predict masked tokens |
| Generation | Natural (sequential) | Requires iterative refinement |
| Examples | GPT, LLaMA, Claude | BERT, RoBERTa |
| Primary use | Text generation, chat | Classification, embeddings |

### Key Facts
- The full sequence probability factors into conditional probabilities through the chain rule.
- Autoregressive models predict each token from previous tokens only.
- Masked language modeling uses bidirectional context but does not naturally support generation.
- Cross-entropy is the standard training loss, and perplexity is the standard intrinsic evaluation metric.
- Sampling controls like temperature and top-k/top-p affect generation quality and diversity.

---

## 🔬 Deep Dive
### Technical Details
A language model computes a probability distribution over a vocabulary at each position in a sequence. In the autoregressive (causal) formulation, used by GPT and most modern LLMs, the model predicts `P(x_t | x_1, ..., x_{t-1})` — the probability of the next token given all previous tokens. The full sequence probability factors as a product of conditional probabilities via the chain rule.

The masked language modeling (MLM) objective, used by BERT, instead randomly masks some tokens and predicts them from bidirectional context. This gives richer contextual representations but does not naturally support generation.

Training minimizes cross-entropy loss between the model's predicted distribution and the actual next token. Perplexity — the exponentiation of the average cross-entropy — serves as the standard intrinsic evaluation metric. A perplexity of 10 means the model is, on average, as uncertain as if it had to choose uniformly among 10 options.

### Limitations and Criticisms
- Masked language modeling yields strong bidirectional representations but does not naturally support left-to-right generation.
- Perplexity is useful as an intrinsic metric, but it does not fully capture instruction-following, reasoning quality, or downstream usefulness.
- The field still lacks a complete theory for why scaling next-token prediction produces broad capabilities like reasoning and code generation.

### Impact and Legacy
The core language-modeling setup became the basis of the modern LLM stack. Autoregressive next-token prediction, paired with large-scale pretraining and sampling-based inference, enabled the GPT-style trajectory toward general-purpose text generation. The contrast with MLM also shaped the split between encoder-style representation models and decoder-style generative models.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What does `P(x_t | x_{<t})` mean in an autoregressive language model?
2. Why does a lower perplexity correspond to a better language model?
3. Why is masked language modeling less natural for generation than causal language modeling?

### Core Problems
1. Explain how teacher forcing changes the training process compared with autoregressive generation at inference time.
2. Compare causal and masked language modeling in terms of attention direction, training signal, and downstream use cases such as chat, embeddings, and classification.

### Challenge
1. Give a principled argument for or against the claim that next-token prediction alone is sufficient to produce general-purpose intelligence when scaled.

*See also:*
- [[Transformer Architecture]] — the architecture that superseded RNN-based language models
- [[Decoder-Only Models]] — the autoregressive LM paradigm scaled up with GPT
- [[Scaling Laws]] — formal power-law relationships governing language model performance
- [[Instruction Tuning]] — adapting pretrained language models to follow instructions
- [[LLM/Study/Tiny Decoder-Only Transformer Training Lab|Tiny Decoder-Only Transformer Training Lab]] — implement next-token loss, teacher forcing, and autoregressive generation in a toy decoder-only model

## Supporting Chunks
### Supporting Chunks
- No supporting chunk notes are attached yet.

## References
- [[LLM/Sources/Sources Index]]
