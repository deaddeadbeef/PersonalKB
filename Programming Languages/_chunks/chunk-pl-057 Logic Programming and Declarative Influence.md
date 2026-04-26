---
tags: [chunk, programming-languages, logic]
source: "[[raw-pl-005]]"
---

# chunk-pl-057 Logic Programming and Declarative Influence

**Prolog (1972):** Programs are facts + rules + queries. Execution uses unification (pattern matching on steroids) and backtracking (systematic search). Declare what relationships hold; the runtime finds answers.

Prolog excels at: symbolic AI, NLP, expert systems, constraint satisfaction, theorem proving. Struggles with: numerical computation, systems programming.

**Datalog:** Restricted Prolog for databases. Always terminates. Used in program analysis (Facebook's Doop), access control, network config. Experiencing a renaissance.

**Logic programming's influence on mainstream languages:**
- SQL: declarative queries over tables (what, not how)
- Type inference: uses unification (same algorithm as Prolog)
- Pattern matching in ML/Haskell/Rust: restricted form of unification
- GraphQL: declarative API queries
- Terraform: declarative infrastructure (desired state, not steps)

Why niche: performance unpredictability, debugging difficulty, paradigm mismatch with imperative thinking, limited ecosystem. But the declarative philosophy increasingly influences mainstream through query languages and constraint systems.
