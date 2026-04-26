---
tags:
  - csos
  - csos/memory
confidence: verified
up: "[[Memory Management Overview]]"
tier-coverage:
  - intuition
  - core
  - deep-dive
  - practice
---
# Page Replacement Algorithms

> **One-line summary**: When physical memory is full and a page fault occurs, the OS must choose which page to evict — the algorithm used determines how many future faults occur.

## 🎯 Intuition
**The Core Idea:** Page replacement is the OS deciding which book to remove from a small desk (RAM) to make room for a new one from the library shelves (disk).
**Analogy:** You have a desk that holds 4 books (frames). You're studying and need a 5th book. Which book do you remove? OPT = remove the one you won't need for the longest time (requires clairvoyance). LRU = remove the one you haven't touched in the longest time (good guess). FIFO = remove the one that's been on the desk longest (simple but sometimes wrong). Clock = quickly scan: "Have I touched this recently? No? Remove it."
**Why It Matters:** A bad replacement policy causes thrashing — the system spends more time swapping pages than doing useful work. Good policies keep the "working set" in memory.

---

## ⚙️ Core Mechanics
### How It Works
When a page fault occurs and physical memory is full, the OS must choose a **victim frame** to evict — writing it to the swap area if dirty, then loading the needed page. The goal is to minimise future page faults.

### Key Concepts / Algorithms

**Optimal (OPT / MIN)**
Evict the page that will not be used for the longest time in the future. Optimal by definition — minimises page faults — but **not implementable** (requires future knowledge). Used only as a benchmark.

**FIFO**
Evict the page that has been in memory longest. Simple; no hardware support needed. Suffers **Bélády's anomaly**: adding more frames can *increase* page faults for some reference strings.

**Least Recently Used (LRU)**
Evict the page that was last accessed longest ago. Good approximation of OPT. Exact LRU requires hardware time-stamping every memory access — expensive. Approximate implementations use the **accessed bit** in the PTE.

**Clock Algorithm (Second-Chance)**
A practical approximation of LRU:
1. Frames arranged in a circular list with a "clock hand".
2. On page fault: inspect the page under the hand.
   - Accessed bit = 1 → clear it (give a second chance); advance hand.
   - Accessed bit = 0 → evict this page.
3. Hardware sets the accessed bit on every reference.

$O(1)$ per replacement; no software time-stamp needed. Used in Linux (as part of its active/inactive list split) and many other systems.

**Not Recently Used (NRU)**
Uses the accessed (R) and dirty (M) bits to classify pages into four classes (00, 01, 10, 11). Randomly evict from the lowest non-empty class. Very cheap; slightly worse than clock.

### Algorithm Comparison

| Algorithm | Complexity | Hardware Needed | Anomaly Risk | Quality |
|-----------|-----------|-----------------|--------------|---------|
| OPT | N/A | N/A (theoretical) | None | Perfect (benchmark) |
| FIFO | $O(1)$ | None | Bélády's anomaly | Poor |
| LRU | $O(1)$ amortised | Timestamp or stack | None | Good |
| Clock | $O(1)$ | Accessed bit | None | Good (practical) |
| NRU | $O(1)$ | R + M bits | None | Fair |

### Key Facts
- OPT is the theoretical benchmark — no real algorithm can beat it.
- FIFO is the only common algorithm that suffers Bélády's anomaly.
- LRU is a "stack algorithm" and immune to Bélády's anomaly (more frames ≥ always ≤ faults).
- The clock algorithm is the practical standard — approximates LRU with minimal overhead.
- A process's **working set** W(t, τ) is the set of pages referenced in the past τ seconds; thrashing occurs when RAM < total working sets.

---

## 🔬 Deep Dive
### Working Set Model
A process's **working set** W(t, τ) is the set of pages it referenced in the past τ seconds. Keeping only the working set in memory reduces faults; thrashing occurs when physical memory < sum of working sets.

