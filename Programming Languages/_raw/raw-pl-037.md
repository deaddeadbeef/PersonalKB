---
tags: [pl, raw, testing, tdd]
up: "[[Sources Index]]"
---

# Raw Note 037 — Testing Frameworks and Philosophies

## Testing Philosophies by Language

### Built-in Testing
Languages with testing as a first-class feature:
- **Go:** `go test` + `_test.go` convention — no external framework needed
- **Rust:** `#[test]` attribute + `cargo test` — tests live alongside code
- **Zig:** `test` blocks inline with code — comptime testing
- **Python:** unittest (stdlib), but pytest dominates in practice
- **Elixir:** ExUnit built into the language

### External Framework Ecosystem
Languages that rely on third-party test frameworks:
- **Java:** JUnit (standard), TestNG, Spock (Groovy-based BDD)
- **JavaScript:** Jest, Vitest, Mocha, Cypress (E2E), Playwright
- **C++:** Google Test, Catch2, doctest — fragmented
- **Ruby:** RSpec (BDD), Minitest (shipped with Ruby)
- **Haskell:** HUnit, QuickCheck, Hedgehog
- **C#:** xUnit, NUnit, MSTest

## Testing Paradigms

### Property-Based Testing
Test with random inputs against properties rather than specific examples:
- **Haskell QuickCheck:** Pioneer — `prop_reverse_reverse xs = reverse (reverse xs) == xs`
- **Rust proptest:** Inspired by QuickCheck
- **Python Hypothesis:** Most mature PBT library outside Haskell
- **Scala ScalaCheck:** JVM property testing
- **F# FsCheck:** .NET property testing

### Snapshot/Golden Testing
Compare output against saved "golden" files:
- **Jest snapshots:** Popular in React testing
- **Rust insta:** Snapshot testing with review workflow
- **Go golden files:** Manual but common pattern

### Fuzzing
Generate malformed inputs to find crashes and bugs:
- **Go:** Built-in `go test -fuzz` (Go 1.18+)
- **Rust:** cargo-fuzz (libFuzzer-based)
- **C/C++:** AFL, libFuzzer, honggfuzz — most mature ecosystem
- **Python:** Atheris (libFuzzer wrapper)

### BDD (Behavior-Driven Development)
- **Ruby RSpec:** `describe`, `it`, `expect` — the gold standard
- **Kotlin Kotest:** Rich BDD DSL leveraging Kotlin's syntax
- **Elixir ExUnit:** Describe/test blocks with doc-based examples
- **JavaScript Cucumber:** Gherkin syntax (Given/When/Then)

## Testing Culture

| Language | Testing Culture | Typical Coverage |
|----------|----------------|-----------------|
| Rust | Strong — compiler + tests = high confidence | High |
| Go | Moderate — table-driven tests are idiomatic | Moderate-high |
| Java | Strong — enterprise demands thorough testing | High (corporate) |
| Python | Variable — depends on domain (ML often untested) | Variable |
| Haskell | Type system reduces need, QuickCheck fills gaps | Moderate |
| C++ | Weak historically, improving | Low-moderate |
| JavaScript | Strong in frontend, inconsistent elsewhere | Variable |

## Type Systems vs Tests

A recurring debate: do strong types reduce the need for tests?
- **Haskell position:** "If it compiles, it probably works" — types eliminate many bug classes
- **Rust position:** Types prevent memory/thread bugs; tests cover logic
- **Go position:** Simple types + extensive tests = practical correctness
- **Dynamic language position:** Tests are your type system (TDD essential)

Reality: types and tests are complementary. Types prevent structural errors; tests verify business logic.

## References
→ [[Sources Index]]
