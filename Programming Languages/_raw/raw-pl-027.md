---
tags: [raw, programming-languages, zig-deep-dive]
source: "Zig documentation, Andrew Kelley talks, Zig community resources"
created: 2025-07-25
---

# raw-pl-027: Zig Deep Dive — No Hidden Behavior

## The Core Principle

Andrew Kelley's design goal: **no hidden behavior**. In Zig:
-  + b is always integer addition, never a user-defined operator
- There are no hidden function calls (no constructors, no destructors triggered implicitly)
- There are no hidden memory allocations (every allocation requires an explicit allocator)
- There are no hidden concurrency mechanisms (no goroutines spawned implicitly)

If you read Zig code, what you see is what happens. This is a direct response to C++'s implicit behaviors (copy constructors, move constructors, destructor calls, operator overloading, implicit conversions).

## Comptime: The Killer Feature

Instead of separate generics, templates, or macros, Zig uses comptime — compile-time execution of normal code:

`zig
fn max(comptime T: type, a: T, b: T) T {
    return if (a > b) a else b;
}
`

T is a type passed at compile time. The compiler generates specialized code for each concrete T. But unlike C++ templates, the error messages are clear because Zig evaluates normal code — there's no separate template language.

Comptime enables: generic data structures, conditional compilation, code generation, and compile-time validation — all with one mechanism.

## Allocator-Aware Design

Every Zig function that allocates takes an Allocator parameter. Common allocators:
- GeneralPurposeAllocator: Default, with safety checks
- ArenaAllocator: Bulk free, no individual deallocation
- FixedBufferAllocator: Allocate from a fixed-size buffer
- page_allocator: Direct OS page allocation

This design enables: custom memory strategies, memory tracking, and operation in freestanding environments (kernels, embedded) where there's no malloc.

## Safety Model

Zig's safety approach differs from Rust:
- **Debug mode:** Full safety checks — bounds checking, integer overflow detection, null pointer detection, use-after-free detection via poisoning
- **Release mode:** Safety checks removed for performance (ReleaseSafe keeps them; ReleaseFast strips them)
- **No borrow checker:** Zig doesn't prevent memory errors at compile time. It detects them at runtime in debug mode.

This is a conscious trade-off: simpler language (no lifetime annotations, no borrow checker fights) at the cost of less compile-time safety.

## C Interoperability

Zig's C interop is unmatched:
- Import C headers directly: const c = @cImport(@cInclude("stdio.h"))
- Call C functions without wrappers, bindings, or FFI ceremony
- Zig's build system can compile C and C++ code with the same toolchain
- Cross-compile to any target with built-in libc headers

This makes Zig practical for incremental C replacement: adopt one file at a time.

## Notable Users

Bun (JavaScript runtime) is written in Zig — chosen for predictable performance and C interop. TigerBeetle (financial database) uses Zig for deterministic execution. The Zig compiler itself is written in Zig (bootstrapped from C).
