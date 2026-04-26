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
# Deadlock Detection and Recovery

## 🎯 Intuition

**The Core Idea:** Detection lets deadlock occur, then checks for it and recovers after the fact. This trades lower upfront cost for potentially expensive cleanup.

**Analogy:** Instead of installing guards to stop every possible traffic jam, you send tow trucks only when a gridlock actually happens.

**Why It Matters:** Detection and recovery can be cheaper than strict prevention when deadlocks are rare, but the system must be ready to identify victims and undo work.

## ⚙️ Core Mechanics

### Detection with a Single Instance per Resource Type

Use the resource-allocation graph. The OS periodically runs a cycle-detection algorithm:
- A cycle means deadlock is present.
- Time complexity is **$O(n²)$** for `n` processes.

### Detection with Multiple Instances per Resource Type

Use a detection algorithm similar to Banker's safety test:

1. Maintain `Available`, `Allocation`, and `Request`.
2. Mark all processes as **unfinished**.
3. Find an unfinished process `P` whose `Request ≤ Available`.
4. Simulate completion: add `P`'s allocation to `Available`; mark `P` finished.
5. Repeat until no progress is possible. Any unfinished processes are **deadlocked**.

### When to Run Detection

- **Every denied request:** immediate detection, but high overhead.
- **Periodically:** lower overhead, but deadlock can persist until the next check.
- **When CPU utilisation drops below a threshold:** pragmatic heuristic.

### Recovery Options

#### Process Termination

- Abort all deadlocked processes: simple, but expensive.
- Abort one process at a time and re-run detection until the deadlock disappears.

Victim choice often considers least progress, least priority, or most resources held.

#### Resource Preemption

- Take a resource from one process and give it to another.
- Use **rollback** or checkpointing so the victim can restart safely.
- Beware **starvation** if the same process is repeatedly chosen as victim.

## 🔬 Deep Dive

### Why Detection Is Attractive

Detection avoids the constant restrictions of prevention and the constant safety checks of avoidance. This makes it appealing when deadlocks are uncommon enough that occasional recovery is cheaper than permanent caution.

### Single- vs. Multiple-Instance Detection

With **single-instance** resource types, a cycle in the resource-allocation graph is enough. With **multiple-instance** resources, graph cycles alone are not sufficient, so the OS needs the matrix-based detection procedure to determine which processes are truly stuck.

### Recovery Trade-Offs and Risks

- **Abort all** is easy but can waste large amounts of computation.
- **Abort incrementally** reduces lost work but needs repeated detection passes.
- **Preemption** may require checkpointing support.
- Poor victim choice can cause **starvation**, especially if the system always sacrifices the same kind of process.

## 🏋️ Practice

### Warm-Up

- Compare the cost of running detection on every request versus periodically.

### Core Problems

- Given `Allocation` and `Request` matrices, which processes are deadlocked?

### Challenge

- A system always picks the youngest process as the victim during recovery. What problem can arise?

## Supporting Chunks

- [[Deadlocks - Resource-allocation graph cycles indicate potential deadlock]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 6.
