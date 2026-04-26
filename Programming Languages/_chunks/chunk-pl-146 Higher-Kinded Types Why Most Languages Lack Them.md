---
tags: [pl, chunk, functional, hkt]
up: "[[Type Systems Overview]]"
---

# Higher-Kinded Types Why Most Languages Lack Them

Higher-kinded types (HKTs) are type constructors that take other type constructors as parameters — the type-level equivalent of higher-order functions.

## What Are HKTs?

Regular generics: List<Int> — a concrete type applied to a concrete type
HKTs: Functor<F> where F is itself generic (like List, Option, Result)

`haskell
-- Haskell: F is a type constructor (kind * -> *)
class Functor f where
    fmap :: (a -> b) -> f a -> f b

-- Works for ANY container: List, Maybe, IO, Tree, etc.
instance Functor [] where
    fmap = map

instance Functor Maybe where
    fmap f Nothing = Nothing
    fmap f (Just x) = Just (f x)
`

## Why HKTs Matter

Without HKTs, you can't abstract over containers generically:

`ust
// Rust: CANNOT write this (no HKTs)
trait Functor<F> {  // F should be a type constructor
    fn map<A, B>(fa: F<A>, f: fn(A) -> B) -> F<B>;
}

// Instead, Rust uses individual Iterator, Option::map, Result::map
// Each reimplements the pattern separately
`

## Language Support

| Language | HKT Support | How |
|----------|-------------|-----|
| Haskell | Full | Kind system with * -> * |
| Scala | Full | F[_] syntax |
| OCaml | Modules only | Functors (module-level) |
| Rust | None (workarounds exist) | GATs approximate some uses |
| Kotlin | None | Arrow library simulates |
| Swift | None | Protocol with associated types approximates |
| TypeScript | None | Mapped types approximate |
| Java | None | |
| Go | None | |

## Workarounds in Languages Without HKTs

**Rust GATs (Generic Associated Types):**
`ust
trait Container {
    type Item<T>;  // Associated type that's generic
    fn map<A, B>(self: Self::Item<A>, f: fn(A) -> B) -> Self::Item<B>;
}
`
GATs cover many HKT use cases but not all.

**Kotlin Arrow:**
`kotlin
// Arrow library uses "type class" pattern with extension functions
fun <F> Kind<F, Int>.double(): Kind<F, Int> = ...
`

## Why Most Languages Skip HKTs

1. **Complexity:** Understanding kinds requires type theory background
2. **Diminishing returns:** 95% of generic code doesn't need HKTs
3. **Implementation complexity:** Type inference with HKTs is much harder
4. **Error messages:** Already complex with basic generics
5. **Alternative patterns:** Interfaces/traits + code generation covers most cases

## Key Insight
HKTs are the dividing line between "practical" and "principled" type systems. Languages that support them (Haskell, Scala) enable powerful abstractions like Monad, Applicative, and Traversable. Languages that don't (Rust, Go, Java) accept some code duplication in exchange for simpler mental models.

## References
→ [[Sources Index]]
