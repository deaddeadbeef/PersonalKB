---
tags: [pl, queries, roadmap]
up: "[[Programming Languages]]"
---

# QnA System Roadmap

## Purpose
This roadmap defines the question-answer pairs that drive active recall across the Programming Languages wiki. Each question maps to specific wiki pages and chunks.

## Tier 1 — Foundational Questions

### Type Systems
1. **Q:** What is the fundamental trade-off between static and dynamic typing?
   **A:** Static typing catches errors at compile time but requires more upfront annotation; dynamic typing enables rapid prototyping but defers errors to runtime. Modern languages blur this with type inference (Rust, OCaml) and gradual typing (TypeScript, Python).
   **Sources:** [[Static vs Dynamic Typing]], [[chunk-pl-001 Static vs Dynamic Typing Trade-offs]]

2. **Q:** How does Hindley-Milner type inference work?
   **A:** HM uses constraint-based unification: it assigns type variables, collects constraints from usage, then solves them. It can infer the most general (principal) type without annotations. Used by OCaml, Haskell, Rust (extended), and ML family.
   **Sources:** [[Type Inference and Hindley-Milner]], [[chunk-pl-002 Hindley-Milner Type Inference]]

3. **Q:** What is the difference between nominal and structural typing?
   **A:** Nominal: types are distinct if they have different names (Java, Rust, C#). Structural: types are compatible if they have the same shape (Go interfaces, TypeScript, OCaml modules). Trade-off: nominal prevents accidental compatibility; structural enables decoupled design.
   **Sources:** [[Programming Languages/Type Systems/Nominal vs Structural Typing|Nominal vs Structural Typing]], [[chunk-pl-003 Nominal vs Structural Typing]]

### Memory Management
4. **Q:** How does Rust prevent use-after-free without garbage collection?
   **A:** Ownership rules: each value has exactly one owner; when the owner goes out of scope, the value is dropped. Borrowing allows temporary references (one mutable XOR many immutable). The borrow checker enforces these at compile time.
   **Sources:** [[Ownership and Borrowing]], [[chunk-pl-007 Ownership and Borrowing in Rust]]

5. **Q:** Compare the 3 main GC strategies: tracing, reference counting, and generational.
   **A:** Tracing (mark-sweep): finds all reachable objects from roots, frees the rest. Reference counting (Swift ARC, Python): tracks reference counts per object, frees at zero. Generational: divides heap by age, collects young gen frequently (most objects die young). Most modern GCs combine generational + tracing.
   **Sources:** [[Garbage Collection Strategies]], [[chunk-pl-006 Garbage Collection Strategies Compared]]

### Concurrency
6. **Q:** What are the 4 main concurrency models?
   **A:** (1) Threads + locks (C, C++, Java), (2) CSP/channels (Go, Clojure core.async), (3) Actor model (Erlang, Elixir, Swift actors), (4) Async/await (JS, Python, Rust, C#). Each trades off between explicitness, safety, and performance.
   **Sources:** [[Concurrency Models Overview]], [[chunk-pl-009 Threads Locks and Data Race Prevention]]

7. **Q:** How does Go's concurrency model differ from Erlang's?
   **A:** Go uses CSP (goroutines + channels) with shared memory possible. Erlang uses actors (processes + messages) with NO shared memory. Go's race detector catches bugs at runtime; Erlang's isolation prevents them by design. Erlang sacrifices raw performance for fault tolerance.
   **Sources:** [[Programming Languages/Concurrency Models/CSP and Channel-Based Concurrency|CSP and Channel-Based Concurrency]], [[The Actor Model]], [[chunk-pl-010 CSP Channels and the Actor Model]]

## Tier 2 — Design Philosophy Questions

8. **Q:** Why did Go deliberately ship without generics for 12 years?
   **A:** Go prioritized simplicity and fast compilation. The designers believed generics would complicate the language and slow the compiler. They waited until they found an approach (type parameters with constraints) that preserved Go's simplicity goals. Added in Go 1.18 (2022).
   **Sources:** [[Go — Language Profile]], [[chunk-pl-029 Go Simplicity and Goroutine Concurrency]]

9. **Q:** What makes Rust's error handling a "design triumph"?
   **A:** Rust separates recoverable errors (Result<T,E>) from unrecoverable ones (panic!). The ? operator enables concise error propagation without exceptions' hidden control flow. Combined with pattern matching, errors are always explicit and compiler-enforced.
   **Sources:** [[Result and Option Types]], [[chunk-pl-012 Result Types and the Question Mark Operator]]

10. **Q:** How do languages balance safety vs performance?
    **A:** Spectrum: C (trust programmer, max perf) → C++ (zero-cost abstractions) → Rust (safe by default, unsafe escape hatch) → Go/Java (GC safety, some perf cost) → Python (max safety/convenience, significant perf cost). Rust's innovation: proving safety without runtime cost.
    **Sources:** [[chunk-pl-025 Safety vs Performance Trade-off Spectrum]], [[chunk-pl-070 Trust vs Protection in Language Philosophy]]

## Tier 3 — Cross-Cutting Synthesis Questions

11. **Q:** Are programming languages converging? What features appear in nearly all modern languages?
    **A:** Yes — pattern matching, algebraic data types, async/await, closures/lambdas, generics, null safety, and first-class functions are appearing across paradigm boundaries. Even Java added records, sealed classes, and pattern matching. The convergence is toward "multi-paradigm with strong types."
    **Sources:** [[chunk-pl-064 Multi-Paradigm Reality of Modern Languages]], [[chunk-pl-120 Language Convergence The Great Merge]]

12. **Q:** How does a language's memory model constrain its concurrency model?
    **A:** GC languages (Java, Go) can share heap objects freely but need synchronization. Rust's ownership prevents data races at compile time. Erlang's per-process heaps eliminate shared state entirely. The memory model fundamentally shapes what concurrency abstractions are safe and efficient.
    **Sources:** [[Memory Management Overview]], [[Concurrency Models Overview]]

## How to Use This Roadmap
1. **Active recall:** Cover the answer, try to answer from memory
2. **Spaced repetition:** Review Tier 1 weekly, Tier 2 biweekly, Tier 3 monthly
3. **Source diving:** Follow the links to deepen understanding
4. **Connection building:** After answering, think of 2 related questions

## References
→ [[Sources Index]]
