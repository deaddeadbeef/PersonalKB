---
tags: [chunk, programming-languages, clojure]
source: "[[raw-pl-028]]"
---

# chunk-pl-090 Clojure Immutable Data and REPL-Driven Development

Rich Hickey's Clojure (2007) thesis: **state is the root of all evil.**

**Immutable persistent data structures:** Hash maps, vectors, sets — all immutable. Modification returns a new structure sharing most data with the original (structural sharing). O(log32 N) access — effectively O(1) for practical sizes.

**Controlled mutation:** When state change is needed:
- **Atoms:** Single value, atomic swap. (swap! counter inc)
- **Refs:** Coordinated multi-value changes via STM (dosync)
- **Agents:** Asynchronous state updates

**JVM interop:** Full access to Java libraries. Call Java from Clojure and vice versa. Access to the entire Maven ecosystem. This practical decision gave Clojure a massive library ecosystem from day one.

**REPL-driven development:** The defining Clojure workflow. Evaluate expressions interactively. Modify running systems. Tighten the feedback loop to seconds. REPL-driven development is more interactive than test-driven development — you explore and verify in real time.

**ClojureScript:** Compile Clojure to JavaScript. Shared code between server (JVM) and client (browser). Re-frame (ClojureScript framework) brings functional reactive programming to the browser.

**The philosophy:** "It is better to have 100 functions operate on one data structure than 10 functions on 10 data structures." Clojure's small set of persistent collections with hundreds of operations is the opposite of OOP's many classes with few methods.
