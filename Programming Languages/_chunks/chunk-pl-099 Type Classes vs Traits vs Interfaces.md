---
tags: [chunk, programming-languages, type-classes]
source: "[[raw-pl-016]]"
---

# chunk-pl-099 Type Classes vs Traits vs Interfaces

Three approaches to ad-hoc polymorphism (different behavior per type):

**Haskell type classes:**
- Most powerful. Multi-parameter type classes, associated types, type families.
- Open: anyone can add instances. No orphan restriction (can cause coherence issues).
- Higher-kinded types enable abstracting over Functor, Monad, etc.
- Resolved at compile time (dictionary passing or specialization).

**Rust traits:**
- Directly inspired by Haskell. Associated types, default implementations.
- Coherent: orphan rule prevents conflicting implementations.
- Static dispatch (monomorphization) by default; dynamic dispatch (dyn Trait) opt-in.
- No higher-kinded types (GATs provide some power).

**Go interfaces:**
- Structural: satisfied by having the right methods, no declaration needed.
- Simple: no associated types, no default methods, no generics until 1.18.
- Dynamic dispatch always (interface values are fat pointers).
- Consumer-defined: interfaces in the caller's package.

**Java interfaces:**
- Nominal: explicit implements required.
- Default methods (Java 8): partial implementation in interface.
- Limited compared to traits: no associated types, no coherence guarantees across packages.

**Swift protocols:**
- Nominal with associated types and protocol extensions.
- Protocol-oriented programming as primary paradigm.
- No orphan rule (unlike Rust).

Trade-off: more power (Haskell) = more complexity. More simplicity (Go) = less abstraction.
