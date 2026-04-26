---
tags: [pl, chunk, concurrency, async-coloring]
up: "[[Async-Await Patterns]]"
---

# The Function Coloring Problem Async vs Sync

Bob Nystrom's "What Color is Your Function?" essay identified a fundamental problem with async/await: it splits the language into two incompatible worlds.

## The Problem

In languages with async/await, functions have a "color":
- **Red functions** (async): can call other red or blue functions
- **Blue functions** (sync): can ONLY call blue functions

`python
# Python: two incompatible worlds
def sync_fetch():          # Blue function
    return requests.get(url)

async def async_fetch():   # Red function
    return await aiohttp.get(url)

# Can't call async_fetch from sync_fetch without runtime tricks!
`

This means:
- Libraries must provide both sync and async versions
- Code is duplicated for each "color"
- Choosing wrong at the start requires rewriting

## Language Approaches

### Colored (The Problem Exists)
- **JavaScript:** async function vs function
- **Python:** async def vs def
- **Rust:** async fn vs fn
- **C#:** async Task<T> vs T

### Uncolored (Problem Solved)
- **Go:** Goroutines are transparent — all functions work the same way
- **Java 21:** Virtual threads make blocking calls cheap — no async needed
- **Erlang:** All processes are concurrent — no sync/async distinction
- **Zig:** Async is transparent (compiler chooses)

### Partially Solved
- **OCaml 5:** Algebraic effects make concurrency transparent (no coloring)
- **Kotlin:** Coroutines use suspend keyword (colored, but structured concurrency mitigates)

## The Go/Loom Solution

`go
// Go: just write normal code, goroutines handle concurrency
func fetch(url string) string {
    resp, _ := http.Get(url)  // "Blocks" but goroutine yields
    body, _ := io.ReadAll(resp.Body)
    return string(body)
}
// No async/await needed - goroutines make blocking calls cheap
`

`java
// Java 21: same idea with virtual threads
String fetch(String url) {
    return HttpClient.newHttpClient()
        .send(request, HttpResponse.BodyHandlers.ofString())
        .body();
    // Runs on virtual thread - blocking is cheap
}
`

## Why Rust Accepted Coloring

Rust chose colored async because:
1. Zero-cost: no runtime overhead for non-async code
2. Explicit: you know exactly where yields happen
3. No runtime: no green thread scheduler required
4. Trade-off: complexity for performance

## Key Insight
The function coloring problem is real and impacts developer experience significantly. Go and Java Loom solved it elegantly with cheap blocking (green threads). Rust accepted it for zero-cost abstractions. OCaml 5 may have found the best solution with algebraic effects. The ideal future: async is an implementation detail, not a function signature.

## References
→ [[Sources Index]]
