---
id: chunk-csos-103
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 2 — Inter-Process Communication"
topic: "processes"
claim: "Shared memory IPC is the fastest form of inter-process communication because once the shared region is established, data transfer involves no system calls and no kernel intervention — processes read and write at hardware memory speed"
confidence: verified
supports:
  - "[[Interprocess Communication]]"
  - "[[Processes Overview]]"
tags:
  - csos
  - csos/processes
  - chunk
up: "[[CS Operating Systems]]"
---
# Processes — Shared memory IPC avoids kernel mediation for maximum throughput

## Context

Inter-process communication has two fundamental paradigms: shared memory and message passing. Shared memory is the fastest because after the shared region is established (via shm_open() and mmap() on POSIX, creating a named object in /dev/shm), processes communicate by simply reading and writing memory locations — no system calls, no kernel copies, no context switches per data exchange. The tradeoff is that processes must explicitly synchronize access using semaphores, mutexes, or other primitives to avoid race conditions on the shared region.

## Why It Matters

The speed advantage of shared memory makes it the preferred IPC mechanism for high-throughput scenarios: database shared buffer pools, multimedia pipelines, and inter-process caches. The producer-consumer problem is the canonical shared memory IPC scenario, requiring synchronization on buffer-full and buffer-empty conditions.

## QnA Seeds

- Q: Why is shared memory the fastest IPC mechanism?
- Q: What POSIX calls establish a shared memory region between processes?
- Q: What is the main drawback of shared memory IPC compared to message passing?
