---
tags: [programming-languages, module-systems]
up: "[[Programming Languages]]"
confidence: plausible
---
# Module Systems Overview

A module system determines how code is organized, how dependencies are managed, how names are scoped, and how abstractions are enforced at scale. While type systems get more attention, module systems are equally important for building large programs — they determine whether a codebase remains maintainable as it grows.

## What Module Systems Provide

1. **Namespacing:** Prevent name collisions between independent code units
2. **Encapsulation:** Hide implementation details, expose only public interfaces
3. **Separate compilation:** Compile modules independently for faster builds
4. **Dependency management:** Express what a module needs from other modules
5. **Abstraction:** Define interfaces separately from implementations

## The Spectrum

| Approach | Encapsulation | Abstraction Power | Languages |
|----------|--------------|-------------------|-----------|
| Header files | Weak (convention-based) | None | C, C++ |
| Packages | Medium (visibility modifiers) | Low | Java, Go, Kotlin |
| ML modules | Very strong (signatures) | Very high (functors) | OCaml, Standard ML |
| Type classes | Medium | High | Haskell |
| Crate system | Strong (pub/private) | Medium | Rust |
| Dynamic modules | Weak | Low | Python, Ruby, JavaScript |

## In This Hub

- [[Package and Namespace Systems]]
- [[ML Module System and Functors]]
- [[Visibility and Access Control]]
- [[Dependency Management Approaches]]
- [[Import and Export Mechanisms]]

## References

- [[Sources Index]]
