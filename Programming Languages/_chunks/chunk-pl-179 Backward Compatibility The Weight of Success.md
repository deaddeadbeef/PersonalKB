---
tags: [pl, chunk, design, backward-compatibility]
up: "[[Language Genealogy Overview]]"
---

# Backward Compatibility The Weight of Success

Backward compatibility is both the greatest strength and greatest burden of successful languages.

## The Compatibility Spectrum

| Language | Compatibility Promise | Strategy |
|----------|---------------------|----------|
| Go | Go 1 compatibility guarantee | Never break, deprecate slowly |
| Java | Nearly absolute | Remove nothing, add carefully |
| JavaScript | Never break the web | Add but never remove features |
| Rust | Editions (opt-in) | New semantics per edition |
| Python | Breaking changes allowed | Python 2 → 3 (10-year migration) |

## Case Studies

### Python 2 → 3: The Painful Migration
- **2008:** Python 3.0 released with breaking changes
- **2010-2019:** Community split
- **2020:** Python 2 officially end-of-life
- **Lesson:** 12 years of pain. Don't do breaking changes lightly.

### Rust Editions: The Elegant Solution
Rust never breaks existing code but evolves via editions (2015, 2018, 2021, 2024).

### JavaScript: Never Remove Anything
typeof null === "object" is a bug from 1995 that can NEVER be fixed because millions of websites depend on it.

## Key Insight
Rust's edition system is the most elegant solution to the backward compatibility problem. It allows evolution without breaking code.

## References
→ [[Sources Index]]
