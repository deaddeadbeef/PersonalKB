---
tags: [cs-ds, chunk]
id: chunk-ds-138
source: "[[raw-ds-040]]"
supports: ["[[Foundational Concepts Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Succinct trees need only 2n plus o(n) bits for n nodes

## Context
Pointer-based trees use at least 16n bytes for n nodes.

## Claim
The number of distinct n-node binary trees is the nth Catalan number requiring ceiling(log2 C(n)) = 2n - O(log n) bits minimum. Succinct encodings like LOUDS and balanced parentheses achieve 2n + o(n) bits.

## Why It Matters
Reduces tree storage by 50-100x enabling in-memory representation of billion-node trees.

## QnA Seeds
- Q: What is the information-theoretic minimum? -> A: 2n - O(log n) bits from Catalan number.
- Q: What is balanced parentheses encoding? -> A: Open paren for each node in DFS visit, close paren when leaving.
