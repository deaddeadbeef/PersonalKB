---
tags: [chunk, programming-languages, modules]
source: "[[raw-pl-008]]"
---

# chunk-pl-022 Dependency Management Quality Spectrum

Dependency management quality often matters more than language features:

**Cargo (Rust):** Gold standard. Builds, tests, benchmarks, publishes, docs — all integrated. Cargo.toml declarative config. Feature flags. Workspaces for monorepos. Crates are immutable once published.

**npm (JS):** 2M+ packages, largest registry. Semantic versioning with ranges. Nested dependencies solve version conflicts at cost of node_modules size. Supply chain security concerns.

**Go modules:** URL-based dependencies. Minimum version selection for reproducibility. Import compatibility rule (v2+ = different path). No central registry.

**pip/poetry/uv (Python):** Fragmented ecosystem converging toward Cargo-like experience. Virtual environments, no standard lock file format until recently.

**Maven/Gradle (Java):** Mature but complex. Transitive dependency resolution causes classpath hell.

The reproducibility problem: lock files help but don't solve system libraries, compiler versions, and platform differences. Nix attempts complete reproducibility.
