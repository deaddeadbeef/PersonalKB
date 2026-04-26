---
tags: [pl, chunk, java, renaissance]
up: "[[Java – Language Profile]]"
---

# Java Modern Renaissance Records Loom and Beyond

Java has undergone a dramatic modernization since Java 9 (2017), shedding its reputation as a verbose legacy language.

## The Six-Month Release Train

After Java 8's 3-year gap, Java switched to 6-month releases:
```
Java 9 (2017): Modules
Java 10 (2018): var keyword
Java 11 (2018 LTS): HTTP client
Java 14 (2020): Records (preview)
Java 15 (2020): Sealed classes (preview)
Java 16 (2021): Records (final)
Java 17 (2021 LTS): Sealed classes (final), pattern matching preview
Java 21 (2023 LTS): Virtual threads, pattern matching, sequenced collections
Java 22 (2024): Unnamed variables, string templates (preview)
Java 23 (2024): Primitive types in patterns
```

## Key Modern Features

### Records (Java 16)
```java
// Before: 50+ lines for a simple data class
// After: one line
record Point(double x, double y) {}
// Automatically generates: constructor, getters, equals, hashCode, toString
```

### Sealed Classes (Java 17)
```java
sealed interface Shape permits Circle, Rectangle, Triangle {}
record Circle(double radius) implements Shape {}
record Rectangle(double w, double h) implements Shape {}
record Triangle(double b, double h) implements Shape {}
```

### Pattern Matching (Java 21)
```java
double area = switch (shape) {
    case Circle c -> Math.PI * c.radius() * c.radius();
    case Rectangle r -> r.w() * r.h();
    case Triangle t -> 0.5 * t.b() * t.h();
};
// Exhaustive! Compiler error if a shape is missing.
```

### Virtual Threads (Java 21 / Project Loom)
```java
// Create 1 million concurrent tasks
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    IntStream.range(0, 1_000_000).forEach(i ->
        executor.submit(() -> {
            Thread.sleep(Duration.ofSeconds(1));
            return i;
        })
    );
}
// Each task runs on a virtual thread (~few KB, not ~1MB)
```

## Java vs Kotlin in 2025

| Feature | Java 21+ | Kotlin |
|---------|----------|--------|
| Null safety | Limited (annotations) | Built-in (`?` types) |
| Data classes | Records | data class |
| Pattern matching | switch with patterns | when (more flexible) |
| Coroutines | Virtual threads | Coroutines (more structured) |
| Extension functions | No | Yes |
| String templates | Preview | Standard (templates) |

Java is closing the gap, but Kotlin still has advantages in null safety and coroutine ergonomics.

## Key Insight
Java's renaissance proves that a 30-year-old language can reinvent itself while maintaining backward compatibility. The combination of records, sealed classes, pattern matching, and virtual threads makes Java 21+ a genuinely modern language. The 6-month release cadence ensures continuous improvement.

## References
→ [[Sources Index]]
