---
tags: [chunk, programming-languages, string-handling]
source: "[[raw-pl-010]]"
---

# chunk-pl-104 String Handling Across Languages

String design reveals language philosophy:

**C:** Null-terminated char arrays. No length tracking. Buffer overflows everywhere. Fast but dangerous. strlen() is O(n).

**C++:** std::string (owned, heap-allocated) and std::string_view (borrowed, non-owning). SSO (Small String Optimization) avoids heap for short strings.

**Rust:** String (owned, heap, UTF-8) and &str (borrowed slice, UTF-8). No indexing by character position (UTF-8 is variable-width). String operations are explicit about encoding.

**Go:** Strings are immutable byte slices (usually UTF-8). []byte for mutable. Simple but no character-level indexing.

**Python:** Strings are immutable Unicode sequences. Rich operations (split, join, format). f-strings for interpolation. No distinction between owned and borrowed.

**Java:** String (immutable, UTF-16 internally). StringBuilder for efficient concatenation. String interning for literals.

**Haskell:** String is [Char] (linked list of characters — slow). Text (packed UTF-16) and ByteString (packed bytes) for performance. The string type situation is Haskell's most confusing aspect for newcomers.

**The UTF-8 everywhere movement:** Rust, Go, and modern practice favor UTF-8 as the internal representation. Java and Windows use UTF-16 (historical). UTF-8 is more compact for ASCII-heavy text and is the web standard.
