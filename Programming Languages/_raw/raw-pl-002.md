---
tags: [raw, programming-languages, memory-management]
source: "The Garbage Collection Handbook (Jones et al., 2011), Rust Reference Manual"
created: 2025-07-25
---

# raw-pl-002: Memory Management Strategies

## Manual Memory Management (C, C++)

The programmer explicitly allocates (malloc/new) and frees (free/delete) memory. Maximum control, maximum risk. Common bugs: use-after-free, double-free, memory leaks, buffer overflows. C++ mitigates with RAII and smart pointers (unique_ptr, shared_ptr), but the underlying model is still manual.

## Garbage Collection

GC automatically reclaims memory no longer referenced. Major strategies:

**Mark-and-sweep:** Walk the object graph from roots, mark reachable objects, sweep unmarked ones. Simple but causes stop-the-world pauses. Used by: Go (concurrent variant), Ruby (generational mark-sweep), OCaml (generational).

**Generational GC:** Based on the generational hypothesis — most objects die young. Divide heap into young and old generations. Collect young generation frequently (fast, small), old generation rarely. Used by: JVM (G1, ZGC), .NET, OCaml, Python (for cycle detection).

**Concurrent/incremental GC:** Collect while the program runs, reducing pause times. Go's GC achieves sub-millisecond pauses. Java's ZGC and Shenandoah target <10ms pauses even with huge heaps. The trade-off: concurrent GC has higher throughput overhead.

## Reference Counting (Swift, Python, Objective-C)

Each object tracks how many references point to it. When the count reaches zero, the object is freed. Advantages: deterministic destruction, no GC pauses, simple implementation. Disadvantages: can't handle reference cycles (need cycle detection), overhead of incrementing/decrementing counts, cache-unfriendly count updates.

Swift uses ARC (Automatic Reference Counting) — the compiler inserts retain/release calls. Python uses reference counting as the primary GC mechanism, with a cycle detector for circular references.

## Ownership and Borrowing (Rust)

Rust's ownership system is unique: each value has exactly one owner. When the owner goes out of scope, the value is dropped. References (borrows) can be shared (&T, many readers) or exclusive (&mut T, one writer), never both. The borrow checker enforces these rules at compile time.

This eliminates: use-after-free (owned values are dropped exactly once), data races (can't have shared mutable state), and dangling references (lifetimes ensure references are valid). No GC, no reference counting, no runtime overhead — safety checked entirely at compile time.

## Zig's Allocator Model

Zig makes allocation explicit: every function that allocates takes an allocator parameter. No global allocator, no hidden allocations. This enables: custom allocators (arena, pool, stack), memory tracking, and operation in environments without a standard allocator (kernels, embedded).

## Value Types vs Reference Types

**Value types** (copied on assignment): C structs, Rust (everything by default), Swift structs, Go structs. Stored on the stack when possible — fast allocation, cache-friendly.

**Reference types** (shared by reference): Java objects, Python objects, Ruby objects, Swift classes. Stored on the heap — require GC or reference counting.

Languages that emphasize value types (Rust, Swift, Go) tend to have better cache performance and simpler reasoning about aliasing.
