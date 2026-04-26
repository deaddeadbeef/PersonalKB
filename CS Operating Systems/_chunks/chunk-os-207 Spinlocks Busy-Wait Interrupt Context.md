---
id: chunk-csos-207
type: chunk
source: "[[raw-os-040]]"
source_loc: "Kernel Synchronization Primitives"
topic: "synchronization"
claim: "Spinlocks are busy-wait locks appropriate for short critical sections in interrupt context where sleeping is forbidden, degenerating to preemption disabling on uniprocessor systems"
confidence: verified
supports:
  - "[[Kernel Synchronization]]"
tags:
  - csos
  - csos/synchronization
  - chunk
up: "[[CS Operating Systems]]"
---
# Synchronization — Spinlocks busy-wait for interrupt-safe locking

## Context

A spinlock makes the waiting thread loop until the lock is released, consuming CPU cycles. This is appropriate for short hold times in interrupt handlers where sleeping is impossible. spin_lock_irqsave() disables local interrupts to prevent deadlock when an interrupt handler tries to acquire the same lock. On uniprocessor kernels, spinlocks just disable preemption. Linux uses queued spinlocks (MCS-based since 3.15) for NUMA fairness.

## Why It Matters

Spinlocks are the most fundamental kernel synchronization primitive. Understanding when to use them (short, interrupt-safe) vs. mutexes (long, sleepable) is essential for kernel and driver development and explains why spin_lock_irqsave exists.

## QnA Seeds

- Q: Why are spinlocks used instead of sleeping locks in interrupt context?
- Q: What does spin_lock_irqsave() do beyond acquiring the lock?
- Q: Why do spinlocks degenerate to preemption disabling on uniprocessor systems?
