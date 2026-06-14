---
status: done
area: LLM
created: 2026-06-15
completed: 2026-06-15
---

# Local Embedding and Reranker Hosting Lab

## Outcome

Added [[LLM/Study/Local Embedding and Reranker Hosting Lab|Local Embedding and Reranker Hosting Lab]] to close the applied gap between RAG theory and the local inference services that create embeddings and rerank candidates.

## Coverage Added

- Provider choice map for Ollama, LM Studio, llama.cpp, vLLM, SGLang, TEI, and Sentence Transformers.
- Endpoint smoke tests for embedding vector shape, normalization, batching, truncation, latency, and route compatibility.
- Service card for local embedding/reranker providers.
- Index compatibility rules for dimension, metric, corpus version, model id, and reindex triggers.
- Provider A/B retrieval comparison row.
- Reranker endpoint smoke test and keep/skip decision row.
- Operational checks for loopback binding, logs, caches, private corpora, and reranker payloads.

## Routing

Linked the lab from the main LLM map, study index, mastery roadmap, capstone workbook, self-assessment, RAG assistant lab, retrieval evaluation lab, minimal Python harness, runtime matrix, benchmark log, quality harness, deployment matrix, embeddings note, reranking note, and mechanism bridge.

## Sources Checked

- Ollama embeddings
- LM Studio embeddings
- llama.cpp server
- vLLM embedding usages
- SGLang embedding and rerank model docs
- Hugging Face Text Embeddings Inference and TEI quick tour
- Sentence Transformers retrieve and rerank
