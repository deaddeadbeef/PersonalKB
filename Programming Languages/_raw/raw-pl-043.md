---
tags: [pl, raw, strings, unicode]
up: "[[Sources Index]]"
---

# Raw Note 043 — String and Unicode Handling

## String Representation

| Language | Internal Encoding | Immutable? | Indexing |
|----------|------------------|------------|---------|
| Rust | UTF-8 bytes | Yes (owned String, &str) | By bytes, not chars |
| Go | UTF-8 bytes | Yes | By bytes; range iterates runes |
| Python | UCS-1/2/4 (adaptive) | Yes | By code point (O(1)) |
| Java | UTF-16 (compact strings: Latin1/UTF-16) | Yes | By char (UTF-16 code unit) |
| C# | UTF-16 | Yes | By char (UTF-16 code unit) |
| JavaScript | UTF-16 | Yes | By code unit (not code point!) |
| Swift | UTF-8 (since Swift 5) | Yes (value type) | By Character (grapheme cluster) |
| C | null-terminated bytes | Mutable | By byte |
| Haskell | Lazy linked list of Char (default String) | Yes | By Char (code point), O(n) indexing |
| Elixir | UTF-8 binaries | Yes | By byte; String.graphemes for clusters |

## The Unicode Challenge

### What is a "character"?

The seemingly simple question "what is the length of this string?" has different answers:

The string "é" (e + combining accent):
- **Bytes (UTF-8):** 3
- **Code units (UTF-16):** 2
- **Code points:** 2 (U+0065, U+0301)
- **Grapheme clusters:** 1 (what the user sees as a single character)

The emoji "👨‍👩‍👧‍👦" (family emoji):
- **Bytes (UTF-8):** 25
- **Code points:** 7 (4 people + 3 ZWJ)
- **Grapheme clusters:** 1

### Language Approaches

**Swift** (most correct):
\\\swift
let family = "\u{1F468}\u{200D}\u{1F469}\u{200D}\u{1F467}"
family.count  // 1 (grapheme clusters - correct!)
\\\

**Rust** (explicit choice required):
\\\
ust
let s = "hello";
s.len()           // 5 bytes
s.chars().count()  // 5 code points
// No built-in grapheme API - use unicode-segmentation crate
\\\

**Python** (code point level):
\\\python
s = "👨‍👩‍👧"
len(s)  # 5 (code points, not grapheme clusters)
\\\

**JavaScript** (historically broken):
\\\javascript
"hello".length     // 5 (UTF-16 code units)
"\u{1F468}".length // 2 (surrogate pair counted as 2!)
// Fix: [..."\u{1F468}"].length → 1 (iterator-based)
\\\

## String Concatenation and Building

| Language | Efficient Building | Interpolation |
|----------|--------------------|---------------|
| Rust | \String::push_str\, \ormat!\ | \ormat!("Hello {name}")\ |

| Go | \strings.Builder\ | \mt.Sprintf("Hello %s", name)\ |

| Python | \"".join(list)\, f-strings | \"Hello {name}"\ |

| Java | \StringBuilder\ | \STR."Hello \{name}"\ (Java 21+ preview) |
| JavaScript | Template literals | \\Hello \\\ |
| C# | \StringBuilder\, interpolation | \$"Hello {name}"\ |
| Swift | Native interpolation | \"Hello \(name)"\ |

## Key Insight
Swift's grapheme cluster-based String is the most "correct" but also the most expensive (O(n) for indexing). Rust and Go chose UTF-8 bytes as the unit, forcing developers to be explicit about what "character" means. JavaScript's UTF-16 legacy creates subtle bugs with emoji and non-BMP characters.

## References
→ [[Sources Index]]
