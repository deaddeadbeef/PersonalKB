---
tags: [pl, chunk, design, error-recovery]
up: "[[Error Handling Overview]]"
---

# Error Handling Evolution From C to Rust

Error handling has evolved through distinct generations, each learning from the failures of the previous.

## Generation 1: Error Codes (C, 1972)
`c
int result = open("file.txt", O_RDONLY);
if (result == -1) {
    // Check errno for details
    perror("open failed");
}
`
**Problem:** Easy to forget checking. Nothing prevents ignoring the return value.

## Generation 2: Exceptions (C++ 1990, Java 1995)
`java
try {
    File f = new File("data.txt");
    String content = readAll(f);
} catch (FileNotFoundException e) {
    handleMissing();
} catch (IOException e) {
    handleError(e);
}
`
**Problem:** Hidden control flow. Any line might throw. Checked exceptions (Java) added ceremony without solving the core issue.

## Generation 3: Multi-Return (Go, 2009)
`go
data, err := readFile("config.toml")
if err != nil {
    return fmt.Errorf("config: %w", err)
}
`
**Problem:** Verbose (30% of Go code is error handling). Still possible to ignore errors (though go vet warns).

## Generation 4: Result Types (Rust, 2015)
`ust
fn read_config() -> Result<Config, Error> {
    let data = fs::read_to_string("config.toml")?;
    let config: Config = toml::from_str(&data)?;
    Ok(config)
}
`
**Advantage:** Compiler-enforced handling. ? for ergonomic propagation. must_use attribute warns if Result is ignored.

## Generation 5: Effect-Based (OCaml 5, Koka, 2022+)
`koka
effect raise
    ctl raise(msg: string): a

fun read-config(): raise config
    val data = read-file("config.toml")  // effect tracked in type
    parse-toml(data)
`
**Advantage:** Effects compose naturally. Can swap handlers (real vs mock error handling).

## The Convergence

| Feature | C | Java | Go | Rust | Koka |
|---------|---|------|----|------|------|
| Explicit errors | Yes | No (hidden throw) | Yes | Yes | Yes |
| Compiler-enforced | No | Partial (checked) | No | Yes | Yes |
| Ergonomic propagation | No | No | No | Yes (?) | Yes |
| Composable | No | No | No | Yes | Yes (effects) |
| Zero-cost happy path | Yes | Yes | Yes | Yes | Yes |

## Key Insight
The trend is unmistakable: toward explicit, compiler-enforced, ergonomic error handling. Rust's Result + ? represents the current state of the art for mainstream languages. Algebraic effects may be the next step, but they need more mainstream adoption to prove themselves.

## References
→ [[Sources Index]]
