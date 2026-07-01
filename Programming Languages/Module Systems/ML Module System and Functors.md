---
tags: [programming-languages, module-systems, ml-modules]
up: "[[Module Systems Overview]]"
confidence: established
freshness: stable
tier-coverage: full
confidence: plausible
---
# ML Module System and Functors

## 🎯 Intuition

**The Core Idea:** The ML module system (OCaml, Standard ML) provides the most powerful module system in any widely-used programming language — abstract types, module-level functions (functors), and first-class modules.

**Analogy:** If ordinary modules are like sealed boxes with labelled input/output slots, ML modules are a full factory system — structures are the machines on the floor, signatures are the specification sheets describing what each machine must do, and functors are assembly lines that take one machine as a template and stamp out a new customised machine.

**Why It Matters:** ML modules solve problems other languages work around with generics, traits, or design patterns. Understanding them reveals what a truly expressive module system can look like and clarifies the trade-offs other languages made for simplicity.

## ⚙️ Core Mechanics

### The Three Components

**Structures:** Concrete modules containing types, values, and sub-modules. A structure is like a record (struct) at the module level.

**Signatures:** Module types (interfaces) specifying what a module must provide. Signatures can hide types (making them abstract) and restrict which values are visible.

**Functors:** Functions from modules to modules. A functor takes a module satisfying a signature and produces a new module. This is parameterized programming at the module level.

### Abstract Types via Signatures

The most powerful feature: signatures can make types abstract. If a signature exposes `type t` without revealing its definition, code outside the module cannot construct or inspect values of type `t` directly — only through the module's functions.

```ocaml
module type SET = sig
  type t
  type elt
  val empty : t
  val add : elt -> t -> t
  val member : elt -> t -> bool
end
```

Code using a SET module knows that `t` exists and can use `empty`, `add`, `member` — but cannot peek inside `t` to see if it's a list, tree, or hash table. This is the strongest form of encapsulation available in any programming language.

### Functors: Parameterized Modules

A functor takes a module as input and produces a module as output. OCaml's standard library uses functors extensively:

```ocaml
module IntSet = Set.Make(Int)    (* Set of integers *)
module StringMap = Map.Make(String)  (* Map with string keys *)
```

`Set.Make` is a functor that takes any module with a compare function and produces a balanced tree set for that type. This is the module-level analogue of generics/templates but with more power: functors can add types, compose modules, and enforce invariants that generics cannot.

### First-Class Modules (OCaml)

OCaml allows packing modules into values and unpacking them, making modules first-class. This enables runtime selection of module implementations — e.g., choosing between different data structure implementations based on input size.

## 🔬 Deep Dive

### Trade-offs and Historical Context

#### Why Other Languages Don't Have This

ML modules are powerful but complex:
- **Dependent types (in a limited sense):** Module types can depend on module values, creating a sophisticated type theory
- **Sharing constraints:** When combining modules, you must specify which types are equal across modules
- **Higher-order functors:** Functors that take functors as arguments (OCaml supports this)

Most languages chose simpler mechanisms: Java's packages + interfaces, Rust's crates + traits, Haskell's type classes. These sacrifice some expressive power for a lower learning curve.

#### Rust Traits vs OCaml Functors

Rust's traits and OCaml's functors solve similar problems differently:
- Traits dispatch on types (a type implements a trait); functors operate on modules (a module satisfies a signature)
- Traits are open (any crate can implement a trait for a type); functors are closed (the functor application is explicit)
- Traits integrate with the type system (generic bounds); functors are a separate language layer
- Rust has no equivalent of abstract types through signatures; OCaml has no equivalent of trait objects (dynamic dispatch on traits)

#### The Expressiveness–Complexity Trade-off

The ML module system sits at the far end of the expressiveness spectrum. It enables patterns impossible in other languages — parameterised libraries, type-safe plugin systems, and abstraction boundaries that cannot be broken. The cost is a steeper learning curve: sharing constraints, applicative vs generative functors, and the interaction between the core type system and the module type system add genuine complexity.

## 🏋️ Practice

**Exercise 1 — Functor from Scratch:** In OCaml, write a functor `MakeStack(Elem : sig type t end)` that produces a module implementing a stack (push, pop, top, empty, is_empty) where the element type is `Elem.t` and the internal representation is abstract. Then apply it to create an `IntStack` and a `StringStack`.

**Exercise 2 — Signature Restriction:** Start with a concrete OCaml module that exposes its type as `type t = int list`. Write two signatures: one that keeps `t` transparent (`type t = int list`) and one that makes it abstract (`type t`). Demonstrate that code using the abstract signature cannot pattern-match on the list, while code using the transparent signature can. Explain when each choice is appropriate.

**Exercise 3 — Traits vs Functors Comparison:** Implement a sorted-set abstraction in both Rust (using a trait `Ord` and generics) and OCaml (using a functor over an `ORDERED` signature). Compare the resulting APIs: which is easier to instantiate? Which gives stronger encapsulation? Which supports adding new operations after the fact?

## References

- [[Programming Languages/Sources/Sources Index|Sources Index]]
