---
tags: [cs-ds, chunk]
id: chunk-ds-159
source: "[[raw-ds-040]]"
supports: ["[[Foundational Concepts Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Information-theoretic lower bound sets minimum bits for any encoding

## Context
How compact can a data structure possibly be?

## Claim
For a combinatorial object with N possible instances the minimum encoding requires ceiling(log2 N) bits. Any structure using this minimum is implicit. Succinct uses minimum plus lower-order terms.

## Why It Matters
Provides absolute reference point for evaluating space efficiency of any data structure.

## QnA Seeds
- Q: Example for binary trees? -> A: C(n) distinct trees. Minimum is about 2n bits (Catalan number log).
- Q: Example for permutations? -> A: n! permutations. Minimum is about n log2 n bits.
