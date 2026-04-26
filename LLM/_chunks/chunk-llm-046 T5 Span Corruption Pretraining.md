---
tags: [chunk, llm]
id: "chunk-llm-046"
source: "[[LLM/_raw/raw-llm-012 T5 Unified Text-to-Text Transformer]]"
source_loc: "Key Takeaways 3"
topic: "T5 span corruption objective"
claim: "T5 uses span corruption pretraining: replace random spans with sentinel tokens and predict the missing spans."
confidence: "verified"
supports: ["[[LLM/Pretraining/Language Modeling Objectives]]"]
up: "[[LLM/LLM]]"
---

# T5 Span Corruption Pretraining

## Context
T5's pretraining objective — span corruption — randomly selects contiguous spans of tokens in the input, replaces each span with a unique sentinel token (e.g., `<extra_id_0>`, `<extra_id_1>`), and trains the model to generate the missing spans preceded by their corresponding sentinel tokens. This is a denoising autoencoder objective framed in the text-to-text format.

Compared to BERT's masked language modeling (which masks individual tokens), span corruption is more efficient because the target sequence is shorter — it contains only the corrupted spans rather than the full input. The systematic comparison in the T5 paper showed that span corruption with a 15% corruption rate and average span length of 3 tokens outperformed both standard language modeling and BERT-style token masking on downstream tasks.

## Why It Matters
Span corruption proved to be a more compute-efficient pretraining objective than alternatives because the decoder processes fewer tokens (just the masked spans) while the encoder processes the full context. This efficiency advantage influenced later encoder-decoder models and demonstrated that the choice of pretraining objective has a measurable impact on downstream task quality.

## QnA Seeds
- Q: How does T5's span corruption differ from BERT's masked language modeling?
  A: BERT masks individual tokens and predicts them independently. T5's span corruption replaces contiguous multi-token spans with sentinel tokens, then generates all missing spans sequentially. This is more efficient because the target sequence is shorter (only missing spans, not the full input).
- Q: What span corruption hyperparameters did T5 find most effective?
  A: A corruption rate of 15% (fraction of tokens replaced) with an average span length of 3 tokens. This configuration outperformed single-token masking, full-sequence language modeling, and other denoising variants in their systematic comparison.
