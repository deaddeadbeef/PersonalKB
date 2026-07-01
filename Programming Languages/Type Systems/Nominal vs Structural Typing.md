---
tags: [programming-languages, type-systems, nominal-structural]
up: "[[Type Systems Overview]]"
confidence: established
freshness: stable
tier-coverage: full
confidence: plausible
---
# Nominal vs Structural Typing

## 🎯 Intuition

**The Core Idea:** Languages decide type compatibility in two main ways: nominal typing says compatibility comes from the same declared identity, while structural typing says compatibility comes from the same shape.

**Analogy:** Nominal typing is like checking passports and official membership lists; structural typing is like letting anyone in who has the right tools and knows the right handshake.

**Why It Matters:** This choice affects whether two types with identical fields are interchangeable, whether interfaces must be planned up front, how APIs compose across libraries, and whether a language treats structure alone as enough to capture meaning.

## ⚙️ Core Mechanics

### Nominal Typing

**Philosophy:** A type is defined by its declaration. Two types with identical fields are different types if declared separately. Identity comes from the name, not the structure.

**Java** is the canonical nominal language. A `Dog` class and a `Cat` class with identical fields (`name: String`, `age: int`) are completely incompatible types. To share behavior, they must explicitly implement a common interface or extend a common class. This is deliberate — a `Velocity` and a `Temperature` might both wrap a `double`, but they represent fundamentally different concepts and should never be interchangeable.

**Rust** uses nominal typing for structs and enums but structural compatibility for traits. A type implements a trait if it has the right methods (though the implementation must be explicitly declared with `impl Trait for Type`).

**OCaml** is interestingly split: its core type system (variants, records) is nominal, but its object system uses structural typing (row polymorphism). This means two OCaml objects with the same methods are type-compatible regardless of class hierarchy — a unique combination.

**Swift, Kotlin, C#** are all nominally typed, requiring explicit protocol/interface implementation.

### Structural Typing

**Philosophy:** A type is defined by its shape. If two types have the same fields and methods, they are compatible — regardless of what they're called. Structure is meaning.

**TypeScript** is the most prominent structurally typed language. If an object has a `name: string` and `greet(): void`, it satisfies any interface requiring those members — no explicit `implements` needed. This aligns with JavaScript's duck typing while adding compile-time checking.

**OCaml objects** use structural typing: `method greet : string` matches any object type requiring that method signature. This is unusual for an ML-family language and reflects OCaml's pragmatic multi-paradigm philosophy.

**Go** uses structural interface satisfaction: any type that has the methods of an interface automatically implements it. There's no `implements` keyword. This was a deliberate design choice — it allows interfaces to be defined after types, enabling retroactive abstraction. The `io.Reader`/`io.Writer` interfaces work because any type with `Read([]byte) (int, error)` is automatically a `Reader`.

**Haskell type classes** are somewhat structural in spirit — any type with the right operations can be an instance — but instance declarations are explicit (nominal).

### The Trade-offs

| Aspect | Nominal | Structural |
|--------|---------|------------|
| Safety | Prevents accidental compatibility | Allows unintended matches |
| Flexibility | Requires upfront interface design | Retroactive compatibility |
| Documentation | Types explicitly state relationships | Relationships are implicit |
| Refactoring | Renaming a type breaks compatibility | Changing structure breaks compatibility |
| Cross-library | Needs shared interface definitions | Types compose across library boundaries |

## 🔬 Deep Dive

### Trade-offs / Historical Context

Dynamic languages like Python and Ruby practice "duck typing" — runtime structural typing. If it has a `.read()` method, treat it as a file-like object. This is the dynamic equivalent of Go's implicit interfaces. TypeScript and Python type hints attempt to formalize duck typing with compile-time structural checks while preserving the flexibility.

The core philosophical argument for nominal typing is that **structure doesn't capture semantics**. A `Meters` type and a `Seconds` type might both wrap a `float64`, but adding meters to seconds is a category error. Nominal typing catches this; structural typing doesn't.

Languages like Haskell and Rust address this with **newtypes** — zero-cost nominal wrappers around existing types. `struct Meters(f64)` is structurally identical to `f64` but nominally distinct. This combines structural efficiency with nominal safety.

OCaml's split design is historically interesting because it demonstrates that a language does not have to choose one model exclusively. Its core types stay nominal, while its object system uses structural typing via row polymorphism. Rust is similarly hybrid in a different way: nominal structs and enums, but traits that feel structural in capability while still requiring explicit declarations.

## 🏋️ Practice

1. Invent two domain types with the same representation—such as `Velocity` and `Temperature`—and explain why a nominal system would keep them separate while a structural system might not.
2. Compare Java interfaces, Go interfaces, and TypeScript interfaces. Which relationships must be declared in advance, and which can emerge retroactively?
3. Look at the trade-off table and choose one system for a plugin ecosystem spanning many third-party libraries. Defend your choice using safety, flexibility, and cross-library composition.

## References

- [[Programming Languages/Sources/Sources Index|Sources Index]]
