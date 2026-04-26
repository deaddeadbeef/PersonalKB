---
tags: [cs-ds, chunk]
id: chunk-ds-144
source: "[[raw-ds-013]]"
supports: ["[[Segment Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Iterative segment tree uses 2n array for better cache performance

## Context
Recursive segment trees use 4n array with significant overhead.

## Claim
Iterative (bottom-up) segment tree stores leaves in positions n to 2n-1 and internal nodes in 1 to n-1. Updates and queries traverse from leaf to root via index/2 with excellent cache locality and lower constant factors.

## Why It Matters
Preferred in competitive programming for speed. Up to 2x faster than recursive version.

## QnA Seeds
- Q: How to query range [l,r]? -> A: Start at l+n and r+n. Move both upward collecting results at boundaries.
- Q: Why 2n vs 4n? -> A: Iterative packs leaves contiguously. Recursive may leave gaps needing 4n to be safe.
