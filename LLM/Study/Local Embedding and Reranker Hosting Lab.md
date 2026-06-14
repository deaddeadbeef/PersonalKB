---
tags: [study, llm, rag, embeddings, reranking, local-llm, inference, serving]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [core, practice]
last-verified: 2026-06-15
---

# Local Embedding and Reranker Hosting Lab

> **One-line summary** Embedding and reranker endpoints are model inference services too: before trusting a local RAG assistant, prove the model, route, vector shape, normalization, batching, ranking gain, latency, and privacy boundary.

Use this after [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]], [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]], and [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] when the RAG stack needs a local embedding model, a local reranker, or both.

Use this before [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab|Local RAG Retrieval Evaluation and Reranking Lab]] and [[LLM/Study/Local RAG Minimal Python Harness|Local RAG Minimal Python Harness]]. The retrieval evaluation lab measures whether a retrieval choice works; this lab proves the inference service behind that choice is real, compatible, and measurable.

For the academic model, pair this with [[LLM/2023 — Open Models and Agents/Embeddings and Vector Databases|Embeddings and Vector Databases]], [[LLM/2023 — Open Models and Agents/Reranking|Reranking]], [[LLM/_chunks/chunk-llm-225 DPR Dual-Encoder Dense Retrieval|DPR dual-encoder retrieval]], and [[LLM/2020–2021 — The Scaling Era/Retrieval Pipelines and Context Assembly|Retrieval Pipelines and Context Assembly]]. The applied question is not only "which API returns a vector?" It is "which encoder/reranker gives the right evidence to the generator under this hardware and latency budget?"

## What This Lab Decides

It decides which local embedding and reranker provider to use for one corpus and workload.

| Decision | Evidence required |
| --- | --- |
| Embedding provider | Model id, runtime, route, vector dimension, normalization behavior, batch behavior, latency, and index metric. |
| Query/document encoding | Whether the model needs prefixes, instructions, asymmetric query/document methods, or the same raw text path for both sides. |
| Vector index compatibility | Dimension, distance metric, metadata schema, reindex trigger, and corpus version. |
| Reranker provider | Candidate format, score semantics, top_n behavior, latency delta, and ranking gain over first-stage retrieval. |
| Keep/skip reranking | Context precision gain versus latency, memory, and complexity. |
| Privacy boundary | Whether query text, document snippets, and scores stay on loopback and out of unwanted logs. |

Do not debug RAG quality with a hidden embedding service. Save the service card first.

## Academic Bridge

| Concept | Hosting consequence |
| --- | --- |
| Bi-encoder dense retrieval | Corpus chunks can be embedded offline and indexed; each query is embedded at runtime. The stored vector dimension and metric must match the model. |
| Contrastive embedding training | Model fit depends on domain, language, query style, and hard negatives, not just vector size. |
| Normalized vectors | If vectors are unit length, cosine similarity and dot product are easier to compare; still record the index metric explicitly. |
| Asymmetric search | Some models expect different query and document prompts or encode paths. Mixing them can look like "bad retrieval" while the service is technically healthy. |
| Cross-encoder reranking | Query and candidate text are scored together, so relevance can improve, but every candidate pair costs inference time. |
| Late interaction and decoder-only reranking | Not every reranker is a classic cross-encoder. Treat score semantics and launch flags as part of compatibility. |
| Matryoshka or truncated embeddings | Lower dimensions can reduce storage and search cost only when the model supports that representation. |

## Provider Choice Map

| Provider | Route shape | Best first use | First proof |
| --- | --- | --- | --- |
| Ollama | Native `/api/embed` | Fast laptop proof with model-managed local embeddings. | `ollama list`, model tag, vector length, L2 norm, batch input, same model for corpus/query. |
| LM Studio | OpenAI-compatible embeddings at a local `/v1` base URL | Desktop workflow and client compatibility checks. | Loaded embedding-capable model id, `http://localhost:1234/v1`, response dimension, GUI/server settings. |
| llama.cpp server | `/embedding`, `/v1/embeddings`, and rerank aliases when launched for those modes | GGUF, CPU/edge, low-level launch control. | GGUF file, `--embedding` or rerank launch flags, route, vector dimension, normalization setting, rerank response. |
| vLLM | OpenAI-compatible pooling/embedding server | GPU serving, batching, Matryoshka-capable models, server-style throughput. | `vllm serve ... --runner pooling` when needed, `/v1/embeddings`, dimensions/truncation behavior, latency. |
| SGLang | `/v1/embeddings` for embedding runner; reranker-specific launch modes | GPU serving with embedding models, cross-encoder rerankers, decoder-only rerankers. | `--is-embedding` for embedding and cross-encoder rerank models, no `--is-embedding` for decoder-only yes/no rerankers, score response. |
| Text Embeddings Inference | `/embed`, `/v1/embeddings`, `/rerank` | Production-style embedding/reranker service with Docker, batching, metrics, and tracing. | Container image, model id, mounted cache, route, vector dimension, batch/latency, metrics endpoint if used. |
| Sentence Transformers local Python | In-process `SentenceTransformer` and `CrossEncoder` | Offline baseline, small harness, explicit Python control. | Model path/name, `encode` path, vector shape, `CrossEncoder.predict` scores, dependency versions. |

