---
tags: [llm, inference]
up: "[[2024–2025 — Frontier and Efficiency Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# KV Cache and Context Reuse

> **One-line summary**: The KV cache speeds autoregressive inference by storing prior attention keys and values so each new token can reuse past computation instead of recomputing it.

---

## 🎯 Intuition

### Core Idea
The KV cache stores previously computed **key** and **value** vectors from the attention mechanism during autoregressive generation. When a new token is generated, it still needs to attend to all earlier tokens, but the keys and values for those earlier tokens do not change. Caching them avoids recomputing that work every step.

### Analogy
The KV cache is like **bookmarks in a textbook — remember where you left off**. Instead of reopening every chapter from scratch each time, the model keeps the useful positions ready for reuse.

### Why It Matters
Without KV caching, inference would repeatedly recompute attention over the full prefix at every step, making generation much slower. The cache changes the practical cost profile of generation, but it also introduces a major memory bottleneck.

---

## ⚙️ Core Mechanics

### How It Works
For each layer and token position, the model stores the computed `(key, value)` tensors. During decode, the new token only needs to compute its own query plus the new key/value entries, then attend over the existing cached tensors. This trades **memory for speed**.

### Key Specs
- **Cache structure**: stores key/value tensors for each layer and token position
- **Memory formula**: `2 × layers × seq_len × hidden_dim × bytes_per_element × batch_size`
- **Scaling**: cache memory grows linearly with sequence length and batch size
- **MQA**: one KV head shared by all query heads, often cutting cache size by about **8×**
- **GQA**: query heads grouped to share KV heads; **Llama 2** uses **8 groups for 32 query heads**
- **PagedAttention**: block-level memory management with copy-on-write support for cases like beam search
- **Prefix caching**: hash and reuse KV states for repeated prompt prefixes
- **Eviction**: when memory fills, systems may drop old tokens or use sliding-window attention

### Key Facts
- For a **7B** model with **32 layers**, **4096 hidden size**, and **FP16**, a single **2048-token** sequence can use roughly **1 GB** of KV-cache memory.
- At long context lengths, KV cache can exceed the memory used by the model weights.
- **PagedAttention** makes continuous batching practical by reducing fragmentation.
- **Prefix caching** is especially useful when many requests share the same system prompt or few-shot prefix.


| Concept | What It Is | What It's Not |
| --- | --- | --- |
| **KV Cache vs Activations** | Stored across generation steps, grows with sequence length | Temporary per-forward-pass, fixed size per batch |
| **MQA vs GQA** | MQA = 1 KV head shared by all queries | GQA = multiple groups, each with shared KV head |
| **PagedAttention vs Prefix Caching** | Memory management (how to store) | Content deduplication (what to reuse) |
| **Cache Size vs Model Size** | Often larger than weights for long contexts | Not the same as parameter memory |
| **Prefill vs Decode** | Prefill builds initial cache, parallel | Decode appends one token at a time |

---

## 🔬 Deep Dive

### Technical Details
The KV cache is central to why autoregressive decoding is practical. It turns repeated full-prefix recomputation into incremental extension. But the price is memory pressure. Since the cache grows with **sequence length × layers × hidden size × batch size**, inference servers handling many long-context requests can run out of VRAM even when weights are quantized.

This is why architectural and systems optimizations matter:
- **MQA** aggressively compresses KV storage by sharing one KV head.
- **GQA** provides a compromise between memory savings and expressivity.
- **PagedAttention** treats cache allocation more like virtual memory, allowing non-contiguous blocks and avoiding fragmentation.
- **Prefix caching** reuses already-built prefix states across requests.

### Limitations
- Cache growth is still linear in context length and concurrency.
- Reuse only helps when the prefix really is shared or still relevant.
- Memory savings techniques can introduce quality or architectural tradeoffs.

### Impact
KV-cache engineering strongly influences capacity planning, latency, and throughput in production inference. Many real serving gains come less from changing the model than from storing, sharing, and scheduling KV state more intelligently.

---

## 🏋️ Practice

### Warm-Up
1. What does the KV cache store?
2. Why does autoregressive inference get much slower without it?
3. Which grows cache size faster: longer contexts or larger batches?

### Core Problems
1. Explain the memory formula for KV cache and what each term represents.
2. Compare MQA, GQA, PagedAttention, and prefix caching by the problem each one solves.
3. Why can KV cache become the dominant memory consumer during inference?

### Challenge
You are serving a chatbot with long shared system prompts and occasional 100K-token contexts. Propose a KV-cache strategy that balances reuse, fragmentation control, and memory pressure.

For local operations, use [[LLM/Study/Local LLM Serving Internals and Scheduler Lab|Local LLM Serving Internals and Scheduler Lab]] to connect KV-cache claims to scheduler evidence: active sequences, slots, max batched tokens, preemption, OOM, queueing, and long-prompt interference. Use [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]] to save loaded-model state, prompt tokens, active requests, cache usage or prefix-cache counters when the runtime exposes them, memory pressure, and the next controlled change. Use [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab|Local LLM Prompt Cache and KV Reuse Lab]] when the question is whether repeated prefixes actually reduce prefill or TTFT.

---

## Supporting Chunks

- [[chunk-llm-214 KV Cache Memory Bandwidth Bottleneck]] — decode bottleneck caused by reading cached keys and values
- [[chunk-llm-213 Multi-Query Attention Shared KV Heads]] — MQA as an architectural cache-size reduction
- [[chunk-llm-217 GQA Mechanism Interpolating MHA and MQA]] — GQA as the practical middle ground between MHA and MQA
- [[chunk-llm-117 PagedAttention Eliminates KV Fragmentation]] — cache allocation as virtual-memory-style paging
- [[chunk-llm-119 PagedAttention Copy-on-Write Sharing]] — shared-prefix and beam-search cache reuse
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]] — local evidence for KV pressure, preemption, slots, and batching decisions
- [[LLM/Study/Local LLM Observability and Operations Runbook]] — local evidence for cache pressure and resource counters
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab]] — local repeated-prefix, prompt-cache, and cache-hit evidence
- [[chunk-llm-260 Prompt caching reduces input token costs 50-90 percent by reusing KV cache for repeated prefixes]] — prefix caching for repeated context

---

## See Also

- [[Attention Mechanism]] — KV cache stores precomputed attention key-value states
- [[Transformer Architecture]] — caching is integral to transformer autoregressive inference
- [[Quantization]] — compressing KV cache entries with quantization techniques
- [[Scaling Laws]] — KV cache memory scales linearly with context length
- [[Chunking Strategies]] — chunk boundaries interact with cache management

---

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/_raw/raw-llm-030 vLLM PagedAttention Serving|vLLM PagedAttention Serving]]
- [[LLM/_raw/raw-llm-054 Fast Transformer Decoding One Write-Head MQA|Fast Transformer Decoding: One Write-Head Is All You Need]]
- [[LLM/_raw/raw-llm-055 GQA Training Generalized Multi-Query Transformer Models|GQA: Training Generalized Multi-Query Transformer Models]]
- [[Batching and Continuous Batching]]
- [[Serving Architectures and Throughput-Latency Trade-offs]]
- [[Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab]]
