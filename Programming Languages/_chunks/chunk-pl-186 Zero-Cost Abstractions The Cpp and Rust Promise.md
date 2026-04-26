---
tags: [pl, chunk, design, zero-cost]
up: "[[Compilation and Runtime Overview]]"
---

# Zero-Cost Abstractions The C++ and Rust Promise

"You don't pay for what you don't use, and what you do use, you couldn't hand-code any better." - Bjarne Stroustrup

## What Zero-Cost Means

An abstraction is zero-cost if using it produces the same machine code as writing the low-level equivalent by hand.

\\\ust
// High-level Rust:
let sum: i32 = (0..1000).filter(|x| x % 2 == 0).sum();

// Compiles to the same machine code as:
let mut sum = 0i32;
let mut i = 0;
while i < 1000 {
    if i % 2 == 0 { sum += i; }
    i += 1;
}
\\\

## Zero-Cost Examples

| Abstraction | Language | Cost |
|-------------|---------|------|
| Iterators | Rust | Zero (monomorphized, inlined) |
| Generics | Rust, C++ | Zero (monomorphized) |
| Smart pointers | Rust (Box), C++ (unique_ptr) | Zero vs raw pointer |
| Closures | Rust (non-dyn), C++ (lambda) | Zero (inlined) |
| Async/await | Rust | Zero (state machine, no heap alloc) |
| RAII destructors | C++, Rust | Zero (deterministic, inlined) |
| Traits (static dispatch) | Rust | Zero (monomorphized) |
| References | Rust | Zero (compiled away in optimized builds) |

## Non-Zero-Cost Abstractions

| Abstraction | Language | Cost |
|-------------|---------|------|
| Virtual dispatch | Java, C# | Vtable indirection |
| Garbage collection | Go, Java, Python | GC overhead |
| Dynamic dispatch | Rust (dyn Trait) | Vtable + no inlining |
| Reflection | Java, Go, C# | Runtime metadata lookup |
| Boxing | Java generics | Heap allocation per primitive |
| Exceptions (error path) | C++, Java | Stack unwinding |

## The Trade-off

Zero-cost abstractions have costs that aren't measured at runtime:
- **Compile time:** Monomorphization creates many copies
- **Binary size:** Specialized code for every type combination
- **Compile errors:** More complex type inference
- **Learning curve:** Understanding ownership, lifetimes, traits

## Key Insight
Rust's achievement is providing zero-cost abstractions for MORE features than C++ (async, iterators, closures, Option/Result) while also being memory-safe. The compile-time cost is real (Rust compiles slowly), but the runtime result is indistinguishable from hand-optimized C.

## References
→ [[Sources Index]]
