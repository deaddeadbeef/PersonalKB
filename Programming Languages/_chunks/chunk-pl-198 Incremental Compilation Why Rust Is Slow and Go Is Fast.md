---
tags: [pl, chunk, compilation, incremental]
up: "[[Compilation Pipeline Stages]]"
---

# Incremental Compilation Why Rust Is Slow and Go Is Fast

Compilation speed dramatically affects developer experience. The difference between Go's sub-second builds and Rust's multi-minute builds is a deliberate design trade-off.

## Compilation Speed Comparison

| Language | Hello World | Medium Project (100K LOC) | Why |
|----------|------------|--------------------------|-----|
| Go | ~100ms | ~2-5s | Minimal optimization, simple type system |
| Zig | ~200ms | ~3-8s | Simple language, LLVM for release only |
| C (gcc -O0) | ~100ms | ~5-15s | Simple parsing, no templates |
| Java (javac) | ~500ms | ~5-15s | No optimization (JIT does it) |
| Rust (debug) | ~2s | ~30-120s | Monomorphization, borrow checking, LLVM |
| Rust (release) | ~5s | ~60-300s | Aggressive LLVM optimization |
| C++ | ~500ms | ~60-600s | Templates, header inclusion, optimization |

## Why Go Is Fast

1. **No generics (historically):** No monomorphization overhead
2. **Simple type system:** No HM inference, no trait resolution
3. **Fast parser:** Go's grammar is designed for one-pass parsing
4. **Package-level compilation:** Each package compiled independently
5. **No LLVM:** Go has its own simpler compiler backend
6. **Minimal optimization:** Focus on compile speed over peak performance

## Why Rust Is Slow

1. **Monomorphization:** Each generic instantiation generates new code
2. **Borrow checking:** Lifetime analysis across the entire function
3. **Trait resolution:** Complex resolution with associated types, where clauses
4. **Macro expansion:** Procedural macros run at compile time
5. **LLVM backend:** Powerful but slow optimization passes
6. **Deep dependency trees:** Large crate graphs need full analysis

## Mitigation Strategies

### Incremental Compilation
- **Rust:** Caches intermediate results, only recompiles changed code
- **Go:** Always fast enough that incremental isn't critical
- **C++:** Precompiled headers, modules (C++20)
- **Java:** Incremental javac, Gradle daemon

### Parallel Compilation
- **Rust:** Parallelizes across codegen units (cargo build -j N)
- **Go:** Parallelizes across packages
- **C++:** Parallelizes across translation units

### Alternative Backends
- **Rust Cranelift:** Faster compile, less optimized output (debug mode)
- **Rust gcc-rs:** GCC backend as alternative to LLVM

## Key Insight
There's a fundamental trade-off: compile-time analysis (borrow checking, monomorphization, optimization) catches more bugs and produces faster code, but takes longer. Go chose fast compilation over maximum optimization. Rust chose maximum safety and performance over compilation speed. Both are valid — for different use cases.

## References
→ [[Sources Index]]
