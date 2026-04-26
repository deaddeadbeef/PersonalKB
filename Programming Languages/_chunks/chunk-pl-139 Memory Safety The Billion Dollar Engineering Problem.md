---
tags: [pl, chunk, security, memory-safety]
up: "[[Memory Management Overview]]"
---

# Memory Safety The Billion Dollar Engineering Problem

Memory safety bugs (buffer overflows, use-after-free, double-free) account for approximately 70% of security vulnerabilities in systems software.

## The Evidence

| Source | Finding |
|--------|---------|
| Microsoft (2019) | 70% of CVEs in Microsoft products are memory safety bugs |
| Google Chrome (2020) | 70% of high-severity security bugs are memory safety |
| Android (2022) | Memory safety bugs declined as Rust adoption increased |
| US White House (2024) | Recommended memory-safe languages for critical infrastructure |

## The Language Safety Spectrum

Unsafe --------- Safe-ish ----------- Safe-by-default ------- Fully safe
C         C++ (smart pointers)         Rust                  Haskell
           Zig (safety checks)         Swift (ARC)           Erlang
                                       Go (GC)               Python
                                       Java (GC)

## Rust's Breakthrough

Before Rust, the conventional wisdom was:
- **Safe = slow** (garbage collector overhead)
- **Fast = unsafe** (manual memory management)

Rust proved this was a false dichotomy:
- Ownership + borrowing = memory safety without GC
- Zero-cost abstractions = safe code that's as fast as C
- unsafe blocks = explicit opt-out when needed (and reviewable)

## The Cost of Unsafety

Real-world exploits from memory bugs:
- **Heartbleed (2014):** Buffer over-read in OpenSSL — leaked server private keys
- **WannaCry (2017):** Buffer overflow in SMBv1 — ransomware affecting 200K+ computers
- **Sudo heap overflow (2021):** 10-year-old bug in privileged C code
- **xz backdoor (2024):** Exploited C memory management complexity

## Key Insight
The industry is converging on a clear answer: new systems software should be written in memory-safe languages (Rust preferred for performance-critical, Go/Java/C# for everything else). The remaining question is how to handle the billions of lines of existing C/C++ code.

## References
→ [[Sources Index]]
