---
tags: [cs-os, raw]
source_type: textbook_chapter
source_title: "Threads and Concurrency"
authors: "Andrew S. Tanenbaum, Herbert Bos"
year: 2015
---

# Threads and Concurrency

## Summary
Threads enable concurrent execution within a single process, sharing the same address space while maintaining independent program counters, registers, and stacks. The threading model—user-level, kernel-level, or hybrid—determines the tradeoffs between creation speed, scheduling flexibility, and the ability to exploit multiprocessor hardware. POSIX pthreads provides a standardized API that abstracts these implementation differences across Unix-like systems.

## Key Claims
- Threads within the same process share code, data, and open files, making inter-thread communication orders of magnitude cheaper than inter-process communication since no kernel crossing or data copying is required
- User-level threads are invisible to the kernel and can be created/switched in microseconds, but a single blocking system call blocks all threads in the process (the many-to-one problem)
- The one-to-one model (used by Linux NPTL and Windows) maps each user thread to a kernel thread, enabling true parallelism on multiprocessors at the cost of higher creation/switching overhead
- Thread pools amortize creation cost by pre-allocating worker threads that process tasks from a shared queue, avoiding both the overhead of per-request thread creation and the resource exhaustion of unbounded thread spawning
- Thread-local storage (TLS) provides per-thread global variables, solving the problem of thread-unsafe libraries that rely on global state without requiring API changes

## Atomic Facts
1. In the many-to-one model, the thread library (e.g., GNU Pth) manages all scheduling in user space; the kernel sees only a single-threaded process, so these threads cannot run in parallel on multiprocessors
2. The many-to-many model (Solaris LWP, early Windows fibers) multiplexes M user threads onto N kernel threads (M ≥ N), combining user-level scheduling flexibility with kernel-level parallelism, but its complexity led most OSes to adopt the simpler one-to-one model
3. Linux implements threads via the clone() system call, which creates a new task that shares specified resources (address space, file descriptors, signal handlers) with its parent—internally, Linux makes no distinction between processes and threads
4. POSIX pthreads defines pthread_create(), pthread_join(), pthread_exit(), and synchronization primitives (mutexes, condition variables, read-write locks) as a portable threading API mandated by the Single UNIX Specification
5. A typical thread stack size is 1–8 MB (default 8 MB on Linux), which limits the practical number of threads per process; this is one motivation for event-driven architectures and coroutines
6. Thread pools typically size their worker count to the number of CPU cores for compute-bound work, or to a larger multiple (e.g., 2×–10× cores) for I/O-bound work where threads spend most time blocked

## Significance
The thread model is central to modern systems programming: web servers, databases, and GUI applications all rely on threading for responsiveness and throughput. Understanding the tradeoffs between threading models explains architectural choices from Node.js's single-threaded event loop (avoiding thread overhead) to Java's massive thread pools (leveraging one-to-one kernel threads), and the recent resurgence of lightweight threads (Go goroutines, Java virtual threads).

## Chunks Extracted
*Pending*
