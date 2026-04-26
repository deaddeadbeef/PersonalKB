---
tags: [chunk, programming-languages, memory]
source: "[[raw-pl-002]]"
---

# chunk-pl-006 Garbage Collection Strategies Compared

**Mark-and-sweep:** Walk object graph from roots, mark reachable, sweep unmarked. Simple but stop-the-world pauses. Base for most GCs.

**Generational:** Most objects die young (generational hypothesis). Young generation collected frequently (fast), old generation rarely. Used by: JVM (G1, ZGC), .NET, OCaml, Python cycle detector.

**Concurrent/incremental:** Collect while program runs. Go achieves sub-millisecond pauses. Java ZGC and Shenandoah target under 10ms even with huge heaps. Trade-off: higher throughput overhead.

**Reference counting (Swift, Python, Objective-C):** Track reference count per object. Free when count hits zero. Deterministic destruction, no GC pauses. Can't handle cycles without separate cycle detection. Cache-unfriendly count updates.

OCaml's GC is tuned for functional programming: fast allocation of short-lived values, generational collection, and one of the lowest-latency GCs for allocation-heavy workloads.
