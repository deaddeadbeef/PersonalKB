---
tags: [study, llm, rag, local-llm, implementation, harness]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [core, practice]
last-verified: 2026-06-15
---

# Local RAG Minimal Python Harness

> **One-line summary** A local RAG harness is credible only when corpus version, chunking, embeddings, index metadata, retrieval evidence, generated answer, citations, and failure rows are all reproducible.

Use this with [[LLM/Study/Local RAG Assistant Lab|Local RAG Assistant Lab]]. That lab explains the pipeline and failure modes. This note turns it into a minimal implementation contract you can run against a small local corpus.

Use [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab|Local RAG Retrieval Evaluation and Reranking Lab]] when the harness needs a retrieval-only evaluation pass before generation: supported query set, top-k sweep, first relevant rank, reranking row, hybrid decision, context selection, and citation audit.

Use this after [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]], [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]], and [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]]. The endpoint, route, model id, context budget, and sampler settings should be known before retrieval is blamed for model failures.

Use [[LLM/Study/Local Embedding and Reranker Hosting Lab|Local Embedding and Reranker Hosting Lab]] before freezing `rag_config.json` when the embedding provider, vector dimension, normalization, query/document encoding rule, reranker endpoint, or reranker score semantics are not already proven.

Before indexing private notes or project files, use [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] to define the corpus boundary, citation redaction policy, log retention, and prompt-injection tests.

## Outcome

After this lab you should have:

- a fixed corpus manifest
- deterministic chunk records with metadata
- one embedding/index configuration
- one retrieval evidence file per query
- one generated answer with citations
- one unsupported-question refusal
- one diagnosed RAG failure row
- one benchmark and quality-harness row

The point is not to build a fancy application first. The point is to prove the retrieval loop in a form that survives reruns.

## Minimal Artifact Contract

Create a small experiment folder outside the vault or in an ignored workspace:

```text
rag_experiments/
  corpus/
  corpus_manifest.jsonl
  chunks.jsonl
  rag_config.json
  index/
  queries.jsonl
  runs/
    2026-06-15-q001-retrieval.json
    2026-06-15-q001-answer.md
    2026-06-15-q001-eval.json
```

| Artifact | Required fields |
|---|---|
| `corpus_manifest.jsonl` | `source_id`, `title`, `path_or_url`, `allowed_for_rag`, `updated_at`, `sha256` |
| `chunks.jsonl` | `chunk_id`, `source_id`, `section`, `ordinal`, `text`, `token_estimate`, `chunk_policy` |
| `rag_config.json` | embedding model, index type/path, generator model, runtime base URL, top-k, rerank policy, context budget, citation style |
| embedding/reranker service card | provider, model id, route, vector dimension, normalization, query/document rule, reranker score semantics, latency, privacy boundary |
| retrieval run | query id, query text, retrieved chunk ids, scores/distances, selected context ids, missing expected source flag |
| retrieval evaluation | expected source ids, Hit@k, first relevant rank, reranking impact, hybrid decision, final context ids, citation audit |
| answer file | assembled prompt summary, final answer, citation ids, refusal if unsupported |
| eval row | retrieval recall, context precision, citation validity, faithfulness, latency, decision, failure mode |

If any artifact is missing, you cannot tell whether the problem is corpus ingestion, chunking, embeddings, retrieval, context assembly, generation, or evaluation.

## Stack Choices

Start with one stack. Add alternatives only after the first run is reproducible.

| Stack | Good first use | What to record |
|---|---|---|
| Ollama embeddings plus Chroma | Fully local laptop experiment with a persistent vector store. | Ollama embedding model, Chroma path, collection name, vector dimension, top-k. |
| Sentence Transformers plus Chroma | Offline Python embedding path with explicit local model control. | model path/name, `encode_query`/`encode_document` decision, Chroma path, dimensionality. |
| Flat in-memory cosine search | Tiny corpus, debugging chunking and citation logic. | normalized vectors, similarity function, corpus size, no-persistence decision. |
| Hybrid sparse plus dense | Filenames, code symbols, rare terms, or exact note titles matter. | lexical query, dense query, fusion/rerank policy, duplicate handling. |

Current implementation facts checked 2026-06-15:

- Ollama's embedding API supports `/api/embed`, batch input, and L2-normalized vectors; its docs also recommend cosine similarity and using the same embedding model for indexing and querying.
- Chroma collections store embeddings, documents, and metadata; its query API runs nearest-neighbor similarity search and supports text queries or explicit query embeddings.
- Chroma's `PersistentClient` stores local database files on disk and reloads them on start.
- Sentence Transformers frames semantic search as embedding corpus entries and queries in the same vector space; for question-to-paragraph search, choose models and encode paths suitable for asymmetric search.
- Ollama's OpenAI-compatible route can be called through an OpenAI client at `http://localhost:11434/v1/`, with an API key value required by the client but ignored by Ollama.

