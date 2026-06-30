---
tags:
  - csos
  - moc
up: "[[CS Operating Systems]]"
confidence: verified
---
# Synchronization Overview

When multiple processes or threads share resources, correct behavior requires coordination. This domain covers the critical-section problem, classic primitives (semaphores, monitors), and the canonical problems that reveal synchronization subtleties.

---

## Learn in This Order

1. [[Race Conditions and Mutual Exclusion]] — critical sections; Peterson's solution; hardware test-and-set
2. [[Semaphores]] — binary and counting semaphores; P/V operations; mutual exclusion and signalling
3. [[Monitors and Condition Variables]] — high-level structured synchronization; Mesa vs Hoare semantics
4. [[Classic Synchronization Problems]] — producer-consumer; readers-writers; dining philosophers

---

## In This Domain

| Page | One-line summary |
|------|-----------------|
| [[Race Conditions and Mutual Exclusion]] | Critical sections; Peterson; test-and-set; spinlocks |
| [[Semaphores]] | Binary/counting semaphores; P/V; implementation |
| [[Monitors and Condition Variables]] | Language-level synchronization; wait/signal/broadcast |
| [[Classic Synchronization Problems]] | Producer-consumer, readers-writers, dining philosophers |

---

## Common Distinctions

| Question | Answer |
|----------|--------|
| Mutex vs semaphore? | A mutex (binary semaphore with ownership) is for mutual exclusion. A counting semaphore can also be used for signalling and resource counting. |
| Mesa vs Hoare monitors? | Mesa (used in Java, pthreads): `signal` wakes a waiter but doesn't immediately yield — waiter must re-check condition. Hoare: signaller immediately hands off CPU. Mesa is simpler and more common. |
| Busy-waiting vs blocking? | Spinlock = busy-wait (wastes CPU but low latency). Semaphore = blocks (frees CPU but has wake-up overhead). Use spinlocks for very short critical sections on multiprocessors. |

---

## How to Navigate

- **First encounter with concurrency bugs?** Start at [[Race Conditions and Mutual Exclusion]] to understand the problem before solutions.
- **Need a specific primitive?** → semaphores for low-level; monitors for structured high-level.
- **Classic interview/exam problems?** [[Classic Synchronization Problems]] covers the standard trio.

---

## Related Domains

- **[[Processes Overview]]** — synchronization is needed because processes and threads share resources; the threading model is defined there.
- **[[Deadlocks Overview]]** — improper synchronization (circular wait on locked resources) causes deadlock; the two domains are tightly coupled.

## References
- [[CS Operating Systems/Sources/Sources Index|CS Operating Systems Sources Index]]
