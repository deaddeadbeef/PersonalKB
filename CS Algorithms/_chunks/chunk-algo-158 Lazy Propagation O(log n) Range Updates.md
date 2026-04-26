---
id: chunk-csa-158
type: chunk
source: "[[Halim 2013 - Segment Trees]]"
source_loc: "Lazy Propagation"
topic: "data-structures"
claim: "Lazy propagation enables O(log n) range updates on segment trees by deferring modifications to subtrees until they are queried"
confidence: verified
supports:
  - "[[Segment Tree]]"
  - "[[Lazy Propagation]]"
tags:
  - csa
  - csa/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# Data Structures — Lazy propagation defers range updates for O(log n) cost

## Context

Without lazy propagation, updating every element in a range [l, r] would cost O(n) per update. Lazy propagation stores a pending update tag at a node indicating a deferred modification to its entire subtree. The tag is propagated to children only when those children are accessed (pushed down before any query or update traverses into them). This amortizes the update cost to O(log n). Common lazy operations include range addition, range assignment, and range flip. A separate lazy array stores pending values alongside the segment tree.

## Why It Matters

Lazy propagation transforms segment trees from a query-only structure into one supporting efficient range modifications, essential for problems requiring both range queries and range updates.

## QnA Seeds

- Q: How does lazy propagation convert O(n) range updates to O(log n)?
- Q: When are lazy tags pushed down to children in a segment tree?
- Q: What are common operations enhanced by lazy propagation?
