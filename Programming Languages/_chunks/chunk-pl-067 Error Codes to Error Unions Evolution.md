---
tags: [chunk, programming-languages, error-codes]
source: "[[raw-pl-004]]"
---

# chunk-pl-067 Error Codes to Error Unions Evolution

**C error codes:** Return -1, NULL, or sentinel values. errno for details. Problems: easily ignored, in-band signaling, no context, non-composable. Still standard in OS APIs and C libraries because they work across language boundaries.

**Go error interface:** Richer than C codes — errors are values with context, wrapping, and chains. errors.Is() and errors.As() for matching. Explicit but verbose: if err != nil is the most-written Go code. Intentionally verbose — error handling should be visible.

**Zig error unions:** !T — either valid T or error from compile-time error set. Compiler tracks which errors are possible. 	ry propagates errors (like Rust's ?). Modernizes error codes with type safety while maintaining C interop.

The evolution: C error codes (unsafe, ignorable) -> Go error values (explicit, verbose) -> Zig error unions (type-safe, ergonomic) -> Rust Result (full algebraic type). Each step adds safety while maintaining explicitness.
