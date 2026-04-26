---
tags: [raw, programming-languages, design-philosophy]
source: "On the Design of Programming Languages, various PL research papers"
created: 2025-07-25
---

# raw-pl-013: Language Design Trade-offs

## Safety vs Performance

The fundamental tension. More safety (bounds checking, GC, borrow checking) costs either runtime performance or compilation time. Languages position themselves on this spectrum:

- C/Zig: Maximum performance, minimal safety checks
- Rust: Maximum safety AND performance (at the cost of compilation time and learning curve)
- Go/Java/OCaml: High safety with moderate performance (GC overhead)
- Python/Ruby: Maximum safety and convenience with significant performance cost

Rust proved you can have both safety and performance — but the borrow checker's learning curve is the price.

## Simplicity vs Expressiveness

Simple languages (Go, C) are easy to learn and read but require more code for complex patterns. Expressive languages (Haskell, Rust, C++) enable concise, powerful abstractions but have steep learning curves and complex interactions between features.

Go chose radical simplicity: no generics (until 1.18), no exceptions, no inheritance. The result: every Go programmer can read every Go codebase, but some patterns require verbose boilerplate.

Haskell chose maximum expressiveness: type classes, monads, lazy evaluation, higher-kinded types. The result: expert Haskell code is incredibly concise, but the learning curve is years, not weeks.

## Consistency vs Pragmatism

Consistent languages apply their design principles uniformly (Smalltalk: everything is an object, Haskell: everything is pure). Pragmatic languages make exceptions for practical reasons (Java: primitives aren't objects, OCaml: allows mutation despite being functional-first).

Pragmatic exceptions usually reflect performance requirements (Java primitives avoid heap allocation) or real-world usage patterns (OCaml mutation for performance-critical inner loops).

## Compilation Speed vs Optimization

Fast compilation enables rapid development. Heavy optimization enables peak performance. You usually can't have both:
- Go: Compiles in seconds. Moderate optimization. Developer experience wins.
- Rust: Compiles in minutes. Heavy LLVM optimization. Performance wins.
- C++: Compiles in minutes to hours. Maximum optimization. Legacy constraints.
- Zig: Fast compilation with its own backend. LLVM for release builds.

## Static vs Dynamic — The Eternal Debate

Static types catch errors early, enable tooling, document code. Dynamic types allow rapid prototyping, flexible metaprogramming, simpler code.

The trend: gradual typing (TypeScript, Python type hints, Ruby Sorbet) lets developers start dynamic and add types where they matter. The future may be: write prototypes dynamically, production code statically, in the same language.
