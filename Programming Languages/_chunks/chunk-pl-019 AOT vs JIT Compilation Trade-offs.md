---
tags: [chunk, programming-languages, compilation]
source: "[[raw-pl-007]]"
---

# chunk-pl-019 AOT vs JIT Compilation Trade-offs

**AOT (Ahead-of-Time):** Compile before execution. Predictable performance, fast startup, no runtime compiler overhead. Languages: C, C++, Rust, Go, Zig, OCaml, Haskell, Swift.

**JIT (Just-in-Time):** Compile during execution using runtime profiles. Can optimize based on actual behavior (speculative inlining, branch prediction). Slow warmup. Languages: Java HotSpot, V8 (JavaScript), .NET, Julia, LuaJIT.

**Java HotSpot:** Tiered compilation — interpreter to C1 (basic) to C2 (aggressive). Profile-guided optimization makes Java competitive with C++ for long-running services.

**V8 (JavaScript):** Speculates on types at each call site. Hidden classes + inline caches + TurboFan optimizer achieve 10-50x faster than CPython despite being dynamically typed.

**GraalVM:** Universal JIT — write interpreter in Java/Truffle, get JIT for free. Also offers Native Image (AOT for Java — instant startup).

Trade-off: AOT gives predictable performance; JIT gives adaptive optimization. For long-running servers, JIT wins. For CLIs and serverless, AOT wins.
