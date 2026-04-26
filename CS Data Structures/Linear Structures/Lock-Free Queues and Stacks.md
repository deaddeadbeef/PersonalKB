---
tags: [cs-ds, concurrency]
up: "[[Linear Structures Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Lock-Free Queues and Stacks

> **One-line summary**: Concurrent queue and stack implementations that use atomic compare-and-swap (CAS) operations instead of locks, guaranteeing system-wide progress even when threads are arbitrarily delayed.

## 🎯 Intuition
**The Core Idea:** Replace mutex-based critical sections with atomic CAS loops — each thread optimistically attempts its operation, and retries if another thread intervened.
**Analogy:** A lock-based queue is like a turnstile with a guard — only one person passes at a time, and if the guard falls asleep, everyone is stuck. A lock-free queue is like a revolving door — multiple people can push through simultaneously, and if one person pauses mid-push, others simply go around them. Nobody is ever blocked; at worst, they spin through again.
**Why It Matters:** Lock-free structures eliminate deadlock, priority inversion, and convoying. They're essential for real-time systems, OS kernels, high-frequency trading, and any latency-sensitive concurrent system.

---

## ⚙️ Core Mechanics
### How It Works

**Treiber Stack (Lock-Free Stack, 1986):**
- A singly linked list with a `top` pointer.
- **Push(value):** Allocate a new node. Loop: read current `top`, set `node.next = top`, CAS(`top`, expected_top, node). If CAS fails (another thread modified top), retry.
- **Pop():** Loop: read current `top`. If null, stack is empty. Read `top.next`. CAS(`top`, expected_top, top.next). If CAS fails, retry. Return the old top's value.

**Michael-Scott Queue (Lock-Free Queue, 1996):**
- A singly linked list with `head` and `tail` pointers, and a sentinel (dummy) node.
- **Enqueue(value):** Allocate new node. Loop: read `tail` and `tail.next`. If `tail.next` is null, CAS(`tail.next`, null, new_node). If CAS succeeds, advance `tail` to new_node (helping). If `tail.next` is not null, another enqueue is in progress — help by advancing `tail` and retry.
- **Dequeue():** Loop: read `head`, `tail`, and `head.next`. If `head == tail` and `head.next` is null, queue is empty. If `head == tail` and `head.next` is not null, help advance `tail`. Otherwise, read value from `head.next`, CAS(`head`, expected_head, head.next). If CAS succeeds, free old head and return value.

The **helping mechanism** is critical: if a thread stalls mid-operation, other threads complete its work, ensuring system-wide progress.

### Key Operations

| Operation | Treiber Stack | Michael-Scott Queue | Notes |
|-----------|---------------|---------------------|-------|
| Push / Enqueue | $O(1)$ expected | $O(1)$ expected | May retry under contention |
| Pop / Dequeue | $O(1)$ expected | $O(1)$ expected | May retry under contention |
| Peek | $O(1)$ | $O(1)$ | Read without modification |
| IsEmpty | $O(1)$ | $O(1)$ | Check pointer equality |
| Memory per node | pointer + data | pointer + data | Plus any reclamation metadata |

### Key Facts
- **No deadlocks**: no locks means no possibility of deadlock or priority inversion.
- **CAS contention**: under high contention, CAS retries can cause livelock-like behavior. Exponential backoff mitigates this.
- **The ABA problem** is the main pitfall: a CAS on a pointer can succeed even if the pointed-to node was freed and reallocated. Use tagged pointers (pointer + version counter) or hazard pointers.
- **Memory ordering matters**: on weakly-ordered architectures (ARM, POWER), explicit memory barriers (acquire/release) are required around CAS operations.
- **Single-producer/single-consumer (SPSC)** queues are much simpler: no CAS needed, just atomic loads/stores with acquire/release semantics. Used for inter-thread communication channels.

---

## 🔬 Deep Dive
### Formal Properties
**Progress guarantees (hierarchy):**
1. **Obstruction-free**: a thread makes progress if it runs in isolation (all others are suspended). Weakest non-blocking guarantee.
2. **Lock-free**: at least one thread makes progress in any execution. The Treiber stack and M-S queue are lock-free.
3. **Wait-free**: every thread completes in $O(f(n)$) steps regardless of other threads. Kogan-Petrank (2011) designed a wait-free queue.

