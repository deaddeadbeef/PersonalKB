---
tags: [chunk, programming-languages, iterator-patterns]
source: "[[raw-pl-020]]"
---

# chunk-pl-100 Iterator and Collection Patterns

Functional collection operations across languages:

**Rust iterators:**
`ust
items.iter()
     .filter(|x| x.is_valid())
     .map(|x| x.transform())
     .collect::<Vec<_>>()
`
Lazy (no intermediate collections). Zero-cost: compiles to a single loop. .collect() materializes.

**Java Streams:**
`java
items.stream()
     .filter(Item::isValid)
     .map(Item::transform)
     .collect(Collectors.toList());
`
Lazy. Parallel streams for multi-threaded execution. API more verbose than Rust/Kotlin.

**Kotlin:**
`kotlin
items.filter { it.isValid() }
     .map { it.transform() }
`
Eager by default. .asSequence() for lazy evaluation. Most concise syntax.

**Python:** List comprehensions [x.transform() for x in items if x.is_valid()]. Generators for lazy: (x for x in items if x.valid). Most readable for simple cases.

**Key pattern:** map (transform each), filter (keep matching), fold/reduce (accumulate), flatMap (one-to-many), zip (combine parallel sequences), take/skip (windowing).

All languages converge on these same operations. The syntax varies; the semantics are universal.
