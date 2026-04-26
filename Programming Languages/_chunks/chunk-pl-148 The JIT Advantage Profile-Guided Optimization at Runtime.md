---
tags: [pl, chunk, compilation, aot-jit]
up: "[[AOT vs JIT Compilation]]"
---

# The JIT Advantage Profile-Guided Optimization at Runtime

JIT compilers can optimize code based on actual runtime behavior — something AOT compilers can only approximate.

## What JIT Can Do That AOT Cannot

### 1. Speculative Optimization
`javascript
function add(a, b) { return a + b; }
// V8 observes: add is always called with integers
// JIT compiles an optimized integer-add path
// If a string is passed later, it "deoptimizes" and falls back
`

### 2. Inline Caching
`java
// JVM observes: this virtual method always dispatches to Dog.bark()
// JIT devirtualizes: replaces virtual call with direct call
// Enormous speedup for hot paths
`

### 3. Profile-Guided Inlining
The JIT inlines hot call sites based on actual call frequency:
- Cold code stays unoptimized (saves memory)
- Hot loops get maximum optimization
- This information is available at runtime, not compile time

## JIT Compilation Tiers

### Java HotSpot

| Tier | Compiler | When | Optimization |
|------|----------|------|-------------|
| 0 | Interpreter | Always first | None |
| 1-3 | C1 (client) | After ~100 invocations | Basic |
| 4 | C2 (server) | After ~10,000 invocations | Aggressive |

### V8 (JavaScript)

| Stage | Component | When |
|-------|-----------|------|
| 1 | Ignition (interpreter) | Immediate |
| 2 | Sparkplug (baseline) | After initial profiling |
| 3 | Maglev (mid-tier) | Hot functions |
| 4 | TurboFan (optimizing) | Hottest functions |

## The AOT Counterattack

### GraalVM Native Image
Java compiled AOT, avoiding JIT warmup:
- 10-100x faster startup
- Lower memory usage
- But: no speculative optimization, potentially slower peak throughput

### Rust/Go/Zig Position
"We don't need JIT because our AOT compilation is already optimal":
- Static dispatch, monomorphization = no devirtualization needed
- No boxing/unboxing = no speculative optimization needed
- Predictable performance from the first request

### PGO (Profile-Guided Optimization) for AOT
AOT compilers can use profiles from previous runs:
`ash
# Rust
cargo pgo instrument  # Build instrumented binary
./my-app              # Run with realistic workload
cargo pgo optimize    # Rebuild with profile data
`

## Key Insight
JIT excels for dynamic languages (JavaScript, Python) where types aren't known until runtime. For statically-typed languages (Rust, Go), AOT is usually sufficient because the compiler already knows the types. Java sits in between — its nominal type system plus virtual dispatch benefits from JIT, but GraalVM is proving AOT can work well too.

## References
→ [[Sources Index]]
