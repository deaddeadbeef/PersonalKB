---
tags: [pl, chunk, build-systems, tooling]
up: "[[Compilation and Runtime Overview]]"
---

# Integrated Toolchains The Cargo Revolution

Cargo (Rust's build system and package manager) set a new standard for language tooling that influenced every language designed after it.

## What Cargo Got Right
1. **Single tool:** build, test, publish, format (via rustfmt), lint (via clippy), benchmark, doc
2. **Declarative config:** TOML-based Cargo.toml - no Turing-complete build scripts needed for 95% of projects
3. **Reproducible builds:** Cargo.lock pins exact versions
4. **Integrated registry:** crates.io is the single source of truth
5. **Workspace support:** Monorepo-friendly multi-crate workspaces
6. **Cross-compilation:** --target flag for any supported platform

## The Fragmentation Problem (Counter-Examples)

**C/C++:** No standard build system
- CMake (de facto standard) is powerful but notoriously complex
- Meson, Bazel, Ninja, Make all compete
- No standard package manager
- Result: Onboarding a new C++ project can take hours

**JavaScript/TypeScript:** Too many tools
- Package managers: npm, yarn, pnpm, bun
- Bundlers: webpack, vite, esbuild, turbopack, rollup, parcel
- Test runners: jest, vitest, mocha, ava
- Linters: eslint
- Result: "JavaScript fatigue" is recognized phenomenon

**Python:** Evolving rapidly
- Package managers: pip, poetry, pdm, hatch, uv
- Virtual envs: venv, virtualenv, conda, pyenv
- Build systems: setuptools, flit, maturin
- Result: "Which Python tool?" is a FAQ

## Key Insight
Cargo proved that excellent integrated tooling is a competitive advantage as important as language features. The "cargo new, cargo build, cargo test, cargo publish" workflow sets developer expectations that older ecosystems struggle to match.

## References
-> [[Sources Index]]
