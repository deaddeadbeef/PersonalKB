---
tags: [pl, chunk, numeric-types, precision]
up: "[[Type Systems Overview]]"
---

# Numeric Type Design Choices and Safety

How a language handles numbers reveals its priorities: convenience, safety, performance, or mathematical correctness.

## Integer Overflow: The Silent Killer

C undefined behavior for signed overflow:
- int x = INT_MAX;
- x + 1;  // UB - compiler can assume this never happens

| Language | Overflow Behavior | Rationale |
|----------|------------------|-----------|
| C/C++ | UB (signed), wrap (unsigned) | Performance - no checks |
| Rust | Panic (debug), wrap (release) | Safety with escape hatch |
| Swift | Trap (always crashes) | Safety above all |
| Zig | Illegal (caught in safe mode) | Explicit is better |
| Go | Silent wrap | Simplicity |
| Java | Silent wrap | Backward compatibility |
| Python | Auto-promote to bigint | Convenience |
| Haskell | Int wraps, Integer is arbitrary | Choice available |

Rust additionally provides explicit methods: wrapping_add(), checked_add(), saturating_add(), overflowing_add() — the developer declares their intent.

## Floating-Point Design

Every mainstream language uses IEEE 754, but they differ in defaults:
- **Rust:** f32 and f64, no implicit widening, NaN comparisons handled
- **JavaScript:** Only number (f64) and BigInt — no integers!
- **Python:** float (f64) + Decimal for precision
- **Go:** float32, float64 with strict typing

## The BigInt Question
- **Python, Ruby, Erlang:** Arbitrary-precision integers by default
- **Pro:** No overflow bugs, mathematical correctness
- **Con:** 10-100x slower for simple arithmetic, unpredictable allocation

- **Rust, Go, C:** Fixed-width by default
- **Pro:** Predictable performance, cache-friendly
- **Con:** Overflow is possible

## Key Insight
Rust's numeric type design is exemplary: explicit sizes, debug-mode overflow checks, and named methods for every overflow behavior. It forces developers to think about numeric edge cases without sacrificing release-mode performance.

## References
→ [[Sources Index]]