## Lab 0: Runtime Smoke Checks

Record these before indexing:

| Check | Evidence |
|---|---|
| Ollama running | `curl http://localhost:11434/api/tags` or equivalent model list |
| Embedding model available | model name and `ollama pull` or local model list evidence |
| Generator endpoint available | one small non-RAG chat response from the serving runbook |
| Chroma storage path chosen | absolute or project-relative path, plus whether it is disposable |
| Python environment frozen | `python --version`, dependency versions, and whether network is needed |

Starter dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install chromadb requests openai
```

Use a separate environment per experiment if you are testing multiple vector stores or embedding libraries.

## Lab 1: Corpus Manifest

Start with 5-20 documents you can inspect manually. For a vault experiment, do not index the whole vault first. Pick one folder or a small list of LLM notes.

| Field | Example |
|---|---|
| `source_id` | `llm-rag-001` |
| `title` | `RAG Evaluation and Failure Modes` |
| `path_or_url` | `LLM/2023 - Open Models and Agents/RAG Evaluation and Failure Modes.md` |
| `allowed_for_rag` | `true` |
| `updated_at` | file modified date or explicit corpus version date |
| `sha256` | digest of the raw source text |

Pass signal: every answer citation can be traced back to a source id and immutable text digest.

## Lab 2: Chunk Records

Chunk Markdown by heading first, then paragraph, then token budget. Keep source metadata attached to every chunk.

Starter policy:

| Setting | Value |
|---|---|
| chunk target | 300-800 tokens |
| overlap | 10-20 percent only when boundary loss appears |
| boundary order | heading -> paragraph -> sentence -> token fallback |
| chunk id | `{source_id}#s{section_ordinal}-c{chunk_ordinal}` |
| citation label | `[source_id:section:chunk]` or Obsidian link plus section |

Reject chunks that have no source id, no section, no text, or no citation label. Debugging RAG without stable chunk ids is wasted effort.

## Lab 3: Embed And Index

Use the same embedding model for corpus chunks and queries. If the endpoint returns normalized vectors, cosine similarity and inner product become easier to reason about, but still record the actual index metric.

Minimal Chroma plus Ollama embedding pattern:

```python
import json
import pathlib
import requests
import chromadb

ROOT = pathlib.Path("rag_experiments")
EMBED_MODEL = "embeddinggemma"
OLLAMA = "http://localhost:11434"

def embed(texts):
    response = requests.post(
        f"{OLLAMA}/api/embed",
        json={"model": EMBED_MODEL, "input": texts},
        timeout=120,
    )
    response.raise_for_status()
    return response.json()["embeddings"]

chunks = [json.loads(line) for line in (ROOT / "chunks.jsonl").read_text(encoding="utf-8").splitlines()]
ids = [row["chunk_id"] for row in chunks]
docs = [row["text"] for row in chunks]
metas = [
    {
        "source_id": row["source_id"],
        "section": row["section"],
        "ordinal": row["ordinal"],
        "citation": row["citation"],
    }
    for row in chunks
]

client = chromadb.PersistentClient(path=str(ROOT / "index" / "chroma"))
collection = client.get_or_create_collection(name="local_rag_minimal")
collection.upsert(ids=ids, documents=docs, metadatas=metas, embeddings=embed(docs))
```

Record:

- embedding model
- vector dimension
- corpus chunk count
- Chroma collection name
- persistent index path
- whether embeddings were produced locally or by a networked service

## Lab 4: Retrieval Evidence

Run retrieval without generation first.

```python
query = "What are the main RAG failure modes?"
query_vector = embed([query])[0]
results = collection.query(
    query_embeddings=[query_vector],
    n_results=5,
)
```

For each query, save:

| Field | Why it matters |
|---|---|
| query id and text | Reproducible evaluation unit |
| expected source ids | Tests retrieval recall |
| retrieved chunk ids | Shows what the generator was allowed to see |
| distances or scores | Explains rank order and weak matches |
| selected context ids | Distinguishes retrieval from context packing |
| not-found flag | Separates retrieval miss from generation hallucination |

Pass signal: for known-answer questions, the supporting chunk appears in top-k before you call the generator.

## Lab 5: Context Assembly

Turn retrieval output into a small, auditable context block.

```text
You answer only from the provided context.
Use citations like [1] for every factual claim.
If the context does not support the answer, say: not enough evidence.

Context:
[1] source_id=llm-rag-001 section="Failure Modes"
...chunk text...

[2] source_id=llm-rag-002 section="Evaluation"
...chunk text...

Question:
What are the main RAG failure modes?
```

