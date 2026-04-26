---
tags: [pl, chunk, dependent-types, verification]
up: "[[Type Systems Overview]]"
---

# Dependent Types From Theory to Practice

Dependent types allow types to depend on values, enabling the compiler to verify properties that regular type systems cannot express.

## The Power of Dependent Types

### Length-Indexed Vectors
The type encodes the length
append : Vect n a -> Vect m a -> Vect (n + m) a
The compiler PROVES the output length equals the sum of inputs

### Matrix Multiplication
Types ensure dimensions are compatible
multiply : Matrix m n -> Matrix n p -> Matrix m p
Trying to multiply incompatible matrices is a TYPE ERROR

### Sorted Lists
The type guarantees the list is sorted
data SortedList : List Nat -> Type where
  insert maintains the sortedness proof

## Mainstream Approximations

Languages are incorporating limited dependent type features:

**Rust const generics:**
fn dot_product<const N: usize>(a: [f64; N], b: [f64; N]) -> f64 {
    a.iter().zip(b.iter()).map(|(x, y)| x * y).sum()
}
N is a value in the type - a limited form of dependent typing

**TypeScript conditional types:**
type ElementType<T> = T extends (infer E)[] ? E : never;
Types depend on other types (not values, but approaching it)

**Haskell with extensions:**
- DataKinds promotes values to types
- GADTs enable type-level computation
- Singletons library bridges value/type gap
- Not full dependent types but can encode many patterns

## Why Full Dependent Types Remain Niche

| Challenge | Explanation |
|-----------|------------|
| Decidability | Type checking can become undecidable |
| Phase distinction | Blurs compile-time vs runtime |
| Ergonomics | Proofs are code you must write and maintain |
| Tooling | Limited IDE support, error messages |
| Learning curve | Requires type theory background |

## The Lean 4 Bridge
Lean 4 is the most promising bridge between dependent types and practical programming:
- Full dependent types
- Compiled to C for performance
- Used by Mathlib (largest math formalization project)
- Growing adoption beyond academia

## Key Insight
The trend is clear: mainstream languages are incrementally absorbing dependent-type ideas (const generics, GADTs, conditional types). Full dependent types may never go mainstream, but their influence is already visible in every modern type system.

## References
-> [[Sources Index]]
