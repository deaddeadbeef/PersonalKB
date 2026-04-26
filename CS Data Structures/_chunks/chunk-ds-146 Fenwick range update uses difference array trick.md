---
tags: [cs-ds, chunk]
id: chunk-ds-146
source: "[[raw-ds-014]]"
supports: ["[[Fenwick Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Fenwick tree range update plus point query uses difference array trick

## Context
Standard Fenwick supports point update and prefix query.

## Claim
By operating on a difference array a Fenwick tree can support O(log n) range updates and O(log n) point queries. Adding v to range [l,r] becomes add v at l and add -v at r+1. Point query sums prefix.

## Why It Matters
Extends Fenwick tree applicability to lazy range update scenarios without full segment tree complexity.

## QnA Seeds
- Q: What is the difference array? -> A: d[i] = a[i] - a[i-1]. Prefix sum of d recovers original array.
- Q: Can we do range update AND range query? -> A: Yes with two Fenwick trees using the B*i + C identity.
