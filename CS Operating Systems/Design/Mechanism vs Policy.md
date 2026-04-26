---
tags:
  - csos
  - csos/design
confidence: verified
up: "[[Design Principles Overview]]"
tier-coverage: [intuition, core, deep-dive, practice]
---
# Mechanism vs Policy

## 🎯 Intuition
**The Core Idea:** The **mechanism vs policy separation** is the most cited design principle in operating systems. It was articulated explicitly by the HYDRA OS team (Wulf et al., 1974) and remains the gold standard for OS architecture.

**Analogy:** A car engine provides the ability to move the car, but it does not decide where to drive. The driver chooses the route. The engine is the mechanism; the driver is the policy.

**Why It Matters:** Separate “what the system can do” from “when and how it should do it” so policies can evolve for different workloads or users without rewriting the underlying engine.

## ⚙️ Core Mechanics
### The Principle
**Mechanism** answers: *what can the system do?*  
**Policy** answers: *when and how should it do it?*

Keep them in separate components so that policy can be changed — for different workloads, user classes, or domains — without modifying the mechanism.

### Classic Examples
#### Scheduling
**Mechanism:** context switching — the OS can save and restore CPU state, and assign any runnable thread to any CPU core.  
**Policy:** which thread runs next — FCFS, SJF, round-robin, CFS, real-time priority. Changing the scheduler does not require rewriting the context-switch code.

#### Memory Management
**Mechanism:** page fault handler and page replacement infrastructure — the OS can evict any page, write it to swap, and load any page from swap.  
**Policy:** which page to evict — LRU, clock, random. Swap space size. NUMA placement preference. These are policy decisions layered on top of the page-fault mechanism.

#### Access Control
**Mechanism:** the security reference monitor checks every object access against a policy database.  
**Policy:** who gets what rights — DAC, MAC (Bell-LaPadula), RBAC, SELinux type enforcement. All use the same check mechanism.

## 🔬 Deep Dive
### Why the Separation Matters
Without this separation, the OS bakes policy in. Changing the scheduler or page replacement algorithm requires modifying kernel mechanisms — risky, error-prone, and forces a one-size-fits-all approach. With the separation, microkernels can export mechanisms to user-space policy servers; Linux's pluggable schedulers (CFS, SCHED_DEADLINE) exemplify this even in a monolithic kernel.

### Tension and Pragmatic Compromises
Full separation can impose IPC overhead in the microkernel case. Real systems make pragmatic compromises: some policy (default scheduler, default page replacement) lives near the mechanism for performance, but hooks allow override. The principle is still valuable as a design goal even when pure separation is impractical.

## 🏋️ Practice
### Warm-Up
1. In one sentence, what is the difference between mechanism and policy?
2. Which historical OS project is most associated with this principle?
3. Why is this principle considered so important in OS design?

### Core Problems
1. Identify the mechanism and the policy in Linux page replacement.
2. For scheduling, explain why changing FCFS to round-robin is a policy change rather than a mechanism change.
3. In access control, what stays constant when moving from DAC to RBAC or MAC?

### Challenge
1. Why might pure mechanism/policy separation hurt performance in a microkernel?
2. Give an example of a system that bakes policy into mechanism and explain the consequences.
3. Explain why Linux's pluggable schedulers are a strong example of this principle even though Linux is not a microkernel.

## Supporting Chunks

- [[Design - Separating mechanism from policy lets policy evolve without rewriting mechanisms]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 12.
