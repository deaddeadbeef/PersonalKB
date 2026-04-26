---
tags: [llm, inference]
up: "[[2024–2025 — Frontier and Efficiency Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Batching and Continuous Batching

> **One-line summary**: Continuous batching keeps GPU decode batches full by swapping finished requests out and new requests in at each iteration instead of waiting for the longest request to finish.

---

## 🎯 Intuition

### Core Idea
Batching multiple requests together is essential for efficient LLM serving because it amortizes the cost of loading model weights across multiple sequences, dramatically improving throughput. But naive static batching has a critical flaw: all sequences in a batch must stay together until the longest sequence finishes. If one sequence generates 500 tokens while others finish at 50 tokens, the short sequences sit idle, wasting GPU compute and memory.

### Analogy
Continuous batching is like **a restaurant seating new diners as tables open vs. waiting for everyone to finish**. Static batching waits for the slowest table; continuous batching refills capacity the moment space becomes available.

### Why It Matters
This "straggler problem" cripples throughput in production workloads where sequence lengths vary widely. Continuous batching (also called *iteration-level scheduling* or *dynamic batching*) fixes that by operating at the level of individual decoding iterations: as soon as one sequence finishes, the server evicts it and inserts a waiting request without disrupting the rest of the batch. The Orca paper from Microsoft showed throughput gains of roughly **2-20×** over static batching, especially when sequence-length variance is high.

---

## ⚙️ Core Mechanics

### How It Works
The key distinction is between the **prefill** and **decode** phases. Prefill processes the input prompt in parallel and computes KV cache for all prompt tokens at once, so it is primarily **compute-bound**. Decode generates one token at a time per active sequence, so it is primarily **memory-bound**. Continuous batching is most valuable in decode, where active sequences finish at different times and capacity can be reused immediately.

### Key Specs
- **Static batching**: wait for N requests, process until all complete, repeat
- **Continuous batching**: insert/evict at each iteration, maintaining a full batch dynamically
- **Iteration-level scheduling**: schedule at token-generation granularity rather than request granularity
- **Prefill phase**: parallel prompt processing that generates the initial KV cache
- **Decode phase**: sequential token generation, one token per iteration per sequence
- **Chunked prefill**: split long prompts into chunks so long prefills do not block decode traffic
- **Batch-size tradeoff**: larger batches usually increase throughput but also increase latency

### Key Facts
- Static batching wastes compute whenever short requests wait behind a long request.
- Continuous batching is the default pattern in modern serving stacks such as **vLLM**, **TGI**, and **TensorRT-LLM**.
- Mixing prefill and decode is tricky because prefill wants large compute-heavy work while decode wants low per-token latency.
- Chunked prefill is a practical compromise for systems that must serve both long prompts and responsive generation.


| Concept | What It Is | What It's Not |
| --- | --- | --- |
| **Static vs Continuous Batching** | Continuous: evict/insert at each iteration | Static: process entire batch to completion |
| **Prefill vs Decode** | Prefill: parallel prompt processing | Decode: sequential token generation |
| **Throughput vs Latency** | Throughput: tokens/sec (higher with batching) | Latency: time per request (increases with batch size) |
| **Chunked Prefill vs Full Prefill** | Split prompt into chunks, interleave with decode | Process entire prompt in one pass |
| **Iteration-Level vs Request-Level Scheduling** | Schedule at each token generation step | Schedule at request arrival/completion |
| **Batch Size vs Concurrency** | Batch size: sequences processed per iteration | Concurrency: total active requests in system |

---

## 🔬 Deep Dive

### Technical Details
Continuous batching works best when the serving layer can cheaply admit and evict sequences, which is why it pairs naturally with memory-management optimizations such as **PagedAttention**. Without good KV-cache management, the system may suffer fragmentation or allocation overhead whenever requests churn in and out of the active set.

The prefill/decode split is operationally important:
- **Prefill** benefits from parallelism over prompt tokens.
- **Decode** is inherently sequential per sequence and tends to be limited by memory bandwidth.
- A long prefill can starve latency-sensitive decode work unless the system chunks or schedules it carefully.

### Limitations
- Larger batches can improve throughput while harming user-perceived latency.
- Long-prompt prefills can still block short decode work if the scheduler is naive.
- Continuous batching helps most when workloads have variable output lengths; if all requests are near-identical, the advantage shrinks.

### Impact
Continuous batching is one of the main reasons production inference can handle multi-tenant chatbot and API traffic efficiently. Without it, a single long generation can monopolize the GPU while shorter requests pile up in the queue.

---

## 🏋️ Practice

### Warm-Up
1. Why does static batching suffer from the straggler problem?
2. Which phase is compute-bound: prefill or decode?
3. Why does larger batch size usually increase throughput?

### Core Problems
1. Explain why continuous batching is scheduled at the iteration level rather than the request level.
2. Compare prefill and decode in terms of hardware bottlenecks and scheduling goals.
3. Describe when chunked prefill becomes necessary in a production serving system.

### Challenge
Design a serving policy for a chatbot workload with many short prompts and occasional very long prompts. Explain how you would balance throughput, latency, and fairness using continuous batching plus chunked prefill.

---

## Supporting Chunks

_Placeholder for links to specific techniques, implementation details, and case studies._

---

## References to Sources Index

_Placeholder for references to papers, documentation, and source materials._