### Implementation Details
- **Linux page reclaim (kswapd)**: Linux uses an active/inactive list split inspired by the clock algorithm. Pages start on the inactive list; if accessed, they're promoted to the active list. Under memory pressure, `kswapd` demotes pages from active → inactive → eviction. The "second chance" happens during demotion.
- **Linux MGLRU (Multi-Gen LRU)**: Introduced in Linux 6.1 (2022), MGLRU improves on the active/inactive split by tracking multiple generations of page age, reducing the rate of premature evictions for workloads with mixed access patterns.
- **Windows page replacement**: Windows uses a modified clock algorithm with a "standby list" — evicted clean pages remain on the standby list and can be reclaimed without disk I/O if re-accessed before the frame is reused. This acts as a soft cache layer.
- **Dirty page write-back**: The OS writes dirty pages to disk proactively (Linux: `pdflush`/`writeback` threads) to convert dirty pages to clean — making them cheaper to evict later. The `/proc/sys/vm/dirty_ratio` controls when aggressive write-back begins.

### Edge Cases and Pitfalls
- **Bélády's anomaly (FIFO)**: Reference string 1,2,3,4,1,2,5,1,2,3,4,5 with 3 frames → 9 faults; with 4 frames → 10 faults. More memory, more faults!
- **Thrashing**: When the sum of all processes' working sets exceeds physical memory, the system spends most of its time handling page faults. The CPU utilisation drops; the OS may respond by scheduling more processes, making it worse. Solution: reduce the degree of multiprogramming.
- **Sequential scan problem**: A process reading a large file sequentially evicts useful pages and fills memory with pages used only once. Solution: scan-resistant algorithms (Linux uses the inactive list to detect one-shot pages).

### Real-World Systems
- **Linux**: Active/inactive LRU lists + MGLRU (6.1+); kswapd for background reclaim; OOM killer as last resort.
- **Windows**: Clock-based with standby/modified page lists; Memory Manager trims working sets under pressure.
- **PostgreSQL**: Uses its own clock-sweep algorithm for the shared buffer cache, independent of the OS page cache.
- **Redis**: Application-level eviction policies (LRU, LFU, random, volatile-ttl) for its in-memory data store.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why is the OPT algorithm not implementable in a real system?
2. Explain Bélády's anomaly in one sentence. Which algorithm suffers from it?
3. What is the clock hand doing when it encounters an accessed bit of 1?

### Core Problems
1. **Algorithm trace**: Reference string: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1. Trace the contents of 3 frames and count page faults for: (a) FIFO, (b) LRU, (c) OPT. Which algorithm has the fewest faults? Demonstrate Bélády's anomaly by tracing FIFO with 4 frames on a reference string where it gets worse.
2. **Clock algorithm simulation**: 5 frames in a circular buffer. Reference string: A, B, C, D, E, A, B, F, A, B, C, D. Trace the clock hand position, accessed bits, and eviction decisions. Compare the number of faults to exact LRU on the same trace.

### Challenge
Design an adaptive page replacement algorithm that switches between LRU-like and FIFO-like behaviour based on workload detection. Your algorithm should: (a) detect sequential scan patterns (one-shot pages) and avoid polluting the cache, (b) detect looping access patterns and keep the loop's working set in memory, (c) handle mixed workloads. Describe your detection heuristic, the switching mechanism, and analyse the overhead. Compare your design to Linux's MGLRU approach.

---

*See also:* [[Disk Scheduling Algorithms]] — evicted dirty pages generate disk writes whose latency depends on the I/O scheduler · [[File System Implementation]] — the buffer cache uses similar eviction policies for cached file blocks · [[CPU Scheduling]] — thrashing (working sets exceed RAM) degrades scheduling performance · [[Virtual Memory and Paging]] — page faults trigger the replacement algorithm

## Supporting Chunks

- [[Memory - Page replacement policies decide which frame to evict on a page fault]]
- [[Memory - The clock algorithm approximates LRU using a reference bit with O(1) overhead]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 3.
