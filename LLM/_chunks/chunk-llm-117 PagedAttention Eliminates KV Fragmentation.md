---
tags: [chunk, llm]
id: "chunk-llm-117"
source: "[[LLM/_raw/raw-llm-030 vLLM PagedAttention Serving]]"
source_loc: "What Is This, Key Takeaways 1, 3"
topic: "PagedAttention non-contiguous KV cache"
claim: "PagedAttention manages KV cache as non-contiguous memory pages, eliminating the ~60-80% memory waste from internal fragmentation in naive implementations."
confidence: "verified"
supports: ["[[LLM/Inference and Serving/KV Cache and Context Reuse]]"]
up: "[[LLM/LLM]]"
---

# PagedAttention Eliminates KV Cache Memory Fragmentation

## Context
In naive LLM serving implementations, the KV (key-value) cache for each request is allocated as a single contiguous block of GPU memory sized for the maximum possible sequence length. Since most requests don't use the full context window, 60-80% of the allocated memory is wasted as internal fragmentation. This waste directly limits the number of concurrent requests a GPU can serve, severely reducing throughput.

PagedAttention, inspired by operating system virtual memory, divides the KV cache into fixed-size non-contiguous blocks (pages) mapped via a block table. Memory is allocated on demand as the sequence grows, page by page. When a request completes, its pages are immediately freed for reuse. This eliminates both internal fragmentation (unused space within allocations) and external fragmentation (unusable gaps between allocations), reducing KV cache memory waste to near zero.

## Why It Matters
KV cache memory is the primary bottleneck in LLM serving throughput. By eliminating 60-80% memory waste, PagedAttention enables serving 2-4× more concurrent requests on the same hardware. This directly translates to proportionally lower cost per token in production, making PagedAttention one of the highest-impact optimizations in the LLM serving stack.

## QnA Seeds
- Q: What problem does PagedAttention solve in LLM serving?
  A: It eliminates the 60-80% GPU memory waste caused by pre-allocating contiguous KV cache blocks for maximum sequence length, by instead using non-contiguous pages allocated on demand.
- Q: How is PagedAttention inspired by operating system design?
  A: It applies the virtual memory concept — mapping logical addresses to non-contiguous physical memory pages via a page/block table — to KV cache management in GPU memory.
