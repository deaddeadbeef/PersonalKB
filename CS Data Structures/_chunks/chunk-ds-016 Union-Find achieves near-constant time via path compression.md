---
tags: [cs-ds, chunk]
id: chunk-ds-016
source: "[[raw-ds-012]]"
supports: ["[[Disjoint Sets and Union-Find]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Union-Find achieves near-constant time via path compression plus union by rank

## Context
Naive union-find trees can become tall, making Find slow.

## Claim
Combining union by rank with path compression achieves O(alpha(n)) amortized per operation where alpha is inverse Ackermann -- at most 4 for any practical input.

## Why It Matters
Effectively constant-time, enabling near-linear MST and dynamic connectivity algorithms.

## QnA Seeds
- Q: What is inverse Ackermann? -> A: Extremely slowly growing function, at most 4 for all practical n.
- Q: Why both optimizations needed? -> A: Each alone gives O(log n); only combination achieves O(alpha(n)).
