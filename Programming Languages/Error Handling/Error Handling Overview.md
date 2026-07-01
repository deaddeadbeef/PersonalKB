---
tags: [programming-languages, error-handling]
up: "[[Programming Languages]]"
confidence: established
freshness: stable
tier-coverage: [intuition, core, deep-dive]
---
# Error Handling Overview

How a language handles errors reveals its philosophy about failure, safety, and programmer responsibility. Error handling is a design axis where languages diverge dramatically — from C's trust-the-programmer approach to Rust's make-errors-impossible-to-ignore approach.

## The Fundamental Approaches

| Strategy | Mechanism | Languages |
|----------|-----------|-----------|
| Exceptions | Throw/catch stack unwinding | Java, Python, C#, Ruby, C++, OCaml, Kotlin, Swift |
| Result/Option types | Return values encoding success/failure | Rust, Haskell, OCaml, Kotlin, Swift, Go (error values) |
| Error codes | Integer or sentinel return values | C, older APIs |
| Panics | Unrecoverable abort + optional recovery | Rust (panic!), Go (panic/recover) |
| Conditions | Restartable exceptions | Common Lisp |

## The Design Tension

Every error handling system navigates a tension between **ergonomics** and **visibility**. Exceptions are ergonomic (you don't have to handle them at every call site) but invisible (you can't see which functions might throw just by reading the signature). Result types are visible (the function signature tells you it can fail) but verbose (every call site must handle the error or explicitly propagate it).

## In This Hub

- [[Exception-Based Error Handling]]
- [[Result and Option Types]]
- [[Error Codes and Sentinel Values]]
- [[Panic and Recovery Mechanisms]]
- [[Effect Systems and Checked Exceptions]]

## References

- [[Programming Languages/Sources/Sources Index|Sources Index]]
