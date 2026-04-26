---
id: chunk-algo-130
type: chunk
source: "[[raw-algo-023]]"
source_loc: "Union-Find - Atomic Facts"
topic: "data-structures"
claim: "Path compression sets every node on the Find path directly to the root, flattening the tree; path splitting and halving are single-pass alternatives achieving the same O(alpha(n)) asymptotic bound."
confidence: verified
supports:
  - "[[Union-Find]]"
tags:
  - cs-algorithms
  - cs-algorithms/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# Path Compression Flattens Find Trees to Root

## Context

Find with path compression uses two passes: first traverse to root, then set every visited node's parent to root. Subsequent Finds on any path node take O(1). Path splitting (each node points to grandparent) and path halving (every other node points to grandparent) achieve O(alpha(n)) in a single pass. Without path compression, union by rank alone keeps height O(log n); the combination reduces effective height to O(alpha(n)) amortized.

## Why It Matters

Path compression is the key heuristic taking Union-Find from O(log n) to O(alpha(n)). Understanding its variants matters for efficient implementation.

## QnA Seeds

- Q: How does path compression modify the tree during Find?
- Q: How do path splitting and halving compare to full compression?
- Q: What is Find complexity with rank alone vs with compression?