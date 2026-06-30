---
tags: [programming-languages, paradigms, oop]
up: "[[Programming Paradigms Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Object-Oriented Programming Philosophies

> Object-oriented programming is not a single philosophy but a family of related ideas that different languages interpret very differently — the gap between Smalltalk's pure OOP and Java's industrial OOP is as wide as between C and Haskell.

---

## 🎯 Intuition

### Core Idea

OOP organizes software around **objects** — bundles of data and the procedures that operate on that data — rather than around functions and logic. Different language communities disagree sharply on what this means in practice.

### Analogy

OOP is like **organizing a company where each department has its own data and procedures, communicates through memos, and new departments clone existing ones with modifications**. Smalltalk's vision is a company where every memo is a polite request that the department can interpret however it likes; Java's vision is a company with a strict org chart, job descriptions, and formal inter-department protocols.

### Why It Matters

OOP is the dominant paradigm in industry. Understanding its *different* philosophies — not just the Java/C# flavor — prevents cargo-culting patterns, reveals when to reach for alternative paradigms, and explains why modern languages are moving away from deep inheritance toward composition and traits.

---

## ⚙️ Core Mechanics

### How It Works

Two major lineages define OOP:

**Smalltalk lineage (message-oriented OOP):** Alan Kay coined "object-oriented programming" in the context of Smalltalk (1972). Everything is an object — numbers, booleans, classes, even code blocks. Objects communicate via messages: you don't call methods, you send messages and the object decides how to respond. Late binding everywhere means the receiver determines behavior at runtime, enabling maximum flexibility. The system is live — objects exist in a running image, modified interactively.

**Industrial lineage (class-oriented OOP):** Java (1995) and C# (2000) popularized a very different form. Classes serve as blueprints — every object is an instance of a class that defines its structure and behavior. Classes form tree-shaped IS-A inheritance hierarchies. Encapsulation is enforced via access modifiers (public, private, protected). Static typing with nominal subtyping means type compatibility is based on declared class relationships. This model prioritizes code organization for large teams, IDE tooling (autocomplete, refactoring), and design patterns (Factory, Observer, Strategy). The "Gang of Four" patterns book (1994) codified best practices for this style.

### Key Concepts

| Style | Dispatch | Typing | Polymorphism | Inheritance | Philosophy |
|---|---|---|---|---|---|
| Smalltalk | Message sends; receiver decides | Dynamic | Via message protocol | Single; class-based | "Messaging is the big idea" |
| Java / C# | Virtual method tables | Static, nominal | Interfaces + subclassing | Single class + interfaces | Organization & tooling |
| C++ | Virtual when requested | Static, nominal | Templates + virtual | Multiple | "Don't pay for what you don't use" |
| Python | Attribute lookup (MRO) | Dynamic, duck typing | Duck typing | Multiple (C3 linearization) | Pragmatic — classes when they help |
| Ruby | Message sends (Smalltalk-inspired) | Dynamic, duck typing | Duck typing + open classes | Single + mixins | "Programmer happiness" |

### Language Examples

**Smalltalk:** Everything is an object — numbers, booleans, classes, code blocks. Objects communicate via messages; the receiver decides how to respond. The system is a live, running image modified interactively. Kay later said: "I made up the term 'object-oriented' and I can tell you I did not have C++ in mind." His vision was about messaging and late binding, not classes and inheritance.

**Java / C#:** Classes as blueprints with inheritance hierarchies, access modifiers, and nominal subtyping. Optimized for large teams, IDE tooling, and codified design patterns.

**C++ (1985):** Added OOP to C as an additional paradigm, not a replacement. You can write C++ without classes. The philosophy of "don't pay for what you don't use" means OOP is opt-in and performance-oriented: virtual dispatch only when explicitly requested (`virtual` keyword), objects can live on the stack (no mandatory heap allocation), and templates provide compile-time polymorphism without virtual dispatch overhead.

**Python:** Everything is an object (like Smalltalk) but classes use C3 linearization for multiple inheritance, and duck typing replaces interface declarations. Python's OOP is pragmatic — use classes when they help, use functions when they don't.

**Ruby:** "Programmer happiness" OOP inspired by Smalltalk. Everything is an object including primitives. Open classes allow modifying existing classes at runtime. Blocks and procs are objects. Matz chose to optimize for the programmer's experience rather than the machine's.

### Key Facts

The major critiques of OOP expose real design trade-offs:

