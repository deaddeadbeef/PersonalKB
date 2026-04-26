---
tags: [llm, rag]
up: "[[2023 — Open Models and Agents Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Hybrid Search
> **One-line summary:** Hybrid search improves retrieval by combining semantic vector search with exact lexical matching.

---

## 🎯 Intuition

### Core Idea
Hybrid search combines dense retrieval (embedding-based semantic similarity) with sparse retrieval (lexical matching via BM25 or TF-IDF) to capture both the meaning of a query and its exact surface-level terms. In practice, this fusion consistently outperforms either method alone across a wide range of retrieval benchmarks and real-world RAG deployments.

Dense retrieval encodes queries and passages into embedding vectors and ranks by cosine similarity. It excels at paraphrase, synonymy, and conceptual matching—"automobile repair" retrieves documents about "car maintenance." But it struggles with rare tokens, proper nouns, acronyms, and exact-match requirements where a single keyword is the critical signal. Sparse retrieval (BM25) counts term frequencies, penalizes common words via inverse document frequency, and ranks by lexical overlap. It handles exact keywords and rare terms reliably but misses semantic equivalence entirely.

### Analogy
Hybrid search is like checking both the card catalog AND asking the librarian.

### Why It Matters
In production RAG systems, hybrid search is often the default recommendation because it hedges against both types of retrieval failure at minimal additional cost. Running a BM25 index alongside a vector index is cheap—BM25 is fast and memory-efficient—and the recall improvement from fusion is consistent. Many teams report 5–15% recall gains from moving to hybrid, which translates directly into better downstream answer quality.

---

## ⚙️ Core Mechanics

### How It Works
Hybrid search runs both retrievers in parallel and fuses their ranked result lists. The most common fusion method is **Reciprocal Rank Fusion (RRF)**: for each document, compute `score = Σ 1/(k + rank_i)` across retrievers, where `k` is a constant (typically 60) that dampens the influence of high ranks. RRF is parameter-light, doesn't require score normalization, and is surprisingly robust.

Alternative approaches include weighted linear combination of normalized scores (`α × dense_score + (1 − α) × sparse_score`), where α is tuned on a validation set, and learned fusion models that train a small ranker on top of both score signals.

The key insight is that dense and sparse retrievers make *different* errors. Dense retrieval might miss a document containing an obscure product code even though it's perfectly relevant; sparse retrieval will catch it via exact match. Conversely, sparse retrieval fails when the user phrases a query differently from the document's wording; dense retrieval bridges that gap. Hybrid search exploits this complementarity.

### Key Specifications
- **BM25**: `score(q, d) = Σ IDF(t) × (tf(t,d) × (k1+1)) / (tf(t,d) + k1 × (1 − b + b × |d|/avgdl))`. Standard sparse baseline. Parameters `k1` (term saturation) and `b` (length normalization) typically default to 1.2 and 0.75.
- **Reciprocal Rank Fusion (RRF)**: `score(d) = Σ_r 1/(k + rank_r(d))` with `k = 60`. Merges ranked lists without requiring score calibration.
- **Weighted scoring**: `α × normalize(dense_score) + (1 − α) × normalize(sparse_score)`. Requires score normalization (min-max or z-score) since dense and sparse scores live on different scales.
- **When sparse beats dense**: Exact keyword matching, rare/domain-specific terms, product IDs, acronyms, code identifiers.
- **When dense beats sparse**: Paraphrase, synonymy, cross-lingual queries, conceptual similarity, natural-language questions.
- **Infrastructure**: Weaviate, Qdrant, and Elasticsearch natively support hybrid search. For FAISS + BM25, you typically run both and fuse externally.

### Key Facts
- Dense and sparse retrieval fail in different ways, which is why fusion helps.
- RRF is popular because it is robust and parameter-light.
- Hybrid usually adds only modest latency if both retrievers run in parallel.
- Many teams report **5–15% recall gains** from moving to hybrid retrieval.


| Dimension | Dense Retrieval | Sparse Retrieval (BM25) | Hybrid |
| --- | --- | --- | --- |
| Signal | Semantic similarity | Lexical overlap | Both |
| Strengths | Paraphrase, synonymy | Exact match, rare terms | Complementary coverage |
| Weaknesses | Rare tokens, exact match | No semantic understanding | Slightly more complex |
| Typical latency | ~10–50 ms (ANN) | ~5–20 ms | ~20–60 ms (parallel) |
| Fusion method | — | — | RRF or weighted scoring |

---

## 🔬 Deep Dive

### Technical Details
The main technical issue in hybrid search is fusion. Dense and sparse scores live on different scales, so direct score addition is brittle unless you normalize carefully. That is why RRF is so widely used: it works on ranks instead of raw scores. Learned fusion can outperform simple heuristics, but it needs validation data and adds operational complexity.

### Limitations
Hybrid search is not free. You now run two retrieval systems and have to manage fusion logic, tuning, and sometimes two storage layers. Weighted scoring can be unstable if normalization is poor. Learned fusion adds the cost of training and maintenance.

### Impact
Despite that added complexity, hybrid search is often the safest production default because it protects against exact-match misses and semantic misses at the same time.

---

## 🏋️ Practice

### Warm-Up
1. What kind of query is BM25 especially good at?
2. Why can dense retrieval miss a product code or acronym?
3. What does RRF combine: scores or ranks?

### Core Problems
1. A user searches with a rare internal error code. Which retrieval signal is most likely to catch it first?
2. A user asks a paraphrased question that shares few keywords with the source text. Which retrieval signal helps more?
3. Why is hybrid often stronger than either retriever alone?

### Challenge
Design a retrieval stack for an enterprise wiki that contains product SKUs, acronyms, and messy natural-language questions. Explain whether you would use RRF, weighted fusion, or a learned ranker.

---

## Supporting Chunks / References

### Supporting Chunks
*(To be populated as chunks are created)*

### References
- [[LLM/Sources/Sources Index]]
