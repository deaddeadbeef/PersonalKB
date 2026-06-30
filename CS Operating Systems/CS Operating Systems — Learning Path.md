---
tags: [csos, learning-path]
up: "[[CS Operating Systems/CS Operating Systems|CS Operating Systems]]"
confidence: policy
---
# CS Operating Systems — Learning Path

> A guided, progressive tour through operating-systems theory and practice. Four passes, each building on the last.

## How to Use This Path

| Pass | Focus | Read | Time |
|------|-------|------|------|
| 1 — Intuition | Build mental map | 🎯 sections only | ~2 hrs |
| 2 — Core | Understand mechanics | ⚙️ sections + Warm-Up | ~8 hrs |
| 3 — Deep Dive | Master details | 🔬 sections (selective) | ~15 hrs |
| 4 — Practice | Build skill | 🏋️ sections + drills | Ongoing |

---

## Pass 1 — Intuition (~2 hours)

Read ONLY the 🎯 Intuition section of each page. Build a broad mental map of how operating systems work before diving into any details.

### Foundations
1. [[OS Foundations Overview]] — what an OS is and why it exists
2. [[OS Fundamentals]] — kernel vs user space, privileged instructions
3. [[OS Structure]] — monolithic, microkernel, hybrid architectures
4. [[System Calls]] — the boundary between user programs and the kernel

### Processes
5. [[Processes Overview]] — the process abstraction hub
6. [[Process Model]] — what a process is, PCBs, creation and termination
7. [[Process States and Transitions]] — running, ready, blocked lifecycle
8. [[Threads and Multithreading]] — lightweight concurrency within a process
9. [[CPU Scheduling]] — how the OS decides who runs next
10. [[Interprocess Communication]] — pipes, shared memory, message passing

### Memory
11. [[Memory Management Overview]] — the memory abstraction hub
12. [[Address Spaces]] — logical vs physical addresses
13. [[Virtual Memory and Paging]] — page tables, TLBs, demand paging
14. [[Page Replacement Algorithms]] — FIFO, LRU, clock, working set
15. [[Segmentation]] — segment-based address translation

### Synchronization
16. [[Synchronization Overview]] — the concurrency-control hub
17. [[Race Conditions and Mutual Exclusion]] — why concurrent access breaks things
18. [[Semaphores]] — Dijkstra's counting primitive
19. [[Monitors and Condition Variables]] — structured synchronization
20. [[Classic Synchronization Problems]] — producer-consumer, readers-writers, dining philosophers

### Deadlocks
21. [[Deadlocks Overview]] — the deadlock hub
22. [[Deadlock Fundamentals]] — four Coffman conditions
23. [[Deadlock Prevention]] — deny one condition
24. [[Deadlock Avoidance]] — Banker's algorithm
25. [[Deadlock Detection and Recovery]] — detect cycles, recover

### File Systems
26. [[File Systems Overview]] — the file-systems hub
27. [[File System Fundamentals]] — files, metadata, operations
28. [[Directory Structures]] — naming, paths, directory implementations
29. [[File System Implementation]] — inodes, allocation, free-space management
30. [[Journaling File Systems]] — crash consistency and recovery

### I/O
31. [[IO Overview]] — the I/O hub
32. [[IO Hardware Fundamentals]] — controllers, buses, ports
33. [[Interrupts and DMA]] — interrupt handling and direct memory access
34. [[IO Software Layers]] — layers from user space to hardware
35. [[Device Drivers]] — driver model and interface
36. [[Disk Scheduling Algorithms]] — FCFS, SSTF, SCAN, C-SCAN

### Security
37. [[Security Overview]] — the security hub
38. [[OS Security Fundamentals]] — threat model, attack surface
39. [[Access Control]] — ACLs, capabilities, RBAC, MAC
40. [[Authentication and Protection]] — passwords, 2FA, protection domains
41. [[Malware and Defenses]] — viruses, worms, rootkits, ASLR, DEP

### Multiprocessor Systems
42. [[Multiprocessor Overview]] — the multiprocessor hub
43. [[Multiprocessor Systems]] — SMP, NUMA, cache coherence, scheduling
44. [[Distributed Systems Overview]] — when shared memory disappears

