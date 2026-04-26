---
tags: [chunk, llm]
id: "chunk-llm-119"
source: "[[LLM/_raw/raw-llm-030 vLLM PagedAttention Serving]]"
source_loc: "Key Takeaways 2"
topic: "PagedAttention copy-on-write memory sharing"
claim: "PagedAttention enables efficient memory sharing across requests (e.g., shared system prompt KV cache) through copy-on-write semantics."
confidence: "verified"
supports: ["[[LLM/Inference and Serving/KV Cache and Context Reuse]]"]
up: "[[LLM/LLM]]"
---

# PagedAttention Enables Copy-on-Write KV Cache Sharing

## Context
PagedAttention's block-based memory management naturally supports memory sharing across requests through copy-on-write (CoW) semantics, borrowed from OS virtual memory design. When multiple requests share the same prefix (e.g., a system prompt that is identical across all requests), their KV cache pages for that prefix can point to the same physical memory blocks. Pages are only duplicated when one request diverges from the shared prefix — hence "copy-on-write."

This is particularly valuable for parallel sampling (generating multiple completions for one prompt), beam search (maintaining multiple hypothesis beams), and the common production pattern where all requests share a long system prompt. Without CoW, serving N parallel samples requires N copies of the prompt's KV cache; with CoW, they share one copy, reducing memory usage by up to (N-1)/N for the shared portion.

## Why It Matters
System prompt KV cache sharing is critical for production LLM serving, where system prompts can consume thousands of tokens across all requests. Copy-on-write eliminates this redundant memory usage, enabling higher concurrency and lower latency. For beam search and parallel sampling, CoW makes these techniques practical at scale by eliminating the memory multiplication that previously made them prohibitively expensive.

## QnA Seeds
- Q: How does PagedAttention enable memory sharing across requests?
  A: Through copy-on-write semantics — requests sharing the same prefix (e.g., system prompt) point to the same physical KV cache pages, which are only duplicated when a request diverges from the shared content.
- Q: What practical scenarios benefit most from copy-on-write KV cache sharing?
  A: Shared system prompts across all requests (reduces per-request memory), parallel sampling (N completions share one prompt cache), and beam search (hypothesis beams share common prefix pages).
