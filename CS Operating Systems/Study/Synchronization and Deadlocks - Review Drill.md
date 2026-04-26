---
tags:
  - csos
  - csos/study
  - csos/synchronization
  - csos/deadlocks
up: "[[OS Study Index]]"
---
# Synchronization and Deadlocks — Review Drill

Active-recall drill for race conditions, mutual exclusion primitives, classic synchronisation problems, and the full spectrum of deadlock handling strategies.

**Canon pages:** [[Race Conditions and Mutual Exclusion]] · [[Semaphores]] · [[Monitors and Condition Variables]] · [[Classic Synchronization Problems]] · [[Deadlock Fundamentals]] · [[Deadlock Prevention]] · [[Deadlock Avoidance]] · [[Deadlock Detection and Recovery]] · [[Synchronization Overview]] · [[Deadlocks Overview]]

---

## How to Use

Answer each question aloud or in writing before revealing the answer. Synchronisation and deadlocks require mechanical precision — vague answers usually indicate a gap.

---

## Core Recall

**Race Conditions and Mutual Exclusion**

Q: What is a race condition, and why does `count++` create one?
A: A race condition occurs when the correct result depends on the interleaving order of concurrent operations. `count++` compiles to three instructions: LOAD, INCREMENT, STORE. If two threads execute this concurrently, both can load the same value, increment it, and store — one update is lost. The outcome is non-deterministic and depends on the precise context-switch schedule.

Q: What three properties must a correct mutual-exclusion solution satisfy?
A: (1) **Mutual exclusion** — at most one thread in the critical section at any time. (2) **Progress** — if no thread is in the critical section and some want to enter, one eventually does (no livelock). (3) **Bounded waiting** — no thread waits forever to enter (no starvation).

Q: Compare spin locks to blocking locks. When should each be used?
A: **Spin lock (busy-waiting)**: the waiting thread loops testing the lock; never sleeps. Very low latency for short critical sections. Wastes CPU cycles if the lock is held for long. Correct choice on multiprocessors where the lock holder is running in parallel and will release soon. **Blocking lock**: the waiting thread is descheduled by the OS; woken when the lock is free. Efficient for long waits; adds system-call overhead. Correct choice for long critical sections or uniprocessors.

---

**Semaphores**

Q: Define P(s) and V(s) precisely.
A: **P(s)** (wait/down): if s > 0, decrement s atomically. Else block the caller. **V(s)** (signal/up): increment s atomically. If any threads are blocked in P, wake one. Both are atomic — indivisible by the OS.

Q: How do you use semaphores to implement: (a) a mutex; (b) a counting resource pool; (c) signalling?
A: (a) **Mutex**: initialise to 1. P(s) acquires; V(s) releases. At most one holder at a time. (b) **Counting pool**: initialise to N. Each P grants one resource unit; each V returns one. Up to N concurrent holders. (c) **Signalling**: initialise to 0. Thread B calls P(s) to wait; thread A calls V(s) when done. B cannot proceed until A signals.

Q: State the canonical semaphore ordering for the bounded-buffer producer-consumer.
A: Three semaphores: `mutex = 1`, `empty = N`, `full = 0`. Producer: `P(empty) → P(mutex) → add item → V(mutex) → V(full)`. Consumer: `P(full) → P(mutex) → remove item → V(mutex) → V(empty)`. Critical rule: always P the resource semaphore (empty/full) *before* P(mutex) — reversing this order causes deadlock.

---

**Monitors and Condition Variables**

Q: What problem do monitors solve that semaphores do not?
A: Semaphore misuse (wrong order, forgotten V, V without P) is hard to catch and causes deadlock or data corruption. A **monitor** encapsulates shared data and operations; mutual exclusion is enforced automatically by the language/runtime — a thread that calls a monitor procedure is guaranteed exclusive access. Programmers cannot accidentally forget to acquire or release the lock.

Q: What is the difference between `wait()` and `signal()` on a condition variable?
A: `wait(cv, mutex)`: atomically releases the mutex and blocks the caller on the condition queue. The mutex is reacquired before wait returns. `signal(cv)`: wakes one blocked waiter (if any) — it moves to the ready state; in Hoare semantics the signaller yields immediately; in Mesa semantics (most implementations) the signaller continues and the waiter re-checks the condition with a `while` loop.

Q: Why must condition variable waits always be in a `while` loop, not an `if`?
A: In Mesa semantics (used by Java, pthreads), a signalled thread does not run immediately — other threads may intervene and change the condition before the waiter runs. The `while` loop re-checks the condition after waking and goes back to sleep if it is no longer true. Using `if` is a classic bug: the woken thread assumes the condition holds and proceeds incorrectly.

---

**Classic Synchronisation Problems**

Q: Describe the dining philosophers problem and why naive "pick up left then right" causes deadlock.
A: Five philosophers alternate between thinking and eating. Eating requires two forks (shared with neighbours). If all simultaneously pick up their left fork, each holds one fork and waits for the right — forming a circular wait. No one proceeds: deadlock. Four Coffman conditions all hold.

