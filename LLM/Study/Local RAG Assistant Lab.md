---
tags: [study, llm, rag, local-llm, lab]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [practice]
---

# Local RAG Assistant Lab

> **One-line summary** A local RAG assistant proves that you can connect retrieval theory to a running local model: ingest documents, chunk them, embed and index them, retrieve evidence, assemble context, generate with citations, and diagnose failures.

Use this after [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]] and [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]]. The local model endpoint should already work before you add retrieval. Use [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] to decide whether the assistant is good enough for the workload.

When you are ready to implement rather than only design the pipeline, use [[LLM/Study/Local RAG Minimal Python Harness|Local RAG Minimal Python Harness]]. It defines the concrete artifacts for a small reproducible build: corpus manifest, chunks, embedding/index config, retrieval evidence, cited answer, refusal test, failure row, and benchmark/quality rows.

Before indexing private documents, use [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] to define the corpus boundary, log policy, access boundary, and prompt-injection tests.

Before packing retrieved passages into a prompt, use [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]] to reserve output tokens, count template/history/tool overhead, and set a maximum retrieved-context budget.

## Outcome

After this lab you should be able to:

- build a small document-grounded assistant over a local corpus
- explain each stage of the RAG pipeline: ingest -> chunk -> embed -> index -> retrieve -> rerank -> assemble -> generate -> verify
- cite retrieved passages in the answer instead of relying on parametric memory
- separate retrieval failures from generation failures
- log latency, memory, retrieval quality, and answer quality for a local model

This is the applied Level 4 proof in [[LLM/Study/LLM Mastery Roadmap|LLM Mastery Roadmap]] and a bridge into the capstone RAG assistant.

## Architecture

| Layer | Role | Study anchor |
| --- | --- | --- |
| Corpus | The documents the assistant is allowed to use | [[LLM/2020–2021 — The Scaling Era/Retrieval Pipelines and Context Assembly|Retrieval Pipelines and Context Assembly]] |
| Chunker | Splits documents into retrieval units | [[LLM/2023 — Open Models and Agents/Chunking Strategies|Chunking Strategies]] |
| Embedding model | Maps chunks and queries into vector space | [[LLM/2023 — Open Models and Agents/Embeddings and Vector Databases|Embeddings and Vector Databases]] |
| Index | Stores searchable vectors plus metadata | [[LLM/_chunks/chunk-llm-225 DPR Dual-Encoder Dense Retrieval|DPR dual-encoder retrieval]] |
| Retriever | Returns candidate chunks for a query | [[LLM/_chunks/chunk-llm-228 DPR as RAG Retrieval Backbone|DPR as RAG backbone]] |
| Reranker | Reorders candidates by query-specific relevance | [[LLM/2023 — Open Models and Agents/Reranking|Reranking]] |
| Context assembler | Packs evidence into the model prompt | [[LLM/2020–2021 — The Scaling Era/Retrieval Pipelines and Context Assembly|Context Assembly]] |
| Local generator | Calls the local LLM endpoint | [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]] |
| Evaluator | Checks support, citations, and failure mode | [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes|RAG Evaluation and Failure Modes]] |

## Build Sequence

### Phase 0: Pick The Workload

Define the assistant narrowly before writing code.

| Field | Example |
| --- | --- |
| Workload | "Answer questions over my project docs with citations." |
| Corpus boundary | Folder, file list, database export, or notes subset |
| Allowed answer source | Retrieved passages only, or retrieved passages plus model background knowledge |
| Citation style | `[doc:section]`, `[1]`, file path, URL, or note link |
| Refusal rule | Say "not enough evidence" when retrieved context does not support the answer |
| Privacy boundary | Who may query the corpus and what metadata may appear in answers/logs |
| Latency target | Interactive, batch, or offline |
| Evaluation set | 10-30 private questions with known supporting passages |

Do not start with "answer anything." A small assistant with clear source boundaries is easier to evaluate than a broad assistant with vague authority.

Implementation handoff: after this workload row is filled, create the artifact set in [[LLM/Study/Local RAG Minimal Python Harness|Local RAG Minimal Python Harness]] so the build has stable evidence files instead of ad hoc notebook output.

### Phase 1: Prepare The Corpus

Create a clean input folder for the first build. Use a small corpus you can inspect manually before scaling.

Minimum metadata per document:

| Metadata | Why it matters |
| --- | --- |
| `source_id` | Stable citation target |
| `title` | Human-readable citation label |
| `path` or `url` | Provenance and debugging |
| `section` | Better citation and filtering |
| `updated_at` | Helps detect stale answers |
| `chunk_id` | Maps generated citations back to evidence |

Keep raw documents immutable during a run. If the corpus changes, rebuild or version the index so benchmark results remain reproducible.

### Phase 2: Chunk Documents

Start with recursive chunking for Markdown, HTML, and structured notes. Use fixed-size chunking only when the source lacks reliable structure.

| Decision | Starter setting | Watch for |
| --- | --- | --- |
| Chunk size | 300-800 tokens | Too small loses context; too large dilutes relevance |
| Overlap | 10-20 percent | Too little drops boundary facts; too much creates duplicate retrieval noise |
| Boundary | Heading, paragraph, sentence, then token | Mid-sentence chunks produce weak citations |
| Metadata | title, path, section, ordinal | Missing metadata makes citations unverifiable |
| Parent context | optional larger parent chunk | Useful when precise chunks lack enough surrounding context |

Chunking is a quality lever, not just preprocessing. If the answer exists in the corpus but never appears in the retrieved chunks, the assistant has a chunking or retrieval problem before it has a model problem.

### Phase 3: Embed And Index

Use one embedding model for both corpus chunks and incoming queries. Store the model name, dimensionality if known, index type, chunk settings, and corpus version.

