---
tags: [pl, chunk, kotlin, multiplatform]
up: "[[Kotlin – Language Profile]]"
---

# Kotlin The Pragmatic Modernizer

Kotlin succeeded by being the "better Java" with full interop – the perfect second-system strategy.

## What Kotlin Fixed About Java

| Java Pain Point | Kotlin Solution |
|----------------|-----------------|
| NullPointerException | Nullable types `String?` with flow-sensitive checking |
| Verbose getters/setters | Data classes: `data class User(val name: String)` |
| No type inference | `val` and `var` with full inference |
| Checked exceptions | No checked exceptions |
| No pattern matching | `when` expression (exhaustive with sealed) |
| Verbose lambdas | Trailing lambda syntax, `it` keyword |
| No coroutines | First-class coroutines with structured concurrency |
| No extension functions | `fun String.isPalindrome(): Boolean` |
| No null-safe calls | `user?.address?.city` |
| No string templates | `"Hello, $name!"` |

## Kotlin Multiplatform (KMP)

Kotlin compiles to multiple targets:
```
Kotlin Source Code

    |
    +-- JVM bytecode (Android, server)
    +-- JavaScript (web frontend)
    +-- Native (iOS via LLVM, desktop, embedded)
    +-- WASM (browser, edge)
```

### Shared Code Architecture
```kotlin
// commonMain - shared business logic
expect class Platform() {
    fun name(): String
}

// androidMain
actual class Platform actual constructor() {
    actual fun name(): String = "Android ${android.os.Build.VERSION.SDK_INT}"
}

// iosMain
actual class Platform actual constructor() {
    actual fun name(): String = UIDevice.currentDevice.systemName()
}
```

## Kotlin Coroutines

Kotlin's structured concurrency is the most mature mainstream implementation:
```kotlin
coroutineScope {
    val user = async { fetchUser(id) }
    val orders = async { fetchOrders(id) }
    Response(user.await(), orders.await())
}
// Both tasks scoped to this block
// Cancellation propagates automatically
// Exceptions propagate to parent
```

## Adoption Trajectory

- **2011:** Created at JetBrains
- **2016:** Version 1.0 released
- **2017:** Google announces first-class Android support
- **2019:** Google announces Kotlin-first for Android
- **2023:** Kotlin Multiplatform stable
- **2025:** 95%+ of new Android projects use Kotlin

## Key Insight
Kotlin's success formula: fix the biggest pain points of the dominant language (Java), maintain 100% interop (call Java from Kotlin and vice versa), and get platform endorsement (Google for Android). This is the "better X" playbook executed perfectly.

## References
→ [[Sources Index]]
