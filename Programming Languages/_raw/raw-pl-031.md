---
tags: [pl, raw, dsl, embedded-languages]
up: "[[Sources Index]]"
---

# Raw Note 031 — DSLs and Embedded Languages

## Domain-Specific Languages (DSLs)

### External DSLs
External DSLs have their own syntax and parser, separate from any host language:
- **SQL** — declarative data query, universally supported across languages
- **Regular Expressions** — pattern matching DSL embedded in string literals
- **HTML/CSS** — markup and styling, consumed by browsers
- **GraphQL** — API query language, typed schema definition
- **Terraform HCL** — infrastructure-as-code declarative language

### Internal/Embedded DSLs
Internal DSLs leverage host language syntax to create domain-specific APIs:

**Ruby** — king of internal DSLs thanks to flexible syntax:
- Rails routes: get '/users', to: 'users#index'
- RSpec: describe User do; it "validates email" do; end; end
- Chef recipes: package 'nginx' do; action :install; end

**Kotlin** — designed for DSL creation:
- Type-safe builders: html { body { p { +"Hello" } } }
- Gradle Kotlin DSL: dependencies { implementation("org.lib:name:1.0") }
- Receiver lambdas enable context-sensitive APIs

**Scala** — operator overloading + implicits enable rich DSLs:
- SBT build definitions
- Akka actor definitions
- Parser combinators

**Haskell** — monadic DSLs:
- Parsec parser combinators
- QuickCheck property definitions
- Lens library for data access

**Lisp/Scheme** — macros create true language extensions:
- (defmacro when (test &body body) ...) is indistinguishable from built-in syntax
- Racket takes this furthest with #lang for entirely new languages

### Language Workbenches
- **Racket** — "the language-oriented programming language"
- **JetBrains MPS** — projectional editor for DSL creation
- **Xtext** — framework for developing programming languages on JVM

## Design Trade-offs

| Approach | Pros | Cons |
|----------|------|------|
| External DSL | Clean syntax, domain-optimized | Requires parser, tooling from scratch |
| Internal DSL | Host language tooling, gradual adoption | Constrained by host syntax |
| Language workbench | Full customization, projectional editing | Learning curve, vendor lock-in |

## Key Insight
The best DSL host languages have flexible syntax (Ruby, Kotlin), powerful macros (Lisp, Rust), or both. Go's rigid syntax makes it poor for DSLs. Python's significant whitespace and decorator syntax enable moderate DSL capability.

## References
→ [[Sources Index]]
