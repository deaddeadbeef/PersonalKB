---
id: chunk-csos-114
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 8 — Multiprocessor and SMP Systems"
topic: "multiprocessor"
claim: "NUMA architectures physically distribute memory across processor nodes, making local access 2–10× faster than remote access; NUMA-aware allocation and Linux AutoNUMA page migration are critical for scalability beyond 4–8 cores"
confidence: verified
supports:
  - "[[Multiprocessor Systems]]"
  - "[[Multiprocessor Overview]]"
tags:
  - csos
  - csos/multiprocessor
  - chunk
up: "[[CS Operating Systems]]"
---
# Multiprocessor — NUMA-aware allocation is critical for scalability beyond 4-8 cores

## Context

NUMA (Non-Uniform Memory Access) architectures physically attach memory to specific processor nodes. Local memory access typically takes 50–100ns while remote access (to another node's memory) takes 100–300ns — a 2–10× penalty. On systems with 8+ cores, a NUMA-unaware allocator that spreads data across nodes can devastate performance. Linux's NUMA balancing (AutoNUMA) automatically migrates pages to the node where they are most frequently accessed. Processor affinity — binding threads to specific CPUs via sched_setaffinity() or taskset — preserves warm caches and avoids cross-node migration penalties.

## Why It Matters

NUMA awareness explains why "just add more cores" doesn't linearly improve performance. A 64-core server with NUMA-unaware software may perform worse than a 16-core system running NUMA-optimized code. Database systems (PostgreSQL, MySQL) and JVMs include explicit NUMA-aware memory allocation for this reason.

## QnA Seeds

- Q: What makes memory access "non-uniform" in NUMA systems?
- Q: What is the typical latency difference between local and remote NUMA access?
- Q: How does Linux AutoNUMA decide which pages to migrate?
