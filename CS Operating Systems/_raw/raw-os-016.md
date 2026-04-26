---
tags: [cs-os, raw]
source_type: textbook_chapter
source_title: "Multiprocessor and SMP Systems"
authors: "Andrew S. Tanenbaum, Herbert Bos"
year: 2015
---

# Multiprocessor and SMP Systems

## Summary
Symmetric multiprocessing (SMP) systems contain multiple identical processors sharing a single physical memory through a common bus or interconnect, with each processor running the same OS kernel and capable of executing any process. The fundamental challenge of SMP is maintaining cache coherence—ensuring that all processors see a consistent view of memory despite having private caches. NUMA architectures, processor affinity, and specialized synchronization primitives like spinlocks address the performance implications of shared-memory multiprocessing.

## Key Claims
- In SMP systems, all processors are equal peers with identical access to memory and I/O devices; the OS runs on all processors simultaneously, requiring all kernel data structures to be protected against concurrent access—this is fundamentally harder than single-processor kernel design
- Cache coherence protocols (primarily MESI on x86) ensure that when one processor writes to a cached memory location, all other processors' caches either invalidate or update their copies—without this hardware guarantee, shared-memory programming would be intractable
- Spinlocks are the appropriate synchronization primitive for short critical sections on multiprocessors because the cost of spinning (busy-waiting) for a few microseconds is less than the overhead of context-switching to another thread and back; on uniprocessors, spinlocks are replaced with interrupt disabling
- NUMA (Non-Uniform Memory Access) architectures physically distribute memory across processor nodes, making local memory access 2–10x faster than remote access; NUMA-aware memory allocation (placing data near the accessing processor) is critical for scalability beyond 4–8 cores
- Processor affinity binds a process or thread to specific CPUs, preserving warm caches and avoiding the performance penalty of migration; Linux supports both soft affinity (scheduler preference) and hard affinity (strict binding via sched_setaffinity or taskset)

## Atomic Facts
1. The MESI protocol defines four cache line states: Modified (dirty, exclusive—must write back before others can read), Exclusive (clean, only copy), Shared (clean, multiple copies may exist), and Invalid (stale—must be re-fetched); state transitions are triggered by local and remote read/write operations
2. Linux transitioned from a Big Kernel Lock (BKL, a single global spinlock protecting the entire kernel) to fine-grained per-subsystem locking between kernel versions 2.4 and 2.6; BKL was finally removed entirely in kernel 3.0 (2011)
3. Read-Copy-Update (RCU) is a Linux kernel synchronization mechanism optimized for read-heavy workloads: readers proceed without locks, writers create modified copies and atomically swap pointers, and old versions are reclaimed after all pre-existing readers complete—this achieves zero-overhead reads
4. On a NUMA system, a memory access to the local node typically takes 50–100ns, while a remote access takes 100–300ns; the Linux NUMA balancing feature (AutoNUMA) automatically migrates pages to the node where they are most frequently accessed
5. Gang scheduling ensures that all threads of a parallel application are scheduled simultaneously across processors, preventing the situation where one thread holds a lock while being descheduled—which would cause all other threads spinning on that lock to waste their time slices
6. Load balancing on SMP systems moves processes between processor run queues to equalize utilization; Linux performs this via periodic rebalancing and idle balancing (when a CPU's run queue is empty, it steals work from the busiest CPU's queue)

## Significance
Multiprocessor systems are the dominant computing architecture of the modern era—from dual-core smartphones to 128-core servers. Understanding SMP principles explains why simply adding more cores doesn't linearly increase performance (Amdahl's Law, cache coherence overhead, lock contention), and why software architecture must be NUMA-aware and concurrency-aware to scale effectively on modern hardware.

## Chunks Extracted
- [[chunk-os-111 SMP Requires Concurrent Protection of All Kernel Structures]]
- [[chunk-os-112 MESI Protocol Maintains Cache Coherence Across Caches]]
- [[chunk-os-113 RCU Achieves Zero-Overhead Reads for Kernel Data]]
- [[chunk-os-114 NUMA-Aware Allocation Critical for Multi-Core Scalability]]
