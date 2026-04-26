---
tags: [chunk, programming-languages, design-philosophy]
source: "[[raw-pl-030]]"
---

# chunk-pl-026 Explicit vs Implicit Language Philosophy

The most fundamental design axis:

**Explicit languages (Go, Zig, Rust):** Code says what it does. No hidden behavior. More verbose but easier to reason about. Go: no inheritance (no hidden method resolution), no exceptions (error handling visible), no operator overloading (+ always means addition). Zig: no hidden control flow, no hidden allocations.

**Implicit languages (Ruby, Python, C++):** Language does things for you. Less verbose but behavior can surprise. Ruby: method_missing, open classes, convention-over-configuration. C++: implicit constructors, operator overloading, template instantiation.

**The spectrum:** Go and Zig are maximally explicit. Ruby and C++ are heavily implicit. Rust is explicit about safety (ownership annotations) but implicit about type inference. Python is explicit in syntax ("explicit is better than implicit") but implicit in types (dynamic).
