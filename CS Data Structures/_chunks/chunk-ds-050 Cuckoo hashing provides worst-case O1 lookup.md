---
tags: [cs-ds, chunk]
id: chunk-ds-050
source: "[[raw-ds-036]]"
supports: ["[[Cuckoo Hashing]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Cuckoo hashing provides worst-case O1 lookup with two hash functions

## Context
Standard hash tables only guarantee expected O(1), with worst-case O(n).

## Claim
Cuckoo hashing uses two hash functions and two tables; an element is always in one of two positions, giving guaranteed O(1) worst-case lookup by checking exactly two locations.

## Why It Matters
Critical for hardware implementations (network routers) where worst-case latency matters.

## QnA Seeds
- Q: Why worst-case O(1)? -> A: Element is at T1[h1(k)] or T2[h2(k)] — always exactly 2 probes.
- Q: What about insertion? -> A: Expected O(1) amortized, but may trigger eviction chain or full rehash.
