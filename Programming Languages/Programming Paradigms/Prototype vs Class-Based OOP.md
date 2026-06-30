---
tags: [programming-languages, paradigms, prototype-class]
up: "[[Programming Paradigms Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Prototype vs Class-Based OOP

> OOP splits into two inheritance models — class-based (objects are instances of blueprints) and prototype-based (objects inherit directly from other objects) — revealing deep assumptions about abstraction and flexibility.

---

## 🎯 Intuition

### Core Idea

Object-oriented programming splits into two fundamentally different inheritance models: class-based (objects are instances of classes) and prototype-based (objects inherit directly from other objects). This distinction reveals deep assumptions about abstraction and flexibility.

### Analogy

**Class-based OOP** = building houses from blueprints. An architect draws up plans (the class), and every house built from those plans shares the same layout. Want a different layout? Draw a new blueprint, possibly extending an existing one.

**Prototype-based OOP** = copying your neighbor's house and making modifications — no blueprints needed. You point at a concrete, working house and say "make mine like that, but with an extra room." There is no separate plan; the existing house *is* the plan.

### Why It Matters

The model you choose shapes how you think about code reuse, extensibility, and system design. Class-based thinking asks "What category does this belong to?" while prototype-based thinking asks "What existing thing is this similar to?" Understanding both unlocks fluency across languages like Java, Python, JavaScript, Lua, and the modern trait-based alternatives.

---

## ⚙️ Core Mechanics

### How It Works

**Class-Based Model:** A class is a blueprint defining the structure (fields) and behavior (methods) of its instances. Objects are created by instantiating a class. Classes form inheritance hierarchies — a subclass inherits from a superclass, overriding or extending behavior.

**Prototype-Based Model:** There are no classes — only objects. An object can inherit directly from another object (its prototype). To create a new kind of object, you clone an existing one and modify it. The prototype chain provides method lookup: if an object doesn't have a property, its prototype is checked, then the prototype's prototype, and so on.

### Key Concepts

| Dimension | Class-Based | Prototype-Based |
|---|---|---|
| Fundamental unit | Class (abstract blueprint) | Object (concrete exemplar) |
| Object creation | Instantiate a class | Clone an existing object |
| Inheritance | Subclass → superclass hierarchy | Prototype chain (object → object) |
| Reuse mechanism | Extend / override in subclasses | Delegate up the prototype chain |
| Flexibility | Rigid — new kind requires new class | Fluid — modify any object at runtime |
| Structure | Hierarchy decisions made upfront | No upfront hierarchy needed |
| Tooling | IDE-friendly — navigable hierarchies | Harder to analyze statically |
| Type safety | Type systems reason about class relationships (subtyping, generics) | No type system enforcement of relationships |
| Failure mode | Over-engineering / wrong abstraction | Under-structuring / spaghetti delegation |
| Classic pitfall | Diamond problem (multiple inheritance ambiguity) | Confused identity (what *is* this object?) |

### Language Examples

**Class-Based:** Java, C++, C#, Python, Ruby, Kotlin, Swift, OCaml (optionally)

**Prototype-Based:** JavaScript, Lua, Self, Io

**Modern Alternatives (neither model):**
- **Rust** — Traits provide polymorphism without classes or prototypes. No inheritance — only trait implementation.
- **Go** — Interfaces define behavior contracts. Struct embedding provides code reuse. No inheritance hierarchy.
- **Haskell** — Type classes define ad-hoc polymorphism. No objects, no prototypes.
- **OCaml** — Has optional class-based OOP but the community overwhelmingly prefers modules and functors for abstraction.

### Key Facts

