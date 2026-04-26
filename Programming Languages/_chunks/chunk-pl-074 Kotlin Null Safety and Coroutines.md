---
tags: [chunk, programming-languages, kotlin-features]
source: "[[raw-pl-023]]"
---

# chunk-pl-074 Kotlin Null Safety and Coroutines

**Null safety:** Kotlin's most impactful feature. String (never null) vs String? (nullable). Compiler enforces null checks.
- Smart casts: if (x != null) makes x non-null in the branch
- Safe call: x?.method() — returns null if x is null
- Elvis operator: x ?: default — use default if x is null
- Not-null assertion: x!! — throws if null (escape hatch, discouraged)

Result: NullPointerException essentially eliminated from Kotlin code.

**Coroutines:** Structured concurrency — async code in sequential style.
- suspend fun fetchData(): Data — suspending function
- coroutineScope { } — structured scope (children tied to parent)
- launch { } — fire-and-forget coroutine
- sync { } / await() — coroutine returning a value
- Cancellation propagates through scope hierarchy

**Data classes:** data class Point(val x: Int, val y: Int) auto-generates: equals, hashCode, toString, copy, componentN functions. One line replaces hundreds of Java boilerplate.

**Extension functions:** un String.isPalindrome() = this == this.reversed(). Add methods to existing types without inheritance.
