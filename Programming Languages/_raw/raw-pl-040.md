---
tags: [pl, raw, security, safety]
up: "[[Sources Index]]"
---

# Raw Note 040 — Language Security Models

## Memory Safety

The #1 source of security vulnerabilities in systems software is memory unsafety:

### Unsafe Languages
- **C:** Buffer overflows, use-after-free, double-free — ~70% of CVEs in C projects
- **C++:** Same issues plus object lifetime complexity

### Memory-Safe Languages
- **Rust:** Compile-time ownership prevents memory bugs without GC overhead
- **Go, Java, C#, Python:** GC prevents most memory issues
- **Swift:** ARC prevents most issues; unsafe features exist
- **Zig:** Runtime safety checks (bounds checking) with manual memory

### The White House Report (2024)
The US government recommended memory-safe languages for critical infrastructure, specifically citing Rust, Go, Java, C#, and Swift. This shifted the conversation from academic to policy.

## Type Safety and Security

| Feature | Security Benefit | Languages |
|---------|-----------------|-----------|
| Null safety | Prevents null pointer bugs | Kotlin, Rust, Swift, TypeScript (strict) |
| Bounds checking | Prevents buffer overflows | Rust, Go, Java, Python |
| Immutability defaults | Prevents accidental mutation | Rust (immutable by default), Haskell |
| Sealed types | Prevents unauthorized subclassing | Kotlin sealed, Java sealed (17+) |
| Capability-based | Limits what code can do | Wasm, Deno permissions |

## Sandboxing and Capabilities

### WebAssembly
WASM provides a sandboxed execution environment:
- No access to host filesystem, network, or memory by default
- Capabilities must be explicitly granted
- Linear memory model prevents out-of-bounds access

### Deno
Deno's permission system is capability-based:

`ash
deno run --allow-net --allow-read=./data app.ts
`

- No permissions by default — must opt in
- Contrasts with Node.js's full access model

### Java Security Manager (deprecated)
- Attempted fine-grained security policies
- Too complex and slow — deprecated in Java 17
- Replaced by module system access controls

## Supply Chain Security

| Threat | Mitigation | Example |
|--------|------------|---------|
| Typosquatting | Registry policies, lockfiles | npm, PyPI registries |
| Dependency confusion | Namespace scoping | npm scopes, Go module paths |
| Malicious updates | Lockfiles, auditing | cargo audit, npm audit |
| Compromised maintainers | 2FA, provenance | npm provenance, Sigstore |

## Unsafe Escape Hatches

Most safe languages provide escape hatches for when safety rules are too restrictive:

| Language | Escape Hatch | Use Case |
|----------|-------------|----------|
| Rust | `unsafe {}` blocks | FFI, raw pointers, inline assembly |
| C# | `unsafe {}` blocks | Pointer arithmetic, interop |
| Go | `unsafe` package | Type punning, reflect internals |
| Haskell | `unsafePerformIO` | Breaking purity (use sparingly) |
| Kotlin | `@Suppress("UNCHECKED_CAST")` | Type system escape |

## Key Insight
Language-level safety is the most effective security measure. Rust has demonstrated that memory safety without GC is practical. The industry is shifting from "write C carefully" to "use a safe language by default, unsafe only when proven necessary."

## References
→ [[Sources Index]]
