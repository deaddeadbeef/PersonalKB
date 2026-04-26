---
tags: [pl, raw, closures, lambdas]
up: "[[Sources Index]]"
---

# Raw Note 045 — Closures and Lambda Implementations

## What is a Closure?

A closure is a function that captures variables from its enclosing scope. The captured environment travels with the function.

## Capture Semantics

### Capture by Reference
- **Python:** Closures capture variables by reference (late binding)
  \\\python
  funcs = [lambda: i for i in range(3)]
  [f() for f in funcs]  # [2, 2, 2] - all see final value of i!
  # Fix: funcs = [lambda i=i: i for i in range(3)]
  \\\
- **JavaScript:** Closures capture by reference (var has function scope)
  \\\javascript
  // Classic gotcha with var:
  for (var i = 0; i < 3; i++) {
    setTimeout(() => console.log(i), 100); // 3, 3, 3
  }
  // Fix: use let (block-scoped)
  \\\
- **C#:** Captures by reference (variable, not value)
- **Java:** Can only capture "effectively final" variables (safe but restrictive)

### Capture by Value
- **C++:** Explicit choice: \[x]\ by value, \[&x]\ by reference, \[=]\ all by value, \[&]\ all by reference
- **Swift:** Captures by reference by default, but \[x]\ in capture list copies

### Capture by Move/Ownership
- **Rust:** Three closure traits based on how they capture:
  - \Fn\ — borrows captured variables immutably
  - \FnMut\ — borrows captured variables mutably
  - \FnOnce\ — takes ownership (consumed on first call)
  - \move\ keyword forces ownership transfer:
    \\\ust
    let name = String::from("Rust");
    let greet = move || println!("Hello, {name}!");
    // name is now owned by the closure
    \\\

## Implementation Strategies

### Heap-Allocated Closure Objects
- **Python, Ruby, JavaScript:** Closures are objects on the heap
- Simple but GC-dependent

### Stack-Allocated (When Possible)
- **Rust:** Closures are anonymous structs; stack-allocated unless boxed
- **C++:** Lambda objects are stack-allocated by default
- **Swift:** Captured values promoted to heap only when necessary (escape analysis)

### Function Pointers vs Closures
- **C:** No closures — only function pointers (no captured state)
- **Go:** Closures are heap-allocated function values
- **Rust:** Non-capturing closures can coerce to function pointers: \n(i32) -> i32\

## Closure as Design Pattern

### Higher-Order Functions
\\\ust
let numbers = vec![1, 2, 3, 4, 5];
let evens: Vec<_> = numbers.iter().filter(|&&x| x % 2 == 0).collect();
\\\

### Builder/Configuration Patterns
\\\go
type Option func(*Server)
func WithPort(p int) Option { return func(s *Server) { s.port = p } }
func NewServer(opts ...Option) *Server { ... }
\\\

### Event Handlers
\\\javascript
button.addEventListener('click', (event) => {
    // Closure captures surrounding scope
    updateCounter(count++);
});
\\\

## Performance

| Language | Closure Overhead | Inlining |
|----------|-----------------|----------|
| Rust | Zero-cost (monomorphized) | Fully inlined |
| C++ | Zero-cost (usually) | Compiler optimizes aggressively |
| Go | Heap allocation | Limited inlining |
| Java (lambda) | invokedynamic + lambda metafactory | JIT can inline |
| Python | Object allocation + dict lookup | No inlining (interpreted) |
| JavaScript | V8 optimizes hot closures | JIT can inline |

## Key Insight
Rust's closure model is the most principled: the three traits (Fn, FnMut, FnOnce) precisely encode how the closure uses its captures, enabling zero-cost abstraction. C++'s explicit capture lists give similar control but with more syntactic overhead. Dynamic languages make closures easy to use but hard to optimize.

## References
→ [[Sources Index]]
