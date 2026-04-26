---
tags: [cs-ds, chunk]
id: chunk-ds-095
source: "[[raw-ds-016]]"
supports: ["[[Binary Search Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Splay tree sequential access theorem gives On total for sorted traversal

## Context
Individual splay operations can cost O(n). Is sequential access efficient?

## Claim
Accessing all n elements of a splay tree in sorted order costs O(n) total (amortized O(1) per access) due to the sequential access theorem. The tree restructures to make in-order traversal cheap.

## Why It Matters
Proves splay trees are competitive with any BST for any access sequence (dynamic optimality conjecture).

## QnA Seeds
- Q: What is the sequential access theorem? -> A: Accessing keys in sorted order costs O(n) total in a splay tree.
- Q: What is dynamic optimality? -> A: Conjecture that splay trees match any BST on any access sequence within constant factor.
