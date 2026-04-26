---
tags: [chunk, programming-languages, concurrency-patterns]
source: "[[raw-pl-019]]"
---

# chunk-pl-098 Concurrency Patterns and Best Practices

**Fan-out/Fan-in (Go):** Launch N goroutines (fan-out), collect results via channel (fan-in). Pattern for parallel processing of independent work items.

**Worker pool (Go, Rust):** Fixed number of worker goroutines/tasks consuming from a shared channel/queue. Controls resource usage while processing items concurrently.

**Select/Multiplex (Go):** select waits on multiple channels simultaneously. First ready channel wins. Timeout via 	ime.After. Used for: combining multiple sources, implementing timeouts, cancellation.

**Structured concurrency (Kotlin, Swift, Java 21):** Child tasks tied to parent scope. Parent waits for children. Cancellation propagates. No orphaned tasks. Prevents resource leaks.

**Back-pressure (Rust tokio, Elixir GenStage):** When consumer is slower than producer, signal producer to slow down. Prevents unbounded queue growth. Essential for production systems.

**Share nothing (Erlang):** Processes share no memory. All communication via message passing. Data copied between processes. Eliminates data races by construction. Scale by adding processes, not threads.

**Lock-free data structures (C++, Rust, Java):** CAS (Compare-And-Swap) operations instead of locks. Higher throughput under contention. Much harder to implement correctly. crossbeam (Rust), java.util.concurrent.atomic.
