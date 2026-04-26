---
tags: [cs-os, raw]
source_type: textbook_chapter
source_title: "Process Synchronization"
authors: "Andrew S. Tanenbaum, Herbert Bos"
year: 2015
---

# Process Synchronization

## Summary
When multiple processes or threads access shared data concurrently, race conditions arise that can corrupt data and produce non-deterministic behavior. The critical section problem formalizes the requirements for safe concurrent access: mutual exclusion, progress, and bounded waiting. Solutions range from purely software algorithms (Peterson's solution) to hardware-assisted primitives (test-and-set, compare-and-swap) to higher-level abstractions (mutex locks, semaphores) that form the building blocks of all concurrent systems.

## Key Claims
- A race condition occurs when the outcome of concurrent execution depends on the specific order of interleaved instructions—these bugs are notoriously difficult to reproduce and diagnose because they depend on timing
- Any correct solution to the critical section problem must satisfy three properties: mutual exclusion (at most one process in the critical section), progress (only contending processes participate in the decision), and bounded waiting (a finite limit on how many times other processes can enter before a waiting process)
- Peterson's solution is the simplest correct software-only solution for two processes, using a turn variable and an interested array, but it fails on modern hardware without memory barriers due to instruction reordering
- Hardware atomic instructions (test-and-set, compare-and-swap) provide the foundation for all practical synchronization primitives; they execute indivisibly, preventing interleaving at the instruction level
- Semaphores generalize mutex locks: a binary semaphore (values 0 and 1) behaves identically to a mutex, while a counting semaphore (values 0 to N) controls access to a resource pool with N identical instances

## Atomic Facts
1. Peterson's algorithm for two processes P0 and P1 uses two shared variables: `flag[2]` (indicating desire to enter) and `turn` (tiebreaker); process Pi sets flag[i]=true, turn=j, then waits while flag[j]==true AND turn==j
2. The test-and-set instruction atomically reads a memory location, returns its old value, and sets it to true—a spinlock is implemented by looping on test-and-set until the old value is false (meaning the lock was free)
3. Compare-and-swap (CAS) atomically compares a memory location to an expected value and, only if they match, replaces it with a new value; CAS is the basis for lock-free data structures and is exposed as `cmpxchg` on x86
4. Dijkstra introduced semaphores in 1965 with two atomic operations: wait(S) (also called P or down) decrements S and blocks if the result is negative, and signal(S) (also called V or up) increments S and wakes a blocked process if any
5. A mutex differs from a binary semaphore in that a mutex has ownership semantics—only the thread that acquired the mutex may release it—enabling priority inheritance to combat priority inversion
6. On x86 processors, memory ordering is relatively strong (total store order), but ARM and RISC-V have weaker memory models requiring explicit memory barriers (fences) to prevent the reordering that breaks algorithms like Peterson's

## Significance
Process synchronization is where theory meets the hardware reality of modern processors. Every concurrent program—from database engines to web servers—depends on these primitives being correctly implemented. The gap between Peterson's elegant algorithm and the memory-barrier-aware implementations required on real hardware illustrates why concurrent programming remains one of the hardest areas in systems development.

## Chunks Extracted
*Pending*
