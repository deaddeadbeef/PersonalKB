---
tags:
  - csos
  - csos/processes
confidence: verified
up: "[[Processes Overview]]"
tier-coverage:
  - intuition
  - core
  - deep-dive
  - practice
---
# Threads and Multithreading

> **One-line summary**: A thread is a lightweight unit of execution within a process — threads share the address space but have independent stacks, PCs, and registers.

## 🎯 Intuition
**The Core Idea:** Threads are sous chefs working in the same kitchen (process) — they share ingredients (memory) and equipment (resources) but each follows their own recipe step (program counter).
**Analogy:** A process is a restaurant kitchen; a thread is a cook. All cooks share the pantry (heap), counter space (globals), and recipe book (code). But each cook has their own cutting board (stack) and keeps track of which step they're on (PC, registers). Hiring a new cook (creating a thread) is cheap — they just need a cutting board. Opening a whole new kitchen (creating a process) is expensive.
**Why It Matters:** Threads are how modern software exploits multi-core CPUs. Web servers, GUIs, and scientific applications all use threads. But sharing memory means data races are a constant hazard.

---

## ⚙️ Core Mechanics
### How It Works
A **thread** is a unit of execution within a process. All threads in a process share the same address space (code, heap, globals) but each has its own program counter, stack, and register set. This sharing makes threads cheaper to create and context-switch than full processes.

### Key Concepts

| Property | Process | Thread |
|----------|---------|--------|
| Address space | Private | Shared with siblings |
| Creation cost | High (copy-on-write, PCB setup) | Low (stack + TCB only) |
| Context-switch cost | High (TLB flush, address-space switch) | Low (same address space) |
| Communication | Requires IPC (pipes, sockets, shared mem) | Direct access to shared globals |
| Failure isolation | Crash is contained | Crash kills all threads |

#### User-Space Threads
The thread library runs in user space; the kernel sees only one process. Thread switching is fast (no system call), but a blocking system call by one thread blocks the entire process. M:1 model.

#### Kernel-Space Threads
The kernel manages each thread; `clone()` / `pthread_create()` creates a kernel-visible task. Blocking one thread does not block others. Context switching requires a system call. 1:1 model (Linux, Windows).

#### Hybrid (M:N) Threads
N user threads multiplexed over M kernel threads. Attempts to get the speed of user-space switching with the blocking-tolerance of kernel threads. Complex to implement correctly; rare in production.

### Key Facts
- Threads share code, heap, and globals but each has a private stack and register set.
- User-space threads are fast to switch but one blocking syscall blocks the entire process.
- Kernel-space threads (1:1) are the standard in Linux and Windows — blocking is per-thread.
- A thread crash (e.g., segfault) kills the entire process — no fault isolation between threads.

### Classic Multithreading Uses

- Web server: one thread per connection; I/O blocks one thread while others serve.
- GUI application: one thread for UI, another for background work.
- Scientific computing: parallel computation over independent data partitions.

---

## 🔬 Deep Dive
### Implementation Details
- **Linux `clone()` syscall**: Both `fork()` and `pthread_create()` are implemented via `clone()`. The flags argument controls what is shared: `CLONE_VM` (share address space = thread), `CLONE_FILES` (share file descriptors), `CLONE_SIGHAND` (share signal handlers). A thread is simply a `task_struct` that shares `mm_struct` with its parent.
- **Thread stack allocation**: pthreads allocates a default 8 MB stack per thread (but physical pages are demand-allocated). Stack overflow writes to a guard page → segfault. Stack size is configurable via `pthread_attr_setstacksize()`.
- **Thread-local storage (TLS)**: Each thread gets private copies of `__thread` (C) or `thread_local` (C++11) variables. Implemented via a segment register (FS on x86-64 Linux) pointing to a per-thread TLS block.
- **Green threads and goroutines**: Go uses M:N scheduling with goroutines (user-space tasks) multiplexed over OS threads. The Go runtime handles scheduling, stack growth (starting at 2 KB, growing dynamically), and I/O multiplexing. This avoids the per-thread 8 MB stack overhead.

### Edge Cases and Pitfalls
- **Data races**: Threads sharing globals without synchronisation produces undefined behaviour. Even "benign" races (e.g., a boolean flag) can break under compiler/CPU reordering.
- **False sharing**: Two threads writing to different variables that happen to share a cache line cause constant cache invalidation, destroying performance. Align hot variables to cache-line boundaries.
- **Deadlock via lock ordering**: Thread A locks mutex X then waits for mutex Y; Thread B locks Y then waits for X. Always acquire locks in a consistent global order.
- **Signal delivery in multithreaded programs**: Signals are delivered to an arbitrary thread (unless directed with `pthread_kill()`). Use `sigwait()` in a dedicated signal-handling thread for predictable behaviour.

### Real-World Systems
- **Linux (NPTL)**: Native POSIX Threads Library; 1:1 model; `clone()` creates kernel-scheduled threads. Futex-based mutexes avoid syscalls in the uncontended case.
- **Windows**: Each thread has a TEB (Thread Environment Block) and a kernel-mode KTHREAD. `CreateThread()` / `_beginthreadex()` for creation. Thread pool API for managed concurrency.
- **Java**: `java.lang.Thread` maps to native OS threads (1:1). Java 21+ introduces virtual threads (Project Loom) — M:N scheduling within the JVM, similar to goroutines.
- **Go**: Goroutines are M:N user-space tasks; the Go scheduler multiplexes them over OS threads with work-stealing.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why is creating a thread cheaper than creating a process?
2. In the M:1 threading model, what happens when one thread makes a blocking system call?
3. Why does a segfault in one thread kill all threads in the process?

### Core Problems
1. **Thread vs process decision**: You're building a chat server handling 10,000 concurrent connections. Compare three designs: (a) one process per connection, (b) one thread per connection, (c) event loop with non-blocking I/O. Analyse memory overhead, context-switch cost, and programming complexity for each.
2. **False sharing experiment**: Two threads each increment their own counter 100 million times. In Design A, both counters are adjacent in an array (`int counters[2]`). In Design B, they are padded to separate cache lines. Predict the performance difference and explain why. (Hint: L1 cache line = 64 bytes on x86.)

### Challenge
Go's goroutine scheduler uses M:N threading with work-stealing. When a goroutine makes a blocking syscall, Go parks the OS thread and spins up a new one to keep other goroutines running. Design a simplified M:N scheduler: (a) Define the data structures (user thread queue, OS thread pool, runnable queue). (b) Describe the scheduling algorithm when a user thread blocks. (c) How does your design handle the case where all OS threads are blocked on syscalls? (d) Compare your design to Go's `GOMAXPROCS` mechanism.

---

*See also:* [[Race Conditions and Mutual Exclusion]] — threads sharing data need mutual exclusion to avoid races · [[Address Spaces]] — threads share the process address space; processes do not · [[Multiprocessor Systems]] — threads exploit multiple cores; false sharing and cache coherence matter · [[CPU Scheduling]] — the scheduler dispatches threads (or processes) to CPUs

## Supporting Chunks

- [[Processes - Threads share address space but have independent stacks and program counters]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 2.
