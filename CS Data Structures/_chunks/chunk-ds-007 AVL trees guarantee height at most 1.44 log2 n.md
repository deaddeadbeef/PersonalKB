---
tags: [cs-ds, chunk]
id: chunk-ds-007
source: "[[raw-ds-005]]"
supports: ["[[AVL Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# AVL trees guarantee height at most 1.44 log2 n via balance factors

## Context
Unbalanced BSTs can degrade to O(n) height.

## Claim
AVL trees maintain balance factor of -1, 0, or 1 at every node, guaranteeing height at most 1.44 log2(n) and O(log n) worst-case operations.

## Why It Matters
As the first self-balancing BST (1962), AVL trees proved logarithmic worst-case was achievable with local rotations.

## QnA Seeds
- Q: What is AVL balance factor constraint? -> A: Every node has balance factor in {-1, 0, 1}.
- Q: AVL vs Red-Black? -> A: AVL more strictly balanced (faster reads) but more rotations on writes.
