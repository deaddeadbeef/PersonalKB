---
tags: [pl, chunk, cpp, modern]
up: "[[C++ Language Profile]]"
---

# Modern C++ The Renaissance Since C++11

C++11 was such a dramatic improvement that Bjarne Stroustrup called it "a new language." Each subsequent standard has continued the modernization.

## Evolution Timeline

### C++11 (The Revolution)
- `auto` type deduction
- Range-based for loops
- Lambda expressions
- Move semantics and rvalue references
- Smart pointers (unique_ptr, shared_ptr)
- `nullptr` (replacing NULL)
- Variadic templates
- constexpr

### C++14 (Polish)
- Generic lambdas `[](auto x) { return x; }`
- Return type deduction
- Binary literals

### C++17 (Major Additions)
- Structured bindings: `auto [x, y, z] = tuple;`
- `std::optional`, `std::variant`, `std::any`
- `if constexpr` (compile-time branching)
- Filesystem library
- Parallel algorithms

### C++20 (The Next Revolution)
- Concepts: `template<typename T> requires Sortable<T>`
- Ranges: `views::filter | views::transform`
- Coroutines: `co_await`, `co_yield`, `co_return`
- Modules: replace header files
- Three-way comparison (`<=>` spaceship operator)
- `consteval` (guaranteed compile-time evaluation)

### C++23/26 (Ongoing)
- `std::expected` (Result type!)
- `std::print` (modern formatting)
- Pattern matching (proposal)
- Reflection (proposal for C++26)
- Contracts (proposal for C++26)

## The Safe C++ Movement

C++ is grappling with memory safety:
- **Profiles proposal:** Compiler-enforced safety subsets
- **Carbon:** Google's proposed C++ successor with interop
- **Circle compiler:** Experimental safe C++ extensions (borrow checking)
- **cppfront (Cpp2):** Herb Sutter's evolution of C++ syntax

## Key Insight
Modern C++ is barely recognizable compared to C++98. `std::optional`, ranges, concepts, and coroutines bring it closer to Rust's expressiveness. But the fundamental problem remains: new features are additive — all old features still exist, making the language enormous and hard to learn.

## References
→ [[Sources Index]]
