---
tags: [cs-ds, concurrency]
up: "[[Advanced Structures Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Concurrent Data Structures

> **One-line summary**: Thread-safe data structures designed for simultaneous access by multiple threads, ranging from coarse-grained locking to lock-free and wait-free designs that guarantee progress without mutual exclusion.

## 🎯 Intuition
**The Core Idea:** Multiple threads need to read and write shared data without corrupting it. Concurrent data structures provide correctness guarantees (linearizability, serializability) while maximizing parallelism.
**Analogy:** A shared whiteboard in an office: with a single lock, only one person can write at a time (coarse-grained locking). With fine-grained locking, different people can write in different sections simultaneously. Lock-free is like a revolving door — everyone keeps moving; nobody blocks anyone, though some may need to retry their step.
**Why It Matters:** Modern CPUs have 16-128+ cores. Sequential data structures become bottlenecks. High-performance servers, databases, and real-time systems require data structures that scale with core count.

---

## ⚙️ Core Mechanics
### How It Works

**Locking strategies (weakest to strongest progress guarantee):**

1. **Coarse-grained locking**: one mutex protects the entire structure. Simple but serializes all access.
2. **Fine-grained locking**: multiple locks protect different regions (e.g., per-bucket in a hash map, per-node in a linked list). More parallelism but risk of deadlock.
3. **Lock-free**: at least one thread makes progress in a finite number of steps. Uses atomic operations (CAS — Compare-And-Swap) instead of locks.
4. **Wait-free**: every thread completes in a bounded number of steps. Strongest guarantee but hardest to implement.

**CAS (Compare-And-Swap) — the primitive:**
```
CAS(addr, expected, desired):
  atomically: if *addr == expected: *addr = desired; return true
              else: return false
```
CAS is the building block of nearly all lock-free algorithms.

**Common concurrent structures:**
- **ConcurrentHashMap**: partitioned buckets with per-segment locks (Java) or lock-free with CAS (Java 8+).
- **Michael-Scott Queue**: a lock-free FIFO queue using CAS on head/tail pointers.
- **Harris Linked List**: a lock-free sorted linked list using marked pointers for logical deletion.
- **Skip List (concurrent)**: lock-free or fine-grained locking; used in Java's `ConcurrentSkipListMap`.

### Key Operations

| Structure | Insert | Delete | Search | Progress |
|-----------|--------|--------|--------|----------|
| Coarse-grained list | $O(n)$ | $O(n)$ | $O(n)$ | Blocking |
| Fine-grained list | $O(n)$ | $O(n)$ | $O(n)$ | Deadlock-free |
| Lock-free list (Harris) | $O(n)$ | $O(n)$ | $O(n)$ | Lock-free |
| Lock-free queue (M-S) | $O(1)$ | $O(1)$ | — | Lock-free |
| ConcurrentHashMap | $O(1)$ avg | $O(1)$ avg | $O(1)$ avg | Lock-free (Java 8+) |
| Concurrent skip list | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | Lock-free |

### Key Facts
- **Linearizability** is the gold standard: every operation appears to take effect at a single instant between its invocation and response.
- **Lock-free ≠ wait-free**: lock-free guarantees system-wide progress; individual threads can starve. Wait-free guarantees per-thread progress.
- **Memory reclamation** is the hardest part of lock-free programming: you can't free a node while another thread might be reading it. Solutions: hazard pointers, epoch-based reclamation (EBR), RCU.
- **False sharing**: when threads modify variables on the same cache line, causing expensive cache coherence traffic. Pad structures to cache-line boundaries (64 bytes).
- Modern lock-free structures rarely outperform well-designed lock-based structures under low contention. Their advantage emerges under high contention.

---

## 🔬 Deep Dive
### Formal Properties
**Linearizability (Herlihy & Wing, 1990):**
A concurrent execution is linearizable if there exists a sequential execution of the same operations that:
1. Respects the real-time ordering of non-overlapping operations.
2. Is a valid sequential execution of the data structure.

