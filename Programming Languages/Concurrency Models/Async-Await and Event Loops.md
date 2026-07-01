---
tags: [programming-languages, concurrency, async]
up: "[[Concurrency Models Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---

# Async-Await and Event Loops

> Async/await is the most widely adopted concurrency pattern of the 2010s-2020s — it lets you write concurrent code that looks sequential, hiding the complexity of callback-based or thread-based concurrency behind familiar syntax.

---

## 🎯 Intuition

### Core Idea

Many programs spend most of their time waiting: for network responses, database queries, file I/O, user input. Dedicating an OS thread to each waiting operation wastes resources (threads are expensive: ~1 MB stack each, context-switch overhead). Async programming allows thousands of concurrent I/O operations using a small number of threads. Async/await provides a way to express this concurrency in code that reads like ordinary sequential logic.

### Analogy

Async/await is like **a restaurant waiter who takes multiple orders and checks on each table in turn**, rather than standing by one table until the food arrives. The waiter (event loop) serves many tables (tasks) concurrently without cloning themselves (spawning threads). When one table's food isn't ready, they move on; when it is, they come back to deliver it. A single attentive waiter can handle a surprisingly large dining room — just as a single-threaded event loop can handle thousands of concurrent I/O operations.

### Why It Matters

- Scales I/O-heavy workloads (web servers, APIs, UIs) without the memory and context-switch cost of one-thread-per-request.
- Eliminates "callback hell" — deeply nested, hard-to-follow callback chains — by making asynchronous control flow read top-to-bottom.
- Has become the dominant concurrency model across JavaScript, C#, Python, Rust, Swift, and Kotlin.

---

## ⚙️ Core Mechanics

### How It Works

1. **Event Loop** — A central loop repeatedly checks for completed I/O events and dispatches the corresponding continuations. JavaScript pioneered this model: one thread, one loop, all I/O non-blocking. You register a callback (or await a promise/future), the runtime manages the I/O, and your code resumes when the result is ready.
2. **State Machine Transformation** — The compiler rewrites each async function into a state machine. Every `await` becomes a state transition point. The generated code manages suspension and resumption automatically, so the programmer writes straight-line code while the runtime drives it cooperatively. C# pioneered this approach and nearly every subsequent language adopted it.

### Key Concepts

| Concept | Description |
|---|---|
| **Coroutine** | A function that can suspend and resume; the foundation beneath async/await |
| **Future / Promise / Task** | A handle representing a value that will be available later |
| **Event Loop** | The scheduler that polls for I/O readiness and resumes suspended coroutines |
| **Executor / Runtime** | The component that drives futures to completion (explicit in Rust, implicit elsewhere) |
| **Structured Concurrency** | Child tasks are scoped to a parent; the parent cannot exit until children finish |
| **Cooperative Scheduling** | Tasks yield control voluntarily at `await` points; no preemption |

### Language Examples

**JavaScript** — Pioneered mainstream async with its single-threaded event loop. Evolution: raw callbacks → Promises (composable callbacks) → async/await syntax (ES2017). One thread, one event loop, no parallelism within a single context — this eliminates data races entirely but means CPU-intensive work blocks the loop. Web Workers provide separate execution contexts for CPU parallelism.

**C#** — Introduced async/await in version 5.0 (2012), establishing the pattern most other languages adopted. `async` marks a method as asynchronous; `await` suspends execution until a `Task` completes. The runtime uses a thread pool to schedule continuations. C#'s key innovation was the compile-time state-machine transformation: each `await` becomes a state transition, and the generated code manages suspension and resumption automatically.

