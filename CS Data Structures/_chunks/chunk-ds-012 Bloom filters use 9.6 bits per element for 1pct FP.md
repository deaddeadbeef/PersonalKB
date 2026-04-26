---
tags: [cs-ds, chunk]
id: chunk-ds-012
source: "[[raw-ds-009]]"
supports: ["[[Bloom Filters and Probabilistic Structures]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Bloom filters use 9.6 bits per element for 1 percent false positive rate

## Context
Exact set membership requires storing actual elements or hashes.

## Claim
A Bloom filter achieves 1 percent false positive rate using only 9.6 bits per element regardless of element size, with zero false negatives guaranteed.

## Why It Matters
Extraordinary space efficiency enables checking millions of URLs with kilobytes of memory.

## QnA Seeds
- Q: How many bits for 1 percent FP? -> A: 9.6 bits per element with k=7 hash functions.
- Q: Why no false negatives? -> A: Inserted elements set all k bits to 1 permanently.
