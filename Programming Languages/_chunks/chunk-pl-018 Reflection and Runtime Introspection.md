---
tags: [chunk, programming-languages, metaprogramming]
source: "[[raw-pl-006]]"
---

# chunk-pl-018 Reflection and Runtime Introspection

**Full reflection (Java, C#):** Discover classes, invoke methods by name, access private fields, create dynamic proxies. Powers: Spring DI, Hibernate ORM, JUnit. Trade-off: bypasses type safety, performance overhead, hard to analyze statically.

**Dynamic language reflection (Python, Ruby):** Natural because types are runtime concepts. Python: type(), dir(), getattr/setattr, metaclasses. Ruby: method_missing, define_method, open classes. ActiveRecord turns database columns into Ruby methods via method_missing.

**Minimal reflection (Go):** reflect package is deliberately limited. Used by encoding/json, fmt. Discouraged in application code.

**No reflection (Rust, Zig, C):** Types erased after compilation. Rust has Any trait for limited runtime type checking. Zig has compile-time reflection via @typeInfo. C has nothing.

The trend: compile-time metaprogramming (macros, comptime) over runtime reflection. Compile-time is faster, type-safe, and analyzable.
