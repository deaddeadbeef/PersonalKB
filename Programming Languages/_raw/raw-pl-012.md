---
tags: [raw, programming-languages, language-profiles]
source: "Various language documentation, design papers"
created: 2025-07-25
---

# raw-pl-012: Functional Languages — Haskell, OCaml, Erlang/Elixir, Lisp

## Haskell (1990) — Purity Enforced

Pure functional: all functions have no side effects. IO monad sequences effects in a pure framework. Lazy evaluation by default. Type classes for ad-hoc polymorphism. GHC is one of the most sophisticated compilers.

Haskell proved purity is practical. Its ideas spread: Rust traits (from type classes), Swift protocols, Kotlin sealed classes. STM (Software Transactional Memory) is composable, deadlock-free concurrency.

Challenges: laziness causes space leaks, monad transformers are complex, string types are confusing, steep learning curve, limited industry adoption.

## OCaml (1996) — Pragmatic Rigor

ML lineage: Hindley-Milner type inference, algebraic data types, pattern matching. Functional-first but allows imperative code (mutable refs, loops). Module system with functors is the most powerful in any practical language.

OCaml 5: multicore support + algebraic effects (subsume exceptions, async/await, generators into one mechanism). Used at: Jane Street (trading), Facebook (Infer), Tezos (blockchain).

Fast compilation, excellent GC for allocation-heavy code, small runtime. The compiler writer's language — Rust's original compiler was written in OCaml.

## Erlang/Elixir — Fault-Tolerant Concurrency

Erlang (1986): designed for telecom switches. BEAM VM: millions of lightweight processes, per-process GC, hot code swapping. "Let it crash" philosophy: processes crash, supervisors restart them. Message passing only — no shared memory.

Elixir (2011): modern syntax + macros on BEAM. Phoenix framework for web. LiveView for real-time UI. WhatsApp served 2B users on Erlang. Discord uses Elixir.

## Lisp Family — Code as Data

Lisp (1958) invented: GC, dynamic typing, higher-order functions, REPL, macros. Homoiconicity: code is data (lists), enabling macros that transform code as easily as functions transform data.

Common Lisp: feature-rich, CLOS (most flexible OOP), conditions/restarts. Scheme: minimal, hygienic macros, lexical scope (influenced JavaScript). Clojure: JVM-hosted, immutable persistent data structures, STM. Racket: language-building platform.
