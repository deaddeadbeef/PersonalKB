---
tags: [chunk, programming-languages, template-metaprogramming]
source: "[[raw-pl-006]]"
---

# chunk-pl-055 Template Metaprogramming and Concepts

**C++ templates:** Designed for generics, accidentally Turing-complete. Template instantiation generates specialized code. SFINAE (Substitution Failure Is Not An Error) enables compile-time type selection. TMP can compute Fibonacci at compile time, implement type-level state machines.

**The cost:** Notoriously difficult to write, read, debug. Error messages legendary for length. Compile times balloon. The C++ committee steadily replaces TMP with friendlier alternatives.

**C++20 Concepts:** Named constraints on template parameters. `template<std::totally_ordered T>` replaces SFINAE hacks with readable constraints. Brings C++ closer to Rust's trait-bounded generics.

**D templates:** C++ done better. static if for compile-time branching. String mixins for code generation. CTFE (Compile-Time Function Evaluation). Proves TMP can be powerful without being painful.

**Rust generics vs C++ templates:** Rust checks generics at definition time (via trait bounds); C++ checks at instantiation time. Rust catches errors earlier with better messages. C++ is more flexible but defers errors to template users.
