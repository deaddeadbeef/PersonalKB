---
tags:
  - csos
  - csos/deadlocks
confidence: verified
freshness: stable
up: "[[Deadlocks Overview]]"
tier-coverage:
  - intuition
  - core
  - deep-dive
  - practice
---
# Deadlock Avoidance

## 🎯 Intuition

**The Core Idea:** Avoidance examines every resource request before approving it. The OS denies a request if granting it would move the system into an **unsafe state**.

**Analogy:** A cautious banker approves a loan only if enough reserves remain for every customer to eventually be paid back.

**Why It Matters:** Avoidance is more flexible than prevention because it does not ban dangerous patterns outright. Instead, it uses runtime checks to stay out of states from which deadlock could happen.

## ⚙️ Core Mechanics

### Safe State vs. Unsafe State

A state is **safe** if there exists at least one execution order, called a **safe sequence**, in which every process can complete using currently available resources plus resources released by earlier completions.

An **unsafe state** does **not** guarantee deadlock. It means deadlock is possible if future requests arrive badly. Avoidance keeps the system in safe states only.

### The Banker's Algorithm (Dijkstra, 1965)

Developed for loan allocation, the Banker's Algorithm applies directly to OS resource management.

### Data Structures

- `Available[m]` — vector of available instances per resource type
- `Max[n][m]` — maximum demand of each process
- `Allocation[n][m]` — resources currently held by each process
- `Need[n][m]` = `Max − Allocation` — remaining needs

### Safety Test

1. `Work = Available`, `Finish[i] = false` for all i.
2. Find i such that `Finish[i] = false` AND `Need[i] ≤ Work`.
3. `Work = Work + Allocation[i]`, `Finish[i] = true`.
4. Repeat. If all `Finish[i]` become true → safe.

### Resource-Request Algorithm

1. If `Request[i] ≤ Need[i]` — otherwise error.
2. If `Request[i] ≤ Available` — else wait.
3. Tentatively allocate: subtract from `Available`, add to `Allocation[i]`, reduce `Need[i]`.
4. Run safety test. If safe → commit. If unsafe → rollback and block process.

## 🔬 Deep Dive

### Why Unsafe Does Not Mean Deadlocked

In an unsafe state, the system has lost its guarantee that all processes can finish in some order. But a fortunate order of future releases may still avoid deadlock. Deadlock is therefore a **subset** of unsafe states, not the same thing.

### Cost of the Safety Test

The safety procedure repeatedly scans for a process whose remaining need can be satisfied by current `Work`. In standard analysis, this adds overhead of **$O(n²m)$**, where `n` is the number of processes and `m` is the number of resource types.

### Practical Limitations

- Processes must declare maximum resource needs upfront, which is often unrealistic.
- The algorithm assumes fixed numbers of processes and resource instances.
- Every request may require a nontrivial safety check.
- Because of this overhead and rigidity, it is rarely used in general-purpose operating systems, though it can fit predictable real-time systems.

## 🏋️ Practice

### Warm-Up

- What is the time complexity of the Banker's safety algorithm?

### Core Problems

- Given `Available = [3,3,2]` and specific `Max` and `Allocation` matrices, determine whether the state is safe.

### Challenge

- Why is Banker's Algorithm impractical for a web server?

## Supporting Chunks

- [[Deadlocks - The Bankers Algorithm avoids deadlock by only granting resources in safe states]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 6.
