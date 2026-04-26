---
tags: [pl, chunk, error-handling, rust-question-mark]
up: "[[Result and Option Types]]"
---

# The Question Mark Operator Ergonomic Error Propagation

Rust's \?\ operator is widely considered one of the best error handling innovations in programming language design.

## The Problem It Solves

Without \?\, every fallible operation needs explicit matching with verbose match expressions.

With \?\:
- Concise error propagation
- Automatic type conversion via From trait
- Early return on error

## What ? Actually Does

\xpression?\ desugars to:
- On Ok(value): returns value
- On Err(err): returns Err(From::from(err)) from the function

## Comparison with Other Languages

| Language | Error Propagation | Verbosity |
|----------|------------------|-----------|
| Rust | \?\ operator | Concise, type-safe |
| Go | \if err != nil { return err }\ | Verbose (30%+ of code) |
| Swift | \	ry\ keyword | Similar to \?\ |
| Zig | \	ry\ keyword | Similar to \?\ |

## Key Insight
The \?\ operator proves that explicit error handling doesn't have to be verbose. Swift's \	ry\ and Zig's \	ry\ took direct inspiration from Rust's \?\.

## References
→ [[Sources Index]]
