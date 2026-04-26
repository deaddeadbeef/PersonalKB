---
id: chunk-csos-104
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 2 — Inter-Process Communication"
topic: "processes"
claim: "Message passing via send/receive provides a cleaner abstraction than shared memory because the kernel handles synchronization and copying, eliminating the class of bugs caused by concurrent unsynchronized access to shared regions"
confidence: verified
supports:
  - "[[Interprocess Communication]]"
  - "[[Processes Overview]]"
tags:
  - csos
  - csos/processes
  - chunk
up: "[[CS Operating Systems]]"
---
# Processes — Message passing provides safety through kernel-mediated synchronization

## Context

Message passing IPC uses explicit send() and receive() operations where the kernel copies data between process address spaces. This is slower than shared memory (each exchange involves system calls and data copies) but safer — the kernel enforces synchronization implicitly, making race conditions on the communicated data impossible. Synchronous (blocking) message passing causes the sender to block until the receiver calls receive, creating a natural rendezvous point (used in Ada's concurrency model). Asynchronous message passing uses kernel-managed queues, decoupling sender and receiver timing.

## Why It Matters

Message passing naturally extends across network boundaries, making it the foundation for distributed systems (sockets, RPC, gRPC). The safety vs. performance tradeoff between shared memory and message passing is one of the most fundamental design decisions in system architecture — the same tension appears at every scale from threads to microservices.

## QnA Seeds

- Q: How does message passing eliminate race conditions that shared memory must handle manually?
- Q: What is a rendezvous in synchronous message passing?
- Q: Why does message passing naturally extend to distributed systems while shared memory does not?
