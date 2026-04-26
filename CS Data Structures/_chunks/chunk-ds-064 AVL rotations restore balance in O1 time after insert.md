---
tags: [cs-ds, chunk]
id: chunk-ds-064
source: "[[raw-ds-005]]"
supports: ["[[AVL Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# AVL rotations restore balance in O1 time after insert

## Context
After AVL insert the balance factor of ancestors may violate the -1 to 1 constraint.

## Claim
At most two rotations (single or double) suffice to restore balance after an insert each taking O(1) time. Only ancestors of the inserted node need checking.

## Why It Matters
Rotations are the mechanism that converts O(n) worst-case BST height to guaranteed O(log n).

## QnA Seeds
- Q: How many rotations for insert? -> A: At most 2 (one single or one double rotation).
- Q: How many rotations for delete? -> A: Up to O(log n) since rebalancing can cascade upward.
