---
tags: [chunk, programming-languages, design-patterns]
source: "[[raw-pl-017]]"
---

# chunk-pl-094 Design Patterns and Language Features

Many "design patterns" are workarounds for missing language features:

**Iterator pattern -> built-in iterators:** Java needed the Iterator interface and for-each loop. Rust, Python, Go, Kotlin, Swift all have native iteration.

**Visitor pattern -> pattern matching:** Java pre-17 needed the Visitor to dispatch over type hierarchies. Rust match, Kotlin when, Java 21 pattern switch eliminate the need.

**Strategy pattern -> first-class functions:** Java pre-8 needed Strategy interfaces. Any language with lambdas/closures makes Strategy trivial.

**Singleton pattern -> module-level values:** Python modules, Rust static/lazy_static, Go package-level vars. Singleton is a pattern because Java requires classes for everything.

**Observer pattern -> reactive streams/channels:** Go channels, Rust tokio::broadcast, Kotlin Flow, Swift Combine. Built-in reactive primitives replace Observer.

**Builder pattern -> named parameters:** Kotlin's named and default parameters, Python's keyword arguments eliminate the need for builders in many cases.

Peter Norvig observed: "Design patterns are bug reports against your programming language." Languages evolve by absorbing patterns into features.
