---
tags: [chunk, programming-languages, formatters]
source: "[[raw-pl-024]]"
---

# chunk-pl-117 Opinionated Formatters That Ended Debates

**gofmt (Go):** The original. One style, zero configuration. Shipped with the language. "Gofmt's style is no one's favorite, yet gofmt is everyone's favorite." Ended all Go formatting debates on day one.

**rustfmt (Rust):** cargo fmt. Some configuration options but strong defaults. Community uses rustfmt consistently. Part of the standard Rust toolchain.

**Black (Python):** "The Uncompromising Code Formatter." Minimal configuration. Deterministic output. Growing standard in the Python community.

**Prettier (JavaScript/TypeScript):** Opinionated formatter for JS, TS, CSS, HTML, JSON, Markdown. De facto standard for web projects.

**Why opinionated formatters win:**
1. Eliminate bikeshedding (no style arguments in code review)
2. Diffs are meaningful (no formatting-only changes)
3. Consistent across entire ecosystem (all Go code looks the same)
4. New team members productive immediately (no style guide to memorize)
5. Automated (pre-commit hooks, CI checks)

**Languages without standard formatters:** C/C++ (clang-format exists but many styles), Java (multiple formatters, none dominant), Haskell (ormolu, fourmolu — newer). The lack of consensus formatter is a minor but real friction.
