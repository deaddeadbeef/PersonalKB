---
tags: [programming-languages, concurrency, stm]
up: "[[Concurrency Models Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Software Transactional Memory

> **Database-style transactions for shared memory let concurrent code commit atomically or retry automatically instead of coordinating with locks.**

## 🎯 Intuition
**The Core Idea:** Software Transactional Memory (STM) applies database transaction concepts to in-memory concurrency.

**Analogy:** STM is like editing a shared Google Doc: everyone works on their own draft; when you save, the system checks if anyone else changed the same paragraphs — if so, you revise and retry.

**Why It Matters:** Instead of locks, programmers wrap shared-state operations in transactions that either commit atomically or retry. It's the most elegant concurrency model — and the least adopted in mainstream languages.

Software Transactional Memory (STM) applies database transaction concepts to in-memory concurrency. Instead of locks, programmers wrap shared-state operations in transactions that either commit atomically or retry. It's the most elegant concurrency model — and the least adopted in mainstream languages.

---

## ⚙️ Core Mechanics

### How It Works

A transaction reads and writes shared variables within a delimited block. At commit time, the runtime checks if any variables were modified by other transactions since they were read. If not, the transaction commits atomically. If yes, the transaction aborts and retries automatically. This is **optimistic concurrency control** applied to memory.

### Key Concepts

| Concept | Meaning |
|---|---|
| Transaction | A delimited block that reads and writes shared variables |
| Commit | The runtime verifies that nothing relevant changed and applies updates atomically |
| Abort and retry | If another transaction modified something that was read, the current transaction is re-executed |
| Optimistic concurrency control | Assume conflicts are rare, then validate at commit time |

| Language/runtime constraint | Why it matters |
|---|---|
| No I/O inside transactions | Transactions may be re-executed multiple times |
| Controlled side effects | Safe retry depends on being able to re-run code without observable external effects |
| Snapshot semantics | A transaction can operate on a consistent view of shared state |

### Language Examples

#### Haskell STM

Haskell provides the purest STM implementation via the STM monad:

```haskell
transfer :: TVar Int -> TVar Int -> Int -> STM ()
transfer from to amount = do
    fromBal <- readTVar from
    toBal <- readTVar to
    writeTVar from (fromBal - amount)
    writeTVar to (toBal + amount)
```

Key properties of Haskell STM:
- **Composability:** Transactions compose — `transfer a b 100 >> transfer c d 200` is a single atomic transaction. This solves the fundamental composition problem of locks.
- **No deadlocks:** There are no locks, so deadlock is impossible.
- **Retry:** If a transaction can't proceed (e.g., insufficient balance), `retry` blocks until a relevant variable changes, then automatically re-executes.
- **Type safety:** The STM monad ensures you can't perform I/O inside a transaction — only memory operations are allowed. This is essential because transactions may be re-executed multiple times.

Haskell's purity makes STM particularly elegant: since the type system tracks side effects, the runtime can safely re-execute transactions knowing they have no observable side effects.

#### Clojure Refs and STM

Clojure includes STM as a core language feature. `ref` creates a transactional reference, and `dosync` delimits transactions:

```clojure
(dosync
  (alter account-a - 100)
  (alter account-b + 100))
```

Clojure's STM uses Multi-Version Concurrency Control (MVCC), similar to PostgreSQL. Each transaction sees a consistent snapshot of the world. Clojure also provides `atom` (single uncoordinated reference, like an atomic variable) and `agent` (asynchronous update), giving programmers a spectrum of concurrency tools.

### Key Facts

- STM replaces lock-based coordination with transactional shared-memory updates.
- Transactions either commit atomically or abort and retry automatically.
- The strongest STM story appears in languages that can control or track side effects.
- Haskell and Clojure are the canonical mainstream language examples discussed here.

---

## 🔬 Deep Dive

### Formal Foundations

STM applies database transaction concepts to in-memory concurrency. A transaction reads and writes shared variables within a delimited block. At commit time, the runtime checks if any variables were modified by other transactions since they were read. If not, the transaction commits atomically. If yes, the transaction aborts and retries automatically. This is **optimistic concurrency control** applied to memory.

In Clojure, STM uses Multi-Version Concurrency Control (MVCC), similar to PostgreSQL. Each transaction sees a consistent snapshot of the world.

### Trade-offs and Design Decisions

#### Why STM Hasn't Gone Mainstream

Despite its elegance, STM has limited adoption outside Haskell and Clojure:

1. **Performance overhead:** Transaction bookkeeping, version tracking, and retries add overhead compared to fine-grained locks
2. **Unpredictable retries:** Under high contention, transactions may retry many times, making performance hard to predict
3. **I/O restriction:** Transactions can't perform I/O (since they might retry), limiting what code can be transactional
4. **Imperative mismatch:** STM works best in languages with controlled side effects. In Java or C++, where any code might have side effects, safe retry is impossible without pervasive purity tracking

### Historical Context

#### The Deeper Lesson

STM's limited adoption illustrates a recurring theme in language design: technically superior solutions don't always win. Locks are conceptually simple (even if error-prone), async/await maps to familiar sequential code, and message passing is easy to reason about. STM requires thinking in transactions — a mental model most programmers don't already have.

However, STM's influence persists: database-style transactions in concurrent systems (Datomic, CRDTs), compare-and-swap atomics (a single-variable STM), and the general principle that composable concurrency primitives are more valuable than high-performance non-composable ones.

---

## 🏋️ Practice

### Warm-Up (5 min) — 3 conceptual questions

1. Why does STM use retries instead of locking threads until a conflict disappears?
2. Why is performing I/O inside a transaction unsafe in an STM system?
3. Why does composability make STM more attractive than locks in principle?

### Core Problems — 2 problems

1. Compare a bank-transfer implemented with locks versus with STM. Which parts of the correctness story get simpler, and which performance concerns get harder?
2. Suppose transactions are frequently aborting under high contention. Based on this page, explain why that happens and what it does to predictability.

### Challenge — 1 design problem

Design a concurrency strategy for an application that needs to update several shared values atomically while also performing network I/O. Which parts would you put inside STM transactions, which parts would stay outside, and why?

---

*See also:* [[Concurrency Models Overview]], [[Sources Index]]

## Supporting Chunks / References

- [[Sources Index]]

## References
- [[Programming Languages/Sources/Sources Index|Programming Languages Sources Index]]
