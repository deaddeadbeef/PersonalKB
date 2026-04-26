---
tags: [programming-languages, error-handling, result-types]
up: "[[Error Handling Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Result and Option Types

> Result and Option types encode success/failure and presence/absence directly in the type system — the preferred error handling mechanism for modern languages.

---

## 🎯 Intuition

### Core Idea

Result and Option types replace invisible failure modes (null, unchecked exceptions) with values the type system can see and the compiler can enforce. Every operation that might fail returns an explicit envelope: success-with-value or failure-with-reason. Every operation that might be absent returns presence-or-absence. You cannot proceed without acknowledging which case you received.

### Analogy

Result/Option = **a package delivery where every delivery comes with a tracking slip saying "delivered" or "failed — here's why," and you MUST sign acknowledging which.** You can never find an unmarked box on your doorstep; the system won't let the courier leave without your signature on the right slip. Option is the simpler variant: the slip says "package here" or "nothing to deliver" — no reason given, just presence or absence.

### Why It Matters

Tony Hoare called null references his "billion-dollar mistake." Option types eliminate null pointer exceptions at compile time. Result types make error paths as visible as success paths, turning runtime surprises into compile-time obligations. This approach, pioneered by ML-family languages, has become the preferred error handling mechanism for new languages.

---

## ⚙️ Core Mechanics

### How It Works

The compiler forces you to handle the None/Err case — you cannot use an Option or Result value as if it's guaranteed to contain something. Functions that can fail declare it in their return type; callers must explicitly unwrap, match, propagate, or transform the result before using the inner value.

### Key Concepts — Option/Maybe

Option types replace null with an explicit type:

| Language | Type | Variants |
|----------|------|----------|
| Rust | `Option<T>` | `Some(value)` / `None` |
| Haskell | `Maybe a` | `Just value` / `Nothing` |
| OCaml | `'a option` | `Some value` / `None` |
| Swift | `T?` (optional) | value / `nil` (typed, not universal null) |
| Kotlin | `T?` (nullable) | value / `null` (with null safety operators; `T` is non-nullable) |

### Key Concepts — Result

Result types carry either a success value or an error value:

| Language | Type | Variants |
|----------|------|----------|
| Rust | `Result<T, E>` | `Ok(value)` / `Err(error)` |
| Haskell | `Either a b` | `Right value` / `Left error` (or custom error monads) |
| OCaml | `('a, 'b) result` | `Ok value` / `Error error` |
| Swift | `Result<Success, Failure>` | `.success(value)` / `.failure(error)` (also `throws` functions) |
| Kotlin | `Result<T>` | Used primarily in coroutine contexts |

### Language Examples

**Rust — Result + `?` Operator.** Rust's error handling is built around Result types with the `?` operator for ergonomic propagation. If a function returns `Result<T, E>`, calling `another_function()?` either unwraps the Ok value or returns the Err early from the current function. This gives visibility (function signatures show which functions can fail) with nearly the ergonomics of exceptions (a single `?` replaces try/catch blocks). The trade-off: every fallible call site needs explicit handling (`?`, `match`, `unwrap`, or combinators).

**Haskell — Monadic Composition.** Haskell uses the `Either` type for errors and `Maybe` for optionality, composed using monadic operations (`>>=`, do-notation). The power: error handling composes naturally with other monadic effects. The cost: understanding monads is a prerequisite, creating a steep learning curve.

**Go — Error Values.** Go takes a unique approach: functions return an error value alongside the result. By convention, the error is the last return value:

```go
result, err := doSomething()
if err != nil {
    return err
}
```

This is explicit but verbose — the `if err != nil` pattern is the most written Go code. Go chose this verbosity deliberately: error handling should be visible and explicit, never hidden. Critics note it creates boilerplate; proponents argue it forces you to think about every failure path.

### Key Facts

- Option eliminates null pointer exceptions at compile time by forcing callers to handle the absent case.
- Result makes error paths first-class citizens in function signatures, visible to both humans and tooling.
- The `?` operator in Rust is syntactic sugar for match-and-return-err, giving exception-like ergonomics without hidden control flow.
- Go intentionally omits propagation sugar — verbosity is a feature, not a bug.

---

## 🔬 Deep Dive

### Formal Foundations — Monadic Composition

Both `Option` and `Result` form monads: they support `bind` (Haskell `>>=`, Rust `and_then`) and `return` (wrapping a value in `Some`/`Ok`). This means error-producing computations compose sequentially — if any step fails, the chain short-circuits. Haskell exploits this directly through do-notation; Rust's `?` achieves the same desugaring with imperative syntax. OCaml's `let*` binding operators provide yet another surface syntax for the same monadic plumbing.

### Trade-offs and Design Decisions

**The Propagation Problem.** Result types require explicit propagation at every call site. Without syntactic support, this creates boilerplate:

| Language | Propagation Mechanism | Notes |
|----------|----------------------|-------|
| Rust | `?` operator | Sugar for match-and-return-err |
| Haskell | do-notation | Monadic sequencing |
| OCaml | `let*` / pattern matching | Binding operators |
| Go | (none) | `if err != nil` boilerplate is intentional |

**When to Use Each.**

| Approach | Best When |
|----------|-----------|
| Result types | Errors are expected and recoverable (file not found, network timeout); you want type-safe error propagation; you need to transform or combine error types |
| Exceptions | Errors are unexpected (programmer bugs); deeply nested call stacks where errors skip many layers; code where most operations succeed |

### Historical Context

The Option/Result pattern originates in the ML family of languages (Standard ML, OCaml) where algebraic data types make defining `Some`/`None` and `Ok`/`Error` natural. Haskell generalized these patterns through its monad type class. Rust adopted and popularized them for systems programming, proving that type-safe error handling need not sacrifice performance or ergonomics. Swift and Kotlin brought lighter-weight variants into mainstream mobile development.

---

## 🏋️ Practice

### Warm-Up

1. Explain why `Option<T>` is safer than a nullable pointer even though both represent "might not have a value."
2. Given a Rust function `fn parse_port(s: &str) -> Result<u16, ParseIntError>`, what happens at the call site if you append `?` vs. if you call `.unwrap()`?
3. In Go's `result, err := doSomething()` pattern, what goes wrong if you forget to check `err`?

### Core Problems

1. Design an `Option`-based API for a key-value store `get` method in your language of choice. Show how a caller chains two lookups where the second depends on the first, handling the absent case without any `if/else`.
2. Compare Rust's `?` operator and Haskell's do-notation for a three-step pipeline where each step can fail with a different error type. What must be true about the error types for the chain to compile in each language?

### Challenge

1. Implement a small interpreter for an arithmetic expression tree where division can fail (divide-by-zero) and variable lookup can fail (undefined variable). Use Result types to propagate errors without exceptions. Then refactor to add a logging side-effect at each node — how does your error handling strategy interact with the effect?

---

*See also:* [[Error Handling Overview]] · [[Algebraic Data Types]] · [[Monads]] · [[Rust Error Handling]] · [[Go Idioms]]

---

## Supporting Chunks / References

- [[Sources Index]]
