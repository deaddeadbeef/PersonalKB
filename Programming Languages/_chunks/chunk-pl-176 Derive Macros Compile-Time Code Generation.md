---
tags: [pl, chunk, metaprogramming, derive-macros]
up: "[[Macro Systems]]"
---

# Derive Macros Compile-Time Code Generation

Derive macros (Rust) and annotation processors (Java, Kotlin) generate boilerplate code at compile time, eliminating the need for runtime reflection.

## Rust Derive Macros

One line replaces hundreds of lines of boilerplate:
- \Debug\ → fmt::Debug impl (pretty printing)
- \Clone\ → Clone impl (deep copy)
- \PartialEq\ → equality comparison
- \Serialize/Deserialize\ → serde serialization

### Custom Derive Macros
Define your own with #[proc_macro_derive(MyTrait)] - runs at compile time, not runtime.

## Java Annotation Processing

Lombok and similar tools process annotations during compilation, generating bytecode.

## Kotlin Compiler Plugins

kotlinx.serialization - compiler plugin, not reflection, so no reflection at runtime.

## Key Insight
Derive macros eliminate boilerplate without runtime cost. Rust's derive system is the most mature. The pattern is spreading: Kotlin's compiler plugins, C#'s source generators, and Swift's macros all follow the same principle.

## References
→ [[Sources Index]]
