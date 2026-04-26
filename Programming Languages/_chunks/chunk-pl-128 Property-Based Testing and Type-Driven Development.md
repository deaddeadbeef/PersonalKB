---
tags: [pl, chunk, testing, property-based]
up: "[[Programming Paradigms Overview]]"
---

# Property-Based Testing and Type-Driven Development

Property-based testing (PBT) generates random inputs to test properties rather than specific examples. It originated in Haskell and has spread to most languages.

## QuickCheck and Its Legacy

Haskell's QuickCheck (2000) was the pioneer for property-based testing concepts.

### PBT Libraries by Language

| Language | Library | Notable Feature |
|----------|---------|----------------|
| Haskell | QuickCheck, Hedgehog | Type-class-based generators |
| Rust | proptest, quickcheck | Shrinking, strategy composition |
| Python | Hypothesis | Most feature-rich outside Haskell |
| Scala | ScalaCheck | Integration with ScalaTest |
| F# | FsCheck | .NET property testing |
| Erlang | PropEr, QuickCheck | State machine testing |
| Kotlin | Kotest property testing | Kotlin DSL for properties |
| Go | rapid, gopter | Stateless and stateful testing |
| JavaScript | fast-check | TypeScript support, shrinking |
| Java | jqwik | JUnit 5 integration |

## The Types + Tests Spectrum

No types, no tests (dangerous)
Dynamic types + tests (Python with pytest)
Static types + tests (Java with JUnit)
Rich types + PBT (Haskell, Rust) 
Dependent types + proofs (Idris, Lean)

Each level catches more bugs at compile time but requires more developer effort.

## State Machine Testing
PBT can test stateful systems by modeling them as state machines:
- **Erlang QuickCheck:** Pioneered this for testing concurrent systems
- **Hypothesis Stateful:** Python equivalent
- **proptest-state-machine:** Rust state machine testing

This is extraordinarily effective for finding concurrency bugs.

## Key Insight
PBT is most natural in languages with strong type systems because types guide generator creation. Haskell's type classes auto-derive generators; Rust's proptest uses strategy combinators. Dynamic languages can do PBT but require manual generator specification.

## References
-> [[Sources Index]]
