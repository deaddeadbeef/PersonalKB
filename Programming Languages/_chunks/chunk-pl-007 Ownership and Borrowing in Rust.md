---
tags: [chunk, programming-languages, memory]
source: "[[raw-pl-002]]"
---

# chunk-pl-007 Ownership and Borrowing in Rust

Rust's ownership system eliminates memory errors at compile time without GC:

**Ownership rules:**
1. Every value has exactly one owner
2. When owner goes out of scope, value is dropped (freed)
3. Ownership transfers on assignment (move semantics)

**Borrowing rules:**
1. Many shared references (&T) OR one mutable reference (&mut T), never both
2. References must not outlive the data they point to

**Lifetimes** annotate how long references are valid: n longest<'a>(x: &'a str, y: &'a str) -> &'a str. Usually inferred; explicit when the compiler needs help.

This eliminates: use-after-free, double-free, data races, dangling references — all at compile time with zero runtime overhead. The borrow checker is Rust's most innovative and most challenging feature.
