---
tags: [raw, programming-languages, type-safety]
source: "Types and Programming Languages (Pierce), Safe Systems Programming in Rust and Beyond"
created: 2025-07-25
---

# raw-pl-029: Type Safety — From Weak to Dependent

## The Type Safety Spectrum

Languages range from essentially untyped to fully formally verified:

**Weakly typed (C):** Types exist but the compiler barely enforces them. Implicit conversions, void pointers, unchecked casts. The type system is a suggestion.

**Strongly typed, dynamic (Python, Ruby):** Types are enforced at runtime. "3" + 3 throws TypeError. You can't accidentally mix incompatible types, but errors happen at runtime.

**Strongly typed, static (Java, Go):** Types checked at compile time. The compiler prevents type mismatches. But: null is a universal escape hatch in Java, and Go's interface{} bypasses typing.

**Strongly typed, static, null-safe (Kotlin, Swift, Rust):** No null references. Optional types (T?, Option<T>) force explicit handling. Eliminates null pointer errors.

**Strongly typed with exhaustive ADTs (Rust, Haskell, OCaml):** Algebraic data types with exhaustive pattern matching. The compiler ensures every case is handled. Adding a variant forces updating all match sites.

**Dependently typed (Idris, Agda, Lean):** Types can depend on values. A vector's type includes its length: Vec 5 Int. The type system can express: "this function takes a non-empty list," "this matrix multiplication is dimension-compatible," "this array index is in bounds."

## Null Safety

Tony Hoare's "billion-dollar mistake." Languages that have eliminated null:
- **Rust:** Option<T> — Some(value) or None. No null.
- **Haskell:** Maybe a — Just value or Nothing. No null.
- **Kotlin:** T (non-nullable) vs T? (nullable). Compiler enforces null checks.
- **Swift:** T vs T? (Optional). force-unwrap ! exists but is discouraged.

Languages that still have null: Java (mitigated by Optional and annotations), Go (nil for pointers, slices, maps, channels, interfaces), C/C++ (null pointers everywhere).

## Type-Level Programming

Advanced type systems enable computation at the type level:
- **Haskell:** Type families, GADTs, DataKinds — push values into types for compile-time guarantees
- **TypeScript:** Conditional types, template literal types, mapped types — turing-complete type-level computation
- **Rust:** Const generics, associated types, trait bounds — limited but growing
- **C++:** Template metaprogramming, concepts (C++20) — powerful but hard to read

## The Safety-Ergonomics Trade-off

More type safety means more upfront effort:
- Python: Write code, run it, fix type errors at runtime. Fast to prototype.
- TypeScript: Write types, compiler checks them. Slower to start but catches errors.
- Rust: Write types + lifetimes + trait bounds. Slowest to start but catches the most errors.
- Haskell: Write types + prove properties. Slowest iteration but highest confidence.

The trend: languages are moving up the safety spectrum, but making it less painful via inference and ergonomic syntax.
