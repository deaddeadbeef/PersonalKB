---
tags:
  - csos
  - csos/multiprocessor
confidence: verified
up: "[[Multiprocessor Overview]]"
---
# Distributed Systems Overview

A **distributed system** is a collection of independent computers that communicate by passing messages over a network, appearing to users as a single coherent system. Unlike shared-memory multiprocessors, distributed nodes have *no* shared memory — all coordination must be explicit.

---

## Fundamental Differences from Shared Memory

| Aspect | Shared Memory | Distributed |
|--------|--------------|-------------|
| Communication | Load/store | Message passing (send/receive) |
| Failure model | Core fail = whole system fails | Nodes fail independently |
| Latency | Nanoseconds | Milliseconds (LAN) to seconds (WAN) |
| Consistency | Cache coherence hardware | Must be engineered in software |
| Synchronisation | Locks, semaphores | Distributed protocols (Paxos, Raft) |

---

## Key Challenges

- **Partial failure**: a node can fail while others continue — the system must tolerate this gracefully.
- **Network partition**: nodes cannot communicate even though they are running — is the other side dead or just slow?
- **Clock skew**: independent clocks drift; there is no global "now" in a distributed system (Lamport clocks, vector clocks).
- **Consistency vs availability trade-off** (CAP theorem): during a network partition, a system must choose between consistency (all nodes see the same data) and availability (every request gets a response).

---

## Communication Primitives

- **RPC (Remote Procedure Call)**: call a function on a remote machine as if it were local; transparency is the goal.
- **Message queues**: asynchronous, durable message delivery (Kafka, RabbitMQ).
- **Shared distributed storage**: NFS, HDFS, Ceph — file systems that span machines.

---

## Supporting Chunks

- [[Multiprocessor - Distributed systems replace shared memory with explicit message passing]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 8.
