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
# Monitors and Condition Variables

> **One-line summary**: A monitor bundles a mutex with condition variables into a single construct — providing automatic mutual exclusion and structured waiting.

## 🎯 Intuition
**The Core Idea:** A monitor is a room with one door (only one thread inside at a time) and waiting benches (condition variables) where threads sit until they're told conditions have changed.
**Analogy:** Imagine a one-person-at-a-time fitting room (monitor). You enter (acquire lock), try on clothes, and if nothing fits (condition not met), you sit in the waiting area (condition variable wait — releasing the room). When new clothes arrive (signal), someone from the waiting area re-enters the room. The room's lock is automatic — you can't forget to lock/unlock.
**Why It Matters:** Monitors eliminate the most common synchronisation bugs: forgetting to release a lock, signalling in the wrong order, or using `if` instead of `while`. Java's `synchronized` and Python's `Condition` are monitor implementations.

---

## ⚙️ Core Mechanics
### How It Works
A **monitor** is a high-level synchronisation construct that combines a mutex and a set of **condition variables** into a single module. Only one thread can execute inside the monitor at a time; mutual exclusion is automatic, not manual. Proposed by Hoare (1974) and Hansen (1975).

#### Structure

```
monitor BoundedBuffer {
    mutex m;
    condition not_full, not_empty;
    buffer[N];

    void produce(item) {
        lock(m);
        while (buffer.full())  wait(not_full);
        buffer.add(item);
        signal(not_empty);
        unlock(m);
    }

    item consume() {
        lock(m);
        while (buffer.empty()) wait(not_empty);
        item = buffer.remove();
        signal(not_full);
        unlock(m);
    }
}
```

### Key Concepts / Operations

| Operation | Effect |
|-----------|--------|
| `wait(cond)` | Release the monitor lock; block on cond; reacquire lock on wake |
| `signal(cond)` | Wake one thread waiting on cond |
| `broadcast(cond)` | Wake all threads waiting on cond |

### Mesa vs Hoare Semantics
- **Hoare**: signaller immediately hands the lock to the waiter (atomically). Woken thread can assume the condition is still true. Rare in practice.
- **Mesa** (Java, pthreads): signaller keeps running; woken thread is placed in the ready queue and must recheck the condition when it eventually runs. Always use `while`, not `if`, for condition checks.

### Key Facts
- Monitors are easier to use correctly than semaphores — the programmer cannot forget to release a lock or call wait in the wrong order.
- Semaphores are more flexible (usable across modules) but error-prone.
- Java's `synchronized` keyword and `wait/notify` implement a monitor.
- Under Mesa semantics, ALWAYS use `while` loops for condition checks, never `if` — the condition may become false again before the woken thread runs.
- `broadcast()` wakes ALL waiters; `signal()` wakes exactly one. Use broadcast when multiple waiters may proceed.

---

## 🔬 Deep Dive
### Implementation Details
- **POSIX condition variables**: `pthread_cond_t` paired with `pthread_mutex_t`. `pthread_cond_wait(&cond, &mutex)` atomically releases the mutex and blocks; re-acquires it on wake. `pthread_cond_signal()` wakes one waiter; `pthread_cond_broadcast()` wakes all.
- **Java monitors**: Every Java object has an intrinsic lock. `synchronized` acquires it; `wait()` releases it and blocks on the object's implicit condition variable; `notify()`/`notifyAll()` signal it. Java 5+ added `ReentrantLock` + `Condition` for multiple condition variables per lock.
- **Futex-based implementation (Linux)**: pthreads condition variables use `futex()` internally. In the uncontended case, `signal` is a fast user-space atomic operation. Only when threads are actually blocked does the kernel get involved (via `FUTEX_WAKE`). This avoids syscall overhead in the common case.
- **Spurious wakeups**: POSIX allows `pthread_cond_wait()` to return even without a corresponding `signal` — an artifact of the implementation. This is another reason `while` loops are mandatory.

### Edge Cases and Pitfalls
- **`if` vs `while` bug**: Using `if (buffer.empty()) wait(not_empty)` under Mesa semantics → another thread may consume the item between signal and wakeup → the buffer is empty again → crash. Always use `while`.
- **Lost wake-up**: If `signal()` is called when no thread is waiting, the signal is lost (condition variables don't count). If a thread then calls `wait()`, it blocks forever. Solution: always check the predicate before waiting.
- **signal vs broadcast correctness**: Using `signal()` when multiple waiters could proceed (e.g., different conditions) may wake the "wrong" waiter, who re-blocks. `broadcast()` is safer but slower.
- **Nested monitor problem**: Thread holds monitor A, calls into monitor B, which calls `wait()` — thread releases B's lock but still holds A's lock → potential deadlock if B needs A.

### Real-World Systems
- **Java**: Intrinsic monitors (`synchronized` + `wait`/`notify`) for basic cases; `java.util.concurrent.locks.Condition` for multiple conditions per lock.
- **C/C++ (POSIX)**: `pthread_mutex_t` + `pthread_cond_t`; C++11 `std::condition_variable` + `std::mutex`.
- **Python**: `threading.Condition` wraps a lock with wait/notify; the GIL means only one thread runs Python at a time, but I/O-bound threads still benefit.
- **Go**: `sync.Cond` provides condition variable semantics; but idiomatic Go prefers channels over shared-memory synchronisation.
- **Rust**: `std::sync::Condvar` + `Mutex`; ownership model prevents most data races at compile time.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What does `wait(cond)` do atomically, and why is atomicity important here?
2. Under Mesa semantics, why must you use `while` instead of `if` when checking a condition?
3. What is the difference between `signal()` and `broadcast()`? When would you choose each?

### Core Problems
1. **Monitor-based bounded buffer**: Implement a thread-safe bounded buffer using POSIX mutexes and condition variables in C-like pseudocode. Support `produce(item)` and `consume() → item`. Test your implementation mentally: trace two producers and two consumers with buffer size 2. Verify no deadlock, no race, and no lost items.
2. **Semaphore-to-monitor translation**: Given this semaphore-based producer-consumer: `P(empty); P(mutex); add(); V(mutex); V(full)`. Rewrite it using a monitor with condition variables. What bugs does the monitor version prevent that the semaphore version is vulnerable to?

### Challenge
Implement a readers-writers lock using only a mutex and condition variables (no semaphores). Your implementation should support: (a) multiple concurrent readers, (b) exclusive writer access, (c) a configurable fairness policy (reader-prefer, writer-prefer, or FIFO). Provide pseudocode for `read_lock()`, `read_unlock()`, `write_lock()`, `write_unlock()`. Trace a scenario showing each fairness mode behaves differently for the sequence: R1, R2, W1, R3, W2.

---

*See also:* [[Semaphores]], [[Race Conditions and Mutual Exclusion]], [[Classic Synchronization Problems]]

## Supporting Chunks

- [[Synchronization - Monitors enforce mutual exclusion automatically at the language level]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 2.
