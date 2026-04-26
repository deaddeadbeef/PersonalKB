---
tags: [pl, raw, numeric-types, precision]
up: "[[Sources Index]]"
---

# Raw Note 044 — Numeric Types and Precision

## Integer Types

### Fixed-Width Integers
Languages that give precise control:
- **Rust:** i8, i16, i32, i64, i128, u8, u16, u32, u64, u128, isize, usize
- **Go:** int8, int16, int32, int64, uint8-64, int (platform-sized)
- **C/C++:** char, short, int, long — sizes are platform-dependent!
- **Zig:** i1 through i65535, u1 through u65535 (arbitrary bit-width)
- **Swift:** Int8, Int16, Int32, Int64, UInt8-64
- **C#:** byte, short, int, long, sbyte, ushort, uint, ulong

### Arbitrary-Precision Integers
- **Python:** int is always arbitrary precision — no overflow possible
- **Haskell:** Integer is arbitrary; Int is fixed
- **Ruby:** Integer auto-promotes from Fixnum to Bignum
- **Erlang:** Integers are arbitrary precision by default
- **Java:** BigInteger class (not a primitive)
- **Go:** math/big package

### Integer Overflow Behavior

| Language | Default Behavior | Safety |
|----------|-----------------|--------|
| C/C++ | Undefined behavior (signed), wrapping (unsigned) | Unsafe |
| Rust | Panic in debug, wrapping in release | Checked in debug |
| Go | Wrapping (silent) | Silent overflow |
| Java | Wrapping (silent) | Silent overflow |
| Swift | Trap (crash) on overflow | Safe by default |
| Zig | Illegal behavior (caught in safe mode) | Checked |
| Python | N/A (arbitrary precision) | Safe |
| C# | Wrapping default, checked blocks available | Configurable |

## Floating-Point Types

Most languages use IEEE 754:
- **f32/f64** (Rust), **float32/float64** (Go), **float/double** (C/Java)
- **f16** support: Zig, Rust (limited), C++23 (std::float16_t)
- **f128** support: Rust (unstable), Zig, C (optional _Float128)
- **Decimal types:** C# decimal (128-bit), Python Decimal, Java BigDecimal

### Floating-Point Gotchas
\\\python
>>> 0.1 + 0.2 == 0.3
False  # 0.30000000000000004
\\\

Every language has this problem with IEEE 754. Solutions:
- Decimal types for money (C# decimal, Java BigDecimal)
- Integer arithmetic in smallest unit (cents, not dollars)
- Epsilon comparison: \bs(a - b) < epsilon\

## Numeric Literals

| Feature | Languages |
|---------|-----------|
| Underscores in literals | Rust, Python, Java, C#, Swift, Kotlin, Go, Zig |
| Binary literals (0b) | Rust, Python, Go, C++14, Java 7+, Swift |
| Octal literals (0o) | Rust, Python, Go, Zig (prefix 0o) |
| Type suffixes | Rust (42u64), Go (none), C (42L, 42ULL) |
| Complex literals | Python (3+4j), Fortran |

## Key Insight
The trend is toward explicit, safe numeric types. Rust and Zig require choosing exact integer sizes. Python's arbitrary-precision integers are convenient but hide performance costs. The C legacy of platform-dependent int sizes continues to cause portability bugs.

## References
→ [[Sources Index]]
