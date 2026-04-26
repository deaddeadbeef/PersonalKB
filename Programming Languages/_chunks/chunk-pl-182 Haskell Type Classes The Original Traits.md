---
tags: [pl, chunk, haskell, type-classes]
up: "[[Haskell Language Profile]]"
---

# Haskell Type Classes The Original Traits

Type classes are Haskell's mechanism for ad-hoc polymorphism. They directly inspired Rust's traits, Swift's protocols, and Scala's implicits.

## How Type Classes Work

\\\haskell
-- Define a type class (like an interface)
class Eq a where
    (==) :: a -> a -> Bool
    (/=) :: a -> a -> Bool
    x /= y = not (x == y)  -- Default implementation

-- Implement for a type (like impl Trait for Type)
instance Eq Bool where
    True == True = True
    False == False = True
    _ == _ = False

-- Use in constraints (like trait bounds)
member :: Eq a => a -> [a] -> Bool
member x [] = False
member x (y:ys) = x == y || member x ys
\\\

## Type Class Hierarchy

Haskell's standard type classes form a mathematical hierarchy:
\\\
Functor -> Applicative -> Monad

    |
Foldable -> Traversable

Eq -> Ord
Num -> Fractional -> Floating
Show, Read
Semigroup -> Monoid
\\\

## Type Classes vs Alternatives

| Mechanism | Language | Dispatch | Coherence |
|-----------|---------|----------|-----------|
| Type classes | Haskell | Static (dictionary) | Global coherence |
| Traits | Rust | Static (monomorphized) | Orphan rule |
| Protocols | Swift | Static or dynamic | Module-scoped |
| Interfaces | Java, Go | Dynamic (vtable) | N/A |
| Implicits/givens | Scala | Static (implicit search) | Import-scoped |

## Coherence and the Orphan Rule

Type classes (and Rust traits) enforce **coherence**: there's exactly one implementation of a type class for any given type, globally.

Haskell: Only one \instance Eq MyType\ can exist in the entire program.
Rust: The orphan rule prevents implementing foreign traits for foreign types.

This prevents ambiguity but limits extensibility.

## Key Insight
Haskell's type classes proved that you can have the flexibility of OOP interfaces with the performance of static dispatch. Rust's traits are essentially type classes with monomorphization instead of dictionary passing. The pattern is so successful that every new statically-typed language adopts some form of it.

## References
→ [[Sources Index]]
