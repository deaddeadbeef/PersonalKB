---
tags: [study, llm, drill]
up: "[[LLM/Study/LLM Study Index]]"
---

# RAG & Prompting — Review Drill

## Quick-Fire Questions

1. **What is the full RAG pipeline?**
   Query → (optional transform) → Retrieve → Rerank → Assemble context → Generate. Each stage can fail independently.

2. **Dense vs sparse retrieval — when does each win?**
   Dense (embeddings): semantic similarity, paraphrased queries. Sparse (BM25): exact keywords, rare terms, entity names. Hybrid combines both.

3. **What is reciprocal rank fusion (RRF)?**
   Merge ranked lists by scoring each document as Σ 1/(k + rank_i). Simple, parameter-free way to combine multiple retrieval methods.

4. **Bi-encoder vs cross-encoder for retrieval?**
   Bi-encoder: encode query and doc independently, fast (precompute doc embeddings). Cross-encoder: encode query+doc together, much more accurate but too slow for initial retrieval. → Two-stage: bi-encoder retrieves, cross-encoder reranks.

5. **What is the "Lost in the Middle" problem?**
   LLMs attend more to the beginning and end of long contexts, potentially missing information placed in the middle. Put important context at the start or end.

6. **Chain-of-thought: why does it only work at scale?**
   Smaller models lack the capacity to maintain coherent multi-step reasoning. CoT requires sufficient model capability to decompose problems and track intermediate results.

7. **What is HyDE (Hypothetical Document Embedding)?**
   Generate a hypothetical answer to the query, embed that, use it for retrieval. The hypothesis is often closer to relevant documents in embedding space than the original question.

8. **Grammar-constrained decoding — how does it work?**
   At each token generation step, restrict the probability distribution to only tokens that are valid according to a grammar/schema. Guarantees syntactically valid output (JSON, SQL, etc.).

9. **What are the main RAG failure modes?**
   Retrieval miss (relevant doc not found), context poisoning (irrelevant doc misleads), extraction failure (model ignores relevant context), hallucination despite context.

10. **When to use RAG vs fine-tuning vs long context?**
    RAG: dynamic/changing knowledge, attribution needed. Fine-tuning: consistent behavioral changes, domain adaptation. Long context: when all info fits and you want simplicity.
