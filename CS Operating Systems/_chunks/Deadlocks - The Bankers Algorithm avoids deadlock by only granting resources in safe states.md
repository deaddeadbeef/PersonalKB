---
id: chunk-csos-034
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 6"
topic: "deadlocks"
claim: "The Banker's Algorithm avoids deadlock by only granting resource requests that leave the system in a safe state — one from which a safe execution order exists for all processes"
confidence: verified
supports:
  - "[[Deadlock Avoidance]]"
tags:
  - csos
  - csos/deadlocks
  - chunk
up: "[[CS Operating Systems]]"
---
# Deadlocks — The Bankers Algorithm avoids deadlock by only granting resources in safe states

## Context

Dijkstra modelled the OS as a banker who must not loan resources in a way that could leave it unable to satisfy future requests. The safety test simulates completing processes one at a time: if a process's remaining needs can be satisfied by current available resources, simulate its completion and reclaim its allocation; repeat. If all processes can eventually complete, the state is safe. On every resource grant request, the OS tentatively allocates, runs the safety test, and commits only if safe — otherwise it blocks the requesting process.

## Why It Matters

The Banker's Algorithm proves that deadlock avoidance is theoretically solvable. In practice it is rarely used in general-purpose OSes (it requires upfront declaration of maximum needs and has O(n²m) overhead per request), but it is directly applicable in real-time systems with predictable resource profiles (avionics, industrial control). Understanding it is required for OS exams and for reasoning about any resource allocation system.

## QnA Seeds

- Q: What makes a state "safe" in the Banker's Algorithm?
- Q: What are the practical limitations of the Banker's Algorithm for general-purpose OSes?
- Q: Walk through the safety test algorithm step by step.
