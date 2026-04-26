---
tags:
  - csos
  - csos/synchronization
confidence: verified
up: "[[Synchronization Overview]]"
tier-coverage:
  - intuition
  - core
  - deep-dive
  - practice
---
# Semaphores

> **One-line summary**: A semaphore is an atomic integer counter with P (decrement/block) and V (increment/wake) operations — solving both mutual exclusion and signalling without busy-waiting.

## 🎯 Intuition
**The Core Idea:** A semaphore is a bathroom key at a coffee shop — if the key is on the hook (counter > 0), you take it and enter (P). When you leave, you hang it back (V) and the next person waiting can go.
**Analogy:** Binary semaphore (mutex) = one bathroom, one key on the hook. If someone's inside, you wait. Counting semaphore = a hotel pool with 5 towels (N=5). Each guest takes a towel (P); when they return it (V), the next guest can swim. Zero towels = you wait at the desk. Signalling = your friend drops a towel on the hook (V) specifically to let you know it's your turn (P), even though you don't share a resource.
**Why It Matters:** Semaphores were the first systematic solution to mutual exclusion and inter-thread signalling. They're the building block for producer-consumer, readers-writers, and most OS synchronisation. Understanding semaphores is prerequisite to understanding monitors and lock-free programming.

---

## ⚙️ Core Mechanics
### How It Works
A **semaphore** is a kernel-managed non-negative integer counter with two atomic operations: **P** (down / wait — decrement; block if result would go negative) and **V** (up / signal — increment; wake a blocked waiter if any). Introduced by Dijkstra (1965) to solve mutual exclusion and signalling without busy-waiting.

### Key Concepts / Operations

| Operation | Also called | Effect |
|-----------|-------------|--------|
| `P(s)` | `wait(s)`, `down(s)` | If s > 0: s−−. Else: block caller. |
| `V(s)` | `signal(s)`, `up(s)` | s++. If blocked waiters exist, wake one. |

Both operations are **atomic** — the OS guarantees they are indivisible.

#### Binary Semaphore (Mutex)
Initialised to 1. P acquires the lock; V releases it. At most one thread proceeds past P at a time — enforcing mutual exclusion over a critical section.

```
sem = 1
P(sem)   // enter critical section
  ... critical section ...
V(sem)   // leave
```

#### Counting Semaphore
Initialised to N. Allows up to N threads to hold the resource simultaneously. Used to manage a pool of N identical resources (e.g., a connection pool of size N).

#### Signalling
Semaphores also express ordering: thread A does `V(s)` after completing work; thread B does `P(s)` to wait until A is done. Initialise s = 0 so B always blocks until A signals.

### Key Facts
- P and V are always atomic — the OS guarantees no interleaving between the test and the decrement/block.
- Binary semaphore (initialised to 1) enforces mutual exclusion; counting semaphore (initialised to N) manages a resource pool.
- Semaphores can express ordering (signalling) — not just mutual exclusion.
- **Binary semaphore ≠ mutex**: POSIX mutexes track ownership (only the acquiring thread can release); semaphores do not.
- Forgetting V after a critical section = permanent deadlock for all subsequent threads.

---

## 🔬 Deep Dive
### Pitfalls
- **Deadlock by P-order**: two threads each P one semaphore and then try to P the other — circular wait.
- **Forgetting V**: thread exits critical section without calling V; all subsequent callers block forever.
- **Binary semaphore ≠ mutex**: POSIX mutexes track ownership (only the acquiring thread can release); semaphores do not.

