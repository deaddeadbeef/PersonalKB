---
tags: [pl, chunk, modules, visibility]
up: "[[Visibility and Access Control]]"
---

# Module System Philosophy Privacy and Encapsulation

How languages handle visibility reveals their trust model: do they trust developers to respect boundaries, or enforce them?

## Visibility Spectrum

```
Everything public          Enforced boundaries         Everything private
   (C, Python)             (Rust, Java, C#)           (default in Rust)
```

## Language Approaches

### Rust (Crate-Level Privacy)
```rust
pub struct User {
    pub name: String,      // Public
    email: String,         // Private to module (default)
    pub(crate) id: u64,   // Public within crate
    pub(super) age: u8,    // Public to parent module
}
```
Rust's default is private. You must explicitly opt into visibility.

### Java/C# (Class-Level Access)
```java
public class User {
    public String name;      // Accessible everywhere
    protected int age;       // Subclasses + same package
    String email;            // Package-private (default in Java)
    private long id;         // This class only
}
```

### Go (Capitalization Convention)
```go
type User struct {
    Name  string  // Exported (uppercase = public)
    email string  // Unexported (lowercase = package-private)
}
```
Brilliantly simple: visibility is encoded in the name itself.

### Python (Convention Only)
```python
class User:
    def __init__(self):
        self.name = "public"      # Public (convention)
        self._email = "private"   # "Private" (convention, not enforced)
        self.__id = 42            # Name-mangled (harder to access, still possible)
```
Python trusts developers: "We're all consenting adults here."

### Haskell (Module-Level Exports)
```haskell
module User (User(..), createUser) where  -- Only export what's listed
-- Internal functions are invisible outside this module
```

## Design Trade-offs

| Approach | Enforcement | Refactoring Safety | Developer Trust |
|----------|------------|-------------------|-----------------|
| Rust | Compiler-enforced | Excellent | Low trust (prove it) |
| Java/C# | Compiler-enforced | Good | Moderate trust |
| Go | Compiler-enforced (naming) | Good | Moderate trust |
| TypeScript | Compiler-enforced | Good | Moderate trust |
| Python | Convention only | Risky | High trust |
| Ruby | Convention + access modifiers | Moderate | High trust |

## Key Insight
The trend is toward compiler-enforced privacy (Rust, Go, TypeScript). Python's convention-based approach works for small teams but breaks down at scale. Go's capitalization convention is elegant — visibility is immediately visible without reading declarations.

## References
→ [[Sources Index]]
