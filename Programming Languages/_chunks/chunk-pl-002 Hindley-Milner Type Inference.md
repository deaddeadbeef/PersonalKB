---
tags: [chunk, programming-languages, type-systems]
source: "[[raw-pl-001]]"
---

# chunk-pl-002 Hindley-Milner Type Inference

Hindley-Milner (HM) type inference allows compilers to deduce types without annotations. The algorithm uses **unification** — matching type variables with concrete types.

OCaml: let add x y = x + y inferred as int -> int -> int. Haskell: map :: (a -> b) -> [a] -> [b] — fully polymorphic, no annotations needed.

Languages with HM inference: OCaml, Haskell, F#, Standard ML, Elm. Languages with partial inference: Rust (local, within function bodies), Kotlin (local + some return types), Swift (local + closures), Go (:= shorthand), C++ (uto), Java (ar).

Full HM is decidable for rank-1 polymorphism. Higher-rank types (Haskell extensions) require explicit annotations. Rust deliberately limits inference to function bodies — function signatures must be explicit for readability and separate compilation.
