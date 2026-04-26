---
tags: [raw, programming-languages, modules]
source: "Programming Language Pragmatics (Scott, 2015), OCaml Manual"
created: 2025-07-25
---

# raw-pl-008: Module Systems and Code Organization

## Why Modules Matter

Module systems determine: how code is organized, how dependencies are managed, how names are scoped, how abstractions are enforced, and how separately compiled units interact. A great module system enables large-scale software development; a poor one makes large codebases unmaintainable.

## The ML Module System

OCaml/SML modules are the most powerful in any practical language:

**Structures:** Concrete modules containing types, values, sub-modules. Like records at the module level.

**Signatures:** Module types (interfaces). Can make types abstract — code outside the module can use the type but can't see its implementation. This is the strongest encapsulation in any language.

**Functors:** Functions from modules to modules. Set.Make(String) produces a set of strings. Map.Make(Int) produces a map with int keys. Functors enable parameterized libraries that Rust traits and Java generics can approximate but not fully match.

First-class modules (OCaml): modules can be packed into values and unpacked, enabling runtime module selection.

## Rust Crates and Modules

Two levels: crates (compilation/dependency units, published to crates.io) and modules (organizational units within a crate). pub controls visibility: pub, pub(crate), pub(super), pub(in path). The module tree is explicit — you declare modules; files aren't auto-included.

Cargo + crates.io is widely considered the best dependency management system: semantic versioning, lock files, feature flags, documentation generation, and builds — all integrated.

## Go Packages

One directory = one package. Exported names start with uppercase. No circular dependencies. Import paths are URLs (github.com/user/repo). go.mod with minimum version selection for reproducible builds.

Go's package simplicity is a deliberate design choice: packages are easy to understand but limited in abstraction power compared to ML modules or Rust crates.

## Java Packages and Modules

Packages map to directory hierarchy. Four visibility levels: public, protected, package-private, private. Java 9 added the Module System (JPMS): module-info.java declares exports and requires. JPMS adds a coarse-grained encapsulation layer above packages.

## JavaScript Module Evolution

No modules (global scope) → CommonJS (require/module.exports, Node.js) → AMD (browser async) → ES Modules (import/export, the standard). ES Modules are static (analyzable for tree-shaking), unlike CommonJS's dynamic require().

## Python Modules

Each .py file is a module. Directories with __init__.py are packages. Dynamic module system: import-time code execution, runtime module modification, monkey-patching. Simple but: no encapsulation enforcement, circular import hazards, __init__.py complexity.

## Dependency Management

The quality of dependency management often matters more than language features:
- **Cargo (Rust):** Gold standard. Integrated build, test, publish, documentation.
- **npm (JS):** Largest registry. Nested dependencies solve version conflicts at cost of size.
- **Go modules:** URL-based, minimum version selection, no central registry.
- **pip/poetry/uv (Python):** Fragmented ecosystem, converging toward Cargo-like experience.
- **Maven/Gradle (Java):** Mature but complex. Transitive dependency resolution can cause classpath hell.
