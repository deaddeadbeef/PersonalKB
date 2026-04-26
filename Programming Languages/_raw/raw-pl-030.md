---
tags: [raw, programming-languages, philosophy]
source: "Various language design talks, papers, and community discussions"
created: 2025-07-25
---

# raw-pl-030: Programming Language Design Philosophies

## Explicit vs Implicit

The most fundamental design axis:
- **Explicit (Go, Zig, Rust):** The code says what it does. No hidden behavior. More verbose but easier to reason about.
- **Implicit (Ruby, Python, C++):** The language does things for you. Less verbose but behavior can be surprising.

Go is maximally explicit: no inheritance (no hidden method resolution), no exceptions (error handling is visible), no operator overloading (+ always means addition). Ruby is maximally implicit: method_missing, open classes, convention-over-configuration (Rails).

## Correctness vs Velocity

Languages optimize for different development phases:
- **Correctness-first (Rust, Haskell, OCaml):** Spend more time writing code that's correct from the start. Slower initial development but fewer bugs in production.
- **Velocity-first (Python, Ruby, JavaScript):** Write code quickly, iterate rapidly, fix bugs as they appear. Faster initial development but more runtime errors.

Neither is universally better. Prototypes benefit from velocity; payment systems benefit from correctness.

## Batteries-Included vs Minimal Core

**Batteries-included (Python, Go, Java):** Large standard library covering common needs. Reduced dependency on third-party packages. Slower language evolution (the stdlib is forever).

**Minimal core (Rust, Haskell, Zig):** Small standard library. Rich ecosystem of community packages. Faster evolution (packages can break backward compatibility). Risk: package quality varies, ecosystem fragmentation.

## Opinionated vs Flexible

**Opinionated (Go, Elm, Python):** One way to do things. gofmt, go vet, single module system. Reduces bikeshedding, improves readability across projects. Can feel restrictive.

**Flexible (C++, Lisp, Scala):** Many ways to do things. Multiple paradigms, styles, and patterns. Powerful for experts. Codebases can look completely different depending on the author.

## Trust the Programmer vs Protect the Programmer

**Trust (C, Zig):** The programmer knows best. Minimal guardrails. Maximum performance and flexibility. Bugs are the programmer's responsibility.

**Protect (Rust, Haskell, Java):** The compiler catches mistakes. The type system prevents invalid states. The cost: learning curve, compilation time, sometimes fighting the compiler.

Rust occupies a unique position: maximum protection with maximum performance. The price is the steepest learning curve of any mainstream language.

## The Zen of Language Design

Every language design is a set of trade-offs frozen in time. No language makes every trade-off correctly for every domain. The best programmers understand which trade-offs their language makes and choose the language whose trade-offs align with their problem domain.
