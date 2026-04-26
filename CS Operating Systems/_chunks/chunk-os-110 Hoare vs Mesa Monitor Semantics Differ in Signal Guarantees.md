---
id: chunk-csos-110
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 2 — Classic Synchronization Problems"
topic: "synchronization"
claim: "Hoare monitor semantics guarantee the signaled thread runs immediately (signaler suspends), while Mesa semantics only move the signaled thread to the ready queue, requiring a while-loop recheck — Mesa is used by virtually all modern systems including Java and POSIX pthreads"
confidence: verified
supports:
  - "[[Monitors and Condition Variables]]"
  - "[[Classic Synchronization Problems]]"
tags:
  - csos
  - csos/synchronization
  - chunk
up: "[[CS Operating Systems]]"
---
# Synchronization — Hoare vs Mesa monitor semantics differ in signal-wakeup guarantees

## Context

Monitors encapsulate shared data and synchronization into a construct where only one thread executes at a time. The critical design choice is condition variable semantics. Hoare semantics (1974): signal(cv) immediately transfers execution to the waiting thread — the signaler is suspended until the waiter finishes or waits again. Mesa semantics (Xerox PARC, 1980): signal(cv) merely moves a waiter to the ready queue, and the signaler continues — the waiter must re-verify the condition in a while loop because another thread may change state before the waiter actually runs. Condition variables support wait(cv, mutex) — atomically release mutex and suspend — and signal(cv)/broadcast(cv).

## Why It Matters

Mesa semantics won in practice because Hoare semantics require expensive immediate context switches on every signal. The practical consequence is that every correct use of condition variables wraps the wait in `while(!condition)`, not `if(!condition)`. This is one of the most common concurrency bugs — using `if` instead of `while` with Mesa-semantic condition variables.

## QnA Seeds

- Q: What is the practical difference between Hoare and Mesa condition variable semantics?
- Q: Why must condition variable waits use a while loop under Mesa semantics?
- Q: Which semantics do Java's synchronized/wait/notify and POSIX pthreads use?
