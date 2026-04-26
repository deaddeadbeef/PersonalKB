---
tags: [cs-os, raw]
source_type: textbook_topic
source_title: "Kernel Synchronization Primitives"
authors: Love; McKenney; Corbet, Rubini, Kroah-Hartman
year: 2010
---

# Kernel Synchronization Primitives

## Summary

Kernel synchronization primitives protect shared data structures within the operating system kernel, where concurrency arises from multiple CPUs, interrupts, preemption, and softirqs executing kernel code simultaneously. Unlike user-space synchronization (pthreads mutexes, condition variables), kernel primitives must handle interrupt contexts, non-preemptible regions, and the absence of a scheduler to block on.

**Spinlocks** are the most basic kernel lock. A thread attempting to acquire a held spinlock busy-waits in a tight loop, consuming CPU cycles until the lock is released. Spinlocks are appropriate for short critical sections in interrupt context (where sleeping is forbidden) and on multiprocessor systems. On uniprocessor kernels, spinlocks degenerate to disabling preemption. The `spin_lock_irqsave()` variant disables local interrupts while holding the lock, preventing interrupt handlers from deadlocking on the same lock.

**Mutexes** (`struct mutex` in Linux) are sleeping locks: if the lock is held, the waiting thread is put to sleep and woken when the lock becomes available. They are more efficient than spinlocks for long critical sections because they don't waste CPU cycles spinning, but they cannot be used in interrupt context (you cannot sleep in an interrupt handler). Mutexes enforce strict ownership—only the lock holder can release it.

**Reader-writer locks** (`rwlock_t` for spinlock variant, `struct rw_semaphore` for sleeping variant) allow concurrent readers but exclusive writers. They improve throughput for read-dominated workloads but can cause writer starvation if readers continuously acquire the lock.

**RCU (Read-Copy-Update)** is a high-performance synchronization mechanism optimized for read-mostly data structures. Readers access shared data without acquiring any locks, incurring zero overhead. Writers create a modified copy of the data structure, atomically update the pointer to the new version, and defer freeing the old version until all pre-existing readers have completed (a "grace period"). In Linux, `rcu_read_lock()`/`rcu_read_unlock()` delimit the read-side critical section (which simply disables preemption), and `synchronize_rcu()` or `call_rcu()` handle grace period waiting. RCU is used extensively in the Linux kernel for routing tables, the dcache, and module lists.

**Sequential locks (seqlocks)** protect data read frequently but written rarely. Writers increment a sequence counter before and after writing; readers read the counter before and after reading data, retrying if the counter changed (indicating a concurrent write). Seqlocks favor writers—writers never block, even if readers are active.

**Per-CPU variables** avoid synchronization entirely by maintaining separate copies of a variable for each CPU. Access requires disabling preemption (`get_cpu_var()`/`put_cpu_var()`) to ensure the accessing thread isn't migrated mid-operation.

**Memory barriers** (`mb()`, `rmb()`, `wmb()`, `smp_mb()`) enforce ordering of memory operations, which is necessary because modern CPUs and compilers may reorder reads and writes for performance. Atomic operations (`atomic_t`, `atomic_inc()`, `atomic_cmpxchg()`) provide indivisible read-modify-write operations on shared variables.

## Key Claims

- Spinlocks are the appropriate primitive for short critical sections in interrupt context where sleeping is forbidden, degenerating to preemption disabling on uniprocessor systems
- RCU achieves near-zero read-side overhead by allowing lock-free reads and deferring memory reclamation until all pre-existing readers complete, making it ideal for read-mostly kernel data structures
- Mutexes provide sleeping semantics that avoid wasting CPU cycles on contention but cannot be used in interrupt context due to the prohibition on sleeping in interrupt handlers
- Seqlocks favor writers by never blocking them, at the cost of forcing readers to retry when concurrent writes are detected via the sequence counter mechanism
- Memory barriers are essential on modern out-of-order CPUs to enforce the ordering of memory operations that synchronization algorithms depend on, preventing subtle bugs invisible in sequential reasoning

## Atomic Facts

1. Linux spinlocks use ticket locks or queued spinlocks (MCS-based since kernel 3.15) to ensure fairness and prevent cache-line bouncing on NUMA systems
2. RCU grace period detection in Linux relies on each CPU passing through a quiescent state (voluntary context switch, idle, or user mode), after which all pre-existing RCU read-side critical sections are guaranteed complete
3. `spin_lock_irqsave(lock, flags)` saves the current interrupt state in `flags`, disables local interrupts, and acquires the spinlock; `spin_unlock_irqrestore(lock, flags)` reverses both operations
4. The Linux kernel contains over 100,000 uses of RCU in the 6.x kernel tree, including the networking routing table, dcache (directory entry cache), and PID lookup hash table
5. Seqlocks are used in the Linux kernel for `jiffies` (system timer tick count) and `xtime` (wall-clock time), where timer interrupts write frequently but many readers need consistent timestamps
6. `atomic_cmpxchg(v, old, new)` atomically compares `*v` with `old` and sets it to `new` if equal, returning the original value; this is the foundation of lock-free algorithms

## Significance

Kernel synchronization primitives are the foundation of correctness and performance in multiprocessor operating systems. The spectrum from spinlocks (simple, busy-wait) through mutexes (sleeping) to RCU (lock-free reads) reflects the kernel's need for different tradeoffs at different performance points. RCU in particular is one of the most important innovations in kernel concurrency, enabling Linux to scale efficiently to hundreds of CPUs. Understanding these primitives is essential for kernel development, driver writing, and comprehending how modern operating systems achieve both correctness and performance under concurrent access.

## Chunks Extracted

*Pending*
