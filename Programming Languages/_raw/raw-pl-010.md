---
tags: [raw, programming-languages, language-profiles]
source: "Various language documentation and design papers"
created: 2025-07-25
---

# raw-pl-010: Systems Languages — C, C++, Rust, Zig, Go

## C (1972) — Trust the Programmer

Dennis Ritchie designed C to write Unix. Minimal abstraction over hardware. No GC, no bounds checking, no hidden behavior. The C ABI is the universal interface between languages. Every major language has C FFI. Problems: memory unsafety (buffer overflows, use-after-free), undefined behavior, no modules (header files).

C remains essential: Linux kernel, SQLite, Python interpreter, nginx, PostgreSQL. For interacting with hardware and OS APIs, C is irreplaceable.

## C++ (1985) — Zero-Cost Abstraction

Stroustrup's "C with Classes" became the most feature-rich language in existence. Zero-overhead abstraction: virtual dispatch only when requested, stack allocation by default, templates generate specialized code. RAII (tie resource lifetime to object lifetime) is C++'s greatest contribution — Rust's ownership is formalized RAII.

Problems: extreme complexity (1800+ page standard), undefined behavior inherited from C, template error messages, slow compilation, fragmented ecosystem (no standard package manager).

## Rust (2015) — Safety Without GC

Ownership + borrowing eliminate memory errors at compile time. No GC, no runtime overhead. Result types for error handling. Fearless concurrency via Send/Sync traits. Cargo is the best build/package system.

Problems: steep learning curve (borrow checker, lifetimes), slow compilation, complex async story (Pin, lifetime interaction), orphan rules limit trait flexibility.

Rust is replacing C/C++ in security-sensitive contexts: the Linux kernel accepts Rust, Android uses Rust for new native code, Microsoft rewrites Windows components in Rust.

## Zig (2016) — Simplicity Without Sacrifice

Andrew Kelley's "better C": no hidden control flow, no hidden allocations, explicit allocator passing. Comptime replaces generics, templates, and macros with compile-time execution of normal code. Direct C interop (import C headers, compile C code).

No GC, no borrow checker — runtime safety checks in debug mode, stripped in release. Simpler than Rust but less safe. Used by: Bun (JS runtime), TigerBeetle.

## Go (2009) — Simplicity at Scale

Google's answer to C++ build times and complexity. Fast compilation, goroutines + channels for concurrency, GC for memory safety, single static binaries. Deliberately omits: generics (until 1.18), exceptions, inheritance, macros.

Go's simplicity is its superpower and its limitation. Dominates: cloud infrastructure (Docker, Kubernetes, Terraform), CLIs, network services.
