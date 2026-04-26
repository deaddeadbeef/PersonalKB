---
tags: [raw, programming-languages, type-systems]
source: "Types and Programming Languages (Pierce, 2002), Programming Language Pragmatics (Scott, 2015)"
created: 2025-07-25
---

# raw-pl-001: Type System Foundations

## Static vs Dynamic Typing — Core Concepts

Static typing checks types at compile time. Dynamic typing checks at runtime. This is the most visible design axis in programming languages.

**Static typing advantages:** Catch errors early, enable IDE tooling (autocomplete, refactoring), allow compiler optimizations, serve as documentation. Languages: C, C++, Java, Rust, Go, Haskell, OCaml, Swift, Kotlin, TypeScript, Zig.

**Dynamic typing advantages:** Faster prototyping, no type annotation burden, simpler metaprogramming, duck typing enables flexible polymorphism. Languages: Python, Ruby, JavaScript, Erlang, Elixir, Lisp, Lua.

**The spectrum is not binary.** TypeScript adds gradual types to JavaScript. Python has type hints (PEP 484). Kotlin has smart casts. C# has dynamic. The trend is toward optional static typing layered on dynamic languages.

## Type Inference

Hindley-Milner type inference (1969/1978) allows the compiler to deduce types without annotations. OCaml and Haskell rarely need type annotations — the compiler infers them from usage. Rust uses local type inference (within function bodies). Go uses := for type-inferred declarations. C++ has uto. Java has ar (Java 10).

Full Hindley-Milner inference is decidable for rank-1 polymorphism. Higher-rank types (Haskell extensions) require annotations at polymorphism boundaries. Rust deliberately limits inference to function bodies — function signatures must be annotated for readability.

## Nominal vs Structural Typing

**Nominal:** Types are compatible based on declared names. Java, C#, Rust, Swift — class Dog and class Cat are different even with identical fields.
**Structural:** Types are compatible based on shape. TypeScript, Go interfaces, OCaml objects — if it has the right fields/methods, it's compatible.

Go's interfaces are structurally typed: any type with a Read([]byte) (int, error) method satisfies io.Reader, without declaring it. This enables retroactive interface satisfaction — existing types can satisfy interfaces defined later.

## Generics and Parametric Polymorphism

Generics allow writing code that works with any type satisfying certain constraints:
- **C++ templates:** Unconstrained, checked at instantiation, Turing-complete
- **Java generics:** Erased at runtime, bounded by interfaces
- **Rust generics:** Monomorphized, bounded by traits, zero-cost
- **Go generics (1.18):** Type parameters with interface constraints
- **Haskell parametric polymorphism:** Universal quantification, type classes for constraints
- **OCaml parametric polymorphism:** Implicit via Hindley-Milner, no explicit type parameters needed

The key distinction: **parametric polymorphism** (works for ANY type uniformly — Haskell, OCaml) vs **bounded polymorphism** (works for types satisfying constraints — Rust traits, Java bounds).

## Gradual Typing

Gradual typing allows mixing typed and untyped code. TypeScript is the most successful gradual type system: ny escapes the type checker, strict mode enforces types. Python's type hints (mypy) are another example. The challenge: gradual types must interact safely with untyped code, requiring runtime checks at boundaries.
