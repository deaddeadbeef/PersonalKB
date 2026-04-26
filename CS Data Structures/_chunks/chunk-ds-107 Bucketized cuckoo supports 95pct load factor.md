---
tags: [cs-ds, chunk]
id: chunk-ds-107
source: "[[raw-ds-036]]"
supports: ["[[Cuckoo Hashing]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Bucketized cuckoo hashing supports 95pct load factor with bucket size 4

## Context
Standard cuckoo hashing fails above 50 percent load factor per table.

## Claim
Using buckets of size 4 instead of single slots allows load factors up to 95 percent while maintaining O(1) worst-case lookup by checking at most 2 buckets of 4 entries each.

## Why It Matters
MemC3 and other high-performance systems use bucketized cuckoo for near-perfect space utilization.

## QnA Seeds
- Q: Why bucket size 4? -> A: Fits in a cache line and achieves 95 percent occupancy.
- Q: Does worst-case lookup change? -> A: Still O(1) just checking 2 buckets of 4 entries = 8 comparisons max.
