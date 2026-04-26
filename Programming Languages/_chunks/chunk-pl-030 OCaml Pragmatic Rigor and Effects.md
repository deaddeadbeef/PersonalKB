---
tags: [chunk, programming-languages, ocaml]
source: "[[raw-pl-015]]"
---

# chunk-pl-030 OCaml Pragmatic Rigor and Effects

OCaml's philosophy: **pragmatic rigor** — strongest practical type system with imperative escape hatches.

**Hindley-Milner inference:** Rarely write type annotations. let add x y = x + y inferred as int -> int -> int. Safety of static types with conciseness of dynamic.

**Eager evaluation:** Unlike Haskell's laziness. Performance is predictable. No space leaks from thunk accumulation.

**Imperative escape hatches:** ef for mutable variables, mutable record fields, for/while loops. Philosophy: functional 90% of the time, imperative when needed.

**Module system:** Structures, signatures (with abstract types), functors. Most powerful module system in any practical language.

**Algebraic effects (OCaml 5):** Effects are like resumable exceptions. Handler provides a value, execution continues. Subsumes: exceptions, async/await, generators, coroutines — all as library code.

**Fast compilation + excellent GC:** Native code compiler is fast. Generational GC optimized for allocation-heavy functional code. Used at Jane Street (trading), Facebook (Infer).
