---
tags: [cs-ds, chunk]
id: chunk-ds-115
source: "[[raw-ds-020]]"
supports: ["[[k-d Trees and Spatial Data]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# K-d tree nearest neighbor uses priority queue for best-first search

## Context
Naive nearest neighbor in k-d tree may visit many branches.

## Claim
Best-first search maintains a priority queue of unexplored subtrees ordered by minimum possible distance. This prunes more aggressively than depth-first reaching the answer in O(log n) expected for low dimensions.

## Why It Matters
The standard algorithm for nearest neighbor search in k-d trees used in computer vision and robotics.

## QnA Seeds
- Q: What is the pruning criterion? -> A: Skip subtree if minimum distance to its bounding box exceeds current best.
- Q: Expected complexity? -> A: O(log n) for low dimensions but degrades to O(n) in high dimensions.
