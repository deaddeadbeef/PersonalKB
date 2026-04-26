---
tags: [pl, raw, pattern-matching, adt]
up: "[[Sources Index]]"
---

# Raw Note 042 — Pattern Matching Evolution

## Pattern Matching History

Pattern matching originated in ML (1973) and has spread to nearly every modern language.

### ML Family (Origin)
\\\ocaml
(* OCaml - exhaustive, with warnings for missing cases *)
match shape with

| Circle r -> pi *. r *. r
| Rectangle (w, h) -> w *. h
| Triangle (b, h) -> 0.5 *. b *. h
\\\

### Haskell
\\\haskell
-- Guards + patterns
area (Circle r)        = pi * r * r
area (Rectangle w h)   = w * h
area (Triangle b h)    = 0.5 * b * h
\\\

### Rust (ML-inspired, with ownership)
\\\
ust
match msg {
    Message::Quit => println!("quit"),
    Message::Move { x, y } => move_to(x, y),
    Message::Write(text) => println!("{text}"),
    Message::Color(r, g, b) => set_color(r, g, b),
}
// Exhaustive - compiler error if cases missing
\\\

### Scala (JVM pioneer)
\\\scala
expr match {
  case Num(n) => n
  case Add(l, r) => eval(l) + eval(r)
  case Mul(l, r) => eval(l) * eval(r)
}
\\\

### Swift
\\\swift
switch value {
case .success(let data) where data.count > 0:
    process(data)
case .failure(let error):
    handle(error)
default:
    break
}
\\\

### Kotlin (when expression)
\\\kotlin
when (shape) {
    is Circle -> PI * shape.radius.pow(2)
    is Rectangle -> shape.width * shape.height
    else -> 0.0
}
\\\

### Python (3.10+ structural pattern matching)
\\\python
match command:
    case ["go", direction]:
        move(direction)
    case ["take", item]:
        pick_up(item)
    case _:
        print("Unknown command")
\\\

### Java (21+ pattern matching, preview features)
\\\java
switch (shape) {
    case Circle c -> Math.PI * c.radius() * c.radius();
    case Rectangle r -> r.width() * r.height();
    // Exhaustive with sealed types
}
\\\

### C# (progressive enhancement C# 7-12)
\\\csharp
var result = shape switch
{
    Circle { Radius: var r } => Math.PI * r * r,
    Rectangle { Width: var w, Height: var h } => w * h,
    _ => 0
};
\\\

## Evolution Timeline

| Year | Language | Feature |
|------|---------|---------|
| 1973 | ML | Original pattern matching |
| 1990 | Haskell | Guards, where clauses |
| 2004 | Scala | Case classes + match |
| 2010 | Rust | Exhaustive match + ownership |
| 2014 | Swift | Powerful switch with value binding |
| 2016 | Kotlin | when expression |
| 2017 | C# 7 | Type patterns, var patterns |
| 2021 | Python 3.10 | Structural pattern matching |
| 2023 | Java 21 | Record patterns, exhaustive switches |
| 2024 | C# 12 | List patterns, property patterns |

## Exhaustiveness Checking

The killer feature of pattern matching: the compiler warns about missing cases.

| Language | Exhaustive? | How |
|----------|-------------|-----|
| OCaml | Yes | ADTs must cover all variants |
| Haskell | Yes (with warnings) | GHC warns about incomplete patterns |
| Rust | Yes (enforced) | Compile error on non-exhaustive match |
| Scala 3 | Yes (sealed) | Sealed traits enable exhaustive checks |
| Kotlin | Yes (sealed) | Sealed classes/interfaces |
| Swift | Yes | Enum exhaustiveness required |
| Java 21 | Yes (sealed) | Sealed classes enable it |
| C# | Partial | Warnings but not enforced |
| Python | No | Structural, no compile-time check |

## Key Insight
Pattern matching is converging across languages, but quality varies. ML-family languages have decades of experience and deep integration with algebraic data types. Newer adopters (Python, Java) bolt it on, losing exhaustiveness guarantees or requiring verbose syntax.

## References
→ [[Sources Index]]
