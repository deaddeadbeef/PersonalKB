---
tags: [programming-languages, error-handling, error-codes]
up: "[[Error Handling Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---

# Error Codes and Sentinel Values

> The oldest error handling strategy — functions return special values indicating failure, predating exceptions, result types, and every structured error mechanism.

---

## 🎯 Intuition

### Core Idea

A function communicates failure by returning a designated value from its normal return type. The caller must know which values are "magic" and remember to check for them. Nothing in the mechanism itself enforces correctness — it relies entirely on programmer discipline.

### Analogy

Error codes are like a doctor who just says a number instead of explaining — "your result is −1" tells you *something* failed but not *why*, not how severe it is, and not what to do next. You have to look up the code in a separate table (errno, documentation) to get the full picture, and if you forget to look, you walk away thinking everything is fine.

### Why It Matters

This pattern is the foundation every later error mechanism reacts against. Understanding its strengths (simplicity, zero overhead, cross-language compatibility) and weaknesses (ignorability, in-band signaling) is essential for evaluating exceptions, Result types, and algebraic error handling. It also remains the *active* convention at OS and FFI boundaries — you will encounter it regardless of what language you prefer.

---

## ⚙️ Core Mechanics

### How It Works

A function returns a value from its normal return type that has been designated as "error." Common patterns:

- **Negative values:** C's `read()` returns bytes read, or −1 on error (with errno set)
- **NULL pointer:** C's `malloc()` returns NULL on failure
- **Boolean success:** C's `fclose()` returns 0 on success, EOF on failure
- **Sentinel values:** Python's `str.find()` returns −1 when not found

### Key Concepts

| Concept | Description |
|---|---|
| In-band signaling | Error values occupy the same domain as legitimate return values |
| Sentinel value | A reserved value (−1, NULL, EOF) that means "not a real result" |
| errno | Global (thread-local on modern systems) variable holding the specific POSIX error code |
| Error indicator | The return value that tells you *an* error occurred (distinct from errno, which tells you *which* error) |

### Language Examples

**C errno** — C uses a global variable `errno` set by failed system calls. After a function returns an error indicator, you check `errno` for the specific error code (ENOENT, EPERM, ENOMEM, etc.). This is the standard POSIX error mechanism.

Problems with errno:
- You must check it immediately — any subsequent call might overwrite it
- It's a global variable, creating thread-safety issues (modern systems use thread-local errno)
- Nothing forces you to check it — ignoring the error is the path of least resistance
- The error indicator (return value) and error details (errno) are separated

**Go error** — Go's `error` interface is technically an error value (not an exception), but it's richer than C error codes: errors are first-class values that can carry context, be wrapped, and form chains. Go's `errors.Is()` and `errors.As()` enable structured error matching. This represents an evolution of the error code pattern — keeping explicitness while adding structure.

**Zig error union** — Zig combines error codes with type safety: error unions `!T` indicate a value that's either a valid T or an error from an error set. Like Rust's Result but with compiler-managed error sets. Zig even allows `try` as shorthand for propagation, similar to Rust's `?`. This modernizes the error code approach while maintaining C interop.

### Key Facts

- Error codes are the only error mechanism that works across every language boundary (C ABI)
- Exceptions have overhead (stack unwinding); error codes are just integer comparisons
- Go and Zig represent modern evolutions: error *values* with type-system support, not raw integers

---

## 🔬 Deep Dive

### Formal Foundations

Error codes implement a *total function* convention: every call returns a value, and a subset of the codomain is partitioned off to signal failure. This is the degenerate case of a sum type — the return type is implicitly `T | error`, but the "sum" is encoded as overlapping values rather than distinct variants. Algebraic error types (Result, Either, error unions) make this partition explicit and compiler-verifiable.

### Trade-offs and Design Decisions

**Why languages moved away:** Error codes have fundamental design problems:

1. **Ignorable:** Nothing in the language forces checking. Unchecked errors are silent bugs.
2. **In-band signaling:** Error values occupy the same domain as legitimate return values. Is −1 an error or a valid result? Depends on the function.
3. **Non-composable:** Chaining operations requires checking errors at every step, obscuring the happy path.
4. **No context:** An integer code carries minimal information compared to an exception object or Result error type with fields.

**Where error codes persist:** Despite their problems, error codes remain standard in:

- **Operating system APIs:** POSIX, Windows API — the lowest-level interfaces use integer error codes because they work across language boundaries
- **C libraries:** Libraries consumed by multiple languages can't use language-specific exception mechanisms
- **FFI boundaries:** When Rust, Go, or Python call C libraries, they work with C's error conventions
- **Performance-critical paths:** Exceptions have overhead (stack unwinding); error codes are just integer comparisons

### Historical Context

Error codes are the original error mechanism, dating to early C and assembly. POSIX standardized the errno convention. Exceptions (C++, Java) were a direct reaction to the ignorability and non-composability of error codes. Rust's `Result`, Haskell's `Either`, and Zig's error unions represent a second wave — retaining the explicit-checking philosophy while using the type system to prevent the classic pitfalls. Go chose a middle path: explicit error values with interface-based structure, but no compiler enforcement of checking.

---

## 🏋️ Practice

### Warm-Up

1. A C function returns `int` and uses −1 as its error sentinel. You call it in a loop accumulating results. Write pseudocode showing how an unchecked error silently corrupts the running total.
2. Explain why `errno` must be checked *immediately* after the call that might set it, not after two or three subsequent operations.
3. Python's `str.find()` returns −1 on "not found" while `str.index()` raises `ValueError`. What class of bug does `find()` enable that `index()` prevents?

### Core Problems

4. Design a C-style API for a `read_config(path, buf, buf_len)` function. Define the return value semantics and error indicators. Then refactor it into a Go-style API using an `error` return — what information can you now attach that was impossible with the integer code alone?
5. You are wrapping a C library that uses errno in a Zig program. Sketch how you would translate errno values into a Zig error set and return `!T` from your wrapper function. Identify where information might be lost in the translation.

### Challenge

6. Argue for *and* against replacing all error-code-based POSIX APIs with Result-type wrappers at the libc level. Consider: ABI stability, performance, backward compatibility, multi-language consumers, and incremental adoption. Which trade-off do you find most decisive?

---

*See also:* [[Error Handling Overview]] · [[Programming Languages/Error Handling/Exception-Based Error Handling|Exceptions]] · [[Result and Option Types]] · [[Programming Languages/Error Handling/Result and Option Types|Algebraic Error Handling]]

---

## Supporting Chunks / References

- [[Programming Languages/Sources/Sources Index|Sources Index]]

## References

- [[Programming Languages/Sources/Sources Index]]
- [[Programming Languages/Programming Languages Book Reading Spine]]
- [[Programming Languages/Programming Languages]]
