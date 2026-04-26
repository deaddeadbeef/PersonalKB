---
tags: [chunk, programming-languages, type-systems]
source: "[[raw-pl-016]]"
---

# chunk-pl-004 Generics Implementation Strategies

Three ways to implement generics:

**Monomorphization (Rust, C++):** Compiler generates specialized code for each concrete type. Vec<i32> and Vec<String> become separate compiled types. Zero runtime overhead. Cost: code size growth, longer compilation.

**Type erasure (Java):** Generic types erased to bounds at compile time. List<String> becomes List<Object> in bytecode. Preserves backward compatibility. Cost: no runtime type info, can't do 
ew T(), boxing for primitives.

**Reification (.NET):** Generic types preserved at runtime. List<int> is a distinct runtime type from List<string>. Best of both worlds. Cost: more complex runtime.

Rust's monomorphization is why generics are zero-cost: the compiler generates optimal code per type, identical to what you'd write by hand.
