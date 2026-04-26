---
tags: [chunk, programming-languages, batteries]
source: "[[raw-pl-030]]"
---

# chunk-pl-068 Batteries-Included vs Minimal Core

**Batteries-included (Python, Go, Java):** Large standard library covering common needs. Python: os, json, http, sqlite3, unittest, datetime, re, pathlib. Go: net/http, encoding/json, testing, crypto. Reduced third-party dependency. Slower evolution (stdlib is forever).

**Minimal core (Rust, Haskell, Zig):** Small standard library. Rich community packages. Rust: no HTTP, no JSON, no async runtime in stdlib — use reqwest, serde, tokio. Faster ecosystem evolution (packages can break compat). Risk: quality varies, ecosystem fragmentation.

**Java's middle ground:** Large stdlib (java.util, java.io, java.net) but critical features come from ecosystem (Spring, Jackson, Guava). Maven Central is essentially an extended standard library.

**The Node.js lesson:** Minimal core + npm = massive ecosystem. But: left-pad incident, supply chain attacks, dependency bloat (1000+ transitive deps common). Size of node_modules is a meme.

Trade-off: batteries-included reduces dependency risk but constrains evolution. Minimal core enables rapid innovation but requires trust in third-party packages.
