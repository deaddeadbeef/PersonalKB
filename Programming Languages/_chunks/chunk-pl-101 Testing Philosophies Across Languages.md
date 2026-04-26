---
tags: [chunk, programming-languages, testing]
source: "[[raw-pl-024]]"
---

# chunk-pl-101 Testing Philosophies Across Languages

**Go:** Testing built into the toolchain. go test. Test files alongside source (oo_test.go). Table-driven tests (slices of test cases). No assertions library in stdlib — if/t.Fatal. Benchmarking built in. Property testing via 	esting/quick.

**Rust:** Tests in the same file as code (#[test] annotation). cargo test runs all. Unit tests in mod tests with #[cfg(test)]. Integration tests in 	ests/ directory. Doc tests: code examples in documentation are compiled and tested.

**Python:** unittest (stdlib), pytest (community standard). pytest's fixtures and parametrize are powerful. Property testing via Hypothesis.

**Haskell:** QuickCheck invented property-based testing. Define properties; the framework generates random inputs. prop_reverse_reverse xs = reverse (reverse xs) == xs. Influenced: Hypothesis (Python), proptest (Rust), test.check (Clojure).

**Java:** JUnit 5 with annotations (@Test, @BeforeEach, @ParameterizedTest). Mockito for mocking. Massive testing ecosystem.

**Elixir:** ExUnit built into language. Doctests (examples in docs are tests). Property testing via StreamData. mix test with watch mode.

Key insight: languages with strong type systems need fewer tests (the compiler is a test suite). Languages with weak types need more tests to compensate.
