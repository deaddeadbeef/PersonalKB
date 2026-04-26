---
tags: [chunk, programming-languages, paradigms]
source: "[[raw-pl-017]]"
---

# chunk-pl-015 OOP Evolution From Hierarchies to Traits

The history of OOP in three acts:

**Act 1 — Smalltalk vision:** Everything is an object. Objects communicate via messages. Late binding. The system is live.

**Act 2 — Industrial OOP:** Java/C++ class hierarchies. Design patterns (Gang of Four). AbstractFactoryBean problem. Fragile base class problem. "Kingdom of nouns."

**Act 3 — Trait/interface revolution:** Modern languages converge on traits/protocols/interfaces as primary abstraction:
- **Rust traits:** No inheritance. impl Trait for Type.
- **Go interfaces:** Structural satisfaction. No implements keyword.
- **Swift protocols:** Protocol-oriented programming with extensions.
- **Haskell type classes:** Ad-hoc polymorphism.
- **OCaml module signatures:** Strongest encapsulation via abstract types.

The consensus: "prefer composition over inheritance." Inheritance creates coupling; traits/interfaces provide polymorphism without hierarchy. The future of polymorphism is trait-based, not hierarchy-based.
