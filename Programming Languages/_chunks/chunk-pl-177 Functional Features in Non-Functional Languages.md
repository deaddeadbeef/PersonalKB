---
tags: [pl, chunk, paradigms, fp-migration]
up: "[[Functional Programming Principles]]"
---

# Functional Features in Non-Functional Languages

The most impactful trend in language evolution is the migration of functional programming features into mainstream imperative/OOP languages.

## The Migration Map

| FP Feature | Origin | Now In |
|------------|--------|--------|
| First-class functions | Lisp (1958) | Every modern language |
| Closures/Lambdas | Scheme (1975) | Java 8, C++11, Go |
| Pattern matching | ML (1973) | Rust, Scala, Kotlin, Swift, Java 21 |
| Algebraic data types | ML (1973) | Rust, Scala, Kotlin, Java |
| Option/Maybe types | ML, Haskell | Rust, Swift, Kotlin, Java |
| Type inference | ML (1978) | Rust, Kotlin, Swift, Go |

## Case Study: Java's Functional Journey

Java went from zero FP features to pattern matching + records + sealed classes + streams in 9 years (1996-2023).

## The Convergence

Modern multi-paradigm languages share a common feature set:
- Lambdas/closures
- Collection pipelines (map/filter/reduce)
- Pattern matching
- Algebraic data types
- Option/Result types
- Immutability support

## Key Insight
Functional programming won the ideas war. Haskell's greatest contribution isn't Haskell itself — it's that every mainstream language now includes FP features pioneered in Haskell and ML.

## References
→ [[Sources Index]]
