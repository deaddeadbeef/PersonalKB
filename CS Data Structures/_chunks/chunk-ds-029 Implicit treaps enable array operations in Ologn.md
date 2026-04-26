---
tags: [cs-ds, chunk]
id: chunk-ds-029
source: "[[raw-ds-025]]"
supports: ["[[Binary Search Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Implicit treaps enable array operations in Ologn via subtree sizes

## Context
Standard arrays have O(n) insert/delete at arbitrary positions.

## Claim
Implicit treaps use subtree sizes as implicit keys instead of stored keys, enabling split, merge, insert-at-position, delete-at-position, and reverse-range all in O(log n) expected time.

## Why It Matters
Turns a balanced BST into a powerful sequence data structure for competitive programming and text editors.

## QnA Seeds
- Q: How do implicit keys work? -> A: Position is computed from subtree sizes during traversal, not stored.
- Q: What operations does this enable? -> A: Split, merge, reverse range, insert/delete at any position.
