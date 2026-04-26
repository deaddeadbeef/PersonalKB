---
tags: [raw, programming-languages, error-handling]
source: "Programming Language Pragmatics (Scott, 2015), Rust Error Handling Working Group"
created: 2025-07-25
---

# raw-pl-004: Error Handling Philosophies

## The Fundamental Question

When a function can fail, how should it communicate that failure to its caller? This question has produced four major answers, each reflecting a different philosophy about safety, ergonomics, and trust.

## Exceptions (Java, Python, C++, OCaml, Ruby)

Throw an error that propagates up the call stack until caught. Pros: ergonomic (intermediate functions don't need to handle errors), familiar, powerful (carry arbitrary error information). Cons: invisible control flow (you can't tell from a function signature that it might throw), exception safety is hard (maintaining invariants when exceptions interrupt operations).

Java's checked exceptions attempted to make exceptions visible in types but failed due to verbosity, poor composition with generics, and developer frustration. No major language adopted checked exceptions after Java. The consensus: checked exceptions were a noble experiment that didn't work in practice.

OCaml exceptions are notably lightweight — faster than Result types for common cases. They're used for both errors and control flow (e.g., breaking out of recursive searches). OCaml 5's algebraic effects provide a principled alternative.

## Result Types (Rust, Haskell, OCaml)

Return a value encoding success or failure. Rust's Result<T, E> is the modern gold standard: function signatures show which functions can fail, the ? operator provides ergonomic propagation, and the compiler ensures all errors are handled.

Haskell uses Either for errors and Maybe for optionality, composed via monadic operations. The power: error handling composes naturally with other monadic effects. The cost: monads are a prerequisite concept.

Go's error values (esult, err := ...) are conceptually similar but without type system enforcement — nothing prevents ignoring the err return value.

## Error Codes (C, POSIX)

Return special values indicating failure. The oldest approach. Problems: easily ignored, in-band signaling (error values overlap with valid values), no context beyond an integer code. Still standard in: OS APIs, C libraries, FFI boundaries.

Zig modernizes error codes with error unions and compile-time error sets, achieving type safety without the overhead of algebraic types.

## Panic/Crash (Rust, Go, Erlang)

For unrecoverable errors (bugs, invariant violations), terminate the execution unit:
- Rust: panic! unwinds the thread or aborts the process
- Go: panic() + recover() for unrecoverable situations
- Erlang: let the process crash, supervisor restarts it

The key insight: separating recoverable errors (Result/exceptions) from unrecoverable errors (panic) leads to clearer code. Rust enforces this separation in the type system.

## The Modern Consensus

The PL community is converging on: Result types for expected failures (with syntactic sugar like ?), panics for bugs, and algebraic effects as the next evolution (OCaml 5, Koka). Exceptions remain in existing languages but new languages avoid them.
