---
tags: [chunk, programming-languages, memory]
source: "[[raw-pl-002]]"
---

# chunk-pl-008 Manual Memory and Allocator Models

**C malloc/free:** Programmer allocates and frees explicitly. Maximum control. Common bugs: use-after-free, double-free, memory leaks, buffer overflows. No safety net.

**C++ RAII + smart pointers:** Tie resource lifetime to object lifetime. unique_ptr (single owner, auto-free), shared_ptr (reference-counted), weak_ptr (non-owning). RAII is C++'s greatest contribution — Rust formalized it into the ownership system.

**Zig allocator model:** Every function that allocates takes an explicit Allocator parameter. No global heap. Common allocators: GeneralPurposeAllocator (default with safety checks), ArenaAllocator (bulk free), FixedBufferAllocator (from fixed buffer), page_allocator (OS pages). Enables custom memory strategies and operation in freestanding environments.

**Value types vs reference types:** Value types (C structs, Rust, Swift structs, Go structs) copied on assignment, stack-allocated when possible — fast, cache-friendly. Reference types (Java objects, Python objects) heap-allocated, need GC. Languages emphasizing value types tend to have better performance.
