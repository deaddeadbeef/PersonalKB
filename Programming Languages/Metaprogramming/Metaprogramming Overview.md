---
tags: [programming-languages, metaprogramming]
up: "[[Programming Languages]]"
confidence: plausible
---
# Metaprogramming Overview

Metaprogramming is writing code that writes or manipulates other code. It is the most powerful and most dangerous tool in a language designer's toolkit — enabling elegant abstractions but also enabling incomprehensible complexity. How a language supports metaprogramming reveals its philosophy about abstraction, safety, and trust.

## The Spectrum of Metaprogramming

| Mechanism | When | Safety | Power | Languages |
|-----------|------|--------|-------|-----------|
| Macros (hygienic) | Compile time | High | High | Rust, Scheme, Elixir |
| Macros (unhygienic) | Compile time | Low | Highest | Common Lisp, C preprocessor |
| Templates | Compile time | Medium | High | C++, D |
| Comptime | Compile time | High | High | Zig |
| Reflection | Runtime | Medium | Medium | Java, C#, Python, Ruby |
| Decorators/Annotations | Compile or runtime | High | Medium | Python, Java, TypeScript |
| Code generation | Build time | Medium | High | Go generate, protobuf |

## The Design Tension

More metaprogramming power means more abstraction ability but also more potential for confusion. Languages navigate this by: limiting the mechanism (Go has no macros — `go generate` is the escape hatch), making it hygienic (Rust's proc macros can't accidentally capture variables), or embracing it fully (Lisp's macros can transform the entire language syntax).

## In This Hub

- [[Macro Systems Compared]]
- [[Reflection and Introspection]]
- [[Template Metaprogramming]]
- [[Compile-Time Computation]]
- [[Decorators Annotations and Attributes]]

## References

- [[Sources Index]]
