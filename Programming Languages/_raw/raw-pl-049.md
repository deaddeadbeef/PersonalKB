---
tags: [pl, raw, performance, benchmarks]
up: "[[Sources Index]]"
---

# Raw Note 049 – Language Performance Benchmarks

## Performance Tiers (General CPU-Bound Tasks)

### Tier 1: Near-Bare-Metal (1x)
- **C** – baseline, manual optimization
- **C++** – zero-cost abstractions, RAII
- **Rust** – matches C/C++ with safety guarantees
- **Zig** – matches C, explicit control over optimization

### Tier 2: Compiled with Runtime (1.5-3x)
- **Go** – GC pauses, but excellent concurrent throughput
- **Java** – JIT compilation approaches native speed for long-running processes
- **C#** – similar to Java with .NET JIT
- **Swift** – ARC overhead, but good optimization
- **Kotlin/JVM** – same as Java (JVM-based)
- **OCaml** – good native compilation, GC overhead

### Tier 3: Optimized Interpreters/VMs (5-20x)
- **JavaScript (V8)** – highly optimized JIT, but dynamic overhead
- **Haskell** – lazy evaluation overhead, but GHC optimizes well
- **Erlang/Elixir** – BEAM optimizes for latency, not throughput

### Tier 4: Interpreted (20-100x)
- **Python (CPython)** – interpreted, GIL limits parallelism
- **Ruby (CRuby)** – interpreted, improving with YJIT
- **Perl** – interpreted

## Benchmark Caveats

### Why Benchmarks Lie
1. **Microbenchmarks** don't represent real workloads
2. **Startup time** vs **throughput** vs **latency** are different metrics
3. **Memory usage** is often ignored but critical
4. **Developer time** is often more expensive than compute time
5. **Ecosystem libraries** (e.g., Python NumPy) can bypass language slowness

### Benchmark Game Results (approximate, CPU-bound)

| Benchmark | C | Rust | Go | Java | Python |
|-----------|---|------|----|------|--------|
| n-body | 1.0x | 1.0x | 1.5x | 1.8x | 65x |
| binary-trees | 1.0x | 1.1x | 2.1x | 1.3x | 48x |
| mandelbrot | 1.0x | 1.0x | 1.3x | 1.1x | 180x |
| regex-redux | 1.0x | 1.2x | 5.5x | 2.4x | 3.2x |

### Real-World Performance Characteristics

| Language | Startup | Throughput | Latency (p99) | Memory |
|----------|---------|------------|----------------|--------|
| C/Rust | Instant | Excellent | Predictable | Minimal |
| Go | Fast | Very good | Good (GC pauses) | Low |
| Java | Slow (JVM) | Excellent (warmed up) | Variable (GC) | High |
| Python | Moderate | Poor (CPU) | Variable | Moderate |
| Node.js | Fast | Good (I/O) | Variable (GC) | Moderate |
| Erlang | Fast | Moderate | Excellent (per-process GC) | Moderate |

## When Performance Doesn't Matter

For many applications, raw performance is not the bottleneck:
- **I/O bound:** Web servers, database queries – language speed barely matters
- **ML/Data Science:** Python orchestrates C/CUDA kernels (NumPy, PyTorch)
- **Prototyping:** Ship fast, optimize later
- **Scripting:** Automation tasks complete in seconds regardless

## Key Insight
The performance gap between languages has narrowed dramatically. Modern GC languages (Go, Java, C#) are often within 2x of C for real workloads. The real question is: what kind of performance matters? Throughput? Latency? Startup? Memory? Each language optimizes for different metrics.

## References
→ [[Sources Index]]
