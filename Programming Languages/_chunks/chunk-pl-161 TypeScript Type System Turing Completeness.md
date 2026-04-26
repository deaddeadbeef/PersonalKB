---
tags: [pl, chunk, javascript, typescript]
up: "[[JavaScript and TypeScript Language Profile]]"
---

# TypeScript Type System Turing Completeness

TypeScript's type system is Turing-complete — you can compute arbitrary logic at the type level. This is both its greatest power and its most dangerous feature.

## Type-Level Programming

### Template Literal Types
```typescript
type Route = `/${"users" | "posts"}/${"create" | "delete"}`;
// Route = "/users/create" | "/users/delete" | "/posts/create" | "/posts/delete"
```

### Recursive Conditional Types
```typescript
type DeepReadonly<T> = {
    readonly [P in keyof T]: T[P] extends object ? DeepReadonly<T[P]> : T[P];
};
// Recursively makes every property readonly, at any depth
```

### Type-Level Arithmetic
```typescript
type BuildTuple<L extends number, T extends any[] = []> =
    T['length'] extends L ? T : BuildTuple<L, [...T, any]>;
type Add<A extends number, B extends number> =
    [...BuildTuple<A>, ...BuildTuple<B>]['length'];
type Result = Add<3, 4>; // 7 at the type level!
```

## Why This Exists

TypeScript must type JavaScript's extremely dynamic patterns:
```javascript
// Express.js route parameters
app.get("/users/:id/posts/:postId", (req, res) => {
    req.params.id;      // TypeScript must infer this exists
    req.params.postId;  // And this too
});
```

To type this correctly, TypeScript needs to parse string literals at the type level.

## The Dark Side

Type-level computation can make:
- Error messages incomprehensible (pages of expanded types)
- IDE performance sluggish (type checker doing heavy computation)
- Types harder to read than the code they describe

## Comparison

| Language | Type-Level Power | Compile-Time Logic |
|----------|-----------------|-------------------|
| TypeScript | Turing-complete types | Conditional, mapped, template literal types |
| Haskell | Very powerful | Type families, GADTs, DataKinds |
| Rust | Limited | Const generics, associated types |
| C++ | Turing-complete | Template metaprogramming, constexpr |
| Go | Minimal | Type constraints only |
| Zig | Full language | Comptime (not type-level, compile-time execution) |

## Key Insight
TypeScript's powerful type system exists because JavaScript is so dynamic that simpler type systems can't accurately describe existing code. It's a case where the type system evolved to match the language's complexity, not the other way around.

## References
→ [[Sources Index]]
