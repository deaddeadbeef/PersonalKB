---
id: chunk-csos-130
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 10 — Real-Time Operating Systems"
topic: "scheduling"
claim: "Priority inversion occurs when a high-priority task is blocked by a low-priority resource holder while medium-priority tasks preempt the holder; the priority inheritance protocol solves this by temporarily boosting the holder's priority"
confidence: verified
supports:
  - "[[CPU Scheduling]]"
  - "[[Classic Synchronization Problems]]"
tags:
  - csos
  - csos/scheduling
  - csos/synchronization
  - chunk
up: "[[CS Operating Systems]]"
---
# Scheduling — Priority inversion blocks high-priority tasks behind lower-priority holders

## Context

Priority inversion is a scheduling pathology where a high-priority task H is blocked waiting for a resource held by a low-priority task L, while medium-priority tasks M preempt L — effectively making H wait for M, inverting the priority hierarchy. The Mars Pathfinder incident (1997) is the canonical real-world case: a low-priority meteorological task held a mutex needed by a high-priority bus management task, while medium-priority communication tasks preempted the meteorological task, causing repeated watchdog resets. The priority inheritance protocol temporarily raises L's priority to H's while L holds the resource. The priority ceiling protocol goes further — raising L's priority to the highest of any task that may use the resource when the lock is acquired, preventing deadlock entirely.

## Why It Matters

Priority inversion is the most insidious real-time correctness threat because it can survive extensive testing and manifest only under specific runtime timing conditions. The Mars Pathfinder fix (enabling priority inheritance remotely from Earth) is both a teaching example and a testament to the importance of building recovery mechanisms into deployed systems.

## QnA Seeds

- Q: Describe the three-task scenario that causes priority inversion.
- Q: How did priority inversion manifest in the Mars Pathfinder mission?
- Q: What is the difference between priority inheritance and priority ceiling protocols?
