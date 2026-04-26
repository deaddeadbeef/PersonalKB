---
tags: [chunk, llm]
id: "chunk-llm-225"
source: "[[LLM/_raw/raw-llm-057 Dense Passage Retrieval DPR]]"
source_loc: "What Is This, Chunk Candidates"
topic: "DPR dual-encoder architecture"
claim: "DPR uses separate BERT encoders for questions and passages with dot-product similarity, replacing sparse retrieval for open-domain QA."
confidence: "verified"
supports: ["[[LLM/2023 — Open Models and Agents/Embeddings and Vector Databases]]", "[[LLM/2020–2021 — The Scaling Era/Retrieval Pipelines and Context Assembly]]"]
qna_seeds:
  - q: "What is DPR's dual-encoder architecture?"
    a: "Two independently fine-tuned BERT-base models encode questions and passages into dense vectors, and retrieval is performed via maximum inner product search (dot product) over pre-computed passage embeddings."
  - q: "Why use separate encoders for questions and passages?"
    a: "Separate encoders allow passages to be pre-encoded and indexed offline, so retrieval at query time only requires encoding the question and performing a fast approximate nearest neighbor search — enabling sub-second retrieval over millions of passages."
up: "[[LLM/LLM]]"
---
# DPR Uses Dual BERT Encoders for Dense Retrieval

Dense Passage Retrieval (DPR) introduced the dual-encoder architecture for open-domain question answering, using two independently fine-tuned BERT-base models: one encodes questions into dense vectors and one encodes passages. Retrieval is performed via maximum inner product search (dot product) between the question vector and pre-computed passage vectors stored in a FAISS index.

The dual-encoder design enables practical deployment because all passage embeddings can be pre-computed and indexed offline. At query time, only the question needs to be encoded (a single BERT forward pass), followed by an approximate nearest neighbor search that retrieves the top-k passages in milliseconds even over corpora of 21 million passages (the full English Wikipedia). This efficiency made DPR the template for all subsequent dense retrieval systems and the backbone of Retrieval-Augmented Generation (RAG) pipelines.
