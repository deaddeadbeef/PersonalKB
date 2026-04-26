---
tags: [pl, chunk, strings, unicode]
up: "[[Type Systems Overview]]"
---

# Unicode String Handling The Hardest Easy Problem

String handling reveals deep language design philosophy differences. The question "what is a character?" has no universally correct answer.

## The Four Levels of Text

1. **Bytes:** Raw encoded data (UTF-8: variable 1-4 bytes per code point)
2. **Code units:** Encoding-specific units (UTF-16: 2 bytes each, may need pairs)
3. **Code points:** Unicode scalar values (U+0000 to U+10FFFF)
4. **Grapheme clusters:** What users perceive as "characters"

Example: The flag emoji (US flag):
- 8 bytes (UTF-8), 4 code units (UTF-16), 2 code points, 1 grapheme cluster

## Language Choices

**Swift — Grapheme-correct (most principled):**
- String count returns grapheme clusters
- O(n) for count and indexing (must scan the string)
- The only mainstream language that gets this right by default

**Rust — Byte-oriented (explicit):**
- len() counts bytes, .chars() iterates code points
- No built-in grapheme support — unicode-segmentation crate needed
- Forces developers to choose what "character" means

**JavaScript — UTF-16 legacy (broken):**
- Emoji.length returns 2 (surrogate pair counted as 2 characters)
- Fix: [...emoji].length returns 1 (iterator-based)
- Decades of legacy code assumes 1 char = 1 unit

**Go — UTF-8 pragmatic:**
- len("hello") returns bytes; range iterates runes (code points)
- Rob Pike co-invented UTF-8, so Go is deeply UTF-8 native

## Key Insight
There's no free lunch: Swift's correctness costs O(n) indexing. Rust's explicitness requires developer knowledge. JavaScript's legacy creates subtle bugs. The best approach is Rust's: make the choice explicit and let developers pick the right abstraction for their use case.

## References
→ [[Sources Index]]
