---
tags:
  - csos
  - moc
up: "[[CS Operating Systems]]"
---
# Processes Overview

How operating systems create, manage, schedule, and communicate between running programs. Covers the process abstraction, thread models, scheduling algorithms, and the mechanisms programs use to talk to one another.

---

## Learn in This Order

1. [[Process Model]] — process concept; PCB; address space; creation and termination
2. [[Process States and Transitions]] — running/ready/blocked lifecycle; scheduler trigger points
3. [[Threads and Multithreading]] — user-space vs kernel-space threads; why threads share address space
4. [[CPU Scheduling]] — FCFS, SJF, round-robin, priority, multilevel queues; preemption
5. [[Interprocess Communication]] — shared memory, pipes, message passing, signals; coupling trade-offs

---

## In This Domain

| Page | One-line summary |
|------|-----------------|
| [[Process Model]] | Process abstraction; PCB; address space; fork/exec lifecycle |
| [[Process States and Transitions]] | Running/ready/blocked state machine; scheduler role |
| [[Threads and Multithreading]] | User-space vs kernel threads; benefits and pitfalls |
| [[CPU Scheduling]] | Scheduling algorithms; quantum; preemption; fairness vs throughput |
| [[Interprocess Communication]] | IPC mechanisms; shared memory vs message passing; pipes |

---

## Common Distinctions

| Question | Answer |
|----------|--------|
| Process vs thread? | A process has its own address space. Threads within a process share the address space but have independent stacks and registers. Threads are cheaper to create and switch. |
| Preemptive vs cooperative scheduling? | Preemptive = OS can interrupt a running process (via timer interrupt). Cooperative = process voluntarily yields. Modern OSes are preemptive. |
| User-space vs kernel-space threads? | User-space threads are managed by a library (fast context switch, no kernel call). Kernel threads are scheduled by the OS (slower but block independently). |

---

## How to Navigate

- **Understanding process basics?** [[Process Model]] → [[Process States and Transitions]]
- **Thread design question?** [[Threads and Multithreading]]
- **Scheduling a system?** [[CPU Scheduling]] has the algorithm comparison
- **Processes communicating?** [[Interprocess Communication]]

---

## See Also

- [[Virtual Memory and Paging]] — paging gives each process an isolated address space and enables demand-loaded memory
- [[Race Conditions and Mutual Exclusion]] — threads sharing an address space need mutual exclusion to avoid data races
- [[Deadlock Fundamentals]] — processes that hold and wait on shared resources can deadlock
- [[System Calls]] — fork, exec, wait, and exit are the system-call interface to the process lifecycle

---

## Related Domains

- **[[Synchronization Overview]]** — once processes/threads share resources, you need synchronization to avoid race conditions.
- **[[OS Foundations Overview]]** — the OS structure and system-call mechanism underpin everything in this domain.
- **[[Deadlocks Overview]]** — blocking on shared resources (covered in Processes) can lead to deadlock.
