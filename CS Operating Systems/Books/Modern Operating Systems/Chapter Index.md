---
tags:
  - csos
  - chapter-index
up: "[[Modern Operating Systems]]"
confidence: established
freshness: stable
tier-coverage: [core]
---
# Chapter Index — Modern Operating Systems

Status key: `unread` · `seeded` · `in-progress` · `processed`

| # | Title | Status | Chunks | Note |
|---|-------|--------|--------|------|
| 1 | Introduction | seeded | 5 | [[MOS - Chapter 01]] |
| 2 | Processes and Threads | seeded | 10 | [[MOS - Chapter 02]] |
| 3 | Memory Management | seeded | 6 | [[MOS - Chapter 03]] |
| 4 | File Systems | seeded | 5 | [[MOS - Chapter 04]] |
| 5 | Input/Output | seeded | 5 | [[MOS - Chapter 05]] |
| 6 | Deadlocks | seeded | 4 | [[MOS - Chapter 06]] |
| 7 | Virtualization and the Cloud | seeded | 3 | [[MOS - Chapter 07]] |
| 8 | Multiple Processor Systems | seeded | 4 | [[MOS - Chapter 08]] |
| 9 | Security | seeded | 5 | [[MOS - Chapter 09]] |
| 10 | Case Study 1: UNIX, Linux, and Android | seeded | 3 | [[MOS - Chapter 10]] |
| 11 | Case Study 2: Windows 8 | seeded | 2 | [[MOS - Chapter 11]] |
| 12 | Operating System Design | seeded | 2 | [[MOS - Chapter 12]] |

**Total chunks in initial seed: 54** (target was ~47; additional coverage added for Ch02 and Ch09 where density justified it).

---

## Back to Book

[[Modern Operating Systems]] · [[Tanenbaum 2015 - Modern Operating Systems]]

## Reading Workflow

Treat the chapter notes as a book-progress ledger. A `seeded` chapter has enough extracted concepts to orient the wiki, but it is not the same as a finished reading pass. Move a chapter to `in-progress` when you are actively reconciling the textbook with the topic pages, and move it to `processed` only after the core mechanisms have been routed into the relevant OS domains.

The highest-value reading path is not strictly chapter order. Read chapters 1-3 first for the process, thread, address-space, and memory vocabulary. Then branch by implementation need: file systems and I/O for storage behavior, deadlocks and synchronization for concurrency hazards, virtualization for isolation boundaries, and security for threat models.

## What To Extract

For every chapter, extract three things: the abstraction boundary, the failure mode, and the implementation trade-off. Operating systems are best remembered as controlled compromises. Processes hide CPU multiplexing, virtual memory hides physical memory scarcity, file systems hide device details, and synchronization hides interleaving risk. The notes should make those compromises explicit enough that they can guide emulator, runtime, or systems-programming decisions later.

## References

- [[CS Operating Systems/Books/Modern Operating Systems/Modern Operating Systems]]
- [[CS Operating Systems/Sources/Sources Index]]
