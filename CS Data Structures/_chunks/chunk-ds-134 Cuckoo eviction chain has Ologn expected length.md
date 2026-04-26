---
tags: [cs-ds, chunk]
id: chunk-ds-134
source: "[[raw-ds-036]]"
supports: ["[[Cuckoo Hashing]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Cuckoo hash eviction chain has O(log n) expected length

## Context
Insertion into occupied slot triggers displacement chain.

## Claim
The expected eviction chain length during cuckoo insertion is O(log n) with load factor below 50 percent. Chains exceeding O(log n) threshold trigger a full rehash with new hash functions.

## Why It Matters
Understanding chain length is key to proving expected O(1) amortized insertion complexity.

## QnA Seeds
- Q: What triggers full rehash? -> A: Eviction chain exceeding threshold (typically 6 log n) indicating a cycle.
- Q: How often does rehash happen? -> A: Expected O(1/n) probability per insertion at reasonable load factors.
