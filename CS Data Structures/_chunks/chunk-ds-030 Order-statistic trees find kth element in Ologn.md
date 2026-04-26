---
tags: [cs-ds, chunk]
id: chunk-ds-030
source: "[[raw-ds-026]]"
supports: ["[[Advanced Structures Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Order-statistic trees find kth element in Ologn via size augmentation

## Context
Finding the kth smallest element in a sorted set normally requires O(n) scan.

## Claim
Augmenting each BST node with its subtree size enables O(log n) rank and select queries — find kth element or determine the rank of any element.

## Why It Matters
Fundamental augmentation technique demonstrating how extra metadata transforms BST capabilities.

## QnA Seeds
- Q: What is augmented in an order-statistic tree? -> A: Subtree size at each node.
- Q: How to find kth element? -> A: Compare k with left subtree size to decide going left, returning current, or going right.