Record a context-budget row before generation:

| Budget field | Value |
|---|---|
| runtime context limit |  |
| system prompt tokens |  |
| query tokens |  |
| retrieved context tokens |  |
| output reserve |  |
| safety margin |  |
| fits? | yes/no |

RAG failures often start here: too many irrelevant chunks, duplicated context, weak citation labels, or a prompt that lets parametric memory override missing evidence.

## Lab 6: Generate With Local Endpoint

Use the generator endpoint already proven by the serving and API-contract labs.

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1/", api_key="ollama")

response = client.chat.completions.create(
    model="your-local-generator",
    temperature=0,
    max_tokens=512,
    messages=[
        {"role": "system", "content": "Answer only from the provided context with citations."},
        {"role": "user", "content": assembled_prompt},
    ],
)

answer = response.choices[0].message.content
```

Save the final answer and the retrieved context used to produce it. A cited answer without the exact context is not enough evidence.

## Lab 7: Unsupported Question Test

Ask one question whose answer is not in the corpus.

| Expected behavior | Failure signal |
|---|---|
| Says `not enough evidence` or equivalent configured refusal | Answers from parametric memory |
| Cites no unsupported chunk | Invents citation or cites weakly related text |
| Logs retrieval was insufficient | Treats irrelevant top-k as enough context |

This is the simplest way to test whether the assistant obeys the source boundary.

## Lab 8: Failure Row

Add at least one diagnosed failure.

| Failure class | Evidence | First controlled change |
|---|---|---|
| Retrieval miss | Expected source absent from top-k | improve chunking, metadata, query, hybrid search, or top-k |
| Bad chunking | Right source retrieved but relevant sentence split away | adjust heading/paragraph/token boundary |
| Context poisoning | Irrelevant or contradictory chunks crowd the prompt | dedupe, rerank, filter metadata, lower top-k |
| Generation hallucination | Correct evidence present but unsupported claim appears | tighten prompt, lower temperature, add citation checker, try stronger model |
| Citation failure | Answer is right but citation points to weak chunk | assign citations before generation and validate post-answer |
| Latency/memory failure | Query works but exceeds benchmark target | reduce context, choose smaller model, change runtime, cache retrieval |

Do not label a run "bad model" until retrieval and context evidence are visible.

## Quality And Benchmark Rows

Add a RAG row to [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]]:

| Run id | Query id | Expected source | Top-k contains source? | Answer supported? | Citations valid? | Refusal works? | Decision |
|---|---|---|---|---|---|---|---|
|  |  |  | Yes/No | Yes/No | Yes/No | Yes/No | Pass/Hold/Fail |

Add a performance row to [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]]:

| Run id | Corpus version | Chunks | Embed model | Index | Top-k | Retrieved tokens | Generator | TTFT | Total latency | Peak RAM/VRAM | Decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |

Score retrieval and generation separately. A fluent answer fails if retrieval missed the source, and a perfect top-k still fails if the generator invents unsupported claims.

## Completion Gate

This harness is complete when you have:

- [ ] a corpus manifest with source ids and digests
- [ ] chunk records with section metadata and citation labels
- [ ] a recorded embedding/index configuration
- [ ] a persistent or explicitly disposable index
- [ ] retrieval evidence for at least one supported query
- [ ] retrieval evidence for at least one unsupported query
- [ ] retrieval evaluation row for top-k, rank, reranking/hybrid decision, and citation audit when applicable
- [ ] one generated cited answer with saved context
- [ ] one refusal for missing evidence
- [ ] one diagnosed failure row
- [ ] one RAG quality row
- [ ] one benchmark row with retrieval and generation latency separated
- [ ] one security/privacy note covering corpus boundary, logs, and citation metadata

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local RAG Assistant Lab]]
- [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab]]
- [[LLM/Study/Local Embedding and Reranker Hosting Lab]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/2020–2021 — The Scaling Era/Retrieval Pipelines and Context Assembly]]
- [[LLM/2023 — Open Models and Agents/Chunking Strategies]]
- [[LLM/2023 — Open Models and Agents/Embeddings and Vector Databases]]
- [[LLM/2023 — Open Models and Agents/Reranking]]
- [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes]]

Current external docs checked 2026-06-15:

- [Ollama embeddings](https://docs.ollama.com/capabilities/embeddings)
- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
- [Chroma getting started](https://docs.trychroma.com/docs/overview/getting-started)
- [Chroma clients and persistence](https://docs.trychroma.com/docs/run-chroma/clients)
- [Chroma query and get](https://docs.trychroma.com/docs/querying-collections/query-and-get)
- [Sentence Transformers semantic search](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html)
