---
tags: [pl, chunk, paradigms, composition]
up: "[[OOP Philosophies]]"
---

# Composition Over Inheritance The Universal Lesson

Every modern language has moved toward composition and away from deep inheritance hierarchies. This is the single most important OOP lesson of the last 30 years.

## The Inheritance Problem

```java
// Classic OOP: deep hierarchy
class Animal { }
class Mammal extends Animal { }
class Dog extends Mammal { }
class GuideDog extends Dog { }
// What if you need a RobotDog? A SwimmingDog? The hierarchy breaks.
```

### The Diamond Problem
Multiple inheritance creates ambiguity:
```
    Animal
   /      \
Flying   Swimming
   \      /
  FlyingFish   // Which Animal.breathe() do I inherit?
```

## How Modern Languages Solve This

### Rust: Traits (No Inheritance)
```rust
trait Swim { fn swim(&self); }
trait Fly { fn fly(&self); }

struct Duck;
impl Swim for Duck { fn swim(&self) { println!("paddle"); } }
impl Fly for Duck { fn fly(&self) { println!("flap"); } }
// Duck composes behaviors without hierarchy
```

### Go: Embedding + Interfaces
```go
type Swimmer interface { Swim() }
type Flyer interface { Fly() }

type Duck struct {
    SwimAbility  // Embedded struct
    FlyAbility   // Embedded struct
}
// Duck gets Swim() and Fly() via embedding, not inheritance
```

### Kotlin: Delegation
```kotlin
interface Swimmer { fun swim() }
class SwimAbility : Swimmer { override fun swim() = println("paddle") }

class Duck(swimmer: Swimmer = SwimAbility()) : Swimmer by swimmer
// Delegation: Duck delegates Swimmer to SwimAbility instance
```

### Swift: Protocol Extensions
```swift
protocol Swimmer { func swim() }
extension Swimmer { func swim() { print("default swim") } }

struct Duck: Swimmer, Flyer { }
// Gets default implementations from protocol extensions
```

## The Evidence

| Year | Language | Composition Feature |
|------|---------|-------------------|
| 1994 | GoF Design Patterns | "Favor composition over inheritance" |
| 2003 | Scala | Traits (mixin composition) |
| 2010 | Rust | Traits (no inheritance at all) |
| 2012 | Go | Embedding + interfaces |
| 2015 | Swift | Protocol-oriented programming |
| 2016 | Kotlin | Interface delegation |
| 2017 | Java 8+ | Default methods in interfaces |

## Key Insight
The trajectory is clear: languages evolved from "everything is a class with inheritance" (Java, C++) to "compose behaviors from small interfaces/traits" (Rust, Go, Swift). Rust took the most radical position by removing inheritance entirely. The result: simpler, more flexible, more testable code.

## References
→ [[Sources Index]]
