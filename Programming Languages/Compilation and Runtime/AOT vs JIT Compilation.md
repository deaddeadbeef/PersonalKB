---
tags: [programming-languages, compilation, aot-jit]
up: "[[Compilation and Runtime Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# AOT vs JIT Compilation

> **One-line summary:** AOT compilation translates code to machine instructions before execution for predictable performance, while JIT compilation translates during execution to exploit runtime behavior — each trading startup speed, peak throughput, memory, and deployment complexity differently.

## 🎯 Intuition
**The Core Idea:** AOT compiles everything upfront before the program runs; JIT compiles incrementally during execution, guided by what the program actually does at runtime.
**Analogy:** JIT compilation is like translating a book paragraph-by-paragraph as someone reads it, while AOT is translating the whole book upfront before anyone reads it.
**Why It Matters:** The AOT-vs-JIT choice shapes startup latency, peak throughput, memory budget, deployment model, and which optimizations are even possible — every production system sits somewhere on this spectrum.

---

## ⚙️ Core Mechanics
### How It Works
**AOT compilation** — compilers like gcc, clang, rustc, and the Go compiler translate source code to native machine code before the program runs. The compiled binary contains all the machine instructions needed — no compiler or runtime is required at execution time.

**JIT compilation** — compilers compile code during program execution, typically starting with interpretation or bytecode execution and progressively optimizing hot code paths based on runtime profiling.

### Key Concepts

| Dimension | AOT | JIT |
|---|---|---|
| When compilation happens | Before execution (build time) | During execution (runtime) |
| Startup performance | Predictable from the first instruction; no warmup | Warmup period (seconds to minutes for peak performance) |
| Peak throughput | Full optimization at build time (LLVM, GCC backends) | Can optimize based on actual runtime behavior (profile-guided); speculative optimizations; can inline virtual calls based on observed receiver types; adapts to workload changes |
| Memory footprint | Smaller (no runtime compiler) | Higher (compiler lives in process) |
| Deployment | Simpler — single binary for Go and Rust | Platform-independent bytecode distribution |
| Performance predictability | High | Lower — GC pauses + JIT compilation pauses |
| Runtime adaptability | Can't optimize based on runtime behavior; must choose target architecture at build time | Speculative optimizations (assume a type, deoptimize if wrong) |
| Code size concerns | Generics require monomorphization (code size growth) | N/A — generics resolved at runtime |
| Build time | Long compile times for large projects (C++, Rust) | Compilation cost paid at runtime |
| Implementation complexity | Straightforward compiler pipeline | Complex (deoptimization, on-stack replacement) |

### Language Examples
**AOT languages:** C, C++, Rust, Go, Zig, OCaml, Haskell, Swift, Fortran

**JIT languages:** Java (HotSpot), C# (.NET), JavaScript (V8, SpiderMonkey), Julia, LuaJIT, PyPy

**The Java HotSpot Model** — the most sophisticated JIT implementation:
1. Bytecode starts in the interpreter
2. Methods called frequently are compiled by the C1 (client) compiler with basic optimizations
3. Very hot methods are recompiled by the C2 (server) compiler with aggressive optimizations
4. Speculative optimizations (type profiling, branch prediction) are deoptimized if assumptions break

This tiered approach gives reasonable startup (interpreter) with excellent peak performance (C2-compiled code rivaling C++ for many workloads).

**V8: JIT for a Dynamic Language** — JavaScript's V8 engine faces a harder problem than Java's JIT because JavaScript has no static types. V8 uses:
- **Hidden classes:** Infer object shapes from construction patterns
- **Inline caches:** Remember the types seen at each call site
- **TurboFan:** Optimizing compiler that speculates based on observed types and deoptimizes when wrong

V8 achieves remarkable performance for a dynamically typed language — 10-50x faster than CPython — by treating JavaScript as if it were statically typed at each call site.

**GraalVM** (Oracle) attempts to be a universal JIT: write a language interpreter in Java using the Truffle framework, and GraalVM automatically JIT-compiles it. This works for Python, Ruby, R, and LLVM bitcode. The result: near-JVM-level performance for interpreted languages with minimal implementation effort.

GraalVM also offers **Native Image** — AOT compilation of Java programs to native binaries. This trades JIT optimization for instant startup and lower memory, making Java competitive with Go for serverless/containers.

