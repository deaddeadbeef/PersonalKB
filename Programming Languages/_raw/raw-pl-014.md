---
tags: [raw, programming-languages, web-languages]
source: "JavaScript: The Good Parts (Crockford), TypeScript documentation, MDN Web Docs"
created: 2025-07-25
---

# raw-pl-014: JavaScript/TypeScript and the Web Platform

## JavaScript's Unlikely Rise

Created in 10 days by Brendan Eich (1995). Originally a simple scripting language for web pages. Now the world's most ubiquitous language: browsers, servers (Node.js), mobile (React Native), desktop (Electron), edge computing, IoT.

JavaScript's unique heritage: Self (prototypes) + Scheme (closures, first-class functions) in C-like syntax. This combination was accidental genius — first-class functions and closures made JavaScript surprisingly suitable for event-driven, callback-heavy programming.

## The Language Quirks

JavaScript's hasty design created infamous quirks: 	ypeof null === "object", [] + [] === "", "" == 0 is true. Implicit type coercion is the source of most JavaScript confusion. Strict mode and TypeScript mitigate but don't eliminate these issues.

The 	his keyword's binding rules are notoriously confusing: depends on how a function is called (method, constructor, arrow function, explicit binding). Arrow functions (ES2015) solved this by capturing the enclosing 	his.

## TypeScript's Revolution

Anders Hejlsberg (also designer of C# and Turbo Pascal) created TypeScript (2012) as a strict superset of JavaScript with static types. Key insight: don't restrict JavaScript — add information.

TypeScript's structural type system is one of the most expressive in any mainstream language: union types (string | number), intersection types, literal types, mapped types, conditional types, template literal types, and discriminated unions. This expressiveness is necessary because TypeScript must type JavaScript's dynamic patterns.

## The Event Loop Model

JavaScript is single-threaded with an event loop. All I/O is asynchronous and non-blocking. The evolution: callbacks → Promises → async/await. This model eliminates data races by construction (one thread, no shared mutable state) but means CPU-intensive work blocks everything.

Web Workers and Node.js worker_threads provide true parallelism when needed, but the default model is cooperative single-threaded concurrency.

## The Ecosystem

npm has 2M+ packages — the largest software registry. This is both JavaScript's greatest strength (a library for everything) and greatest weakness (dependency sprawl, supply chain attacks, left-pad incident).

Frontend frameworks (React, Vue, Angular, Svelte), backend frameworks (Express, Fastify, NestJS), and meta-frameworks (Next.js, Nuxt, SvelteKit) form a massive ecosystem.

Node.js (2009) brought JavaScript to the server. Deno (2020, also by Ryan Dahl) and Bun (2022, written in Zig) are next-generation runtimes with TypeScript support, better security, and faster startup.
