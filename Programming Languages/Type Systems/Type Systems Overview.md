---
tags: [programming-languages, type-systems]
up: "[[Programming Languages]]"
confidence: plausible
---
# Type Systems Overview

A type system is a set of rules that assigns a type to every expression in a program. It is the single most impactful design decision in a programming language — it shapes how programmers think, what errors are caught when, and how code composes. Every language designer must answer: How much should the compiler know about your data?

## The Fundamental Spectrum

At one extreme, **dynamically typed** languages (Python, Ruby, JavaScript, Lisp) check types at runtime. Variables can hold any value, and type errors surface during execution. At the other extreme, **statically typed** languages (Haskell, OCaml, Rust, Java) check types at compile time. The compiler rejects programs that violate type rules before they run.

Neither extreme is objectively better — they represent different trade-offs between flexibility, safety, and development speed. The most interesting design space lies in the middle ground: gradual typing, type inference, and optional typing.

## Key Design Dimensions

| Dimension | Question | Examples |
|-----------|----------|----------|
| Static vs Dynamic | When are types checked? | Rust (static) vs Python (dynamic) |
| Nominal vs Structural | How is type compatibility determined? | Java (nominal) vs TypeScript (structural) |
| Inferred vs Explicit | Must types be written? | OCaml (inferred) vs Java (explicit) |
| Strong vs Weak | Are implicit conversions allowed? | Python (strong) vs C (weak) |
| Gradual | Can typed and untyped code coexist? | TypeScript, Python (mypy) |
| Dependent | Can types depend on values? | Idris, Agda (full), Rust (limited via const generics) |

## In This Hub

- [[Static vs Dynamic Typing]]
- [[Type Inference and Hindley-Milner]]
- [[Nominal vs Structural Typing]]
- [[Generics and Parametric Polymorphism]]
- [[Gradual and Optional Typing]]

## References

- [[Sources Index]]
