---
tags: [chunk, programming-languages, prototype-oop]
source: "[[raw-pl-017]]"
---

# chunk-pl-056 Prototype vs Class-Based OOP

**Class-based (Java, C++, C#, Python, Ruby):** Class is blueprint. Objects are instances. Inheritance hierarchies. Type system reasons about class relationships. Clear structure for large codebases. Rigid — changes to base class can break subclasses.

**Prototype-based (JavaScript, Lua, Self):** No classes — objects inherit from objects. Clone existing objects and modify. Prototype chain for method lookup. Flexible — no upfront hierarchy needed.

JavaScript is the only mainstream prototype-based language. class (ES2015) is syntactic sugar — the underlying mechanism is still prototype chains. Self (1986) pioneered this; Brendan Eich brought it to JavaScript.

**Philosophical divide:** Class-based asks "what category is this?" (taxonomy). Prototype-based asks "what is this similar to?" (exemplars).

**Modern alternatives:** Rust (traits, no inheritance), Go (interfaces + embedding), Haskell (type classes), OCaml (modules preferred over optional OOP). These suggest the class-vs-prototype debate matters less than: do you need inheritance at all?
