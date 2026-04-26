---
tags: [cs-ds, chunk]
id: chunk-ds-015
source: "[[raw-ds-011]]"
supports: ["[[Skip Lists]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Skip lists achieve O(log n) expected time with probabilistic layering

## Context
Balanced BSTs achieve O(log n) through complex rotation rules.

## Claim
Skip lists promote each element to higher layers with probability 1/2, creating O(log n) express lanes with O(n) total space.

## Why It Matters
Simpler than balanced BSTs and naturally support concurrent access -- used in Redis and LevelDB.

## QnA Seeds
- Q: Why O(log n) levels? -> A: With p=1/2, expected levels is log2(n), each level halves elements.
- Q: Why preferred for concurrent systems? -> A: Lock-free skip list algorithms are simpler than lock-free balanced tree algorithms.
