---
tags: [cs-ds, chunk]
id: chunk-ds-002
source: "[[raw-ds-001]]"
supports: ["[[Arrays and Dynamic Arrays]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Arrays provide O(1) random access via base address arithmetic

## Context
Arrays store elements contiguously in memory.

## Claim
Array element access is O(1) because the address is computed directly: base_address + index * sizeof(element), requiring no traversal.

## Why It Matters
This constant-time access is the fundamental advantage of arrays and why they underpin most other data structures.

## QnA Seeds
- Q: Why is array access O(1)? -> A: Memory address computed arithmetically from base and index.
- Q: Why can't linked lists match this? -> A: Nodes are scattered in memory; reaching node i requires i pointer traversals.
