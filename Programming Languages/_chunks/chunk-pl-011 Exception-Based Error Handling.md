---
tags: [chunk, programming-languages, error-handling]
source: "[[raw-pl-004]]"
---

# chunk-pl-011 Exception-Based Error Handling

Exceptions propagate failures up the call stack until caught. Originated in PL/I, formalized in CLU.

**Java checked exceptions:** Must declare throws clause. Intent: visible error signatures. Reality: verbose boilerplate, poor generics/lambda composition, catch-and-ignore patterns. No major language adopted checked exceptions after Java.

**Python:** Unchecked exceptions, EAFP philosophy. Any function can raise anything. Flexible but no visibility from signatures.

**C++:** Powerful but controversial. Exception safety (maintaining invariants mid-throw) is hard. Many codebases (Google) disable exceptions entirely.

**OCaml:** Lightweight exceptions — faster than Result types. Used for both errors and control flow. OCaml 5 adds algebraic effects as a principled alternative.

**Modern consensus:** New languages (Rust, Go, Zig) avoid exceptions. Existing languages (Java, Python, C++) keep them for backward compatibility.
