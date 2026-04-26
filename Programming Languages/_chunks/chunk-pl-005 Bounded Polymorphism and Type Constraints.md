---
tags: [chunk, programming-languages, type-systems]
source: "[[raw-pl-016]]"
---

# chunk-pl-005 Bounded Polymorphism and Type Constraints

Constraining what types a generic accepts:

- **Rust:** n sort<T: Ord>(slice: &mut [T]) — T must implement Ord trait
- **Java:** <T extends Comparable<T>> — T must implement Comparable
- **Haskell:** sort :: Ord a => [a] -> [a] — a must be in Ord class
- **Go 1.18:** unc Sort[T constraints.Ordered](s []T) — T satisfies Ordered
- **C++20:** 	emplate<std::totally_ordered T> — named concepts

**Higher-kinded types (HKTs):** Types parameterized over type constructors. Haskell's Functor, Monad, Applicative abstract over Maybe, List, IO. Rust lacks HKTs — can't express a generic Monad trait. GATs (Generic Associated Types) provide partial power.

**Variance:** How generic types relate when parameters are related. Covariant (List<Dog> subtypes List<Animal> for reading), contravariant (for writing), invariant (for both). Java: use-site variance (wildcards). Kotlin/C#: declaration-site variance (out/in).
