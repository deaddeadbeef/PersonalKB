---
tags: [chunk, programming-languages, variance]
source: "[[raw-pl-016]]"
---

# chunk-pl-108 Variance in Generic Types

If Dog is a subtype of Animal, what about List<Dog> and List<Animal>?

**Covariant (out):** List<Dog> subtypes List<Animal>. Safe for reading/producing. Java: ? extends Animal. Kotlin: out Animal. C#: out T.

**Contravariant (in):** Consumer<Animal> subtypes Consumer<Dog>. Safe for writing/consuming. Java: ? super Dog. Kotlin: in Dog. C#: in T.

**Invariant:** No subtype relationship. Safe for both reading and writing. Java: raw List<Animal>. Rust: default for mutable references.

**Java's approach (use-site variance):** Wildcards at each usage. List<? extends Animal> (covariant use), List<? super Dog> (contravariant use). Flexible but verbose. The "Get-Put Principle": use extends for getting, super for putting.

**Kotlin/C# approach (declaration-site variance):** Declare variance once at the type definition. class Producer<out T>, class Consumer<in T>. Cleaner than Java but less flexible per-use.

**Rust:** Variance inferred by the compiler based on usage. PhantomData controls variance for unsafe code. Shared references (&T) are covariant; mutable references (&mut T) are invariant.

**OCaml:** Variance inferred for type parameters. The compiler checks that declared variance is safe.
