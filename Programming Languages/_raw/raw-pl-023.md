---
tags: [raw, programming-languages, swift-kotlin]
source: "Swift Documentation, Kotlin Documentation, WWDC sessions"
created: 2025-07-25
---

# raw-pl-023: Swift and Kotlin — Modern Language Design

## The Successor Languages

Swift (2014) succeeded Objective-C for Apple platforms. Kotlin (2016) succeeded Java for Android and JVM. Both learned from decades of language design mistakes and share many design choices.

## Shared Design Principles

**Null safety:** Both distinguish nullable from non-nullable types at the type level. Swift: String? vs String. Kotlin: String? vs String. Both provide: safe call (?.), elvis/nil coalescing (?: / ??), forced unwrap (!).

**Type inference:** Both infer types aggressively. let x = 42 (Swift) and al x = 42 (Kotlin) — the compiler infers Int.

**Value semantics encouraged:** Swift: structs (value types) preferred over classes. Kotlin: data classes, immutable val. Both reduce aliasing bugs.

**Functional features:** Both support: first-class functions, closures, map/filter/reduce, pattern matching (switch/when), and extension functions.

## Swift-Specific Features

**Protocol-oriented programming:** Apple's recommended paradigm. Protocols with associated types + extensions provide polymorphism without inheritance hierarchies. Value types (structs) conform to protocols, avoiding reference counting overhead.

**ARC (Automatic Reference Counting):** Compile-time reference counting. No GC pauses. Deterministic destruction. Trade-off: reference cycles require weak/unowned references.

**Actors (Swift 5.5):** Language-level actor model for concurrency. Actor methods are async. The compiler prevents direct access to actor state from outside, ensuring isolation.

**Property wrappers:** @Published, @State, @Binding — custom types that intercept property access. Powers SwiftUI's reactive model.

## Kotlin-Specific Features

**Coroutines:** Structured concurrency — async code in sequential style. Scoped (coroutineScope), cancellable, structured (child cancellation propagates). More ergonomic than Java's CompletableFuture.

**Extension functions:** Add methods to existing types: un String.isPalindrome() = this == reversed(). Eliminates Java's StringUtils pattern.

**Multiplatform:** Kotlin Multiplatform shares code across JVM, JS, iOS (via Kotlin/Native), and desktop. expect/actual declarations for platform-specific implementations.

**Null safety operators:** Smart casts (if x != null, x is automatically non-null in the branch), safe call (?.), elvis (?:), not-null assertion (!!).

## Contrast: Memory Models

Swift uses ARC (compile-time, no GC pauses, deterministic, but cycle-prone). Kotlin/JVM uses GC (runtime, occasional pauses, but no cycle concerns). Kotlin/Native uses a custom memory manager with concurrent mark-and-sweep.
