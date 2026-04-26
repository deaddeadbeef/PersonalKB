---
tags: [chunk, programming-languages, javascript-typescript]
source: "[[raw-pl-014]]"
---

# chunk-pl-035 JavaScript TypeScript and the Event Loop

**JavaScript's heritage:** Self (prototypes) + Scheme (closures) in C syntax. Created in 10 days, now the most ubiquitous language: browsers, servers, mobile, desktop.

**Single-threaded event loop:** All I/O asynchronous and non-blocking. Evolution: callbacks -> Promises -> async/await. Eliminates data races by construction (one thread). CPU work blocks everything — Web Workers for true parallelism.

**TypeScript revolution:** Anders Hejlsberg layered structural types on JavaScript. All valid JS is valid TS. Structural typing: shape-based compatibility fits duck-typing heritage. Expressive type system: union types, intersection types, mapped types, conditional types, template literal types.

**Prototype-based OOP:** Objects inherit directly from objects (prototype chain). class (ES2015) is sugar over prototypes. Understanding the prototype mechanism is essential for advanced JS.

**The ecosystem:** npm (2M+ packages), Node.js, React/Vue/Angular, Deno, Bun. Largest software ecosystem. Both greatest strength (library for everything) and weakness (dependency sprawl, supply chain attacks).
