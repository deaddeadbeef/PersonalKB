---
id: chunk-algo-131
type: chunk
source: "[[raw-algo-023]]"
source_loc: "Union-Find - Atomic Facts"
topic: "data-structures"
claim: "Union by rank attaches the lower-rank tree under the higher-rank root; a tree of rank r has >= 2^r nodes (by induction), so maximum rank is floor(log n), guaranteeing O(log n) height without path compression."
confidence: verified
supports:
  - "[[Union-Find]]"
tags:
  - cs-algorithms
  - cs-algorithms/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# Union by Rank Guarantees O(log n) Tree Height

## Context

Ranks increase only when merging equal-rank trees, increasing the result's rank by 1. A tree of rank r has >= 2^r nodes because merging two rank-(r-1) trees (each with >= 2^{r-1} nodes) yields >= 2^r nodes. Maximum rank is floor(log n), bounding height to O(log n). Union by size (smaller under larger) is an equivalent alternative. Both are crucial prerequisites for the O(alpha(n)) combined bound with path compression.

## Why It Matters

Union by rank prevents degeneration to linked lists. The 2^r node count invariant is the core structural lemma for both the standalone O(log n) and the combined O(alpha(n)) bounds.

## QnA Seeds

- Q: What does the rank field represent?
- Q: Why does rank-r tree have >= 2^r nodes?
- Q: When does rank increase during Union?