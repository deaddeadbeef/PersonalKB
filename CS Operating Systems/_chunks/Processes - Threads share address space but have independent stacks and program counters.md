---
id: chunk-csos-008
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 2"
topic: "processes"
claim: "Threads within a process share the same address space and open file table but each has an independent stack, program counter, and register set"
confidence: verified
supports:
  - "[[Threads and Multithreading]]"
tags:
  - csos
  - csos/processes
  - chunk
up: "[[CS Operating Systems]]"
---
# Processes — Threads share address space but have independent stacks and program counters

## Context

When a process creates a thread, the new thread gets its own stack (so function calls work independently) and its own program counter (so it executes independently). Everything else — the heap, global variables, open file descriptors, signal handlers — is shared. This sharing is exactly what makes thread communication cheap (no IPC, just write to a shared variable) and thread creation fast (no new address space needed).

## Why It Matters

The thread model is the basis for all server architectures that handle many simultaneous connections, for parallelising computation across CPU cores, and for separating UI responsiveness from background work. The shared address space is also the source of the thread's hazard: a stack overflow in one thread or a bad pointer write corrupts shared data for all threads.

## QnA Seeds

- Q: What does a thread have that is independent from other threads in the same process?
- Q: What is shared between threads of the same process?
- Q: Why is creating a thread cheaper than creating a process?
