---
tags: [programming-languages, type-systems, generics]
up: "[[Type Systems Overview]]"
confidence: established
freshness: stable
tier-coverage: full
confidence: plausible
---
# Generics and Parametric Polymorphism

## 🎯 Intuition

**The Core Idea:** Generics allow code to operate on multiple types without duplication, and the design of a language's generics system reveals deep assumptions about the trade-off between abstraction power, implementation complexity, and runtime performance.

**Analogy:** Generics are like cookie cutters that work with any dough: you use one reusable shape, but different kitchens handle the baking differently—some make a fresh batch for each dough, some reuse one mold everywhere, and some add extra wrapping to keep everything uniform.

**Why It Matters:** Without generics, a list container must either: (1) be duplicated for each element type (C approach — macros or copy-paste), (2) use a universal base type (Java pre-5 — Object, losing type safety), or (3) use dynamic typing (Python — no compile-time checks). Generics let you write `List<T>` once, preserving type safety and avoiding duplication.

## ⚙️ Core Mechanics

### Implementation Strategies

**Monomorphization (Rust, C++):** The compiler generates a specialized copy of the generic code for each concrete type used. `Vec<i32>` and `Vec<String>` produce entirely different machine code. Advantage: zero runtime overhead, full optimization per type. Disadvantage: larger binary sizes, longer compile times.

**Type Erasure (Java, Kotlin on JVM):** Generic type parameters are erased after compilation. `List<Integer>` and `List<String>` become the same `List<Object>` at runtime. Advantage: no code duplication, backward compatibility with pre-generics JVM. Disadvantage: no runtime type information (can't do `instanceof T`), boxing overhead for primitives.

**Uniform Representation (OCaml, Haskell via dictionary passing):** All values are represented uniformly (typically as boxed pointers), so generic code works without specialization. OCaml compiles generic functions once, passing types implicitly. Advantage: fast compilation, small binaries. Disadvantage: boxing overhead, less optimization opportunity.

**Go's Late Addition:** Go added generics in version 1.18 (2022) after years of deliberation. The team used a hybrid approach: monomorphization for some types, dictionary passing for others (GC shape stenciling). Go's generics are deliberately constrained — no operator overloading, no method-level type parameters initially. This reflects Go's philosophy: add features reluctantly and minimally.

### Bounded Polymorphism: Constraining Type Parameters

Raw parametric polymorphism says nothing about what operations `T` supports. Languages add constraints differently:

**Rust trait bounds:** `fn sort<T: Ord>(list: &mut [T])` — `T` must implement the `Ord` trait. Multiple bounds compose with `+`. `where` clauses handle complex constraints. This is the most precise system — the compiler knows exactly what operations are available.

**Haskell type classes:** `sort :: Ord a => [a] -> [a]` — similar to Rust but with different resolution rules and more powerful features (higher-kinded types, multi-parameter type classes).

**OCaml:** Generic functions are constrained by usage — if you use `+` on a type parameter, OCaml infers it must be numeric. OCaml's module system (functors) provides another form of bounded generics at the module level, allowing parameterization over entire module interfaces.

**Java wildcards:** `List<? extends Comparable>` — wildcards express use-site variance. The `extends`/`super` bounds are powerful but notorious for complexity ("PECS: Producer Extends, Consumer Super").

**TypeScript:** `<T extends HasName>` — structural bounds. `T` must have the shape of `HasName`, checked structurally.

### Variance: Covariance and Contravariance

If `Dog` is a subtype of `Animal`, is `List<Dog>` a subtype of `List<Animal>`? This depends on **variance**:

- **Covariant** (safe for reading): `List<Dog>` IS-A `List<Animal>` for read-only access
- **Contravariant** (safe for writing): `List<Animal>` IS-A `List<Dog>` for write-only access
- **Invariant** (safe for both): No subtype relationship

**Kotlin** makes variance explicit: `List<out T>` (covariant), `MutableList<T>` (invariant), `Comparable<in T>` (contravariant). **Rust** infers variance from usage. **Java** uses wildcards at use-site. **OCaml** infers variance for type parameters automatically.

## 🔬 Deep Dive

### Trade-offs / Historical Context

The implementation strategy a language chooses is not just a compiler detail; it encodes what that language prioritizes. Monomorphization prioritizes zero-cost abstraction and optimization, but pays with larger binaries and longer compile times. Type erasure prioritizes interoperability and backward compatibility, but loses runtime type information and can impose boxing overhead. Uniform representation prioritizes simpler compilation and smaller binaries, but often gives up optimization opportunities because values are boxed and handled generically.

Go's delayed adoption of generics is historically revealing. It spent years resisting the feature, then introduced it in 1.18 (2022) with a hybrid implementation and deliberately constrained surface area. No operator overloading and no method-level type parameters initially were not accidents; they were expressions of Go's broader philosophy that powerful abstraction features should be added reluctantly and minimally.

Bounded polymorphism and variance show that "generic" does not mean "anything goes." Once you ask what operations `T` supports, you need trait bounds, type classes, structural bounds, or wildcards. Once you ask whether `List<Dog>` should be usable where `List<Animal>` is expected, you enter the safety trade-offs of covariance, contravariance, and invariance. Different languages answer these questions differently because they optimize for different balances of safety, ergonomics, and expressiveness.

## 🏋️ Practice

1. Explain how you would implement a generic `List<T>` in a language with no generics, and identify exactly what is lost in each of the three fallback approaches: duplication, universal base type, and dynamic typing.
2. Compare Rust/C++ monomorphization with Java/Kotlin type erasure for a generic sorting library. Which approach gives better runtime optimization, and which one gives better backward compatibility?
3. Given `Dog <: Animal`, decide whether each of these should be covariant, contravariant, or invariant: a read-only list, a write-only sink, and a mutable list. Then explain why Kotlin uses `out`, `in`, and invariant positions the way it does.

## References

- [[Programming Languages/Sources/Sources Index|Sources Index]]
