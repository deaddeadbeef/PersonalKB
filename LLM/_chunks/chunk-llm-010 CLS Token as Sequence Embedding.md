---
tags: [chunk, llm]
id: "chunk-llm-010"
source: "[[LLM/_raw/raw-llm-003 BERT Pre-training of Deep Bidirectional Transformers]]"
source_loc: "Section 3, Section 4"
topic: "sequence representation"
claim: "BERT's [CLS] token representation serves as a fixed-size sequence embedding for classification tasks"
confidence: "verified"
supports: ["[[LLM/Architecture Variants/Encoder-Only Models]]"]
up: "[[LLM/LLM]]"
---

# CLS Token as Sequence Embedding

## Context

BERT prepends a special [CLS] token to every input sequence. After processing through all Transformer layers, the final hidden state of this [CLS] token serves as an aggregate representation of the entire sequence. For classification tasks (sentiment analysis, NLI, etc.), a simple linear classifier is added on top of the [CLS] representation, and the entire model is fine-tuned end-to-end.

The [CLS] token works because self-attention allows it to attend to every other token in the sequence. Through the multiple layers of the Transformer, the [CLS] position accumulates information from the full input. During pre-training, the Next Sentence Prediction (NSP) objective specifically uses the [CLS] representation, giving it an incentive to encode sequence-level meaning. For tasks requiring token-level predictions (like NER), the individual token representations are used instead.

## Why It Matters

The [CLS] token approach established a simple, effective pattern for extracting fixed-size representations from variable-length sequences. This design influenced sentence embedding models (Sentence-BERT), cross-encoders for retrieval, and became the standard interface between Transformer encoders and downstream classification heads. It demonstrated that a single token position can serve as an information bottleneck for entire sequences.

## QnA Seeds
- Q: Why use a special [CLS] token instead of pooling all token representations?
  A: The [CLS] token provides a dedicated position for aggregating sequence-level information without disrupting the representations of actual input tokens. Mean-pooling or max-pooling over all tokens can also work (and sometimes works better, as shown by Sentence-BERT), but the [CLS] approach has the advantage of being specifically trained for sequence-level tasks through the NSP objective.
- Q: Does the [CLS] token always produce good sentence embeddings?
  A: Not out-of-the-box for similarity tasks. Research (Reimers & Gurevych, 2019) showed that BERT's [CLS] embeddings without fine-tuning are poor for semantic similarity — they can be outperformed by simple GloVe averaging. Sentence-BERT fine-tunes with a siamese/triplet objective to produce embeddings where cosine similarity correlates with semantic similarity.
