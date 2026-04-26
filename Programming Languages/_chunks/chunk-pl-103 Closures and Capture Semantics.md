---
tags: [chunk, programming-languages, closures]
source: "[[raw-pl-020]]"
---

# chunk-pl-103 Closures and Capture Semantics

A closure is a function that captures variables from its enclosing scope.

**JavaScript:** Closures capture by reference. Inner function sees changes to outer variable. This is why ar in loops is surprising (all closures share the same variable). let fixes this with block scoping.

**Python:** Closures capture by reference but with quirks. Lambda captures the variable name, not the value. [lambda: i for i in range(3)] all return 2 (the final value of i). Fix: default argument lambda i=i: i.

**Rust:** Three capture modes determined by usage:
- Fn: borrow immutably (&T)
- FnMut: borrow mutably (&mut T)
- FnOnce: take ownership (move)
The compiler infers which mode. move keyword forces ownership transfer.

**C++:** Explicit capture specification:
- [&]: capture all by reference
- [=]: capture all by value (copy)
- [x, &y]: x by value, y by reference

**Go:** Closures capture by reference. Goroutine + closure = common bug when loop variable is captured. go func(v int) { use(v) }(i) passes by value instead.

**Swift:** Closures capture by reference by default. [weak self] and [unowned self] capture lists prevent retain cycles.

Capture semantics interact with concurrency: closures sent to other threads must capture safely. Rust's type system enforces this (Send/Sync bounds on closures).
