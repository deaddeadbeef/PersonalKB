---
tags: [pl, chunk, zig, comptime]
up: "[[Zig – Language Profile]]"
---

# Zig Comptime The Generics Alternative

Zig doesn't have generics in the traditional sense. Instead, it has comptime – the ability to run any Zig code at compile time. This single feature replaces generics, macros, and metaprogramming.

## How Comptime Works

```zig
// "Generic" function - type is a comptime parameter
fn max(comptime T: type, a: T, b: T) T {
    return if (a > b) a else b;
}

// Usage:
const result = max(i32, 10, 20);    // Compiled as i32 max
const fresult = max(f64, 1.5, 2.5); // Compiled as f64 max
```

The compiler literally runs `max` at compile time to determine the output type, then generates specialized code.

## Comptime vs Traditional Generics

| Property | Zig comptime | Rust generics | C++ templates |
|----------|-------------|---------------|---------------|
| Mechanism | Interpreter at compile time | Monomorphization | Instantiation |
| Error messages | Clear (it's just Zig) | Good (trait bounds) | Terrible (historically) |
| Turing complete | Yes | Limited | Yes (but arcane) |
| Debugging | step-through comptime | N/A | N/A |
| Syntax | Same as runtime Zig | Different (<T>, where) | Different (<T>, requires) |

## Comptime Power Examples

### Type-Level Computation
```zig
fn Matrix(comptime rows: usize, comptime cols: usize) type {
    return struct {
        data: [rows][cols]f64,

        fn multiply(self: @This(), other: Matrix(cols, rows)) Matrix(rows, rows) {
            // Dimension checking happens at compile time
            // Wrong dimensions = compile error
        }
    };
}
```

### Compile-Time String Processing
```zig
// Parse a format string at compile time
fn print(comptime fmt: []const u8, args: anytype) void {
    // fmt is analyzed at compile time
    // Type mismatches between format string and args = compile error
}
```

### Compile-Time Reflection
```zig
fn dumpFields(comptime T: type) void {
    const info = @typeInfo(T);
    inline for (info.Struct.fields) |field| {
        @compileLog(field.name, field.type);
    }
}
```

## No Hidden Behavior

Zig's comptime aligns with its core philosophy of "no hidden control flow":
- No implicit allocations
- No implicit type conversions
- No operator overloading
- What you see in the source code is what executes

## Key Insight
Zig's comptime is arguably the most elegant solution to the generics/metaprogramming problem. By making the compile-time language identical to the runtime language, it eliminates the need for a separate template/macro sublanguage. The trade-off: Zig's compiler must include an interpreter, and compile times can increase for heavy comptime usage.

## References
→ [[Sources Index]]
