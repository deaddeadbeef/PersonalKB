---
tags:
  - csos
  - csos/synchronization
confidence: verified
freshness: stable
up: "[[Synchronization Overview]]"
tier-coverage:
  - intuition
  - core
  - deep-dive
  - practice
---
# Race Conditions and Mutual Exclusion

> **One-line summary**: A race condition occurs when concurrent threads access shared state and the outcome depends on timing — mutual exclusion primitives prevent this.

## 🎯 Intuition
**The Core Idea:** When two threads touch the same data without coordination, the result depends on who gets there first — and that's a coin flip.
**Analogy:** Two people editing the same shared Google Doc paragraph simultaneously without seeing each other's cursor — one person's edits overwrite the other's. A **mutex** is like a talking stick: only the person holding the stick can edit; everyone else waits their turn. A **critical section** is the paragraph you're editing.
**Why It Matters:** Race conditions are the #1 cause of concurrency bugs. They're intermittent, hard to reproduce, and devastating — from lost database updates to security vulnerabilities. Mutual exclusion is the fundamental defence.

---

## ⚙️ Core Mechanics
### How It Works
A **race condition** occurs when two or more threads (or processes) access shared state concurrently, and the final outcome depends on the relative timing of their accesses — making the result non-deterministic and potentially incorrect.

#### Why Races Happen
Modern systems interleave instruction streams from multiple threads at arbitrary points (preemption, multicore parallelism). A simple-looking operation like `count++` compiles to three instructions (load, increment, store). If two threads execute this concurrently, both may load the same value, increment it, and store it — losing one update.

#### Critical Section
A **critical section** is a region of code that accesses shared state and must not be executed by more than one thread at a time. A correct mutual-exclusion solution must satisfy:

1. **Mutual exclusion**: at most one thread in the critical section at any time.
2. **Progress**: if no thread is in the critical section and some want to enter, one eventually does.
3. **Bounded waiting**: no thread waits forever to enter its critical section.

### Key Concepts / Solutions

**Peterson's Algorithm (Software Solution)**
Uses two shared variables (`flag[2]` and `turn`) to give each of two threads a turn. Correct but not portable — modern CPUs reorder instructions and need memory barriers.

**Hardware Primitives**
- **Disable interrupts**: works on uniprocessors; not scalable to multiprocessors.
- **Test-And-Set (TSL / XCHG)**: atomic read-modify-write; builds spin locks.
- **Compare-And-Swap (CAS)**: atomically compare a location and swap if equal; basis of lock-free data structures.

#### Busy-Waiting vs Blocking

| Approach | Mechanism | Best For | Weakness |
|----------|-----------|----------|----------|
| Spin locks (busy-waiting) | Thread loops testing the lock | Short critical sections on multiprocessors | Wastes CPU for long waits |
| Blocking locks | Thread sleeps; OS wakes on release | Long critical sections | System-call overhead |

### Key Facts
- `count++` is NOT atomic — it compiles to load-increment-store (three instructions).
- A correct mutual-exclusion solution must provide: mutual exclusion, progress, and bounded waiting.
- Peterson's algorithm is correct for two threads but requires memory barriers on modern hardware.
- CAS is the building block of most modern lock-free data structures.
- Spin locks are preferred for short critical sections on multiprocessors; blocking locks for long ones.

---

## 🔬 Deep Dive
### Implementation Details
- **x86 atomic instructions**: `LOCK XCHG` (test-and-set), `LOCK CMPXCHG` (CAS), `LOCK XADD` (fetch-and-add). The `LOCK` prefix locks the cache line, ensuring atomicity across cores. These are the hardware foundation of all synchronisation on x86.
- **Linux futex (Fast User-space muTEX)**: In the uncontended case, a mutex is just an atomic CAS in user space (no syscall). Only when contention occurs does the thread call `futex(FUTEX_WAIT)` to sleep in the kernel. On unlock, `futex(FUTEX_WAKE)` wakes one waiter. This gives near-zero overhead for uncontended locks.
- **Ticket locks**: A spin lock variant using two counters (next_ticket, now_serving). Guarantees FIFO ordering — no starvation. Used in the Linux kernel before MCS locks.
- **MCS locks**: Each thread spins on its own cache line (not a shared variable), eliminating cache-line bouncing on multiprocessors. $O(1)$ space per lock, FIFO fair. Linux uses qspinlock (a compressed MCS variant) since kernel 4.2.

