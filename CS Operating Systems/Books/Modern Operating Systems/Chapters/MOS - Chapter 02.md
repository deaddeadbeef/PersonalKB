---
id: mos-ch-02
type: book-chapter
chapter: 2
book: "Modern Operating Systems"
author: "Andrew S. Tanenbaum"
status: seeded
chunk_count: 10
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
tags:
  - csos
  - book-chapter
up: "[[CS Operating Systems/Books/Modern Operating Systems/Chapter Index|Chapter Index]]"
confidence: established
freshness: stable
tier-coverage: [core]
---
# MOS — Chapter 02: Processes and Threads

## Summary

The longest chapter in the book covers the two fundamental abstractions for concurrent execution. Processes encapsulate an address space, execution state, and metadata (PCB); they transition among running, ready, and blocked states as the scheduler and I/O events dictate. Threads share a process's address space while maintaining independent stacks and program counters; user-space and kernel-space thread implementations each carry distinct trade-offs. The chapter then covers inter-process communication (pipes, shared memory, message passing, signals), CPU scheduling policies (FCFS, SJF, round-robin, priority, multilevel feedback), and the core synchronization problems. Race conditions are defined, mutual exclusion solutions are developed from software (Peterson) through hardware (TSL) to OS-level primitives (semaphores, monitors), and the classical problems (producer-consumer, dining philosophers, readers-writers) are worked through in detail.

## Key Concepts

| Concept | One-liner |
|---------|-----------|
| Process | OS abstraction: address space + execution state + PCB |
| Thread | Lightweight execution unit sharing a process address space |
| Race condition | Non-deterministic outcome from unsynchronised shared-state access |
| Semaphore | Kernel counter supporting P (down) and V (up) atomic operations |
| Monitor | Language-level construct enforcing mutual exclusion automatically |
| Round-robin scheduling | Time quantum per process; fair CPU sharing |

## Chunk Candidates

- [x] [[Processes - The process model gives each program the illusion of an exclusive CPU]]
- [x] [[Processes - Process states form a three-state lifecycle driven by scheduler and IO events]]
- [x] [[Processes - Threads share address space but have independent stacks and program counters]]
- [x] [[Processes - IPC mechanisms differ in coupling, latency, and scope]]
- [x] [[Processes - Round-robin scheduling gives each process a quantum for fair CPU sharing]]
- [x] [[Synchronization - Race conditions arise when correctness depends on interleaving order]]
- [x] [[Synchronization - Semaphores implement mutual exclusion and signalling with P and V operations]]
- [x] [[Synchronization - Monitors enforce mutual exclusion automatically at the language level]]
- [x] [[Synchronization - The producer-consumer problem requires a bounded buffer with synchronised access]]
- [x] [[Synchronization - The dining philosophers problem exposes deadlock and starvation in resource allocation]]

## Wiki Pages Seeded

- [[Process Model]] — process concept, PCB, creation, termination
- [[Process States and Transitions]] — three-state model, scheduler role
- [[Threads and Multithreading]] — user-space vs kernel threads
- [[CPU Scheduling]] — round-robin, priority, SJF
- [[Interprocess Communication]] — pipes, shared memory, message passing
- [[Race Conditions and Mutual Exclusion]] — critical sections, Peterson, TSL
- [[Semaphores]] — P/V, binary vs counting
- [[Monitors and Condition Variables]] — high-level sync
- [[Classic Synchronization Problems]] — producer-consumer, dining philosophers, readers-writers

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Tanenbaum 2015]].
