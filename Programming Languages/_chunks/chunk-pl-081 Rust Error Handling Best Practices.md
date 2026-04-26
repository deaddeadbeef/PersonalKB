---
tags: [chunk, programming-languages, rust-error]
source: "[[raw-pl-021]]"
---

# chunk-pl-081 Rust Error Handling Best Practices

Rust's error handling ecosystem:

**In libraries:** Use 	hiserror crate for custom error types with derive macros. Define specific error enums for each module. Return Result<T, MyError>.

**In applications:** Use nyhow crate for convenient error boxing. nyhow::Result<T> wraps any error type. .context("what we were doing") adds context to errors.

**The ? operator pattern:**
```rust
fn load_config() -> Result<Config, Error> {
    let text = fs::read_to_string("config.toml")?;
    let config: Config = toml::from_str(&text)?;
    Ok(config)
}
```
Each ? either unwraps Ok or propagates Err. Function signature documents all failure modes.

**Error conversion:** From trait enables automatic conversion between error types. impl From<io::Error> for MyError lets ? work across error types.

**When to panic:** Only for programmer bugs (assertion failures, unreachable code, invariant violations). Never for expected errors (file not found, parse failure, network timeout).

**Compared to Go:** Both explicit. Rust: type-safe, can't ignore errors, composable. Go: simpler, verbose (if err != nil), errors are values without type enforcement.
