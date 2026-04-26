---
tags: [chunk, programming-languages, visibility]
source: "[[raw-pl-008]]"
---

# chunk-pl-050 Visibility and Access Control Compared

How languages control access to internal implementation details:

**Java:** Four levels — public, protected, package-private, private. Java 9 modules add coarse-grained exports.

**Rust:** Path-based — pub, pub(crate), pub(super), pub(in path), private (default). No protected (no inheritance). Fine-grained module-relative visibility.

**Go:** Binary — uppercase = exported, lowercase = package-private. Simplest mechanism. Intentionally limited.

**Python:** Convention only — _private by convention, __mangled but still accessible. "We're all consenting adults here."

**OCaml:** Signature-based — .mli files define what's visible. Types can be made fully abstract. Most principled approach: interface declared separately from implementation.

**C++:** Class-based — public, protected, private + friend. Friend creates tight coupling.

Spectrum: OCaml (strongest) > Rust (fine-grained) > Java (four levels) > C++ (class + friend) > Go (binary) > Python (convention).

Strong access control enables safe refactoring at scale. Weak access control enables rapid iteration.
