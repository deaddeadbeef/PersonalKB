---
tags: [cs-os, raw]
source_type: textbook_chapter
source_title: "Classic Synchronization Problems"
authors: "Andrew S. Tanenbaum, Herbert Bos"
year: 2015
---

# Classic Synchronization Problems

## Summary
Three classic synchronization problems—producer-consumer, readers-writers, and dining philosophers—serve as canonical exercises for testing the correctness and expressiveness of synchronization primitives. These problems expose the fundamental challenges of concurrent programming: ensuring mutual exclusion without causing starvation, maximizing concurrency for read-heavy workloads, and preventing deadlock in cyclic resource dependencies. Monitors with condition variables provide a structured, less error-prone alternative to raw semaphores for solving these problems.

## Key Claims
- The bounded-buffer (producer-consumer) problem requires three synchronization elements: a mutex for buffer access, a semaphore tracking empty slots (blocks producer when full), and a semaphore tracking full slots (blocks consumer when empty)—omitting any one leads to race conditions or deadlock
- The readers-writers problem has two variants: the first gives readers priority (writers may starve), the second gives writers priority (readers may starve); no solution simultaneously prevents starvation for both without additional mechanisms like fair queuing
- The dining philosophers problem demonstrates that even with simple, symmetric resource acquisition patterns, deadlock can occur when all participants simultaneously acquire their left resource; solutions include resource ordering, an arbitrator, or limiting concurrency to N−1 philosophers
- Monitors encapsulate shared data, procedures, and synchronization into a single construct, ensuring that only one thread executes within the monitor at a time—this structural guarantee eliminates the possibility of the missed-signal bugs common with raw semaphore solutions
- The distinction between Hoare semantics and Mesa semantics for condition variables affects correctness: Hoare semantics guarantee the signaled thread runs immediately (the signaler suspends), while Mesa semantics only move the signaled thread to the ready queue, requiring it to recheck the condition with a while loop

## Atomic Facts
1. The producer-consumer solution with semaphores uses: semaphore mutex=1 (binary, protects buffer), semaphore empty=N (counting, initially N empty slots), semaphore full=0 (counting, initially 0 full slots); the producer does wait(empty), wait(mutex), insert, signal(mutex), signal(full)
2. In the first readers-writers solution, readers maintain a read_count protected by a mutex; the first reader locks the resource (blocking writers), and the last reader unlocks it—while any readers are active, writers are blocked indefinitely, causing writer starvation
3. The dining philosophers deadlock occurs when all five philosophers simultaneously pick up their left fork; Dijkstra's solution assigns each fork a number and requires philosophers to pick up the lower-numbered fork first, breaking the circular wait condition
4. Monitors were proposed by C.A.R. Hoare (1974) and Per Brinch Hansen (1973) independently; Java's synchronized keyword and Python's threading.Condition implement monitor-like semantics in modern languages
5. Mesa semantics (used by Java, POSIX pthreads, and virtually all modern systems) require the signaled thread to re-verify the condition in a while loop because another thread may have changed the state between the signal and the signaled thread's resumption
6. Condition variables support two operations: wait(cv, mutex) atomically releases the mutex and suspends the thread until signaled, and signal(cv) wakes one waiting thread (broadcast(cv) wakes all)—the atomicity of the wait operation is critical for correctness

## Significance
These classic problems endure in computer science education because they distill real-world concurrency challenges into minimal, analyzable forms. The producer-consumer pattern appears in every message queue and pipeline system. The readers-writers tradeoff governs database locking strategies (shared vs exclusive locks). And the dining philosophers' deadlock potential manifests in any system where multiple agents compete for multiple resources—from database transactions to distributed microservices.

## Chunks Extracted
- [[chunk-os-107 Bounded-Buffer Needs Mutex Plus Two Counting Semaphores]]
- [[chunk-os-108 Readers-Writers Forces Reader or Writer Starvation Choice]]
- [[chunk-os-109 Dining Philosophers Demonstrates Deadlock in Symmetric Acquisition]]
- [[chunk-os-110 Hoare vs Mesa Monitor Semantics Differ in Signal Guarantees]]