**Linearizability of Michael-Scott Queue:**
Each operation has a linearization point:
- Enqueue: the successful CAS on `tail.next` (the moment the node becomes reachable).
- Dequeue: the successful CAS on `head` (the moment the old head is logically removed).

**ABA in detail:**
Thread 1: reads `top = A` (stack: A→B→C).
Thread 2: pops A, pops B, pushes A back (stack: A→C, but B is freed).
Thread 1: CAS(`top`, A, B) succeeds! But B is freed → use-after-free, corrupt stack.

**Solutions to ABA:**
- **Tagged pointers**: pair each pointer with a monotonically increasing counter. CAS on the (pointer, tag) pair. Most practical on x86-64 (128-bit CAS via `CMPXCHG16B`).
- **Hazard pointers (Michael, 2004)**: each thread publishes pointers it's currently reading. Reclamation skips any node that appears in any hazard pointer list.
- **Epoch-based reclamation (EBR)**: threads announce entry/exit from "epochs." Nodes retired in epoch E are freed when all threads have passed epoch E+2.
- **RCU (Read-Copy-Update)**: readers enter RCU read-side sections (nearly free). Writers defer freeing until all readers have exited. Used extensively in the Linux kernel.

### Edge Cases and Pitfalls
- **ABA problem**: the #1 correctness bug in lock-free code. Always use tagged pointers or safe reclamation.
- **Memory reclamation**: the hardest part. Naive `free()` after CAS causes use-after-free. Choose hazard pointers (bounded memory), EBR (simpler but unbounded under long-running readers), or RCU (read-optimized).
- **CAS spurious failure**: on some architectures (ARM LL/SC), CAS can fail even when the value matches. Always use a retry loop.
- **False sharing**: ensure head and tail pointers are on separate cache lines (`alignas(64)`). Otherwise, enqueue and dequeue contend on the same cache line even though they access different pointers.
- **Starvation under contention**: lock-free doesn't prevent individual thread starvation. If fairness matters, use wait-free algorithms or add backoff.
- **Testing**: concurrency bugs are notoriously hard to reproduce. Use stress tests with random scheduling, address sanitizers, and formal verification tools (TLA+, SPIN).

### Real-World Usage
- **Java**: `ConcurrentLinkedQueue` is a Michael-Scott queue. `ConcurrentLinkedDeque` uses a similar CAS-based design.
- **Intel TBB (Threading Building Blocks)**: provides lock-free `concurrent_queue` and `concurrent_bounded_queue`.
- **LMAX Disruptor**: a lock-free ring buffer queue used in high-frequency trading, achieving millions of operations/second with predictable latency.
- **Linux kernel**: `kfifo` (lock-free SPSC ring buffer) for kernel-to-user data transfer. RCU-based lock-free read paths throughout.
- **Tokio (Rust)**: uses lock-free work-stealing queues for its async runtime's task scheduler.
- **Go runtime**: uses lock-free structures internally for goroutine scheduling.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why does the Michael-Scott queue use a sentinel (dummy) node?
2. Explain the ABA problem on a lock-free stack with a concrete 3-step scenario.
3. What is the difference between lock-free and wait-free progress guarantees?

### Core Problems
1. **Treiber Stack**: Implement a lock-free stack using `std::atomic` (C++) or `AtomicReference` (Java). Use tagged pointers (128-bit CAS or packed counter) to prevent ABA. Stress-test with 8 producer threads and 8 consumer threads pushing/popping 1M items.
2. **SPSC Ring Buffer**: Implement a single-producer single-consumer lock-free ring buffer using only atomic loads/stores (no CAS). Prove that it's correct under x86-TSO and ARM memory models. Benchmark throughput.

### Challenge
Implement a **lock-free work-stealing deque** (Chase-Lev, 2005) with:
- `push()` and `pop()` by the owning thread (LIFO end)
- `steal()` by other threads (FIFO end)
This is the building block of task-parallel runtimes (Cilk, TBB, Tokio). Test with a divide-and-conquer parallel mergesort where each thread has its own deque and steals work when idle.

---

*See also:* [[Concurrent Data Structures]] · [[Queues]] · [[Stacks]] | **CS Algorithms:** [[Parallel Algorithms]] · [[Synchronization Primitives]]

## References
-> [[Sources Index]]
