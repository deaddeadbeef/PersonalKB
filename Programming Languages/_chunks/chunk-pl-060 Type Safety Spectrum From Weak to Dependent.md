---
tags: [chunk, programming-languages, type-safety]
source: "[[raw-pl-029]]"
---

# chunk-pl-060 Type Safety Spectrum From Weak to Dependent

**Weakly typed (C):** Types barely enforced. Implicit conversions, void pointers, unchecked casts.

**Strongly dynamic (Python, Ruby):** Types enforced at runtime. No implicit coercion. Errors at runtime.

**Strongly static (Java, Go):** Compile-time checking. Null is an escape hatch (Java). interface{}/any bypasses typing (Go).

**Null-safe static (Kotlin, Swift, Rust):** Optional types force explicit null handling. Eliminates null pointer errors.

**ADT + exhaustive matching (Rust, Haskell, OCaml):** Compiler ensures every case handled. Adding a variant forces updating all match sites.

**Dependently typed (Idris, Agda, Lean):** Types depend on values. Vector type includes length. Matrix multiplication dimension-checked at compile time. Array bounds proved at compile time.

Trend: languages move up the spectrum. Each level catches more errors at compile time, at cost of more upfront effort. Type inference reduces annotation burden, making stronger type systems more ergonomic.
