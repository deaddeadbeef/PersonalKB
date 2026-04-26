---
tags: [raw, programming-languages, paradigms]
source: "Concepts, Techniques, and Models of Computer Programming (Van Roy, 2004), SICP (Abelson & Sussman)"
created: 2025-07-25
---

# raw-pl-005: Programming Paradigm Deep Dive

## What Is a Paradigm?

A paradigm is a way of thinking about computation. It determines: what concepts are primitive (functions? objects? rules?), how you structure solutions (compose functions? inherit behavior? define constraints?), and what the language makes easy or hard.

## Imperative/Procedural

The oldest paradigm. Commands change state sequentially. Variables are mutable storage locations. Loops iterate. Conditionals branch. Maps directly to von Neumann hardware.

C is the purest procedural language. Go is modern procedural — functions and packages, no classes. Zig extends procedural with comptime. Even functional languages need imperative escape hatches: OCaml has mutable refs, Haskell has IO monad.

## Object-Oriented Programming

Two traditions:
1. **Smalltalk tradition (message passing):** Objects communicate via messages. Late binding. Everything is an object. Influenced Ruby, Objective-C.
2. **C++ tradition (class hierarchies):** Classes as blueprints, inheritance for code reuse, virtual dispatch for polymorphism. Influenced Java, C#, Kotlin.

Modern OOP critiques: "prefer composition over inheritance," "the banana-gorilla problem," "kingdom of nouns." Response: modern languages (Rust, Go, Kotlin, Swift) favor traits/interfaces/protocols over class hierarchies.

## Functional Programming

Core principles: pure functions (no side effects), immutable data, first-class functions, composition.

**Pure functional (Haskell):** Enforced purity via the type system. IO monad for effects. Lazy evaluation. Mathematically rigorous.

**Pragmatic functional (OCaml, Erlang):** Functional by default, imperative when needed. Eager evaluation. Practical for production use.

**Functional features in other languages:** Rust (iterators, closures, pattern matching), Kotlin (data classes, sealed classes, collections API), Swift (value types, map/filter/reduce), JavaScript (closures, array methods), Python (comprehensions, functools).

The FP advantage: immutable data is inherently thread-safe. This is why Erlang (concurrent systems) and Haskell (STM) are functional.

## Logic Programming

Prolog: facts, rules, queries. Unification and backtracking. The programmer describes what, not how. Excellent for: symbolic AI, natural language processing, constraint satisfaction. Limited for: numerical computation, systems programming.

SQL is essentially logic programming over tables. Type inference uses unification (same algorithm as Prolog). Pattern matching in ML/Rust is restricted unification.

## Multi-Paradigm Reality

No modern language is single-paradigm. Rust is imperative with functional features. Python is OOP with functional features. OCaml is functional with imperative escape hatches. Kotlin is OOP with functional features. The paradigm question isn't "which one?" but "which one is the default, and how easily can you reach the others?"
