---
tags: [chunk, programming-languages, functional-migration]
source: "[[raw-pl-020]]"
---

# chunk-pl-039 FP Features Migrating to All Languages

Functional programming features spreading to every mainstream language:

**First-class functions:** JS (always), Python (lambda, closures), Java 8 (lambdas), C++11 (lambdas), Go (function values).

**Immutability options:** Rust (let default immutable), Kotlin (val vs var), Swift (let vs var), JS (const), Java 16 (records).

**Map/filter/reduce:** Java Streams, Python comprehensions, Kotlin stdlib, Rust iterators, JS array methods, Swift higher-order methods.

**Pattern matching adoption:** Rust (full ADTs), Swift (enum + switch), Kotlin (sealed + when), Java 21 (pattern switch), Python 3.10 (match/case).

**Pipe operator:** OCaml/Elixir/F# (|>). Rust uses method chaining (.). Kotlin uses extension functions. JS proposal pending.

**Why FP spreads:** (1) Immutable data is thread-safe. (2) Pure functions are easy to test. (3) Declarative operations (map, filter) often clearer than imperative loops. (4) Composition scales better than inheritance.
