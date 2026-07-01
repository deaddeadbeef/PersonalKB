---
tags:
  - csos
  - moc
up: "[[CS Operating Systems]]"
confidence: established
freshness: stable
tier-coverage: [intuition, core]
---
# Deadlocks Overview

A deadlock occurs when a set of processes each hold a resource and wait for another held by another process in the set — a circular wait from which no process can escape without external intervention. This domain covers the four necessary conditions, and the three main strategies: prevention, avoidance, and detection-and-recovery.

---

## Learn in This Order

1. [[Deadlock Fundamentals]] — four Coffman conditions (mutual exclusion, hold-and-wait, no preemption, circular wait); resource-allocation graphs
2. [[Deadlock Prevention]] — attacking each condition; trade-offs and costs
3. [[Deadlock Avoidance]] — Banker's algorithm; safe vs unsafe state; conservative reservation
4. [[Deadlock Detection and Recovery]] — detection algorithms; recovery via preemption or process rollback

---

## In This Domain

| Page | One-line summary |
|------|-----------------|
| [[Deadlock Fundamentals]] | Four Coffman conditions; resource-allocation graph cycles |
| [[Deadlock Prevention]] | Eliminating one condition; trade-offs |
| [[Deadlock Avoidance]] | Banker's algorithm; safe-state guarantee |
| [[Deadlock Detection and Recovery]] | Cycle detection; preemption; rollback |

---

## Common Distinctions

| Question | Answer |
|----------|--------|
| Prevention vs avoidance vs detection? | Prevention = statically deny one Coffman condition (conservative). Avoidance = dynamically check safety before granting (Banker's). Detection = allow deadlocks, detect and recover (optimistic). |
| Safe state vs deadlock? | A safe state is one where the OS can schedule requests in some order that completes without deadlock. An unsafe state *may* lead to deadlock but doesn't guarantee it. |
| Deadlock vs starvation? | Deadlock = no process makes progress (circular wait). Starvation = one process makes no progress because others always get priority (not necessarily circular). |

---

## How to Navigate

- **Understanding deadlock for the first time?** [[Deadlock Fundamentals]] — the four conditions must *all* hold simultaneously.
- **OS or system design choice?** Understand all three strategies in [[Deadlock Prevention]], [[Deadlock Avoidance]], [[Deadlock Detection and Recovery]], then choose based on resource cost and risk tolerance.
- **Exam question on Banker's?** [[Deadlock Avoidance]]

---

## Related Domains

- **[[Synchronization Overview]]** — improper synchronization (acquiring locks in wrong order) is the typical *cause* of deadlock. Understand synchronization primitives before deadlock conditions.
- **[[Processes Overview]]** — deadlock involves competing processes; the resource-allocation context is established there.

## References

- [[CS Operating Systems/Sources/Sources Index]]
- [[CS Operating Systems/CS Operating Systems Book Reading Spine]]
