---
tags: [cs-ds, chunk]
id: chunk-ds-058
source: "[[raw-ds-040]]"
supports: ["[[Foundational Concepts Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Succinct bit vectors answer rank and select in O1 with sublinear overhead

## Context
Rank counts 1s up to position i and select finds jth 1 as fundamental operations.

## Claim
Succinct bit vectors store n bits plus o(n) extra bits and answer both rank and select queries in O(1) time using two-level lookup tables.

## Why It Matters
Building block for all succinct structures including FM-index wavelet trees and compressed representations.

## QnA Seeds
- Q: What is rank(i)? -> A: Count of 1-bits in positions 0 through i.
- Q: How is O(1) achieved? -> A: Two-level table with superblocks and blocks with precomputed popcount.