### Edge Cases and Pitfalls
- **The ABA problem (CAS)**: CAS checks "is the value still A?" But another thread may have changed it from A→B→A. CAS succeeds, but the state has changed. Solution: use a version counter (e.g., double-width CAS) or hazard pointers.
- **Memory ordering**: On weakly-ordered architectures (ARM, RISC-V), stores can become visible to other cores out of order. Locks must include memory barriers (`dmb` on ARM, `mfence` on x86) to ensure visibility.
- **Priority inversion with spin locks**: A low-priority thread holds a spin lock; a high-priority thread spins waiting for it; medium-priority threads preempt the holder → the high-priority thread starves. Solution: disable preemption while holding kernel spin locks (Linux does this).
- **Lock-free ≠ wait-free**: Lock-free guarantees system-wide progress (some thread always makes progress). Wait-free guarantees per-thread progress (every thread finishes in bounded steps). Wait-free is stronger but harder to achieve.

### Real-World Systems
- **Linux kernel**: Spin locks (qspinlock), read-write locks, RCU, seqlocks, and per-CPU variables. Mutexes use adaptive spinning: spin briefly, then sleep.
- **Windows**: Critical sections (user-mode mutexes with spin count), SRW locks (slim reader-writer locks), `InterlockedCompareExchange` for CAS.
- **Java**: `synchronized` (monitor-based), `java.util.concurrent.atomic` (CAS-based), `ReentrantLock`, `StampedLock` (optimistic reading).
- **Rust**: `Mutex<T>` wraps data — you literally cannot access the data without holding the lock (compile-time enforcement). `RwLock<T>` for readers-writers.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why is `count++` not safe to execute concurrently from two threads without a lock?
2. What are the three requirements for a correct mutual-exclusion solution?
3. When would you choose a spin lock over a blocking lock?

### Core Problems
1. **Lost update trace**: Two threads execute `count++` concurrently (initial count = 0). Show an interleaving of the load-increment-store instructions where the final value is 1 instead of 2. Then show how wrapping `count++` in a mutex (lock/unlock) prevents this interleaving.
2. **CAS-based counter**: Implement an atomic counter using Compare-And-Swap in pseudocode:
   ```
   function atomic_increment(counter):
       repeat:
           old = load(counter)
           new = old + 1
       until CAS(counter, old, new) succeeds
   ```
   Trace two threads racing on this code and show that no update is lost. What is the worst-case number of CAS retries with N threads?

### Challenge
Design a lock-free concurrent stack (Treiber stack) using CAS. Support `push(item)` and `pop() → item`. (a) Write pseudocode for both operations. (b) Prove that your implementation is linearisable. (c) Identify the ABA vulnerability in `pop()` and propose a fix using a version counter. (d) Analyse the performance: when does this lock-free stack outperform a mutex-protected stack? When does it underperform?

---

*See also:* [[Deadlock Fundamentals]] — mutual exclusion is one of the four necessary conditions for deadlock · [[Threads and Multithreading]] — threads sharing an address space are the primary source of race conditions · [[Multiprocessor Systems]] — spin locks and cache coherence affect mutual exclusion performance on SMP · [[Interprocess Communication]] — shared-memory IPC needs mutual exclusion to prevent data corruption

## Supporting Chunks

- [[Synchronization - Race conditions arise when correctness depends on interleaving order]]
- [[Synchronization - Semaphores implement mutual exclusion and signalling with P and V operations]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 2.
