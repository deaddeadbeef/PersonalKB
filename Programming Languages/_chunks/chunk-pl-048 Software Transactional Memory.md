---
tags: [chunk, programming-languages, stm]
source: "[[raw-pl-003]]"
---

# chunk-pl-048 Software Transactional Memory

STM treats memory operations like database transactions. Read and write shared variables within a transaction; if conflict, retry automatically.

**Haskell STM:** The gold standard. Properties:
- **Composable:** Transactions can be nested and combined (unlike locks, which compose unsafely)
- **Type-safe:** STM operations compose only with other STM operations (not arbitrary IO)
- **Deadlock-free:** No locks means no deadlocks
- **Retry:** \etry\ blocks until a read variable changes, then re-executes
- **OrElse:** Try one transaction; if it retries, try another

**Clojure refs + dosync:** STM for managed references. Coordinated changes to multiple refs within a transaction. Uses MVCC (Multi-Version Concurrency Control).

**Why STM isn't mainstream:** Performance overhead (transaction bookkeeping), limited to memory operations (can't do I/O in a transaction — it might retry), and most languages chose locks/channels/async instead.

STM's composability advantage: \	ransfer(a, b, amount) = atomically { withdraw a amount >> deposit b amount }\ — composing two transactions into one is trivial. With locks, composing two locked operations requires careful lock ordering.
