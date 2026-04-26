---
tags: [chunk, programming-languages, swift-protocols]
source: "[[raw-pl-023]]"
---

# chunk-pl-073 Swift Protocol-Oriented Programming

Apple's recommended paradigm for Swift: protocol-oriented programming (POP).

**Protocols:** Define behavior contracts (like Rust traits). Types conform to protocols.

**Protocol extensions:** Provide default implementations. Any conforming type gets the default unless it overrides. This gives "mixin" behavior without inheritance.

**Associated types:** Protocols can have ssociatedtype — the conforming type provides the concrete type. Enables generic programming at the protocol level.

**Value types + protocols:** Swift encourages structs (value types) conforming to protocols rather than class inheritance. Benefits: no reference counting overhead, no aliasing bugs, copy-on-write for large collections.

**Protocol composition:** unc process(item: Encodable & Sendable) — require multiple protocols.

**Comparison:**
- Like Rust traits: explicit conformance, associated types, default implementations
- Unlike Rust: no orphan rule (any type can conform to any protocol in any module)
- Unlike Java interfaces: can have stored property requirements, work with value types
- Unlike Go interfaces: explicit conformance required (not structural)
