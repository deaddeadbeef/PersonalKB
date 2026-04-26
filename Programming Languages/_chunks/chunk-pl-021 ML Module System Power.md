---
tags: [chunk, programming-languages, modules]
source: "[[raw-pl-008]]"
---

# chunk-pl-021 ML Module System Power

The ML module system (OCaml, SML) is the most powerful in any practical language:

**Structures:** Concrete modules — types, values, sub-modules. Like records at the module level.

**Signatures:** Module types/interfaces. Can make types **abstract** — code outside can use the type but can't see implementation. Strongest encapsulation in any language.

**Functors:** Functions from modules to modules. Set.Make(String) produces a string set. Map.Make(Int) produces an int-keyed map. Module-level generics more powerful than type-level generics.

**First-class modules (OCaml):** Pack modules into values, unpack at runtime. Enables runtime implementation selection.

Why other languages don't have this: ML modules involve dependent typing concepts, sharing constraints, and higher-order functors. Most languages chose simpler mechanisms (traits, interfaces, type classes) trading power for lower learning curve.
