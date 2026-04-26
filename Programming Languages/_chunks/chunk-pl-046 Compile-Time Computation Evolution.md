---
tags: [chunk, programming-languages, comptime]
source: "[[raw-pl-006]]"
---

# chunk-pl-046 Compile-Time Computation Evolution

Moving computation from runtime to build time:

**Zig comptime:** The purest model. Any code marked comptime executes during compilation. No separate template/macro language. Types are first-class comptime values. Generic functions are just functions with comptime parameters.

**C++ constexpr/consteval:** Progressive expansion over decades. C++11: simple functions. C++14: loops, variables. C++17: if constexpr. C++20: consteval (guaranteed compile-time). Converging toward "any code can run at compile time."

**Rust const fn:** Functions evaluable at compile time. More restricted than Zig/C++23. Conservative expansion — new capabilities added only when proven sound. Const generics allow values as type parameters.

**OCaml functors:** Module-level computation. Functors take modules, produce modules. Not as general as comptime but powerful for code organization.

**Lisp:** The distinction between compile-time and runtime is blurred. Macros run during compilation with full language access. eval-when controls execution timing. Influenced Zig's design.
