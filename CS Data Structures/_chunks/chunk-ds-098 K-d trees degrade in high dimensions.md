---
tags: [cs-ds, chunk]
id: chunk-ds-098
source: "[[raw-ds-020]]"
supports: ["[[k-d Trees and Spatial Data]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# K-d trees degrade in high dimensions due to curse of dimensionality

## Context
K-d trees work well in 2-3 dimensions.

## Claim
In high dimensions d greater than about 20 k-d tree pruning becomes ineffective because the splitting hyperplane affects a shrinking fraction of the space. Query time approaches O(n) and approximate methods like LSH become necessary.

## Why It Matters
Understanding dimensionality limits is essential for choosing the right spatial index structure.

## QnA Seeds
- Q: Why does pruning fail in high dimensions? -> A: Most of the space is far from any splitting plane so few branches are pruned.
- Q: What replaces k-d trees? -> A: LSH locality-sensitive hashing or approximate nearest neighbor methods.
