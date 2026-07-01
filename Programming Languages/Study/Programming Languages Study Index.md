---
tags: [pl, study, index]
up: "[[Programming Languages]]"
confidence: verified
freshness: stable
tier-coverage: [practice]
---
# Programming Languages Study Index

## Start Here By Goal

Use this page to compare design choices. The drills are useful after you can say what trade-off a language feature is making.

| Goal | Start with | Then use | Proof you should leave behind |
|---|---|---|---|
| Read programming languages as a book | [[Programming Languages/Programming Languages Book Reading Spine|Programming Languages Book Reading Spine]] | [[Programming Languages/Programming Paradigms/Programming Paradigms Overview|Programming Paradigms Overview]], [[Programming Languages/Language Genealogy/Language Genealogy Overview|Language Genealogy Overview]] | A genealogy-to-design map for one language family |
| Compare languages for a project | [[Cheatsheet - PL Design Decisions Quick Reference]] | [[Programming Languages/Type Systems/Type Systems Overview|Type Systems Overview]], [[Programming Languages/Memory Management/Memory Management Overview|Memory Management Overview]], [[Programming Languages/Concurrency Models/Concurrency Models Overview|Concurrency Models Overview]] | A comparison row with type, memory, concurrency, runtime, package, and error-handling constraints |
| Understand runtime behavior | [[Programming Languages/Compilation and Runtime/Compilation and Runtime Overview|Compilation and Runtime Overview]] | [[Programming Languages/Memory Management/Memory Management Overview|Memory Management Overview]], [[Programming Languages/Module Systems/Module Systems Overview|Module Systems Overview]] | A request or program lifecycle from source text to runtime behavior |
| Design a toy language | [[Programming Languages/Type Systems/Type Systems Overview|Type Systems Overview]] | [[Programming Languages/Error Handling/Error Handling Overview|Error Handling Overview]], [[Programming Languages/Metaprogramming/Metaprogramming Overview|Metaprogramming Overview]] | A language design note with one accepted trade-off and one rejected trade-off |

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
2. [[Programming Languages/Memory Management/Memory Management Overview|Memory Management Overview]] → GC Strategies → Ownership
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
→ [[Programming Languages/Sources/Sources Index|Sources Index]]
