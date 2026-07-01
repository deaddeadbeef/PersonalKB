---
tags: [programming-languages, module-systems, packages]
up: "[[Module Systems Overview]]"
confidence: established
freshness: stable
tier-coverage: full
confidence: plausible
---
# Package and Namespace Systems

## 🎯 Intuition

**The Core Idea:** Packages and namespaces group related code under a hierarchical name, preventing collisions and providing organisational structure — the most common module mechanism across languages.

**Analogy:** Packages are like the postal addressing system for code — country (org), city (project), street (sub-package), house number (module). Just as no two houses share the same full address, no two symbols share the same fully-qualified name. Different languages choose different levels of address granularity.

**Why It Matters:** The details of how packages map to files, enforce visibility, and handle naming conventions vary significantly across languages, directly affecting how teams organise, navigate, and scale codebases.

## ⚙️ Core Mechanics

### Java Packages

Java packages map to directory structure: `com.example.app.model` corresponds to `com/example/app/model/`. Each file declares its package; classes within a package can access each other's package-private members. Java's convention of reverse-domain-name packages (`com.google`, `org.apache`) ensures global uniqueness.

**Strengths:** Clear physical organisation, globally unique names, IDE navigation.
**Weaknesses:** Deep hierarchy (`AbstractBeanFactoryAwareAdvisorAutoProxyCreator` lives in a 6-level package), no way to split a logical module across multiple packages without losing package-private access.

### Go Packages

Go packages are simpler: a package is a directory. All `.go` files in a directory belong to the same package. Visibility is controlled by capitalisation — exported names start with an uppercase letter; unexported names start with lowercase.

Go's package system is distinctive: no circular dependencies allowed (enforced by the compiler), packages are the unit of compilation, and the import path is the canonical package identifier (e.g., `github.com/user/repo/pkg`).

### Python Modules and Packages

Python's module system is file-based: each `.py` file is a module. A directory with `__init__.py` is a package. Imports are simple: `import math`, `from os.path import join`, `from . import sibling` (relative imports).

**Strengths:** Simple mental model, dynamic (can import at runtime, patch modules).
**Weaknesses:** No encapsulation (underscore prefix `_private` is convention, not enforced), circular import issues, `__init__.py` executing on import can cause surprises.

### Rust Crates and Modules

Rust has a two-level system:
- **Crate:** The compilation unit and dependency unit. A crate is a library or binary published to crates.io.
- **Module:** Organisational unit within a crate. `mod` declares a module; `pub` exports items.

Rust modules can be defined inline or in separate files. The module tree is explicit — you must declare `mod foo;` to include a file. This avoids the "everything in the directory is included" ambiguity of some languages.

### C++ Namespaces and Modules (C++20)

C++ traditionally used header files (`#include`) and namespaces for organisation. Header files are textual inclusion — the preprocessor copies header content into every file that includes it, causing slow compilation and fragile dependencies.

C++20 modules replace headers with proper module declarations: `export module math;` defines a module; `import math;` uses it. Modules are parsed once (not re-parsed per inclusion), dramatically improving build times. Adoption is still early (2024).

### JavaScript/TypeScript Modules

JavaScript evolved through multiple module systems:
- **No modules (early JS):** Everything in global scope. Script tags concatenated.
- **CommonJS (Node.js):** `require()` and `module.exports`. Synchronous, file-based.
- **ES Modules (standard):** `import`/`export`. Static, analysable, supports tree-shaking.
- **AMD, UMD:** Legacy browser module formats, largely superseded by ES Modules.

TypeScript adds: type-only imports (`import type`), module augmentation, and declaration files (`.d.ts`) for describing external JavaScript modules' types.

### OCaml: Files as Modules

In OCaml, every source file is automatically a module named after the file. `list.ml` defines a module `List`. Module interfaces are defined in `.mli` files (signatures). No explicit `export` or `import` — all top-level definitions in a module are accessible unless restricted by a signature.

OCaml's approach: modules are the fundamental organising principle. Files, libraries, and functors all use the same module language. See [[ML Module System and Functors]] for the advanced features.

## 🔬 Deep Dive

### Trade-offs and Historical Context

#### File-System Coupling

Java enforces a strict package-to-directory mapping; Go uses a simpler one-directory-one-package rule; Python requires `__init__.py` markers; Rust lets you choose inline or file-based modules. C++ historically had no mapping at all (header files are just textual inclusion). The trend is toward explicit but flexible mapping — Rust's `mod` declarations balance clarity with developer choice.

#### Naming Conventions and Global Uniqueness

Java's reverse-domain convention (`com.google.common`) scales globally but creates deep hierarchies. Go's URL-based import paths (`github.com/user/repo`) piggyback on existing infrastructure. Python and JavaScript rely on registry-assigned unique names (PyPI, npm). The tension is always between global uniqueness and local ergonomics.

#### The Evolution of JavaScript Modules

JavaScript's module history — from global scripts, through CommonJS and AMD, to ES Modules — is a case study in retrofitting modularity. Each transition broke backward compatibility and tooling. The lesson: building module support into a language from the start (Rust, Go) avoids years of ecosystem fragmentation.

## 🏋️ Practice

**Exercise 1 — Package Layout Comparison:** Design a small "shapes" library (Circle, Rectangle, Triangle with area/perimeter methods) in Java, Go, and Rust. Map out the directory structure, file names, and visibility declarations for each. Which language requires the most boilerplate? Which gives the finest-grained visibility control?

**Exercise 2 — Circular Dependency Detection:** In Python, create three modules A, B, C where A imports B, B imports C, and C imports A. Observe the resulting ImportError. Then restructure to eliminate the cycle using one of: (a) dependency inversion, (b) lazy imports, (c) extracting shared code into a fourth module D. Explain why Go's compiler rejects circular dependencies outright and whether that is a net benefit.

**Exercise 3 — C++20 Modules Migration:** Take a small C++ project using header files and refactor it to use C++20 modules. Measure compilation time before and after. Document which patterns (macros, textual inclusion tricks, header-only libraries) were hardest to migrate and why.

## References

- [[Programming Languages/Sources/Sources Index|Sources Index]]
