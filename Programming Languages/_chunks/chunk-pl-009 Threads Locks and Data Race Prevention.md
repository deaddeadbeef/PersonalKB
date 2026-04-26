---
tags: [chunk, programming-languages, concurrency]
source: "[[raw-pl-003]]"
---

# chunk-pl-009 Threads Locks and Data Race Prevention

**Traditional threading:** OS threads + mutex locks. Every mainstream language supports this. Problems: deadlocks, data races, priority inversion, complexity explosion.

**Rust's compile-time guarantee:** Send trait (transferable between threads) + Sync trait (accessible from multiple threads) + shared-xor-mutable rule. If it compiles, no data races. The strongest concurrency guarantee in any mainstream language.

**Java:** Mature threading: synchronized, java.util.concurrent, virtual threads (Java 21 — millions of lightweight threads on JVM).

**Go:** Convention-based safety. "Share memory by communicating." Race detector (go run -race) catches violations at runtime but can't prove absence.

**Erlang:** Data races impossible by design — no shared memory, all data immutable, processes communicate only via message passing.

Safety spectrum: Erlang (impossible) > Rust (compile-time proof) > Haskell STM (composable safety) > Go (convention + detection) > Java (model + primitives) > C/C++ (raw, your problem).