### Virtualization
45. [[Virtualization Overview]] — the virtualization hub
46. [[Virtualization Fundamentals]] — why virtualize, requirements
47. [[Hypervisors]] — type 1 vs type 2, trap-and-emulate, para-virtualization

### Design
48. [[Design Principles Overview]] — the design-philosophy hub
49. [[OS Design Principles]] — goals, trade-offs, simplicity
50. [[Mechanism vs Policy]] — separating what from how

### Case Studies
51. [[Case Studies Overview]] — the case-studies hub
52. [[Linux Architecture Overview]] — monolithic kernel, VFS, CFS
53. [[Android Architecture]] — Linux kernel + Binder + permissions sandbox
54. [[Windows NT Architecture]] — hybrid kernel, HAL, Registry

---

## Pass 2 — Core Mechanics (~8 hours)

Now re-read each page's ⚙️ Core Mechanics and 🏋️ Warm-Up sections. Focus on *how* things work, not just *what* they are.

### Suggested order
Follow the same sequence as Pass 1. Spend extra time on:
- **Process scheduling** — understand FCFS, SJF, Round Robin, priority, MLFQ
- **Virtual memory** — walk through a page-table lookup step by step
- **Synchronization primitives** — trace through semaphore P/V operations
- **Deadlock avoidance** — work through a Banker's algorithm example
- **File system implementation** — trace an inode-based file read
- **I/O interrupt flow** — follow an interrupt from hardware to handler

### Checkpoints
After this pass you should be able to:
- [ ] Draw the process state diagram from memory
- [ ] Explain how a TLB miss triggers a page-table walk
- [ ] Solve a Banker's algorithm safety check
- [ ] Describe the layers of I/O software
- [ ] Compare monolithic vs microkernel trade-offs

---

## Pass 3 — Deep Dive (selective, ~15 hours)

Read the 🔬 Deep Dive sections for areas you want to master. Recommended deep-dive tracks:

### Track A — Concurrency & Deadlocks
- [[Race Conditions and Mutual Exclusion]] — hardware support (TSL, XCHG)
- [[Semaphores]] — implementation details, binary vs counting
- [[Classic Synchronization Problems]] — formal solutions
- [[Deadlock Fundamentals]] — resource-allocation graphs
- [[Deadlock Avoidance]] — safety algorithm proofs

### Track B — Memory Subsystem
- [[Virtual Memory and Paging]] — multi-level page tables, inverted page tables
- [[Page Replacement Algorithms]] — Bélády's anomaly, working-set model
- [[Segmentation]] — segmentation with paging

### Track C — File Systems & Storage
- [[File System Implementation]] — log-structured FS, extent-based allocation
- [[Journaling File Systems]] — write-ahead logging, metadata vs full journaling
- [[Disk Scheduling Algorithms]] — deadline schedulers, SSDs vs HDDs

### Track D — Systems Architecture
- [[Hypervisors]] — binary translation, shadow page tables, EPT/NPT
- [[Multiprocessor Systems]] — MESI protocol, affinity scheduling
- [[Linux Architecture Overview]] — kernel subsystems deep dive

---

## Pass 4 — Practice (ongoing)

Build active-recall skill through drills and applied exercises.

### Drills
- [[Processes and Scheduling - Review Drill]]
- [[Memory Management - Review Drill]]
- [[Synchronization and Deadlocks - Review Drill]]
- [[File Systems and IO - Review Drill]]
- [[Virtualization Security and Case Studies - Review Drill]]

### Applied Exercises
- Trace a `fork()` + `exec()` sequence through process creation
- Simulate a page-replacement algorithm by hand (LRU clock)
- Solve the dining-philosophers problem with monitors
- Run a Banker's algorithm safety check on paper
- Compare Linux CFS with Windows thread scheduling

### Capstone
Pick one case study ([[Linux Architecture Overview]], [[Android Architecture]], or [[Windows NT Architecture]]) and map every concept from Passes 1–3 onto the real system.

## References
- [[CS Operating Systems/Sources/Sources Index|CS Operating Systems Sources Index]]
