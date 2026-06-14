---
tags: [study, llm, rag, retrieval, reranking, local-llm, evaluation]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [core, practice]
last-verified: 2026-06-15
---

# Local RAG Retrieval Evaluation and Reranking Lab

> **One-line summary** A local RAG system is diagnosable only when retrieval quality is measured before generation: expected sources, top-k hits, rank, scores, reranking impact, context selection, citations, and failure mode must be visible.

Use this between [[LLM/Study/Local RAG Assistant Lab|Local RAG Assistant Lab]] and [[LLM/Study/Local RAG Minimal Python Harness|Local RAG Minimal Python Harness]]. The assistant lab explains the end-to-end pipeline; the minimal harness stores artifacts. This lab decides whether the retrieval layer is good enough before a local generator sees the context.

Use [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] after this lab to judge final answers. Use [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]] when retrieved passages must be packed into a limited context window. Use [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] before indexing private corpora.

## What This Lab Decides

It answers six retrieval questions:

1. Does the supporting source appear in the candidate set before generation?
2. Is the supporting chunk ranked high enough to be selected for context?
3. Are irrelevant or contradictory chunks crowding out useful evidence?
4. Does reranking improve the selected evidence enough to justify latency?
5. Do exact terms, filenames, code symbols, or entity names require sparse or hybrid search?
6. Can every generated citation point back to a retrieved chunk with stable metadata?

Do not label a failed RAG answer as "bad model" until these questions have evidence.

## Measurement Vocabulary

| Metric | Meaning | Use it when |
| --- | --- | --- |
| Hit@k | Whether at least one expected source appears in the top-k. | Quick supported-question smoke tests. |
| Recall@k | Fraction of expected sources retrieved in top-k. | Multi-source or multi-hop questions. |
| Precision@k | Fraction of top-k results that are relevant. | Detecting context poisoning and noisy retrieval. |
| MRR | Reciprocal rank of the first relevant result. | Measuring whether useful evidence appears early. |
| Context precision | Fraction of selected context chunks that are useful. | After reranking, filtering, and packing. |
| Citation validity | Whether each citation supports the cited claim. | Final RAG answer acceptance. |
| Retrieval latency | Time spent embedding, searching, filtering, and reranking. | Deciding whether an improvement is usable locally. |

For small local corpora, start with Hit@k, MRR, context precision, and citation validity. Add full recall/precision only when there are enough labeled queries to make the numbers meaningful.

## Query Set Design

Create 10-30 retrieval queries before tuning.

| Query type | Tests | Expected evidence |
| --- | --- | --- |
| Direct fact | Can the obvious source be found? | One source id and one chunk id. |
| Paraphrase | Does dense retrieval bridge wording differences? | Source id even when query uses different phrasing. |
| Exact identifier | Do filenames, commands, symbols, IDs, or names survive? | Exact-match or sparse path should help. |
| Multi-hop | Can all required sources enter candidates? | Two or more expected source ids. |
| Boundary case | Does chunking split the answer away from context? | Parent section or adjacent chunk evidence. |
| Unsupported | Does retrieval correctly show no sufficient evidence? | Empty expected source; refusal later. |
| Conflicting | Can the system surface the current/authoritative source? | Expected source plus stale distractor. |

Do not tune only against easy direct facts. The point of retrieval evaluation is to expose where semantic search, chunking, metadata, or reranking fails.

## Lab 0: Freeze The Retrieval Run

Fill this before changing retriever settings.

| Field | Value |
| --- | --- |
| Run id |  |
| Corpus version |  |
| Corpus manifest path |  |
| Chunk policy | size / overlap / boundary / metadata |
| Chunk count |  |
| Embedding model |  |
| Vector dimension |  |
| Index/vector store | Chroma / Qdrant / FAISS / flat cosine / other |
| Sparse or lexical path | none / BM25 / full-text filter / Qdrant sparse / other |
| Reranker | none / cross-encoder / late interaction / hosted / other |
| Candidate top-k |  |
| Rerank candidate count |  |
| Final context count |  |
| Metadata filters |  |
| Query set |  |
| Latency target |  |

If any row changes, it is a new retrieval run.

