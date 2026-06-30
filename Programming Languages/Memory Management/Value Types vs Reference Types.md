---
tags: [programming-languages, memory-management, value-reference]
up: "[[Memory Management Overview]]"
tier-coverage: full
confidence: plausible
---
# Value Types vs Reference Types

## 🎯 Intuition
**The Core Idea:** Whether a language defaults to copying data or sharing data through references strongly shapes reasoning about state, mutation, and performance.

**Analogy:** Value semantics are like handing someone a photocopy; reference semantics are like handing them access to the same shared whiteboard.

**Why It Matters:** Many bugs and performance surprises come directly from whether assignment makes a new independent value or just another handle to the same underlying object.

## ⚙️ Core Mechanics
### Value Semantics
**Philosophy:** Assignment creates an independent copy. Mutating one variable never affects another. This is the default in C (structs), Go (structs), Rust (all types by default), Swift (structs, enums), and OCaml (immutable values are effectively value-typed).

**Advantages:**
- **Local reasoning:** A function can't mutate your data unless you explicitly pass a mutable reference
- **Thread safety:** Copies don't share state, eliminating data races on copied values
- **Cache-friendly:** Small values live on the stack, close to the code that uses them

**Disadvantages:**
- **Copying cost:** Large data structures are expensive to copy
- **No sharing:** Multiple references to the same data require explicit references/pointers

**Swift's approach** is instructive: structs are value types (copied on assignment), classes are reference types (shared via pointer). This gives programmers a clear choice: use structs for data (Points, Rectangles, Colors) and classes for identity (ViewControllers, NetworkManagers). Swift's copy-on-write (CoW) optimization avoids actual copying until mutation occurs.

**Rust** defaults to value semantics but uses move semantics instead of copying: assignment transfers ownership rather than copying. Explicit `.clone()` is needed for actual deep copies. This makes the cost of copies visible in the code.

### Reference Semantics
**Philosophy:** Variables hold references (pointers) to objects on the heap. Assignment copies the reference, not the data. Multiple variables can refer to the same object.

**Java** uses reference semantics for all objects (`new` always allocates on the heap). Primitives (`int`, `boolean`) are value types for performance. This split creates complexity: autoboxing, `Integer` vs `int`, `equals()` vs `==`.

**Python** uses reference semantics for everything. Variables are names bound to objects. Assignment is always reference copying. This is why `a = [1,2,3]; b = a; b.append(4)` modifies both `a` and `b` — they reference the same list.

**JavaScript** uses reference semantics for objects and arrays, value semantics for primitives. Like Python, object assignment shares rather than copies.

### The Mutation Problem
Reference semantics plus mutation creates aliasing bugs — multiple references to the same mutable data produce surprising behavior. This is the root cause of countless bugs in Java, Python, and JavaScript. The three main solutions:

1. **Immutability (Haskell, OCaml, Clojure):** If data can't be mutated, sharing is always safe. Haskell and OCaml default to immutable values. Clojure's persistent data structures enable efficient "modification" by structural sharing.
2. **Ownership (Rust):** Allow mutation but prevent aliasing. The borrow checker ensures mutable access is exclusive.
3. **Copy-on-Write (Swift):** Share until mutation, then copy. The standard library collections (`Array`, `Dictionary`, `String`) use CoW to get the safety of value semantics with the performance of reference semantics.

### Go's Simple Model
Go structs are value types — they're copied on assignment and when passed to functions. To share, you explicitly use pointers (`*T`). Slices, maps, and channels are reference types (they contain internal pointers). This simplicity is deliberate: Go avoids the class/struct distinction of Swift and the complex value categories of C++ (lvalue, rvalue, xvalue).

### Language Examples
- **Swift:** Structs and enums are value types, classes are reference types, and standard collections use CoW.
- **Rust:** Defaults to value semantics but uses move semantics so copies stay explicit.
- **Go:** Uses value-typed structs plus explicit pointers, with slices, maps, and channels behaving as reference types.
- **Java / Python / JavaScript:** Use reference semantics heavily for objects.
- **OCaml:** Heap-allocated data can still be shared safely in practice because immutable-by-default values avoid aliasing bugs.

## 🔬 Deep Dive
### Trade-offs / Historical Context
Copying versus sharing is not just a low-level implementation detail; it drives API design, mutation safety, concurrency ergonomics, and language complexity.

### Value vs. Reference at a Glance

| Aspect | Value Semantics | Reference Semantics |
|--------|-----------------|---------------------|
| Assignment | Creates an independent copy | Copies a reference to the same object |
| Mutation behavior | Mutating one variable does not affect another | Mutations can be observed through aliases |
| Reasoning style | Strong local reasoning | Aliasing must be tracked |
| Performance risk | Large values can be expensive to copy | Hidden sharing and heap indirection can surprise you |
| Typical examples | C structs, Go structs, Rust values, Swift structs/enums | Java objects, Python objects, JavaScript objects/arrays |

### OCaml's Immutable-by-Default
OCaml's approach is distinctive: most data is immutable and heap-allocated, but the GC handles lifetime. Since immutable data can be freely shared without aliasing bugs, OCaml achieves much of what Rust's ownership provides through a completely different mechanism — immutability. Mutable data exists (`ref`, mutable record fields) but is used sparingly, making aliasing bugs rare in practice.

### The C++ Value Category Complexity
C++ has the most complex value/reference model: lvalues, rvalues, xvalues, prvalues, and glvalues, plus move semantics, perfect forwarding, and RVO (Return Value Optimization). This complexity exists because C++ tries to give programmers maximum control over when data is copied, moved, or referenced — at the cost of one of the steepest learning curves in programming.

## 🏋️ Practice
1. Why does `a = [1,2,3]; b = a; b.append(4)` change both names in Python, and what value-semantics mental model would prevent that surprise?
2. Compare Swift's copy-on-write collections with Rust's move semantics. How does each reduce the practical cost of value-oriented programming?
3. Choose a Java or JavaScript API that passes mutable objects around. How would immutability or ownership reduce aliasing bugs in that design?

## References

- [[Sources Index]]
