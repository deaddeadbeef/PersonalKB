---
tags:
  - csos
  - query
up: "[[CS Operating Systems/_queries/QnA System Roadmap|QnA System Roadmap]]"
---
# QnA — Chunk Coverage Map

## Purpose

See which canonical wiki notes have supporting chunks and which still have gaps. Use this to identify where the evidence base needs strengthening.

## Dataview Query (Optional)

> [!info] Requires the Dataview plugin. If not installed, use the manual approach below.

**Chunks grouped by the wiki notes they support:**

```dataview
TABLE rows.claim AS "Supporting Claims", rows.confidence AS "Confidence"
FROM "CS Operating Systems/_chunks"
FLATTEN supports AS supported_note
GROUP BY supported_note
```

**All chunks by topic:**

```dataview
TABLE claim, confidence, source
FROM "CS Operating Systems/_chunks"
WHERE type = "chunk"
SORT topic ASC, claim ASC
```

## Manual Search Fallback

**Find all chunks supporting a specific wiki note:**
1. Open the wiki note (e.g., [[Deadlock Fundamentals]]).
2. Open the backlinks pane — all chunk notes linking to it appear there.

**Find all chunks by topic:**
```
path:"CS Operating Systems/_chunks" topic: deadlocks
```

## Current Coverage

Current (post consistency-patch sync):

| Wiki Note | Chunk Count |
|-----------|-------------|
| [[OS Fundamentals]] | 3 |
| [[System Calls]] | 2 |
| [[OS Structure]] | 4 |
| [[Process Model]] | 2 |
| [[Process States and Transitions]] | 1 |
| [[Threads and Multithreading]] | 1 |
| [[CPU Scheduling]] | 1 |
| [[Interprocess Communication]] | 2 |
| [[Race Conditions and Mutual Exclusion]] | 2 |
| [[Semaphores]] | 2 |
| [[Monitors and Condition Variables]] | 1 |
| [[Classic Synchronization Problems]] | 2 |
| [[Address Spaces]] | 2 |
| [[Virtual Memory and Paging]] | 2 |
| [[Page Replacement Algorithms]] | 2 |
| [[Segmentation]] | 1 |
| [[File System Fundamentals]] | 2 |
| [[Directory Structures]] | 1 |
| [[File System Implementation]] | 3 |
| [[Journaling File Systems]] | 1 |
| [[IO Hardware Fundamentals]] | 2 |
| [[Interrupts and DMA]] | 2 |
| [[IO Software Layers]] | 2 |
| [[Device Drivers]] | 1 |
| [[Disk Scheduling Algorithms]] | 1 |
| [[Deadlock Fundamentals]] | 3 |
| [[Deadlock Detection and Recovery]] | 1 |
| [[Deadlock Avoidance]] | 1 |
| [[Deadlock Prevention]] | 2 |
| [[Virtualization Fundamentals]] | 3 |
| [[Hypervisors]] | 2 |
| [[Multiprocessor Systems]] | 3 |
| [[Distributed Systems Overview]] | 1 |
| [[OS Security Fundamentals]] | 2 |
| [[Access Control]] | 1 |
| [[Authentication and Protection]] | 1 |
| [[Malware and Defenses]] | 2 |
| [[Linux Architecture Overview]] | 2 |
| [[Android Architecture]] | 1 |
| [[Windows NT Architecture]] | 2 |
| [[OS Design Principles]] | 2 |
| [[Mechanism vs Policy]] | 1 |

**All 42 canonical wiki pages have at least one supporting chunk.**

**Pages at minimum coverage (1 chunk):** Process States and Transitions, Threads and Multithreading, CPU Scheduling, Monitors and Condition Variables, Segmentation, Directory Structures, Journaling File Systems, Device Drivers, Disk Scheduling Algorithms, Deadlock Detection and Recovery, Deadlock Avoidance, Distributed Systems Overview, Access Control, Authentication and Protection, Android Architecture, Mechanism vs Policy. Target: 2+ chunks per page in Phase 2.

## Notes

- Update this coverage map as new chunks are added.
- With Dataview installed, the table auto-updates; without it, maintain manually.
