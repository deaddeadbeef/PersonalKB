---
tags: [chunk, programming-languages, compilation]
source: "[[raw-pl-007]]"
---

# chunk-pl-020 Virtual Machines and Bytecode Formats

**JVM:** Stack-based bytecode. Most mature VM: sophisticated GC (G1, ZGC), tiered JIT (HotSpot), excellent tooling. Hosts Java, Kotlin, Scala, Clojure. The JVM ecosystem is its greatest asset.

**CLR (.NET):** Register-based CIL. Reified generics (unlike JVM erasure). Value types on stack. Hosts C#, F#. RyuJIT for consistent compilation.

**BEAM (Erlang):** Designed for concurrency. Lightweight processes (millions per node), per-process GC (no global pauses), hot code swapping, distribution built in. Hosts Erlang, Elixir.

**CPython:** Simple bytecode interpreter. No JIT in standard CPython. GIL limits parallelism. PyPy adds tracing JIT for 5-20x speedup.

**WebAssembly (Wasm):** Newest major bytecode. Portable, sandboxed, near-native performance. Compilation target for C, C++, Rust, Go. Runs in browsers and standalone (WASI). May become the universal runtime.

**LLVM IR:** Not a VM but a shared compiler backend. Optimization passes + code generation. Used by Rust, Swift, Clang, Julia. Write a frontend, get world-class optimization free.
