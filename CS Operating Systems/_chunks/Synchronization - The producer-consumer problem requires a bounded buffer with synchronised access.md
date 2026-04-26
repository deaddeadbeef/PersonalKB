---
id: chunk-csos-014
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 2"
topic: "synchronization"
claim: "The producer-consumer problem requires a bounded buffer protected by a mutex plus two counting semaphores (empty and full) to block producers when full and consumers when empty without deadlock"
confidence: verified
supports:
  - "[[Classic Synchronization Problems]]"
  - "[[Semaphores]]"
tags:
  - csos
  - csos/synchronization
  - chunk
up: "[[CS Operating Systems]]"
---
# Synchronization — The producer-consumer problem requires a bounded buffer with synchronised access

## Context

The key insight: three semaphores are needed, not one. `mutex=1` protects the buffer. `empty=N` counts free slots (producers wait here). `full=0` counts filled slots (consumers wait here). The ordering matters: each thread must P the resource count (empty or full) *before* P(mutex), never after. Reversing the order — P(mutex) then P(empty) — creates a deadlock: a producer holds the mutex and blocks on empty; a consumer blocks on mutex waiting to V(full).

## Why It Matters

The producer-consumer problem is the prototype for all buffered pipeline systems: web servers (request queue), operating system kernel (interrupt-to-process event queues), message brokers (Kafka). The bounded buffer pattern with correct semaphore ordering is directly used in real-world code.

## QnA Seeds

- Q: Why are three semaphores needed for the bounded-buffer producer-consumer?
- Q: What deadlock occurs if the P operations are in the wrong order?
- Q: How does the solution generalise to multiple producers and consumers?
