---
id: chunk-csos-209
type: chunk
source: "[[raw-os-040]]"
source_loc: "Kernel Synchronization Primitives"
topic: "synchronization"
claim: "Kernel mutexes put contending threads to sleep instead of spinning, saving CPU cycles for long critical sections but cannot be used in interrupt context where sleeping is forbidden"
confidence: verified
supports:
  - "[[Kernel Synchronization]]"
tags:
  - csos
  - csos/synchronization
  - chunk
up: "[[CS Operating Systems]]"
---
# Synchronization — Kernel mutexes sleep instead of spin

## Context

Linux struct mutex is a sleeping lock: if held, the waiter is put to sleep and woken on release. This is more efficient than spinlocks for long critical sections (no wasted CPU cycles) but forbidden in interrupt context since interrupt handlers cannot sleep. Mutexes enforce strict ownership — only the holder can release. Reader-writer variants (rw_semaphore) allow concurrent readers but can cause writer starvation.

## Why It Matters

The spinlock-vs-mutex choice is the most frequent synchronization decision in kernel development. Understanding the sleep-vs-spin tradeoff and the interrupt-context constraint explains the kernel rich set of synchronization primitives and when each is appropriate.

## QnA Seeds

- Q: When should a kernel developer choose a mutex over a spinlock?
- Q: Why cannot mutexes be used in interrupt handlers?
- Q: What ownership rule distinguishes mutexes from semaphores?