- **Class-based advantages:** Clear structure for large codebases — classes provide organizational units. IDE tooling works well — class hierarchies are navigable and searchable. Type systems can reason about class relationships. Design patterns provide proven solutions for common problems.
- **Class-based disadvantages:** Rigid — creating a new kind of object requires defining a new class. Hierarchy decisions must be made upfront and are expensive to change. Diamond problem: multiple inheritance creates ambiguity (which parent's method?). Class hierarchies often model the wrong abstraction.
- **Prototype-based advantages:** More flexible — no upfront hierarchy design needed. Objects can be modified at runtime. Simpler mental model (only objects, no meta-layer of classes).
- **Prototype-based disadvantages:** Less structured — no type system enforcement of relationships. Harder for tooling to analyze. Can lead to unclear object identity and delegation chains.
- **JavaScript's Prototype System:** JavaScript is the only mainstream prototype-based language. Every object has a hidden `[[Prototype vs Class-Based OOP|Prototype]]` link to another object. Method calls traverse the prototype chain until found or exhausted. Constructor functions and `Object.create()` set up prototype relationships. JavaScript added `class` syntax in ES2015, but it's syntactic sugar over prototypes — the underlying mechanism is unchanged. This caused confusion: JavaScript looks class-based but behaves prototype-based. Understanding this distinction is essential for advanced JavaScript programming.

---

## 🔬 Deep Dive

### Formal Foundations — The Philosophical Divide

**Class-based thinking:** "What category does this belong to?" Objects are instances of abstract categories. A Dog IS-A Animal IS-A LivingThing. Taxonomy drives design.

**Prototype-based thinking:** "What existing thing is this similar to?" Objects are concrete exemplars. This dog is like that dog, with some differences. Cloning drives design.

Prototype-based OOP is more flexible (no upfront hierarchy design needed) but less structured (no type system enforcement of relationships). Class-based OOP provides more safety and organization at the cost of rigidity.

At its root this is a debate between *Platonic idealism* (classes as ideal forms, objects as imperfect instances) and *Wittgensteinian family resemblance* (no fixed category — just overlapping similarities between concrete examples).

### Trade-offs and Design Decisions — Modern Alternatives

Several modern languages reject both models entirely. Rust uses traits, Go uses interfaces with struct embedding, Haskell uses type classes, and OCaml's community prefers modules and functors over its optional class system.

These languages suggest that the class-vs-prototype debate may be less important than the broader question: do you need inheritance-based polymorphism at all, or are traits/interfaces/type classes sufficient?

### Historical Context

Self (1986, Ungar and Smith at Xerox PARC) pioneered prototype-based OOP. Its core insight: classes are unnecessary overhead. An object already demonstrates what it does — why create a separate class to describe it? Self's influence on JavaScript came through Brendan Eich, who was familiar with Self's research. JavaScript (1995) became the only mainstream prototype-based language, later adding `class` syntax in ES2015 as sugar over its prototype core.

---

## 🏋️ Practice

### Warm-Up

1. In a class-based language, what happens when you call a method that isn't defined on the subclass but exists on the superclass? Trace the lookup path.
2. In JavaScript, what is the difference between `Object.create(proto)` and using the `new` keyword with a constructor function? Which prototype chain does each produce?
3. Explain why JavaScript's ES2015 `class` keyword does *not* make JavaScript a class-based language.

### Core Problems

4. Design a small object hierarchy (e.g., `Shape → Circle, Rectangle`) once using class-based inheritance (Python or Java) and once using prototype delegation (JavaScript with `Object.create`). Compare: how does adding a new shape type differ between the two approaches?
5. The "diamond problem" occurs in class-based multiple inheritance. Does an equivalent problem exist in prototype-based languages? Construct or argue against a scenario in JavaScript's single-prototype-chain model.

### Challenge

6. Several modern languages (Rust, Go, Haskell) reject both class-based and prototype-based OOP. Pick one and demonstrate how it achieves polymorphism and code reuse without inheritance. Then argue: is there a category of problem where prototype-based or class-based OOP remains genuinely superior to the trait/interface/type-class approach?

---

*See also:* [[Programming Paradigms Overview]]

---

## Supporting Chunks / References

- [[Sources Index]]

## References
- [[Programming Languages/Sources/Sources Index|Programming Languages Sources Index]]
