---
tags: [chunk, programming-languages, design-philosophy]
source: "[[raw-pl-013]]"
---

# chunk-pl-025 Safety vs Performance Trade-off Spectrum

The fundamental language design tension:

**Maximum performance, minimal safety:** C, Zig. Trust the programmer. No GC, no bounds checks, no hidden costs. Bugs are your responsibility.

**Maximum safety AND performance:** Rust. Ownership system prevents memory errors at compile time. Zero runtime overhead. Price: steep learning curve, long compile times.

**High safety, moderate performance:** Go, Java, OCaml. Garbage collection for memory safety. Type system catches errors. GC pauses are the trade-off.

**Maximum convenience, lower performance:** Python, Ruby. Dynamic typing, GC, interpreted. 10-100x slower than C for CPU-bound work. Excellent for prototyping and orchestrating fast libraries.

Rust's unique achievement: proving safety and performance are compatible. The borrow checker is the price — but languages are exploring ways to bring ownership to simpler systems (Swift ownership annotations, Mojo).
