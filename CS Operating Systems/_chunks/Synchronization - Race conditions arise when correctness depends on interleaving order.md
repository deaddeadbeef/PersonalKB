---
id: chunk-csos-011
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 2"
topic: "synchronization"
claim: "A race condition occurs when two or more threads access shared state without synchronisation, and the result depends on their scheduling interleaving — making it non-deterministic and potentially wrong"
confidence: verified
supports:
  - "[[Race Conditions and Mutual Exclusion]]"
tags:
  - csos
  - csos/synchronization
  - chunk
up: "[[CS Operating Systems]]"
---
# Synchronization — Race conditions arise when correctness depends on interleaving order

## Context

Tanenbaum's canonical example: two processes both execute `count++` (load, increment, store) on a shared variable. If process A loads the value (say 5), is preempted, B loads the same 5, B stores 6, A stores 6 — the double increment produced only one net increment. The result (5 or 6) is correct on any single run but differs between runs. This is a race condition: the program's output depends on the *race* between threads' instruction streams.

## Why It Matters

Races are the most insidious bugs in concurrent programming — they are non-deterministic, often disappear under a debugger (Heisenbugs), and may only manifest under specific load patterns in production. The entire field of synchronisation primitives (semaphores, mutexes, monitors, lock-free atomics) exists to eliminate races by enforcing serialisation at the right granularity.

## QnA Seeds

- Q: What makes a race condition different from an ordinary bug?
- Q: Show how a race condition can occur on `count++` with two threads.
- Q: What three properties must a mutual-exclusion solution satisfy?
