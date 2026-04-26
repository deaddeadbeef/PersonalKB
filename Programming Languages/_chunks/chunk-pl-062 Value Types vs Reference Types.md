---
tags: [chunk, programming-languages, value-reference]
source: "[[raw-pl-002]]"
---

# chunk-pl-062 Value Types vs Reference Types

**Value types** (copied on assignment, typically stack-allocated):
- C: structs, primitives
- Rust: everything by default (Copy trait for bitwise copy, Clone for explicit)
- Swift: structs, enums (with copy-on-write optimization)
- Go: structs, arrays, primitives
- C#: structs, primitives
- Kotlin: primitive types on JVM

**Reference types** (shared via pointer/reference, heap-allocated):
- Java: all objects (except primitives)
- Python: all objects
- Ruby: all objects
- Swift: classes
- Kotlin: all objects on JVM

**Why it matters:** Value types are cache-friendly (contiguous memory), have no aliasing (mutation doesn't affect other references), and require no GC. Reference types enable sharing and polymorphism but introduce aliasing, require GC, and cause cache misses.

**Swift's approach:** Default to structs (value types). Use classes only when you need reference semantics or inheritance. Array, Dictionary, String are all value types with copy-on-write. This gives value semantics with reference performance for large collections.
