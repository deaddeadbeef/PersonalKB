---
tags: [cs-ds, chunk]
id: chunk-ds-085
source: "[[raw-ds-005]]"
supports: ["[[Red-Black Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Red-Black tree height is at most 2 log2 n plus 1

## Context
AVL trees guarantee 1.44 log n. Red-Black is less strict.

## Claim
Red-Black trees guarantee height at most 2 log2(n+1) due to the black-height property: every root-to-leaf path has the same number of black nodes and red nodes cannot be adjacent.

## Why It Matters
The 2x factor vs AVL means slightly worse read performance but fewer rotations on writes.

## QnA Seeds
- Q: Why 2x the optimal? -> A: A path can alternate red-black doubling length while maintaining equal black-height.
- Q: What is black-height? -> A: Number of black nodes on any path from a node to a leaf.
