---
tags: [chunk, programming-languages, paradigms]
source: "[[raw-pl-005]]"
---

# chunk-pl-014 Imperative vs Functional Default

Every modern language is multi-paradigm. The key question: which paradigm is the **default**?

**Imperative-first:** C, Go, Zig, Python, Ruby, Java. Mutable variables, loops, sequential statements. Functional features available but not primary.

**Functional-first:** Haskell, OCaml, Erlang/Elixir, Clojure, Elm. Immutable data, recursion/higher-order functions, composition. Imperative available as escape hatch.

**Balanced:** Rust, Kotlin, Swift, Scala. Strong support for both styles. Community norms determine which dominates.

The FP advantage for concurrency: immutable data is inherently thread-safe. This is why Erlang (concurrent telecom) and Haskell (STM) are functional.

The imperative advantage: maps directly to hardware, intuitive for sequential algorithms, easier debugging (step-through works naturally).

Modern convergence: every language is adopting FP features (map/filter/reduce, pattern matching, immutability options). The question shifts from "which paradigm?" to "which is the default?"
