---
tags: [pl, chunk, rust, ownership-patterns]
up: "[[Ownership and Borrowing]]"
---

# Ownership Patterns Beyond the Basics

Rust's ownership system has patterns that emerge once you master the fundamentals.

## The Newtype Pattern
Wrap a type to give it different semantics:
\\\ust
struct Meters(f64);
struct Seconds(f64);
// Cannot accidentally mix: velocity = Meters(10.0) / Seconds(2.0)
// Without newtypes: velocity = 10.0 / 2.0 (units lost)
\\\
Zero-cost at runtime (same representation as the inner type).

## The Builder Pattern
Ownership enables fluent builders that consume self:
\\\ust
struct RequestBuilder { url: String, method: Method, headers: Vec<Header> }
impl RequestBuilder {
    fn url(mut self, url: &str) -> Self { self.url = url.to_string(); self }
    fn method(mut self, m: Method) -> Self { self.method = m; self }
    fn header(mut self, h: Header) -> Self { self.headers.push(h); self }
    fn build(self) -> Request { Request { /* move fields */ } }
    // After build(), the builder is consumed - can't be reused accidentally
}
\\\

## The Typestate Pattern
Use the type system to enforce valid state transitions:
\\\ust
struct Locked;
struct Unlocked;
struct Door<State> { _state: PhantomData<State> }

impl Door<Locked> {
    fn unlock(self) -> Door<Unlocked> { Door { _state: PhantomData } }
}
impl Door<Unlocked> {
    fn lock(self) -> Door<Locked> { Door { _state: PhantomData } }
    fn open(&self) { println!("Opening door"); }
}
// door.open() only compiles if door is Unlocked
// Calling unlock() consumes the Locked door and returns an Unlocked one
\\\

## Interior Mutability
When you need mutation behind a shared reference:
\\\ust
use std::cell::RefCell;
let data = RefCell::new(vec![1, 2, 3]);
data.borrow_mut().push(4); // Runtime borrow checking
// For thread-safe: use Mutex<T> or RwLock<T>
\\\

## Cow (Clone-on-Write)
Defer cloning until mutation is needed:
\\\ust
use std::borrow::Cow;
fn process(input: Cow<str>) -> Cow<str> {
    if input.contains("bad") {
        Cow::Owned(input.replace("bad", "good"))
    } else {
        input // No clone if no modification needed
    }
}
\\\

## Key Insight
Rust's ownership system enables design patterns impossible in other languages. The typestate pattern turns runtime state errors into compile-time errors. The builder pattern with consumed self prevents misuse. These patterns demonstrate that ownership isn't just about memory - it's about encoding invariants in the type system.

## References
→ [[Sources Index]]
