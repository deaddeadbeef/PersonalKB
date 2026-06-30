---
tags: [pl, study, memory-management]
up: "[[Programming Languages Study Index]]"
confidence: policy
---
# Review Drill — Memory Management Models

## Quick Recall

1. Name the 4 main memory management strategies and one language that uses each.
2. How does Rust's ownership system prevent use-after-free without a garbage collector?
3. What is the difference between tracing GC and reference counting?
4. Explain mark-and-sweep vs generational GC. Which languages use which?
5. What are value types vs reference types? How does Swift handle this distinction?

## Deep Dive Questions

### Manual Memory Management
- Why is C's malloc/free model both the most flexible and most dangerous?
- How do arena allocators work? Where does Zig use them?
- What is RAII? How does C++ use destructors to manage resources beyond memory?

### Garbage Collection
- Compare Java's G1GC, Go's concurrent collector, and .NET's generational GC.
- Why does Go optimize for low latency while Java's G1GC optimizes for throughput?
- How does Erlang/BEAM's per-process GC enable soft real-time guarantees?
- What are GC pauses and how do different collectors minimize them?

### Ownership and Borrowing
- Explain Rust's borrowing rules: one mutable OR many immutable references.
- What is the borrow checker? How does it reason about lifetimes?
- How do smart pointers (Box, Rc, Arc) extend Rust's ownership model?
- Why is Pin needed for self-referential structs in async Rust?

### Reference Counting
- How does Swift's ARC differ from Python's reference counting?
- What is the retain cycle problem? How do weak references solve it?
- Why did Objective-C move from manual retain/release to ARC?

### Trade-offs
- Plot memory strategies on a safety vs performance axis. Where does each language fall?
- Why might a language with GC (Go) outperform one without (C++) in certain scenarios?
- What is the "zero-cost abstraction" ideal and how close does Rust get?

## Connections to Explore
- [[Memory Management Overview]] — hub page
- [[Ownership and Borrowing]] — Rust's model
- [[Garbage Collection Strategies]] — GC approaches
- [[Value Types vs Reference Types]] — data layout

## References
→ [[Sources Index]]
