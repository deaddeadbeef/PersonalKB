---
id: chunk-csos-193
type: chunk
source: "[[raw-os-036]]"
source_loc: "Concurrency Bugs and Detection"
topic: "synchronization"
claim: "Lock ordering discipline prevents deadlocks by requiring all threads to acquire locks in a globally consistent order, eliminating the possibility of circular wait"
confidence: verified
supports:
  - "[[Concurrency Bugs]]"
tags:
  - csos
  - csos/synchronization
  - chunk
up: "[[CS Operating Systems]]"
---
# Synchronization — Lock ordering prevents deadlock circular wait

## Context

Deadlocks arise when threads hold locks and circularly wait for each other. If all threads always acquire locks in the same global order, circular wait is impossible. Helgrind detects violations by tracking lock acquisition order across threads and reporting if two threads acquire the same lock pair in different orders. Alternatives include trylock with backoff and lock-free data structures using CAS.

## Why It Matters

Lock ordering is the most practical deadlock prevention strategy in real systems. Understanding it explains Linux kernel lock documentation, database lock hierarchies, and why static analysis tools that check lock ordering catch real bugs.

## QnA Seeds

- Q: How does consistent lock ordering prevent deadlock?
- Q: How does Helgrind detect potential deadlocks?
- Q: What alternatives to lock ordering exist for deadlock prevention?
