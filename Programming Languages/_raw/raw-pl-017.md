---
tags: [raw, programming-languages, oop-evolution]
source: "Design Patterns (Gamma et al.), A Theory of Objects (Abadi & Cardelli)"
created: 2025-07-25
---

# raw-pl-017: OOP Evolution — From Smalltalk to Traits

## The Original Vision (Smalltalk)

Alan Kay's Smalltalk: everything is an object communicating via messages. Objects decide how to respond. Late binding everywhere. The system is live — you modify running objects. This vision emphasized flexibility and interactivity over static safety.

## Industrial OOP (Java, C#)

OOP became: classes as blueprints, inheritance hierarchies, design patterns. Gang of Four patterns (Factory, Observer, Strategy, Visitor) became standard vocabulary. The AbstractFactoryBean problem: deep hierarchies, excessive abstraction, and the "kingdom of nouns."

Java forced everything into classes — even static utility functions need a class wrapper. This led to verbose, over-engineered designs. Kotlin, Scala, and modern Java (records, sealed classes) are corrections.

## Composition Over Inheritance

The most important OOP lesson: inheritance creates tight coupling. Changing a base class can break all subclasses (fragile base class problem). Modern consensus: use inheritance sparingly; prefer composition, delegation, and interfaces.

**Go:** No inheritance at all. Struct embedding provides code reuse. Interfaces for polymorphism. "Go is about composition, not inheritance."

**Rust:** No inheritance. Traits provide behavior. Trait implementations can have default methods. Types compose via struct fields and trait bounds.

**Kotlin/Swift:** Have inheritance but encourage protocols/interfaces. Extension functions add behavior without inheritance.

## Prototype-Based OOP (JavaScript, Self)

Self (1986): objects inherit directly from other objects (prototypes). No classes — clone existing objects and modify. JavaScript adopted this model, then added class syntax (ES2015) as sugar over prototypes. The philosophical difference: class-based asks "what category is this?"; prototype-based asks "what is this similar to?"

## The Trait/Protocol/Interface Revolution

Modern languages converge on traits/protocols/interfaces as the primary abstraction:
- **Rust traits:** Define behavior. Types opt in via impl Trait for Type. No inheritance.
- **Swift protocols:** Define behavior + associated types. Protocol extensions provide defaults.
- **Go interfaces:** Structural — satisfy by having the right methods. No explicit declaration.
- **Haskell type classes:** Define behavior. Instances for each type. Multi-parameter type classes.
- **OCaml module signatures:** Define module interfaces. Functors parameterize over them.

This convergence suggests: the future of polymorphism is trait-based, not hierarchy-based.
