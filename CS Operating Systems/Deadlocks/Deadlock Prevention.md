---
tags:
  - csos
  - csos/deadlocks
confidence: verified
up: "[[Deadlocks Overview]]"
tier-coverage:
  - intuition
  - core
  - deep-dive
  - practice
---
# Deadlock Prevention

## 🎯 Intuition

**The Core Idea:** Prevention eliminates deadlock by ensuring that at least one of the four Coffman conditions can **never** hold, making deadlock structurally impossible.

**Analogy:** Instead of waiting for a traffic jam to happen, you redesign the road rules so the bad traffic pattern cannot form at all.

**Why It Matters:** Prevention gives the strongest guarantee, but the price is usually lower utilisation, stricter programming rules, or both.

## ⚙️ Core Mechanics

### 1. Eliminate Mutual Exclusion

Make resources shareable. This works only for inherently shareable resources such as read-only files. Most hardware resources and write locks cannot be made shareable, so this approach has **limited applicability**.

### 2. Eliminate Hold and Wait

Require each process to request *all* resources it will ever need before starting, and proceed only when all are granted simultaneously.

- **Pro:** no hold-and-wait, so no circular wait can form.
- **Cons:** processes must know maximum needs upfront; utilisation is low because resources may sit unused; starvation is possible for processes waiting on popular bundles.

Alternative: require a process to release all current resources before requesting new ones.

### 3. Allow Preemption

If a process cannot get a needed resource, the system may preempt resources from other processes.

- Works for resources whose state can be saved and restored, such as CPU registers or memory pages.
- Does **not** work well for side-effect resources such as printers in mid-job or database locks in mid-transaction.

### 4. Eliminate Circular Wait (Resource Ordering)

Assign a global ordering to all resource types. Require processes to request resources in increasing order of their assigned numbers. If a process holds `Rᵢ`, it may request only `Rⱼ` where `j > i`.

This guarantees no circular wait can form, because the wait graph remains acyclic.

## 🔬 Deep Dive

### Why Prevention Works Structurally

Deadlock requires all four Coffman conditions. Prevention attacks the problem at the level of system rules: if one condition is permanently impossible, deadlock is permanently impossible too.

### Practical Limits of Each Strategy

- **Mutual exclusion:** rarely removable because many real resources are inherently non-shareable.
- **Hold and wait:** safe but inefficient, since resources may be reserved long before use.
- **Preemption:** depends on whether the resource can be cleanly taken away and restored later.
- **Resource ordering:** often the most practical method, especially in kernels and concurrent libraries.

### Why Resource Ordering Is Widely Used

Global lock ordering is popular because it is simple to state and easy to verify locally: always acquire lower-numbered resources before higher-numbered ones. The main drawback is enforcement discipline, especially in large codebases with many contributors and nested locking paths.

## 🏋️ Practice

### Warm-Up

- Why can't mutual exclusion be eliminated for a printer?

### Core Problems

- Process `P` holds `R5` and requests `R3` under resource ordering. What happens?

### Challenge

- Design a hold-and-wait prevention policy for a database. What benefit does it give, and what cost does it impose?

## Supporting Chunks

- [[Deadlocks - Deadlock requires all four Coffman conditions to hold simultaneously]]
- [[Deadlocks - Prevention eliminates deadlock by attacking one Coffman condition structurally]]

## See Also

- [[Classic Synchronization Problems]] — the asymmetric-ordering dining philosophers solution is resource-ordering prevention in action
- [[Semaphores]] — lock ordering discipline prevents deadlock from nested semaphore acquisitions
- [[Multiprocessor Systems]] — kernel lock ordering is critical on SMP systems with fine-grained locks
- [[Race Conditions and Mutual Exclusion]] — eliminating mutual exclusion (Coffman condition 1) is one prevention strategy

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 6.