**Consensus number (Herlihy, 1991):**
- Read/write registers: consensus number 1 (can't solve consensus for 2+ threads).
- CAS: consensus number ∞ (can solve consensus for any number of threads).
- This is why CAS is universal — any sequential data structure can be made lock-free using CAS (universal construction).

**ABA problem:** A CAS might succeed spuriously if a value changes from A→B→A between the read and the CAS. Thread thinks nothing changed, but the state is different. Solutions: tagged/versioned pointers (use upper bits as a counter), hazard pointers, or DCAS.

**Memory ordering:**
- Sequential consistency is intuitive but expensive.
- Relaxed memory models (x86-TSO, ARM/POWER) allow reorderings. Use memory fences (`std::atomic` with appropriate `memory_order` in C++).
- `memory_order_acquire` / `memory_order_release` is the minimum for most lock-free algorithms.

### Edge Cases and Pitfalls
- **ABA problem**: classic trap with CAS on pointers. Use 128-bit CAS (pointer + counter) or hazard pointers.
- **Memory reclamation bugs**: freeing a node while another thread holds a reference → use-after-free. Extremely hard to debug (intermittent crashes).
- **Livelock**: two threads repeatedly invalidate each other's CAS, making no progress. Add exponential backoff.
- **Priority inversion**: with locks, a low-priority thread holding a lock blocks a high-priority thread. Lock-free avoids this.
- **Testing difficulty**: concurrent bugs are non-deterministic. Use tools like ThreadSanitizer, Relacy Race Detector, or CHESS (systematic concurrency testing).

### Real-World Usage
- **Java**: `ConcurrentHashMap`, `ConcurrentSkipListMap`, `ConcurrentLinkedQueue`, `AtomicReference` — all in `java.util.concurrent`.
- **C++**: `std::atomic`, lock-free queues in Folly (Facebook), libcds (concurrent data structure library).
- **Go**: `sync.Map` for read-heavy concurrent maps.
- **Databases**: concurrent B-trees (Bw-tree in SQL Server Hekaton), lock-free skip lists in MemSQL/SingleStore.
- **Linux kernel**: RCU (Read-Copy-Update) is used extensively — lock-free reads with deferred reclamation for routing tables, file system caches.
- **Game engines**: lock-free job queues for task-based parallelism.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What is the difference between lock-free and wait-free?
2. Explain the ABA problem with a concrete example involving a stack.
3. Why is memory reclamation harder in lock-free structures than in lock-based ones?

### Core Problems
1. **Lock-Free Stack (Treiber Stack)**: Implement a lock-free stack using CAS. Handle the ABA problem using a version counter. Test with multiple producer/consumer threads.
2. **Michael-Scott Queue**: Implement the classic lock-free queue with sentinel node. Verify linearizability by running concurrent enqueue/dequeue operations and checking that no elements are lost or duplicated.

### Challenge
Implement a **lock-free concurrent hash map** with:
- Open addressing with linear probing
- CAS-based insert and delete (use tombstone markers)
- Dynamic resizing using a "helping" mechanism (threads help complete in-progress resize)
Test with 8 threads performing mixed read/write workloads and measure throughput vs. `std::unordered_map` with a mutex.

---

*See also:* [[Lock-Free Queues and Stacks]] · [[Hash Tables and Hash Functions|Hash Tables]] · [[Skip Lists]] | **CS Algorithms:** Parallel Algorithms · Synchronization Primitives

## Supporting Chunks
- [[chunk-ds-024 Lock-free guarantees system-wide progress without deadlock]]
- [[chunk-ds-025 The ABA problem corrupts lock-free algorithms]]
- [[chunk-ds-101 RCU lets readers proceed with zero synchronization]]
- [[chunk-ds-140 Epoch-based reclamation batches memory frees]]

## References
- [[CS Data Structures/Sources/Sources Index|Sources Index]]
