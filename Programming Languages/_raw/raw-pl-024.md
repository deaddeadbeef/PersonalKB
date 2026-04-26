---
tags: [raw, programming-languages, tooling-ecosystem]
source: "Various package manager documentation, build tool documentation"
created: 2025-07-25
---

# raw-pl-024: Developer Tooling and Ecosystem Quality

## Build Systems

**Cargo (Rust):** The gold standard. Builds, tests, benchmarks, publishes, generates docs — all in one tool. Cargo.toml for declarative config. Build scripts (build.rs) for custom compilation steps. Feature flags for conditional compilation. Workspaces for monorepos.

**Go toolchain:** go build, go test, go run, go mod — all built in. No external build tool needed. Fast by design. go vet for static analysis, go fmt for formatting (non-negotiable), go doc for documentation.

**npm/yarn/pnpm (JS/TS):** package.json + scripts. Flexible but chaotic. Multiple competing package managers. node_modules is notoriously large. Lock files (package-lock.json, yarn.lock) pin versions.

**Maven/Gradle (Java):** Maven: XML-based, convention-over-configuration. Gradle: Groovy/Kotlin-based, more flexible. Both handle dependency resolution from Maven Central. Build times can be long for large projects.

## Formatters and Linters

**gofmt (Go):** The first non-negotiable formatter. One style, no configuration. Ended all formatting debates in Go. "Gofmt's style is no one's favorite, yet gofmt is everyone's favorite."

**rustfmt (Rust):** Similar to gofmt but with some configuration. cargo fmt formats the entire project.

**Black (Python):** "The uncompromising formatter." Minimal configuration. Increasingly standard.

**Prettier (JS/TS):** Opinionated formatter for JS, TS, CSS, HTML, JSON, Markdown.

**clippy (Rust):** Linter with hundreds of checks. Catches common mistakes, suggests idiomatic code. More opinionated than rustfmt.

## IDE Support

**JetBrains IDEs:** Best-in-class for Java (IntelliJ), Python (PyCharm), Go (GoLand), Rust (RustRover), and Kotlin (built into IntelliJ). Refactoring, navigation, debugging, profiling.

**VS Code:** Dominant for web development (JS/TS), Go, Rust (via rust-analyzer), Python. Extension ecosystem. Language Server Protocol (LSP) enables consistent IDE features across languages.

**rust-analyzer:** LSP server for Rust. Real-time type checking, completion, inline type hints, refactoring. A significant contributor to Rust's developer experience.

## Package Registries and Ecosystems

Ecosystem size matters enormously:
- **npm (JS):** 2M+ packages. Largest, but quality varies wildly. Supply chain concerns.
- **PyPI (Python):** 500K+ packages. Strong in data science, ML, web.
- **crates.io (Rust):** 140K+ packages. Smaller but high quality. Good documentation culture.
- **Maven Central (Java):** 550K+ artifacts. Enterprise ecosystem. Spring, Hibernate, Jakarta EE.
- **RubyGems:** 170K+ gems. Rails-centric ecosystem.
- **Go modules:** No central count. URL-based. Minimal ecosystem compared to npm/PyPI.
