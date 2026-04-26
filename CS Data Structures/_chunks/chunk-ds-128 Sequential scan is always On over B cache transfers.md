---
tags: [cs-ds, chunk]
id: chunk-ds-128
source: "[[raw-ds-022]]"
supports: ["[[Foundational Concepts Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Sequential scan is always O(n over B) cache transfers

## Context
Sequential memory access is the best case for cache performance.

## Claim
Scanning n elements sequentially requires exactly n/B cache transfers where B is the cache line size in elements. This is optimal because every transferred byte is used and hardware prefetching fully overlaps latency.

## Why It Matters
The baseline for cache performance. Any data structure aspiring to cache efficiency must approach this rate.

## QnA Seeds
- Q: Why is n/B optimal? -> A: Each cache line of B elements is fetched exactly once with zero waste.
- Q: How does prefetching help? -> A: Hardware detects sequential pattern and fetches next lines before they are needed.
