---
tags: [cs-ds, chunk]
id: chunk-ds-006
source: "[[raw-ds-004]]"
supports: ["[[Binary Search Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# BST in-order traversal yields sorted output in O(n)

## Context
The BST property (left < root < right) creates an implicit ordering.

## Claim
In-order traversal visits all n nodes in sorted key order in O(n) time, making BSTs natural for maintaining sorted dynamic data.

## Why It Matters
This connects BSTs to sorting: building a BST from n elements and traversing in-order is equivalent to sorting.

## QnA Seeds
- Q: What traversal gives sorted output from BST? -> A: In-order: left subtree, root, right subtree.
- Q: How does BST relate to quicksort? -> A: BST insertion sequence mirrors quicksort partitioning.
