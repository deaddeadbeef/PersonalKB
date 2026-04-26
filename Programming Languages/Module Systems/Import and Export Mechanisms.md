---
tags: [programming-languages, module-systems, imports]
up: "[[Module Systems Overview]]"
tier-coverage: full
---

# Import and Export Mechanisms

## 🎯 Intuition

**The Core Idea:** How a language brings names into scope (importing) and makes them available to others (exporting) shapes the developer's daily experience with code organisation.

**Analogy:** Importing is like choosing items from a catalogue and placing them on your workbench — you can grab the whole catalogue (wildcard), pick individual tools (named imports), or give them nicknames (aliases). Exporting is deciding which of your finished products go on the shelf for others to pick up.

**Why It Matters:** The syntax and semantics of imports vary surprisingly across languages, reflecting different philosophies about explicitness, convenience, and namespace pollution. Choosing the right import style prevents name clashes, aids readability, and enables tooling like tree-shaking.

## ⚙️ Core Mechanics

### Explicit Imports: Python, Rust, Java

**Python** offers multiple import styles:
- `import os` — qualified access: `os.path.join()`
- `from os.path import join` — direct access: `join()`
- `from os.path import *` — wildcard import (discouraged)
- `import numpy as np` — aliased import (idiomatic for common libraries)

Python's philosophy: explicit is better than implicit, but convenience matters. Star imports are available but linting tools flag them.

**Rust** uses `use` declarations with explicit paths:
- `use std::collections::HashMap;`
- `use crate::module::*;` (glob import, discouraged in libraries)
- `use std::io::{self, Read, Write};` (grouped imports)

Rust requires declaring `use` for every imported name. Items not `use`d must be referenced by full path. This is maximally explicit — you can always trace where a name comes from.

**Java** imports classes by fully qualified name:
- `import java.util.List;`
- `import java.util.*;` (wildcard import)
- `import static java.lang.Math.PI;` (static import)

Java's import is just a name shortening mechanism — `import java.util.List` means "when I write `List`, I mean `java.util.List`." This is less flexible than Python's renaming imports.

### Implicit Imports: Go, Haskell

**Go** automatically imports everything from an imported package's exported namespace:
- `import "fmt"` — use as `fmt.Println()`
- `import . "fmt"` — dot import: use as `Println()` (strongly discouraged)

Go enforces that all imports must be used — unused imports are compilation errors. This keeps code clean but can be annoying during development (goimports tool auto-manages imports).

**Haskell** imports are module-level:
- `import Data.Map` — imports all exported names
- `import Data.Map (Map, lookup, insert)` — import specific names
- `import qualified Data.Map as Map` — qualified access only
- `import Data.Map hiding (map)` — import everything except `map`

Haskell's qualified imports are the recommended style for avoiding name clashes in a language where short function names (map, filter, head) are pervasive.

### OCaml Opens

OCaml uses `open` to bring a module's names into scope:
- `open List` — all names from List module available unqualified
- `let open List in ...` — local open (scoped)
- `List.(map f xs)` — inline local open (OCaml 4.01+)

OCaml's philosophy: modules should be openable for convenience, but qualified names (`List.map`) are preferred for clarity. The compiler warns about ambiguous opens.

### JavaScript ES Modules

ES modules separate named and default exports:

```javascript
// Exporting
export function helper() { ... }
export default class App { ... }

// Importing
import App from './app.js'          // default import
import { helper } from './utils.js'  // named import
import * as utils from './utils.js'  // namespace import
```

The default export mechanism is controversial: it makes renaming easy but autocompletion harder.

### The Re-Export Pattern

Most languages support re-exporting: a module imports something and exports it again, creating a facade:
- **Rust:** `pub use sub_module::Widget;` (very common for API design)
- **Python:** Import in `__init__.py` to expose sub-module items at package level
- **TypeScript:** `export { Thing } from './sub';`
- **Go:** Embedding a type re-exports its methods

Re-exports are essential for creating clean public APIs that differ from internal module structure.

## 🔬 Deep Dive

### Trade-offs and Historical Context

#### Explicitness vs Convenience

Languages sit on a spectrum: Rust demands every name be explicitly imported, Python offers a range from explicit to wildcard, and Haskell defaults to importing everything from a module. More explicit imports aid grep-ability and refactoring safety; more implicit imports reduce boilerplate. The industry trend favours explicitness — even Haskell style guides now recommend qualified imports.

#### The Default Export Debate

JavaScript's `export default` was designed around the assumption that most modules export one primary thing. In practice, it creates friction: IDEs cannot auto-import default exports as reliably, and renaming at the import site means the exported name is lost. TypeScript and modern JS style guides increasingly prefer named exports exclusively.

#### Unused Import Policies

Go's compile-error on unused imports is the strictest approach. Most other languages rely on linters (Python's flake8, Rust's warnings, Java's IDE inspections). The Go approach keeps code clean automatically but adds friction during iterative development — addressed by the goimports tool.

## 🏋️ Practice

**Exercise 1 — Import Style Audit:** Take a medium-sized project in your preferred language. Categorise every import as qualified, unqualified, wildcard, or aliased. Count how many names would clash if all imports were converted to wildcard. What does this tell you about the codebase's namespace hygiene?

**Exercise 2 — Re-Export Facade:** In Rust or TypeScript, create a library with three internal modules (`auth`, `db`, `api`). Design a public API surface using re-exports in the crate root (or index.ts) so users never need to import from internal paths. Then refactor the internal module layout without breaking the public API.

**Exercise 3 — Cross-Language Translation:** Take the following Python module structure and translate the import/export relationships into idiomatic Rust and idiomatic Go: a package `shapes` containing `circle.py`, `rectangle.py`, and `__init__.py` that re-exports `Circle` and `Rectangle`. Note which language requires the most boilerplate and which enforces the strictest visibility.

## References

- [[Sources Index]]
