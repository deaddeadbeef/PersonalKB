---
tags: [pl, chunk, paradigms, immutability]
up: "[[Functional Programming Principles]]"
---

# Immutability Defaults The Quiet Revolution

The default mutability of variables is one of the most impactful language design choices, and the trend is decisively toward immutable-by-default.

## The Mutability Spectrum

| Language | Default | Mutable Syntax | Immutable Syntax |
|----------|---------|---------------|-----------------|
| Rust | Immutable | let mut x = 5 | let x = 5 |
| Kotlin | N/A | ar x = 5 | al x = 5 |

| Swift | N/A | ar x = 5 | let x = 5 |

| Scala | N/A | ar x = 5 | al x = 5 |

| JavaScript | Mutable (var) | let x = 5 | const x = 5 |
| TypeScript | Mutable | let x = 5 | const x = 5 |
| Java | Mutable | int x = 5 | inal int x = 5 |

| Python | Mutable | x = 5 | (no enforcement) |
| Go | Mutable | ar x = 5 / x := 5 | (constants only) |

| C | Mutable | int x = 5 | const int x = 5 |
| Haskell | Immutable | (monadic state) | x = 5 |
| Erlang | Immutable | (impossible) | X = 5 (single assignment) |
| Clojure | Immutable | (atoms, refs) | (def x 5) |

## Why Immutability Wins

### Thread Safety
Immutable data is inherently thread-safe:
`
ust
// Rust: shared immutable references are always safe
let data = vec![1, 2, 3];
let r1 = &data; // OK: multiple immutable borrows
let r2 = &data; // OK: no data race possible
`

### Reasoning
`kotlin
val list = listOf(1, 2, 3)
process(list)
// list is still [1, 2, 3] - guaranteed by val + immutable collection
// With mutable: process might have modified it - must check
`

### Performance (Counterintuitively)
- Immutable data enables sharing without copying
- Persistent data structures (Clojure) reuse structure
- Compiler optimizations (constant folding, memoization)

## Key Insight
The industry has converged on immutable-by-default. Rust, Kotlin, Swift, and Scala all make immutability the path of least resistance. Even JavaScript's const is now recommended over let by most style guides. The reasoning: immutability eliminates entire categories of bugs (mutation-related, concurrency-related) with minimal cost.

## References
→ [[Sources Index]]
