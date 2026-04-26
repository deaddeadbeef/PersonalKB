---
id: chunk-csos-013
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 2"
topic: "synchronization"
claim: "Monitors enforce mutual exclusion automatically at the language level — only one thread executes inside a monitor at a time — while condition variables allow threads to wait for predicates without holding the lock"
confidence: verified
supports:
  - "[[Monitors and Condition Variables]]"
tags:
  - csos
  - csos/synchronization
  - chunk
up: "[[CS Operating Systems]]"
---
# Synchronization — Monitors enforce mutual exclusion automatically at the language level

## Context

Hoare (1974) and Hansen (1975) independently proposed the monitor as a higher-level construct that cannot be used incorrectly in the same way semaphores can. The programmer writes code inside a monitor; the runtime or compiler inserts the lock acquisition and release automatically. Condition variables (wait, signal, broadcast) let a thread inside the monitor atomically release the lock and sleep until a predicate becomes true, then reacquire the lock.

## Why It Matters

Monitors eliminate the "forgot to V" and "wrong order P" bugs that make semaphore programming error-prone. Java's `synchronized` + `wait/notify` and C++'s `std::condition_variable` implement monitor semantics. Because Mesa semantics (the common production implementation) re-check the condition after waking, the canonical rule is: always use `while`, not `if`, around a `wait()` call.

## QnA Seeds

- Q: What does `wait(cond)` do inside a monitor?
- Q: What is the difference between Hoare and Mesa monitor semantics?
- Q: Why should condition variable checks use `while` rather than `if`?
