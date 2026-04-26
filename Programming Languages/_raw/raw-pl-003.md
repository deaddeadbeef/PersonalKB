---
tags: [raw, programming-languages, concurrency]
source: "Communicating Sequential Processes (Hoare, 1978), Seven Concurrency Models (Butcher, 2014)"
created: 2025-07-25
---

# raw-pl-003: Concurrency Models in Practice

## Threads and Locks (Traditional Model)

OS threads with mutual exclusion locks. Every mainstream language supports this. Problems: deadlocks (threads wait for each other forever), data races (unsynchronized access to shared data), priority inversion, and complexity explosion as thread count grows.

**Java:** Mature threading model with synchronized keyword, java.util.concurrent, and virtual threads (Project Loom, Java 21). Virtual threads are lightweight (similar to goroutines) — millions per JVM.

**C++:** std::thread, std::mutex, std::atomic. Low-level control. No runtime safety net.

**Rust:** std::thread with ownership-based safety. The compiler prevents data races: if a type doesn't implement Send, it can't be shared across threads. If it doesn't implement Sync, it can't be accessed from multiple threads. This is compile-time concurrency safety — unique to Rust.

## CSP and Channels (Go, Rust)

Communicating Sequential Processes (Hoare, 1978): independent processes communicate by sending messages through channels. No shared memory — data is sent, not shared.

**Go:** Goroutines (lightweight green threads, 4KB stack) communicate via channels. select multiplexes over multiple channels. The Go runtime schedules goroutines onto OS threads (M:N scheduling). Go's concurrency model is its strongest feature.

**Rust:** std::sync::mpsc provides channels. Tokio provides async channels. Rust combines channels with ownership: sending a value through a channel transfers ownership — the sender can't use it after sending. This prevents data races on channel-communicated values.

## Actor Model (Erlang, Akka)

Actors are independent entities with private state that communicate via asynchronous messages. Each actor has a mailbox (message queue). Actors process one message at a time — no concurrency within an actor, so no locks needed.

**Erlang/Elixir:** The actor model is fundamental. BEAM processes ARE actors. Millions per node. Fault tolerance via supervision trees. The "let it crash" philosophy.

**Akka (JVM):** Actor framework for Scala/Java. Brings Erlang-style actors to the JVM ecosystem.

**Swift:** Swift 5.5+ has actors as a language-level construct. Actor methods are async and the compiler prevents direct access to actor state from outside.

## Async/Await (JavaScript, Python, Rust, C#, Kotlin)

Cooperative multitasking: functions yield control at await points, allowing other tasks to run on the same thread. No threads, no locks — concurrency without parallelism (unless combined with multi-threading).

**JavaScript:** Single-threaded event loop with Promises and async/await. All I/O is non-blocking. The model is simple: no data races possible because there's only one thread.

**Rust:** async/await with futures and the tokio or async-std runtime. Rust's async is zero-cost: futures are state machines compiled to efficient code. But: lifetime interaction with async is complex, Pin is confusing, and the ecosystem split between runtimes is a pain point.

**Python:** asyncio with async/await. Single-threaded cooperative multitasking for I/O-bound workloads. The GIL means even threaded Python is effectively single-threaded for CPU work.

## Software Transactional Memory (Haskell, Clojure)

STM treats memory operations like database transactions: read and write shared variables within a transaction; if there's a conflict, the transaction retries. Haskell's STM is the gold standard — composable (transactions can be nested), type-safe (STM operations can only be composed with other STM operations), and deadlock-free.

Clojure's refs and dosync provide STM for managed references. The philosophy: make state changes explicit, transactional, and composable.
