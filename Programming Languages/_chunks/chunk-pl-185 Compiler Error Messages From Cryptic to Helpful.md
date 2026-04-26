---
tags: [pl, chunk, compilation, error-messages]
up: "[[Compilation and Runtime Overview]]"
---

# Compiler Error Messages From Cryptic to Helpful

The quality of error messages has become a competitive advantage for programming languages.

## The Error Message Spectrum

### Gold Standard: Rust
\\\
error[E0382]: borrow of moved value: \s\
 --> src/main.rs:5:20

  |
3 |     let s = String::from("hello");

  |         - move occurs because \s\ has type \String\
4 |     let s2 = s;

  |              - value moved here
5 |     println!("{}", s);

  |                    ^ value borrowed here after move
  |
help: consider cloning the value

  |
4 |     let s2 = s.clone();

  |               ++++++++
\\\

Rust errors:
- Point to the exact location
- Explain WHY it's wrong
- Suggest HOW to fix it
- Link to detailed explanations (\
ustc --explain E0382\)

### Good: Elm (Pioneer)
Elm pioneered friendly errors before Rust adopted the approach:
\\\
-- TYPE MISMATCH
The 2nd argument to \dd\ is not what I expect:
6|   add 1 "hello"
             ^^^^^^^
This argument is a String, but \dd\ needs its 2nd argument to be a number.
Hint: Try using String.toInt to convert it.
\\\

### Terrible: C++ Templates
\\\
/usr/include/c++/v1/algorithm:642:23: error: invalid operands to binary expression
  ('const Foo' and 'const Foo')
  ... (followed by 200 lines of template instantiation backtrace)
\\\

C++20 Concepts improved this significantly but legacy template errors remain painful.

### Improving: Haskell
GHC has invested heavily in error quality:
\\\
error:
    * Couldn't match type 'Int' with '[Char]'
      Expected: String
        Actual: Int
    * In the expression: 42
      In an equation for 'name': name = 42
\\\

## What Makes Great Error Messages

| Quality | Example | Languages |
|---------|---------|-----------|
| Location | Underline the exact problem | Rust, Elm, Go |
| Explanation | Why it's wrong | Rust, Elm |
| Suggestion | How to fix it | Rust (help:), Elm (Hint:) |
| Context | Show surrounding code | Rust, most modern |
| Links | To documentation | Rust (--explain) |
| Colors | Highlight important parts | Rust, cargo, clang |

## Key Insight
Elm proved and Rust popularized the idea that error messages are a user interface. Investing in error quality dramatically reduces learning curve and debugging time. Languages that treat errors as documentation (Rust, Elm) have measurably better developer satisfaction than those that treat them as implementation details (C++, older GHC).

## References
→ [[Sources Index]]
