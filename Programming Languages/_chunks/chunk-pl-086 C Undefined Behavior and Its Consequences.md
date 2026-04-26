---
tags: [chunk, programming-languages, c-systems]
source: "[[raw-pl-010]]"
---

# chunk-pl-086 C Undefined Behavior and Its Consequences

**Undefined behavior (UB):** The C standard says certain operations have no defined result. The compiler may assume they never happen and optimize accordingly.

**Common UB:** Signed integer overflow, null pointer dereference, buffer overflow, use-after-free, data races, division by zero, shift by negative/oversized amount.

**Why UB is dangerous:** The compiler can remove code it proves only executes after UB. A null check if (ptr != NULL) can be removed if the compiler sees ptr was already dereferenced (UB if null, so compiler assumes non-null).

**Real-world impact:** Security vulnerabilities (Heartbleed, countless CVEs), mysterious production bugs, "works in debug, crashes in release" (optimizer exploits UB differently).

**Languages responding to C's UB:**
- **Rust:** No UB in safe code. Unsafe blocks explicitly opt in.
- **Zig:** Well-defined behavior for everything. Integer overflow is detectable error, not UB.
- **Go:** No UB. Runtime panics for out-of-bounds, nil dereference.
- **C++:** Inherits C's UB plus new sources (dangling references, object lifetime).

UB is C's greatest weakness: it makes programs fragile, unpredictable, and vulnerable.
