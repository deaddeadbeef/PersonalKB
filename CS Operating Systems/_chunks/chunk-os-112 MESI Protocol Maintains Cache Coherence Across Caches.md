---
id: chunk-csos-112
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 8 — Multiprocessor and SMP Systems"
topic: "multiprocessor"
claim: "The MESI cache coherence protocol defines four states (Modified, Exclusive, Shared, Invalid) for each cache line, ensuring all processors see consistent memory despite private caches — without this hardware guarantee, shared-memory programming would be intractable"
confidence: verified
supports:
  - "[[Multiprocessor Systems]]"
tags:
  - csos
  - csos/multiprocessor
  - chunk
up: "[[CS Operating Systems]]"
---
# Multiprocessor — MESI protocol maintains cache coherence across processor caches

## Context

Each processor in an SMP system has private L1/L2 caches for performance. Without coherence, processor A could cache a stale value of variable X while processor B has written a new value — violating the shared-memory programming model. The MESI protocol (standard on x86) tracks each cache line in one of four states: Modified (dirty, exclusive — must write back before others read), Exclusive (clean, only copy), Shared (clean, multiple copies may exist), Invalid (stale — must re-fetch). State transitions are triggered by local and remote read/write operations via bus snooping or directory-based protocols.

## Why It Matters

MESI is the invisible hardware foundation making multithreaded programming possible on modern CPUs. Every mutex, atomic variable, and lock-free data structure relies on the hardware delivering coherent memory. Understanding MESI also explains performance phenomena like false sharing — two unrelated variables on the same cache line cause constant invalidation bouncing between cores.

## QnA Seeds

- Q: What are the four MESI states and what does each mean?
- Q: What would happen if cache coherence were not maintained by hardware?
- Q: How does MESI relate to the false sharing performance problem?
