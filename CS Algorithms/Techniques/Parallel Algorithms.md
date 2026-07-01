---
tags: [cs-algorithms, techniques, parallelism]
up: "[[Techniques Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, practice]
---

# Parallel Algorithms

> **One-line summary** Parallel algorithms divide work across processors while managing dependence, synchronization, communication, and load balance.

## Intuition

Parallelism helps only when the work can be split without creating more coordination cost than useful computation. A good parallel algorithm identifies independent subproblems, keeps processors busy, and reduces communication or synchronization bottlenecks.

Two measures matter: **work**, the total amount of computation, and **span**, the length of the longest dependency chain. If span is large, adding processors cannot help much because some steps must happen sequentially.

## Core Patterns

- **Divide and conquer:** split independent subproblems, solve in parallel, then combine.
- **Parallel reduction:** combine many values through a tree-shaped aggregation.
- **Map/filter style data parallelism:** apply the same operation across many records.
- **Graph parallelism:** process frontier sets or independent components.
- **Work stealing:** dynamically balance uneven recursive work across worker threads.

## Why It Matters

Modern hardware is parallel by default: multicore CPUs, SIMD units, GPUs, and distributed systems all reward algorithms that expose independent work. Parallel thinking also clarifies why some data structures are hard to make concurrent: contention and shared mutable state can erase theoretical speedups.

## Practice

1. Define work and span for a parallel sum over an array.
2. Explain why synchronization can make a parallel algorithm slower than a sequential one.
3. Compare parallel merge sort with ordinary merge sort in terms of available independent work.

## References

- [[CS Algorithms/Divide and Conquer/Divide and Conquer Overview]]
- [[CS Data Structures/Advanced Structures/Concurrent Data Structures]]
- [[CS Operating Systems/Multiprocessor/Multiprocessor Overview]]
