---
tags: [llm, history]
up: "[[Pre-2017 — Before Transformers Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---

# Pre-Transformer Foundations

> **One-line summary** Before transformers, NLP advanced through n-grams, static embeddings, and recurrent models that each solved part of the language problem while exposing the limitations transformers later overcame.

## 🎯 Intuition
**The Core Idea:** Before transformers dominated NLP, the field progressed through a series of architectures—from simple count-based n-gram models to dense word embeddings and recurrent neural networks—each solving one limitation while introducing another, ultimately setting the stage for the attention-based revolution of 2017.

**Analogy:** Pre-transformer NLP was like building roads through rough terrain: n-grams gave short local streets, embeddings added a map of semantic neighborhoods, and RNNs built winding highways through sequences—but attention was needed for a true high-speed network.

**Why It Matters:** Every major idea in transformers—embeddings, attention, contextual representations—was invented in this era. Understanding these foundations clarifies *why* transformers were designed the way they were. The attention mechanism from Bahdanau directly evolved into the self-attention that powers every modern LLM, and the pre-train/fine-tune paradigm that ELMo pioneered became the dominant workflow for BERT and GPT.

Before transformers dominated NLP, the field progressed through a series of architectures—from simple count-based n-gram models to dense word embeddings and recurrent neural networks—each solving one limitation while introducing another, ultimately setting the stage for the attention-based revolution of 2017.

For the neural-network-specific spine behind this transition, read [[Pre-LLM Neural Network Foundations]] first: it separates backpropagation, embeddings, recurrence, gating, encoder-decoder models, and attention into the ideas that survived into modern LLMs and the limitations transformers solved.

---

## ⚙️ Core Mechanics
### How It Works
Statistical language modeling began with **n-gram models**, which estimated the probability of a word given the previous *n−1* words. These were effective for short-range patterns and powered early machine translation and speech recognition systems, but they suffered from data sparsity and an inability to capture meaning. The curse of dimensionality meant that increasing context length caused an exponential explosion in the number of parameters needed.

**Word2Vec** (Mikolov et al., 2013) represented a paradigm shift by learning dense, low-dimensional vector representations of words from large corpora. Its skip-gram and CBOW architectures revealed that vector arithmetic could capture semantic relationships—the famous `king − man + woman ≈ queen` analogy. GloVe (2014) extended this idea with global co-occurrence statistics. However, these embeddings were *static*: a word had one vector regardless of context, so "bank" meant the same thing in "river bank" and "bank account."

**Recurrent Neural Networks (RNNs)** and their gated variants—**LSTMs** (Hochreiter & Schmidhuber, 1997) and **GRUs** (Cho et al., 2014)—introduced sequential processing that could, in theory, model arbitrarily long dependencies. The **seq2seq** framework with **attention** (Bahdanau et al., 2014) was a breakthrough for machine translation, allowing the decoder to focus on relevant parts of the input. **ELMo** (Peters et al., 2018) finally delivered *contextualized* embeddings by running a bidirectional LSTM over entire sentences. Yet RNNs processed tokens one at a time, making them inherently slow to train on long sequences and still struggling with very long-range dependencies despite gating mechanisms.

- **N-grams**: P(wₙ | wₙ₋₁, ..., w₁) approximated via fixed-window count ratios; smoothing techniques (Kneser-Ney) to handle unseen sequences
- **Word2Vec (Skip-gram)**: Predict context words from a center word; trained with negative sampling for efficiency; produces 100–300 dim vectors
- **Word2Vec (CBOW)**: Predict center word from context; faster training, slightly less accurate on rare words
- **GloVe**: Factorizes the global word-word co-occurrence matrix; combines benefits of count-based and predictive methods
- **RNN**: Hidden state hₜ = f(Whₜ₋₁ + Wxₜ); vanishing gradient limits effective memory to ~10–20 tokens in practice
- **LSTM**: Cell state + forget/input/output gates; mitigates vanishing gradients but not computational bottleneck
- **GRU**: Simplified LSTM with reset and update gates; fewer parameters, comparable performance
- **Seq2seq + Attention (Bahdanau)**: Encoder produces hidden states for each input token; decoder computes attention weights over all encoder states at each generation step
- **ELMo**: Two-layer bidirectional LSTM; concatenates forward and backward representations; produces context-dependent word vectors used as features for downstream tasks

### Key Specifications

