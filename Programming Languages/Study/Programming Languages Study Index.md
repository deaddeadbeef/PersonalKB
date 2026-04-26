---
tags: [pl, study, index]
up: "[[Programming Languages]]"
---

# Programming Languages Study Index

## Review Drills

| Drill | Focus Areas |
|-------|-------------|
| [[Review Drill - Type Systems and Inference]] | Static/dynamic, HM inference, generics, gradual typing |
| [[Review Drill - Memory Management Models]] | Manual, GC, ownership, ARC, value/reference types |
| [[Review Drill - Concurrency and Error Handling]] | Threads, CSP, actors, async, exceptions, Result types |
| [[Review Drill - Language Design Philosophy]] | Explicit/implicit, trade-offs, convergence, trust |
| [[Review Drill - Compilation and Metaprogramming]] | AOT/JIT, VMs, macros, reflection, comptime |

## Cheatsheets

| Sheet | Contents |
|-------|----------|
| [[Cheatsheet - PL Design Decisions Quick Reference]] | Type systems, memory, concurrency, errors — all 15 languages side by side |

## Study Approach

### Phase 1 — Dimensions (Weeks 1-2)
Work through each dimension hub, reading the overview then deep-diving into 2-3 pages:
1. [[Type Systems Overview]] → Static vs Dynamic → Generics
2. [[Memory Management Overview]] → GC Strategies → Ownership
3. [[Concurrency Models Overview]] → CSP → Actor Model → Async
4. [[Error Handling Overview]] → Result Types → Exceptions

### Phase 2 — Cross-Cutting (Weeks 3-4)
Use review drills to connect dimensions:
- How does a language's type system affect its error handling?
- How does memory model constrain concurrency options?
- Why do some paradigms pair naturally with certain type systems?

### Phase 3 — Language Profiles (Weeks 5-6)
Read 2-3 language profiles per day, using the cheatsheet to compare:
- Start with languages you know (Python, JS) and trace their design choices
- Then explore unfamiliar paradigms (Haskell, Erlang, OCaml)
- End with systems languages (C, C++, Rust, Zig) to see the safety spectrum

### Phase 4 — Synthesis (Week 7+)
- Review raw notes for deeper insights
- Use chunks for spaced repetition
- Design your own toy language — what trade-offs would you make?

## References
→ [[Sources Index]]
