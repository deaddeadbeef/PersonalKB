---
tags: [pl, raw, dependent-types, formal-verification]
up: "[[Sources Index]]"
---

# Raw Note 038 — Dependent Types and Formal Verification

## The Type Safety Spectrum

No types → Dynamic → Static → Generics → GADTs → Dependent → Full specification
Assembly    Python    Java      Rust      Haskell    Idris      Coq/Lean

## Dependent Types

A type system where types can depend on values. This enables encoding invariants in the type system itself.

### What Dependent Types Enable

`idris
-- A vector whose length is part of its type
data Vect : Nat -> Type -> Type where
  Nil  : Vect 0 a
  (::) : a -> Vect n a -> Vect (S n) a

-- append's return type proves the lengths add up
append : Vect n a -> Vect m a -> Vect (n + m) a
`

This makes it impossible to write `head` on an empty vector — the type system rejects it at compile time.

### Languages with Dependent Types
- **Idris 2:** Full dependent types, designed for practical programming
- **Agda:** Dependent types for mathematical proofs
- **Lean 4:** Proof assistant + general-purpose programming (used by Mathlib)
- **Coq:** Foundational proof assistant, extracts to OCaml/Haskell
- **F*:** Microsoft Research, effectful dependent types

### Dependent Types Leaking into Mainstream
- **TypeScript:** Conditional types, template literal types approach dependent-type expressiveness
- **Rust:** Const generics (`[T; N]` where N is a value) are a limited form
- **Haskell:** GADTs, type families, DataKinds, singletons — encoding dependent-type patterns
- **Scala 3:** Match types, dependent function types

## Formal Verification

### Verified Software
- **CompCert:** Verified C compiler (proved in Coq to preserve semantics)
- **seL4:** Formally verified microkernel (Isabelle/HOL)
- **HACL*:** Verified cryptographic library (F*)
- **Everest:** Verified HTTPS stack (F*, Kremlin)
- **CertiKOS:** Verified concurrent OS kernel (Coq)

### Lightweight Verification in Practice
- **Rust's borrow checker:** Verifies memory safety properties
- **Ada/SPARK:** Subset of Ada with formal verification support — used in avionics
- **Dafny:** Microsoft Research language with built-in verification
- **TLA+:** Temporal logic specification language (used at Amazon for AWS)

## Why Dependent Types Aren't Mainstream

| Challenge | Impact |
|-----------|--------|
| Learning curve | Requires understanding type theory |
| Compile times | Type checking becomes theorem proving |
| Tooling | Fewer IDEs, debuggers, profilers |
| Diminishing returns | 95% of bugs caught by simpler type systems |
| Proof burden | Developer must provide proofs, not just code |

## Key Insight
The practical frontier is moving: Rust proved compile-time verification is viable for memory safety. Lean 4 is making dependent types more accessible. The trend is toward more expressive type systems that catch more bugs without requiring full formal proofs.

## References
→ [[Sources Index]]
