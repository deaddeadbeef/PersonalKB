---
tags: [cs-os, raw]
source_type: textbook_topic
source_title: "Concurrency Bugs and Detection"
authors: Lu, Park, Seo, Zhou; Arpaci-Dusseau, Arpaci-Dusseau
year: 2008
---

# Concurrency Bugs and Detection

## Summary

Concurrency bugs are defects that arise from incorrect synchronization in multi-threaded programs. A landmark 2008 study by Lu et al. analyzed 105 concurrency bugs from four major open-source projects (MySQL, Apache, Mozilla, OpenOffice), categorizing them into four types: data races, atomicity violations, order violations, and deadlocks. Atomicity violations (the assumption that a code region executes atomically when it does not) accounted for the majority at approximately 70%, followed by order violations (~30% of non-deadlock bugs).

A **data race** occurs when two threads access the same memory location concurrently, at least one access is a write, and there is no synchronization ordering the accesses. Data races are a necessary but not sufficient condition for most bugs—some data races are benign, while some bugs occur without data races (atomicity violations with individual accesses properly locked but the compound operation unprotected). An **atomicity violation** occurs when a programmer intends a sequence of operations to execute atomically, but interleaving by another thread breaks the intended invariant. Example: Thread A reads a pointer, is preempted, Thread B sets the pointer to NULL, Thread A dereferences the now-NULL pointer. An **order violation** occurs when operations that must execute in a specific order (e.g., initialization before use) are not properly synchronized with condition variables or barriers.

**Deadlocks** arise when threads hold locks and circularly wait for locks held by each other. Prevention strategies include lock ordering discipline (always acquire locks in a globally consistent order), trylock with backoff, and lock-free data structures.

Detection tools employ various techniques. **ThreadSanitizer (TSan)** instruments memory accesses at compile time and uses a happens-before algorithm to detect data races at runtime with typically 5–15x slowdown. **Helgrind** (a Valgrind tool) also detects data races and lock-order violations using happens-before analysis. The **happens-before** relation (Lamport 1978) defines a partial order on events: if event A happens-before event B, then A's effects are visible to B. Two events with no happens-before relation are concurrent, and if one is a write, a data race exists. Static analysis tools (Coverity, Infer) detect potential concurrency bugs without running the code but suffer from false positives.

## Key Claims

- Atomicity violations are the most common concurrency bug type (~70% of non-deadlock bugs in the Lu et al. study), more prevalent than simple data races or order violations
- Data races are a necessary but not sufficient condition for most concurrency bugs—atomicity violations can occur even when individual memory accesses are properly synchronized
- Lock ordering discipline (always acquiring locks in a globally consistent order) prevents deadlocks by eliminating the possibility of circular wait
- Happens-before analysis provides the theoretical foundation for race detection by defining a partial order on thread events: concurrent accesses with at least one write constitute a data race
- Runtime detection tools like ThreadSanitizer impose 5–15x overhead, making them practical for testing but not production deployment

## Atomic Facts

1. The Lu et al. 2008 study ("Learning from Mistakes") found that 97% of non-deadlock concurrency bugs involved only one or two variables, suggesting simple patterns dominate
2. ThreadSanitizer (TSan) uses shadow memory to track access metadata (thread ID, clock, type) for each memory location and vector clocks for happens-before tracking
3. Helgrind tracks lock acquisition order across all threads and reports if two threads acquire the same pair of locks in different orders (potential deadlock)
4. The happens-before relation is established by synchronization events: lock release → lock acquire, thread create → first instruction, signal → wait on the same condition variable
5. Lock-free data structures use atomic compare-and-swap (CAS) operations to avoid locks entirely, eliminating deadlock at the cost of increased algorithmic complexity and potential livelock
6. The `-fsanitize=thread` flag in GCC and Clang enables ThreadSanitizer, which adds compile-time instrumentation to detect races with approximately 2x memory overhead and 5–15x runtime overhead

## Significance

Concurrency bugs are among the most difficult defects to reproduce, diagnose, and fix due to their dependence on non-deterministic thread scheduling. Understanding the taxonomy (data races, atomicity violations, order violations, deadlocks) and detection techniques is essential for writing correct concurrent software. The Lu et al. study's finding that most bugs involve simple patterns with few variables suggests that targeted tool support and disciplined locking practices can prevent the majority of real-world concurrency defects.

## Chunks Extracted

*Pending*
