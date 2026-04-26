---
id: chunk-csos-040
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 8"
topic: "multiprocessor"
claim: "Cache coherence protocols (MESI) ensure all CPU cores see a consistent view of shared memory by tracking cache line states and invalidating stale copies on write"
confidence: verified
supports:
  - "[[Multiprocessor Systems]]"
tags:
  - csos
  - csos/multiprocessor
  - chunk
up: "[[CS Operating Systems]]"
---
# Multiprocessor — Cache coherence protocols prevent stale reads across cores in a shared-memory system

## Context

Each CPU core has L1/L2 caches. Without a coherence protocol, core A could hold a cached copy of address X = 5, while core B writes X = 7 to its cache — core A continues to see the stale value 5. MESI (Modified, Exclusive, Shared, Invalid) solves this with a state machine per cache line: when core B writes a Shared line, it broadcasts an invalidation; other cores must fetch the new value before their next read. Modern CPUs use point-to-point directory-based protocols (Intel QPI/UPI, AMD Infinity Fabric) to scale this to many cores.

## Why It Matters

Cache coherence is transparent to programmers but its implications are not: coherence traffic (invalidation messages) limits scalability, and false sharing (two threads accessing different variables in the same 64-byte cache line) causes unnecessary coherence traffic and performance collapse. Padding structs to cache-line boundaries is a standard performance technique in high-performance OS and database code.

## QnA Seeds

- Q: What does "Modified" mean in the MESI cache coherence protocol?
- Q: What is false sharing and how can it be avoided?
- Q: Why does cache coherence traffic limit multiprocessor scalability?
