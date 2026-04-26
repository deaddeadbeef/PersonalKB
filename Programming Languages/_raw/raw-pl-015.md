---
tags: [raw, programming-languages, language-profiles]
source: "OCaml Manual, Haskell Wiki, Real World OCaml, Learn You a Haskell"
created: 2025-07-25
---

# raw-pl-015: ML Family Deep Dive — OCaml and Haskell

## The ML Heritage

ML (Meta Language, Robin Milner, 1973) was designed for theorem proving. Its innovations became standard: Hindley-Milner type inference, algebraic data types, pattern matching, parametric polymorphism, the module system. ML proved that strong static typing could be concise — you rarely need type annotations.

## OCaml's Pragmatic Approach

OCaml chooses pragmatism over purity at every decision point:

**Eager evaluation:** OCaml evaluates expressions immediately (like most languages). Haskell's lazy evaluation is elegant but causes space leaks and makes performance reasoning difficult. OCaml's eagerness makes performance predictable.

**Imperative escape hatches:** ef for mutable variables, mutable record fields, or/while loops, arrays with mutable elements. The philosophy: functional is the default, but when a hash table needs mutation for performance, you shouldn't fight the language.

**Module system over type classes:** OCaml uses modules/functors for abstraction where Haskell uses type classes. Modules are more powerful (abstract types, module-level functions) but less convenient (no automatic dispatch).

**No lazy evaluation:** OCaml has Lazy.t for explicit lazy values but isn't lazy by default. This makes reasoning about performance straightforward.

**Algebraic effects (OCaml 5):** The most exciting recent addition. Effects are like exceptions that can be resumed: a handler provides a value and execution continues. This subsumes async/await, generators, and exceptions into one mechanism.

## Haskell's Pure Approach

**Lazy by default:** Expressions are only evaluated when their values are needed. Enables infinite data structures and elegant generate-and-filter patterns. But: thunk accumulation causes space leaks, and reasoning about when evaluation happens is difficult.

**Monads everywhere:** IO, Maybe, Either, State, Reader, Writer, Parser, STM — all monadic. Do-notation provides imperative-looking syntax. Monad transformers stack effects (ReaderT, StateT, ExceptT). The power is real; the learning curve is steep.

**Type classes:** Ad-hoc polymorphism that's more powerful than traits or interfaces. Multi-parameter type classes, associated types, type families, and GHC extensions (TypeFamilies, GADTs, DataKinds) push the type system toward dependent types.

**GHC as research platform:** GHC implements Haskell plus dozens of extensions. It's a research testbed for type system innovations. Features like Linear Types, dependent types (via singletons), and effect systems are explored through GHC extensions before potentially becoming standard.

## The Comparison

OCaml is Haskell's pragmatic cousin: same ML heritage, different choices at every junction. OCaml: eager, impure, modules, fast compilation. Haskell: lazy, pure, type classes, sophisticated optimizations. Both have influenced Rust heavily — Rust's type inference from ML, traits from Haskell's type classes, pattern matching from both.
