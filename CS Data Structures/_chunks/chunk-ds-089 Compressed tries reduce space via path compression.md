---
tags: [cs-ds, chunk]
id: chunk-ds-089
source: "[[raw-ds-010]]"
supports: ["[[Tries and Prefix Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Compressed tries reduce space from O(n sigma) to O(n) via path compression

## Context
Standard tries allocate sigma-sized arrays at every node wasting space.

## Claim
Compressed tries (Patricia tries) merge chains of single-child nodes into single edges labeled with entire substrings reducing total nodes from O(n sigma) to O(n) where n is the number of stored strings.

## Why It Matters
Makes tries practical for large datasets. Used in IP routing tables and text indices.

## QnA Seeds
- Q: What is path compression? -> A: Single-child chains collapsed into one edge with multi-character label.
- Q: Space improvement? -> A: From O(total character count times sigma) to O(total character count).
