---
tags: [chunk, llm]
id: "chunk-llm-093"
source: "[[LLM/_raw/raw-llm-024 RAG Retrieval-Augmented Generation]]"
source_loc: "What Is This, Key Takeaways 1"
topic: "RAG parametric plus retrieval architecture"
claim: "RAG combines a parametric language model with a non-parametric retrieval component, allowing the model to access external knowledge at inference time."
confidence: "verified"
supports: ["[[LLM/Retrieval-Augmented Generation/Retrieval Pipelines and Context Assembly]]"]
up: "[[LLM/LLM]]"
---

# RAG Combines Parametric and Non-Parametric Knowledge

## Context
Retrieval-Augmented Generation (RAG) introduced a hybrid architecture that pairs a parametric seq2seq generator (BART) with a non-parametric retrieval component (Dense Passage Retrieval over Wikipedia). At inference time, the retriever fetches the top-k most relevant documents for a given query, and the generator conditions its output on both the query and the retrieved passages via cross-attention.

The original paper presented two variants: RAG-Sequence, where the same retrieved document is used to generate the entire output sequence, and RAG-Token, where different documents can influence different tokens in the output. Both variants use marginalization over retrieved documents during training, jointly optimizing the retriever and generator end-to-end.

## Why It Matters
RAG formalized the retrieve-then-generate pattern that became the dominant approach for knowledge-grounded LLM applications. By separating knowledge storage (in the retrieval index) from reasoning (in the generator), RAG enabled systems that can be updated with new knowledge without retraining the language model — a critical requirement for production deployments.

## QnA Seeds
- Q: What are the two components of the RAG architecture?
  A: A parametric seq2seq generator (BART) that produces output, and a non-parametric retriever (DPR) that fetches relevant documents from an external corpus at inference time.
- Q: What are the two RAG variants and how do they differ?
  A: RAG-Sequence uses the same retrieved document for the entire output, while RAG-Token allows different retrieved documents to influence different output tokens.
