---
tags: [cs-ds, chunk]
id: chunk-ds-111
source: "[[raw-ds-001]]"
supports: ["[[Arrays and Dynamic Arrays]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Growth factor 1.5x vs 2x trades memory for copy frequency

## Context
Dynamic arrays must choose a growth factor when resizing.

## Claim
Growth factor 2x doubles capacity (Java ArrayList, C++ vector) giving amortized O(1) but up to 50 percent wasted space. Factor 1.5x (C++ MSVC, Go slices) wastes less but copies more often. Both are amortized O(1).

## Why It Matters
Practical engineering trade-off between memory efficiency and copy frequency.

## QnA Seeds
- Q: Why not growth factor 1.1x? -> A: Too many resizes. Amortized constant gets impractically large.
- Q: Why not 4x? -> A: Too much wasted space. 75 percent waste at worst.
