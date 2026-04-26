---
tags: [chunk, programming-languages, ecosystem]
source: "[[raw-pl-024]]"
---

# chunk-pl-116 IDE and LSP Ecosystem

**Language Server Protocol (LSP):** Microsoft's protocol standardizing IDE features. One language server serves VS Code, Neovim, Emacs, JetBrains. Features: autocomplete, go-to-definition, find references, rename, diagnostics.

**Notable language servers:**
- **rust-analyzer:** Exemplary. Real-time type checking, inline type hints, refactoring. Significantly contributes to Rust's developer experience.
- **gopls:** Go's official language server. Fast, complete. Integrated with gofmt, go vet.
- **TypeScript language service:** Powers VS Code's JavaScript/TypeScript support. The gold standard for web development tooling.
- **Pyright/Pylsp:** Python type checking and completion. Pyright (Microsoft) is faster and stricter.
- **clangd:** C/C++ language server from the LLVM project.
- **ocaml-lsp:** OCaml language server. Merlin-based. Good but smaller community.

**JetBrains IDEs:** Don't use LSP — proprietary analysis engines. Often better than LSP-based tooling for: Java (IntelliJ), Kotlin, Python (PyCharm), Go (GoLand), Rust (RustRover). Deep refactoring, debugging, profiling integration.

**The tooling advantage:** Languages with great tooling (Rust, TypeScript, Kotlin, Go) attract developers. Poor tooling is a major barrier to adoption, regardless of language merit.
