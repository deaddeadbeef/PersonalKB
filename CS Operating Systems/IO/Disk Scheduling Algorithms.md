---
tags:
  - csos
  - csos/io
confidence: verified
up: "[[IO Overview]]"
tier-coverage:
  - intuition
  - core
  - deep-dive
  - practice
---
# Disk Scheduling Algorithms

## 🎯 Intuition
**The Core Idea:** On HDDs, the OS can reorder pending disk requests to reduce head movement and therefore reduce average seek time.

**Analogy:** An elevator does not visit floors in the exact order people pressed buttons; it usually sweeps in one direction to avoid wasteful back-and-forth motion.

**Why It Matters:** Traditional hard disk performance is dominated by **seek time** and **rotational latency**, so good scheduling can greatly improve throughput and average wait time.

## ⚙️ Core Mechanics
### Why Scheduling Matters
Traditional hard disk performance is dominated by **seek time** (moving the head to the right track) and **rotational latency** (waiting for the sector to spin under the head).

### FCFS (First Come, First Served)
Service requests in arrival order. Fair; no starvation. Can produce erratic head movement — high seek time.

### SSTF (Shortest Seek Time First)
Always service the request closest to the current head position. Minimises individual seeks; high throughput. **Starvation** risk: requests at the far end of the disk may wait indefinitely if close requests keep arriving.

### SCAN (Elevator Algorithm)
The disk arm sweeps from one end to the other, servicing all requests in the direction of travel; at the end it reverses direction. Like an elevator. No starvation; more uniform wait time than SSTF. Used in Linux's CFQ and deadline schedulers.

### C-SCAN (Circular SCAN)
Like SCAN but the arm only services requests in one direction. When it reaches the end it jumps back to the beginning without servicing on the return. Provides more uniform wait time distribution than SCAN since requests at the "recently visited" end don't benefit from a quick second pass.

### LOOK / C-LOOK
Optimisations of SCAN/C-SCAN: the arm only travels as far as the last request in each direction, not all the way to the physical disk end.

## 🔬 Deep Dive
### Trade-Offs Across Algorithms
- **FCFS** is simplest and fair, but often performs poorly because head motion can become erratic.
- **SSTF** improves throughput by choosing the closest request, but it can starve distant requests.
- **SCAN** avoids starvation and gives more uniform wait time by sweeping end-to-end.
- **C-SCAN** further improves uniformity by servicing requests in only one direction.
- **LOOK/C-LOOK** keep the sweep logic but avoid needless travel to the physical end of the disk when no request is there.

### Modern Relevance
SSDs have no moving parts — seek time and rotational latency are irrelevant. SSD I/O scheduling focuses on command queuing depth (NCQ/NVMe queues) and write amplification rather than head movement. The Linux `none` and `mq-deadline` schedulers are preferred for SSDs.

### Why Old Algorithms Matter Less on SSDs
- Reordering for head movement matters on HDDs because the disk arm and platter rotation create mechanical delays.
- On SSDs and NVMe devices, there is no arm to move, so queue management and controller parallelism matter more than elevator-style sweeps.

## 🏋️ Practice
### Warm-Up
1. Why do seek time and rotational latency dominate HDD performance?
2. Which scheduling algorithm is most vulnerable to starvation?
3. What is the key difference between SCAN and C-SCAN?

### Core Problems
1. Given request queue `[98, 183, 37, 122, 14, 124, 65, 67]` and head at `53`, calculate total head movement for SCAN. State your assumed initial sweep direction.
2. Why is SSTF not used in practice as the only scheduling policy despite its strong throughput?
3. Compare LOOK with SCAN. What wasted motion does LOOK remove?

### Challenge
1. What scheduling approach should an NVMe SSD prefer: a head-movement algorithm like SCAN, or a lightweight queue-oriented scheduler such as `none` or `mq-deadline`? Why?
2. Linux once used CFQ/deadline with HDD-oriented assumptions. Explain why those choices differ from modern SSD-oriented scheduler choices.

## Supporting Chunks

- [[IO - SCAN disk scheduling services requests in sweep order to reduce average seek time]]

## See Also

- [[File System Implementation]] — file allocation layout (contiguous vs indexed) determines the I/O request pattern
- [[Interrupts and DMA]] — DMA controllers transfer disk data to memory; completion triggers an interrupt
- [[Page Replacement Algorithms]] — dirty page eviction generates the disk writes that the scheduler reorders
- [[Multiprocessor Systems]] — NVMe multi-queue scheduling distributes I/O across cores

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 5.
