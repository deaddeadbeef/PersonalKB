---
tags: [pl, raw, governance, community]
up: "[[Sources Index]]"
---

# Raw Note 035 — Language Governance and Community Models

## Governance Models

### Benevolent Dictator for Life (BDFL)
- **Python:** Guido van Rossum (stepped down 2018, now Steering Council)
- **Lua:** Roberto Ierusalimschy at PUC-Rio
- **Ruby:** Yukihiro "Matz" Matsumoto
- **Zig:** Andrew Kelley (Zig Software Foundation)

### Corporate Stewardship
- **Go:** Google (Rob Pike, Robert Griesemer, Ken Thompson — now broader team)
- **Rust:** Originally Mozilla, now independent Rust Foundation
- **Swift:** Apple (Chris Lattner created it, now broader community)
- **Kotlin:** JetBrains (open-source but JetBrains-driven)
- **C#:** Microsoft (Anders Hejlsberg, .NET Foundation)
- **TypeScript:** Microsoft (Anders Hejlsberg)
- **Java:** Oracle (OpenJDK community process)
- **Dart:** Google (Flutter team drives evolution)

### Committee/Standards Body
- **C:** ISO/IEC JTC1/SC22/WG14 — slow, deliberate evolution
- **C++:** ISO/IEC JTC1/SC22/WG21 — 3-year release cycles, extensive proposals
- **JavaScript:** TC39 (Ecma International) — staged proposal process
- **Fortran:** ISO/IEC JTC1/SC22/WG5

### Community/Foundation
- **Rust:** Rust Foundation + RFC process + teams (compiler, lang, libs, etc.)
- **Haskell:** Haskell Foundation + GHC Steering Committee
- **Erlang/Elixir:** Erlang Ecosystem Foundation
- **OCaml:** OCaml Software Foundation + core team at INRIA

## RFC/Proposal Processes

| Language | Process | Speed | Quality |
|----------|---------|-------|---------|
| Rust | RFC → FCP → merge → nightly → stable | Moderate | High — thorough review |
| Python | PEP (Python Enhancement Proposal) | Slow | High — extensive discussion |
| Go | Proposal → discussion → accept/decline | Slow | Very high — conservative |
| C++ | Paper → study group → committee vote | Very slow | Variable — committee dynamics |
| JavaScript | Stage 0 → 1 → 2 → 3 → 4 | Moderate | Good — staged maturity |
| Swift | Swift Evolution proposals | Moderate | Good — Apple-guided |
| Kotlin | KEEP (Kotlin Evolution and Enhancement Process) | Fast | Good — JetBrains-driven |

## Release Cadences

| Language | Cadence | Stability Promise |
|----------|---------|-------------------|
| Rust | 6-week editions + 3-year epochs | No breaking changes ever (editions opt-in) |
| Go | 6-month releases | Go 1 compatibility promise |
| Python | Annual (3.x) | Deprecation warnings → removal after 2 releases |
| Java | 6-month releases (LTS every 2 years) | Strong backward compatibility |
| C++ | 3-year standards (C++20, C++23, C++26) | Implementation varies by compiler |
| JavaScript | Annual ECMAScript editions | Never removes features (web compat) |
| TypeScript | Quarterly releases | Some breaking changes allowed |

## Community Culture

| Language | Culture | Motto/Vibe |
|----------|---------|------------|
| Rust | Welcoming, safety-focused, intense | "Fearless concurrency" — empowering, sometimes exhausting |
| Go | Pragmatic, conservative, corporate | "Less is exponentially more" — simplicity above all |
| Python | Inclusive, teaching-oriented | "There should be one obvious way" — readability |
| Haskell | Academic, theoretical, passionate | "Avoid success at all costs" — research-driven |
| Ruby | Joyful, creative, Rails-centric | "Programmer happiness" — developer ergonomics |
| Elixir | Friendly, pragmatic-FP | "Let it crash" — inherited from Erlang |
| JavaScript | Chaotic, innovative, fast-moving | "Move fast" — ecosystem churn |
| C++ | Divided, expert-oriented | "Zero overhead" — performance at all costs |

## Key Insight
Governance models profoundly shape language evolution. Corporate-backed languages (Go, Kotlin) evolve faster but risk corporate priorities diverging from community needs. Committee languages (C++) are stable but slow. Rust's RFC model is widely admired but demands significant volunteer effort.

## References
→ [[Sources Index]]
