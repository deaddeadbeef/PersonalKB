---
tags: [pl, chunk, modules, dependency-hell]
up: "[[Dependency Management]]"
---

# Dependency Hell and How Languages Fight It

Dependency management is one of the hardest unsolved problems in software engineering. Languages take different approaches with varying success.

## The Core Problems

### 1. Diamond Dependency
\\\
My App depends on:
  LibA v1.0 (depends on LibC v2.0)
  LibB v1.0 (depends on LibC v3.0)
// Which version of LibC do we use?
\\\

### 2. Version Incompatibility
Semantic versioning (semver) helps but doesn't solve:
- Not all libraries follow semver correctly
- Breaking changes in transitive dependencies
- "Works on my machine" with different resolved versions

### 3. Ecosystem Bloat
npm's \
ode_modules\ is infamous:
\\\
A simple React app: 1,500+ dependencies
A typical Go service: 10-50 dependencies
\\\

## How Languages Address This

### Go: Minimal Version Selection (MVS)
Go uses the MINIMUM version that satisfies all constraints:
\\\
If LibA wants LibC >= 2.0 and LibB wants LibC >= 3.0:
Go selects LibC 3.0 (minimum of what satisfies both)
\\\
- Simple and deterministic
- No SAT solver needed
- Avoids pulling in untested newer versions

### Rust: SAT Solver with Lock Files
Cargo uses a SAT solver for version resolution:
- Finds any valid version combination
- Cargo.lock pins exact versions for reproducibility
- Allows multiple semver-compatible versions of the same crate

### npm: Nested Dependencies
npm allows multiple versions of the same package:
\\\
node_modules/
  LibA/
    node_modules/
      LibC@2.0/
  LibB/
    node_modules/
      LibC@3.0/
\\\
- Avoids conflicts but creates enormous dependency trees
- "npm install creates a black hole of disk space"

### Java: Classpath Hell
JVM loads ONE version of each class:
- First one found on classpath wins
- Maven/Gradle try to resolve conflicts
- Results in \ClassNotFoundException\ or silent wrong-version bugs

## Best Practices Emerging

1. **Lock files everywhere:** Cargo.lock, package-lock.json, go.sum
2. **Dependency auditing:** cargo audit, npm audit, pip-audit
3. **Minimal dependencies:** Go community culture of few deps
4. **Vendoring:** Copying dependencies into your repo
5. **Monorepo tools:** Bazel, Nx, Turborepo for coordinated updates

## Key Insight
Go's approach (minimal version selection, URL-based module paths, checksum database) produces the most predictable and secure dependency resolution. Rust's approach (SAT solver with lockfiles) is more flexible but more complex. npm's approach (nested everything) solves conflicts but at enormous disk space cost.

## References
→ [[Sources Index]]
