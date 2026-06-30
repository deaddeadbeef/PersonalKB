---
tags: [pl, study, type-systems]
up: "[[Programming Languages Study Index]]"
confidence: policy
---
# Review Drill — Type Systems and Inference

## Quick Recall

1. What is the fundamental trade-off between static and dynamic typing?
2. How does Hindley-Milner type inference work? Name 3 languages that use it.
3. Explain the difference between nominal and structural typing with examples.
4. What is gradual typing? How do TypeScript and Python implement it differently?
5. What are generics? Compare erasure (Java) vs monomorphization (Rust) vs reification (C#).

## Deep Dive Questions

### Static vs Dynamic Spectrum
- Why can Haskell infer nearly all types without annotations while Java requires explicit declarations?
- How does OCaml's type inference handle polymorphic variants?
- What makes TypeScript's type system Turing-complete, and why is that both powerful and dangerous?

### Nominal vs Structural
- Go uses structural typing for interfaces. What problems does this solve compared to Java's nominal approach?
- How does TypeScript's structural typing interact with its gradual type system?
- Why did Rust choose a nominal trait system with explicit impl blocks?

### Generics and Bounds
- Explain bounded polymorphism. How do Java's xtends, Rust's trait bounds, and Haskell's type classes compare?
- What is higher-kinded polymorphism? Why does Haskell support it but most languages don't?
- How do C++ concepts improve on unconstrained templates?

### Type Safety Innovations
- What is the "billion dollar mistake" and how do modern languages address it?
- Compare Option/Maybe types across Rust, Haskell, OCaml, Swift, and Kotlin.
- What are dependent types? Why are they mostly limited to proof assistants like Idris and Agda?

## Connections to Explore
- [[Type Systems Overview]] — hub page
- [[Static vs Dynamic Typing]] — core dimension
- [[Type Inference and Hindley-Milner]] — inference algorithms
- [[Generics and Parametric Polymorphism]] — generic systems
- [[Gradual and Optional Typing|Gradual Typing]] — hybrid approach

## References
→ [[Sources Index]]
