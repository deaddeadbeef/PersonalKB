---
tags: [chunk, programming-languages, evaluation-strategy]
source: "[[raw-pl-015]]"
---

# chunk-pl-113 Eager vs Lazy Evaluation

**Eager (strict) evaluation:** Expressions evaluated immediately when bound. All languages except Haskell: OCaml, Rust, Python, Java, Go, C, etc.

Benefits: predictable performance, straightforward debugging (step-through works), no space leaks from unevaluated expressions, easy to reason about memory usage.

**Lazy evaluation:** Expressions evaluated only when their value is needed. Haskell by default.

Benefits: avoids unnecessary computation, enables infinite data structures ([1..]), elegant generate-and-filter patterns, can improve asymptotic complexity in some cases.

Costs: space leaks (unevaluated thunks accumulate), hard to predict when evaluation happens, debugging is difficult (which thunk is being forced?), performance reasoning is non-intuitive.

**Lazy in eager languages:**
- Python generators: (x for x in range(1000000)) — lazy sequence
- Rust iterators: lazy by default, .collect() materializes
- Kotlin sequences: .asSequence() for lazy evaluation
- Java streams: lazy until terminal operation
- Haskell: explicit strictness with seq, BangPatterns, NFData

The consensus: eager evaluation as default, lazy evaluation as opt-in tool. Haskell's lazy-by-default is beautiful for research but challenging for production performance.