## Lab 1: Dense Retrieval Baseline

Run retrieval without generation and save the results.

Minimum result row:

| Query id | Query | Expected source ids | Retrieved ids | Distances/scores | Hit@5 | First relevant rank | Failure mode |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Yes/No |  |  |

Ollama plus Chroma shape:

```python
query = "What are the main RAG failure modes?"
query_vector = embed([query])[0]
results = collection.query(
    query_embeddings=[query_vector],
    n_results=10,
    include=["documents", "metadatas", "distances"],
)
```

Record:

- embedding model and vector dimension
- query embedding path
- retrieved chunk ids
- source ids and citation labels
- distances or scores
- whether the expected source appears
- whether the retrieved text actually contains the answer

Pass signal: every supported query retrieves the expected source within the candidate set used for later reranking or context packing.

## Lab 2: Top-K Sweep

Sweep `k` before adding a reranker.

| Query id | Hit@3 | Hit@5 | Hit@10 | Hit@20 | First relevant rank | Decision |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

Interpretation:

| Pattern | Meaning | Next action |
| --- | --- | --- |
| Hit@20 yes, Hit@5 no | Retriever can find the source but ranks it too low. | Add reranking or improve query/chunk metadata. |
| Hit@20 no | True retrieval miss or missing corpus/chunk. | Inspect corpus, chunking, embedding model, lexical path. |
| Hit@5 yes but context answer fails | Generation or context assembly issue. | Move to quality harness and context-budget lab. |
| Many irrelevant chunks in top-k | Context poisoning risk. | Add metadata filters, reranking, dedupe, or lower final context count. |

Retrieve wide, pack narrow. Candidate top-k is allowed to be larger than final context count.

## Lab 3: Metadata And Lexical Checks

Dense retrieval often misses exact terms. Add a lexical or metadata check when queries depend on:

- filenames
- code symbols
- CLI commands
- proper names
- dates or version strings
- exact note titles
- short acronyms

Chroma supports metadata filters and document text filters through `where` and `where_document`. Use these to test whether exact matching changes retrieval before introducing a full hybrid store.

| Query id | Dense result | Lexical/filter result | Combined decision |
| --- | --- | --- | --- |
|  |  |  | dense only / lexical only / combine / fix chunks |

If lexical matching finds the source and dense retrieval does not, the problem may be embedding model fit, chunk text, query phrasing, or the need for hybrid search.

## Lab 4: Reranking

Use reranking when the right evidence appears in a wider candidate set but the top context remains noisy or poorly ordered.

Two-stage pattern:

1. Retrieve 20-100 candidates cheaply with dense, sparse, or hybrid search.
2. Score query-candidate pairs with a reranker.
3. Select the top 3-10 chunks for context.
4. Measure context precision, citation support, and latency.

Sentence Transformers pattern:

```python
from sentence_transformers import CrossEncoder

reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")
pairs = [(query, candidate["text"]) for candidate in candidates]
scores = reranker.predict(pairs)
```

Reranking row:

| Query id | Candidate top-k | First relevant before | First relevant after | Context precision before | Context precision after | Latency delta | Keep reranker? |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
|  |  |  |  |  |  |  | Yes/No |

Reranking cannot recover evidence that never entered the candidate set. If the expected source is absent from candidates, fix retrieval or chunking first.

## Lab 5: Hybrid Retrieval

Use hybrid retrieval when dense semantic search and lexical exact search solve different parts of the query set.

| Search path | Best at | Weak at |
| --- | --- | --- |
| Dense vectors | Paraphrases, semantic relatedness, conceptual search. | Exact strings, rare symbols, version numbers. |
| Sparse/BM25 | Exact terms, identifiers, names, commands. | Paraphrases and conceptual matches. |
| Hybrid fusion | Combining semantic and exact-match evidence. | Added complexity, duplicate handling, score calibration. |
| Reranking after hybrid | Precision over a broader candidate pool. | Latency and operational cost. |

Reciprocal rank fusion is a practical first fusion rule because it combines rank positions from multiple result lists without needing calibrated dense and sparse scores.

Hybrid decision row:

