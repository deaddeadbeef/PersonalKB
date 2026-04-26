---
tags: [chunk, programming-languages, type-systems]
source: "[[raw-pl-001]]"
---

# chunk-pl-001 Static vs Dynamic Typing Trade-offs

**Static typing** checks types at compile time. Errors caught before execution. Enables IDE autocomplete, refactoring tools, and compiler optimizations. Languages: C, C++, Java, Rust, Go, Haskell, OCaml, Swift, Kotlin, TypeScript, Zig.

**Dynamic typing** checks types at runtime. Faster prototyping, simpler code for small programs, natural metaprogramming. Languages: Python, Ruby, JavaScript, Erlang/Elixir, Lisp, Lua.

The trend is **gradual typing**: TypeScript adds static types to JavaScript. Python has type hints (mypy). Ruby has Sorbet. Start dynamic, add types where they matter. The static-vs-dynamic debate is dissolving into a spectrum.

Key insight: static types serve as **machine-checked documentation**. In large codebases, type annotations are often more reliable than comments.
