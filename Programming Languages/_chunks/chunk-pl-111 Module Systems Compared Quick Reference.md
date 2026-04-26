---
tags: [chunk, programming-languages, module-comparison]
source: "[[raw-pl-008]]"
---

# chunk-pl-111 Module Systems Compared Quick Reference

**C:** Header files (#include). Textual inclusion. No encapsulation. Slow compilation. C++20 modules improving.

**Java:** Packages (directories) + access modifiers (public/protected/private). JPMS modules (Java 9) for coarse-grained encapsulation.

**Go:** Packages (one directory = one package). Uppercase = exported. No circular dependencies. Simple, limited.

**Python:** Files as modules. Directories with __init__.py as packages. No enforced encapsulation (_convention).

**Rust:** Crates (compilation units) + modules (organizational). pub/pub(crate)/private. Explicit module tree. Cargo for dependency management.

**OCaml:** Files as modules automatically. .mli for signatures (interfaces). Functors for parameterized modules. Abstract types for strongest encapsulation.

**JavaScript:** ES Modules (import/export, static). CommonJS (require, dynamic, Node.js). Tree-shaking with ES Modules.

**Haskell:** Module system with explicit exports. import qualified for namespacing. Type classes span modules (open world).

Winner for encapsulation: OCaml (abstract types). Winner for simplicity: Go. Winner for dependency management: Rust (Cargo).
