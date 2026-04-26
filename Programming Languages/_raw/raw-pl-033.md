---
tags: [pl, raw, build-systems, toolchains]
up: "[[Sources Index]]"
---

# Raw Note 033 — Build Systems and Toolchains

## Integrated vs External Build Systems

### Language-Integrated (Blessed) Tools
Modern languages ship with official tooling:
- **Rust:** cargo (build, test, publish, format, lint) — gold standard
- **Go:** go build/test/vet/fmt — batteries included, no config files
- **Zig:** zig build — also serves as a C/C++ cross-compiler
- **Deno:** deno (runtime + bundler + formatter + linter + test)
- **Swift:** Swift Package Manager (SPM)

### External Build Systems
Older languages rely on ecosystem tools:
- **C/C++:** Make, CMake, Bazel, Meson, Ninja — fragmented landscape
- **Java:** Maven, Gradle, Ant (legacy) — XML/Groovy/Kotlin DSL configs
- **Python:** setuptools, pip, poetry, hatch, pdm — still evolving
- **JavaScript:** npm/yarn/pnpm + webpack/vite/esbuild/turbopack — complex ecosystem
- **Haskell:** Cabal, Stack — two competing tools

## Toolchain Components

| Component | Purpose | Examples |
|-----------|---------|---------|
| Compiler/Interpreter | Source → executable | gcc, rustc, javac, cpython |
| Build system | Orchestrate compilation | cargo, cmake, gradle |
| Package manager | Dependency resolution | npm, pip, cargo, nuget |
| Formatter | Code style enforcement | gofmt, rustfmt, prettier, black |
| Linter | Static analysis | clippy, eslint, pylint, golangci-lint |
| Test runner | Execute tests | cargo test, pytest, jest, go test |
| REPL | Interactive evaluation | python, ghci, node, utop (OCaml) |
| Debugger | Runtime inspection | gdb, lldb, delve (Go) |
| LSP server | IDE integration | rust-analyzer, gopls, tsserver |

## Opinionated Formatters

Languages that ship official formatters have ended style debates:
- **gofmt** (Go) — the pioneer, "gofmt's style is nobody's favorite, but gofmt is everybody's favorite"
- **rustfmt** (Rust) — configurable but with strong defaults
- **black** (Python) — "the uncompromising formatter"
- **prettier** (JS/TS) — multi-language, opinionated
- **zig fmt** (Zig) — built into the compiler

Languages without official formatters suffer from style fragmentation (C++, Java before google-java-format).

## Cross-Compilation

| Language | Cross-Compile | Ease |
|----------|--------------|------|
| Rust | cargo build --target | Excellent — many targets |
| Go | GOOS=linux GOARCH=arm64 go build | Excellent — trivial |
| Zig | zig build -Dtarget= | Excellent — also cross-compiles C |
| C/C++ | Complex toolchain setup | Poor — sysroot, cross-compiler needed |
| Java | N/A (JVM portable) | N/A — runs on any JVM |

## Key Insight
Language success increasingly depends on tooling quality. Rust and Go proved that great integrated tooling drives adoption. The JavaScript ecosystem's tooling fragmentation (webpack → vite, npm → yarn → pnpm) creates cognitive overhead that deters new developers.

## References
→ [[Sources Index]]
