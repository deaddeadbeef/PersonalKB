---
tags: [chunk, programming-languages, haskell]
source: "[[raw-pl-012]]"
---

# chunk-pl-033 Haskell Purity Laziness and Monads

**Purity enforced:** Every function is pure — same inputs, same output, no side effects. Effects tracked via monads in the type system. IO String is a "recipe for producing a String with effects," not a String.

**Laziness:** Expressions evaluated only when needed. Enables infinite data structures, elegant generate-and-filter patterns. Cost: space leaks (unevaluated thunks accumulate), hard performance reasoning.

**Monads:** Sequence effects in a pure framework. IO, Maybe, Either, State, Reader, Writer, Parser — all monadic. Do-notation provides imperative-looking syntax. Monad transformers stack effects (ReaderT, StateT). Mathematically elegant, steep learning curve.

**Type classes:** Ad-hoc polymorphism more powerful than traits/interfaces. Multi-parameter type classes, associated types, type families. GHC extensions push toward dependent types.

**STM:** Software Transactional Memory — composable, deadlock-free concurrency. Transactions retry automatically on conflict. Type-safe: STM operations compose only with other STM operations.

**Haskell's ideas spread:** Rust traits (from type classes), Swift protocols, Kotlin sealed classes, Java records + pattern matching. Haskell is more influential than its market share suggests.
