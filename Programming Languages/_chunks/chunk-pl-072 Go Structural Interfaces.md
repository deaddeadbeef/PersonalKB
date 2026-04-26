---
tags: [chunk, programming-languages, go-interfaces]
source: "[[raw-pl-022]]"
---

# chunk-pl-072 Go Structural Interfaces

Go interfaces are satisfied implicitly. Any type with the right methods satisfies an interface — no implements keyword needed.

**Small interfaces:** Go encourages single-method interfaces:
- io.Reader: Read(p []byte) (n int, err error)
- io.Writer: Write(p []byte) (n int, err error)
- mt.Stringer: String() string
- rror: Error() string

**Consumer-defined:** The caller defines what it needs, not the provider. You can define an interface in your package that types from other packages satisfy without modification.

**Retroactive satisfaction:** Existing types satisfy new interfaces. Write a new interface today; types written years ago might already satisfy it.

**The empty interface:** interface{} (now ny) holds any value — Go's escape hatch for dynamic typing. Generics (Go 1.18) reduce the need for ny.

**Comparison with Rust traits:** Go interfaces are purely structural (shape-based). Rust traits are nominal (explicitly implemented). Go: more flexible, less type-safe. Rust: more controlled, no accidental satisfaction.
