---
tags: [raw, programming-languages, concurrency-safety]
source: "Rust Reference, Go Concurrency Patterns, Erlang documentation"
created: 2025-07-25
---

# raw-pl-019: Concurrency Safety Guarantees

## The Data Race Problem

A data race occurs when two threads access the same memory location, at least one is writing, and there's no synchronization. Data races cause: corrupted data, crashes, security vulnerabilities, and bugs that are nearly impossible to reproduce.

## Rust's Compile-Time Guarantee

Rust prevents data races through the type system:
- Send: A type can be transferred between threads. Most types are Send.
- Sync: A type can be referenced from multiple threads. Rc<T> is NOT Sync (use Arc<T> instead).
- Shared XOR mutable: You can have many shared references (&T) OR one mutable reference (&mut T), never both.

If it compiles, there are no data races. Period. This is the strongest concurrency guarantee in any mainstream language.

## Go's Approach: Convention + Tools

Go doesn't prevent data races at compile time. Instead:
- Convention: "Share memory by communicating" (channels over shared state)
- Runtime detection: go run -race enables the race detector (finds races at runtime)
- Sync primitives: sync.Mutex, sync.RWMutex, sync.WaitGroup

Go trusts programmers to follow conventions. The race detector catches violations at test time but can't prove their absence.

## Java's Approach: Memory Model + Primitives

Java has a formal memory model (JSR 133) defining how threads interact with memory. Primitives: synchronized blocks, volatile fields, java.util.concurrent (ConcurrentHashMap, AtomicInteger, locks, executors). Virtual threads (Java 21) simplify concurrent programming but don't eliminate data races.

## Erlang: Data Races Impossible by Design

Erlang processes share no memory. All data is immutable. Processes communicate via message passing (messages are copied). Data races are impossible by construction — there's no shared mutable state to race on.

## Haskell STM: Composable Transactions

Software Transactional Memory: wrap shared state access in atomic transactions. If two transactions conflict, one retries automatically. STM is composable: you can combine transactions (unlike locks, which compose unsafely). Type safety: STM operations can only be composed with other STM operations (not with arbitrary IO).

## The Safety Spectrum

Erlang (impossible) > Rust (compile-time proof) > Haskell STM (composable safety) > Go (convention + runtime detection) > Java (model + primitives) > C++ (raw threads, your problem) > C (what's a thread?)

## Async Concurrency Safety

Async/await (JS, Python, Rust, C#, Kotlin) avoids many concurrency issues by running on fewer threads. JavaScript: single-threaded, data races impossible. Python: GIL makes bytecode execution single-threaded. Rust async: same ownership rules apply, borrow checker prevents races even in async code.
