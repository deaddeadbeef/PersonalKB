---
tags: [chunk, programming-languages, python]
source: "[[raw-pl-011]]"
---

# chunk-pl-032 Python Readability and the Glue Language Pattern

Python's design philosophy (Zen of Python): *"Readability counts. There should be one obvious way to do it. Beautiful is better than ugly."*

**Dynamic typing, strong guarantees:** No implicit coercion — "3" + 3 is TypeError. Types checked at runtime but consistently enforced.

**Duck typing:** Check capabilities, not types. Any object with __len__ works with len(). Polymorphism without inheritance.

**The glue language pattern:** Python orchestrates fast libraries. NumPy (C/Fortran), PyTorch (C++/CUDA), Pandas (C). Write high-level logic in Python, heavy computation in optimized native code. This is why Python dominates data science and ML despite being 10-100x slower than C.

**The GIL trade-off:** Only one thread executes Python bytecode at a time. Simplifies interpreter, makes C extensions easy. Limits parallelism. Workarounds: multiprocessing, asyncio, C extensions releasing GIL. Python 3.13: experimental free-threaded mode.

**Packaging chaos:** pip, setuptools, poetry, conda, uv — fragmented but converging. This is Python's biggest developer experience weakness.
