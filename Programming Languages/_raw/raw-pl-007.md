---
tags: [raw, programming-languages, compilation]
source: "Engineering a Compiler (Cooper & Torczon, 2012), Crafting Interpreters (Nystrom, 2021)"
created: 2025-07-25
---

# raw-pl-007: Compilation and Execution Models

## The Compilation Pipeline

Source code goes through: lexing (characters to tokens), parsing (tokens to AST), semantic analysis (type checking, name resolution), IR generation, optimization, code generation (machine code or bytecode), and linking.

Modern compilers use multiple intermediate representations. Rust: Rust source to HIR (desugared) to MIR (control-flow graph) to LLVM IR to machine code. Each IR makes different analyses and optimizations natural.

## AOT Compilation

Ahead-of-time compilation translates everything before execution. Benefits: predictable performance, fast startup, no runtime compiler overhead. Languages: C, C++, Rust, Go, Zig, OCaml, Haskell, Swift.

Go compiles extremely fast (seconds for large projects) using its own compiler (not LLVM). The trade-off: slightly less optimized output than LLVM-based compilers. Rust uses LLVM for maximum optimization but suffers long compile times.

## JIT Compilation

Just-in-time compilation translates during execution, using runtime profiling to guide optimization.

Java HotSpot: Tiered compilation (interpreter to C1 to C2). Profile-guided optimization: inline virtual calls based on observed types, optimize hot loops, deoptimize if assumptions break. Result: Java performance competitive with C++ for long-running services.

V8 (JavaScript): Ignition interpreter + TurboFan optimizing compiler. Speculates on types observed at each call site. Achieves remarkable performance for a dynamically typed language (10-50x faster than CPython).

LuaJIT: Trace-based JIT. Records execution traces of hot loops and compiles them. Produces code competitive with C for numerical workloads. One of the fastest dynamic language implementations ever.

## Bytecode VMs

JVM: Stack-based bytecode. The most mature VM: sophisticated GC, tiered JIT, excellent tooling. Hosts Java, Kotlin, Scala, Clojure.

CLR (.NET): Register-based CIL. Reified generics (unlike JVM's erased generics). Hosts C#, F#.

BEAM (Erlang): Designed for concurrency. Lightweight processes, per-process GC, hot code swapping. Hosts Erlang, Elixir.

CPython: Simple bytecode interpreter. No JIT (in standard CPython). The GIL limits parallelism. PyPy adds a tracing JIT for 5-20x speedup.

## WebAssembly

Wasm is the newest major bytecode format: portable, sandboxed, near-native performance. Compilation target for C, C++, Rust, Go, and others. Runs in browsers and standalone (WASI). May become the universal runtime for the next generation of applications, fulfilling Java's "write once, run anywhere" promise more broadly.

## LLVM: The Shared Backend

LLVM provides a shared compiler infrastructure: optimization passes and code generation for multiple targets. Used by: Rust, Swift, Julia, Clang (C/C++), and many others. Writing an LLVM frontend gives your language world-class optimization for free. The trade-off: LLVM compilation is slow.
