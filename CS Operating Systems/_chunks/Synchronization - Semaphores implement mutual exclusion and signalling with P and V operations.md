---
id: chunk-csos-012
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 2"
topic: "synchronization"
claim: "Semaphores provide mutual exclusion and signalling through two atomic operations P (down/wait) and V (up/signal), blocking rather than busy-waiting when the resource is unavailable"
confidence: verified
supports:
  - "[[Semaphores]]"
  - "[[Race Conditions and Mutual Exclusion]]"
tags:
  - csos
  - csos/synchronization
  - chunk
up: "[[CS Operating Systems]]"
---
# Synchronization — Semaphores implement mutual exclusion and signalling with P and V operations

## Context

Dijkstra introduced semaphores in 1965 as a kernel-managed primitive that avoids busy-waiting. P(s): if s > 0, decrement and proceed; else block the calling process. V(s): increment; if a process is blocked, wake one. Crucially, both operations are atomic — the OS guarantees they cannot be interrupted mid-operation. A binary semaphore (initialised to 1) implements a mutex. A counting semaphore (initialised to N) controls access to a pool of N resources.

## Why It Matters

Semaphores are the lowest-level general synchronisation primitive available to programmers. Understanding them is necessary for understanding monitors (which are implemented with semaphores), mutexes, condition variables, and the classical synchronisation problems. The correct P-then-V ordering (especially in the producer-consumer problem where the wrong order causes deadlock) is a classic interview and exam topic.

## QnA Seeds

- Q: What does P(s) do when s = 0?
- Q: How do you use a semaphore to signal that an event has completed?
- Q: What is the difference between a binary and a counting semaphore?
