---
tags: [chunk, programming-languages, java]
source: "[[raw-pl-011]]"
---

# chunk-pl-031 Java Platform and Modern Renaissance

Java's lasting impact: the **JVM as platform**. More important than the language itself — hosts Kotlin, Scala, Clojure, Groovy. Mature GC (G1, ZGC with sub-10ms pauses), tiered JIT compilation, monitoring tools, massive library ecosystem.

**Modern Java Renaissance (Java 8-21+):**
- Lambdas + Streams (8): Functional programming support
- var (10): Local type inference
- Records (16): Immutable data classes in one line
- Sealed classes (17): Algebraic data types
- Pattern matching switch (21): Exhaustive matching
- Virtual threads (21): Lightweight concurrency (millions of threads)

**Key trade-offs:** Checked exceptions (well-intentioned failure), null everywhere, type erasure (backward compat over correctness), verbose ceremony (improving with records/var).

Java's extreme backward compatibility built enterprise trust: 1996 code compiles on Java 21. This constrains evolution but makes Java the most trusted platform for large-scale systems.