Start with one provider. Add a second provider only when the query set shows the first one is wrong or the deployment constraints require a different runtime.

## Lab 0: Freeze The Workload

Fill this before serving anything.

| Field | Value |
| --- | --- |
| Workload |  |
| Corpus boundary |  |
| Query set path |  |
| Languages |  |
| Average chunk length |  |
| Exact-term pressure | low / medium / high |
| Multilingual pressure | low / medium / high |
| Privacy boundary | local loopback / LAN / remote / mixed |
| Latency target |  |
| Hardware path | CPU / CUDA / ROCm / Metal / WSL / other |
| Candidate top-k before rerank |  |
| Final context count |  |

Pass signal: the provider choice is tied to a workload instead of a generic leaderboard.

## Lab 1: Embedding Endpoint Smoke Test

The embedding smoke test proves shape, normalization, batching, and route compatibility before indexing a corpus.

| Check | Evidence |
| --- | --- |
| Model identity | Runtime model list or loaded model id. |
| Route | Native route and/or OpenAI-compatible route. |
| Single input | One response with vector length. |
| Batch input | Two or more inputs return the same number of vectors. |
| Vector dimension | `len(embedding)` saved in the service card. |
| Norm | `sqrt(sum(x*x for x in vector))`; record whether vectors are unit length. |
| Same model for query and docs | Explicitly recorded; otherwise retrieval scores are not comparable. |
| Truncation behavior | Long input handling, max length, or explicit truncate setting. |
| Latency | Cold call, warm call, and batch call. |

Ollama shape:

```powershell
curl http://localhost:11434/api/embed `
  -H "Content-Type: application/json" `
  -d '{"model":"embeddinggemma","input":["alpha test","beta test"]}'
```

OpenAI-compatible shape:

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="local")
response = client.embeddings.create(
    model="your-local-embedding-model",
    input=["alpha test", "beta test"],
)
vectors = [row.embedding for row in response.data]
print(len(vectors), len(vectors[0]))
```

Vector sanity helper:

```python
import math

def norm(v):
    return math.sqrt(sum(x * x for x in v))

