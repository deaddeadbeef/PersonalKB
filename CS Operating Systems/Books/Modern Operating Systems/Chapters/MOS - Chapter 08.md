---
id: mos-ch-08
type: book-chapter
chapter: 8
book: "Modern Operating Systems"
author: "Andrew S. Tanenbaum"
status: seeded
chunk_count: 4
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
tags:
  - csos
  - book-chapter
up: "[[Chapter Index]]"
confidence: verified
---
# MOS — Chapter 08: Multiple Processor Systems

## Summary

As clock speeds plateaued, hardware moved to multicore and multi-socket designs. This chapter covers three multiprocessor architectures: UMA (uniform memory access, classic SMP), NUMA (non-uniform; local memory is faster), and clusters. Cache coherence is the central problem — ensuring that all cores see a consistent view of shared memory — solved by protocols such as MSI and MESI. OS-level concerns include scheduler affinity (keeping a thread on the same core to exploit warm caches), spin lock vs blocking lock trade-offs, and the dangers of false sharing in cache lines. The chapter then surveys distributed systems: loosely coupled nodes communicating by message passing, with their own challenges around naming, consistency, and fault tolerance. Distributed file systems and middleware are briefly introduced.

## Key Concepts

| Concept | One-liner |
|---------|-----------|
| SMP | Symmetric multiprocessing: all CPUs share a single memory bus |
| NUMA | Non-uniform memory access: local memory is faster than remote |
| Cache coherence | Protocol ensuring all cores see the same value for a shared location |
| MESI protocol | Cache coherence state machine: Modified, Exclusive, Shared, Invalid |
| Scheduler affinity | Preference to reschedule a thread on the core it last ran |
| False sharing | Two threads accessing different data in the same cache line cause ping-pong |

## Chunk Candidates

- [x] [[Multiprocessor - SMP and NUMA differ in memory access latency uniformity across cores]]
- [x] [[Multiprocessor - Cache coherence protocols prevent stale reads across cores in a shared-memory system]]
- [x] [[Multiprocessor - Scheduler affinity exploits warm caches by keeping threads on their last-run core]]
- [x] [[Multiprocessor - Distributed systems replace shared memory with explicit message passing]]

## Wiki Pages Seeded

- [[Multiprocessor Systems]] — SMP, NUMA, cache coherence, affinity, spin locks
- [[Distributed Systems Overview]] — message-passing model, consistency, fault tolerance

## References

See [[Sources Index#Tanenbaum 2015]].