Core pattern:

1. Normalize each chunk's text and metadata.
2. Embed each chunk.
3. Store vector plus metadata in the index.
4. Embed the user query at runtime.
5. Retrieve top-k candidates by vector similarity.

This follows the dual-encoder pattern in [[LLM/_chunks/chunk-llm-225 DPR Dual-Encoder Dense Retrieval|DPR]]: chunks are pre-encoded offline, while queries are encoded at runtime. Dense retrieval is strong for semantic matching, but exact lexical search can still win on rare names, identifiers, filenames, and code symbols. For those cases, consider a hybrid dense-plus-sparse path.

For a minimal local implementation, [[LLM/Study/Local RAG Minimal Python Harness|Local RAG Minimal Python Harness]] gives a Chroma/Ollama-style pattern where chunk ids, metadata, embeddings, persistent index path, and query embeddings are recorded explicitly.

### Phase 4: Retrieve, Rerank, And Assemble

Start simple, then add complexity only when evaluation identifies a failure.

| Step | Starter policy | Upgrade when |
| --- | --- | --- |
| Retrieve | top 5-10 chunks | Relevant passages are missing |
| Rerank | optional cross-encoder or stronger scorer | Top-k contains right evidence but in poor order |
| Deduplicate | remove near-identical chunks | Repeated chunks crowd out other evidence |
| Pack context | strongest passages first, key passage near the end if needed | Long prompts cause "Lost in the Middle" failures |
| Cite | assign stable IDs before generation | Answers need auditability |

The assembled prompt should tell the model:

```text
Answer only from the provided context.
Use citations like [1] for every factual claim.
If the context does not support the answer, say: not enough evidence.
```

Keep the prompt short enough to fit the context target from [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]] and the measured budget from [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]]. Retrieved context consumes prompt tokens, increases prefill time, and grows KV-cache pressure.

### Phase 5: Generate With The Local Endpoint

Call the local model endpoint already proven by [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]]. For repeatable comparison, keep these fixed across runs:

- model id
- runtime and API base URL
- system prompt
- retrieval top-k
- chunking policy
- context assembly policy
- temperature and max output tokens

For citation-heavy RAG, start with low temperature. The goal is faithful synthesis, not creative variation.

### Phase 6: Verify The Answer

Use the RAG section of [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]].

| Check | Pass signal |
| --- | --- |
| Retrieval recall | Known supporting passage appears in retrieved top-k |
| Context precision | Most retrieved chunks are relevant |
| Citation correctness | Every citation points to a supporting chunk |
| Faithfulness | No substantive claim contradicts or exceeds context |
| Refusal behavior | The assistant says "not enough evidence" for unsupported questions |
| Latency/memory | Query stays within the local benchmark target |

Write down the failure mode, not just the bad answer. A retrieval miss calls for different work than a hallucination despite correct context.

## Failure Triage

| Symptom | Likely layer | First fix |
| --- | --- | --- |
| Right document never retrieved | Chunking, embedding, or query phrasing | Add metadata, adjust chunking, try hybrid search, or use query expansion |
| Right chunk retrieved but ranked low | Reranking | Add a reranker or raise top-k before context packing |
| Correct evidence present but answer misses it | Context assembly or model quality | Put key evidence earlier/later, reduce noise, or try a stronger local model |
| Answer invents unsupported details | Generation guardrails | Tighten prompt, require citations, post-check claims against chunks |
| Citations point to weak evidence | Citation discipline | Force citation IDs in the prompt and verify citations after generation |
| Latency becomes unacceptable | Prompt/context length or runtime | Lower top-k, shrink chunks, use caching, or choose a smaller/faster model |
| Memory spikes on long queries | KV cache | Lower context target, reduce retrieved text, or use a smaller model/quantization |

## Benchmark Log Template

Copy one row per question into [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] or a dated experiment note.

| Run id | Corpus version | Chunk policy | Context budget fit? | Embed/index | Model/runtime | Query id | Expected source | Retrieved top-k contains source? | Answer supported? | Citations valid? | TTFT | Total latency | Peak RAM/VRAM | Decision | Failure mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Yes/No |  |  |  |  | Yes/No | Yes/No | Yes/No |  |  |  | Pass/Hold/Fail |  |

## Completion Gate

The lab is complete when you have:

- a fixed corpus version and chunking policy
- a searchable index with stored metadata
- a local model endpoint that answers from retrieved context
- a context budget proving retrieved chunks, history, and output reserve fit
- at least 10 private evaluation questions
- evidence that known supporting passages appear in top-k
- answers with citations that can be traced back to chunks
- at least one documented retrieval miss, extraction failure, or hallucination case
- a pass/hold/fail decision using [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]]
- a minimal harness artifact set from [[LLM/Study/Local RAG Minimal Python Harness|Local RAG Minimal Python Harness]] if this is being used for the capstone or a real local assistant

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local RAG Minimal Python Harness]]
- [[LLM/Study/Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/2020–2021 — The Scaling Era/Retrieval Pipelines and Context Assembly]]
- [[LLM/2023 — Open Models and Agents/Embeddings and Vector Databases]]
- [[LLM/2023 — Open Models and Agents/Chunking Strategies]]
- [[LLM/2023 — Open Models and Agents/Reranking]]
- [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes]]
- [[LLM/_chunks/chunk-llm-225 DPR Dual-Encoder Dense Retrieval]]
- [[LLM/_chunks/chunk-llm-226 DPR In-Batch and Hard Negative Training]]
- [[LLM/_chunks/chunk-llm-227 DPR vs BM25 Retrieval Accuracy]]
- [[LLM/_chunks/chunk-llm-228 DPR as RAG Retrieval Backbone]]
