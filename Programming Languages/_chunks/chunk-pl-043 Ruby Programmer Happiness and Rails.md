---
tags: [chunk, programming-languages, ruby]
source: "[[raw-pl-011]]"
---

# chunk-pl-043 Ruby Programmer Happiness and Rails

Ruby (1995, Matz): **optimize for programmer happiness.** "Ruby is designed to make programmers happy." Principle of least surprise.

**Everything is an object:** Integers, nil, true, false — all objects with methods. 5.times { puts "hello" } is idiomatic. Classes are objects. Methods are objects (via method(:name)).

**Open classes + metaprogramming:** Reopen any class at runtime. Add/modify methods. method_missing intercepts calls to undefined methods. ActiveSupport: 3.days.ago added to Integer.

**Blocks, Procs, Lambdas:** Block syntax enables elegant iteration and resource management. The primary functional programming mechanism.

**The Rails effect:** Ruby on Rails (2004) made Ruby famous. Convention over configuration. "15-minute blog" demo. Influenced Django, Laravel, Spring Boot. Changed web development for startups.

**Trade-offs:** Slow execution (improving with YJIT), "magic" from metaprogramming obscures behavior, runtime type errors. Ruby excels for small-to-medium web teams prioritizing developer productivity.
