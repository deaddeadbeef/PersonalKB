---
tags: [chunk, programming-languages, cpp-profile]
source: "[[raw-pl-010]]"
---

# chunk-pl-042 C++ Zero-Cost Abstraction and RAII

C++ (1985, Stroustrup): "you don't pay for what you don't use." The most feature-rich systems language.

**RAII (Resource Acquisition Is Initialization):** C++'s greatest contribution. Constructors acquire resources, destructors release them. Deterministic cleanup without GC. smart pointers: unique_ptr (single owner), shared_ptr (ref counted), weak_ptr (non-owning). Rust's ownership system is formalized RAII.

**Zero-cost abstraction:** Virtual dispatch only when requested. Stack allocation by default. Templates generate specialized code. High-level abstractions compile to code you'd write by hand in C.

**The complexity problem:** 1800+ page standard. Raw pointers AND smart pointers. Exceptions AND error codes. Virtual inheritance AND CRTP. Macros AND templates AND constexpr. No single person knows all of C++.

**Move semantics (C++11):** Efficiently transfer resources between objects without copying. Enables returning containers from functions cheaply. Influenced Rust's ownership model.
