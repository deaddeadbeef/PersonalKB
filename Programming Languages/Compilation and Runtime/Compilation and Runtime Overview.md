---
tags: [programming-languages, compilation]
up: "[[Programming Languages]]"
---

# Compilation and Runtime Overview

How a language is compiled and executed determines its performance characteristics, deployment model, debugging experience, and developer workflow. The compilation strategy is one of the most consequential design decisions — it shapes what optimizations are possible, how fast programs start, and how code is distributed.

## The Execution Spectrum

| Strategy | Startup | Peak Performance | Distribution | Languages |
|----------|---------|-----------------|--------------|-----------|
| Ahead-of-time compiled (native) | Fast | Highest | Binary | C, C++, Rust, Go, Zig, OCaml |
| JIT compiled | Slow (warmup) | Very high | Bytecode + runtime | Java, C#, JavaScript (V8), Julia |
| Interpreted | Fast | Lowest | Source | Python (CPython), Ruby (MRI), Perl |
| Transpiled | Depends on target | Depends on target | Target source | TypeScript, CoffeeScript, Elm |
| Bytecode interpreted | Medium | Medium | Bytecode | Python, Erlang (BEAM), Lua |

Most modern language implementations blur these categories. Python has bytecode compilation. Java's JIT makes it competitive with C++ for long-running services. JavaScript's V8 uses both interpretation and JIT compilation.

## The Key Design Decisions

1. **Native vs managed runtime:** Does the compiled program run directly on hardware (C, Rust) or inside a virtual machine (Java, C#, Erlang)?
2. **Ahead-of-time vs just-in-time:** Is optimization done before deployment (Go, Rust) or during execution based on runtime profiles (Java HotSpot, V8)?
3. **Garbage collection vs manual memory:** Does the runtime manage memory (Java, Go, OCaml) or does the programmer (C, C++, Rust)?
4. **Monomorphization vs type erasure:** Are generics specialized at compile time (Rust, C++) or erased to a common representation (Java, Haskell)?

## In This Hub

- [[AOT vs JIT Compilation]]
- [[Virtual Machines and Bytecode]]
- [[Linking and Loading]]
- [[Runtime Systems Compared]]
- [[Compilation Pipeline Stages]]

## References

- [[Sources Index]]
