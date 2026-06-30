---
tags: [pl, study, compilation, metaprogramming]
up: "[[Programming Languages Study Index]]"
confidence: policy
---
# Review Drill — Compilation and Metaprogramming

## Quick Recall — Compilation

1. What are the 6 universal stages of a compilation pipeline?
2. Explain AOT vs JIT compilation. Name 2 languages that use each.
3. What is LLVM? Which languages use it as their backend?
4. How do virtual machines work? Compare JVM, CLR, BEAM, and WASM.
5. What is the difference between static and dynamic linking?

## Deep Dive — Compilation

### Pipeline Stages
- How does parsing differ for C (context-sensitive) vs Lisp (homoiconic)?
- What optimizations happen at each pipeline stage?
- Why do some languages (Go) optimize for compile speed while others (Rust, C++) accept slow compiles?

### Runtime Models
- Compare zero-runtime (C, Zig) vs minimal runtime (Go, Rust) vs heavy runtime (Java, Python, Erlang).
- How does Go include a goroutine scheduler in its runtime while claiming to be a "compiled" language?
- What makes WASM a universal compilation target? What are its current limitations?

### JIT vs AOT
- Why can JIT-compiled code sometimes be faster than AOT? (profile-guided optimization, deoptimization)
- How does Java's tiered compilation (C1 + C2) work?
- Why did JavaScript engines (V8, SpiderMonkey) invest so heavily in JIT technology?
- How does GraalVM enable AOT compilation for JVM languages?

## Quick Recall — Metaprogramming

1. What is homoiconicity? Why does it make Lisp macros uniquely powerful?
2. Compare C preprocessor macros, Rust procedural macros, and Lisp macros.
3. What is reflection? How do Java and Go implement it differently?
4. What is compile-time computation? Compare C++ constexpr, Zig comptime, and Rust const fn.
5. How do decorators (Python), annotations (Java), and attributes (C#, Rust) differ?

## Deep Dive — Metaprogramming

### Macro Systems
- Why are Rust's hygenic macros safer than C's text-substitution macros?
- How does Lisp's quote/unquote mechanism enable code as data manipulation?
- What is Template Haskell? How does it compare to Lisp macros?
- Why did Go originally reject generics — and how is that related to metaprogramming?

### Compile-Time Power
- How does Zig's comptime blur the line between compile time and runtime?
- What can C++ constexpr compute at compile time in C++20?
- How do Rust's procedural macros enable derive, attribute, and function-like macros?

### Reflection vs Macros
- When should you use reflection vs macros vs code generation?
- Why does Rust prefer macros (compile-time) while Java prefers reflection (runtime)?
- How does Go's reflect package interact with its structural typing?

## Connections to Explore
- [[Compilation and Runtime Overview]] — hub page
- [[Metaprogramming Overview]] — hub page
- [[AOT vs JIT Compilation]] — compilation strategies
- [[Macro Systems Compared|Macro Systems]] — macro deep dive

## References
→ [[Sources Index]]
