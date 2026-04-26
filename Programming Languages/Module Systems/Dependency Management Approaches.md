---
tags: [programming-languages, module-systems, dependency-management]
up: "[[Module Systems Overview]]"
tier-coverage: full
---

# Dependency Management Approaches

## 🎯 Intuition

**The Core Idea:** How a language discovers, versions, resolves, and builds external dependencies determines everyday developer productivity and long-term project health.

**Analogy:** Dependency management is like supply-chain logistics for code — each registry is a warehouse, each lock file is a shipping manifest with exact part numbers, and version resolution is the dispatcher deciding which parts are compatible.

**Why It Matters:** The quality of a language's dependency management ecosystem is often more important than the language's technical merits. A great language with broken dependency management loses to a decent language with polished tooling.

## ⚙️ Core Mechanics

### Centralized Registries

**npm (JavaScript/TypeScript):** The largest package registry (2M+ packages). Uses semantic versioning with version ranges. package.json declares dependencies; package-lock.json locks exact versions. npm's early design allowed nested dependencies (different versions of the same package in one project), solving "dependency hell" at the cost of node_modules size.

**crates.io (Rust):** Cargo is widely considered the gold standard for dependency management. Cargo.toml declares dependencies with semantic version requirements; Cargo.lock pins exact versions. Cargo handles: downloading, building (with correct feature flags), linking, and documentation generation. Crates are immutable once published.

**PyPI (Python):** pip installs packages from PyPI. Python's dependency management has been historically problematic: no lock file standard (until pip freeze/pip-tools/poetry/pdm), global vs virtual environments, and the setuptools/distutils/flit/poetry fragmentation. Modern tools (Poetry, PDM, uv) are converging toward a Cargo-like experience.

**Maven Central (Java/Kotlin):** Maven and Gradle resolve dependencies from Maven Central. Uses group:artifact:version coordinates. The Java ecosystem relies heavily on transitive dependency resolution, which can cause version conflicts (classpath hell). Gradle's dependency resolution is more sophisticated than Maven's.

### Go Modules

Go took a unique approach: dependencies are referenced by URL (github.com/user/repo) and managed via go.mod files. Go enforces **minimum version selection** — instead of resolving to the newest compatible version, Go uses the minimum version satisfying all requirements. This makes builds more reproducible at the cost of occasionally using older versions.

Go also has the **import compatibility rule:** if v2+ of a package breaks backward compatibility, it must use a different import path (github.com/user/repo/v2). This eliminates the "major version upgrade breaks everything" problem.

### Haskell Cabal and Stack

Haskell has two competing dependency managers: Cabal (the original) and Stack (which uses curated package sets called Stackage). Haskell's type system means dependency conflicts can create type-level incompatibilities — a problem unique to languages with such rich type systems.

### OCaml opam

OCaml's opam package manager manages packages and compiler versions. opam uses a constraint solver to find compatible package versions. The OCaml ecosystem is smaller than Rust's or JavaScript's but well-curated. opam switch allows multiple OCaml compiler versions to coexist.

### Zig: No Package Manager (By Design)

Zig deliberately has no centralized package registry. Dependencies are fetched by URL (git or tarball) and pinned by hash in build.zig.zon. The philosophy: a centralized registry creates a single point of failure and a trust problem. Zig prefers decentralized, hash-verified dependencies.

## 🔬 Deep Dive

### Trade-offs and Historical Context

#### The Reproducibility Problem

All dependency management systems struggle with reproducibility: given the same source code, will you get the same build? Lock files help but don't solve: system libraries, compiler versions, build tool versions, and platform differences. Nix (the package manager, not the language) attempts to solve this completely by making every dependency — including the compiler and OS libraries — content-addressed and reproducible.

#### Centralized vs Decentralized

Centralized registries (npm, crates.io, PyPI, Maven Central) trade convenience for a single point of failure and a trust problem. Decentralized approaches (Go modules by URL, Zig by hash-pinned URL) avoid the registry bottleneck but lose discoverability. Go's hybrid — URLs as identifiers, proxy.golang.org as a cache — balances both concerns.

#### Version Selection Strategies

Most tools use a SAT-solver approach: find the newest compatible set of versions. Go's minimum version selection is the outlier — it's simpler, more predictable, and more reproducible, but may leave security patches unapplied until explicitly upgraded. Haskell's Stackage takes a third path: curated, tested-together snapshots that sidestep resolution entirely.

## 🏋️ Practice

**Exercise 1 — Registry Comparison Table:** Create a comparison table of npm, Cargo, pip, and Maven along these axes: lock file format, version resolution strategy, mutability of published packages, and monorepo support. Identify which registry best handles each axis and why.

**Exercise 2 — Minimum Version Selection Simulation:** Given three packages A, B, C where A requires B ≥ 1.2 and C requires B ≥ 1.5 and B has versions 1.2, 1.5, 1.8, 2.0: determine which version of B is selected under (a) npm's default strategy, (b) Go's minimum version selection, and (c) a Stackage-like curated set that includes B 1.8. Explain the trade-offs of each outcome.

**Exercise 3 — Reproducibility Audit:** Take a real project (any language) and attempt to build it from scratch on a clean machine. Document every implicit dependency (system libraries, compiler version, build tools) that isn't captured in the project's dependency specification. Propose how Nix-style content-addressing would solve each gap.

## References

- [[Sources Index]]
