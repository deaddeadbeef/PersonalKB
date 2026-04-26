---
tags: [chunk, programming-languages, swift-kotlin]
source: "[[raw-pl-023]]"
---

# chunk-pl-037 Swift and Kotlin Modern Language Design

**Shared principles:** Both succeed older languages (Swift -> Objective-C, Kotlin -> Java). Both feature: null safety (T vs T?), type inference, value semantics encouraged, functional features (map/filter/reduce, closures), and extension functions/methods.

**Swift-specific:**
- Protocol-oriented programming (Apple's paradigm recommendation)
- ARC (compile-time reference counting, deterministic destruction, cycle-prone)
- Actors (Swift 5.5, language-level concurrency isolation)
- Property wrappers (@Published, @State — powers SwiftUI)

**Kotlin-specific:**
- Coroutines (structured concurrency, scoped, cancellable)
- Extension functions (add methods to existing types)
- Multiplatform (share code across JVM, JS, iOS, desktop)
- Full Java interop from day one

**Memory model contrast:** Swift uses ARC (no GC pauses, deterministic, cycles need weak refs). Kotlin/JVM uses GC (no cycle concerns, occasional pauses). Both eliminate manual memory management.
