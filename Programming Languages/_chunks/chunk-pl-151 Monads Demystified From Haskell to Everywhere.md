---
tags: [pl, chunk, haskell, monads]
up: "[[Haskell – Language Profile]]"
---

# Monads Demystified From Haskell to Everywhere

Monads are Haskell's most famous (and most misunderstood) concept. In essence, a monad is a design pattern for chaining computations that carry context.

## The Core Idea

A monad wraps a value with context (failure, multiple results, I/O, state) and provides:
1. **return** (or pure): Wrap a plain value → `return 42 :: Maybe Int` gives `Just 42`
2. **bind** (>>=): Chain computations that might add context

```haskell
-- Maybe monad chains operations that might fail
safeDivide :: Int -> Int -> Maybe Int
safeDivide _ 0 = Nothing
safeDivide x y = Just (x `div` y)

-- Without monads (nested case statements):
result = case safeDivide 100 5 of
    Nothing -> Nothing
    Just a  -> case safeDivide a 2 of
        Nothing -> Nothing
        Just b  -> Just b

-- With monadic bind:
result = safeDivide 100 5 >>= \a -> safeDivide a 2

-- With do notation (syntactic sugar):
result = do
    a <- safeDivide 100 5
    b <- safeDivide a 2
    return b
```

## Common Monads

| Monad | Context | Example Use |
|-------|---------|-------------|
| Maybe | Might fail | Chaining lookups that might return Nothing |
| Either e | Might fail with error info | Error propagation with context |
| IO | Side effects | All I/O in Haskell |
| State s | Mutable state | Stateful computation without mutation |
| Reader r | Shared environment | Configuration, dependency injection |
| Writer w | Accumulated output | Logging, audit trails |
| List | Multiple results | Non-deterministic computation |
| Parser | Parsing state | Parsec combinators |

## Monads in Other Languages

The monad pattern appears everywhere, just without the name:
- **Rust:** `Option::and_then()` is bind for Option. `Result::and_then()` is bind for Result. The `?` operator is do-notation for Result.
- **JavaScript:** `Promise.then()` is bind for Promise (but breaks monad laws slightly)
- **Kotlin:** `?.let {}` chains on nullable (partial monad behavior)
- **C#:** LINQ's `SelectMany` is monadic bind. `from x in xs select ...` is do-notation.
- **Swift:** Optional chaining `?.` is bind for Optional

## Why Monads Matter Beyond Haskell

Monads solve the "colored function" problem in Haskell: pure functions and effectful functions are different types, and monads provide the bridge. This means:
- All side effects are tracked in the type system
- Pure code is guaranteed pure – no hidden I/O
- Different effects compose via monad transformers (or algebraic effects)

## Key Insight
You don't need to understand category theory to use monads. They're just a pattern: "a box with a flatMap/bind operation." Rust's `?` operator and C#'s LINQ prove monadic patterns can be ergonomic. Haskell just names the pattern and makes it explicit.

## References
→ [[Sources Index]]
