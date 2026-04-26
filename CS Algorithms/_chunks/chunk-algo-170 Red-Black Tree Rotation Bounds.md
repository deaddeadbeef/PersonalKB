---
id: chunk-csa-170
type: chunk
source: "[[Cormen 2022 - Red-Black Trees]]"
source_loc: "Insertion and Deletion"
topic: "data-structures"
claim: "Red-black tree insertion requires at most 2 rotations and O(log n) recolorings; deletion requires at most 3 rotations and O(log n) recolorings"
confidence: verified
supports:
  - "[[Red-Black Tree]]"
  - "[[Balanced BST]]"
tags:
  - csa
  - csa/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# Data Structures — Red-black insert max 2 rotations, delete max 3 rotations

## Context

Insertion adds a red node which may violate property 4 (red parent with red child). The fixup has three cases: uncle is red (recolor and move up), uncle is black with triangle configuration (rotate to line), uncle is black with line configuration (rotate and recolor). This requires at most 2 rotations and O(log n) recolorings. Deletion may violate property 5 (black-height imbalance), requiring fixup with four cases based on sibling and its children's colors—at most 3 rotations and O(log n) recolorings. The constant rotation bound is the key advantage over AVL trees.

## Why It Matters

The bounded rotation count makes red-black trees preferable for write-heavy workloads, as each modification requires only O(1) structural changes even though recolorings may propagate.

## QnA Seeds

- Q: What are the three cases in red-black insertion fixup?
- Q: Why is the constant rotation bound significant compared to AVL trees?
- Q: What invariant does insertion fixup restore and what does deletion fixup restore?
