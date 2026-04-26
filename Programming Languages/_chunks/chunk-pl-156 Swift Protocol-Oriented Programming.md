---
tags: [pl, chunk, swift, protocol-oriented]
up: "[[Swift – Language Profile]]"
---

# Swift Protocol-Oriented Programming

Swift's protocol-oriented programming (POP) was introduced at WWDC 2015 as a paradigm shift away from class-based OOP.

## The Core Idea

Instead of class hierarchies with inheritance, use protocols (interfaces) with default implementations:

```swift
// Protocol with associated type
protocol Container {
    associatedtype Element
    var count: Int { get }
    mutating func append(_ item: Element)
    subscript(i: Int) -> Element { get }
}

// Default implementation via extension
extension Container {
    var isEmpty: Bool { count == 0 }
    func describe() -> String { "Container with \(count) elements" }
}

// Structs conform to protocols (no inheritance needed)
struct Stack<T>: Container {
    var items: [T] = []
    var count: Int { items.count }
    mutating func append(_ item: T) { items.append(item) }
    subscript(i: Int) -> T { items[i] }
}
```

## Why Protocols Over Classes

| Property | Classes (OOP) | Protocols (POP) |
|----------|--------------|-----------------|
| Semantics | Reference type | Value type compatible |
| Inheritance | Single inheritance | Multiple protocol conformance |
| Dispatch | Dynamic (vtable) | Static (when possible) |
| Extension | Subclass | Protocol extension |
| Testing | Mock via subclass | Mock via protocol conformance |

## Swift's Protocol Innovations

### Protocol Extensions (Swift 2+)
Add default implementations to protocols:
```swift
extension Collection where Element: Numeric {
    func sum() -> Element { reduce(0, +) }
}
// Now every Collection of numbers gets sum() for free
[1, 2, 3].sum() // 6
```

### Existential Types (Swift 5.7+)
```swift
// `any` keyword makes protocol usage as a type explicit
func process(items: [any Container]) { ... }
// `some` for opaque return types
func makeContainer() -> some Container { Stack<Int>() }
```

### Protocol Witnesses
Swift's compiler uses witness tables (similar to Rust's vtables) for dynamic dispatch, but can optimize to static dispatch when the concrete type is known.

## Comparison with Rust Traits

| Feature | Swift Protocols | Rust Traits |
|---------|----------------|-------------|
| Associated types | Yes | Yes |
| Default implementations | Yes (extensions) | Yes (default methods) |
| Dynamic dispatch | `any Protocol` | `dyn Trait` |
| Static dispatch | `some Protocol` | Generics with trait bounds |
| Conditional conformance | Yes | Yes (where clauses) |
| Retroactive conformance | Yes (extensions) | Yes (impl for foreign types, with orphan rule) |

## Key Insight
Swift's protocol-oriented programming is essentially the same insight as Rust's trait system: prefer composition over inheritance, use protocols/traits for polymorphism, and enable value types to participate. Swift's contribution was marketing this as a paradigm and making it accessible to the Apple developer community.

## References
→ [[Sources Index]]
