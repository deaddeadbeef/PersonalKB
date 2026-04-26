---
tags: [chunk, programming-languages, zig]
source: "[[raw-pl-027]]"
---

# chunk-pl-038 Zig No Hidden Behavior and Comptime

**Core principle:** No hidden behavior.  + b always means arithmetic. No hidden function calls, no hidden allocations, no hidden concurrency. If you read Zig code, what you see is what happens.

**Comptime:** Normal Zig code executes at compile time. No separate generics/template/macro language. n max(comptime T: type, a: T, b: T) T — T is a type value passed at compile time. One language for compile-time and runtime.

**Allocator-aware:** Every allocation requires an explicit Allocator parameter. No global heap. Enables: custom allocators (arena, pool, fixed buffer), memory tracking, freestanding operation (kernels, embedded).

**Safety model:** Runtime safety checks in debug (bounds, overflow, null). Stripped in release. No borrow checker — simpler than Rust but less compile-time safe.

**C interop:** Import C headers directly with @cImport. Call C functions without wrappers. Build system compiles C/C++ code. Cross-compile to any target. Practical for incremental C replacement.

**Users:** Bun (JS runtime), TigerBeetle (financial DB). Chosen for predictable performance and C interop.
