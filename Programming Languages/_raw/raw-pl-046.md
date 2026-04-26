---
tags: [pl, raw, iterators, generators]
up: "[[Sources Index]]"
---

# Raw Note 046 – Iterator and Generator Patterns

## Iterator Protocol by Language

### Rust (most principled)
- Ownership-aware: iter() borrows, into_iter() consumes
- Compiler monomorphizes and inlines iterator chains to loops

### Python (generators as first-class)
- __iter__ + __next__ protocol
- Generator functions with yield
- itertools module for composition
