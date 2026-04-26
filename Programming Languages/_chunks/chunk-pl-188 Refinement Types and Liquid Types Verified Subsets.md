---
tags: [pl, chunk, type-systems, refinement]
up: "[[Type Systems Overview]]"
---

# Refinement Types and Liquid Types Verified Subsets

Refinement types add predicates to types, enabling the compiler to verify properties that regular types cannot express.

## What Are Refinement Types?

A refinement type is a base type plus a predicate:
\\\
{x : Int | x > 0}           -- Positive integers
{s : String | len(s) < 256}  -- Short strings
{xs : [Int] | sorted(xs)}    -- Sorted lists
\\\

## Liquid Haskell

LiquidHaskell adds refinement types to Haskell:
\\\haskell
{-@ type Pos = {v:Int | v > 0} @-}
{-@ type NonEmpty a = {v:[a] | len v > 0} @-}

{-@ head :: NonEmpty a -> a @-}
head (x:_) = x
-- head [] is a COMPILE-TIME error!
-- The refinement type proves the list is non-empty

{-@ divide :: Int -> Pos -> Int @-}
divide x y = x \div\ y
-- Cannot call divide with 0 as second argument
-- PROVEN safe at compile time
\\\

## Similar Systems in Other Languages

| Language | System | Maturity |
|----------|--------|----------|
| Haskell | LiquidHaskell | Research, usable |
| TypeScript | Branded types (workaround) | Manual, limited |
| Rust | Refinement crates (partial) | Limited |
| Ada/SPARK | Subtype predicates | Production (avionics) |
| F* | Dependent + refinement types | Research (verified crypto) |

### TypeScript Branded Types (Approximation)
\\\	ypescript
type PositiveInt = number & { __brand: 'PositiveInt' };

function makePositive(n: number): PositiveInt {
    if (n <= 0) throw new Error("Must be positive");
    return n as PositiveInt;
}
// Runtime check, not compile-time proof
\\\

## Refinement Types vs Dependent Types

| Property | Refinement Types | Dependent Types |
|----------|-----------------|----------------|
| Expressiveness | Predicates on base types | Types depend on values |
| Verification | SMT solver | Type checker = theorem prover |
| Automation | High (SMT) | Low (manual proofs) |
| Usability | Moderate | Steep learning curve |
| Example | LiquidHaskell | Idris, Lean |

## Key Insight
Refinement types hit a sweet spot: more expressive than regular types, easier than dependent types. They use SMT solvers to automatically verify predicates, reducing the proof burden on developers. LiquidHaskell and Ada/SPARK demonstrate they work in practice. This is likely the next step for mainstream type systems after generics and null safety.

## References
→ [[Sources Index]]
