---
id: chunk-csa-160
type: chunk
source: "[[Halim 2013 - Segment Trees]]"
source_loc: "Persistent and 2D Variants"
topic: "data-structures"
claim: "Persistent segment trees enable querying historical versions using O(log n) additional nodes per update by sharing structure between versions"
confidence: verified
supports:
  - "[[Segment Tree]]"
  - "[[Persistent Data Structures]]"
tags:
  - csa
  - csa/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# Data Structures — Persistent segment tree O(log n) nodes per version

## Context

A persistent segment tree allows querying any historical version of the data structure after a sequence of updates. Each update creates a new root and duplicates only the O(log n) nodes on the path from the updated leaf to the root, sharing all other nodes with the previous version. This uses O(log n) additional space per update while preserving all previous versions. Two-dimensional segment trees (segment tree of segment trees) extend range queries to rectangular regions in O(log^2 n) time, useful in computational geometry and image processing.

## Why It Matters

Persistent data structures are essential for functional programming, version control-style queries, and problems requiring access to historical states without O(n)-per-version copying.

## QnA Seeds

- Q: How does a persistent segment tree share structure between versions?
- Q: What is the per-update space cost of a persistent segment tree?
- Q: What is the query complexity of a 2D segment tree?
