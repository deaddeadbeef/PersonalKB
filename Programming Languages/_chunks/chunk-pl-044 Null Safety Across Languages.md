---
tags: [chunk, programming-languages, null-safety]
source: "[[raw-pl-029]]"
---

# chunk-pl-044 Null Safety Across Languages

Tony Hoare called null references his "billion-dollar mistake." Languages that eliminated null:

**Rust:** Option<T> — Some(value) or None. No null. Compiler forces handling None case.
**Haskell:** Maybe a — Just value or Nothing. No null.
**Kotlin:** T (non-nullable) vs T? (nullable). Smart casts: after null check, variable is automatically non-null. Safe call (?.), elvis (?:).
**Swift:** T vs T? (Optional). if let, guard let, optional chaining (?.). Force-unwrap (!) discouraged.

**Languages still with null:** Java (mitigated by Optional, @Nullable annotations), Go (nil for pointers, slices, maps, channels, interfaces), C/C++ (null pointers everywhere), Python (None is universal), JavaScript (both null AND undefined).

The pattern: newer languages eliminate null at the type level. Older languages retrofit optional types and annotations. Null safety is the lowest-hanging fruit in type system design — it eliminates the single most common class of bugs.
