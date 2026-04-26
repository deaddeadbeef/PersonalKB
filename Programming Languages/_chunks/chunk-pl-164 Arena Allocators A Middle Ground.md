---
tags: [pl, chunk, memory, arena-allocators]
up: "[[Manual Memory Management]]"
---

# Arena Allocators A Middle Ground in Memory Management

Arena allocators offer a middle ground between manual malloc/free and garbage collection: allocate many objects in a region, then free them all at once.

## How Arenas Work

```
Traditional:  alloc A, alloc B, alloc C, free B, alloc D, free A, free C, free D
Arena:        alloc A, alloc B, alloc C, alloc D... FREE EVERYTHING AT ONCE
```

An arena is a contiguous block of memory. Allocation is a simple pointer bump (extremely fast). Deallocation frees the entire arena.

## Language Support

### Zig (First-Class Allocator Support)
```zig
var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
defer arena.deinit(); // Free everything when scope ends

const allocator = arena.allocator();
const list = try std.ArrayList(u8).init(allocator);
// All allocations in this arena are freed together
```

Zig's allocator parameter pattern means every allocation is explicit.

### Rust (via crates)
```rust
use bumpalo::Bump;
let arena = Bump::new();
let x = arena.alloc(42);
let s = arena.alloc_str("hello");
// All freed when arena is dropped
```

### C (manual implementation)
```c
typedef struct { char *buf; size_t used; size_t cap; } Arena;
void *arena_alloc(Arena *a, size_t size) {
    void *ptr = a->buf + a->used;
    a->used += size;
    return ptr;
}
// Just reset used=0 to "free" everything
```

### Go (arena package, experimental)
Go 1.20 introduced `arena` package (experimental) for performance-critical allocation.

## Use Cases

| Use Case | Why Arena Fits |
|----------|---------------|
| Game frame data | Allocate per-frame, free all at frame end |
| Request handling | Allocate per-request, free at response |
| Compilers | AST nodes live for one compilation phase |
| Parsers | Parse tree allocated together, freed together |
| Embedded systems | Predictable memory usage, no fragmentation |

## Arena vs GC vs Ownership

| Property | Arena | GC | Ownership (Rust) |
|----------|-------|----|--------------------|
| Allocation speed | Fastest (pointer bump) | Fast | Fast (stack or alloc) |
| Deallocation | All at once | Incremental | Deterministic (drop) |
| Fragmentation | None within arena | Possible | None |
| Safety | Manual (can outlive arena) | Safe | Compile-time checked |
| Overhead | Near zero | GC runtime | Zero |

## Key Insight
Arenas are increasingly popular because they sidestep the malloc/free complexity without requiring a garbage collector. Zig's allocator-parameter design makes arenas first-class citizens.

## References
→ [[Sources Index]]
