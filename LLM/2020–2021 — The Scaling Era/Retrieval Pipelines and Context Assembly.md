---
tags: [llm, rag]
up: "[[2020–2021 — The Scaling Era Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Retrieval Pipelines and Context Assembly

> **Strong RAG systems depend not just on retrieval itself but on how queries are transformed, results reranked, and context assembled before generation.**

## 🎯 Intuition
**The Core Idea:** Production RAG works best as a multi-stage pipeline—query transformation, retrieval, reranking, and context assembly—rather than a simple query → top-k → generate loop.
**Analogy:** A good retrieval pipeline is like a research assistant who rewrites your question, searches multiple catalogs, ranks the best sources, and hands you a carefully ordered packet before you start writing.
**Why It Matters:** The design of the retrieval pipeline, and especially how retrieved context is packed and ordered in the prompt, has a direct and measurable impact on answer quality. A strong pipeline lets embeddings, chunking, search, reranking, and citation behavior reinforce one another, while a naive pipeline wastes even excellent components. It also shapes a recurring architectural choice between RAG, fine-tuning, and long-context ingestion depending on whether knowledge is dynamic, attribution matters, or token cost dominates.

---

## ⚙️ Core Mechanics
### How It Works
- A full RAG pipeline orchestrates multiple stages—query transformation, retrieval, reranking, and context assembly—to deliver the most relevant information to the language model in the most usable form.
- The canonical RAG pipeline flows as: **query → transform → retrieve → rerank → assemble → generate**.
- Each stage is a lever for improvement, and production systems rarely use just raw query → top-k → generate.

**Query transformation:**
- **Query transformation** reshapes the user's question before it hits the retriever.
- **HyDE** (Hypothetical Document Embeddings) asks the LLM to generate a hypothetical answer, then uses that answer's embedding as the search query—this bridges the query-document distribution gap since documents look more like answers than questions.
- **Query expansion** adds synonyms or related terms.
- **Multi-query** generates multiple rephrased versions of the question, retrieves for each, and merges results—capturing different facets of ambiguous queries.

**Multi-hop retrieval:**
- **Multi-hop retrieval** handles questions that require synthesizing information from multiple passages.
- The system retrieves an initial set of passages, extracts intermediate findings, formulates follow-up queries, and retrieves again—iterating until the question is answerable.
- This is essential for complex reasoning tasks ("What was the GDP growth rate of the country where the inventor of the transistor was born?").

**Context assembly:**
- **Context assembly** is where retrieved passages become a prompt.
- Key decisions include: how many passages to include (trading recall against context window noise), what order to place them in (front and back positions receive more attention per the "Lost in the Middle" finding), whether to include passage metadata (source, date) for citation, and how to frame the instruction to the LLM.
- Citation tracking—mapping each claim in the generated answer back to a specific retrieved passage—is increasingly expected in production systems.

**Pipeline patterns:**
- **HyDE**: Query → LLM generates hypothetical answer → embed hypothetical answer → retrieve. Effective when queries are short or keyword-like.
- **Multi-query**: Query → LLM generates 3–5 rephrasings → retrieve for each → deduplicate and fuse results (RRF or union).
- **Query expansion**: Append synonyms, acronyms, or related terms to the original query before retrieval.
- **Multi-hop retrieval**: Retrieve → extract entities/claims → generate follow-up queries → retrieve again. Repeat 2–3 hops.
- **Context window packing**: Fill the context window with retrieved passages up to the token budget. Prioritize by reranker score.
- **Passage ordering**: Place the most relevant passages first and last (primacy/recency bias). Bury lower-relevance passages in the middle.
- **Citation tracking**: Tag each passage with an ID; instruct the LLM to cite `[1]`, `[2]`, etc. Verify citations post-generation.
- **Naive RAG**: Query → embed → top-k → generate. No transformation, no reranking.
- **Advanced RAG**: Full pipeline with query transformation, hybrid search, reranking, multi-hop, citation tracking.
- **RAG vs fine-tuning**: RAG for dynamic/frequently updated knowledge; fine-tuning for teaching style, format, or domain reasoning.
- **RAG vs long context**: Long context windows (128k–1M tokens) can ingest whole documents, but retrieval is still more cost-effective and precise for large corpora.

### Key Specifications

| Approach | Dynamic Knowledge | Source Attribution | Cost at Scale | Reasoning Depth |
|---|---|---|---|---|
| Naive RAG | ✅ | Weak | Low | Shallow |
| Advanced RAG | ✅ | Strong | Moderate | Moderate–Deep |
| Fine-tuning | ❌ (static) | ❌ | High (training) | Deep |
| Long context | ✅ | Moderate | High (tokens) | Moderate |

### Key Facts
- Production RAG rarely stops at simple top-k retrieval; it usually improves the query, reranks results, and carefully assembles context.
- HyDE helps bridge the query-document distribution gap by retrieving from a hypothetical answer instead of the original question alone.
- Multi-hop retrieval is necessary when the answer depends on combining evidence from multiple passages.
- Passage ordering matters because models attend more strongly to content placed early and late in the context window.
- Retrieval remains more cost-effective and precise than brute-force long-context ingestion for large corpora.

---

## 🔬 Deep Dive
### Technical Details
- Query transformation can include HyDE, synonym expansion, acronym expansion, and multi-query generation.
- Multi-query systems often generate 3–5 rephrasings, retrieve for each, then deduplicate and fuse results with strategies such as RRF or union.
- Multi-hop retrieval iterates through retrieve → extract intermediate findings → generate follow-up queries → retrieve again, typically for 2–3 hops.
- Context packing must operate within a token budget, so reranker score and ordering policy determine which passages survive.
- Metadata such as source or date can be included in the assembled prompt to support citation and provenance.
- Citation tracking requires mapping generated claims back to tagged retrieved passages and verifying those citations after generation.

### Limitations and Criticisms
- Adding too many passages can improve recall but also introduces context-window noise, making assembly quality a bottleneck.
- Naive RAG pipelines underperform because they skip query transformation, reranking, and careful prompt packing.
- Long-context ingestion can avoid retrieval for small static corpora, but token costs stay high and precision degrades compared with targeted retrieval on large corpora.

### Impact and Legacy
Retrieval pipelines turned RAG from a simple retrieval trick into a systems-design discipline. A well-designed pipeline can compensate for weaknesses in individual components: query transformation fixes poorly phrased questions, hybrid search covers lexical blind spots, reranking corrects retrieval errors, and context assembly ensures the model attends to the right evidence. This design space also sharpened the architectural distinction between RAG, fine-tuning, and long-context approaches, especially in production settings where freshness, scale, and source attribution matter.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why is query → top-k → generate usually not enough for production RAG?
2. What problem is HyDE trying to solve?
3. Why does passage ordering matter when assembling context for an LLM?

### Core Problems
1. Design a retrieval pipeline for a question-answering system over a frequently updated document corpus, and explain where you would use query transformation, reranking, citation tracking, and context packing.
2. Compare advanced RAG, fine-tuning, and long-context ingestion for a system that must answer with citations from a large, dynamic knowledge base.

### Challenge
1. Propose a production-grade multi-hop RAG pipeline for questions that require synthesizing evidence across documents, and explain how you would control token budget, retrieval fusion, passage ordering, and citation verification without sacrificing answer quality.

*See also:* [[Chunking Strategies]]; [[Embeddings and Vector Databases]]; [[Reranking]]; [[Supervised Fine-Tuning]]; [[Efficient Attention and Long-Context Variants]]

## Supporting Chunks
### Supporting Chunks
- No supporting chunk notes are attached yet.

## References
- [[LLM/Sources/Sources Index]]
