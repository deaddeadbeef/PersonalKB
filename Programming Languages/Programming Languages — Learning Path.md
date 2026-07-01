---
tags: [pl, learning-path]
up: "[[Programming Languages/Programming Languages]]"
confidence: verified
freshness: stable
tier-coverage: [core, practice]
---
# Programming Languages — Learning Path

> A guided, progressive tour through programming-language design and philosophy. Four passes, each building on the last.

## Where This Fits

| Need | Use |
|---|---|
| Read programming languages like a book | [[Programming Languages/Programming Languages Book Reading Spine|Programming Languages Book Reading Spine]] |
| Follow a pass-based curriculum | This learning path |
| Compare languages or design a toy language | [[Programming Languages/Study/Programming Languages Study Index|Programming Languages Study Index]] |
| Verify theory, manual, implementation, or ecosystem claims | [[Programming Languages/Sources/Sources Index|Programming Languages Sources Index]] |

Use this path when you want staged exposure to the design dimensions. Use the book spine for narrative reading, and use the study index when you need a comparison row or language-design decision.

## How to Use This Path

| Pass | Focus | Read | Time |
|------|-------|------|------|
| 1 — Intuition | Build mental map | 🎯 sections only | ~2 hrs |
| 2 — Core | Understand mechanics | ⚙️ sections + Warm-Up | ~8 hrs |
| 3 — Deep Dive | Master details | 🔬 sections (selective) | ~15 hrs |
| 4 — Practice | Build skill | 🏋️ sections + drills | Ongoing |

---

## Pass 1 — Intuition (~2 hours)

Read ONLY the 🎯 Intuition section of each page. Build a broad mental map of how languages differ and why.

### Language Genealogy
1. [[Language Genealogy Overview]] — how languages evolve and influence each other
2. [[PL History and Eras]] — from Fortran to modern multi-paradigm languages
3. [[Language Family Trees]] — visual lineage of major language families
4. [[Influence Chains and Cross-Pollination]] — how ideas flow between languages
5. [[The Rise of Multi-Paradigm Languages]] — why modern languages mix paradigms

### Programming Paradigms
6. [[Programming Paradigms Overview]] — the paradigms hub
7. [[Imperative and Procedural Programming]] — sequential state mutation
8. [[Object-Oriented Programming Philosophies]] — encapsulation, inheritance, polymorphism
9. [[Functional Programming Principles]] — immutability, composition, higher-order functions
10. [[Prototype vs Class-Based OOP]] — JavaScript-style vs Java-style objects
11. [[Logic and Constraint Programming]] — declarative rule-based computation

### Type Systems
12. [[Type Systems Overview]] — the type-systems hub
13. [[Static vs Dynamic Typing]] — compile-time vs runtime type checking
14. [[Type Inference and Hindley-Milner]] — when the compiler figures out types for you
15. [[Generics and Parametric Polymorphism]] — writing code that works for any type
16. [[Nominal vs Structural Typing]] — name-based vs shape-based compatibility
17. [[Gradual and Optional Typing]] — adding types incrementally (TypeScript, mypy)

### Memory Management
18. [[Programming Languages/Memory Management/Memory Management Overview|Memory Management Overview]] — the memory-management hub
19. [[Manual Memory Management]] — malloc/free, the C way
20. [[Garbage Collection Strategies]] — mark-sweep, generational, concurrent GC
21. [[Ownership and Borrowing]] — Rust's compile-time memory safety
22. [[Reference Counting]] — Swift ARC, Python refcounting
23. [[Value Types vs Reference Types]] — stack vs heap, copy vs share semantics

### Error Handling
24. [[Error Handling Overview]] — the error-handling hub
25. [[Exception-Based Error Handling]] — try/catch/finally (Java, Python, C++)
26. [[Result and Option Types]] — Rust Result/Option, Haskell Maybe/Either
27. [[Error Codes and Sentinel Values]] — C-style error returns, Go multi-return
28. [[Panic and Recovery Mechanisms]] — Go panic/recover, Rust panic
29. [[Effect Systems and Checked Exceptions]] — algebraic effects, Java checked exceptions

### Concurrency Models
30. [[Concurrency Models Overview]] — the concurrency hub
31. [[Threads and Locks]] — OS threads, mutexes, the shared-memory model
32. [[CSP and Channel-Based Concurrency]] — Go goroutines, channels
33. [[The Actor Model]] — Erlang/Elixir processes, Akka actors
34. [[Async-Await and Event Loops]] — JavaScript, Python, Rust async
35. [[Software Transactional Memory]] — Haskell STM, composable transactions

### Compilation and Runtime
36. [[Compilation and Runtime Overview]] — the compilation hub
37. [[Compilation Pipeline Stages]] — lexing, parsing, type-checking, codegen
38. [[AOT vs JIT Compilation]] — ahead-of-time vs just-in-time trade-offs
39. [[Virtual Machines and Bytecode]] — JVM, CLR, BEAM, CPython bytecode
40. [[Linking and Loading]] — static/dynamic linking, symbol resolution
41. [[Runtime Systems Compared]] — GC runtimes, minimal runtimes, no runtime

### Metaprogramming
42. [[Metaprogramming Overview]] — the metaprogramming hub
43. [[Macro Systems Compared]] — Lisp macros, Rust proc macros, C preprocessor
44. [[Reflection and Introspection]] — Java reflection, Python inspect, Go reflect
45. [[Template Metaprogramming]] — C++ templates, D templates
46. [[Compile-Time Computation]] — constexpr, comptime, const generics
47. [[Decorators Annotations and Attributes]] — Python decorators, Java annotations

