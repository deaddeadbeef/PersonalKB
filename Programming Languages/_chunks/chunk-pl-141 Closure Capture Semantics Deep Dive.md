---
tags: [pl, chunk, closures, capture]
up: "[[Programming Paradigms Overview]]"
---

# Closure Capture Semantics Deep Dive

How closures capture variables reveals fundamental language design choices about mutability, ownership, and performance.

## The Python-JavaScript Gotcha

Both Python and JavaScript capture variables by reference, leading to the classic loop closure bug:

`python
# Python: all closures see the FINAL value of i
funcs = [lambda: i for i in range(3)]
[f() for f in funcs]  # [2, 2, 2] - not [0, 1, 2]!
`

`javascript
// JavaScript (var): same problem
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0); // 3, 3, 3
}
// Fix: use let (block-scoped)
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0); // 0, 1, 2
}
`

## Rust's Three Closure Traits

Rust's ownership system gives closures precise semantics:

`ust
// Fn - borrows immutably (can call many times)
let name = String::from("Rust");
let greet = || println!("Hello, {name}"); // borrows name
greet(); greet(); // OK

// FnMut - borrows mutably (can call many times, exclusive access)
let mut count = 0;
let mut increment = || { count += 1; }; // mutably borrows count
increment(); increment();

// FnOnce - takes ownership (can call only once)
let name = String::from("Rust");
let consume = move || { drop(name); }; // owns name
consume(); // OK
// consume(); // ERROR: already consumed
`

The compiler automatically determines which trait applies based on how the closure uses captured variables.

## C++'s Explicit Capture Lists

C++ forces the developer to declare capture intent:
`cpp
int x = 10;
auto by_val = [x]() { return x; };        // copy
auto by_ref = [&x]() { return x; };       // reference
auto all_val = [=]() { return x; };        // copy all
auto all_ref = [&]() { return x; };        // reference all
auto mixed = [x, &y]() { return x + y; }; // mixed
`

This explicitness prevents accidental captures but adds syntactic overhead.

## Performance Implications

| Language | Capture Cost | Inlining | Heap Allocation |
|----------|-------------|----------|-----------------|
| Rust | Zero-cost (monomorphized) | Always (when possible) | Only with Box<dyn Fn> |
| C++ | Zero-cost (usually) | Aggressive | Only with std::function |
| Go | Heap allocation | Limited | Always (closure is a pointer) |
| Java | Lambda metafactory | JIT can inline | Optimized by JVM |
| Python | Dict lookup | Never | Always (function object) |

## Key Insight
Rust's three closure traits (Fn/FnMut/FnOnce) are the most principled capture system in any mainstream language. They make the cost model explicit, prevent use-after-move bugs, and enable zero-cost closures that compile to the same code as hand-written structs.

## References
→ [[Sources Index]]