### Implementation Details
- **POSIX semaphores**: `sem_init()` / `sem_open()` (named), `sem_wait()` (P), `sem_post()` (V), `sem_destroy()`. Named semaphores (`/some_name`) persist in the file system and work between unrelated processes. Unnamed semaphores work between threads or between processes sharing memory.
- **Linux kernel semaphores**: `struct semaphore` with `down()` (P) and `up()` (V). Implemented using a spinlock + wait queue. The spinlock protects the counter; `down()` checks the counter, and if zero, adds the task to the wait queue and calls `schedule()`.
- **System V semaphores**: `semget()`, `semop()`, `semctl()`. Support operations on semaphore *sets* (multiple semaphores atomically in one call). More complex API but allows atomic multi-resource allocation — useful for deadlock-free resource acquisition.
- **Dijkstra's original formulation**: P = "probeer te verlagen" (try to decrease); V = "verhoog" (increase). Dutch abbreviations from Dijkstra's 1965 paper.

### Edge Cases and Pitfalls
- **V without prior P**: Incrementing a semaphore without a corresponding P inflates the count — future P calls will succeed when they shouldn't. Unlike mutexes, semaphores have no "owner" to enforce correct pairing.
- **Semaphore as a barrier**: Initialise to 0; N threads do P(s) to wait; another thread does V(s) N times. Alternatively, use a `pthread_barrier`.
- **Semaphore leaks**: Named POSIX semaphores persist after process exit unless explicitly `sem_unlink()`'d. Forgotten semaphores accumulate in `/dev/shm/`.
- **Priority inversion**: A high-priority thread blocked on P(sem) while a low-priority thread holds the semaphore — and a medium-priority thread preempts the holder. Unlike mutexes, semaphores lack ownership, so the OS cannot apply priority inheritance.

### Real-World Systems
- **Linux kernel**: Uses mutexes (with ownership) more than semaphores for most synchronisation. Semaphores remain for legacy code and cases where V is called from a different context than P (e.g., interrupt handlers signalling sleepers).
- **POSIX IPC**: Named semaphores for inter-process synchronisation (e.g., coordinating a producer-consumer between separate binaries).
- **Java**: `java.util.concurrent.Semaphore` — counting semaphore with optional fairness (FIFO ordering). Used for connection pools, rate limiting, and resource throttling.
- **FreeRTOS**: Binary and counting semaphores are primary synchronisation primitives in embedded/RTOS systems where monitors and condition variables are unavailable.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What is the difference between a binary semaphore and a POSIX mutex?
2. How can a semaphore initialised to 0 express ordering (signalling) between two threads?
3. What happens if a thread calls V(sem) without ever calling P(sem) first?

### Core Problems
1. **Semaphore trace**: Two threads share `sem = 1`. Thread A: `P(sem); x++; V(sem)`. Thread B: `P(sem); x++; V(sem)`. Initial x = 0. (a) Show all possible interleavings of P/V operations. (b) Prove that x = 2 in all cases. (c) Now remove the semaphore — show an interleaving where x = 1.
2. **Ordering with semaphores**: Three threads must execute in order: T1 prints "A", T2 prints "B", T3 prints "C". Using only semaphores (no other primitives), design a solution that guarantees the output is always "ABC" regardless of which thread runs first. Define the semaphores, their initial values, and the code for each thread.

### Challenge
Implement a **read-write lock** using only counting semaphores (no mutexes, no condition variables). Support `read_lock()`, `read_unlock()`, `write_lock()`, `write_unlock()`. Your solution should: (a) allow concurrent readers, (b) give writers exclusive access, (c) prevent writer starvation (hint: use an additional semaphore as a "turnstile"). Provide pseudocode and trace a scenario: R1 starts reading, R2 starts reading, W1 arrives, R3 arrives. Show the order of execution and which threads are blocked where.

---

*See also:* [[Deadlock Fundamentals]] — incorrect P-ordering on semaphores is a textbook deadlock cause · [[Interprocess Communication]] — semaphores coordinate shared-memory IPC between processes · [[Monitors and Condition Variables]] — a higher-level synchronisation abstraction that avoids semaphore ordering pitfalls · [[Classic Synchronization Problems]] — producer-consumer and readers-writers are solved with semaphores

## Supporting Chunks

- [[Synchronization - Semaphores implement mutual exclusion and signalling with P and V operations]]
- [[Synchronization - The producer-consumer problem requires a bounded buffer with synchronised access]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 2.