### Module Systems
48. [[Module Systems Overview]] — the module-systems hub
49. [[Package and Namespace Systems]] — Java packages, Python modules, Go packages
50. [[Import and Export Mechanisms]] — ES modules, Python imports, Rust use
51. [[Visibility and Access Control]] — public/private/internal across languages
52. [[ML Module System and Functors]] — OCaml modules, signatures, functors
53. [[Dependency Management Approaches]] — npm, cargo, pip, Maven

### Language Profiles
54. [[Language Profiles Overview]] — all 16 profiles at a glance
55. [[C — Language Profile]] — the systems lingua franca
56. [[C++ — Language Profile]] — zero-cost abstractions, multi-paradigm
57. [[Java — Language Profile]] — JVM, OOP, enterprise ecosystem
58. [[Python — Language Profile]] — readability, scientific computing, scripting
59. [[JavaScript and TypeScript — Language Profile]] — the web platform language
60. [[Go — Language Profile]] — simplicity, goroutines, fast compilation
61. [[Rust — Language Profile]] — ownership, safety, systems programming
62. [[OCaml — Language Profile]] — ML family, pattern matching, type inference
63. [[Haskell — Language Profile]] — purity, laziness, type-class polymorphism
64. [[Erlang and Elixir — Language Profile]] — BEAM VM, fault tolerance, actors
65. [[Lisp and Scheme — Language Profile]] — homoiconicity, macros, REPL-driven
66. [[Swift — Language Profile]] — Apple ecosystem, ARC, protocol-oriented
67. [[Kotlin — Language Profile]] — JVM modern, null safety, coroutines
68. [[Ruby — Language Profile]] — developer happiness, metaprogramming, DSLs
69. [[Zig — Language Profile]] — explicit allocation, comptime, no hidden control flow
70. [[Historical Languages Overview]] — Fortran, COBOL, Smalltalk, ML, Prolog

---

## Pass 2 — Core Mechanics (~8 hours)

Re-read each page's ⚙️ Core Mechanics and 🏋️ Warm-Up sections. Understand *how* each design dimension works across languages.

### Suggested order
Follow the same sequence as Pass 1. Spend extra time on:
- **Type systems** — compare static (Rust, Haskell) vs dynamic (Python, Ruby) trade-offs
- **Memory management** — understand GC roots, Rust borrow checker, ARC cycles
- **Concurrency** — trace a goroutine through CSP vs an Erlang actor message
- **Compilation pipeline** — follow source code through lexer → parser → IR → codegen
- **Error handling** — compare exception unwinding vs Result propagation

### Checkpoints
After this pass you should be able to:
- [ ] Classify any language by its type system, memory model, and concurrency approach
- [ ] Explain trade-offs between GC, ownership, and manual memory management
- [ ] Compare exception-based vs Result-based error handling
- [ ] Describe the compilation pipeline from source to executable
- [ ] Explain why Go chose CSP while Erlang chose actors

---

## Pass 3 — Deep Dive (selective, ~15 hours)

Read the 🔬 Deep Dive sections for dimensions you want to master.

### Track A — Type Theory
- [[Type Inference and Hindley-Milner]] — Algorithm W, let-polymorphism
- [[Generics and Parametric Polymorphism]] — type erasure vs monomorphization
- [[Nominal vs Structural Typing]] — Go interfaces, TypeScript structural types
- [[Gradual and Optional Typing]] — soundness gaps, migration strategies

### Track B — Memory & Safety
- [[Ownership and Borrowing]] — lifetime annotations, NLL, borrow checker internals
- [[Garbage Collection Strategies]] — tri-color marking, generational hypothesis
- [[Manual Memory Management]] — arena allocation, RAII, smart pointers
- [[Value Types vs Reference Types]] — Swift value semantics, C# struct vs class

### Track C — Concurrency Deep Dive
- [[Threads and Locks]] — lock-free data structures, memory ordering
- [[Async-Await and Event Loops]] — Rust Pin/Future, JavaScript microtasks
- [[The Actor Model]] — supervision trees, let-it-crash philosophy
- [[Software Transactional Memory]] — optimistic concurrency, retry semantics

### Track D — Language Implementation
- [[Compilation Pipeline Stages]] — SSA form, optimization passes
- [[Virtual Machines and Bytecode]] — JIT tiers, deoptimization
- [[Macro Systems Compared]] — hygiene, procedural macros, quasi-quotation
- [[Runtime Systems Compared]] — Go scheduler, BEAM preemption, V8 isolates

---

## Pass 4 — Practice (ongoing)

Build active-recall skill through drills and comparative exercises.

### Drills
- [[Programming Languages Study Index]] — full study plan and drills
- [[Cheatsheet - PL Design Decisions Quick Reference]] — all languages side by side

### Comparative Exercises
1. **Implement a linked list** in C (manual), Rust (ownership), and Python (GC) — compare ergonomics and safety
2. **Solve producer-consumer** using threads+locks (Java), channels (Go), and actors (Elixir)
3. **Write a generic sort** in Java (type erasure), Rust (monomorphization), and Python (duck typing)
4. **Handle errors** for file I/O in Go (error codes), Rust (Result), Java (exceptions), and Haskell (Either)
5. **Build a small DSL** using Lisp macros, Rust proc macros, and Ruby metaprogramming

### Capstone
Pick three languages from different paradigms and implement the same small project (e.g., a URL shortener, a Markdown parser, or a task queue). Compare the experience across all dimensions studied.

## References

- [[Programming Languages/Programming Languages]]
- [[Programming Languages/Sources/Sources Index]]
