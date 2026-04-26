---
tags: [chunk, programming-languages, convergence]
source: "[[raw-pl-025]]"
---

# chunk-pl-120 Language Convergence The Great Merge

Modern languages are converging on a shared feature set:

**Features now universal:** First-class functions, closures, generics/parametric polymorphism, pattern matching, async/await, iterators/streams, type inference (at least local), null safety (or options), immutability options.

**What still differentiates:**
- **Default mutability:** Rust/Kotlin (immutable default) vs Go/Java/Python (mutable default)
- **Memory model:** GC (Go, Java, OCaml) vs ownership (Rust) vs RC (Swift) vs manual (C, Zig)
- **Runtime size:** JVM (heavy) vs Go (moderate) vs Rust (minimal) vs C (none)
- **Compilation model:** AOT (Rust, Go) vs JIT (Java, JS) vs interpreted (Python)
- **Ecosystem:** npm (JS), PyPI (Python), Maven (Java), crates.io (Rust)

**The convergence pattern:** Rust adds async. Go adds generics. Java adds records + pattern matching + virtual threads. Python adds type hints. C++ adds concepts + constexpr. Each language absorbs the best ideas from others.

**What won't converge:** The defaults and the runtime model. These are the deepest design decisions and can't be changed without creating a new language. Rust will always have ownership. Go will always have GC. Python will always be dynamically typed (with optional annotations).

The future: languages will differ less in features and more in defaults, runtime, and ecosystem.