1. **Inheritance fragility:** Deep inheritance hierarchies are brittle. Changing a base class can break subclasses in subtle ways. Modern advice: "prefer composition over inheritance."
2. **Banana-gorilla problem:** "You wanted a banana but what you got was a gorilla holding the banana and the entire jungle" (Joe Armstrong) — objects carry too much context.
3. **Kingdom of Nouns:** Java's OOP forces everything into a class, creating AbstractSingletonProxyFactoryBean-style naming. Sometimes a function is just a function.
4. **Shared mutable state:** OOP encourages encapsulating mutable state in objects, which becomes problematic with concurrency.

---

## 🔬 Deep Dive

### Formal Foundations

Alan Kay's original vision centered on **messaging**, not on classes or inheritance. In Kay's model, objects are like biological cells or networked computers: autonomous entities communicating through messages. The receiver has full autonomy over how — or whether — to respond. This makes the *protocol* (the set of messages an object understands) the fundamental abstraction, not the class hierarchy. Smalltalk demonstrated that a tiny set of primitives (objects, messages, closures) could build an entire computing environment, from the UI toolkit to the compiler to the debugger, all within a live image.

The industrial model shifted the emphasis from messaging to **classification**. Java's type system treats the class as the unit of abstraction: types are defined by their position in the inheritance tree (nominal subtyping), and the compiler enforces contracts at compile time. This gained safety and tooling support at the cost of the flexibility Kay envisioned.

### Trade-offs and Design Decisions

Modern languages have internalized the critiques and are evolving OOP accordingly:

- **Kotlin and Swift:** Prefer composition (extensions, protocols) over inheritance
- **Rust:** Has no class inheritance at all — traits provide polymorphism without hierarchies
- **Go:** No classes, no inheritance — just interfaces and struct embedding
- **OCaml:** Has OOP as an optional feature, rarely used in practice; the ML-style module system is preferred

The trend is clear: newer languages retain objects and encapsulation but discard deep inheritance in favor of trait/interface-based composition. The "objects + messaging" core of Kay's vision is converging with the "types + composition" core of functional programming.

### Historical Context

- **1967:** Simula introduces classes and inheritance for simulation modeling
- **1972:** Smalltalk-72 — Kay coins "object-oriented"; messaging is the core idea
- **1985:** C++ — Stroustrup adds OOP to C, emphasizing zero-overhead abstractions
- **1994:** "Gang of Four" *Design Patterns* codifies industrial OOP best practices
- **1995:** Java — Sun standardizes class-based OOP for enterprise development
- **2000:** C# — Microsoft's answer to Java, same class-based model
- **2010s–present:** Rust, Go, Kotlin, Swift move toward traits/interfaces and composition, away from inheritance hierarchies

---

## 🏋️ Practice

### Warm-Up

1. In Smalltalk, what happens when you send a message to an object that doesn't understand it — and how does this differ from calling a non-existent method in Java?
2. Explain the "banana-gorilla problem" in your own words. Give a concrete code example where pulling in one object drags along unwanted dependencies.
3. Why does C++ require the `virtual` keyword for polymorphic dispatch, while Java makes all non-static methods virtual by default? What design philosophies do these choices reflect?

### Core Problems

1. **Refactoring exercise:** Take a three-level inheritance hierarchy (e.g., `Animal → Dog → GuideDog`) and redesign it using composition and interfaces/traits. Identify which behaviors belong in composed components versus the object itself. Discuss what you gain and what you lose.
2. **Cross-paradigm comparison:** Implement a simple "shape area" calculator in both a class-hierarchy style (Java/C#) and a tagged-union-with-pattern-matching style (Rust/OCaml). Compare the two designs on extensibility: which is easier to extend with new shapes? Which is easier to extend with new operations?

### Challenge

1. **Design a messaging system:** Implement a Smalltalk-style message-passing object system in Python or Ruby. Objects should be dictionaries (or open structs) that receive string message names and argument lists, look up handlers dynamically, and fall back to a `doesNotUnderstand` / `method_missing` handler. Demonstrate late binding, delegation, and prototype-based "inheritance" without using language-level classes. Reflect on what this reveals about Kay's original OOP vision versus industrial OOP.

---

*See also:* [[Programming Paradigms Overview]]

---

## Supporting Chunks / References

- [[Sources Index]]

## References
- [[Programming Languages/Sources/Sources Index|Programming Languages Sources Index]]
