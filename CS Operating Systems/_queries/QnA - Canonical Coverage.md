---
tags:
  - csos
  - query
up: "[[CS Operating Systems/_queries/QnA System Roadmap|QnA System Roadmap]]"
---
# QnA — Canonical Coverage

## Purpose

Verify that every canonical OS topic in the architect's plan has a corresponding wiki page, and identify any topic domains that need additional pages.

## Dataview Query (Optional)

> [!info] Requires the Dataview plugin. If not installed, use the manual table below.

```dataview
TABLE file.folder AS "Domain", confidence
FROM "CS Operating Systems"
WHERE type != "chunk" AND type != "raw" AND type != "template" AND type != "book-chapter"
SORT file.folder ASC, file.name ASC
```

## Manual Inventory

**Foundations (3 pages)**
- [x] [[OS Fundamentals]]
- [x] [[System Calls]]
- [x] [[OS Structure]]

**Processes (5 pages)**
- [x] [[Process Model]]
- [x] [[Process States and Transitions]]
- [x] [[Threads and Multithreading]]
- [x] [[CPU Scheduling]]
- [x] [[Interprocess Communication]]

**Synchronization (4 pages)**
- [x] [[Race Conditions and Mutual Exclusion]]
- [x] [[Semaphores]]
- [x] [[Monitors and Condition Variables]]
- [x] [[Classic Synchronization Problems]]

**Memory (4 pages)**
- [x] [[Address Spaces]]
- [x] [[Virtual Memory and Paging]]
- [x] [[Page Replacement Algorithms]]
- [x] [[Segmentation]]

**File Systems (4 pages)**
- [x] [[File System Fundamentals]]
- [x] [[Directory Structures]]
- [x] [[File System Implementation]]
- [x] [[Journaling File Systems]]

**IO (5 pages — 2 extra beyond base plan)**
- [x] [[IO Hardware Fundamentals]]
- [x] [[IO Software Layers]]
- [x] [[Disk Scheduling Algorithms]]
- [x] [[Interrupts and DMA]] ← additional page
- [x] [[Device Drivers]] ← additional page

**Deadlocks (4 pages)**
- [x] [[Deadlock Fundamentals]]
- [x] [[Deadlock Detection and Recovery]]
- [x] [[Deadlock Avoidance]]
- [x] [[Deadlock Prevention]]

**Virtualization (2 pages)**
- [x] [[Virtualization Fundamentals]]
- [x] [[Hypervisors]]

**Multiprocessor (2 pages)**
- [x] [[Multiprocessor Systems]]
- [x] [[Distributed Systems Overview]]

**Security (4 pages — 1 extra beyond base plan)**
- [x] [[OS Security Fundamentals]]
- [x] [[Access Control]]
- [x] [[Malware and Defenses]]
- [x] [[Authentication and Protection]] ← additional page

**Case Studies (3 pages — 1 extra beyond base plan)**
- [x] [[Linux Architecture Overview]]
- [x] [[Windows NT Architecture]]
- [x] [[Android Architecture]] ← additional page

**Design (2 pages)**
- [x] [[OS Design Principles]]
- [x] [[Mechanism vs Policy]]

---

## Summary

| Domain | Pages | Status |
|--------|-------|--------|
| Foundations | 3 | ✅ Complete |
| Processes | 5 | ✅ Complete |
| Synchronization | 4 | ✅ Complete |
| Memory | 4 | ✅ Complete |
| File Systems | 4 | ✅ Complete |
| IO | 5 | ✅ Complete (2 extra) |
| Deadlocks | 4 | ✅ Complete |
| Virtualization | 2 | ✅ Complete |
| Multiprocessor | 2 | ✅ Complete |
| Security | 4 | ✅ Complete (1 extra) |
| Case Studies | 3 | ✅ Complete (1 extra) |
| Design | 2 | ✅ Complete |
| **Total** | **42** | **✅ All covered** |

**All 42 canonical pages created. Base plan was 38; 4 additional pages added (Interrupts and DMA, Device Drivers, Authentication and Protection, Android Architecture).**

## Gaps to Address in Phase 2

- `POSIX Threading Model` — threads API details (pthread_create, mutex, cond_var)
- `NVMe and Modern Storage` — SSD I/O model, queue depth, NVMe over Fabrics
- `CFS — Completely Fair Scheduler` — red-black tree, vruntime, CFS groups
- `Copy-on-Write and Fork` — fork optimisation, COW page sharing
