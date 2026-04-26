---
tags: [pl, chunk, modules, monorepo]
up: "[[Dependency Management]]"
---

# Monorepo vs Multi-Repo Language Tooling Impact

How a language's build system handles multiple packages significantly affects large-scale development practices.

## Monorepo-First Languages

### Rust Workspaces
`	oml
# Root Cargo.toml
[workspace]
members = ["api", "core", "cli", "shared"]
`
- All crates share one Cargo.lock (consistent dependency versions)
- cargo build builds everything; cargo test tests everything
- Changes across crates are atomic

### Go Modules (Multi-Module Workspaces)
`
go work init ./api ./core ./cli
`
- Go 1.18+ workspace mode for multi-module development
- Natural fit for monorepo (Google's internal model)
- go.work coordinates local module replacements

### Bazel (Language-Agnostic)
Google's build system designed for monorepos:
- Hermetic builds (every input specified)
- Incremental: only rebuilds what changed
- Used by Google (billions of LOC), Meta, Uber
- Supports Java, Go, Python, C++, Rust

## Multi-Repo Languages

### npm/JavaScript
- Each package is typically its own repo
- npm workspaces and tools like Nx/Turborepo add monorepo support
- Lerna (deprecated) pioneered JS monorepo tooling

### Python
- pip doesn't natively support monorepos
- Tools like pants, poetry workspaces, uv workspaces emerging
- pyproject.toml is evolving to support workspaces

## Impact on Development

| Factor | Monorepo | Multi-Repo |
|--------|----------|------------|
| Cross-cutting changes | Atomic (one PR) | Multiple PRs, coordination |
| Dependency consistency | Guaranteed (one lockfile) | Possible version drift |
| CI complexity | Needs smart incremental CI | Simpler per-repo CI |
| Code discovery | Easy (everything in one place) | Harder (which repo?) |
| Scale | Needs specialized tooling | Git works naturally |

## Key Insight
Languages with built-in workspace/monorepo support (Rust, Go) make large-scale development significantly easier. JavaScript's monorepo tooling (Nx, Turborepo) is catching up but adds complexity. The trend is toward monorepo-friendly build systems, driven by the success of Google's and Meta's monorepo practices.

## References
→ [[Sources Index]]
