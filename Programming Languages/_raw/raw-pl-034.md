---
tags: [pl, raw, ide, developer-experience, lsp]
up: "[[Sources Index]]"
---

# Raw Note 034 — IDE Support and Developer Experience

## Language Server Protocol (LSP)

LSP (created by Microsoft for VS Code) revolutionized language tooling by decoupling language intelligence from editors:

### Before LSP
- Each editor needed a language-specific plugin (M editors x N languages = M*N plugins)
- IntelliJ had the best Java support; Emacs had the best Lisp support; etc.

### After LSP
- One language server serves all editors (M + N implementations)
- Language teams maintain one server; editor teams maintain one client

### LSP Implementation Quality

| Language | Server | Quality | Notable Features |
|----------|--------|---------|-----------------|
| Rust | rust-analyzer | Excellent | Inline type hints, macro expansion, assist actions |
| TypeScript | tsserver | Excellent | Deep type inference, refactoring |
| Go | gopls | Excellent | Fast, well-integrated with go toolchain |
| Python | Pylance/pyright | Very good | Type checking, auto-imports |
| C/C++ | clangd | Very good | Compile-commands integration |
| Java | Eclipse JDT LS | Good | Used by VS Code Java extension |
| Haskell | HLS | Good | Improving rapidly |
| OCaml | ocaml-lsp | Good | Merlin-based |
| Zig | ZLS | Good | Comptime-aware |
| Erlang | erlang_ls | Fair | Newer, growing |

## Developer Experience (DX) Spectrum

### Excellent DX
- **Rust:** cargo + rust-analyzer + clippy + rustfmt = seamless workflow
- **Go:** go tool + gopls + gofmt + delve = simple and complete
- **TypeScript:** tsserver + prettier + eslint = rich ecosystem

### Good DX
- **Python:** pyright + black + pytest, but virtual env management is painful
- **Kotlin:** IntelliJ-native, excellent in JetBrains IDEs, decent elsewhere
- **Swift:** Xcode integration excellent, non-Apple platform DX is weaker

### Challenging DX
- **C++:** Complex build systems, slow compilation, fragmented tooling
- **Haskell:** Stack vs Cabal confusion, slow builds, steep learning
- **Erlang:** Niche editor support, rebar3 complexity

## Error Messages

Quality of error messages dramatically affects learning curves:

- **Rust:** Gold standard — explains the error, suggests fixes, links to docs
- **Elm:** Pioneered friendly errors, inspired Rust's approach
- **Go:** Clear but terse
- **C++:** Template errors are notoriously impenetrable
- **Haskell:** Type errors can be cryptic for beginners
- **TypeScript:** Generic type errors can explode into walls of text

## REPL-Driven Development
- **Lisp/Clojure:** REPL is the primary development interface
- **Python:** Jupyter notebooks = visual REPL for data science
- **Haskell:** GHCi enables type exploration
- **OCaml:** utop provides rich REPL with auto-complete
- **Elixir:** IEx with runtime introspection
- **Rust/Go/Java:** No traditional REPL (compiled languages)

## References
→ [[Sources Index]]
