---
tags: [pl, raw, packages, registries]
up: "[[Sources Index]]"
---

# Raw Note 036 — Package Ecosystems and Registry Design

## Major Package Registries

| Registry | Language | Packages | Model |
|----------|----------|----------|-------|
| npm | JavaScript/TypeScript | 2.5M+ | Open publish, scoped packages |
| PyPI | Python | 500K+ | Open publish, namespace flat |
| crates.io | Rust | 140K+ | Open publish, immutable versions |
| Maven Central | Java/Kotlin/Scala | 500K+ | Group ID namespacing |
| NuGet | C#/F#/.NET | 380K+ | Open publish, .NET ecosystem |
| RubyGems | Ruby | 175K+ | Open publish, gem format |
| Hackage | Haskell | 17K+ | Community curated |
| opam | OCaml | 4K+ | Community curated |
| Hex | Erlang/Elixir | 16K+ | Immutable, well-designed API |
| Go modules | Go | Decentralized | Module proxy, checksum DB |
| Swift PM | Swift | Growing | Git-based, no central registry (until recently) |

## Design Decisions

### Naming and Namespacing
- **Flat namespace** (npm, crates.io, PyPI): first-come-first-served, squatting risk
- **Scoped/grouped** (npm @scope, Maven groupId, NuGet): organization-based, less collision
- **Decentralized** (Go modules): URL-based import paths, no central registry needed

### Immutability
- **crates.io, Hex:** Published versions can never be changed or deleted (yanked only)
- **npm:** Unpublish allowed within 72 hours (learned from left-pad incident)
- **PyPI:** Deletion allowed, has caused breakage

### Security
- **npm:** Provenance attestations, 2FA for publish, audit command
- **crates.io:** Immutability provides some protection, advisory database
- **PyPI:** Trusted Publishers (OIDC), mandatory 2FA for critical projects
- **Go:** Checksum database prevents tampering, GOPROXY caching

### Dependency Resolution
- **SAT solver** (Cargo, Pub): mathematical satisfiability for version constraints
- **Peer dependencies** (npm): consumer resolves shared dependencies
- **Lock files** (all modern managers): reproducible builds via pinned versions

## Supply Chain Attacks
Major incidents that shaped security practices:
- **left-pad (2016):** npm author unpublished, broke thousands of builds
- **event-stream (2018):** Maintainer transfer led to malicious code injection
- **ua-parser-js (2021):** Account compromise, crypto miner injected
- **colors/faker (2022):** Author intentionally sabotaged own packages
- **xz utils (2024):** Multi-year social engineering attack on compression library

## Quality Indicators

| Factor | Best Practice | Example |
|--------|---------------|---------|
| Documentation | Auto-generated API docs | docs.rs (Rust), javadoc |
| Downloads/stars | Usage signals | npm download counts |
| Maintenance | Recent updates, CI status | crates.io last publish date |
| Type safety | Published type definitions | DefinitelyTyped, inline types |
| Audit | Vulnerability scanning | npm audit, cargo audit |

## Key Insight
Rust's crates.io and Go's module proxy represent the best modern designs: immutable publishes, cryptographic verification, and reproducible builds by default. npm's scale created problems that newer registries learned from.

## References
→ [[Sources Index]]
