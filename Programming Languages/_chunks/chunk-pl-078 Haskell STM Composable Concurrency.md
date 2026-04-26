---
tags: [chunk, programming-languages, concurrency-models]
source: "[[raw-pl-019]]"
---

# chunk-pl-078 Haskell STM Composable Concurrency

Software Transactional Memory in Haskell:

**Core idea:** Treat shared memory access as database transactions. Read and write TVar (transactional variables) within atomically blocks. Conflicts cause automatic retry.

**Composability:** The killer feature. Transfer money: tomically (withdraw a amount >> deposit b amount). Two STM operations composed into one atomic transaction. With locks, composing two locked operations requires careful lock ordering and risks deadlock.

**Type safety:** STM operations can only compose with other STM operations. The type system prevents mixing STM with arbitrary IO. You can't accidentally do I/O inside a transaction (which would be re-executed on retry).

**retry:** etry blocks the transaction until a read variable changes, then re-executes. Enables waiting-for-condition patterns without busy-waiting.

**orElse:** orElse action1 action2 — try action1; if it retries, try action2. Enables composable alternatives.

**Why not mainstream:** Performance overhead (transaction bookkeeping, copying values), can't do I/O in transactions, and most languages chose locks/channels/async. But for correctness-critical concurrent code, STM's composability is unmatched.
