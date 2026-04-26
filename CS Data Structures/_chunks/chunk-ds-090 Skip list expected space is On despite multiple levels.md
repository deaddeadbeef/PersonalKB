---
tags: [cs-ds, chunk]
id: chunk-ds-090
source: "[[raw-ds-011]]"
supports: ["[[Skip Lists]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Skip list expected space is O(n) despite multiple levels of pointers

## Context
Skip lists promote elements to multiple levels using random coin flips.

## Claim
Each element is promoted with probability 1/2 so expected number of pointers per element is 1 + 1/2 + 1/4 + ... = 2 giving O(2n) = O(n) total space. Only O(log n) levels expected.

## Why It Matters
Space overhead is modest and predictable making skip lists practical alternatives to balanced BSTs.

## QnA Seeds
- Q: Expected pointers per element? -> A: 2 on average from geometric series 1 + 1/2 + 1/4 + ...
- Q: Expected number of levels? -> A: O(log n) with high probability.
