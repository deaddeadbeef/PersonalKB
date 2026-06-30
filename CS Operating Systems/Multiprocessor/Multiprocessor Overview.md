---
tags:
  - csos
  - moc
up: "[[CS Operating Systems]]"
confidence: verified
---
# Multiprocessor Overview

Modern machines have multiple CPUs sharing memory or connected via interconnects. This domain covers symmetric multiprocessing (SMP), non-uniform memory access (NUMA), cache coherence, multiprocessor scheduling, and the principles of distributed systems that emerge when shared memory is removed entirely.

---

## Learn in This Order

1. [[Multiprocessor Systems]] — SMP vs NUMA; cache coherence protocols; spinlocks; scheduler affinity; gang scheduling
2. [[Distributed Systems Overview]] — message-passing model; consistency; fault tolerance; CAP theorem intuition

---

## In This Domain

| Page | One-line summary |
|------|-----------------|
| [[Multiprocessor Systems]] | SMP/NUMA; cache coherence; multiprocessor scheduling; affinity |
| [[Distributed Systems Overview]] | Message-passing; consistency models; fault tolerance |

---

## Common Distinctions

| Question | Answer |
|----------|--------|
| SMP vs NUMA? | SMP = all CPUs have uniform access to shared RAM. NUMA = CPUs have fast local memory and slower remote memory. NUMA awareness critical for performance at scale. |
| Cache coherence vs memory consistency? | Cache coherence = all CPUs see the same value for one memory location. Memory consistency = ordering guarantees across multiple locations — a weaker, harder problem. |
| Tightly coupled vs loosely coupled? | Tightly coupled = shared memory (SMP/NUMA). Loosely coupled = separate address spaces communicating by message (distributed systems). |

---

## How to Navigate

- **Shared-memory multiprocessors?** [[Multiprocessor Systems]] covers hardware and scheduling.
- **Distributed / networked systems?** [[Distributed Systems Overview]]
- **Performance tuning?** Scheduler affinity, NUMA placement, and cache coherence are all in [[Multiprocessor Systems]].

---

## Related Domains

- **[[Synchronization Overview]]** — spinlocks and lock-free data structures are the multiprocessor extensions of single-CPU synchronization.
- **[[Virtualization Overview]]** — cloud VMs run on NUMA hosts; hypervisor scheduling must be NUMA-aware.
- **[[Processes Overview]]** — process/thread scheduling on a uniprocessor is the foundation that multiprocessor scheduling extends.

## References
- [[CS Operating Systems/Sources/Sources Index|CS Operating Systems Sources Index]]
