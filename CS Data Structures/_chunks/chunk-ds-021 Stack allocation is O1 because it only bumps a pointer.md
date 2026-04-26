---
tags: [cs-ds, chunk]
id: chunk-ds-021
source: "[[raw-ds-021]]"
supports: ["[[Foundational Concepts Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Stack allocation is O1 because it only bumps a pointer

## Context
Memory allocation strategies have vastly different costs.

## Claim
Stack allocation requires only incrementing the stack pointer making it O(1) with zero fragmentation.

## Why It Matters
This is why local variables are nearly free and stack-based designs outperform heap-heavy ones.

## QnA Seeds
- Q: Why is stack alloc faster than heap? -> A: Single pointer bump vs free list search.
- Q: What limits stack allocation? -> A: Fixed size, LIFO lifetime only.
