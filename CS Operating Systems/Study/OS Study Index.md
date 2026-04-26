---
tags:
  - csos
  - csos/study
up: "[[CS Operating Systems]]"
---
# OS Study Index

Central index for all CS Operating Systems active-recall drill notes. Each drill note covers one domain of the wiki, distilled into questions, contrasts, and common-mistake warnings. Use this index to plan review sessions and track which areas need more repetitions.

---

## How to Use

1. **First pass** — read through a drill note once to surface gaps. If you cannot answer a question without looking, mark it (e.g., highlight or add a `?` comment).
2. **Spaced repetition** — revisit marked questions on subsequent days. The questions are written for retrieval practice, not re-reading.
3. **Check against the wiki** — each note links back to the canonical page. After struggling with a question, open the canonical page for the full explanation, then close it and try again.
4. **Cross-domain sessions** — for a broad review, pick one question from each drill note in a single sitting.

---

## Drill Notes by Domain

| Drill Note | Canon pages covered | Difficulty focus |
|-----------|---------------------|-----------------|
| [[Processes and Scheduling - Review Drill]] | Process Model, Process States and Transitions, CPU Scheduling, Threads and Multithreading, Interprocess Communication | Scheduling algorithm selection; lifecycle transitions |
| [[Memory Management - Review Drill]] | Address Spaces, Virtual Memory and Paging, Page Replacement Algorithms, Segmentation | Page table mechanics; replacement policy trade-offs |
| [[Synchronization and Deadlocks - Review Drill]] | Race Conditions and Mutual Exclusion, Semaphores, Monitors and Condition Variables, Classic Synchronization Problems, Deadlock Fundamentals, Deadlock Prevention, Deadlock Avoidance, Deadlock Detection and Recovery | Semaphore construction; Coffman conditions; Banker's algorithm |
| [[File Systems and IO - Review Drill]] | File System Fundamentals, Directory Structures, File System Implementation, Journaling File Systems, IO Hardware Fundamentals, Interrupts and DMA, IO Software Layers, Disk Scheduling Algorithms | Inode layout; journaling modes; disk scheduling trade-offs |
| [[Virtualization Security and Case Studies - Review Drill]] | Virtualization Fundamentals, Hypervisors, OS Security Fundamentals, Access Control, Authentication and Protection, Malware and Defenses, Case Studies Overview, Linux Architecture Overview, Android Architecture, Windows NT Architecture | Type 1 vs 2; access-control models; Linux/Android/Windows distinctions |

---

## Mapping to the Canonical Wiki

The drill notes shadow the domain structure of the root [[CS Operating Systems]] MOC:

```
CS Operating Systems (root)
├── Processes and Threads    →  Processes and Scheduling - Review Drill
├── Memory Management        →  Memory Management - Review Drill
├── Synchronization          →  Synchronization and Deadlocks - Review Drill
├── Deadlocks                →  Synchronization and Deadlocks - Review Drill
├── File Systems             →  File Systems and IO - Review Drill
├── Input/Output             →  File Systems and IO - Review Drill
├── Virtualization           →  Virtualization Security and Case Studies - Review Drill
├── Security                 →  Virtualization Security and Case Studies - Review Drill
└── Case Studies             →  Virtualization Security and Case Studies - Review Drill
```

Note: Synchronization and Deadlocks share a drill note because they are tightly coupled in practice (deadlock arises from synchronisation design). File Systems and I/O share a drill note because the I/O stack feeds directly into file system implementation.

---

## Session Patterns

| Goal | Pattern |
|------|---------|
| Full domain review | Open one drill note; answer all Core Recall questions cold |
| Quick refresh | Open index; pick 3 questions from two different drill notes |
| Exam sweep | Work through all Compare and Contrast sections across all notes |
| Gap-finding | Focus on any question where you cannot state the answer in one sentence |
| Cross-course synthesis | Compare OS scheduling with Algorithms complexity analysis |

---

## Notes

- Content is distilled from the `_chunks/` layer and canonical wiki pages; go there for derivations and full explanations.
- These notes are intentionally concise — the goal is retrieval, not re-explanation.
- Update drill notes when canonical pages are substantially deepened.
