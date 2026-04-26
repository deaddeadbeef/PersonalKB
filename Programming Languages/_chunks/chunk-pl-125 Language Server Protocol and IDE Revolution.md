---
tags: [pl, chunk, lsp, ide, developer-experience]
up: "[[Compilation and Runtime Overview]]"
---

# Language Server Protocol and IDE Revolution

LSP (Language Server Protocol) democratized language intelligence. Before LSP, every editor needed custom plugins for every language. After LSP, one server serves all editors.

## Impact on Language Adoption

LSP changed the economics of language tooling:
- **Before:** A new language needed IDE plugins for Vim, Emacs, VS Code, IntelliJ, etc.
- **After:** Build one LSP server, get support in every LSP-compatible editor

This lowered the barrier for new languages:
- **rust-analyzer** is widely considered the best LSP implementation
- **gopls** unified Go tooling across editors
- **Zig's ZLS** gave a young language competitive IDE support immediately

## LSP Feature Tiers

**Tier 1 (Basic):** Go to definition, find references, hover info, completion
**Tier 2 (Intermediate):** Rename refactoring, code actions, diagnostics, formatting
**Tier 3 (Advanced):** Inline type hints, semantic highlighting, call hierarchy, code lens

| Language Server | Tier | Standout Feature |
|-----------------|------|-----------------|
| rust-analyzer | 3 | Macro expansion, inline hints, assists |
| tsserver | 3 | Deep type narrowing, refactoring |
| gopls | 2-3 | Fast, integrated with go toolchain |
| clangd | 2-3 | Compile commands, cross-reference |
| Pylance | 2-3 | Type inference, auto-imports |
| HLS (Haskell) | 2 | Type hole suggestions |

## Key Insight
LSP is one of the most impactful standards in modern software development. It decoupled language intelligence from editor choice, enabling a Cambrian explosion of language tooling. A language without a good LSP server in 2025 is at a serious adoption disadvantage.

## References
-> [[Sources Index]]