Q: Give three correct solutions to dining philosophers.
A: (1) **Asymmetric ordering**: one philosopher picks up the right fork first — breaks circular wait. (2) **Arbitrator (waiter)**: philosophers ask permission before touching forks; only granted if both are available. (3) **Limit occupancy**: allow at most four philosophers to sit simultaneously — at least one can always eat.

Q: In the readers-writers problem, what is the difference between the first and second solutions?
A: **First (readers prefer)**: a new reader is never blocked while other readers are active — writers starve if readers arrive continuously. **Second (writers prefer)**: once a writer is waiting, no new readers are admitted — readers may starve. A **third, fair** solution uses a FIFO queue ordering all arrivals so neither starvation can occur.

---

**Deadlock Fundamentals**

Q: State the four Coffman conditions. What is the significance of all four?
A: **Mutual exclusion** — resource held in non-shareable mode. **Hold and wait** — a process holds one resource while waiting for another. **No preemption** — resources cannot be forcibly taken. **Circular wait** — a cycle in the resource-allocation graph. All four must hold *simultaneously* — denying any one prevents deadlock.

Q: What does a cycle in the resource-allocation graph tell you?
A: For **single-instance resources**: a cycle is a deadlock — certain. For **multi-instance resources**: a cycle is necessary but not sufficient — deadlock is possible, not guaranteed. A more detailed analysis (Banker's algorithm or wait-for graph) is needed.

---

**Deadlock Strategies**

Q: Compare prevention, avoidance, detection, and the ostrich strategy.
A: **Prevention**: statically deny one Coffman condition at all times (e.g., require all resources requested upfront — eliminates hold-and-wait; or use resource ordering — eliminates circular wait). Safe but reduces resource utilisation. **Avoidance**: dynamically track system state; only grant requests that leave the system in a safe state (Banker's algorithm). Safe but requires advance declaration of maximum needs. **Detection + recovery**: allow deadlock to happen; periodically run a detection algorithm; recover by killing processes or preempting resources. **Ostrich**: ignore the problem. Pragmatic for systems where deadlock is rare and recovery is cheap (restart the process).

Q: Describe the Banker's algorithm in plain terms.
A: Each process declares its maximum resource needs at start. When a process requests resources, the OS tentatively grants them and checks if the resulting state is **safe**: can there exists a sequence of processes (a "safe sequence") in which each can complete using currently available resources plus whatever earlier processes in the sequence will eventually release? If yes, grant. If no, make the process wait. Safety check is $O(n² · m)$ where n = processes, m = resource types.

---

## Compare and Contrast

**Semaphores vs Monitors**

| Property | Semaphores | Monitors |
|----------|-----------|---------|
| Synchronisation style | Explicit P/V | Implicit (language-enforced) |
| Mutual exclusion | Manual | Automatic |
| Misuse risk | High (wrong order, missing V) | Low (compiler enforced) |
| Expressiveness | Any synchronisation pattern | Structured; condition variables |
| Language examples | POSIX, C | Java synchronized, Mesa |

**Deadlock Handling Strategies**

| Strategy | When to use | Cost | Guarantee |
|----------|-------------|------|-----------|
| Prevention | Offline design phase | Reduced utilisation | Deadlock impossible |
| Avoidance (Banker's) | Systems with known max needs | Runtime overhead | Deadlock impossible |
| Detection + recovery | Deadlock rare; recovery cheap | Detection overhead; recovery disruption | Allows deadlock |
| Ostrich | Deadlock very rare (desktop OS) | None | No guarantee |

---

## Common Mistakes

1. **Semaphore ordering in producer-consumer** — P(mutex) before P(empty) causes deadlock if the buffer is full. Always acquire the resource semaphore first.

2. **Signal semantics** — Hoare monitors guarantee the condition is still true when the signalled thread runs; Mesa (practical) monitors do not. In real code (Java, pthreads), always use `while`, not `if`.

3. **Cycle in multi-instance graph ≠ deadlock** — a cycle is necessary, not sufficient, for deadlock when resources have multiple instances. Students who stop at "there's a cycle" will give wrong answers on exam questions with multi-instance resources.

4. **Banker's algorithm requires advance declaration** — the algorithm is only correct if each process truthfully declares its maximum needs upfront. A process that lies or changes its needs after declaration can defeat the safety guarantee.

5. **No preemption condition** — "no preemption" means resources cannot be *forcibly taken away*. It does not mean the CPU cannot be preempted. Confusing scheduling preemption with resource preemption is a classic error.

---

## Links Back

- [[Race Conditions and Mutual Exclusion]] — critical section; Peterson; TSL/CAS; spin vs blocking
- [[Semaphores]] — P/V operations; binary vs counting; signalling; pitfalls
- [[Monitors and Condition Variables]] — automatic exclusion; wait/signal; Mesa vs Hoare
- [[Classic Synchronization Problems]] — producer-consumer; readers-writers; dining philosophers
- [[Deadlock Fundamentals]] — four Coffman conditions; resource-allocation graph
- [[Deadlock Prevention]] — denying one Coffman condition
- [[Deadlock Avoidance]] — Banker's algorithm; safe state
- [[Deadlock Detection and Recovery]] — wait-for graph; recovery options
- [[Synchronization Overview]] — hub for synchronisation
- [[Deadlocks Overview]] — hub for deadlocks
