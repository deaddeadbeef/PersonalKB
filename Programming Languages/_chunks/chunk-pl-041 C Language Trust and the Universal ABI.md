---
tags: [chunk, programming-languages, c-profile]
source: "[[raw-pl-010]]"
---

# chunk-pl-041 C Language Trust and the Universal ABI

C (1972, Dennis Ritchie) was designed to write Unix. Philosophy: **trust the programmer**. Minimal abstraction over hardware — types map to machine representations, pointers are addresses, structs have predictable layout.

**The C ABI:** Every major language has C FFI. C's calling convention and data layout form the de facto standard for cross-language communication. Rust extern "C", Go cgo, Python ctypes, Java JNI, OCaml external — all call C. This makes C libraries (OpenSSL, SQLite, zlib, POSIX) universally accessible.

**What C got wrong:** Memory unsafety (buffer overflows, use-after-free), undefined behavior (compiler assumes it never happens), no modules (header files = textual inclusion), null-terminated strings.

**Why C persists:** Linux kernel, SQLite, Python interpreter, nginx, PostgreSQL. For hardware interaction and OS APIs, C is irreplaceable. The C ABI is the lingua franca of software.
