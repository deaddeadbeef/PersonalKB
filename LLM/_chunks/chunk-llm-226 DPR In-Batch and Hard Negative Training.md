---
tags: [chunk, llm]
id: "chunk-llm-226"
source: "[[LLM/_raw/raw-llm-057 Dense Passage Retrieval DPR]]"
source_loc: "Chunk Candidates"
topic: "DPR in-batch negatives training"
claim: "DPR trains with in-batch negatives and hard negative mining via BM25, using contrastive learning to separate relevant from irrelevant passages."
confidence: "verified"
supports: ["[[LLM/2023 — Open Models and Agents/Embeddings and Vector Databases]]"]
qna_seeds:
  - q: "What is the in-batch negatives training strategy in DPR?"
    a: "For each question in a training batch, all other questions' positive passages serve as negative examples, providing O(B²) training pairs from a batch of size B without additional retrieval."
  - q: "Why does DPR use BM25 hard negatives?"
    a: "BM25 hard negatives are passages that are lexically similar to the question but not the correct answer — they force the model to learn semantic relevance beyond surface-level keyword matching, which is critical for surpassing sparse retrieval."
up: "[[LLM/LLM]]"
---
# DPR Trains with In-Batch Negatives and Hard Negative Mining

DPR uses a contrastive learning objective where the model must maximize the dot-product similarity between a question and its gold passage while minimizing similarity with negative passages. Two sources of negatives are used: in-batch negatives (other questions' positive passages in the same batch) and BM25 hard negatives (passages that are lexically similar but semantically irrelevant).

In-batch negatives provide efficient O(B²) training pairs from a batch of size B at negligible computational cost. BM25 hard negatives are more challenging — they contain keyword overlap with the question but lack the correct answer, forcing the encoders to learn genuine semantic matching rather than lexical shortcuts. The combination of easy (in-batch) and hard (BM25) negatives produces a robust embedding space that significantly outperforms BM25 retrieval on knowledge-intensive QA benchmarks.
