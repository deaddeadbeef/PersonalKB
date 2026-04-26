---
id: chunk-csos-107
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 2 — Classic Synchronization Problems"
topic: "synchronization"
claim: "The bounded-buffer (producer-consumer) solution requires exactly three synchronization elements: a mutex for buffer access, a counting semaphore for empty slots, and a counting semaphore for full slots — omitting any one leads to race conditions or deadlock"
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
# Synchronization — Bounded-buffer needs mutex plus two counting semaphores

## Context

The producer-consumer solution uses: semaphore mutex=1 (binary, protects buffer), semaphore empty=N (counting, initially N empty slots), semaphore full=0 (counting, initially 0 full slots). The producer does wait(empty), wait(mutex), insert, signal(mutex), signal(full). The consumer does wait(full), wait(mutex), remove, signal(mutex), signal(empty). Each element serves a distinct purpose: mutex prevents concurrent buffer modification, empty blocks the producer when the buffer is full, and full blocks the consumer when the buffer is empty. Omitting the mutex causes data races; omitting either counting semaphore allows buffer overflow or underflow.

## Why It Matters

This is the canonical synchronization pattern underlying every message queue, pipeline buffer, and I/O ring buffer in systems software. The precise three-semaphore formulation also tests whether a student truly understands the difference between mutual exclusion (binary semaphore) and condition signaling (counting semaphores).

## QnA Seeds

- Q: What three semaphores are needed for the bounded-buffer problem and what does each do?
- Q: What goes wrong if the mutex semaphore is omitted?
- Q: Why must the producer call wait(empty) before wait(mutex)?
