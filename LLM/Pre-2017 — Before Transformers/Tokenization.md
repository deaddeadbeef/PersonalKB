---
tags: [llm, foundations]
up: "[[Pre-2017 — Before Transformers Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---

# Tokenization

> **One-line summary** Tokenization turns raw text into model-readable token IDs, and the tokenizer design directly shapes efficiency, context usage, multilingual fairness, and downstream performance.

## 🎯 Intuition
**The Core Idea:** Modern LLMs use subword tokenization — a middle ground between character-level (too fine-grained, very long sequences) and word-level (too coarse, huge vocabulary, can't handle unseen words).

**Analogy:** Tokenization is like chopping a sentence into puzzle pieces the model can swallow: if the pieces are too tiny, processing becomes slow and bloated; if they are too large, the system cannot handle unfamiliar words cleanly.

**Why It Matters:** Tokenization is the often-overlooked first step that affects everything downstream. Poor tokenization of non-English languages (the "tokenization tax") means models need more tokens to represent the same content, increasing cost and reducing effective context length. Common tokens like "the" get a single token while rare terms like "phenomenological" might use 3-4 tokens.

Tokenization converts raw text into the discrete token IDs that a language model actually processes. The choice of tokenizer affects model efficiency, multilingual capability, and even task performance.

---

## ⚙️ Core Mechanics
### How It Works
Modern LLMs use subword tokenization — a middle ground between character-level (too fine-grained, very long sequences) and word-level (too coarse, huge vocabulary, can't handle unseen words). The key insight is to represent common words as single tokens while breaking rare words into meaningful subword pieces.

Byte Pair Encoding (BPE) starts with individual characters and iteratively merges the most frequent adjacent pair into a new token. After training, the vocabulary contains common words, frequent subwords, and individual characters as fallback. GPT-2, GPT-3, GPT-4, and LLaMA all use BPE variants.

SentencePiece operates directly on raw text (including whitespace) without language-specific preprocessing. It supports both BPE and Unigram algorithms. The Unigram model takes a probabilistic approach: start with a large vocabulary and iteratively remove tokens that least affect the likelihood of the training corpus.

- **BPE**: iteratively merge most frequent character pairs; vocabulary size is a hyperparameter (typically 32K-128K)
- **WordPiece**: similar to BPE but merges based on likelihood increase (used in BERT)
- **Unigram**: probabilistic model, prune vocabulary based on marginal likelihood (used in T5 via SentencePiece)
- **SentencePiece**: language-agnostic, treats input as raw byte stream
- **tiktoken**: OpenAI's fast BPE implementation for GPT models
- **Vocabulary size trade-offs**: larger vocab → shorter sequences but larger embedding table; smaller vocab → longer sequences but smaller model
- **Special tokens**: [CLS], [SEP], [PAD], <bos>, <eos>, <unk> for model control
- **Byte-fallback**: represent any byte as a token, ensuring no out-of-vocabulary tokens

### Key Specifications

| Method | Merge Strategy | Used By |
|--------|---------------|---------|
| BPE | Frequency-based merging | GPT-2/3/4, LLaMA, Mistral |
| WordPiece | Likelihood-based merging | BERT |
| Unigram | Probabilistic pruning | T5 (via SentencePiece) |

### Key Facts
- Subword tokenization balances the extremes of character-level and word-level tokenization.
- BPE starts from characters and repeatedly merges the most frequent adjacent pair.
- SentencePiece works directly on raw text, including whitespace, without language-specific preprocessing.
- Vocabulary size trades off sequence length against embedding table size.
- Byte-fallback guarantees the tokenizer can represent any input without true out-of-vocabulary failures.

---

## 🔬 Deep Dive
### Technical Details
The key insight is to represent common words as single tokens while breaking rare words into meaningful subword pieces.

Byte Pair Encoding (BPE) starts with individual characters and iteratively merges the most frequent adjacent pair into a new token. After training, the vocabulary contains common words, frequent subwords, and individual characters as fallback. GPT-2, GPT-3, GPT-4, and LLaMA all use BPE variants.

SentencePiece operates directly on raw text (including whitespace) without language-specific preprocessing. It supports both BPE and Unigram algorithms. The Unigram model takes a probabilistic approach: start with a large vocabulary and iteratively remove tokens that least affect the likelihood of the training corpus.

Tokenization is the often-overlooked first step that affects everything downstream. Poor tokenization of non-English languages (the "tokenization tax") means models need more tokens to represent the same content, increasing cost and reducing effective context length. This affects arithmetic (numbers split across tokens), code (variable names fragmented), and multilingual fairness.

### Limitations and Criticisms
- Poor tokenizer design can impose a "tokenization tax" on some languages, making them more expensive and less context-efficient to model.
- Rare words, numbers, and code identifiers may fragment into multiple tokens, which can hurt arithmetic handling, code modeling, and efficiency.
- Tokenizer choices create trade-offs: larger vocabularies shorten sequences but increase embedding size, while smaller vocabularies reduce embeddings but lengthen sequences.

### Impact and Legacy
The choice of tokenizer affects model efficiency, multilingual capability, and even task performance. Common tokens like "the" get a single token while rare terms like "phenomenological" might use 3-4 tokens. This affects arithmetic (numbers split across tokens), code (variable names fragmented), and multilingual fairness.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why is subword tokenization a compromise between character-level and word-level tokenization?
2. How does BPE decide which new token to add next?
3. Why does poor tokenization reduce effective context length for some languages?

### Core Problems
1. Compare BPE, WordPiece, and Unigram in terms of merge strategy, training objective, and the major model families that use them.
2. You need to tokenize a multilingual dataset with lots of code and rare identifiers. Explain how vocabulary size, byte-fallback, and raw-text processing would affect your tokenizer choice.

### Challenge
1. Propose a tokenizer evaluation framework that measures not just compression efficiency but also multilingual fairness, arithmetic friendliness, and code representation quality.

*See also:* [[LLM/Multimodal/Multimodal Tokenization and Fusion|Multimodal Tokenization]], [[LLM/Pretraining/Data Curation and Deduplication|Data Curation]]

## References
### Supporting Chunks
- Evidence chunks and raw source notes are reachable through [[LLM/LLM Corpus Index|LLM Corpus Index]] and [[LLM/Sources/Sources Index|LLM Sources Index]].

### References
- [[LLM/Sources/Sources Index]]
