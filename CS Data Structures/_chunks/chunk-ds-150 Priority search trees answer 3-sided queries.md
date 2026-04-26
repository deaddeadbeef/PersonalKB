---
tags: [cs-ds, chunk]
id: chunk-ds-150
source: "[[raw-ds-035]]"
supports: ["[[k-d Trees and Spatial Data]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Priority search trees answer 3-sided queries in Ologn plus k

## Context
Some spatial queries have bounded constraint on one side only.

## Claim
Priority search trees combine BST on x-coordinate with heap on y-coordinate in a single structure. They answer 3-sided queries (x in range, y above threshold) in O(log n + k) with O(n) space.

## Why It Matters
Optimal for 3-sided queries. Used in computational geometry for maxima queries and visibility problems.

## QnA Seeds
- Q: What is a 3-sided query? -> A: x1 <= x <= x2 and y >= y0. Three of four sides bounded.
- Q: Why O(n) space? -> A: Single tree combining both dimensions unlike range trees which nest structures.
