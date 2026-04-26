---
tags: [chunk, programming-languages, tooling]
source: "[[raw-pl-024]]"
---

# chunk-pl-047 Build Systems and Developer Tooling

**Cargo (Rust):** Gold standard. Builds, tests, benchmarks, publishes, generates docs — one tool. Feature flags, workspaces for monorepos, build scripts.

**Go toolchain:** All built in: go build, go test, go run, go mod, go fmt, go vet, go doc. No external tools needed. Fast by design.

**npm/yarn/pnpm (JS):** Flexible but chaotic. Multiple competing managers. node_modules notoriously large. Lock files for pinning.

**Maven/Gradle (Java):** Mature, complex. XML (Maven) or Kotlin/Groovy (Gradle) config. Dependency resolution from Maven Central.

**Formatters that ended debates:** gofmt (Go, non-negotiable), rustfmt (Rust), Black (Python), Prettier (JS/TS). Opinionated formatters eliminate style arguments.

**IDE support:** JetBrains (best for Java, Python, Go, Rust, Kotlin), VS Code + LSP (dominant for web dev, extensible). rust-analyzer: real-time type checking, completion, inline hints. Language Server Protocol enables consistent IDE features across languages.
