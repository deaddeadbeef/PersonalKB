---
tags: [chunk, llm]
id: "chunk-llm-172"
source: "[[LLM/_raw/raw-llm-043 SentencePiece]]"
source_loc: "Why It Matters"
topic: "SentencePiece adoption"
claim: "SentencePiece became the de facto tokenizer for multilingual and open-source LLMs, including LLaMA, T5, and mBART."
confidence: "verified"
supports:
  - "[[LLM/Architecture Variants/Architecture Variants]]"
qna_seeds:
  - "Q: Which major LLMs use SentencePiece? A: T5, mBART, LLaMA (1/2/3), PaLM, and many other open-source models use SentencePiece for tokenization."
  - "Q: What is the main alternative to SentencePiece? A: OpenAI's tiktoken (BPE-based, used for GPT-3.5/4) and HuggingFace Tokenizers are alternatives, but SentencePiece dominates the open-source multilingual model ecosystem."
up: "[[LLM/LLM]]"
---

# SentencePiece Is the De Facto LLM Tokenizer

SentencePiece's combination of language independence, lossless reversibility, and support for both BPE and Unigram algorithms made it the standard tokenizer for the open-source LLM ecosystem. It is used by T5, mBART, LLaMA (all versions), PaLM, and many other major models. Its C++ implementation provides fast training and inference, and its model files are self-contained and portable. The main alternative is OpenAI's tiktoken (used for GPT-3.5/4), which is also BPE-based but tightly coupled to OpenAI's vocabulary. SentencePiece's open-source flexibility cemented its role as the default choice.
