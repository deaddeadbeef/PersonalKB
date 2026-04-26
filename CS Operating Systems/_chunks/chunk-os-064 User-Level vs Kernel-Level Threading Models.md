---
tags: [cs-os, chunk]
source: "[[raw-os-004]]"
confidence: high
supports:
  - "[[Threads and Concurrency]]"
qna_seeds:
  - "Q: What is the many-to-one threading problem and how does one-to-one solve it? A: In many-to-one, user-level threads are invisible to the kernel, so a single blocking syscall blocks all threads. One-to-one (Linux NPTL, Windows) maps each user thread to a kernel thread, enabling true multiprocessor parallelism at the cost of higher creation overhead."
---

# User-Level vs Kernel-Level Threading Models

The many-to-one model manages all threads in user space (e.g., GNU Pth); the kernel sees a single-threaded process, so one blocking system call blocks all threads and true parallelism on multiprocessors is impossible. The one-to-one model (Linux NPTL, Windows) maps each user thread to a kernel thread, enabling real parallelism at the cost of higher creation/switching overhead. The many-to-many model (Solaris LWP) multiplexes M user threads onto N kernel threads (M ≥ N), but its complexity led most modern OSes to adopt the simpler one-to-one model.
