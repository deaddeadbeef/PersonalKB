---
tags: [llm, rag]
up: "[[2023 — Open Models and Agents Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Reranking

> **One-line summary** Reranking improves RAG quality by taking a fast first-pass retrieval result set and rescoring it with a stronger relevance model before sending context to the LLM.

## 🎯 Intuition

**The Core Idea:**  
Reranking is a second-stage retrieval step that corrects the rough ordering produced by a fast retriever. The first stage casts a wide net; the reranker decides which candidates are actually the best matches for the query.

**Analogy:**  
It is like using a search engine to gather a pile of promising books, then handing that shortlist to a specialist librarian who carefully reorders them based on what your question really means.

**Why It Matters:**  
Many RAG failures happen not because the right passage was never retrieved, but because it was retrieved too low in the list. Reranking is often the most efficient way to improve precision without rebuilding the whole retrieval system.

---

## ⚙️ Core Mechanics

### How It Works

Reranking is a second-stage retrieval step that takes the top-N candidates from a fast but approximate first-stage retriever and rescores them with a more powerful—but slower—model. This two-stage architecture lets RAG systems combine the speed of bi-encoder retrieval with the accuracy of cross-encoder relevance classification.

A **bi-encoder** (the first stage) independently encodes the query and each passage into separate vectors, then scores by cosine similarity. This is fast because passage embeddings are precomputed and indexed, but the model never sees query and passage together—it cannot capture fine-grained token-level interactions between them. A **cross-encoder** (the reranker) concatenates the query and a candidate passage into a single input sequence, processes them jointly through a transformer, and outputs a relevance score. Because it attends across all query-passage token pairs simultaneously, it captures nuances that bi-encoders miss: negation, qualifier words, entity-attribute binding, and subtle relevance distinctions.

The typical pipeline retrieves 50–200 candidates via the bi-encoder, then reranks the top 20–50 with a cross-encoder, and passes the top 5–10 to the LLM. This narrows the computational cost—cross-encoders are $O(n)$ per candidate with no precomputation—while dramatically improving precision. In practice, reranking yields 5–15% improvement in precision@k and often noticeably better final answer quality.

**ColBERT** offers a middle ground via "late interaction": query and document tokens are independently encoded into per-token embeddings, then similarity is computed via MaxSim (maximum similarity between each query token and all document tokens). This preserves precomputation benefits while capturing richer interactions than a single-vector bi-encoder. Hosted reranking APIs like **Cohere Rerank** and **Jina Reranker** abstract away model serving, accepting a query and candidate list and returning reranked results.

### Key Specifications

- **Bi-encoder (stage 1)**: Encode query and passages independently. Score = cosine(q_vec, p_vec). Fast, scalable, precomputable.
- **Cross-encoder (stage 2)**: Input = `[CLS] query [SEP] passage [SEP]`. Output = relevance logit. Accurate but $O(n)$ per pair, no precomputation.
- **ColBERT late interaction**: Per-token embeddings for query and document. `score = Σ_i max_j sim(q_i, d_j)`. Faster than cross-encoder, richer than bi-encoder.
- **Cohere Rerank API**: Send query + list of documents, receive relevance scores. Models: `rerank-english-v3.0`, `rerank-multilingual-v3.0`.
- **Typical improvement**: 5–15% precision@k gain. Larger gains when first-stage retrieval is noisy or when queries are complex/multi-faceted.
- **Candidate budget**: Retrieve 50–200 from bi-encoder → rerank top 20–50 → pass top 5–10 to LLM. Exact numbers depend on latency budget.
- **When to rerank**: When retrieval precision matters more than latency; when queries are complex or ambiguous; when the first-stage retriever has mediocre quality.
- **When to skip**: Ultra-low-latency requirements; already high retrieval quality; very small corpus where top-k is likely correct.

### Key Facts

Reranking is one of the highest-ROI additions to a RAG pipeline. The first-stage retriever must be fast and therefore makes approximations; the reranker corrects those approximations at manageable cost. For many production systems, adding a reranker is the single change that moves answer quality from "acceptable" to "good"—especially on complex queries where the right passage is retrieved but not ranked first.

| Method | Interaction | Speed | Accuracy | Precomputable |
| --- | --- | --- | --- | --- |
| Bi-encoder | None (independent) | Very fast | Good | Yes |
| Cross-encoder | Full (joint) | Slow | Excellent | No |
| ColBERT | Late (per-token) | Moderate | Very good | Partially |

---

## 🔬 Deep Dive

### Technical Details

The core tradeoff in reranking is interaction quality versus computational cost. Bi-encoders are efficient because they represent query and document separately, enabling approximate nearest-neighbor search over precomputed embeddings. But that efficiency comes from discarding direct token-level interaction during scoring.

Cross-encoders reverse that tradeoff. They jointly process query and candidate passage, which lets them understand relationships that cosine similarity often misses: negation, qualifiers, entity-role mismatches, and subtle relevance cues. The downside is that every query-document pair must be scored from scratch.

ColBERT occupies a useful middle ground. By preserving token-level representations and computing MaxSim, it captures richer structure than a single-vector retriever while retaining some of the benefits of precomputation. This makes it attractive when teams want more accuracy than a bi-encoder can offer but lower cost than a full cross-encoder.

### Limitations and Criticisms

The obvious limitation is latency and cost. Reranking adds another stage, and cross-encoders scale with the number of candidates rescored. If the candidate set is too large, latency can become unacceptable.

Reranking is also not magic. It can only improve ordering within the candidate pool it receives. If the correct passage never enters the first-stage top-N, the reranker cannot recover it. That means reranking complements retrieval quality; it does not replace it.

### Impact and Legacy

Reranking became a standard production pattern because it offers a practical compromise between retrieval speed and answer quality. Instead of forcing teams to choose between very fast but shallow retrieval and very accurate but expensive full matching, the two-stage architecture gives them both in a controlled budget.

Its lasting impact is architectural: many modern RAG systems assume a first-stage retriever plus a second-stage reranker as a default design, especially in enterprise and search-heavy settings where precision at the top of the list matters most.

---

## 🏋️ Practice

### Warm-Up (5 min)

1. What does a bi-encoder do in stage 1 retrieval?
2. Why is a cross-encoder usually more accurate than a bi-encoder?
3. What problem does reranking solve in a RAG pipeline?

### Core Problems

1. Compare bi-encoder retrieval, cross-encoder reranking, and ColBERT across speed, interaction richness, and deployment tradeoffs.
2. Explain why reranking often improves final answer quality even though it does not change the base LLM.
3. Given a fixed latency budget, how would you choose candidate counts for first-stage retrieval, reranking, and final context selection?
4. Why can reranking not fix a true retrieval miss?

### Challenge

Design a retrieval pipeline for a medium-size enterprise knowledge base. Choose whether to use only a bi-encoder, a bi-encoder plus cross-encoder reranker, or ColBERT-style late interaction. Justify the choice in terms of accuracy, latency, candidate budget, and operational complexity.

For a local applied workflow, use [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab|Local RAG Retrieval Evaluation and Reranking Lab]] to compare first relevant rank, context precision, and latency before and after reranking.

## Supporting Chunks / References

### Supporting Chunks

*(To be populated as chunks are created)*

### References

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab]]
