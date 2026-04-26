---
tags: [chunk, programming-languages, type-systems]
source: "[[raw-pl-001]]"
---

# chunk-pl-003 Nominal vs Structural Typing

**Nominal typing:** Types match by declared name. class Dog and class Cat are different even with identical fields. Languages: Java, C#, Rust, Swift, Kotlin, C++.

**Structural typing:** Types match by shape — if it has the right fields/methods, it's compatible. Languages: TypeScript, Go interfaces, OCaml objects.

Go's interfaces are the purest structural typing: any type with a Read([]byte) (int, error) method satisfies io.Reader without declaring it. This enables **retroactive interface satisfaction** — existing types can satisfy interfaces defined later.

TypeScript is structurally typed: {name: string, age: number} satisfies any interface requiring those fields. This fits JavaScript's duck-typing heritage.

Rust is mostly nominal (concrete types) but traits have structural elements (any type implementing the right methods satisfies a trait bound).
