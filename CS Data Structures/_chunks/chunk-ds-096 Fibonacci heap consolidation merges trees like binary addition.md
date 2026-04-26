---
tags: [cs-ds, chunk]
id: chunk-ds-096
source: "[[raw-ds-017]]"
supports: ["[[Fibonacci Heaps]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Fibonacci heap consolidation merges trees like binary addition

## Context
After extract-min the root list may have many trees of various degrees.

## Claim
Consolidation scans the root list merging trees of equal degree exactly like binary addition. Each merge links the larger-root tree under the smaller. Result has at most O(log n) trees of distinct degrees.

## Why It Matters
This is the key operation making extract-min O(log n) amortized despite O(n) trees in root list.

## QnA Seeds
- Q: What triggers consolidation? -> A: Every extract-min operation.
- Q: Why at most O(log n) trees after? -> A: Each tree has unique degree bounded by O(log n).
