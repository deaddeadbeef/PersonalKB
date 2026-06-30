---
tags: [programming-languages, module-systems, visibility]
up: "[[Module Systems Overview]]"
tier-coverage: full
confidence: plausible
---
# Visibility and Access Control

## 🎯 Intuition

**The Core Idea:** How a language controls access to internal implementation details determines how well abstractions hold up as codebases grow.

**Analogy:** Access control is like the security badge system in a building — some doors are open to everyone (public), some require a floor badge (package/module-private), some need a department key (protected/friend), and some only open for the room's occupant (private). Languages differ in how many badge levels they offer and whether the locks are real (compiler-enforced) or just polite signs (convention).

**Why It Matters:** Access control ranges from honour-system conventions to compiler-enforced barriers. Stronger access control enables safe refactoring at scale; weaker control enables rapid iteration. Choosing the right level is a core language-design and software-architecture decision.

## ⚙️ Core Mechanics

### Java: Explicit Modifiers

Java provides four visibility levels:
- `public`: Accessible everywhere
- `protected`: Accessible in the same package + subclasses
- (default/package-private): Accessible within the same package
- `private`: Accessible only within the declaring class

Java 9 added module-level visibility: `exports` in `module-info.java` controls which packages are accessible to other modules, adding a coarser-grained visibility layer above packages.

### Rust: Module-Based Visibility

Rust's `pub` keyword controls visibility relative to the module tree:
- `pub`: Public to everyone
- `pub(crate)`: Public within the current crate
- `pub(super)`: Public to the parent module
- `pub(in path)`: Public to a specific ancestor module
- (default): Private to the current module and its children

Rust's approach is path-based rather than hierarchy-based (no `protected`). There's no concept of subclass access because Rust has no inheritance.

### Go: Capitalisation Convention

Go uses the simplest mechanism: names starting with uppercase are exported; lowercase names are package-private. There's no finer-grained control — everything within a package can access everything else in that package. This simplicity is intentional: Go rejects complexity in access control.

### Python: Convention Only

Python has no access control enforcement. Underscore prefix (`_private`) signals "don't use this" but doesn't prevent it. Double underscore (`__mangled`) triggers name mangling but can still be accessed. The philosophy: "we're all consenting adults here." Programmers are trusted to respect conventions.

### C++: Class-Based Access

C++ uses `public`, `protected`, `private` within classes plus `friend` declarations that grant access to specific functions or classes. The `friend` mechanism is unique to C++ and controversial — it creates tight coupling between classes.

### OCaml: Signature-Based Hiding

OCaml uses module signatures (`.mli` files) to control visibility. If a function isn't listed in the signature, it's not accessible outside the module. Types can be made abstract (hidden implementation). This is the most principled approach: the interface is declared separately from the implementation.

### The Expressiveness Spectrum

**Most restrictive:** OCaml (signatures can hide types entirely) → Rust (fine-grained path-based) → Java (four levels + modules) → C++ (class-based + friend) → Go (binary exported/unexported) → **Least restrictive:** Python (convention only)

Languages with stronger access control tend to produce code that's more maintainable at scale but requires more upfront design. Languages with weaker access control are more flexible for rapid iteration.

## 🔬 Deep Dive

### Trade-offs and Historical Context

#### The Practical Impact

Access control's value becomes clear in large codebases:
- **Strong access control (Rust, OCaml):** Refactoring internal implementations is safe — if it compiles, no external code depends on changed internals
- **Medium access control (Java, C++):** Most internal code is protected, but `protected` and `friend` create coupling that can hinder refactoring
- **Weak access control (Python, JavaScript):** Any internal change might break callers who depend on private details. Semantic versioning and discipline substitute for compiler enforcement

#### Compiler-Enforced vs Convention-Based

The fundamental divide is whether access control is enforced at compile time or by social contract. Compiler enforcement (Rust, OCaml, Java) gives absolute guarantees but requires upfront design and can feel restrictive during prototyping. Convention-based control (Python, JavaScript) is frictionless but fragile — private APIs inevitably leak into downstream code, creating invisible coupling that surfaces during upgrades.

#### The `friend` Problem

C++'s `friend` is an escape hatch from class-based encapsulation. It's useful for operator overloading and tightly-coupled pairs (e.g., iterator + container) but it punches through abstraction boundaries. Rust's `pub(in path)` achieves a similar goal more cleanly by scoping visibility to the module tree rather than granting blanket access to a named class.

## 🏋️ Practice

**Exercise 1 — Visibility Audit:** Pick a medium-sized open-source project in a language with strong access control (Rust or Java). Count how many items are `pub`/`public` vs private. Calculate the public-API surface ratio. Then examine a Python project of similar size — how many `_private`-prefixed names are actually accessed from outside their module? What does this tell you about convention-based control in practice?

**Exercise 2 — Encapsulation Refactor:** Write a small Rust library exposing a struct with all `pub` fields. Then refactor it to make fields private and provide accessor methods. Change the internal representation (e.g., from `Vec` to `HashMap`) and verify that no downstream code breaks. Repeat the exercise in Python — how do you signal the same intent without compiler support?

**Exercise 3 — Access-Control Translation:** Implement the same "bank account" module in Java (using `private` fields + `public` methods), Rust (using `pub`/private + `pub(crate)`), Go (using capitalisation), and Python (using underscore conventions). For each, write a test that attempts to access a private field. Document which languages prevent the access at compile time, which prevent it at runtime, and which allow it silently.

## References

- [[Sources Index]]
