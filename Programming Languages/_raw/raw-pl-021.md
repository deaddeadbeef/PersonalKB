---
tags: [raw, programming-languages, rust-deep-dive]
source: "The Rust Programming Language (Klabnik & Nichols), Rust Reference, Rustonomicon"
created: 2025-07-25
---

# raw-pl-021: Rust Deep Dive — Ownership, Traits, and Async

## The Ownership Model in Detail

Every value has exactly one owner. Ownership transfers on assignment (move semantics). When the owner goes out of scope, the value is dropped (destructor runs, memory freed).

**Move vs Copy:** Types implementing Copy (integers, floats, bools, tuples of Copy types) are copied on assignment. All other types are moved — the original binding becomes invalid after the move. This prevents double-free: only one owner can drop the value.

**Borrowing rules:**
1. You can have many shared references (&T) OR one mutable reference (&mut T), never both simultaneously
2. References must not outlive the data they point to (lifetime checking)

These two rules, enforced at compile time, prevent: data races (shared xor mutable), use-after-free (lifetime checking), and dangling pointers (borrow checker).

## Lifetimes

Lifetimes are annotations telling the compiler how long references are valid. Usually inferred; sometimes explicit:
`ust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str
`
This says: the returned reference lives as long as the shorter of the two input references.

Lifetimes are Rust's most confusing feature. They encode information that C programmers track mentally and frequently get wrong. The borrow checker automates this tracking.

## Traits: Rust's Polymorphism

Traits define shared behavior:
- impl Display for Point { ... } — Point can be printed
- n print<T: Display>(item: T) — generic over any printable type
- dyn Display — trait object for dynamic dispatch (vtable)

Traits are coherent: for any type+trait combination, there's at most one implementation. The orphan rule prevents conflicting implementations across crates.

## Async Rust

sync fn returns a Future. .await suspends until the Future completes. Futures are lazy — they do nothing until polled.

The complexity: async Rust interacts with ownership and lifetimes. Pin prevents moving a self-referential Future. Async traits (stabilized in 2023) required years of design work. The ecosystem split between tokio and async-std was a pain point.

Despite the complexity, Rust async is zero-cost: futures compile to state machines with no heap allocation. This makes Rust competitive with C for high-performance network services.

## Error Handling Pattern

`ust
fn read_config() -> Result<Config, Error> {
    let content = fs::read_to_string("config.toml")?;
    let config: Config = toml::from_str(&content)?;
    Ok(config)
}
`

The ? operator propagates errors ergonomically. Each ? either unwraps Ok or returns Err early. Function signatures document all possible errors. The nyhow crate provides convenient error boxing for applications; 	hiserror for libraries.
