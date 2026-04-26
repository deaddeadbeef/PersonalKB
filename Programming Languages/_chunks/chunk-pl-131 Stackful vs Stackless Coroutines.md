---
tags: [pl, chunk, coroutines, continuations]
up: "[[Concurrency Models Overview]]"
---

# Stackful vs Stackless Coroutines

Coroutine implementation choice fundamentally affects performance and flexibility.

## Stackful Coroutines
Each coroutine has its own call stack and can yield from any depth:
- **Go goroutines:** 2KB initial stack, grows dynamically to 1GB. Runtime scheduler multiplexes onto OS threads. Can yield from any function call depth.
- **Java Virtual Threads (Loom):** Lightweight threads mounted on carrier OS threads. Can yield at any blocking point.
- **Lua coroutines:** First-class stackful coroutines with explicit resume/yield.

## Stackless Coroutines
Compiler transforms the function into a state machine — no separate stack:
- **Rust async:** Each await point becomes a state in an enum. The Future is as small as the data it holds.
- **C++ coroutines (C++20):** Coroutine frame allocated on heap (or optimized away). Customization points (promise_type) give low-level control.
- **Kotlin coroutines:** CPS (Continuation-Passing Style) transformation at compile time.

## The Colored Function Problem
Stackless coroutines create "function colors" — async functions can only be called from other async functions:
- **JavaScript:** sync function vs regular unction
- **Python:** sync def vs def
- **Rust:** sync fn vs n (but can bridge with lock_on)
- **Go:** No coloring — goroutines are transparent
- **Java Loom:** No coloring — virtual threads are transparent

Zig's approach: make async transparent — the compiler chooses the right calling convention.

## Memory Comparison

| Implementation | Per-Coroutine Memory | Context Switch |
|---------------|---------------------|----------------|
| Go goroutine | 2KB-1GB (dynamic) | ~200ns |
| Java Virtual Thread | ~few KB | ~200ns |
| Rust Future | State size (often < 100 bytes) | ~10ns (inlined) |
| C++ coroutine | Frame size | ~20ns |
| OS thread | 1-8MB (fixed) | ~1-10µs |

## Key Insight
Stackful coroutines (Go, Loom) are simpler to use (no function coloring) but cost more memory. Stackless coroutines (Rust, C++) are zero-cost but require viral async annotations. The industry hasn't settled on which trade-off is better.

## References
→ [[Sources Index]]
