---
tags: [programming-languages, error-handling, effects]
up: "[[Error Handling Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Effect Systems and Checked Exceptions

> **One-line summary:** Effect systems extend type systems to track and enforce which side effects — including errors — a function can perform.

---

## 🎯 Intuition

- **The Core Idea:** Effect systems track which side effects a function can perform — including which errors it can produce. They represent the cutting edge of error handling design, learning from both the success of Result types and the failure of Java's checked exceptions.
- **Analogy:** Think of an effect system as a customs declaration form for functions: each function declares what "goods" (side effects) it carries, and the compiler acts as border control ensuring nothing undeclared gets through.
- **Why It Matters:** Effect systems unify ad-hoc tracking of errors, async, and mutability into a single, composable mechanism — solving problems that plagued earlier approaches like Java's checked exceptions.

---

## ⚙️ Core Mechanics

### How It Works

An effect system extends a language's type system to track computational effects: I/O, exceptions, state mutation, nondeterminism, concurrency. A function's type signature declares not just what it returns but what effects it performs. The compiler ensures effects are handled appropriately.

### Key Concepts

| Concept | Description |
|---|---|
| Effect | A tracked side effect (I/O, exceptions, state mutation, nondeterminism, concurrency) |
| Effect handler | Code that intercepts and processes a declared effect |
| Effect propagation | Calling a function adds its effects to the caller's effect set |
| Effect inference | Compiler deduces effects from the function body (e.g., Zig error sets) |
| Effect polymorphism | Higher-order functions that are generic over their arguments' effects |

### Language Examples

| Language | Mechanism | Key Feature |
|---|---|---|
| Java | Checked exceptions (`throws` clause) | Early, limited effect system; poor generics/lambda interaction |
| Zig | Error sets (`!T` return type) | Compile-time tracked, inferred from bodies, ergonomic `try` keyword |
| OCaml 5 | Algebraic effects | User-definable, resumable effects; subsumes exceptions and coroutines |
| Koka | Algebraic effects (built-in) | Designed around effects from the ground up; full effect inference |
| Rust | Ad-hoc markers (`Result`, `async`, `unsafe`, `Send`/`Sync`) | Implicit tracking without a unified effect system |

### Key Facts

- Effect tracking must compose well with the rest of the language, especially generics and higher-order functions.
- Error sets in Zig are inferred from function bodies, not manually declared — avoiding Java's verbosity problems.
- Rust tracks several effects implicitly but lacks a unified effect system.

---

## 🔬 Deep Dive

### Formal Foundations

**Algebraic Effects (OCaml 5, Research Languages)**

OCaml 5.0 introduced **algebraic effects** — a principled mechanism for user-definable effects. An effect is like an exception that can be resumed: the handler can provide a value and continue execution at the point where the effect was raised.

This enables: user-defined async/await, custom scheduling, transactional memory, and exception-like error handling — all as library code, not language primitives. Algebraic effects subsume exceptions, coroutines, and generators into a single mechanism.

**Koka** (Microsoft Research) is designed around algebraic effects from the ground up. Every function's type signature lists its effects. The compiler tracks effect propagation and ensures all effects are handled.

**Zig's Compile-Time Error Sets**

Zig uses error sets — compile-time tracked collections of possible errors. A function returning `!T` can fail with errors from its error set. The compiler tracks which errors are possible and ensures they're handled. Error sets compose: calling a function adds its error set to the caller's possible errors.

This is similar to checked exceptions but without the verbosity problems: error sets are inferred from function bodies, not manually declared. The `try` keyword propagates errors ergonomically.

**Rust's Implicit Effect Tracking**

Rust doesn't have a formal effect system, but its type system implicitly tracks several effects:
- **Fallibility:** `Result<T, E>` in the return type
- **Async:** `async fn` marks asynchronous functions
- **Unsafe:** `unsafe` blocks mark code with unchecked invariants
- **Send/Sync:** Trait bounds track thread-safety

These are ad-hoc effect markers rather than a unified system. Rust community discussion about adding formal effects continues.

### Trade-offs and Design Decisions

**Java's Checked Exceptions: The Cautionary Tale**

Java's checked exceptions were an early, limited effect system: a function's throws clause declares its error effects. The failure teaches important lessons:
- **Verbosity:** Every intermediate function must declare exceptions it might propagate
- **Generics incompatibility:** `Function<A, B>` can't express "this function throws IOException"
- **Lambda friction:** Checked exceptions don't work well with functional APIs (streams, map, filter)
- **Incentive to suppress:** Developers catch-and-ignore to avoid the boilerplate

### Historical Context

**The Future of Error Handling**

The trend is toward: (1) richer type-level effect tracking (what can this function do?), (2) user-definable effects (not hardcoded into the language), (3) composable effect handling (effects work with generics, lambdas, and higher-order functions), and (4) gradual adoption (add effect tracking to existing code incrementally). Algebraic effects in OCaml 5 and Koka represent the leading edge of this evolution.

---

## 🏋️ Practice

### Warm-Up (5 min)

1. Explain the customs-declaration analogy in your own words: what are the "goods," and what does the compiler check?
2. List the effect-like markers Rust already tracks even without a unified effect system.

### Core Problems

3. Compare Java's checked exceptions with Zig's error sets. Why does Zig avoid some of Java's problems?
4. Describe how algebraic effects differ from ordinary exceptions.

### Challenge

5. Use the "future of error handling" section to predict what a well-designed effect system must support.

---

*See also:* [[Error Handling Overview]], [[Result and Option Types]], [[Exception-Based Error Handling]]

## Supporting Chunks / References

- [[Sources Index]]
