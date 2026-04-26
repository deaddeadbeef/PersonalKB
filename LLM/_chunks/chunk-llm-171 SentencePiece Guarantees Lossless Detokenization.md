---
tags: [chunk, llm]
id: "chunk-llm-171"
source: "[[LLM/_raw/raw-llm-043 SentencePiece]]"
source_loc: "Chunk Candidates"
topic: "Lossless detokenization"
claim: "SentencePiece guarantees lossless round-trip tokenization — any tokenized sequence can be perfectly reconstructed back to the original text, including whitespace."
confidence: "verified"
supports:
  - "[[LLM/Architecture Variants/Architecture Variants]]"
qna_seeds:
  - "Q: What does lossless detokenization mean? A: The tokenizer can perfectly reconstruct the original raw text from the token sequence, including exact whitespace, punctuation, and special characters — no information is lost."
  - "Q: How does SentencePiece achieve lossless round-trips? A: By encoding whitespace as an explicit meta-symbol in the vocabulary rather than stripping it during pre-processing, every character in the original input is represented in the token sequence."
up: "[[LLM/LLM]]"
---

# SentencePiece Guarantees Lossless Detokenization

SentencePiece guarantees that tokenization is perfectly reversible: decode(encode(text)) == text for any input. This is achieved by treating whitespace as an explicit token-internal symbol rather than stripping or normalizing it during pre-processing. The lossless property is critical for language models that must generate exact text (code, structured output, multilingual content). Many earlier tokenizers (e.g., WordPiece in BERT) lose whitespace information, requiring heuristic reconstruction. SentencePiece's lossless guarantee made it the standard for generative LLMs.
