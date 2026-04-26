---
tags: [chunk, programming-languages, imports]
source: "[[raw-pl-008]]"
---

# chunk-pl-051 Import and Export Mechanisms Compared

**Python:** `import os`, `from os.path import join`, `import numpy as np`. Multiple styles. Star imports discouraged.

**Rust:** `use std::collections::HashMap;` Explicit paths. Grouped imports `{self, Read, Write}`. Items not `use`d must be fully qualified. Maximally traceable.

**Go:** `import "fmt"` automatic namespace. All imports must be used (compiler error). goimports auto-manages.

**Java:** `import java.util.List;` Name shortening only. Wildcard `.*` available.

**JavaScript ES Modules:** `import App from './app'` (default), `import { helper } from './utils'` (named), `import * as utils` (namespace). Default export controversial.

**Haskell:** `import qualified Data.Map as Map` (recommended). Qualified imports avoid name clashes.

**OCaml:** `open List` brings names into scope. Local opens (`let open List in ...`). Qualified names (`List.map`) preferred.

**Re-exports:** Rust `pub use`, Python `__init__.py`, TypeScript `export { } from`. Essential for creating clean public APIs.