### Key Facts
- The AOT-vs-JIT choice is one of the most impactful decisions in language implementation
- Each approach offers fundamentally different trade-offs between startup performance, peak throughput, memory usage, and deployment complexity
- V8 achieves 10-50x faster performance than CPython for dynamically typed JavaScript
- HotSpot's C2-compiled code rivals C++ for many workloads
- GraalVM Native Image makes Java competitive with Go for serverless/containers

---

## 🔬 Deep Dive
### Formal Foundations
- **Partial evaluation:** JIT compilation can be viewed as partial evaluation of an interpreter with respect to a known program, specializing generic dispatch into direct calls
- **Futamura projections:** formalise the relationship between interpreters, compilers, and compiler-compilers — GraalVM's Truffle framework is a practical realisation of the first Futamura projection
- **Deoptimization:** JIT compilers speculatively compile under optimistic assumptions (e.g., a variable is always an integer); when an assumption breaks, the runtime must undo compiled code and fall back to a safe state — a process called deoptimization
- **On-stack replacement (OSR):** allows a running method to transition between interpreted and compiled versions mid-execution, critical for long-running loops that become hot after the method has already entered

### Trade-offs and Design Decisions
**AOT strengths and when to prefer AOT:**
- Predictable performance from the first instruction — no warmup
- Smaller memory footprint — no runtime compiler in the process
- Simpler deployment — single binary (Go, Rust)
- Full optimization at build time via LLVM or GCC backends
- Best for latency-sensitive cold starts: CLI tools, serverless functions, embedded systems

**AOT weaknesses:**
- Cannot optimize based on runtime behavior
- Must choose target architecture at build time (cross-compilation needed otherwise)
- Generics require monomorphization, causing code size growth
- Long compile times for large projects (C++, Rust)

**JIT strengths and when to prefer JIT:**
- Profile-guided optimization using actual runtime data
- Speculative optimizations that deoptimize when assumptions fail
- Platform-independent bytecode distribution
- Can inline virtual method calls based on observed receiver types
- Adapts to workload changes during execution
- Best for long-running servers and workloads whose hot paths emerge at runtime

**JIT weaknesses:**
- Warmup period (seconds to minutes before reaching peak performance)
- Higher memory usage — the compiler lives inside the process
- Unpredictable performance due to GC pauses and JIT compilation pauses
- Complex implementation: deoptimization, on-stack replacement, safe-points

### Historical Context
- **Emerging hybrid approaches** blur the AOT/JIT boundary:
  - **Rust's cranelift:** Fast AOT backend for debug builds; LLVM for release — optimizing developer iteration speed without sacrificing release performance
  - **Julia:** JIT-compiles functions on first call; feels like an interpreter but generates optimized native code
  - **Swift:** AOT with profile-guided optimization (PGO) — build, profile, rebuild with runtime data
  - **GraalVM Native Image:** AOT-compiles a traditionally JIT-based language (Java) to native binaries, trading runtime adaptability for instant startup
- The trend is toward **hybrid and adaptive strategies**: use fast compilation for development and cold paths, aggressive optimization for production hot paths

---

## 🏋️ Practice
### Warm-Up (5 min)
1. In HotSpot's tiered compilation, what are the four stages a method passes through from first invocation to peak-optimized execution?
2. Why does V8 need hidden classes and inline caches when Java's HotSpot does not?
3. Name three AOT-compiled languages and three JIT-compiled languages from memory.

### Core Problems
1. A Java microservice shows 4-second response times on its first few requests after deployment, then drops to 50 ms. Explain why this happens in terms of JIT warmup, and propose two distinct mitigation strategies.
2. You are choosing between Go (AOT) and C# (.NET JIT) for a latency-sensitive CLI tool that runs for under 500 ms per invocation. Argue which compilation strategy is more appropriate, referencing at least three trade-off dimensions from the comparison table.

### Challenge
1. Design a hybrid compilation pipeline for a new language targeting both serverless functions (cold-start sensitive) and long-running server workloads. Specify which compilation stages run at build time vs. runtime, how you handle speculative optimization and deoptimization, and how your design compares to GraalVM Native Image and HotSpot's tiered model.

---

*See also:* [[Compilation and Runtime Overview]], [[Virtual Machines and Bytecode]]

## Supporting Chunks / References
- [[Sources Index]]
