---
tags: [pl, chunk, python, ecosystem]
up: "[[Python – Language Profile]]"
---

# Python The Glue Language That Ate Machine Learning

Python's dominance in ML/AI is the defining language-ecosystem success story of the 2020s.

## How Python Won ML

### The NumPy Foundation
Python's ML dominance traces back to NumPy (2006):
```python
import numpy as np
# This runs at C speed, not Python speed
result = np.dot(matrix_a, matrix_b)  # BLAS-optimized matrix multiply
```

NumPy proved Python could be fast enough – not by making Python fast, but by making C callable from Python elegantly.

### The Stack
```
User code (Python - slow but readable)

    |
Framework (PyTorch/TensorFlow - Python API, C++ implementation)

    |
NumPy/SciPy (Python API, C/Fortran implementation)

    |
CUDA/cuDNN (NVIDIA GPU acceleration)
```

Python is the **orchestration layer** – it doesn't do the math, it tells C/CUDA to do the math.

### The Ecosystem Flywheel
1. Researchers publish papers with Python code
2. Practitioners adopt the same tools
3. Libraries optimize for Python users
4. More researchers choose Python
5. Repeat → self-reinforcing dominance

## Python's Typing Evolution

Python is gradually adding types without breaking existing code:
```python
# Python 3.0: no types
def greet(name):
    return f"Hello, {name}"

# Python 3.5+: type hints (PEP 484)
def greet(name: str) -> str:
    return f"Hello, {name}"

# Python 3.10+: modern syntax
def process(data: list[int] | None) -> dict[str, int]:
    ...

# Python 3.12+: type parameter syntax (PEP 695)
type Point[T] = tuple[T, T]
```

Type checkers (mypy, pyright, pytype) catch errors without running code. This is gradual typing in action.

## The Performance Problem and Solutions

| Solution | Speed | Approach |
|----------|-------|----------|
| PyPy | ~5x faster | JIT-compiled Python |
| Cython | ~100x faster | Python-like compiled to C |
| mypyc | ~5x faster | Compile type-annotated Python |
| Mojo | ~1000x faster | Python superset compiled to LLVM |
| NumPy/PyTorch | Native speed | C/CUDA behind Python API |
| Rust extensions (PyO3) | Native speed | Rust modules callable from Python |

## Key Insight
Python won ML not because it's fast (it's the slowest major language) but because it minimizes the distance between mathematical notation and working code. `y = model(x)` is readable to anyone. This "executable pseudocode" quality, combined with the NumPy/PyTorch ecosystem, created an insurmountable network effect.

## References
→ [[Sources Index]]
