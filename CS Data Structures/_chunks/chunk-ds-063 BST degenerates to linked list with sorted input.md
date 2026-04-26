---
tags: [cs-ds, chunk]
id: chunk-ds-063
source: "[[raw-ds-004]]"
supports: ["[[Binary Search Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# BST degenerates to a linked list with sorted input giving On height

## Context
BST shape depends on insertion order.

## Claim
Inserting sorted or reverse-sorted keys into a BST creates a single chain with height n making all operations O(n). This worst case motivates self-balancing trees.

## Why It Matters
The fundamental reason balanced BST variants (AVL, Red-Black, B-tree) exist.

## QnA Seeds
- Q: What input causes worst-case BST? -> A: Sorted or reverse-sorted keys create a linear chain.
- Q: What is the expected height with random input? -> A: O(log n) matching balanced trees.
