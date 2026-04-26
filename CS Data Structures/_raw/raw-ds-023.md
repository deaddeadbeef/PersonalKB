---
tags: [cs-ds, raw]
id: raw-ds-023
source: "The Art of Multiprocessor Programming (Herlihy and Shavit)"
up: "[[CS Data Structures]]"
---

# Concurrent Data Structures

## Key Ideas
- Lock-based: mutex/spinlock guards, simple but contention bottleneck
- Lock-free: at least one thread makes progress, no deadlock
- Wait-free: every thread completes in bounded steps
- CAS Compare-and-Swap: hardware primitive enabling lock-free algorithms
- ABA problem: value reverts between CAS checks, solved by version counters
- Lock-free stack Treiber: CAS on head pointer
- Lock-free queue Michael-Scott: CAS on head and tail
- Concurrent skip list: naturally supports lock-free operations
- Concurrent hash map: lock striping or split-ordered lists
- Read-Copy-Update RCU: readers no locks, writers create new version
- Hazard pointers: safe memory reclamation for lock-free structures
