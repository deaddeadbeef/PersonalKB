---
tags: [programming-languages, metaprogramming, templates]
up: "[[Metaprogramming Overview]]"
tier-coverage: full
confidence: plausible
---
# Template Metaprogramming

## 🎯 Intuition

**The Core Idea:** Template metaprogramming (TMP) uses a language's generic/template system to compute values, select types, and generate code at compile time — turning the type checker into an execution engine.

**Analogy:** TMP is like discovering that the blueprint review process at a construction firm is actually Turing-complete — you can encode any computation in the approval stamps and revision marks. The architects (C++ committee) designed blueprints for simple parameterization, but builders discovered they could make the review process *compute*. Now the industry is moving toward giving builders a proper calculator (constexpr/comptime) instead of abusing the stamp system.

**Why It Matters:** TMP demonstrated that compile-time computation was valuable decades before languages offered direct support. Understanding it explains why C++ code looks the way it does, why Boost exists, and why modern languages (Rust, Zig, D) designed cleaner alternatives. It also remains relevant in legacy codebases and advanced library design.

## ⚙️ Core Mechanics

### C++ Templates: The Accidental Language

C++ templates are instantiated by the compiler, generating specialized code for each set of template arguments. This instantiation process can be controlled through:
- **Specialization:** Different implementations for different types
- **SFINAE (Substitution Failure Is Not An Error):** Template instantiation failure silently removes candidates
- **constexpr:** Compile-time function evaluation (C++11 onwards)
- **Concepts (C++20):** Named constraints on template parameters

TMP can compute Fibonacci numbers at compile time, implement type-level state machines, and generate optimal code for specific data sizes. The Boost libraries showcase extreme TMP capabilities.

**The cost:** C++ TMP is notoriously difficult to write, read, and debug. Error messages from failed template instantiation are legendary for their length and inscrutability. Compile times balloon with heavy TMP. The C++ committee has been steadily replacing TMP techniques with friendlier alternatives: `constexpr` for compile-time values, `if constexpr` for compile-time branching, and concepts for readable constraints.

### D Templates: C++ Done Better

D (2001) learned from C++ and provides cleaner template metaprogramming:
- Templates accept values and types as parameters
- `static if` for compile-time branching
- String mixins for code generation from strings
- CTFE (Compile-Time Function Evaluation) for running regular D functions at compile time

D proves that template metaprogramming can be powerful without being painful.

### Rust Generics vs C++ Templates

Rust generics look similar to C++ templates but are fundamentally different:
- **Rust:** Type-checked at definition time via trait bounds. The compiler verifies generic code is valid for ALL possible types satisfying the bounds.
- **C++:** Type-checked at instantiation time. Templates can use any operation on `T` — errors only appear when you try to instantiate with a type that doesn't support it.

Rust's approach catches errors earlier and produces better error messages. C++'s approach is more flexible but defers errors to template users. C++20 concepts bring C++ closer to Rust's model.

## 🔬 Deep Dive

### Trade-offs

| Aspect | C++ TMP | D Templates | Rust Generics |
|---|---|---|---|
| Type checking | At instantiation | At instantiation (+ `static if`) | At definition (trait bounds) |
| Error messages | Notoriously poor | Improved over C++ | Clear and early |
| Compile-time computation | Via template recursion, then `constexpr` | CTFE (regular functions) | `const fn`, const generics |
| Compile-time branching | SFINAE → `if constexpr` → concepts | `static if` | Trait bounds, where clauses |
| Code generation | Implicit via instantiation | String mixins | Proc macros (separate mechanism) |
| Compile time impact | Severe with heavy TMP | Moderate | Moderate (monomorphization) |

The fundamental trade-off is **flexibility vs. early checking**. C++ templates are maximally flexible (duck typing at instantiation) but defer errors to users. Rust generics catch errors at definition but require explicit trait bounds, sometimes making highly generic code verbose. D occupies a middle ground with cleaner syntax than C++ and `static if` for ergonomic compile-time branching.

### Historical Context

C++ templates were designed for generic programming — parameterizing code over types. They accidentally turned out to be Turing-complete, a discovery attributed to Erwin Unruh's prime-number computation in compiler error messages (1994). This spawned TMP as a discipline, codified by Alexandrescu's *Modern C++ Design* (2001) and the Boost libraries. The C++ committee's response has been a two-decade effort to provide intentional compile-time facilities: `constexpr` (C++11), `if constexpr` (C++17), `consteval` (C++20), and concepts (C++20).

Template metaprogramming is being replaced by more direct compile-time computation:
- **C++ constexpr/consteval:** Run regular functions at compile time
- **Zig comptime:** Execute any code at compile time (see [[Compile-Time Computation]])
- **Rust const generics:** Use constant values as type parameters
- **D CTFE:** Full function evaluation at compile time

The trend: instead of encoding computation in the type system (TMP), just run normal code at compile time. This is more readable, more powerful, and produces better error messages.

## 🏋️ Practice

1. **Classic TMP exercise (C++):** Implement a compile-time factorial using both old-style template recursion with specialization *and* modern `constexpr`. Compare the error messages when you pass a negative number to each version. Then rewrite with C++20 concepts to constrain the input.

2. **Rust generics vs C++ templates:** Write a generic `max` function in both Rust (with `PartialOrd` trait bound) and C++ (as a template without concepts, then with a C++20 concept). Intentionally pass a type that doesn't support comparison to each and compare the compiler error output.

3. **D string mixin exploration:** In D, write a string mixin that generates a struct with N fields named `field_0` through `field_N` at compile time using CTFE to build the source string. Verify the generated struct is usable at runtime and inspect the compiler output to confirm no runtime code generation occurs.

## References

- [[Sources Index]]
