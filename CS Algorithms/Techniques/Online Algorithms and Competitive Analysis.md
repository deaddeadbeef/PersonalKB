---
tags: [cs-algorithms, techniques, online-algorithms]
up: "[[Techniques Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, practice]
---

# Online Algorithms and Competitive Analysis

> **One-line summary** Online algorithms make decisions before seeing the full input; competitive analysis compares them with an optimal offline algorithm that sees the future.

## Intuition

Many systems must act immediately: a cache must evict an item before seeing future requests, a scheduler must choose work before knowing future arrivals, and a network service must route traffic before knowing the rest of the day. Online algorithms study this constraint directly.

Competitive analysis asks: how much worse can the online algorithm be than an ideal offline algorithm? If an algorithm is 2-competitive, its cost is at most twice the optimal offline cost, up to lower-order constants.

## Core Patterns

- **Cache eviction:** LRU and LFU choose what to evict without knowing future accesses.
- **Paging:** online algorithms manage limited fast memory against an unknown request stream.
- **Scheduling:** jobs arrive over time and must be assigned before future jobs are known.
- **Admission control:** systems accept or reject work under unknown future load.

## Why It Matters

Online analysis explains why practical heuristics such as LRU can be defensible even without perfect prediction. It also sets expectations: some problems cannot be solved well online without extra assumptions, randomization, or advice.

## Practice

1. Explain why cache replacement is an online problem.
2. Compare LRU with an offline optimal cache replacement policy.
3. Describe what a competitive ratio measures.

## References

- [[CS Data Structures/Advanced Structures/LRU and LFU Caches]]
- [[CS Algorithms/Techniques/Randomized Algorithms]]
- [[CS Algorithms/Sources/Sources Index]]
