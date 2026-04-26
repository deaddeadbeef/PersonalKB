---
tags: [raw, programming-languages, generics]
source: "Types and Programming Languages (Pierce), Rust Reference, Java Generics Tutorial"
created: 2025-07-25
---

# raw-pl-016: Generics and Polymorphism Across Languages

## Parametric Polymorphism — The Core Idea

Write code once, use with any type. The function n identity<T>(x: T) -> T works for any T without knowing what T is. This is fundamentally different from subtype polymorphism (inheritance) where a Dog IS-A Animal.

## Implementation Strategies

**Monomorphization (Rust, C++):** The compiler generates specialized versions for each concrete type. Vec<i32> and Vec<String> become separate compiled types. Benefit: zero runtime overhead, optimal code per type. Cost: code size growth, longer compilation, no dynamic polymorphism without trait objects.

**Type erasure (Java):** Generic types are erased to their bounds at compile time. List<String> becomes List<Object> in bytecode. Benefit: backward compatibility, no code duplication. Cost: no runtime type information, can't create 
ew T(), boxing required for primitives.

**Reification (.NET):** Generic types preserve type information at runtime. List<int> is a different runtime type from List<string>. Benefits of both: runtime type checking AND separate implementations. Cost: more complex runtime.

## Bounded Polymorphism

Constraining what types a generic can accept:
- **Rust trait bounds:** n sort<T: Ord>(slice: &mut [T]) — T must implement Ord
- **Java bounded wildcards:** <T extends Comparable<T>> — T must be Comparable
- **Haskell type class constraints:** sort :: Ord a => [a] -> [a] — a must be in class Ord
- **Go type constraints:** unc Sort[T constraints.Ordered](s []T) — T satisfies Ordered
- **C++ concepts (C++20):** 	emplate<std::totally_ordered T> — named constraints

## Higher-Kinded Types

Types that take type parameters themselves. Functor, Monad, Applicative in Haskell are higher-kinded — they abstract over type constructors (like Maybe, List, IO), not just types.

Haskell and Scala support HKTs. Rust does not (GATs provide some of the power). This is why Rust can't express a generic Monad trait — it would need higher-kinded types.

## Variance

How generic types relate when their type parameters are related. If Dog extends Animal:
- **Covariant:** List<Dog> is a subtype of List<Animal> (safe for reading)
- **Contravariant:** Consumer<Animal> is a subtype of Consumer<Dog> (safe for writing)
- **Invariant:** No subtyping relationship (safe for both)

Java uses use-site variance (wildcards: ? extends T, ? super T). Kotlin and C# use declaration-site variance (out T, in T). Rust's PhantomData controls variance. OCaml infers variance for type parameters.
