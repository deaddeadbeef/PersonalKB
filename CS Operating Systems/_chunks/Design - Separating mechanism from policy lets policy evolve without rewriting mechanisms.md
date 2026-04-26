---
id: chunk-csos-053
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 12"
topic: "design"
claim: "Separating mechanism from policy lets OS designers provide flexible infrastructure: the mechanism (page fault handler, context switch) is stable, while policy (which page to evict, which process runs next) can change without touching the mechanism"
confidence: verified
supports:
  - "[[Mechanism vs Policy]]"
  - "[[OS Design Principles]]"
tags:
  - csos
  - csos/design
  - chunk
up: "[[CS Operating Systems]]"
---
# Design — Separating mechanism from policy lets policy evolve without rewriting mechanisms

## Context

The classic example is paging: the mechanism (page table, TLB, page fault trap, swap I/O) is fixed hardware and kernel infrastructure. The policy (OPT, FIFO, LRU, clock) is a software decision implemented by interchangeable replacement algorithm. Changing from LRU to clock requires changing one function, not rewriting the memory manager. Linux's pluggable I/O schedulers (CFQ, deadline, noop, kyber) and pluggable CPU schedulers (SCHED_OTHER CFS, SCHED_FIFO, SCHED_DEADLINE) are direct embodiments of this principle.

## Why It Matters

Without this separation, every policy change requires touching and re-testing the mechanism — increasing risk and complexity. With the separation, policies can be tuned for different workloads (a database tuned for deadline scheduler, a desktop tuned for CFS) or formally verified independently. Tanenbaum cites this as the single most important OS design principle. It also explains microkernel motivation: push policy to user space; keep mechanism in the kernel.

## QnA Seeds

- Q: Give a concrete example of mechanism vs policy in CPU scheduling.
- Q: Why does mechanism-policy separation make an OS easier to maintain?
- Q: How do Linux's pluggable schedulers embody this principle?
