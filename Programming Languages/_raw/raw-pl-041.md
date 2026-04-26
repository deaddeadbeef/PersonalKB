---
tags: [pl, raw, coroutines, continuations]
up: "[[Sources Index]]"
---

# Raw Note 041 — Coroutines and Continuations

## Coroutines

Coroutines are generalized subroutines that can suspend and resume execution at specific points.

### Stackful vs Stackless Coroutines

**Stackful** (each coroutine has its own call stack):
- **Go goroutines:** Lightweight threads with growable stacks (2KB initial)
- **Lua coroutines:** First-class stackful coroutines
- **Java Virtual Threads (Loom):** Lightweight threads on JVM carrier threads
- **Erlang processes:** Lightweight processes with per-process stacks and heaps

**Stackless** (state machine transformation, no separate stack):
- **Rust async:** Compiler transforms async fn into state machines
- **Python generators/async:** yield-based, frame objects on heap
- **C++ coroutines (C++20):** Compiler-generated state machines with customization points
- **Kotlin coroutines:** CPS-transformed at compile time
- **JavaScript async/generators:** Event loop + microtask queue

### Trade-offs

| Property | Stackful | Stackless |
|----------|----------|-----------|
| Memory | Each coroutine needs a stack | Only state machine size |
| Performance | Context switch cost | Zero-cost (inlined) |
| Flexibility | Can yield from anywhere | Can only yield at suspension points |
| Implementation | Runtime support needed | Compiler transformation |
| Example overhead | Go: ~2KB per goroutine | Rust: as small as the state |

## Continuations

A continuation represents "the rest of the computation" from a given point. First-class continuations allow capturing and invoking them.

### call/cc (call-with-current-continuation)
Scheme's fundamental control flow primitive:
\\\scheme
(call/cc (lambda (k)
  ;; k is the continuation - calling k jumps back to this point
  (k 42)))  ; returns 42 to the caller
\\\

### Delimited Continuations
More structured than call/cc — capture only a portion of the continuation:
- **reset/shift** (Scala, Racket)
- **prompt/control** (Racket)
- Algebraic effects are built on delimited continuations (OCaml 5, Koka)

### CPS Transformation
Continuation-Passing Style transforms code to make continuations explicit:
\\\javascript
// Direct style
function add(a, b) { return a + b; }

// CPS
function addCPS(a, b, k) { k(a + b); }
\\\

CPS is how async/await is implemented internally in many compilers.

## Generators and Iterators

Generators are a restricted form of coroutines:
- **Python:** \yield\ keyword creates generators; \yield from\ for delegation
- **JavaScript:** \unction*\ syntax with \yield\
- **Rust:** No native generators yet (async fn is similar internally)
- **C#:** \yield return\ in IEnumerable methods

## Key Insight
Coroutines, continuations, and async/await are all related: async/await is syntactic sugar over coroutines, which can be implemented via continuations. The spectrum goes from most general (continuations) to most restricted (generators), with each restriction improving usability.

## References
→ [[Sources Index]]
