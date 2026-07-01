---
tags: [llm, architecture]
up: "[[2018–2019 — Pretrained Language Models Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# Encoder-Only Models

> **Bidirectional language models learn rich contextual representations for understanding tasks, and evolved from BERT-style fine-tuning into today’s embedding-centered retrieval stack.**

## 🎯 Intuition
**The Core Idea:** Encoder-only models read an entire sequence at once and learn to understand masked pieces using both left and right context.
**Analogy:** Like a deep reader who can understand every sentence in full context but is not designed to write a novel from scratch.
**Why It Matters:** Encoder-only models proved that self-supervised pretraining on unlabeled text transfers extremely well to downstream NLP tasks with very little labeled data. Although decoder-only models won the generation race, encoders remain the workhorses for classification, named entity recognition, semantic similarity, and especially text embedding for retrieval.

---

## ⚙️ Core Mechanics
### How It Works
- Encoder-only models use masked language modeling (MLM) for pretraining: randomly mask ~15% of input tokens and predict them from the full bidirectional context.
- Unlike autoregressive models that can only look left, encoders see the complete surrounding context for each token, producing richer representations for understanding tasks.
- **Masked Language Modeling**: mask 15% of tokens (80% [MASK], 10% random, 10% unchanged)
- **Bidirectional attention**: no causal mask, every token attends to every other token
- **[CLS] token**: pooled representation for classification/embedding
- **Fine-tuning**: add task-specific head, update all parameters
- BERT (2018) established the paradigm: pretrain with MLM + Next Sentence Prediction, then fine-tune a classification head for downstream tasks.
- The [CLS] token's representation serves as a sequence-level embedding.
- RoBERTa (2019) showed BERT was undertrained — remove NSP, use dynamic masking, train longer with more data.
- DeBERTa (2020) introduced disentangled attention (separate content and position representations) and an enhanced mask decoder.
- The encoder lineage has shifted from task-specific fine-tuning toward embedding models.
- Modern encoders (E5, BGE, GTE, Nomic Embed) are trained with contrastive learning to produce embeddings for retrieval, and they power the entire RAG ecosystem.

### Key Specifications

| Model | Year | Key Innovation | Params |
|-------|------|---------------|--------|
| BERT | 2018 | MLM + NSP pretraining | 110M/340M |
| RoBERTa | 2019 | Better training recipe | 125M/355M |
| DeBERTa | 2020 | Disentangled attention | 134M/390M |
| E5/BGE | 2023 | Contrastive embedding training | ~300M |

### Key Facts
- **BERT-base**: 12 layers, 768 hidden, 12 heads, 110M params
- **BERT-large**: 24 layers, 1024 hidden, 16 heads, 340M params
- **RoBERTa improvements**: dynamic masking, no NSP, 10× more training data, larger batches
- **DeBERTa innovations**: disentangled content/position attention, enhanced mask decoder
- Encoder models now play a central role in retrieval and RAG through high-quality text embeddings.

---

## 🔬 Deep Dive
### Technical Details
Encoder-only models process entire input sequences bidirectionally, building rich contextual representations. Led by BERT, they dominated NLP from 2018-2022 for classification, extraction, and embedding tasks.

BERT-style pretraining combines MLM with, in the original BERT formulation, Next Sentence Prediction. The core training signal is to infer masked tokens from full-sequence context rather than from only left-to-right context. Because there is no causal mask, every token can attend to every other token in self-attention, enabling stronger representations for language understanding.

Architecturally, BERT-base uses 12 layers, 768-dimensional hidden states, 12 attention heads, and 110M parameters, while BERT-large scales to 24 layers, 1024 hidden states, 16 attention heads, and 340M parameters. The [CLS] token provides a sequence-level representation that can be used for classification or embedding.

RoBERTa demonstrated that BERT’s initial recipe was undertrained. Its main improvements were removing Next Sentence Prediction, switching to dynamic masking, training longer, increasing batch sizes, and using roughly 10× more training data. DeBERTa then improved the encoder design further by disentangling content and position representations inside attention and by using an enhanced mask decoder.

The lineage later shifted away from narrow task-specific fine-tuning and toward general-purpose embedding models. Modern encoder families such as E5, BGE, GTE, and Nomic Embed use contrastive learning objectives to produce retrieval-friendly vector representations, making them foundational for the modern RAG ecosystem.

### Limitations and Criticisms
- Encoder-only models are optimized for understanding rather than open-ended generation, so decoder-style models eventually dominated generative use cases.
- Early BERT-style systems required later recipe improvements because the original setup was undertrained relative to what the architecture could support.
- Their strongest modern niche shifted toward embeddings and retrieval rather than being the universal default for every NLP task.

### Impact and Legacy
Encoder-only models established self-supervised pretraining as a dominant paradigm for NLP transfer learning. They enabled strong performance on classification, extraction, semantic similarity, and low-label downstream tasks, and their evolution into contrastive embedding models now powers much of modern retrieval infrastructure and RAG.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why does bidirectional attention usually give encoder-only models an advantage on understanding tasks over left-to-right models?
2. What role does the [CLS] token play in classic BERT-style fine-tuning?
3. Why was RoBERTa considered evidence that BERT was undertrained rather than fundamentally flawed?

### Core Problems
1. Compare BERT, RoBERTa, and DeBERTa in terms of what changed: which improvements came from training recipe changes, and which came from architectural changes?
2. Explain why modern retrieval systems often prefer encoder embeddings such as E5 or BGE over using a generative decoder model directly as the retrieval representation.

### Challenge
1. Trace the conceptual shift from MLM-based fine-tuning to contrastive embedding training and argue why that transition made encoder-only models central to the RAG ecosystem.

---

*See also:* [[Transformer Architecture]], [[Attention Mechanism]], [[Embeddings and Vector Databases]], [[Scaling Laws]], [[Mechanistic Interpretability]]

## References
- Evidence chunks and raw source notes are reachable through [[LLM/LLM Corpus Index|LLM Corpus Index]] and [[LLM/Sources/Sources Index|LLM Sources Index]].

- [[Transformer Architecture]] — the shared foundation architecture for all encoder models
- [[Attention Mechanism]] — bidirectional self-attention that drives encoder representations
- [[Embeddings and Vector Databases]] — encoder models power modern embedding retrieval
- [[Scaling Laws]] — how encoder model performance scales with compute and data
- [[Mechanistic Interpretability]] — probing and interpreting encoder representations
- [[LLM/Sources/Sources Index]]
