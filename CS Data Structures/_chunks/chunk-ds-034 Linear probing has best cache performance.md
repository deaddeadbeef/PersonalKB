---
tags: [cs-ds, chunk]
id: chunk-ds-034
source: "[[raw-ds-028]]"
supports: ["[[Collision Resolution Strategies]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Linear probing has best cache performance among open addressing schemes

## Context
Open addressing variants differ in probe patterns.

## Claim
Linear probing accesses sequential memory locations, maximizing CPU cache line utilization and prefetching effectiveness, often outperforming theoretically superior schemes like double hashing in practice.

## Why It Matters
Cache effects dominate on modern hardware — the simplest scheme wins despite primary clustering.

## QnA Seeds
- Q: Why does linear probing have good cache behavior? -> A: Sequential access hits same cache line.
- Q: What is primary clustering? -> A: Long runs of occupied slots that grow when they merge.
