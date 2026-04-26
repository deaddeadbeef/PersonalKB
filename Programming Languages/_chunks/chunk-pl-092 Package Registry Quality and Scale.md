---
tags: [chunk, programming-languages, package-ecosystems]
source: "[[raw-pl-024]]"
---

# chunk-pl-092 Package Registry Quality and Scale

**npm (JavaScript):** 2M+ packages. Largest registry. Quality varies enormously. Supply chain security concerns (left-pad, ua-parser-js, event-stream incidents). Nested dependencies solve version conflicts at cost of disk space.

**crates.io (Rust):** 140K+ packages. Smaller but high quality. Strong documentation culture (docs.rs auto-generates). Cargo enforces semver. Crates are immutable once published. Audit tools (cargo-audit) for vulnerability scanning.

**PyPI (Python):** 500K+ packages. Strong in data science/ML. Quality varies. Packaging ecosystem fragmented (pip, poetry, conda, uv). Type stubs growing.

**Maven Central (Java):** 550K+ artifacts. Enterprise ecosystem. Mature but XML-heavy (Maven) or complex (Gradle). Strong backward compatibility culture.

**Go modules:** No central count. URL-based identification. Minimal ecosystem philosophy matches Go's minimalism. proxy.golang.org for module mirror/cache.

**The network effect:** Ecosystem size is self-reinforcing. npm's size makes JavaScript the default for any new tool. Python's ML libraries make it the default for data science. Breaking into a domain with a smaller ecosystem requires compelling technical advantages.
