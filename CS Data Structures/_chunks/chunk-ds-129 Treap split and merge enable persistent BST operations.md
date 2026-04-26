---
tags: [cs-ds, chunk]
id: chunk-ds-129
source: "[[raw-ds-025]]"
supports: ["[[Binary Search Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Treap split and merge enable persistent and concurrent BST operations

## Context
Split and merge are fundamental operations for functional BST implementations.

## Claim
Treap split divides tree by key threshold in O(log n) expected. Merge combines two treaps where all keys in one are less than all in the other in O(log n) expected. Together they enable persistent updates and simple concurrent modifications.

## Why It Matters
Foundation for persistent ordered sets in functional programming and for implicit treap array operations.

## QnA Seeds
- Q: What is the precondition for merge? -> A: All keys in left treap must be less than all keys in right treap.
- Q: How does split work? -> A: Recursively split at root based on key comparison and random priority.
