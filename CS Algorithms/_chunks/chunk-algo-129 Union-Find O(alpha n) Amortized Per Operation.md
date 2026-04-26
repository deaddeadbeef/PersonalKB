---
id: chunk-algo-129
type: chunk
source: "[[raw-algo-023]]"
source_loc: "Union-Find - Key Claims"
topic: "data-structures"
claim: "Union-Find with union by rank and path compression achieves O(alpha(n)) amortized per operation, where alpha is the inverse Ackermann function; Fredman-Saks (1989) proved matching Omega(alpha(n)) lower bound for pointer-based implementations."
confidence: verified
supports:
  - "[[Union-Find]]"
  - "[[Amortized Analysis]]"
tags:
  - cs-algorithms
  - cs-algorithms/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# Union-Find O(alpha n) Amortized Per Operation

## Context

The inverse Ackermann alpha(n) grows so slowly that alpha(2^{2^{2^{65536}}}) = 4; for all practical n, alpha(n) <= 4, making operations effectively O(1). Without optimizations, Find degrades to O(n); union by rank alone achieves O(log n). Tarjan (1975) proved the combined O(alpha(n)) bound via a sophisticated potential argument. Fredman-Saks's matching lower bound makes Union-Find provably optimal among pointer-based disjoint set structures.

## Why It Matters

Union-Find is one of the most elegant data structures, achieving near-constant time through two simple heuristics with matching upper and lower bounds—a rare example of a provably optimal data structure.

## QnA Seeds

- Q: What is Union-Find amortized complexity with both optimizations?
- Q: What is alpha(n) for practical input sizes?
- Q: Why is O(alpha(n)) essentially optimal?