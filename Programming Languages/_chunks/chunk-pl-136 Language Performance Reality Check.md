---
tags: [pl, chunk, performance, benchmarks]
up: "[[Compilation and Runtime Overview]]"
---

# Language Performance Reality Check

Raw benchmark performance matters less than you think. What matters is performance characteristics — startup, throughput, latency, memory.

## Performance Profiles

### Systems Languages (Predictable Performance)
**C, C++, Rust, Zig:** Direct hardware access, no GC pauses
- Best for: Latency-critical, embedded, real-time, game engines
- **Rust's advantage:** Same performance as C/C++ with safety guarantees
- **Zig's advantage:** Performance visible in the code — no hidden allocations

### GC Languages (Throughput-Optimized)
**Java, C#, Go:** GC enables fast allocation, but pauses exist
- **Java:** Excellent throughput after JIT warmup; multiple GC options for different profiles
- **Go:** Low-latency GC (sub-millisecond pauses) optimized for web services
- **C#:** Similar to Java; NativeAOT closes the startup gap

### Dynamic Languages (Developer-Optimized)
**Python, Ruby, JavaScript:** Optimized for developer speed, not execution speed
- **Python:** 50-100x slower for CPU work, but numpy/pytorch bypass the interpreter
- **JavaScript (V8):** JIT compilation makes it surprisingly fast (within 5x of C for some tasks)
- **Ruby (YJIT):** JIT compilation closing the gap significantly

## The Performance Doesn't Matter Argument

For most applications, language performance is not the bottleneck:

| Bottleneck | Reality |
|------------|---------|
| Database queries | 1-100ms per query dwarfs language overhead |
| Network I/O | 1-1000ms per request |
| Serialization | JSON parsing costs more than language overhead |
| Algorithm choice | O(n squared) in C is slower than O(n log n) in Python |
| Developer time | Shipping a week earlier often matters more than 2x speedup |

## When Performance Matters

| Domain | Required Language Tier | Why |
|--------|----------------------|-----|
| HFT (high-frequency trading) | C/C++/Rust | Microsecond latency |
| Game engines | C++/Rust | 16ms frame budget |
| Embedded systems | C/Rust/Zig | Memory constraints |
| ML training | Python + C/CUDA kernels | GPU utilization |
| Web API servers | Any (Go, Java, Python) | I/O bound, not CPU bound |
| CLI tools | Rust/Go | Startup time matters |

## Key Insight
The real performance question isn't "which language is fastest?" but "does this language's performance profile match my workload?" Go's low-latency GC is perfect for web services. Rust's predictable performance is perfect for real-time systems. Python's interpreted overhead is irrelevant when orchestrating CUDA kernels.

## References
→ [[Sources Index]]
