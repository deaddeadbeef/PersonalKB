---
tags: [chunk, programming-languages, haskell-influence]
source: "[[raw-pl-012]]"
---

# chunk-pl-089 Haskell Influence on Modern Languages

Haskell's ideas have spread far beyond Haskell itself:

**Type classes -> Traits/Protocols:**
- Rust traits directly inspired by Haskell type classes
- Swift protocols similar to type classes with associated types
- Kotlin interfaces with default methods echo type class defaults

**Maybe/Either -> Option/Result:**
- Rust Option<T> and Result<T,E> from Haskell Maybe and Either
- Swift Optional from Maybe
- Kotlin nullable types (T?) inspired by Maybe's compile-time null tracking

**Pattern matching:**
- Rust match from Haskell case
- Kotlin when from Haskell case
- Java 21 pattern matching from ML/Haskell tradition
- Swift switch with associated values

**Immutability as default:**
- Rust let (immutable by default) from Haskell's pervasive immutability
- Kotlin val from Haskell's default immutability philosophy

**STM:** Haskell's Software Transactional Memory influenced Clojure's ref system and academic research in concurrent programming.

**Monadic error handling:** Rust's ? operator is monadic bind (>>=) specialized for Result. The concept of chaining fallible operations comes from Haskell's monadic programming.

Haskell is the most influential language relative to its market share.
