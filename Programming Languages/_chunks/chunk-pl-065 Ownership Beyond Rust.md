---
tags: [chunk, programming-languages, ownership-beyond-rust]
source: "[[raw-pl-025]]"
---

# chunk-pl-065 Ownership Beyond Rust

Rust proved compile-time memory safety is practical. Other languages exploring similar ideas:

**Swift ownership annotations:** Borrowing and consuming parameters. Moves for unique ownership transfer. Not as comprehensive as Rust's system but brings ownership concepts to a GC-free (ARC) language.

**Mojo:** Python-like syntax with ownership system. Designed for AI/ML workloads. Aims to combine Python's ergonomics with Rust-level performance. Owned values, borrowed references, lifetime checking.

**C++ lifetime annotations:** Proposed extensions for tracking pointer lifetimes. Not yet standardized. Herb Sutter's "lifetime safety" proposal.

**Linear types (Haskell extension):** Values used exactly once. Ensures resources (file handles, connections) are properly consumed. Rust's ownership is a restricted form of linear types.

**Dependent types (Idris, Agda, Lean):** Types depending on values. Array index proven in-bounds at compile time. Vector length in the type. The most powerful but most complex approach.

The trend: compile-time memory and resource safety is too valuable to be Rust-exclusive. Languages are finding ways to add ownership-like guarantees at varying levels of strictness.
