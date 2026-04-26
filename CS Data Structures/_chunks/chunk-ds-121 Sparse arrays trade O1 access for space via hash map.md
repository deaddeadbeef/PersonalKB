---
tags: [cs-ds, chunk]
id: chunk-ds-121
source: "[[raw-ds-001]]"
supports: ["[[Arrays and Dynamic Arrays]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Sparse arrays trade O1 access for space via hash map backing

## Context
Large arrays with few non-default values waste enormous memory.

## Claim
Sparse arrays store only non-default values in a hash map keyed by index. Access is O(1) expected. Space is O(k) where k is the number of non-default entries instead of O(n) for the full range.

## Why It Matters
Essential for scientific computing, sparse matrices, and game maps where most cells are empty.

## QnA Seeds
- Q: What backing structure? -> A: Hash map from index to value. Default value returned for absent keys.
- Q: When to switch to dense array? -> A: When density exceeds about 30 percent hash overhead exceeds savings.
