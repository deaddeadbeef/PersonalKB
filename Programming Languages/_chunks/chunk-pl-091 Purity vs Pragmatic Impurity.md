---
tags: [chunk, programming-languages, functional-purity]
source: "[[raw-pl-012]]"
---

# chunk-pl-091 Purity vs Pragmatic Impurity

**Pure functional (Haskell, Elm):** All functions pure. Side effects tracked in the type system (IO monad). Compiler guarantees: same inputs = same output. Benefits: easy testing, fearless refactoring, automatic parallelization. Cost: monads required for I/O, steep learning curve.

**Pragmatic impurity (OCaml, Erlang, F#):** Functional by default, imperative when needed. OCaml: mutable refs, mutable record fields, imperative loops available. Erlang: all data immutable but processes maintain state via message passing. Philosophy: functional is the right default 90% of the time.

**Functional features in imperative languages (Rust, Kotlin, Swift):** Immutability preferred (let/val), closures and higher-order functions, pattern matching. But mutation readily available. The functional features serve safety and expressiveness, not purity.

**The practical question:** Is purity worth the cost? Haskell says yes: purity enables powerful reasoning and optimization. OCaml says: mostly yes, but imperative escape hatches are important. Rust says: immutability-by-default gives most of purity's benefits without monadic overhead.

**The consensus emerging:** Immutability as default (not enforced purity) plus explicit mutation when needed. This is where Rust, Kotlin, Swift, and modern Java (records) are converging.