print("dimension", len(vectors[0]))
print("norm", norm(vectors[0]))
```

Do not create the vector index until this row is complete.

## Lab 2: Service Card

Copy one service card per provider candidate.

| Field | Value |
| --- | --- |
| Provider | Ollama / LM Studio / llama.cpp / vLLM / SGLang / TEI / Sentence Transformers |
| Runtime version |  |
| Model id or local path |  |
| Model revision, tag, or digest |  |
| License/data boundary |  |
| Launch command or GUI settings |  |
| Host and port |  |
| Embedding route |  |
| Rerank route |  |
| OpenAI-compatible? | Yes / No / Partial |
| Vector dimension |  |
| Normalization | unknown / unit norm / not unit norm / configurable |
| Query/document prompt rule | same text / query prefix / document prefix / encode_query + encode_document / other |
| Batch behavior |  |
| Truncation behavior |  |
| Cold latency |  |
| Warm latency |  |
| Peak RAM/VRAM |  |
| Logs contain text? | yes / no / unknown |
| Decision | keep / compare / reject |

## Lab 3: Index Compatibility

Embedding service changes are schema changes. Treat them like migrations.

| Index field | Rule |
| --- | --- |
| Dimension | Must match every stored vector. A model change usually requires reindexing. |
| Distance metric | Match normalization behavior: cosine is the safe default for semantic search; dot product is safe only when intended. |
| Corpus version | Store corpus hash or manifest version next to the embedding config. |
| Model id | Store full provider model id, not only a friendly alias. |
| Query path | Record query prefix/instruction or encode method. |
| Document path | Record document prefix/instruction or encode method. |
| Chunk policy | Keep chunk size, overlap, and metadata fixed during provider comparison. |
| Reindex trigger | Any model, dimension, normalization, chunking, or instruction change. |

Minimum config row:

| Run id | Provider | Model | Dimension | Norm | Metric | Chunk policy | Corpus version | Reindex required? |
| --- | --- | --- | ---: | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |

## Lab 4: Embedding Provider A/B

Compare providers with retrieval-only evidence before generation.

| Query id | Expected source | Provider A first relevant rank | Provider B first relevant rank | Hit@5 delta | Latency delta | Decision |
| --- | --- | ---: | ---: | --- | --- | --- |
|  |  |  |  |  |  |  |

Control these variables:

- same corpus manifest
- same chunk records
- same query text
- same metadata filters
- same candidate top-k
- same distance metric if possible
- same lexical/hybrid path state

If provider B wins only because it used different chunks or filters, it did not win the embedding comparison.

## Lab 5: Reranker Endpoint Smoke Test

Use a reranker only after first-stage retrieval can place the expected evidence inside the candidate set.

| Check | Evidence |
| --- | --- |
| Candidate input format | List of texts or objects, with ids preserved outside the model call if needed. |
| Query text | Same query used for retrieval evaluation. |
| Score semantics | Larger-is-better, bounded 0-1, raw logits, or provider-specific score. |
| Top_n behavior | Whether the endpoint returns all scores or only the top rows. |
| Document return behavior | Whether text comes back or only indices/scores. |
| Latency | Candidate count versus total rerank time. |
| Ranking gain | First relevant rank and context precision before/after rerank. |

Rerank comparison row:

| Query id | Candidate top-k | First relevant before | First relevant after | Context precision before | Context precision after | Latency delta | Keep? |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  |  |  |  |  |  |  |

Reranking cannot recover evidence that never entered the candidate set. If expected evidence is absent before rerank, return to chunking, embedding, metadata, or hybrid retrieval.

## Lab 6: Operational Boundary

Local embedding and reranker services often process the most sensitive text in the system: private queries and private document chunks.

| Boundary | Check |
| --- | --- |
| Host binding | Keep loopback-only until LAN exposure is intentional. |
| Logs | Check whether queries, documents, scores, or full request bodies are logged. |
| Model cache | Record where weights are stored and whether private/gated models are present. |
| Corpus cache | Keep vector indexes and chunk files out of synced or public folders unless intentional. |
| Client keys | Local OpenAI-compatible clients may require a dummy API key; record whether it is ignored or enforced. |
| Batch jobs | Treat offline embedding of a private corpus as data processing, not a harmless benchmark. |
| Reranker payloads | Candidate snippets can leak more private text than the final answer. |

Use [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] before exposing the service beyond a trusted local process.

## Decision Card

| Field | Decision |
| --- | --- |
| Accepted embedding provider |  |
| Accepted reranker provider | none / provider |
| Rejected alternatives |  |
| Reason for accepted provider |  |
| Retrieval evaluation link |  |
| Benchmark row link |  |
| Quality row link |  |
| Security/privacy note |  |
| Reindex trigger |  |
| Next controlled change |  |

## Completion Gate

This lab is complete when all are true:

- [ ] Workload, corpus boundary, query set, latency target, and privacy boundary are written down.
- [ ] At least one embedding service card records provider, model, route, dimension, normalization, batching, truncation, and latency.
- [ ] The vector index config stores model id, dimension, metric, chunk policy, corpus version, and reindex trigger.
- [ ] Query and document encoding rules are explicit.
- [ ] Retrieval-only evaluation proves expected sources appear in the candidate set.
- [ ] Reranking is tested or explicitly skipped with a latency/quality reason.
- [ ] If reranking is kept, first relevant rank, context precision, and latency delta are recorded.
- [ ] Logs, host binding, cache paths, and private-corpus handling are checked.
- [ ] [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab|Local RAG Retrieval Evaluation and Reranking Lab]] receives the provider decision before generation is evaluated.
- [ ] [[LLM/Study/Local RAG Minimal Python Harness|Local RAG Minimal Python Harness]] records the final provider config in its artifact contract.

## References

Internal:

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local RAG Assistant Lab]]
- [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab]]
- [[LLM/Study/Local RAG Minimal Python Harness]]
- [[LLM/2023 — Open Models and Agents/Embeddings and Vector Databases]]
- [[LLM/2023 — Open Models and Agents/Reranking]]
- [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes]]
- [[LLM/2020–2021 — The Scaling Era/Retrieval Pipelines and Context Assembly]]
- [[LLM/_chunks/chunk-llm-225 DPR Dual-Encoder Dense Retrieval]]
- [[LLM/_chunks/chunk-llm-228 DPR as RAG Retrieval Backbone]]

Current external docs checked 2026-06-15:

- [Ollama embeddings](https://docs.ollama.com/capabilities/embeddings)
- [LM Studio embeddings](https://lmstudio.ai/docs/developer/openai-compat/embeddings)
- [llama.cpp server](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
- [vLLM embedding usages](https://docs.vllm.ai/en/latest/models/pooling_models/embed/)
- [SGLang embedding models](https://sgl-project.github.io/supported_models/retrieval_ranking/embedding_models.html)
- [SGLang rerank models](https://sgl-project.github.io/supported_models/retrieval_ranking/rerank_models.html)
- [Hugging Face Text Embeddings Inference](https://huggingface.co/docs/text-embeddings-inference/en/index)
- [TEI quick tour](https://huggingface.co/docs/text-embeddings-inference/en/quick_tour)
- [Sentence Transformers retrieve and rerank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html)
