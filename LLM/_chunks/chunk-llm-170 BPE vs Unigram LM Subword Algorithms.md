---
tags: [chunk, llm]
id: "chunk-llm-170"
source: "[[LLM/_raw/raw-llm-043 SentencePiece]]"
source_loc: "What Is This, Chunk Candidates"
topic: "BPE vs Unigram in SentencePiece"
claim: "SentencePiece implements both Byte-Pair Encoding (BPE) and Unigram Language Model subword segmentation, with BPE building vocabulary bottom-up by merging frequent pairs and Unigram pruning top-down from a large initial vocabulary."
confidence: "verified"
supports:
  - "[[LLM/Architecture Variants/Architecture Variants]]"
qna_seeds:
  - "Q: What two subword algorithms does SentencePiece support? A: BPE (byte-pair encoding), which iteratively merges the most frequent adjacent pairs bottom-up, and Unigram LM, which starts with a large vocabulary and prunes tokens top-down based on likelihood."
  - "Q: When would you choose Unigram over BPE? A: Unigram produces a probabilistic model over segmentations and can output multiple segmentation candidates with probabilities, which can serve as data augmentation during training."
up: "[[LLM/LLM]]"
---

# BPE vs Unigram LM Subword Algorithms

SentencePiece provides two subword segmentation algorithms in a unified framework. BPE (Byte-Pair Encoding) starts with individual characters and iteratively merges the most frequent adjacent pair until the target vocabulary size is reached — it is deterministic and widely used (GPT family, LLaMA). The Unigram Language Model approach starts with a large candidate vocabulary and iteratively removes tokens whose removal least reduces the corpus likelihood, producing a probabilistic segmentation. Unigram can generate multiple valid segmentations with probabilities, enabling subword regularization as a form of data augmentation during training.
