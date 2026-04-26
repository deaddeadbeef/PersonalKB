---
tags: [cs-os, chunk]
source: "[[raw-os-004]]"
confidence: high
supports:
  - "[[Threads and Concurrency]]"
  - "[[Linux Internals]]"
qna_seeds:
  - "Q: How does Linux implement threads internally? A: Linux uses the clone() system call, which creates a new task that shares specified resources (address space, file descriptors, signal handlers) with its parent. Internally, Linux makes no distinction between processes and threads — both are tasks differing only in what they share."
---

# Linux Implements Threads via Clone

Linux implements threads via the clone() system call, which creates a new task sharing specified resources — address space, file descriptors, signal handlers — with its parent. Internally, Linux makes no structural distinction between processes and threads; both are kernel task_struct objects that differ only in which resources they share. This unified model means fork() is clone() with no sharing flags, while pthread_create() is clone() with full sharing flags. POSIX pthreads on Linux (NPTL) is built on top of clone().
