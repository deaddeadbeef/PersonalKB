---
tags: [cs-ds, chunk]
id: chunk-ds-071
source: "[[raw-ds-010]]"
supports: ["[[Ternary Search Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Ternary search trees use less memory than tries for sparse alphabets

## Context
Standard tries allocate child array of size sigma at every node regardless of occupancy.

## Claim
Ternary search trees store one character per node with three children (less, equal, greater) using only O(n) total pointers versus O(n * sigma) for naive tries.

## Why It Matters
Practical compromise between BST and trie: trie-like prefix operations with BST-like space.

## QnA Seeds
- Q: What are the three children? -> A: Less than, equal to, and greater than the stored character.
- Q: When to use TST vs trie? -> A: TST when alphabet is large and keys share few prefixes.
