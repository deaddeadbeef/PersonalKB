---
tags: [cs-ds, chunk]
id: chunk-ds-084
source: "[[raw-ds-004]]"
supports: ["[[Binary Search Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# BST delete with two children uses inorder successor swap

## Context
Deleting a BST node with two children cannot simply remove it.

## Claim
Replace the deleted nodes key with its inorder successor (smallest in right subtree) then delete the successor which has at most one child. This preserves BST property in O(h) time.

## Why It Matters
The trickiest BST operation. Understanding it is prerequisite for balanced tree deletion.

## QnA Seeds
- Q: Why inorder successor? -> A: Smallest key larger than deleted key preserves BST ordering.
- Q: Could you use inorder predecessor instead? -> A: Yes both work. Some implementations alternate to balance.
