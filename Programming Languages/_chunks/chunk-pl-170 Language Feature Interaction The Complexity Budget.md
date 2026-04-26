---
tags: [pl, chunk, design, expressiveness]
up: "[[Programming Paradigms Overview]]"
---

# Language Feature Interaction The Complexity Budget

Every language has a complexity budget. Adding features doesn't just add complexity linearly — feature interactions create exponential complexity.

## The Complexity Equation

```
Complexity = Features + Feature_Interactions
           = N + N*(N-1)/2
```

With 10 features: 10 + 45 interactions = 55 complexity units
With 20 features: 20 + 190 interactions = 210 complexity units
With 40 features: 40 + 780 interactions = 820 complexity units

This is why C++ (hundreds of features) is so much harder to learn than Go (few features).

## Case Studies

### Go: Small Feature Set, Few Interactions
Go has ~25 keywords and deliberately omits:
- Generics (until 1.18, then minimal generics)
- Exceptions, pattern matching, operator overloading, macros, inheritance

Result: Any Go developer can read any Go code. The language fits in one developer's head.

### Rust: Moderate Features, Managed Interactions
Rust has more features than Go but manages interactions carefully:
- Traits interact with generics, lifetimes, and closures
- The borrow checker constrains how features compose
- Each feature addition goes through extensive RFC review

Result: Powerful but learnable — the type system catches most interaction bugs.

### C++: Maximum Features, Explosive Interactions
C++ has accumulated features for 40+ years:
- Templates interact with concepts, constexpr, SFINAE, ADL, overloading...
- Move semantics interact with constructors, assignment, templates, exceptions...
- The number of interactions is staggering

Result: No single person understands all of C++. Style guides restrict which features to use.

### Scala: Feature Overload
Scala 2 suffered from too many ways to achieve the same thing:
- Implicits could be implicit conversions, implicit parameters, or type class instances
- Scala 3 refactored these into separate, clearer features (given/using, extensions, type classes)

## The Simplicity Tax

Simple languages pay a different cost:
- **Go:** Verbose error handling, code duplication (pre-generics)
- **C:** Manual everything, undefined behavior
- **Lua:** Limited standard library

Complex languages pay:
- **C++:** Incomprehensible error messages, massive learning curve
- **Scala 2:** Multiple ways to do everything, inconsistent codebases
- **Haskell:** Monad transformers, language extensions, GHC-specific features

## Key Insight
The best modern languages (Rust, Kotlin, Swift) manage their complexity budget carefully: each feature must justify its interactions with all existing features. Go takes the extreme position that no feature is worth the interaction cost unless absolutely necessary. C++ is the cautionary tale of what happens without a complexity budget.

## References
→ [[Sources Index]]