**Rust** — Async/await stabilized in 2019. Futures are lazy (don't execute until polled), zero-cost (no heap allocation for the state machine by default), and poll-based (the executor drives futures by calling `poll()` rather than futures pushing results to callbacks). The async runtime is not built into the language — it's a library (tokio, async-std, smol), aligning with Rust's "zero-cost abstraction" philosophy. Trade-off: more complex setup and the infamous "async Rust is hard" learning curve, including lifetime issues with async references.

**Python** — Added asyncio (3.4, 2014) and async/await syntax (3.5, 2015). Single-threaded like JavaScript, using a cooperative event loop. `await` yields control to the loop, which resumes coroutines when their I/O completes. The GIL means async doesn't help with CPU parallelism, but it excels at I/O concurrency.

**Swift** — Swift 5.5 (2021) introduced async/await with **structured concurrency**: async tasks form a tree where parent tasks implicitly wait for child tasks to complete. `TaskGroup` and `async let` create child tasks guaranteed to finish before the parent scope exits. This prevents fire-and-forget task leaks — a common source of bugs in other async systems.

**Kotlin** — Coroutines provide async-like functionality with a different vocabulary: `suspend` functions, `CoroutineScope`, and structured concurrency (from Kotlin's own research, which later influenced Swift). Coroutines compile to state machines on the JVM, similar to C#'s approach.

**Go (absence)** — Go deliberately chose NOT to have async/await. Goroutines are already lightweight enough that blocking I/O in a goroutine is efficient — the Go runtime handles the multiplexing internally. Key philosophical difference: where JavaScript/Python need async because threads are expensive, Go makes threads (goroutines) cheap enough that async syntax is unnecessary.

### Key Facts

| Language | Year | Threading | Runtime | Structured Concurrency |
|---|---|---|---|---|
| JavaScript | 2017 (ES2017) | Single-threaded | Built-in event loop | No (manual) |
| C# | 2012 (v5.0) | Multi-threaded (thread pool) | Built-in (CLR) | No (manual) |
| Rust | 2019 (1.39) | Configurable | Library (tokio, etc.) | No (manual) |
| Python | 2015 (3.5) | Single-threaded (GIL) | Built-in (asyncio) | No (manual) |
| Swift | 2021 (5.5) | Multi-threaded | Built-in | Yes (TaskGroup, async let) |
| Kotlin | 2018 (1.3) | Multi-threaded (JVM) | Library (kotlinx.coroutines) | Yes (CoroutineScope) |
| Go | — | Multi-threaded (goroutines) | Built-in (goroutine scheduler) | N/A — no async/await |

---

## 🔬 Deep Dive

### Formal Foundations: State Machine Transformation

The compiler rewrites every async function into a state machine struct/class. Local variables that live across `await` points are lifted into fields of that struct. Each `await` is a yield point: the machine returns control to the executor with a "pending" status and a handle for resumption. When the awaited future completes, the executor advances the machine to the next state. This transformation is why async/await has near-zero syntactic overhead at the source level but non-trivial generated code underneath. In Rust, the state machine is an enum whose size is the max of all states — no heap allocation required. In C# and Kotlin, the state machine is a class allocated on the heap (though C# applies optimizations for synchronously completing paths via `ValueTask`).

### Trade-offs and Design Decisions: The Coloring Problem

A well-known critique of async/await: it creates a **"function color" split**. Async functions can only be called from other async functions (or with special bridging effort). This splits the ecosystem into sync and async halves that don't compose easily — libraries must be duplicated or wrapped, and mixing the two colors at API boundaries is friction-heavy. This critique, articulated by Bob Nystrom in *"What Color is Your Function?"* (2015), directly influenced Go's design (no coloring — goroutines are "colorless") and Zig's approach (non-coloring async). Languages with the coloring problem include JavaScript, C#, Python, Rust, Swift, and Kotlin.

### Historical Context

- **1960s–70s** — Coroutines appear in Simula and Modula-2; cooperative multitasking in early OSes.
- **1995** — JavaScript ships with a single-threaded event loop; callbacks become the concurrency primitive for the web.
- **2009** — Node.js brings the event-loop model to server-side programming, exposing callback hell at scale.
- **2012** — C# 5.0 ships async/await, establishing the compile-to-state-machine pattern.
- **2014–15** — Python adds asyncio (3.4) then async/await syntax (3.5).
- **2015** — Bob Nystrom publishes "What Color is Your Function?", crystallizing the coloring critique.
- **2017** — ES2017 standardizes async/await in JavaScript.
- **2018** — Kotlin 1.3 stabilizes coroutines.
- **2019** — Rust 1.39 stabilizes async/await with zero-cost, poll-based futures.
- **2021** — Swift 5.5 ships async/await with structured concurrency.

---

## 🏋️ Practice

### Warm-Up

1. A JavaScript `async` function always returns a ______. What happens if you call it without `await`?
2. Explain why a `while(true)` loop with no `await` inside an async function will freeze a single-threaded event loop (JavaScript/Python) but not necessarily a multi-threaded runtime (C#).
3. In Rust, futures are *lazy* — they don't run until polled. What would happen if you wrote `async { fetch(url) }` but never `.await`ed or spawned it?

### Core Problems

4. You have an async C# method that calls three independent web APIs sequentially with `await`. Refactor it to issue all three requests concurrently and wait for all of them. Which API would you use, and what changes about error handling?
5. Design a small async task scheduler (pseudocode) that uses a single thread and an event loop to run multiple coroutines cooperatively. Show how `await` points allow interleaving.

### Challenge

6. A codebase mixes sync and async code heavily, causing deadlocks when sync callers `.Result`-block on async methods in C# (or `asyncio.run()` inside a running loop in Python). Diagnose why this deadlock occurs, propose at least two mitigation strategies, and discuss how Go's goroutine model sidesteps this entire class of problems.

---

*See also:* [[Concurrency Models Overview]] · [[Programming Languages/_chunks/chunk-pl-131 Stackful vs Stackless Coroutines|Coroutines and Fibers]] · [[Programming Languages/Concurrency Models/Threads and Locks|Thread Pools and Work Stealing]] · [[Programming Languages/_chunks/chunk-pl-147 Structured Concurrency The Next Paradigm|Structured Concurrency]]

---

## Supporting Chunks / References

- [[Programming Languages/Sources/Sources Index|Sources Index]]

## References

- [[Programming Languages/Sources/Sources Index]]
- [[Programming Languages/Programming Languages Book Reading Spine]]
- [[Programming Languages/Programming Languages]]
