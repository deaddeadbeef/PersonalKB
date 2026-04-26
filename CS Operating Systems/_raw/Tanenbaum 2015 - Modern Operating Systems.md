---
id: raw-2015-001
type: raw
title: "Modern Operating Systems"
author: "Andrew S. Tanenbaum; Herbert Bos"
year: 2015
publisher: "Pearson"
url: ""
status: seeded
chunk_count: 54
tags:
  - csos
  - raw
up: "[[CS Operating Systems]]"
---
# Tanenbaum 2015 — Modern Operating Systems

## What This Source Is

A textbook (print) — a comprehensive graduate and advanced-undergraduate treatment of operating systems. 4th edition, approximately 1100 pages. 12 main chapters plus appendices. Covers OS theory from first principles through implementation details, with two full case-study chapters on Linux/Android and Windows 8. Written by Andrew S. Tanenbaum (Vrije Universiteit Amsterdam) and Herbert Bos.

Local copy: `C:\Users\fpan1\Downloads\Modern Operating Systems 4th Edition--Andrew Tanenbaum.pdf`

## Why It Matters to CS Operating Systems

This book is the **primary source** for this knowledge base. It is the most widely adopted graduate OS textbook, covering every major subsystem: process and thread management, inter-process communication, virtual memory and paging, file systems, I/O subsystems, deadlock theory, virtualisation, multiprocessor coordination, security, and full case studies of production systems. Tanenbaum's treatment is notable for its balance of conceptual clarity with concrete implementation details — each major concept is backed by a real-world example or system call trace. The MINIX design discussions provide additional design-pattern depth not available in other texts.

## Key Takeaways

- An operating system is fundamentally a resource manager and extended machine that hides hardware complexity behind clean abstractions (processes, files, address spaces).
- Concurrency is inherently dangerous — races, deadlocks, and starvation are not edge cases but inevitable consequences of shared state.
- The key insight in virtual memory is that programs can address more memory than physically exists; demand paging defers the cost until the page is actually needed.
- File systems must solve a persistence problem: surviving crashes with consistent metadata despite the gap between volatile and non-volatile storage speeds.
- Deadlock is unavoidable if all four Coffman conditions hold simultaneously; removing any one prevents it.
- Security is a systems problem, not just a cryptography problem — the weakest link is usually privilege escalation or a misconfigured permission boundary.

## Chunk Candidates

