---
id: chunk-csos-039
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 8"
topic: "multiprocessor"
claim: "SMP gives all CPUs equal access to a shared memory bus (uniform latency); NUMA gives each CPU local memory (fast) and remote memory (slow), requiring NUMA-aware OS allocation and scheduling"
confidence: verified
supports:
  - "[[Multiprocessor Systems]]"
tags:
  - csos
  - csos/multiprocessor
  - chunk
up: "[[CS Operating Systems]]"
---
# Multiprocessor — SMP and NUMA differ in memory access latency uniformity across cores

## Context

Symmetric Multiprocessing (SMP): all CPUs share a single memory bus. Memory access latency is the same for all CPUs. Simple OS memory allocator works correctly. Bottleneck: memory bus contention limits scalability beyond ~16–32 cores. NUMA (Non-Uniform Memory Access): each CPU socket has local RAM; remote RAM is accessible but ~2–5× slower. Modern server CPUs (AMD EPYC, Intel Xeon multi-socket) are NUMA. The OS must allocate memory from the node local to the running CPU (numactl, NUMA-aware allocator) to avoid cross-node latency penalties.

## Why It Matters

NUMA awareness is a real production concern. A database or JVM that allocates memory on a remote NUMA node suffers measurable latency penalties. Linux's NUMA balancing (CONFIG_NUMA_BALANCING) attempts to automatically migrate hot pages to local nodes. Container orchestration (Kubernetes CPU/NUMA pinning) exposes NUMA topology to workload schedulers.

## QnA Seeds

- Q: What is the key performance difference between SMP and NUMA?
- Q: How should an OS allocate memory on a NUMA system?
- Q: Why does SMP not scale beyond ~16–32 cores?
