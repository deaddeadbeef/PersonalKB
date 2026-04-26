---
tags: [programming-languages, memory-management]
up: "[[Programming Languages]]"
---

# Memory Management Overview

How a language manages memory is perhaps its most consequential low-level design decision. It determines performance characteristics, safety guarantees, and the mental model programmers must maintain. Every language answers the question: who is responsible for allocating and freeing memory?

## The Spectrum

| Strategy | Languages | Who Manages | Safety | Performance |
|----------|-----------|-------------|--------|-------------|
| Manual | C, C++ (raw), Zig | Programmer | Unsafe (use-after-free, leaks) | Maximum control |
| RAII | C++ (modern), Zig | Compiler via destructors | Semi-safe (dangling refs possible) | Deterministic |
| Ownership | Rust | Compiler via borrow checker | Safe (compile-time verified) | Zero-cost |
| Reference Counting | Swift, Python (CPython), Obj-C (ARC) | Runtime counter | Safe (cycles need handling) | Deterministic, overhead per ref |
| Tracing GC | Java, Go, C#, OCaml, Haskell, JS | Runtime collector | Safe | Throughput good, latency variable |
| Arena/Region | Zig, Rust (bumpalo), Go (experimental) | Programmer per region | Semi-safe | Bulk deallocation, cache-friendly |

## The Fundamental Trade-offs

**Safety vs. Control:** GC provides safety automatically but removes programmer control over deallocation timing. Manual management gives full control but enables memory bugs. Rust's ownership tries to provide both — safety with control — at the cost of compiler complexity.

**Throughput vs. Latency:** Tracing GC can achieve excellent throughput (amortizing collection costs) but introduces unpredictable pauses. Reference counting has predictable timing but adds per-operation overhead. Manual/ownership management has zero runtime overhead.

**Simplicity vs. Correctness:** Python's reference counting is simple to understand but has the cycle problem. OCaml's GC is simple to use but complex internally. Rust's borrow checker is correct but has a steep learning curve.

## In This Hub

- [[Manual Memory Management]]
- [[Garbage Collection Strategies]]
- [[Reference Counting]]
- [[Ownership and Borrowing]]
- [[Value Types vs Reference Types]]

## References

- [[Sources Index]]
