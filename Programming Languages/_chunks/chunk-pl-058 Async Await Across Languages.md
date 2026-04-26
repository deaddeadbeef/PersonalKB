---
tags: [chunk, programming-languages, async]
source: "[[raw-pl-019]]"
---

# chunk-pl-058 Async Await Across Languages

Cooperative multitasking: functions yield at await points, allowing other tasks to run on the same thread.

**JavaScript:** Single-threaded event loop. All I/O non-blocking. Evolution: callbacks -> Promises -> async/await. Data races impossible (one thread). CPU work blocks everything.

**Python asyncio:** Single-threaded for I/O-bound workloads. GIL means even threads are single-threaded for CPU. Good for network-heavy servers, not CPU-bound.

**Rust async:** Zero-cost futures compiled to state machines. No heap allocation for futures themselves. But: lifetime + async interaction is complex. Pin prevents moving self-referential futures. tokio won the runtime war.

**C# async:** Pioneered modern async/await syntax (2012). Task-based. Integrated with .NET runtime. Influenced every subsequent language's async design.

**Kotlin coroutines:** Structured concurrency. Scoped (coroutineScope), cancellable, parent-child relationships. More ergonomic than Java's CompletableFuture.

**Swift async:** Actor-based isolation. Structured concurrency. Compiler prevents accessing actor state from outside. Integrated with Apple's Combine framework.
