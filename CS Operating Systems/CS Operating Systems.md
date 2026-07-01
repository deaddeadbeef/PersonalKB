---
tags:
  - csos
  - moc
up: "[[Welcome]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# CS Operating Systems

Master index for the *CS Operating Systems* knowledge base. Built around Andrew S. Tanenbaum's *Modern Operating Systems*, 4th ed. (Pearson, 2015) as the primary entry point — a comprehensive treatment of OS theory and practice covering processes, memory management, file systems, I/O, deadlocks, virtualisation, multiprocessors, security, and major case studies.

## Start Here

| Need | Open | Why |
|---|---|---|
| Read operating systems like a book | [[CS Operating Systems/CS Operating Systems Book Reading Spine|CS Operating Systems Book Reading Spine]] | Curated path from processes and memory to files, I/O, virtualization, security, and case studies |
| Follow the textbook route | [[CS Operating Systems/CS Operating Systems — Learning Path|CS Operating Systems Learning Path]] | Guided progression built around Modern Operating Systems |
| Debug a systems question or review | [[CS Operating Systems/Study/OS Study Index|OS Study Index]] | Goal router, active-recall drills, and mechanism-to-symptom routes |
| Check provenance | [[CS Operating Systems/Sources/Sources Index|CS Operating Systems Sources Index]] | Source map for textbook and supporting material |
| Browse the catalog | This page below | Domain hubs, books, study pages, sources, and infrastructure |

---

## Suggested Learning Path

Follow the hubs in this dependency order for a coherent first pass through the knowledge base:

1. [[OS Foundations Overview]] — what an OS is; kernel/user space; monolithic vs microkernel
2. [[Processes Overview]] — process model; scheduling; threads; IPC
3. [[Synchronization Overview]] — race conditions; semaphores; monitors; classic problems
4. [[CS Operating Systems/Memory/Memory Management Overview|Memory Management Overview]] — address spaces; paging; TLBs; page replacement
5. [[File Systems Overview]] — file abstraction; directories; inodes; journaling
6. [[IO Overview]] — device controllers; interrupts; DMA; disk scheduling
7. [[Deadlocks Overview]] — Coffman conditions; prevention; avoidance; detection
8. [[Virtualization Overview]] — type 1/2 hypervisors; trap-and-emulate; para-virt
9. [[Multiprocessor Overview]] — SMP; NUMA; cache coherence; distributed systems
10. [[Security Overview]] — threat model; access control; authentication; malware
11. [[Case Studies Overview]] — Linux, Android, Windows NT in practice
12. [[Design Principles Overview]] — mechanism vs policy; design goals and trade-offs

---

## Foundations

Core vocabulary: what operating systems are, why they exist, and how they are structured — kernel/user space, the system-call boundary, and architectural trade-offs (monolithic, microkernel, hybrid).

→ **[[OS Foundations Overview]]**

---

## Processes and Threads

The process and thread abstractions, the running/ready/blocked lifecycle, CPU scheduling algorithms, and inter-process communication mechanisms.

→ **[[Processes Overview]]**

---

## Synchronization

Race conditions, critical sections, and the primitives (semaphores, monitors) and classic problems (producer-consumer, dining philosophers) that test them.

→ **[[Synchronization Overview]]**

---

## Memory Management

From bare address spaces through virtual memory, paging, TLBs, and page-replacement algorithms — the complete memory abstraction stack.

→ **[[CS Operating Systems/Memory/Memory Management Overview|Memory Management Overview]]**

---

## File Systems

The file and directory abstraction, on-disk implementation (inodes, allocation strategies, free-space management), and crash-consistent journaling.

→ **[[File Systems Overview]]**

---

## Input/Output

I/O hardware (controllers, interrupts, DMA), the layered I/O software stack, device drivers, and disk scheduling algorithms.

→ **[[IO Overview]]**

---

## Deadlocks

The four Coffman conditions, and the three strategies for handling deadlock: prevention (deny a condition), avoidance (Banker's algorithm), and detection-and-recovery.

→ **[[Deadlocks Overview]]**

---

## Virtualization and the Cloud

Type 1 and type 2 hypervisors, full vs para-virtualisation, and how cloud infrastructure is built on these foundations.

→ **[[Virtualization Overview]]**

---

## Multiprocessor Systems

SMP vs NUMA architecture, cache coherence, multiprocessor scheduling (affinity, gang scheduling), and the distributed-systems model when shared memory disappears.

→ **[[Multiprocessor Overview]]**

---

## Security

Threat modeling, access-control models (ACLs, RBAC, MAC), authentication, and defenses against malware and memory-corruption exploits (ASLR, DEP).

→ **[[Security Overview]]**

---

## Case Studies

Abstract OS concepts applied to three real systems: Linux (monolithic + VFS + CFS), Android (Linux kernel + Binder + permissions), and Windows NT (hybrid architecture + HAL + Registry).

→ **[[Case Studies Overview]]**

---

## Design

High-level design philosophy: the goals OSes must balance, the trade-offs they navigate, and the mechanism-vs-policy principle that structures everything else.

→ **[[Design Principles Overview]]**

---

## Study

Drill notes for active recall and review.

- [[OS Study Index]] — index of all study/drill notes
- [[Processes and Scheduling - Review Drill]] — process model, lifecycle, scheduling algorithms, IPC
- [[Memory Management - Review Drill]] — paging, TLBs, page replacement, segmentation
- [[Synchronization and Deadlocks - Review Drill]] — race conditions, semaphores, monitors, Coffman conditions, Banker's algorithm
- [[File Systems and IO - Review Drill]] — inodes, journaling, interrupts, DMA, disk scheduling
- [[Virtualization Security and Case Studies - Review Drill]] — hypervisors, access control, malware defenses, Linux/Android/Windows NT

---

## Books

| Book | Author | Coverage |
|------|--------|----------|
| [[Modern Operating Systems]] | Andrew S. Tanenbaum | All 12 chapters; primary source |

---

## Raw Sources

- [[Tanenbaum 2015 - Modern Operating Systems]] — raw source note for the primary book

## Sources

- [[CS Operating Systems/Sources/Sources Index|Sources Index]] — citation registry for this topic

---

## Queries

| Query | Purpose |
|-------|---------|
| [[CS Operating Systems/_queries/QnA - Chapter Coverage|QnA - Chapter Coverage]] | Chapter processing status |
| [[CS Operating Systems/_queries/QnA - Chunk Coverage Map|QnA - Chunk Coverage Map]] | Which wiki notes have supporting chunks |
| [[CS Operating Systems/_queries/QnA - Canonical Coverage|QnA - Canonical Coverage]] | Which canonical topics have wiki pages |
| [[CS Operating Systems/_queries/QnA System Roadmap|QnA System Roadmap]] | Phase plan for the query system |

## References

- [[CS Operating Systems/CS Operating Systems Book Reading Spine]]
- [[CS Operating Systems/Sources/Sources Index]]