| Query class | Dense hit? | Sparse hit? | Hybrid improves? | Keep hybrid? | Reason |
| --- | --- | --- | --- | --- | --- |
| exact identifier |  |  |  |  |  |
| paraphrase |  |  |  |  |  |
| multi-hop |  |  |  |  |  |

Keep hybrid only if it improves the labeled query set enough to justify added index, query, and debugging complexity.

## Lab 6: Context Selection And Citation Audit

After retrieval and reranking, select the final context.

| Selection field | Record |
| --- | --- |
| Candidate count |  |
| Final chunk count |  |
| Final source ids |  |
| Deduped chunks removed |  |
| Conflicting/stale chunks removed |  |
| Token count |  |
| Context order | highest score first / source order / sandwich / other |
| Citation labels |  |

Citation audit:

| Claim id | Claim | Citation | Supporting chunk id | Supported? | Notes |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Yes/No |  |

If a citation points to a retrieved chunk that does not support the claim, the final answer fails even if retrieval metrics look strong.

## Failure Triage

| Symptom | Failed layer | First controlled change |
| --- | --- | --- |
| Expected source absent from corpus manifest | Corpus boundary | Add or fix source, then rebuild chunks and index. |
| Expected source present but no chunk contains answer | Chunking | Adjust heading/paragraph boundary, parent context, overlap, or metadata. |
| Relevant chunk exists but dense top-k misses it | Embedding/query fit | Try query rewrite, domain embedding, hybrid sparse path, or larger top-k. |
| Relevant chunk appears only at low rank | Ranking | Add reranker, metadata filter, or query expansion. |
| Relevant chunk selected but answer ignores it | Context/generation | Reorder context, reduce noise, lower temperature, or improve prompt. |
| Citations are weak or fake | Citation boundary | Pre-assign citation labels and validate claim-by-claim. |
| Unsupported query gets an answer | Source-boundary failure | Strengthen refusal rule and require retrieval sufficiency check. |
| Retrieval improves but latency fails | Operations | Lower candidate count, cache embeddings, skip reranker for easy queries, or batch offline. |

## Completion Gate

This lab is complete when all are true:

- [ ] Query set has supported, unsupported, paraphrase, exact-identifier, and at least one hard query.
- [ ] Corpus manifest and chunk records identify expected sources and citation labels.
- [ ] Dense retrieval baseline records top-k, scores/distances, Hit@k, and first relevant rank.
- [ ] Top-k sweep distinguishes true retrieval misses from low-rank candidates.
- [ ] Metadata or lexical checks are run for exact-term queries.
- [ ] Reranking is tested when relevant evidence appears low in candidates.
- [ ] Hybrid search is either tested or explicitly rejected with a reason.
- [ ] Context selection records final chunks and token budget.
- [ ] Citation audit checks claims against supporting chunks.
- [ ] Failure rows name the failed layer before changing the generator model.
- [ ] [[LLM/Study/Local RAG Minimal Python Harness|Local RAG Minimal Python Harness]] receives the final artifact paths if this is part of the capstone.

## References

Internal:

- [[LLM/Study/Local RAG Assistant Lab]]
- [[LLM/Study/Local RAG Minimal Python Harness]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/2023 — Open Models and Agents/Embeddings and Vector Databases]]
- [[LLM/2023 — Open Models and Agents/Reranking]]
- [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes]]
- [[LLM/2020–2021 — The Scaling Era/Retrieval Pipelines and Context Assembly]]
- [[LLM/_chunks/chunk-llm-225 DPR Dual-Encoder Dense Retrieval]]
- [[LLM/_chunks/chunk-llm-226 DPR In-Batch and Hard Negative Training]]
- [[LLM/_chunks/chunk-llm-227 DPR vs BM25 Retrieval Accuracy]]
- [[LLM/_chunks/chunk-llm-228 DPR as RAG Retrieval Backbone]]

Current external docs checked 2026-06-15:

- [Ollama embeddings](https://docs.ollama.com/capabilities/embeddings)
- [Chroma query and get](https://docs.trychroma.com/docs/querying-collections/query-and-get)
- [Sentence Transformers retrieve and rerank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html)
- [Qdrant hybrid queries](https://qdrant.tech/documentation/search/hybrid-queries/)
