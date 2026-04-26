---
tags: [cs-ds, chunk]
id: chunk-ds-023
source: "[[raw-ds-022]]"
supports: ["[[Foundational Concepts Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Cache-oblivious structures optimize for all cache levels simultaneously

## Context
Cache-aware algorithms are tuned to specific hardware parameters.

## Claim
Cache-oblivious algorithms achieve optimal cache performance for every level of the memory hierarchy without knowing cache line size or cache capacity.

## Why It Matters
Portable performance across hardware without parameter tuning.

## QnA Seeds
- Q: What makes cache-oblivious different from cache-aware? -> A: No parameters B or M needed.
- Q: Give an example. -> A: Van Emde Boas tree layout achieves optimal search without knowing B.
