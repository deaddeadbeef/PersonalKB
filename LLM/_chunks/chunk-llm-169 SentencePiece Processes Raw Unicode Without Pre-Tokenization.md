---
tags: [chunk, llm]
id: "chunk-llm-169"
source: "[[LLM/_raw/raw-llm-043 SentencePiece]]"
source_loc: "What Is This, Chunk Candidates"
topic: "SentencePiece raw Unicode processing"
claim: "SentencePiece treats input text as a raw Unicode byte stream with no language-specific pre-tokenization, making it truly language-independent."
confidence: "verified"
supports:
  - "[[LLM/Architecture Variants/Architecture Variants]]"
qna_seeds:
  - "Q: How does SentencePiece handle input text? A: It treats the entire input as a raw Unicode stream, using a special whitespace meta-symbol, without assuming word boundaries or requiring language-specific tokenizers."
  - "Q: Why is avoiding pre-tokenization important? A: Pre-tokenization rules (word splitting, punctuation handling) are language-specific; by operating on raw characters/bytes, SentencePiece works equally well for English, Chinese, Japanese, Arabic, or any script."
up: "[[LLM/LLM]]"
---

# SentencePiece Processes Raw Unicode Without Pre-Tokenization

SentencePiece's key design decision is treating input text as a raw sequence of Unicode characters (or bytes) rather than assuming pre-tokenized words. It uses a special meta-symbol to represent whitespace, allowing the model to learn subword units that may span word boundaries. This eliminates the need for language-specific pre-processing rules like word segmentation for Chinese/Japanese or morphological analysis for agglutinative languages. The approach makes SentencePiece truly language-agnostic — the same algorithm and configuration works for any writing system.
