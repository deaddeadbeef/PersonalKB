---
tags: [programming-languages, error-handling, panic]
up: "[[Error Handling Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---

# Panic and Recovery Mechanisms

> **One-line summary:** Panics represent unrecoverable errors that typically abort the program, forming a critical design boundary between expected failures and invariant violations.

---

## 🎯 Intuition

**The Core Idea:** Panics represent a third category between exceptions and error codes: unrecoverable errors that typically abort the program. The distinction between recoverable errors (handled via Results/exceptions) and unrecoverable errors (handled via panics) is a critical design decision.

**Analogy:** Think of a panic like pulling the emergency brake on a train — it's not for regular stops, only when something is fundamentally wrong and continuing is dangerous. Normal errors are scheduled stops; panics mean the rails themselves are broken.

**Why It Matters:** Languages that separate panic from error (Rust, Go) enforce clearer thinking about failure modes. Languages that unify them (Python, Java) are simpler but make it harder to distinguish "this network request might fail" from "we have a fundamental bug." Choosing the right boundary between recoverable and unrecoverable shapes the reliability of an entire system.

---

## ⚙️ Core Mechanics

### How It Works

A panic interrupts normal control flow and begins unwinding the call stack (or aborting immediately, depending on configuration). Unlike returned errors that callers explicitly handle, a panic propagates automatically until caught by a recovery mechanism or the program terminates. Each language provides different tools for triggering, catching, and converting panics.

### Key Concepts

