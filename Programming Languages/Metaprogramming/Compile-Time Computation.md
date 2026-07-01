---
tags: [programming-languages, metaprogramming, comptime]
up: "[[Metaprogramming Overview]]"
confidence: established
freshness: stable
tier-coverage: full
confidence: plausible
---
# Compile-Time Computation

## 🎯 Intuition

**The Core Idea:** Move work from runtime to build time so the compiler evaluates expressions, generates specialized code, and eliminates unnecessary operations before the program ever runs.

**Analogy:** Compile-time computation is like a chef who pre-chops, pre-measures, and pre-mixes every ingredient before the restaurant opens — when orders come in, the kitchen only assembles and plates, delivering results faster with zero wasted motion at serving time.

**Why It Matters:** Programs start faster, run leaner, and fail earlier. Invalid configurations surface at build time instead of crashing in production, and the compiler can produce tightly specialized code that no runtime approach can match.

## ⚙️ Core Mechanics

### Zig Comptime: The Purest Model

Zig's comptime is the most radical implementation of compile-time computation. Any Zig expression can be marked `comptime`, causing it to execute during compilation. There's no separate template or macro language — you write normal Zig code, and the compiler runs it at build time.

```zig
fn fibonacci(comptime n: u32) u32 {
    if (n < 2) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}
const fib10 = comptime fibonacci(10); // computed at compile time
```

Zig uses comptime instead of generics: a "generic" function is simply a function with comptime parameters. Instead of `fn sort<T: Ord>(slice: []T)`, Zig writes `fn sort(comptime T: type, slice: []T)` — T is just a type value passed at compile time.

**Why this is revolutionary:**
- One language for both compile-time and runtime code
- No separate template/macro syntax to learn
- Compile-time code has the same debugging tools as runtime code
- Generics, conditional compilation, and code generation are all just comptime

### C++ constexpr Evolution

C++ has progressively expanded compile-time computation:
- **C++11 constexpr:** Single-return-statement functions evaluable at compile time
- **C++14:** Relaxed rules: loops, local variables, multiple statements
- **C++17:** `if constexpr` for compile-time branching (eliminating SFINAE in many cases)
- **C++20:** `consteval` (guaranteed compile-time), `constinit` (compile-time initialization)
- **C++23:** Further relaxation, approaching Zig's generality

The trajectory: C++ is converging toward "any code can run at compile time," but arriving there incrementally over decades.

### Rust Const Evaluation

Rust has `const fn` (functions evaluable at compile time) and `const` generics (type parameters that are values). Rust's const evaluation is more restricted than Zig's or C++23's — no heap allocation, no floating point (stabilization pending), limited control flow. The Rust team is gradually expanding const capabilities while ensuring soundness.

Rust's approach: conservative expansion. New const capabilities are added only when the team is confident they won't create soundness holes or maintenance burdens.

### OCaml Functors: Module-Level Computation

OCaml's functors (functions from modules to modules) perform a form of compile-time computation at the module level. A functor takes a module satisfying a signature and produces a new module. This enables: parameterized data structures (Map keyed by any ordered type), dependency injection at the module level, and code generation based on module interfaces.

While not as general as Zig's comptime, OCaml's module system achieves similar goals for large-scale code organization.

### Lisp: Compile-Time Is Just Time

In Lisp, the distinction between compile-time and runtime is blurred. Macros run during compilation but have access to the full language. `eval-when` controls when code executes. The REPL allows interactive compilation. This philosophy — computation is computation, regardless of when it happens — influenced Zig's comptime design.

## 🔬 Deep Dive

### Trade-offs

Compile-time computation delivers compelling benefits but introduces its own tensions:

1. **Zero runtime cost:** Work done at compile time doesn't consume runtime resources
2. **Early error detection:** Invalid configurations fail at build time, not in production
3. **Optimization:** The compiler can specialize code for specific values
4. **Reduced binary size:** Unused code paths are eliminated

Against these benefits stand real costs: longer compile times, increased compiler complexity, and (in C++) notoriously opaque error messages when compile-time evaluation fails. Zig sidesteps the error-message problem by reusing the same language for both phases, while C++ has spent decades layering friendlier abstractions (`constexpr`, `consteval`, concepts) atop the original template machinery.

### Historical Context

The concept evolved from simple constant folding in early compilers to executing arbitrary code during compilation. Lisp pioneered the idea that computation is computation regardless of *when* it happens. C++ discovered compile-time power accidentally through Turing-complete templates, then spent C++11 → C++23 making it intentional. Zig (2016) arrived at the cleanest model by starting fresh: one language, one syntax, with a `comptime` keyword to shift any expression to build time.

## 🏋️ Practice

1. **Compile-Time Lookup Table (Zig or C++):** Write a function that generates a lookup table of the first 20 prime numbers entirely at compile time. In Zig, use `comptime`; in C++, use `constexpr`. Verify the table exists as a constant in the emitted binary.

2. **constexpr vs runtime benchmark (C++):** Implement the same algorithm (e.g., SHA-256 of a short string) in both a `constexpr` version and a normal runtime version. Compare the binary output — confirm the `constexpr` version embeds the result directly while the runtime version includes the computation loop.

3. **Rust `const fn` boundary exploration:** Write a Rust `const fn` that works today, then try to extend it with heap allocation or floating-point operations. Document which operations the compiler rejects and find the relevant tracking issues for future stabilization.

## References

- [[Programming Languages/Sources/Sources Index|Sources Index]]
