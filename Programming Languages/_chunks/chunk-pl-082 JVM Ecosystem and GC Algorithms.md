---
tags: [chunk, programming-languages, java-jvm]
source: "[[raw-pl-011]]"
---

# chunk-pl-082 JVM Ecosystem and GC Algorithms

The JVM is one of the most sophisticated runtime environments:

**GC Algorithms:**
- **G1 (Garbage First):** Default since Java 9. Divides heap into regions. Targets pause time goals. Good balance of throughput and latency.
- **ZGC:** Ultra-low latency. Sub-millisecond pauses regardless of heap size (up to 16TB). Concurrent everything.
- **Shenandoah:** Similar goals to ZGC. Concurrent compaction. Red Hat contribution.
- **Parallel GC:** Maximum throughput. Longer pauses acceptable. Good for batch processing.

**JVM Languages:** Java, Kotlin, Scala, Clojure, Groovy, JRuby, Jython. All benefit from: GC, JIT, monitoring, profiling, debugging tools.

**Virtual Threads (Java 21):** Lightweight threads (like goroutines). Millions per JVM. Structured concurrency. Eliminates the need for reactive programming (CompletableFuture, Reactor) for most I/O-bound workloads.

**GraalVM Native Image:** AOT-compile Java to native binary. Instant startup, lower memory. Trade-off: no JIT optimization, restricted reflection. Ideal for serverless/containers where startup time matters.
