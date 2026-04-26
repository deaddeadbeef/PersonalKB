---
id: chunk-csos-208
type: chunk
source: "[[raw-os-040]]"
source_loc: "Kernel Synchronization Primitives"
topic: "synchronization"
claim: "RCU allows lock-free reads with zero overhead and defers memory reclamation until all pre-existing readers complete a grace period, enabling massive read scalability"
confidence: verified
supports:
  - "[[Kernel Synchronization]]"
tags:
  - csos
  - csos/synchronization
  - chunk
up: "[[CS Operating Systems]]"
---
# Synchronization — RCU achieves zero-overhead lock-free reads

## Context

Read-Copy-Update (RCU) lets readers access data without any lock — rcu_read_lock() simply disables preemption. Writers create a modified copy, atomically update the pointer, then defer freeing the old version until all pre-existing readers complete (grace period, detected when each CPU passes through a quiescent state). Over 100,000 RCU uses exist in the Linux 6.x kernel, including routing tables, dcache, and PID hash.

## Why It Matters

RCU is arguably the most important kernel concurrency innovation, enabling Linux to scale to hundreds of CPUs for read-mostly data structures. Understanding RCU read-side zero-overhead explains why it is preferred over reader-writer locks for the kernel most performance-critical paths.

## QnA Seeds

- Q: Why does RCU have zero read-side overhead?
- Q: What is an RCU grace period and how is it detected?
- Q: What kernel data structures are protected by RCU?
