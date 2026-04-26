---
tags: [chunk, programming-languages, gc-tuning]
source: "[[raw-pl-002]]"
---

# chunk-pl-095 GC Tuning and Latency Characteristics

**Java GC tuning:**
- G1: -XX:MaxGCPauseMillis=200 target. Balances throughput and latency.
- ZGC: Sub-millisecond pauses. -XX:+UseZGC. Best for latency-sensitive apps.
- Parallel: Maximum throughput. Longer pauses. -XX:+UseParallelGC.
- Choice depends on: heap size, allocation rate, latency requirements.

**Go GC:** Concurrent mark-sweep. Target: sub-millisecond pauses. GOGC environment variable controls GC frequency (default 100 = collect when heap doubles). Simple tuning model — intentionally few knobs. Go 1.19 added GOMEMLIMIT for memory-constrained environments.

**OCaml GC:** Generational. Minor heap (young generation) collected cheaply. Major heap collected incrementally. Fast for allocation-heavy functional code. Few tuning knobs needed — the defaults work well for most workloads.

**Python GC:** Reference counting (immediate) + cycle detector (periodic). Mostly invisible. gc.collect() for manual trigger. gc.disable() for performance-critical sections (if no cycles).

**The no-GC advantage (Rust, Zig, C):** No GC pauses, predictable latency, smaller memory footprint. Trade-off: programmer manages memory (Rust via ownership, Zig via allocators, C via malloc/free).

For latency-critical systems: Rust/Zig (no GC) > Go/Java ZGC (sub-ms pauses) > Java G1 (tunable) > Python (variable).
