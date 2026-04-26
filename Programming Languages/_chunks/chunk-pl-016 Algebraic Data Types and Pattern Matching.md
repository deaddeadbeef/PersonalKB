---
tags: [chunk, programming-languages, pattern-matching]
source: "[[raw-pl-018]]"
---

# chunk-pl-016 Algebraic Data Types and Pattern Matching

**Sum types** (variants/enums): a value is ONE of several alternatives. **Product types** (records/tuples): a value has ALL fields. Together: model any data structure. "Algebraic" because sum = OR, product = AND.

**Pattern matching** destructures and branches:
`
match shape with Circle r -> pi*r*r | Rect(w,h) -> w*h
`

**Exhaustiveness checking** is the killer feature: forget a case, the compiler warns. Add a variant, every match site becomes a compile error. Safe large-scale refactoring.

Full ADT + pattern matching: OCaml, Haskell, Rust, F#, Scala, Elm, Erlang/Elixir.
Sealed classes + when/switch: Kotlin, Swift, Java 21+.
Limited: Python 3.10 (structural patterns). None: Go, C, JS (TypeScript discriminated unions approximate it).

The Visitor pattern (Java pre-17, C++) is OOP's workaround for lacking pattern matching — verbose but type-safe. Sealed classes + pattern matching eliminate the need for Visitors.
