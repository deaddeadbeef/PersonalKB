---
tags: [chunk, programming-languages, kotlin-multiplatform]
source: "[[raw-pl-023]]"
---

# chunk-pl-084 Kotlin Multiplatform and Extension Functions

**Kotlin Multiplatform (KMP):** Share business logic across platforms:
- **Common code:** Data models, business logic, networking, serialization
- **Platform-specific:** UI, platform APIs, native integrations
- **Targets:** JVM (Android, server), JS (browser, Node), Native (iOS via Kotlin/Native, desktop, embedded)

**expect/actual:** Declare expected API in common code; provide actual implementation per platform. xpect fun platformName(): String in common; ctual fun platformName() = "Android" on JVM.

**Extension functions:** Add methods to existing types without inheritance:
```kotlin
fun String.isPalindrome() = this == this.reversed()
fun List<Int>.median() = sorted().let { it[it.size / 2] }
```
Enables fluent APIs. Eliminates Java's StringUtils.doThing(str) pattern. Extensions are resolved statically (no runtime overhead).

**Scope functions:** let, un, with, pply, lso — concise object configuration and transformation. Kotlin-specific idiom for expressive code.

**Comparison with Swift:** Both are "better predecessor" languages. Kotlin: better Java, JVM ecosystem. Swift: better Objective-C, Apple ecosystem. Both converging on similar features (null safety, protocols/interfaces, async).
