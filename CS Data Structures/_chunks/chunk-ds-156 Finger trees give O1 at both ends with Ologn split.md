---
tags: [cs-ds, chunk]
id: chunk-ds-156
source: "[[raw-ds-024]]"
supports: ["[[Advanced Structures Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Finger trees give O1 amortized at both ends with Ologn split

## Context
Deques give O(1) at ends but O(n) split. Balanced BSTs give O(log n) for everything.

## Claim
Finger trees achieve O(1) amortized prepend and append, O(log n) split and concatenation, and O(log n) indexed access by maintaining fingers (cached endpoints) on a 2-3 tree spine.

## Why It Matters
Default sequence type in Haskell (Data.Sequence). Optimal general-purpose persistent sequence.

## QnA Seeds
- Q: What is a finger? -> A: Direct reference to the leftmost and rightmost elements enabling O(1) access.
- Q: Why 2-3 tree spine? -> A: Guarantees O(log n) depth with flexibility for efficient restructuring.
