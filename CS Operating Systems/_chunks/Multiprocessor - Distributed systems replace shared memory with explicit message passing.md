---
id: chunk-csos-042
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 8"
topic: "multiprocessor"
claim: "Distributed systems replace shared memory with explicit message passing, requiring software-level solutions for consistency, fault tolerance, and coordination that hardware provides transparently in shared-memory systems"
confidence: verified
supports:
  - "[[Distributed Systems Overview]]"
tags:
  - csos
  - csos/multiprocessor
  - chunk
up: "[[CS Operating Systems]]"
---
# Multiprocessor — Distributed systems replace shared memory with explicit message passing

## Context

In a shared-memory multiprocessor, the hardware ensures that all cores see the same memory (via cache coherence). In a distributed system, there is no shared memory — each node has its own private RAM. To share state, nodes must explicitly send messages. This shifts the coordination burden entirely to software: distributed locks, consensus protocols (Paxos, Raft), and distributed transactions must be implemented without hardware assistance. Partial failure (one node crashes while others continue) has no analogue in shared-memory systems.

## Why It Matters

Distributed systems are the architecture of all large-scale internet services (cloud databases, microservices, peer-to-peer systems). The lack of a global clock (Lamport clocks, vector clocks) and the CAP theorem (choose two: consistency, availability, partition-tolerance) are fundamental constraints that every distributed system designer must understand. Tanenbaum's treatment bridges the OS concepts of concurrency and IPC to distributed computing.

## QnA Seeds

- Q: Why can't distributed systems use the same mutual exclusion primitives as shared-memory systems?
- Q: What is the CAP theorem and what does it imply for distributed database design?
- Q: What is a Lamport clock and what problem does it address?