- [x] OS as extended machine and resource manager — dual role
- [x] Kernel vs user mode — hardware-enforced privilege boundary
- [x] System calls as the OS–application interface
- [x] Monolithic kernel architecture
- [x] Microkernel architecture — pros/cons vs monolithic
- [x] Process model — PCB, address space, creation/termination
- [x] Process states — running, ready, blocked; scheduler transitions
- [x] Thread model — shared address space; user-space vs kernel-space threads
- [x] Interprocess communication — pipes, shared memory, message passing
- [x] CPU scheduling — round-robin, priority, multilevel feedback queues
- [x] Race conditions arise when outcome depends on interleaving order
- [x] Mutual exclusion via Peterson's algorithm (software) and TSL (hardware)
- [x] Semaphores — P/V; binary vs counting; blocking vs busy-waiting
- [x] Monitors and condition variables — structured sync for correctness
- [x] Producer-consumer problem — bounded buffer with semaphores
- [x] Dining philosophers — deadlock, starvation, correct solutions
- [x] Address space abstraction — logical vs physical; base/limit protection
- [x] Paging — fixed-size pages; page table; fragmentation comparison
- [x] TLB accelerates paging by caching recent translations
- [x] Page replacement — OPT, FIFO, LRU, clock algorithm
- [x] Segmentation — variable-size segments; combining with paging
- [x] File abstraction — named, persistent byte sequence; metadata
- [x] Directory structures — hierarchical paths; hard links vs symlinks
- [x] Inode-based allocation — Unix VFS; indirect blocks
- [x] Journaling guarantees crash consistency via write-ahead log
- [x] Interrupts — hardware event model; interrupt vector; handler latency
- [x] DMA — offloads bulk transfer from CPU; bus arbitration
- [x] Device drivers as OS–hardware interface layer
- [x] Disk scheduling — SSTF, SCAN/elevator, C-SCAN; seek vs rotational
- [x] Deadlock necessary conditions — mutual exclusion, hold-and-wait, no preemption, circular wait
- [x] Resource-allocation graph — cycle detection for deadlock
- [x] Banker's algorithm — safe state test for deadlock avoidance
- [x] Deadlock prevention — attack each Coffman condition
- [x] Type 1 and type 2 hypervisors — bare-metal vs hosted
- [x] Para-virtualisation — guest OS cooperates with hypervisor for efficiency
- [x] SMP vs NUMA multiprocessor architectures
- [x] Cache coherence — MSI/MESI protocol; false sharing
- [x] OS security threat model — CIA triad; attack surface; least privilege
- [x] Access control matrix — ACLs, capability lists; RBAC abstraction
- [x] Malware taxonomy — viruses, worms, rootkits; defense layers
- [x] Linux kernel architecture — monolithic with modules; CFS; VFS
- [x] Android on Linux — Binder IPC; permission model; ART runtime
- [x] Windows NT architecture — HAL, microkernel-style executive, Win32 subsystem
- [x] Mechanism vs policy separation — flexibility without re-implementation
- [x] OS design trade-offs — simplicity vs performance, portability vs efficiency
- [x] Authentication — passwords, hashing, biometrics, multi-factor
- [x] IO software layers — interrupt handler → driver → OS layer → user space
- [x] Virtual memory demand paging — page fault handling path
- [x] Readers-writers problem — read-write locks; starvation variants

## Related Wiki Notes

- [[OS Fundamentals]] — Chapter 1
- [[System Calls]] — Chapter 1
- [[OS Structure]] — Chapter 1
- [[Process Model]] — Chapter 2
- [[Process States and Transitions]] — Chapter 2
- [[Threads and Multithreading]] — Chapter 2
- [[CPU Scheduling]] — Chapter 2
- [[Interprocess Communication]] — Chapter 2
- [[Race Conditions and Mutual Exclusion]] — Chapter 2
- [[Semaphores]] — Chapter 2
- [[Monitors and Condition Variables]] — Chapter 2
- [[Classic Synchronization Problems]] — Chapter 2
- [[Address Spaces]] — Chapter 3
- [[Virtual Memory and Paging]] — Chapter 3
- [[Page Replacement Algorithms]] — Chapter 3
- [[Segmentation]] — Chapter 3
- [[File System Fundamentals]] — Chapter 4
- [[Directory Structures]] — Chapter 4
- [[File System Implementation]] — Chapter 4
- [[Journaling File Systems]] — Chapter 4
- [[IO Hardware Fundamentals]] — Chapter 5
- [[Interrupts and DMA]] — Chapter 5
- [[IO Software Layers]] — Chapter 5
- [[Device Drivers]] — Chapter 5
- [[Disk Scheduling Algorithms]] — Chapter 5
- [[Deadlock Fundamentals]] — Chapter 6
- [[Deadlock Detection and Recovery]] — Chapter 6
- [[Deadlock Avoidance]] — Chapter 6
- [[Deadlock Prevention]] — Chapter 6
- [[Virtualization Fundamentals]] — Chapter 7
- [[Hypervisors]] — Chapter 7
- [[Multiprocessor Systems]] — Chapter 8
- [[Distributed Systems Overview]] — Chapter 8
- [[OS Security Fundamentals]] — Chapter 9
- [[Access Control]] — Chapter 9
- [[Authentication and Protection]] — Chapter 9
- [[Malware and Defenses]] — Chapter 9
- [[Linux Architecture Overview]] — Chapter 10
- [[Android Architecture]] — Chapter 10
- [[Windows NT Architecture]] — Chapter 11
- [[OS Design Principles]] — Chapter 12
- [[Mechanism vs Policy]] — Chapter 12

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]].
