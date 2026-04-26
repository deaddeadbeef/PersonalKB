---
tags: [cs-ds, chunk]
id: chunk-ds-026
source: "[[raw-ds-024]]"
supports: ["[[Advanced Structures Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Path copying makes BSTs persistent with O log n overhead per update

## Context
Persistent data structures preserve all previous versions.

## Claim
Path copying duplicates only the O(log n) nodes from root to changed node, sharing all other subtrees between versions, giving O(log n) time and space per update.

## Why It Matters
Foundation for persistent data structures in functional programming and version-control systems like Git.

## QnA Seeds
- Q: Why only O(log n) nodes copied? -> A: Only ancestors of the modified node change; siblings are shared.
- Q: What is structural sharing? -> A: Unchanged subtrees are referenced by both old and new versions.
