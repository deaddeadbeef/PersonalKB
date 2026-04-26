---
tags: [pl, chunk, error-handling, exceptions-critique]
up: "[[Error Handling Overview]]"
---

# Why Modern Languages Reject Exceptions

The trend away from exception-based error handling is one of the strongest convergences in modern language design.

## The Case Against Exceptions

### 1. Hidden Control Flow
Exceptions create invisible goto statements:
`java
void processOrder(Order order) {
    validate(order);        // might throw ValidationException
    charge(order.payment);  // might throw PaymentException
    ship(order);            // might throw ShippingException
    notify(order.customer); // might throw NotificationException
}
// Any line can abort execution - but the code reads as sequential
`

### 2. Performance Asymmetry
- Happy path: near-zero cost (table-based unwinding)
- Error path: extremely expensive (stack unwinding, RTTI)
- This makes exceptions unsuitable for expected errors

### 3. Checked Exceptions Failed (Java)
Java tried to fix hidden control flow with checked exceptions:
`java
void readFile() throws IOException { ... }
`
But developers responded with:
`java
try { ... } catch (Exception e) { /* swallow */ }  // The anti-pattern
`
Checked exceptions create "exception fatigue" — too much ceremony.

## What Replaced Exceptions

### Go: Multi-Return Error Values
`go
result, err := doSomething()
if err != nil {
    return fmt.Errorf("context: %w", err)
}
`
Simple but verbose. The if err != nil pattern repeats endlessly.

### Rust: Result<T, E> + ? Operator
`ust
fn process() -> Result<Output, Error> {
    let data = read_file()?;     // ? propagates error
    let parsed = parse(data)?;
    Ok(transform(parsed))
}
`
Concise, type-safe, compiler-enforced. The ? operator is syntactic sugar for match + early return.

### Zig: Error Unions
`zig
fn divide(a: f64, b: f64) !f64 {
    if (b == 0) return error.DivisionByZero;
    return a / b;
}
`
Similar to Rust but with 	ry and catch keywords that work on error unions.

## The Convergence
- **Exceptions:** Java, C#, Python, C++, Ruby (legacy)
- **Result types:** Rust, Haskell, OCaml, Swift (Result), Kotlin (Result)
- **Error values:** Go, Zig, C (return codes)
- **Let it crash:** Erlang, Elixir (supervisor recovery)

New languages overwhelmingly choose Result types or error values over exceptions.

## Key Insight
Exceptions optimized for the wrong thing: making the happy path look clean at the cost of hiding error handling. Result types make error handling visible and type-checked, which catches more bugs and makes error propagation explicit.

## References
→ [[Sources Index]]
