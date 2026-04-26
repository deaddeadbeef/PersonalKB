---
tags: [cs-ds, chunk]
id: chunk-ds-060
source: "[[raw-ds-040]]"
supports: ["[[Foundational Concepts Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Wavelet trees support rank and select on any alphabet symbol in Olog sigma

## Context
Succinct bit vectors handle binary alphabets. What about larger alphabets?

## Claim
Wavelet trees recursively split the alphabet using bit vectors at each level supporting rank select and access queries on sequences over sigma-sized alphabets in O(log sigma) time.

## Why It Matters
Enables succinct representation of text permutations and grids as a core tool in compressed data structures.

## QnA Seeds
- Q: How many levels? -> A: ceil(log2 sigma) levels with one bit per character per level.
- Q: What queries beyond rank/select? -> A: Range frequency range quantile and 2D range counting.
