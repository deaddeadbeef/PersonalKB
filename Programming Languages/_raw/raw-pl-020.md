---
tags: [raw, programming-languages, functional-features]
source: "Functional Programming in Scala, Real World Haskell, OCaml Manual"
created: 2025-07-25
---

# raw-pl-020: Functional Features in Non-Functional Languages

## The FP Migration

Functional programming features are migrating into every mainstream language. The core features spreading:

## First-Class Functions

Functions as values that can be passed as arguments, returned, and stored in variables.
- **JavaScript (1995):** Functions have always been first-class. Closures over lexical scope.
- **Python:** lambda (limited to single expression), nested functions, closures.
- **Java 8 (2014):** Lambda expressions, method references. Enabled the Streams API.
- **C++11 (2011):** Lambda expressions with capture. [&] captures by reference, [=] by value.
- **Go:** First-class functions. Closures over surrounding scope.

## Immutability

Making data immutable by default or by convention:
- **Rust:** Variables immutable by default (let). let mut for mutability.
- **Kotlin:** al (immutable) vs ar (mutable). Data classes are effectively immutable.
- **Swift:** let (immutable) vs ar (mutable). Structs are value types (copied).
- **JavaScript:** const (immutable binding, not deep immutability). Object.freeze() for shallow immutability.
- **Java 16:** Records (immutable data classes).

## Map/Filter/Reduce

Functional collection operations:
- **Java 8 Streams:** list.stream().filter(x -> x > 0).map(x -> x * 2).collect(toList())
- **Python:** List comprehensions [x*2 for x in lst if x > 0], functools.reduce
- **Kotlin:** list.filter { it > 0 }.map { it * 2 } (built into stdlib)
- **Rust:** iter.filter(|x| *x > 0).map(|x| x * 2).collect::<Vec<_>>()
- **JavaScript:** rr.filter(x => x > 0).map(x => x * 2)
- **Swift:** rr.filter {  > 0 }.map {  * 2 }

## Pattern Matching Adoption

ML-style pattern matching spreading:
- **Rust (2015):** Full ADT + match from day one
- **Swift (2014):** Enum + switch with associated values
- **Kotlin (2016):** Sealed classes + when
- **Java 21 (2023):** Sealed classes + pattern matching
- **Python 3.10 (2021):** Structural pattern matching
- **C# 7-12:** Progressive pattern matching additions

## The Pipe Operator

Left-to-right data transformation:
- **OCaml:** x |> f |> g |> h
- **Elixir:** x |> f() |> g() |> h()
- **F#:** x |> f |> g |> h
- **JavaScript (TC39 proposal):** x |> f(%) |> g(%) (not yet standardized)
- **Rust:** Method chaining via . serves similar purpose
- **Kotlin:** Extension functions + stdlib enable fluent chains

## Why FP Features Spread

1. **Concurrency:** Immutable data is thread-safe
2. **Testability:** Pure functions are easy to test (no mocking needed)
3. **Composability:** Small functions compose into complex pipelines
4. **Readability:** Declarative operations (map, filter) are often clearer than imperative loops
