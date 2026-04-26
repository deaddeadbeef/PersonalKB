---
tags: [chunk, programming-languages, reference-counting]
source: "[[raw-pl-002]]"
---

# chunk-pl-079 Reference Counting Swift ARC and Python

**How it works:** Each object tracks how many references point to it. When count reaches zero, object is freed immediately. Deterministic destruction — resource cleanup happens at a predictable point.

**Swift ARC (Automatic Reference Counting):** Compiler inserts retain/release calls at compile time. No GC pauses. Deterministic. Works well for most cases. **The cycle problem:** Two objects referencing each other keep both alive forever. Solution: weak references (nil when referent is freed) and unowned references (crash if accessed after freed).

**Python:** Reference counting as primary GC. Every object has ob_refcnt. Most objects freed immediately when last reference dropped. Cycle detector runs periodically to handle circular references. The GIL makes ref counting thread-safe (each increment/decrement is atomic under the GIL).

**Objective-C ARC:** Same as Swift ARC. Manual retain/release before ARC was error-prone. ARC automates what programmers did manually.

**Comparison with tracing GC:** Ref counting: deterministic, no pauses, but cycle-prone and count-update overhead. Tracing GC (Java, Go): handles cycles automatically, better throughput, but pauses and non-deterministic destruction.

**Rust approach:** No ref counting by default. Ownership handles most cases. Rc<T>/Arc<T> for explicit reference counting when needed.