| Concept | Description |
|---|---|
| **Recoverable error** | Expected failure returned as a value (Result, error, Exception) — callers must handle it |
| **Unrecoverable error (panic)** | Invariant violation or bug that aborts the thread/program by default |
| **Unwinding** | Walking the call stack to run destructors/deferred functions before termination |
| **Abort** | Immediate termination without unwinding (e.g., Rust's `panic = "abort"`) |
| **Recovery** | Catching a panic and converting it to a normal error value (Go's `recover()`, Rust's `catch_unwind()`) |
| **Supervisor** | External process that restarts crashed processes (Erlang/OTP model) |

### Language Examples

**Rust's Dual Error Model**

Rust explicitly separates two kinds of failure:
- **Result<T, E>:** Recoverable errors — file not found, parse failure, network timeout. Callers must handle them.
- **panic!():** Unrecoverable errors — index out of bounds, assertion failure, invariant violation. The thread unwinds and terminates (or the program aborts with `panic = "abort"` in Cargo.toml).

This separation is philosophically important: Result says "this can fail and here's what to do about it." Panic says "something is fundamentally wrong — the program's assumptions are violated."

Rust's `catch_unwind()` can catch panics (for FFI boundaries or thread isolation), but using it for control flow is strongly discouraged. The Rust community enforces: panics are for bugs, Results are for expected failures.

**Go's panic/recover**

Go has a similar dual model:
- **error values:** Normal, expected failures returned as values
- **panic():** Unrecoverable situations (nil pointer dereference, out-of-bounds access, programmer assertions)
- **recover():** Can catch a panic within a deferred function, converting it to an error value

Go's convention: libraries should never panic across API boundaries. Internal panics should be caught with recover() and returned as errors. This keeps panics as an internal implementation detail, not a public API concern.

**Java's Error vs Exception Hierarchy**

Java distinguishes at the type level:
- **Exception** (and subclasses): Recoverable conditions that should be caught. Checked exceptions must be declared.
- **Error** (and subclasses like OutOfMemoryError, StackOverflowError): Conditions that applications should not try to catch. These represent JVM-level failures.
- **RuntimeException** (NullPointerException, ArrayIndexOutOfBoundsException): Unchecked — represent programmer bugs.

In practice, the Error/Exception distinction is less useful than intended — many codebases catch Exception broadly, and OutOfMemoryError sometimes can be recovered from.

**Python's Exception Hierarchy**

Python uses BaseException as the root, with Exception for catchable errors and SystemExit/KeyboardInterrupt as non-catchable (by convention). Python doesn't distinguish recoverable from unrecoverable — any exception can be caught. The philosophy: the programmer decides what's recoverable based on context.

**OCaml's Approach**

OCaml doesn't have a panic mechanism — all errors use exceptions or Result types. An uncaught exception terminates the program. OCaml exceptions are very fast (comparable to C setjmp/longjmp) and are used even for non-error control flow (e.g., early exit from recursive search). OCaml 5.0 added effects as a more structured alternative to exceptions for control flow.

**Erlang's "Let It Crash" Philosophy**

Erlang's "let it crash" philosophy is the opposite extreme: instead of distinguishing recoverable from unrecoverable, Erlang makes everything recoverable at the process level. A process crash is handled by the supervisor, which restarts the process. This eliminates the need for the recoverable/unrecoverable distinction within a process — just crash and let the system recover.

### Key Facts

| Language | Panic Mechanism | Recovery Mechanism | Separation Clarity |
|---|---|---|---|
| Rust | `panic!()` | `catch_unwind()` | Clear — Result vs panic |
| Go | `panic()` | `recover()` in deferred fn | Clear — error vs panic |
| Java | `Error` subclasses | Not intended to be caught | Partial — Error vs Exception hierarchy |
| Python | None (all are exceptions) | `try/except` catches anything | None — programmer decides |
| OCaml | None (all are exceptions) | `try...with` catches anything | None — no panic concept |
| Erlang | Process crash | Supervisor restarts process | None within process — system-level recovery |

---

## 🔬 Deep Dive

### Formal Foundations

The recoverable/unrecoverable distinction maps to a formal concept: **total vs partial functions**. A total function is defined for all inputs in its domain; a partial function is undefined for some inputs. Panics arise when code encounters an input outside the domain of a partial function (e.g., indexing beyond array bounds). Rust's type system tries to make more functions total (using Option/Result), pushing partiality to explicit boundaries. Dependent type systems (Idris, Agda) can eliminate panics entirely by making totality provable at compile time.

### Trade-offs and Design Decisions

- **Explicit separation (Rust, Go):** Forces developers to think about failure modes upfront. More verbose, but failure handling is visible in the type signature. Risk: overuse of `.unwrap()` in Rust degrades back to implicit panics.
- **Unified model (Python, Java):** Simpler API surface. Any failure can be caught. Risk: makes it easy to accidentally swallow critical errors or treat bugs as recoverable.
- **System-level recovery (Erlang):** Moves the recovery boundary from in-process to between-process. Eliminates in-process complexity but requires an actor/supervisor architecture. Risk: not applicable to single-process programs or tight latency requirements.
- **Performance:** Unwinding is expensive (Rust, C++). Aborting is cheap but loses cleanup. Erlang's process crash is cheap because processes are lightweight. OCaml exceptions are fast because they use setjmp/longjmp.

### Historical Context

The panic concept evolved from early abort mechanisms in C (`abort()`, `exit()`) and structured exception handling in C++ and Java. Go introduced `panic/recover` as a deliberate simplification of C++ exceptions, limiting their use to truly exceptional cases. Rust refined this further by making the separation type-level with Result vs panic. Erlang's approach predates all of these, originating in telecom systems (1986) where hardware failures were routine and process-level recovery was a necessity.

---

## 🏋️ Practice

### Warm-Up (5 min)

1. Explain in your own words why panic is different from a normal returned error value.
2. For each language above, classify whether the system separates recoverable and unrecoverable failure clearly, partially, or not at all.
3. Decide whether each scenario should use an error/exception or a panic: missing file, failed parse, broken invariant, index out of bounds, network timeout, impossible internal state.

### Core Problems

1. **Boundary Design:** You are writing a Go library that parses configuration files. Internally, you use `panic` for certain impossible states. Design the public API so that no panic escapes to the caller. Write the `recover()` pattern you would use and explain where it goes.
2. **Rust Unwrap Audit:** Given a Rust codebase that uses `.unwrap()` in 47 places, describe a systematic approach to classify each usage as (a) acceptable (truly impossible failure), (b) should be replaced with `?` operator, or (c) should be replaced with a meaningful error message via `.expect()`. What criteria distinguish the three categories?

### Challenge

1. **Cross-Language Recovery Architecture:** Design a system where a Rust core library (using panic for invariant violations) is called from a Go service (using recover at API boundaries) which is supervised by an Erlang node (using OTP supervisors). Describe the error/panic boundaries at each layer and how a deep invariant violation in Rust propagates through all three layers. What information is preserved or lost at each boundary crossing?

---

*See also:* [[Error Handling Overview]], [[Result and Option Types]], [[Programming Languages/Error Handling/Exception-Based Error Handling|Exception Hierarchies]]

## Supporting Chunks / References

- [[Programming Languages/Sources/Sources Index|Sources Index]]

## References

- [[Programming Languages/Sources/Sources Index]]
- [[Programming Languages/Programming Languages Book Reading Spine]]
- [[Programming Languages/Programming Languages]]
