---
tags: [cs-ds, chunk]
id: chunk-ds-052
source: "[[raw-ds-037]]"
supports: ["[[Advanced Structures Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Van Emde Boas trees achieve O log log u for integer predecessor

## Context
BSTs give O(log n) predecessor queries; can we do better for integer keys?

## Claim
Van Emde Boas trees recursively divide the universe of size u into sqrt(u) clusters, achieving O(log log u) for insert, delete, predecessor, and successor — doubly logarithmic.

## Why It Matters
Breaks the comparison-based O(log n) barrier for integer keys. For 32-bit integers: only 5 operations.

## QnA Seeds
- Q: Why O(log log u)? -> A: Each recursion takes square root of universe, halving the log each time.
- Q: Main drawback? -> A: O(u) space — wasteful for sparse sets.
