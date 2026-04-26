---
tags: [pl, chunk, packages, supply-chain]
up: "[[Dependency Management]]"
---

# Package Registry Design and Supply Chain Security

The design of package registries has become a critical security concern after high-profile supply chain attacks.

## Registry Design Principles

### Immutability (crates.io, Hex)
Once published, a version can never be changed or deleted:
- **Yank:** Mark as deprecated, but dependents with lockfiles still work
- **No unpublish:** Prevents the "left-pad" incident
- **Audit trail:** Every version is permanently archived

### Checksum Verification (Go modules)
Go's module system uses a checksum database:
- No MITM attacks on module downloads
- No registry can tamper with published modules
- go.sum file records expected checksums

### Namespace Design

| Registry | Namespace | Squatting Risk |
|----------|-----------|---------------|
| npm | Flat + scopes (@org/pkg) | Moderate (scopes help) |
| crates.io | Flat | Moderate |
| PyPI | Flat | High |
| Maven | Reverse domain (com.google.guava) | Low |
| Go modules | URL path (github.com/user/repo) | Very low |

## Supply Chain Attack Vectors

1. **Typosquatting:** colorsss instead of colors - PyPI and npm most vulnerable
2. **Maintainer compromise:** Attacker gains access to popular package - ua-parser-js
3. **Dependency confusion:** Internal package matches public registry - Alex Birsan's research
4. **Social engineering:** Long-term trust building before injection - xz utils (2024)
5. **Protestware:** Maintainer intentionally sabotages - colors/faker (2022)

## Modern Defenses
- **Lockfiles:** Pin exact versions (package-lock.json, Cargo.lock, go.sum)
- **Provenance:** Verify packages were built from claimed source (npm, PyPI)
- **SBOM:** Software Bill of Materials for dependency tracking
- **Sigstore:** Keyless signing for package integrity
- **Socket.dev:** Real-time supply chain threat detection

## Key Insight
Go's module system (URL-based paths + checksum DB) and Rust's crates.io represent the state of the art. The industry is converging on: lockfiles + provenance + automated auditing as the minimum security baseline.

## References
-> [[Sources Index]]
