---
tags: [chunk, programming-languages, error-handling]
source: "[[raw-pl-004]]"
---

# chunk-pl-012 Result Types and the Question Mark Operator

Result types encode success/failure in the type system:

- **Rust:** Result<T, E> — Ok(value) or Err(error). The ? operator propagates errors ergonomically.
- **Haskell:** Either a b composed via monadic operations (>>=, do-notation).
- **OCaml:** ('a, 'b) result — Ok value or Error error. Binding operators (let*).
- **Go:** Error values esult, err := ... — explicit but verbose, nothing prevents ignoring err.

**Option/Maybe for absence:**
- Rust: Option<T> — Some(value) or None
- Haskell: Maybe a — Just value or Nothing
- Swift: T? — value or nil (typed)
- Kotlin: T? — nullable with smart casts

The ? operator is Rust's key ergonomic innovation: let content = fs::read_to_string(path)?; either unwraps Ok or returns Err early. Gives visibility of exceptions with explicitness of error codes.
