---
tags: [programming-languages, concurrency, threads]
up: "[[Concurrency Models Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---

# Threads and Locks

> The oldest and most direct concurrency model — create OS threads that execute simultaneously, protect shared data with locks (mutexes) — and despite its dangers, it remains the foundation of concurrent programming in most languages.

---

## 🎯 Intuition

### Core Idea

Multiple independent execution flows (threads) run within a single process, sharing memory. Because shared memory is inherently unsafe to access concurrently, **locks** (mutexes) enforce mutual exclusion so only one thread touches a critical section at a time.

### Analogy

Threads + locks = **multiple chefs in one kitchen sharing knives and cutting boards** — locks are the "in use" signs to avoid accidents. Each chef works independently, but whenever two chefs need the same knife, one must wait for the other to put it down. Remove the signs and you get collisions; add too many signs and everyone stands around waiting.

### Why It Matters

This model is the lowest common denominator of concurrency. Higher-level models — channels, actors, async/await — are almost always built **on top of** threads and locks. Understanding the primitives explains why the abstractions exist and where they leak.

---

## ⚙️ Core Mechanics

### How It Works

An OS thread is an independent execution context with its own stack, sharing the process's heap memory. Mutexes (mutual exclusion locks) prevent multiple threads from accessing shared data simultaneously. Condition variables allow threads to wait for events. Read-write locks allow multiple concurrent readers but exclusive writers.

### Key Concepts

| Concept | Role | Key detail |
|---|---|---|
| **Thread** | Unit of execution | Own stack, shared heap; scheduled by the OS |
| **Mutex** | Mutual exclusion lock | Only one thread holds it at a time |
| **Condition variable** | Signalling primitive | Lets a thread sleep until an event occurs |
| **Read-write lock** | Shared/exclusive access | Multiple concurrent readers **or** one exclusive writer |
| **Critical section** | Protected code region | Code between lock acquisition and release |

### Language Examples

**C/C++:** Raw pthreads/std::thread with mutex/condition_variable. Maximum control, no safety guardrails. The programmer must ensure correct lock ordering, avoid holding locks too long, and never access shared data without the appropriate lock. This is where most concurrency bugs in production systems originate.

**Java:** Built-in `synchronized` keyword, `java.util.concurrent` library with ExecutorService, ConcurrentHashMap, AtomicInteger, etc. Java's memory model (JMM, JSR-133) precisely defines visibility guarantees for shared variables — a landmark specification that influenced all subsequent languages. Despite the good tooling, thread-safety bugs remain common in Java codebases.

**Python:** The Global Interpreter Lock (GIL) means only one thread can execute Python bytecode at a time. Threading exists but provides no CPU parallelism for pure Python code. This is a pragmatic choice — CPython's reference counting is not thread-safe, so the GIL provides safety at the cost of true parallelism. Python 3.13 introduces experimental GIL-free mode.

**Rust:** Provides threads (`std::thread`) with a crucial innovation: the type system prevents data races at compile time. Types that are safe to send between threads implement the `Send` trait; types safe to share via references implement `Sync`. `Mutex<T>` returns a guard that ensures the lock is released when the guard goes out of scope. You literally cannot write a data race in safe Rust — the compiler rejects it.

**OCaml:** Historically single-threaded due to a global runtime lock (similar to Python's GIL). OCaml 5.0 (2022) introduced multicore support with a novel approach: algebraic effects for concurrency and a concurrent minor GC. OCaml's immutable-by-default style means most data is naturally thread-safe.

### Key Facts — The Four Problems

| Problem | Description |
|---|---|
| **Deadlock** | Thread A holds lock 1 and waits for lock 2; Thread B holds lock 2 and waits for lock 1. Neither can proceed. |
| **Race condition** | Unsynchronized access to shared data produces unpredictable results. These bugs are notoriously hard to reproduce and debug. |
| **Priority inversion** | A high-priority thread waits for a lock held by a low-priority thread, which is preempted by a medium-priority thread. |
| **Composition failure** | Correct lock-based code doesn't compose — combining two thread-safe operations doesn't produce a thread-safe operation. |

---

## 🔬 Deep Dive

### Formal Foundations — Java Memory Model

Java's memory model (JMM, JSR-133) is the landmark formal specification for threading semantics. It precisely defines **happens-before** relationships that govern when writes by one thread become visible to reads by another. Before the JMM, language specs left visibility of shared variables implementation-defined. The JMM established that `synchronized`, `volatile`, and thread start/join create happens-before edges — everything else is fair game for the compiler and hardware to reorder. This specification influenced all subsequent language memory models, including C++11's `<atomic>` and Rust's `std::sync`.

### Trade-offs and Design Decisions — Why Threads + Locks Persist

Despite the danger, threads + locks persist because: (1) OS threads map directly to hardware parallelism, (2) existing systems and libraries use this model, (3) sometimes you genuinely need shared mutable state with fine-grained locking for performance. The alternatives each trade something away — actors sacrifice shared memory, STM sacrifices raw throughput, async sacrifices simplicity for I/O-bound workloads.

### Historical Context

The thread-and-lock model descends from early multiprogramming systems of the 1960s. Dijkstra's semaphore (1965) and Hoare's monitor (1974) formalized the primitives. POSIX threads (pthreads, 1995) standardized the API on Unix systems. Java (1995) brought threads into a mainstream language with built-in `synchronized`. Decades of hard-won experience with race conditions and deadlocks drove the creation of safer models — yet the original primitives remain the substrate on which those models run.

---

## 🏋️ Practice

### Warm-Up

1. Two threads each increment a shared counter 1 000 000 times without synchronization. What range of final values is possible, and why?
2. Explain why Python's GIL prevents CPU-parallel execution of pure Python threads but still allows I/O-parallel execution. What changes with Python 3.13's experimental free-threaded mode?
3. In Rust, what compiler error would you get if you tried to share a `Vec<i32>` across threads without wrapping it in `Arc<Mutex<Vec<i32>>>`? Which traits are involved?

### Core Problems

4. Design a lock-ordering protocol for a "bank transfer" function that moves money between two accounts without deadlocking, even when concurrent transfers go in opposite directions. Describe the invariant your protocol maintains.
5. You have a Java class with two `synchronized` methods, `deposit()` and `withdraw()`, each of which is individually thread-safe. Show a concrete interleaving where calling both from separate threads produces an incorrect balance, illustrating the composition-failure problem.

### Challenge

6. Implement a bounded producer-consumer queue using only mutexes and condition variables (no language-specific concurrent collections). Then analyze: under what workload ratio (producers vs. consumers) does your design degrade, and how would you redesign it to handle that case?

---

*See also:* [[Concurrency Models Overview]] · [[Programming Languages/Concurrency Models/The Actor Model|Actor Model]] · [[Software Transactional Memory]] · [[Programming Languages/Concurrency Models/Async-Await and Event Loops|Async-Await]]

---

## Supporting Chunks / References

- [[Programming Languages/Sources/Sources Index|Sources Index]]

## References

- [[Programming Languages/Sources/Sources Index]]
- [[Programming Languages/Programming Languages Book Reading Spine]]
- [[Programming Languages/Programming Languages]]
