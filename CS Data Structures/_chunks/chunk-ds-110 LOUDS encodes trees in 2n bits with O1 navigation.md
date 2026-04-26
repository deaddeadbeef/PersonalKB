---
tags: [cs-ds, chunk]
id: chunk-ds-110
source: "[[raw-ds-040]]"
supports: ["[[Foundational Concepts Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# LOUDS encodes trees in 2n bits with O1 navigation

## Context
Pointer-based trees use 16+ bytes per node.

## Claim
Level-Order Unary Degree Sequence encodes an n-node tree in 2n+1 bits. Child and parent navigation uses rank and select on the bit vector achieving O(1) per operation.

## Why It Matters
Encodes the entire tree structure of XML documents or file system hierarchies in bits instead of bytes.

## QnA Seeds
- Q: How is LOUDS constructed? -> A: BFS order. Each node writes degree in unary (d ones then a zero).
- Q: How to find children? -> A: rank and select on the bit vector to map between node and child positions.
