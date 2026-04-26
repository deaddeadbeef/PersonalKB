---
tags: [chunk, programming-languages, python-ml]
source: "[[raw-pl-011]]"
---

# chunk-pl-083 Python Data Science and ML Dominance

Python dominates data science and ML through the "glue language" pattern:

**The stack:**
- **NumPy:** N-dimensional arrays with C/Fortran performance
- **Pandas:** DataFrame for data manipulation (C underneath)
- **Matplotlib/Seaborn:** Visualization
- **scikit-learn:** Classical ML (classification, regression, clustering)
- **PyTorch:** Deep learning (C++/CUDA backend)
- **TensorFlow:** Deep learning (C++ backend)
- **Jupyter notebooks:** Interactive computing, visualization, reproducible research

**Why Python won ML:** Not performance (Python is slow). Python won because: the ecosystem is unmatched, the syntax is readable for non-programmers (scientists, analysts), and the glue pattern works (Python orchestrates C/CUDA kernels).

**The performance pattern:** Write high-level logic in Python. Heavy computation in optimized native code (NumPy operations, PyTorch tensors). The Python code is <1% of execution time — it's just dispatching to fast libraries.

**Alternatives tried:** Julia (faster but smaller ecosystem), R (statistics focus, less general), MATLAB (proprietary). None displaced Python because ecosystem network effects are overwhelming.
