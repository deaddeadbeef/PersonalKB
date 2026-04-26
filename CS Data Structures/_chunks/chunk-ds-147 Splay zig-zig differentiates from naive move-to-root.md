---
tags: [cs-ds, chunk]
id: chunk-ds-147
source: "[[raw-ds-016]]"
supports: ["[[Binary Search Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Splay tree zig-zig case is what differentiates it from move-to-root

## Context
Naive move-to-root heuristic rotates accessed node up one level at a time.

## Claim
Splay trees use zig-zig (two same-direction rotations) instead of individual rotations for grandparent case. This restructures the path globally giving O(log n) amortized. Naive move-to-root is O(n) amortized.

## Why It Matters
The zig-zig case is the key insight of Sleator and Tarjan 1985 that makes splay trees efficient.

## QnA Seeds
- Q: What is zig-zig? -> A: Node and parent are both left or both right children. Rotate parent first then node.
- Q: Why rotate parent first? -> A: Restructures path more aggressively than rotating node first. Halves path length.
