---
tags: [cs-ds, chunk]
id: chunk-ds-028
source: "[[raw-ds-025]]"
supports: ["[[Binary Search Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Treaps combine BST and heap properties with random priorities

## Context
Balanced BSTs require complex rotation rules (AVL, Red-Black).

## Claim
Treaps assign random priorities at insertion and maintain BST order on keys and heap order on priorities, achieving O(log n) expected height with simpler code than deterministic balanced trees.

## Why It Matters
Treaps provide the simplicity of randomized algorithms with the power of balanced search trees.

## QnA Seeds
- Q: What makes a treap balanced? -> A: Random priorities create the same distribution as a randomly built BST.
- Q: Treap vs Red-Black? -> A: Simpler code and native split/merge, but expected not worst-case.
