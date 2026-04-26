---
tags: [cs-ds, chunk]
id: chunk-ds-077
source: "[[raw-ds-016]]"
supports: ["[[Binary Search Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Splay trees achieve Ologn amortized via move-to-root splaying

## Context
Balanced BSTs use rotations to maintain height bounds.

## Claim
Splay trees rotate every accessed node to the root using zig, zig-zig, and zig-zag cases. This gives O(log n) amortized for all operations and the working set property where frequently accessed items are near the root.

## Why It Matters
Self-optimizing for access patterns. No balance metadata needed. Used in Windows NT and some cache implementations.

## QnA Seeds
- Q: What is the working set property? -> A: If k distinct items accessed since last access of x then accessing x costs O(log k).
- Q: Why amortized not worst-case? -> A: Single access can cost O(n) but restructuring makes future accesses cheaper.
