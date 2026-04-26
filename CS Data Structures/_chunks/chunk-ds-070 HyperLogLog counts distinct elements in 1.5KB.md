---
tags: [cs-ds, chunk]
id: chunk-ds-070
source: "[[raw-ds-009]]"
supports: ["[[Bloom Filters and Probabilistic Structures]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# HyperLogLog counts distinct elements in 1.5KB with 2pct error

## Context
Exact cardinality counting requires O(n) space.

## Claim
HyperLogLog estimates the number of distinct elements using only 1.5KB of memory with roughly 2 percent standard error by observing the maximum number of leading zeros in hashed values across 2^10 registers.

## Why It Matters
Used in Redis, BigQuery, and Presto for approximate COUNT DISTINCT on billions of rows.

## QnA Seeds
- Q: Why leading zeros? -> A: Seeing k leading zeros suggests roughly 2^k distinct elements.
- Q: Why multiple registers? -> A: Reduces variance by splitting elements across 2^p buckets and averaging.