| Model | Year | Type | Context Handling | Key Limitation |
|-------|------|------|-----------------|----------------|
| N-grams | ~1990s | Statistical | Fixed window (n−1 tokens) | Data sparsity, no semantics |
| Word2Vec | 2013 | Embedding | None (static vectors) | No polysemy, no context |
| GloVe | 2014 | Embedding | Global co-occurrence | Same as Word2Vec |
| LSTM | 1997 | Recurrent | Sequential hidden state | Slow training, limited range |
| GRU | 2014 | Recurrent | Simplified gating | Same class of limitations |
| Seq2seq + Attn | 2014 | Enc-Dec RNN | Attention over encoder | Still sequential |
| ELMo | 2018 | Bi-LSTM | Full sentence context | No parallelism, shallow |

### Key Facts
- N-gram models worked for short-range statistical patterns but scaled poorly because longer context windows exploded parameter requirements.
- Word2Vec and GloVe introduced dense semantic embeddings, but both remained static and could not disambiguate polysemous words by context.
- RNNs, LSTMs, and GRUs modeled sequence order directly, but sequential processing made them slow and hard to scale.
- Bahdanau attention was a crucial precursor to transformer self-attention.
- ELMo showed the power of contextualized embeddings and helped establish the pre-train/fine-tune workflow later used by BERT and GPT.
- The pre-LLM neural-network lineage is best read as a set of reusable mechanisms, not as obsolete history: embeddings, logits, losses, attention, and sequence-state trade-offs still appear directly in local LLM inference diagnostics.

---

## 🔬 Deep Dive
### Technical Details
The key limitations that transformers solved were precisely the pain points of this era: **no parallelism** (RNNs process sequentially, blocking GPU utilization), **vanishing gradients over long ranges** (even LSTMs struggled beyond a few hundred tokens), and **static representations** (Word2Vec couldn't disambiguate polysemy). Recognizing these constraints makes the transformer's design choices—self-attention for parallelism, positional encodings instead of recurrence, stacked layers for depth—feel like inevitable solutions rather than arbitrary innovations.

N-grams relied on count ratios plus smoothing such as Kneser-Ney to handle unseen sequences, but fixed windows limited them to local context. Word2Vec skip-gram predicted context words from a center word and used negative sampling for efficiency, while CBOW predicted a center word from its context and trained faster but was slightly less accurate on rare words. GloVe factorized the global word-word co-occurrence matrix, combining count-based and predictive ideas. RNNs used recurrent hidden states hₜ = f(Whₜ₋₁ + Wxₜ), but vanishing gradients limited effective memory to roughly 10–20 tokens in practice. LSTMs added cell state plus forget/input/output gates, and GRUs used reset and update gates for a lighter-weight alternative. Seq2seq with attention let decoders compute attention weights over encoder states at each generation step. ELMo used a two-layer bidirectional LSTM and concatenated forward and backward representations to create context-dependent word vectors for downstream tasks.

### Limitations and Criticisms
- N-grams suffered from data sparsity, lacked semantics, and became infeasible as context length grew.
- Static embeddings like Word2Vec and GloVe gave one vector per word type, so they could not model polysemy or sentence-specific meaning.
- RNN-family models remained sequential and computationally slow, and even gated variants still struggled with very long-range dependencies.

### Impact and Legacy
Every major idea in transformers—embeddings, attention, contextual representations—was invented in this era. The attention mechanism from Bahdanau directly evolved into the self-attention that powers every modern LLM, and the pre-train/fine-tune paradigm that ELMo pioneered became the dominant workflow for BERT and GPT.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why were n-gram models effective for short-range patterns but weak for language understanding?
2. What problem did Word2Vec solve, and what major problem did it leave unsolved?
3. Why did attention become such an important addition to seq2seq models?

### Core Problems
1. Compare Word2Vec, GloVe, and ELMo in terms of training signal, representation type, and whether each model can handle polysemy.
2. Explain why LSTMs improved over vanilla RNNs yet still failed to deliver the parallelism needed for large-scale language modeling.

### Challenge
1. Argue which pre-transformer invention contributed most directly to modern LLMs: dense embeddings, gated recurrence, encoder-decoder attention, or contextualized embeddings.

*See also:* [[Pre-2017 — Before Transformers Overview]], [[Pre-LLM Neural Network Foundations]], [[LLM/Sources/Sources Index]]

## References
### Supporting Chunks
- Evidence chunks and raw source notes are reachable through [[LLM/LLM Corpus Index|LLM Corpus Index]] and [[LLM/Sources/Sources Index|LLM Sources Index]].

### References
- [[LLM/Sources/Sources Index]]
