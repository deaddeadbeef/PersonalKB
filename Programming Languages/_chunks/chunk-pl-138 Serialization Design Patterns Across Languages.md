---
tags: [pl, chunk, serialization, serde]
up: "[[Module Systems Overview]]"
---

# Serialization Design Patterns Across Languages

How languages handle serialization reveals their approach to metaprogramming, type systems, and runtime vs compile-time design.

## The Three Approaches

### 1. Runtime Reflection (Java, Go, Python)
Java - Jackson uses runtime reflection:
ObjectMapper mapper = new ObjectMapper();
String json = mapper.writeValueAsString(user);

- Pro: Works on any type without modification
- Con: Slow (reflection overhead), fragile (field renaming breaks silently)

### 2. Compile-Time Code Generation (Rust, Kotlin)
Rust serde - derive macro generates code at compile time:
- #[derive(Serialize, Deserialize)]
- struct User { name: String, email: String }

- Pro: Zero runtime overhead, compile-time type safety
- Con: Compile time cost, generated code can be opaque

### 3. Schema-First Code Generation (Protobuf, FlatBuffers)
Define schema, generate code for any language:
- message User { string name = 1; string email = 2; }

- Pro: Cross-language, versioned, compact
- Con: Extra tooling step, less ergonomic

## Language Comparison

| Language | Primary Tool | Approach | Speed |
|----------|-------------|----------|-------|
| Rust | serde | Derive macros | Fastest |
| Go | encoding/json | Struct tags + reflection | Fast |
| Kotlin | kotlinx.serialization | Compiler plugin | Fast |
| C# | System.Text.Json | Source generators (new) / reflection (old) | Fast (source gen) |
| Java | Jackson/Gson | Reflection | Moderate |
| Python | pydantic | Runtime validation | Slow |
| TypeScript | zod / class-transformer | Runtime validation | Slow |

## Serde's Design Genius
Serde separates the data model from the format:
- **Serialize/Deserialize traits:** Define how types map to an abstract data model
- **Serializer/Deserializer traits:** Define how the data model maps to a format
- Result: N types × M formats with only N + M implementations (not N × M)

This is the Visitor pattern elevated to a compile-time-generated, zero-cost abstraction.

## Key Insight
Serialization is a litmus test for a language's metaprogramming quality. Rust's derive macros, Kotlin's compiler plugin, and C#'s source generators all solve it at compile time. Java and Python's reflection-based approach works but sacrifices performance and type safety.

## References
→ [[Sources Index]]
