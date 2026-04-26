---
id: chunk-csos-111
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 8 — Multiprocessor and SMP Systems"
topic: "multiprocessor"
claim: "In SMP systems all processors are equal peers that run the OS simultaneously, requiring all kernel data structures to be protected against concurrent access — this is fundamentally harder than single-processor kernel design"
confidence: verified
supports:
  - "[[Multiprocessor Systems]]"
  - "[[Multiprocessor Overview]]"
tags:
  - csos
  - csos/multiprocessor
  - chunk
up: "[[CS Operating Systems]]"
---
# Multiprocessor — SMP requires concurrent protection of all kernel data structures

## Context

In a symmetric multiprocessing system, all processors are identical peers sharing a single physical memory, with each capable of executing any process and running the same OS kernel code simultaneously. This means any kernel data structure — the process table, page frame database, file system caches — may be accessed concurrently by multiple CPUs. Linux transitioned from a Big Kernel Lock (BKL, a single global spinlock) in kernel 2.4 to fine-grained per-subsystem locking in 2.6, finally removing the BKL entirely in kernel 3.0 (2011). This transition took over a decade of engineering effort.

## Why It Matters

The BKL-to-fine-grained-locking transition explains why SMP scalability doesn't come for free — it required re-examining every kernel data structure for concurrent safety. This also illustrates why new OS designs (like microkernels or unikernels) attract interest: retrofitting concurrency into a monolithic kernel is enormously difficult.

## QnA Seeds

- Q: What makes SMP kernel design harder than uniprocessor kernel design?
- Q: What was the Big Kernel Lock and why was it removed?
- Q: Why did the transition from BKL to fine-grained locking take over a decade?
