---
tags: [cs-os, chunk]
source: "[[raw-os-004]]"
confidence: high
supports:
  - "[[Threads and Concurrency]]"
qna_seeds:
  - "Q: What do threads within a process share, and what is private to each thread? A: Threads share code, data (heap), and open files. Each thread has its own program counter, CPU registers, and stack. This sharing makes inter-thread communication orders of magnitude cheaper than IPC since no kernel crossing or data copying is required."
---

# Thread Shared Address Space Model

Threads within the same process share code, data (heap), and open file descriptors, while each thread maintains its own program counter, CPU register set, and stack. This sharing makes inter-thread communication orders of magnitude cheaper than inter-process communication, since no kernel crossing or data copying is needed — threads can communicate via shared memory directly. A process is the unit of resource ownership and protection; a thread is the unit of CPU scheduling and execution.
