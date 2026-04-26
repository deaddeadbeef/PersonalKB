---
tags: [cs-ds, chunk]
id: chunk-ds-031
source: "[[raw-ds-026]]"
supports: ["[[Advanced Structures Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Interval trees find overlapping intervals in Ologn plus k

## Context
Scheduling and geometry problems require finding all intervals overlapping a query.

## Claim
An interval tree augments a BST with max-endpoint per subtree, enabling O(log n) search for any overlapping interval and O(log n + k) for all k overlapping intervals.

## Why It Matters
Core structure for calendar scheduling, computational geometry, and database range predicates.

## QnA Seeds
- Q: What is the augmentation? -> A: Each node stores the maximum endpoint in its subtree.
- Q: How does search work? -> A: If left max >= query.lo, search left; otherwise search right.
