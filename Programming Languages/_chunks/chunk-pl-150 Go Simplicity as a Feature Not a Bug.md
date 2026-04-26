---
tags: [pl, chunk, go, simplicity]
up: "[[Go — Language Profile]]"
---

# Go Simplicity as a Feature Not a Bug

Go's deliberate omission of features is its most controversial and most important design choice.

## What Go Left Out (And Why)

| Feature | Go's Alternative | Rationale |
|---------|-----------------|-----------|
| Generics (until 1.18) | Interfaces + code gen | Simplicity, fast compilation |
| Exceptions | Multi-return (T, error) | Explicit error handling |
| Enums/ADTs | Constants + iota | Keep it simple |
| Macro system | go generate | Avoid compile-time complexity |
| Pattern matching | if/switch | Sufficient for most cases |
| Inheritance | Embedding | Composition over inheritance |
| Operator overloading | Named methods | Clear semantics |
| Immutable variables | Convention | Simplicity over enforcement |
| Sum types | Interfaces | Debated, may come eventually |

## The Simplicity Argument

Rob Pike: "Less is exponentially more"

Go's simplicity means:
- **Any Go developer can read any Go codebase** — there's only one way to write most things
- **Fast compilation:** Go compiles millions of LOC in seconds
- **Low learning curve:** Productive in days, not months
- **gofmt standardization:** All Go code looks the same

## The Criticism

Go's simplicity comes at a cost:
- **Verbose error handling:** if err != nil accounts for ~30% of Go code
- **Code duplication:** Without generics (pre-1.18), common patterns were copy-pasted
- **Limited abstraction:** Can't express some patterns cleanly (no HKTs, no traits)
- **Runtime checks instead of compile checks:** No sum types means invalid states are possible

## Go 1.18+ Generics: The Compromise

After 12 years of debate, Go added generics with the simplest possible design:
`go
func Map[T, U any](s []T, f func(T) U) []U {
    result := make([]U, len(s))
    for i, v := range s {
        result[i] = f(v)
    }
    return result
}
`
- Type constraints via interfaces
- No associated types, no HKTs, no variance annotations
- Keeps Go's simplicity ethos

## When Go's Simplicity Wins

Go excels for:
- **Cloud infrastructure:** Kubernetes, Docker, Terraform, Prometheus
- **CLI tools:** Simple deployment (static binary), fast startup
- **Web services:** Goroutines handle concurrency beautifully
- **Teams:** Large teams with mixed experience levels

## Key Insight
Go's radical simplicity is intentional engineering, not laziness. It trades individual developer expressiveness for team-wide readability and onboarding speed. This explains why Go dominates cloud infrastructure (large teams, many contributors) while Rust dominates systems programming (small teams, high correctness requirements).

## References
→ [[Sources Index]]
