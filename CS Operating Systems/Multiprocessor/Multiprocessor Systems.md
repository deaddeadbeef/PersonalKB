---
tags:
  - csos
  - csos/multiprocessor
confidence: verified
freshness: stable
up: "[[Multiprocessor Overview]]"
tier-coverage: [intuition, core, deep-dive, practice]
---
# Multiprocessor Systems

## 🎯 Intuition
**The Core Idea:** A **multiprocessor system** contains two or more CPUs (or cores) that share memory and are managed by a single OS instance. Multiprocessors improve throughput and enable parallelism but introduce complex sharing and coordination problems.

**Analogy:** Think of a kitchen with multiple chefs sharing one pantry: meals can be prepared faster, but the chefs must coordinate or they will grab the same ingredients, wait on each other, or work from stale assumptions.

**Why It Matters:** Many CPUs sharing one memory enables parallelism but creates coordination headaches. Every modern computer is a multiprocessor, so understanding SMP, NUMA, cache coherence, and scheduling is essential.

## ⚙️ Core Mechanics
### Architectures
#### UMA / SMP (Symmetric Multiprocessing)
All CPUs share a single memory bus and have equal access latency to all memory. This is the simplest model and scales to ~16–32 cores before the bus becomes a bottleneck.

#### NUMA (Non-Uniform Memory Access)
Each CPU (or CPU socket) has **local memory** — faster to access — and can access other CPUs' memory via an interconnect (e.g., AMD Infinity Fabric, Intel UPI), but with higher latency. This is common in modern multi-socket servers.

### Cache Coherence
Each core has its own L1/L2 cache. Without a protocol, core A could read a stale cached copy of a value that core B just modified.

One common coherence approach is the **MESI protocol**:

| State | Meaning |
|-------|---------|
| Modified | Only in this cache; dirty (not in memory) |
| Exclusive | Only in this cache; clean |
| Shared | In this cache and at least one other; clean |
| Invalid | Not valid; must fetch before use |

Write by core A → other caches' copies transition to Invalid → next access triggers a cache miss (cache line fetch). In MESI, if core A writes to a Shared cache line, the other copies are invalidated first.

## 🔬 Deep Dive
### NUMA-Aware Scheduling
The OS prefers to allocate memory on the node local to the CPU currently running a thread, and schedules threads on cores near their allocated memory. NUMA-aware scheduling matters because local memory is faster than remote memory.

### Scheduling Strategies on Multiprocessors
- **Gang scheduling**: run all threads of a process simultaneously on multiple cores.
- **Scheduler affinity**: prefer the last-run core to reuse warm cache data.

### False Sharing
**False sharing** happens when two threads access different variables that happen to share a cache line — writes by one invalidate the other's cache unnecessarily. A common fix is to pad structs to cache-line boundaries.

### Scaling Limits
SMP does not scale indefinitely because the shared memory bus becomes a bottleneck. That is why the simple equal-latency UMA/SMP model typically tops out around ~16–32 cores before more scalable NUMA designs become preferable.

## 🏋️ Practice
### Warm-Up
1. Define a multiprocessor system.
2. Why does UMA / SMP provide equal memory access latency to all CPUs?
3. Why does SMP typically not scale much beyond ~16–32 cores?

### Core Problems
1. Compare UMA / SMP and NUMA in terms of memory access latency, hardware organisation, and scalability.
2. In the MESI protocol, core A writes to a cache line that is currently in the **Shared** state. What state transitions occur, and why?
3. Explain why cache coherence is necessary in a shared-memory multiprocessor where each core has private L1/L2 caches.

### Challenge
1. A NUMA server shows poor performance even though CPU utilisation is low. Explain how remote memory access could cause this and how NUMA-aware scheduling helps.
2. Explain false sharing and propose a concrete fix for a data structure that causes it.
3. A workload has multiple tightly-coupled threads that frequently synchronise. When would gang scheduling help, and what trade-off might it introduce?

## Supporting Chunks

- [[Multiprocessor - SMP and NUMA differ in memory access latency uniformity across cores]]
- [[Multiprocessor - Cache coherence protocols prevent stale reads across cores in a shared-memory system]]
- [[Multiprocessor - Scheduler affinity exploits warm caches by keeping threads on their last-run core]]

## See Also

- [[Race Conditions and Mutual Exclusion]] — spin locks on multiprocessors need atomic instructions and cache-line awareness
- [[CPU Scheduling]] — gang scheduling and affinity are multiprocessor scheduling extensions
- [[Threads and Multithreading]] — threads exploit multiple cores for true parallelism
- [[Hypervisors]] — hypervisors schedule virtual CPUs across physical cores using similar affinity heuristics

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 8.
