---
tags: [cs-ds, chunk]
id: chunk-ds-014
source: "[[raw-ds-010]]"
supports: ["[[Suffix Arrays]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Suffix arrays replace suffix trees with 3-5x less space

## Context
Suffix trees use approximately 20n bytes; suffix arrays use 4-8n bytes.

## Claim
Suffix arrays provide equivalent functionality to suffix trees for most applications while using 3-5x less space and offering better cache performance.

## Why It Matters
Critical for genomics where strings are billions of characters long.

## QnA Seeds
- Q: Why more space-efficient? -> A: Store only integer indices (4-8 bytes) vs tree nodes with pointers (~20 bytes each).
- Q: What extra structure needed? -> A: LCP array, built in O(n) via Kasai's algorithm.
