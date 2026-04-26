---
tags: [chunk, programming-languages, rust-traits]
source: "[[raw-pl-021]]"
---

# chunk-pl-071 Rust Trait System and Coherence

Traits define shared behavior in Rust:
- impl Display for Point { ... } — Point can be formatted
- n print<T: Display>(item: T) — generic over any Display type
- dyn Display — trait object for dynamic dispatch (vtable)

**Trait coherence:** For any type+trait combination, exactly one implementation exists. The **orphan rule** prevents conflicting implementations across crates: you can only implement a trait for a type if your crate defines either the trait or the type.

**Trait bounds:** Specify required capabilities: n process<T: Debug + Clone + Send>(item: T). Multiple bounds compose naturally.

**Default implementations:** Traits can provide default method implementations. Types can override specific methods while inheriting defaults.

**Associated types:** 	ype Output; in a trait — the implementing type chooses the concrete type. Iterator uses 	ype Item to define what it yields.

**Comparison:** Rust traits are more constrained than Haskell type classes (no orphan instances in Haskell, but this causes coherence issues). More powerful than Go interfaces (which are purely structural, no associated types or default methods).
