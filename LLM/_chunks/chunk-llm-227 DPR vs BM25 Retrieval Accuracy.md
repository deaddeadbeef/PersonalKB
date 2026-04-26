---
tags: [chunk, llm]
id: "chunk-llm-227"
source: "[[LLM/_raw/raw-llm-057 Dense Passage Retrieval DPR]]"
source_loc: "Chunk Candidates, Why It Matters"
topic: "DPR vs BM25 retrieval accuracy"
claim: "DPR outperformed BM25 by 9-19 percentage points on top-20 retrieval accuracy across Natural Questions, TriviaQA, and WebQuestions."
confidence: "verified"
supports: ["[[LLM/2020–2021 — The Scaling Era/Retrieval Pipelines and Context Assembly]]"]
qna_seeds:
  - q: "By how much does DPR outperform BM25?"
    a: "On Natural Questions, DPR achieves 78.4% top-20 retrieval accuracy versus BM25's 59.1% — a 19.3 point improvement. Similar gains are seen on TriviaQA and WebQuestions, demonstrating dense retrieval's superiority for knowledge-intensive tasks."
  - q: "Are there cases where BM25 still beats DPR?"
    a: "Yes — on entity-centric tasks and when the query contains rare or highly specific terms, BM25's exact lexical matching can outperform DPR. Hybrid approaches combining both often achieve the best results."
up: "[[LLM/LLM]]"
---
# DPR Outperforms BM25 by Large Margins on QA Retrieval

On standard open-domain QA benchmarks, DPR demonstrated substantial improvements over BM25 sparse retrieval. On Natural Questions, DPR achieved 78.4% top-20 retrieval accuracy compared to BM25's 59.1% — a 19.3 percentage point improvement. Similar gains of 9–15 points were observed on TriviaQA and WebQuestions, establishing that learned dense representations capture semantic relevance that keyword matching cannot.

However, BM25 retains advantages on queries with rare terms or highly specific entities where exact lexical matching is critical. This observation motivated hybrid retrieval approaches that combine dense and sparse signals, which often outperform either method alone. DPR's results established dense retrieval as the default for knowledge-intensive tasks and provided the retrieval backbone that made RAG pipelines viable at scale.
