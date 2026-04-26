---
tags: [cs-ds, chunk]
id: chunk-ds-126
source: "[[raw-ds-010]]"
supports: ["[[Tries and Prefix Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Radix trees store entire edges as strings reducing node count

## Context
Standard tries have one node per character in the key.

## Claim
Radix trees (compact tries) store edge labels as strings instead of single characters. An internal node is created only where paths diverge reducing node count to O(n) for n keys.

## Why It Matters
Used in Linux kernel routing tables (radix tree), Redis, and HTTP routers for URL matching.

## QnA Seeds
- Q: How does radix tree differ from trie? -> A: Edge labels can be multi-character strings. Single-child chains are collapsed.
- Q: What triggers a node split? -> A: Inserting a key that diverges from an existing edge label mid-string.
