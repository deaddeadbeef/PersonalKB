---
tags: [programming-languages, type-systems, static-dynamic]
up: "[[Type Systems Overview]]"
tier-coverage: full
---

# Static vs Dynamic Typing

## 🎯 Intuition

**The Core Idea:** The choice between static and dynamic typing is a deep design decision about whether more guarantees should come before execution or during execution.

**Analogy:** Static typing is like checking a building's blueprint before construction starts; dynamic typing is like inspecting the building while people are already moving through it.

**Why It Matters:** This debate shapes what the compiler is expected to do, how flexible programs feel while being written, how much structure large teams rely on, and what kinds of errors are caught before runtime versus during runtime.

## ⚙️ Core Mechanics

### The Static Typing Philosophy

**Core belief:** Types are documentation that the compiler can verify. If the program compiles, entire categories of bugs are eliminated.

**Haskell** represents the purest static typing philosophy: "If it compiles, it probably works." Haskell's type system is so expressive that types encode business logic — invalid states become unrepresentable. The compiler serves as a proof assistant.

**Rust** uses static typing for memory safety: the borrow checker is essentially a type-level proof that references are valid. Types carry ownership and lifetime information invisible in other languages.

**OCaml** demonstrates that static typing need not be verbose. Hindley-Milner inference means most types are never written explicitly, yet the compiler knows every type in the program. OCaml programmers get the safety of static typing with the conciseness of dynamic typing.

**Java and C#** represent industrial static typing: explicit type declarations serve as documentation for large teams. The verbosity is seen as a feature — code is self-documenting and IDE-navigable.

**Go** takes a minimalist approach to static typing: no generics until 1.18 (2022), no algebraic data types, no type classes. Types are simple and explicit. The philosophy is that most type system complexity doesn't pay for itself in practice.

### The Dynamic Typing Philosophy

**Core belief:** Types are a constraint that slows down development. The programmer knows what the data is; the computer should figure it out.

**Python** embodies "duck typing" — if it walks like a duck and quacks like a duck, it's a duck. Objects are defined by their behavior, not their declared type. This enables extreme flexibility and rapid prototyping.

**Ruby** takes dynamic typing further into the "programmer happiness" philosophy. Types should never get in the way of expressing intent. Method dispatch is always dynamic, enabling powerful metaprogramming.

**JavaScript** demonstrates both the power and peril of dynamic typing. Implicit type coercion (`"1" + 1 === "11"`) creates famous gotchas, but the flexibility enables the browser as a universal runtime.

**Lisp/Scheme** uses dynamic typing to support its code-as-data philosophy. Since code and data share the same structure (S-expressions), static types would constrain metaprogramming. Types are checked at runtime when needed.

### The Modern Convergence

The static/dynamic divide is softening:
- Python added type hints (PEP 484, 2015) — optional static analysis
- TypeScript added static types to JavaScript — gradual adoption
- Ruby gained RBS type signatures and Steep type checker
- Conversely, Java added `var` (2018) for local type inference
- C++ added `auto` — letting the compiler figure it out

The trend suggests the industry is converging on **static types with strong inference** — the OCaml/Rust/Kotlin model where types are checked at compile time but rarely written explicitly.

## 🔬 Deep Dive

### Trade-offs / Historical Context

The choice between static and dynamic typing is the most debated decision in language design. It reflects a deep philosophical divide about the role of the compiler and the nature of programming itself.

Static typing advocates argue: refactoring is safer, APIs are self-documenting, IDEs provide better tooling, and bugs caught at compile time are cheaper to fix. Dynamic typing advocates counter: development is faster, code is more concise, testing is necessary regardless, and types can't catch business logic bugs.

The empirical evidence is mixed. Studies show static typing catches ~15% of bugs that would otherwise reach production (Hanenberg et al., 2014), but dynamic languages enable faster initial development. The gap narrows as codebases grow — large Python/JavaScript projects increasingly adopt type annotations.

Historically, the sharp boundary between these camps is eroding. Dynamic languages are adding optional type layers, while static languages are reducing annotation burden through inference. The result is not that one side "won," but that the industry is increasingly trying to combine static guarantees with the ergonomics traditionally associated with dynamic languages.

## 🏋️ Practice

1. Pick one language from each camp—such as Rust and Python—and explain how each language's typing philosophy affects debugging, refactoring, and prototyping.
2. Evaluate the claim "testing is necessary regardless, so static types do not matter." What kinds of bugs can static types catch that tests might miss, and what kinds of bugs remain outside the reach of types?
3. Compare Python type hints, TypeScript, Java `var`, and C++ `auto`. Which of these reduce annotation burden, and which of them actually move a traditionally dynamic or static language toward the other camp?

## References

- [[Sources Index]]
