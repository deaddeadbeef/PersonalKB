---
tags: [pl, chunk, pattern-matching, adt]
up: "[[Programming Paradigms Overview]]"
---

# Pattern Matching Adoption Across Language Families

Pattern matching, born in ML (1973), has become the most widely adopted feature from functional programming.

## Adoption Timeline
`
1973: ML (original)
1990: Haskell (guards, where clauses)
2004: Scala (case classes)
2010: Rust (exhaustive match with ownership)
2014: Swift (powerful switch)
2016: Kotlin (when expressions)
2017: C# 7 (type patterns)
2020: Python 3.10 (structural patterns)
2023: Java 21 (record patterns)
`

## Quality Spectrum

**Gold standard** (ML family):
- Exhaustiveness checking enforced
- Deeply integrated with algebraic data types
- Nested patterns, guards, bindings
- Languages: OCaml, Haskell, Rust, Scala

**Good adoption:**
- Exhaustiveness with sealed types
- Pattern matching on classes/records
- Languages: Swift, Kotlin, C# 11+, Java 21+

**Bolted-on:**
- No exhaustiveness guarantees
- Limited pattern depth
- Languages: Python (structural, no compile-time checks), JavaScript (TC39 proposal)

## The Sealed Type Connection
Exhaustive pattern matching requires the compiler to know all possible variants:
- **OCaml variants:** 	ype shape = Circle of float | Rect of float * float
- **Rust enums:** num Shape { Circle(f64), Rect(f64, f64) }
- **Kotlin sealed:** sealed class Shape + when exhaustive
- **Java sealed:** sealed interface Shape + switch exhaustive (Java 21)

## Key Insight
Pattern matching quality correlates directly with algebraic data type support. Languages that added ADTs alongside patterns (Rust, Scala) have better integration than those that bolted patterns onto class hierarchies (Java, C#).

## References
→ [[Sources Index]]
