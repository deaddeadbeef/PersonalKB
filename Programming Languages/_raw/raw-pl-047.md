---
tags: [pl, raw, serialization, data-formats]
up: "[[Sources Index]]"
---

# Raw Note 047 – Serialization and Data Formats

## Language Integration with Serialization

### First-Class Serialization Support
- **Go:** encoding/json with struct tags – json:"name,omitempty"
- **Rust:** serde framework – derive macros for any format
- **Python:** pickle (native), json module, dataclasses + pydantic
- **Kotlin:** kotlinx.serialization – compiler plugin, multi-format
- **C#:** System.Text.Json + source generators for AOT

### Serde (Rust) – The Gold Standard
- Zero-copy deserialization possible
- Compile-time generated, no reflection
- 60+ format implementations

### Schema-First vs Code-First

**Schema-first** (define schema, generate code):
- Protocol Buffers (Google): .proto files → generated code in any language
- FlatBuffers (Google): Zero-copy serialization
- Cap'n Proto: "infinitely faster than protobuf"
- Apache Avro: Schema evolution, Hadoop ecosystem
- JSON Schema: Validation for JSON documents

**Code-first** (define types, derive serialization):
- Rust serde: derive macros from structs
- Go encoding/json: struct tags
- Python pydantic: type annotations + validation
- Kotlin kotlinx.serialization: annotation processing

## Format Comparison

| Format | Human Readable | Schema | Speed | Size |
|--------|---------------|--------|-------|------|
| JSON | Yes | Optional | Moderate | Large |
| TOML | Yes | No | Moderate | Medium |
| YAML | Yes | No | Slow | Medium |
| Protocol Buffers | No | Required | Fast | Small |
| MessagePack | No | Optional | Fast | Small |
| FlatBuffers | No | Required | Fastest | Small |
| CBOR | No | Optional | Fast | Small |

## Key Insight
Rust's serde is the most principled serialization system: compile-time generated, format-agnostic, zero-cost. It demonstrates how derive macros can replace runtime reflection for serialization. The industry is moving from code-first (JSON with runtime reflection) to schema-first (protobuf) for API boundaries.

## References
→ [[Sources Index]]
