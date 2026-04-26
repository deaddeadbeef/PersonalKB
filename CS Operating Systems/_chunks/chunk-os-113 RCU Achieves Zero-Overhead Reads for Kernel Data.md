---
id: chunk-csos-113
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 8 — Multiprocessor and SMP Systems"
topic: "multiprocessor"
claim: "Read-Copy-Update (RCU) achieves zero-overhead reads for read-heavy kernel data structures: readers proceed without locks, writers create modified copies and atomically swap pointers, old versions are reclaimed after all pre-existing readers complete"
confidence: verified
supports:
  - "[[Multiprocessor Systems]]"
  - "[[Synchronization Overview]]"
tags:
  - csos
  - csos/multiprocessor
  - chunk
up: "[[CS Operating Systems]]"
---
# Multiprocessor — RCU achieves zero-overhead reads for read-heavy data structures

## Context

Traditional locking serializes all access — even concurrent readers must acquire shared locks. RCU exploits the insight that in many kernel data structures (routing tables, module lists), reads vastly outnumber writes. Under RCU, readers access data without any synchronization — they simply dereference pointers. Writers create a modified copy of the data, atomically swap the pointer to the new version, and defer freeing the old version until all pre-existing readers (who might still hold references) have finished — detected via a "grace period" tied to context switches on all CPUs.

## Why It Matters

RCU is one of the most impactful synchronization innovations in Linux, used thousands of times throughout the kernel. It demonstrates that by constraining the problem (read-dominated workloads, pointer-based data structures), you can achieve dramatically better performance than general-purpose locking. The technique also appears in user-space systems like QSBR (quiescent-state-based reclamation) in databases.

## QnA Seeds

- Q: Why can RCU readers proceed without any locks or atomic operations?
- Q: How does RCU determine when it is safe to free an old data version?
- Q: What constraint on workload makes RCU appropriate?
