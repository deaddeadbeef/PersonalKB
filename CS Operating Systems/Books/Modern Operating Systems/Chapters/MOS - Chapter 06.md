---
id: mos-ch-06
type: book-chapter
chapter: 6
book: "Modern Operating Systems"
author: "Andrew S. Tanenbaum"
status: seeded
chunk_count: 4
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
tags:
  - csos
  - book-chapter
up: "[[Chapter Index]]"
confidence: verified
---
# MOS — Chapter 06: Deadlocks

## Summary

Deadlock is a state where each member of a group of processes waits indefinitely for a resource held by another member. Coffman (1971) identified four necessary and sufficient conditions that must all hold for deadlock to occur: mutual exclusion, hold-and-wait, no preemption, and circular wait. Tanenbaum develops resource-allocation graphs as a visual detection tool. Three main strategies are covered: deadlock prevention (statically eliminate at least one condition), deadlock avoidance (dynamically refuse resource grants that would lead to unsafe states — exemplified by the Banker's Algorithm), and deadlock detection and recovery (allow deadlock, detect it periodically, then recover by preemption or process termination). The chapter includes a critique: most real systems simply ignore deadlock (the "ostrich algorithm"), treating it as too rare and complex to justify the overhead.

## Key Concepts

| Concept | One-liner |
|---------|-----------|
| Coffman conditions | Four conditions that must all hold for deadlock: ME, H&W, NP, CW |
| Resource-allocation graph | Directed graph; cycle implies possible deadlock |
| Safe state | OS can always find an execution order that satisfies all processes |
| Banker's Algorithm | Avoidance: grant only if resulting state is safe |
| Preemption recovery | Take a resource from one process and give to another to break deadlock |

## Chunk Candidates

- [x] [[Deadlocks - Deadlock requires all four Coffman conditions to hold simultaneously]]
- [x] [[Deadlocks - Resource-allocation graph cycles indicate potential deadlock]]
- [x] [[Deadlocks - The Bankers Algorithm avoids deadlock by only granting resources in safe states]]
- [x] [[Deadlocks - Prevention eliminates deadlock by attacking one Coffman condition structurally]]

## Wiki Pages Seeded

- [[Deadlock Fundamentals]] — definition, Coffman conditions, resource-allocation graph
- [[Deadlock Detection and Recovery]] — detection algorithms, recovery strategies
- [[Deadlock Avoidance]] — Banker's Algorithm, safe vs unsafe states
- [[Deadlock Prevention]] — attacking each necessary condition

## References

See [[Sources Index#Tanenbaum 2015]].
