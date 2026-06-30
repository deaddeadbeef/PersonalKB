---
tags:
  - csa
  - csa/compression
confidence: verified
up: "[[Data Compression Overview]]"
tier-coverage: [intuition, core, deep-dive, practice]
---
# Run-Length Encoding

> **Lossless compression that replaces contiguous runs of the same symbol with (count, symbol) pairs — $O(n)$ and self-describing.**

## 🎯 Intuition
**The Core Idea:** Instead of storing every repeated symbol individually, count consecutive identical symbols and store the count once.
**Analogy:** Run-length encoding is like counting repeated tiles — instead of listing "white white white white black black", you write "4 white, 2 black". Simple and effective when long runs of the same symbol are common.
**Why It Matters:** RLE is the simplest compression scheme and often appears as a preprocessing stage in more sophisticated pipelines (TIFF, JPEG, fax standards).

---

## ⚙️ Core Mechanics
### Algorithm Steps
1. **Encoding**: scan the input left to right. For each contiguous run of identical symbols, output a (count, symbol) pair.
2. **Decoding**: for each (count, symbol) pair, emit the symbol `count` times.

### Pseudocode
**Encoding** (linear scan):
```
i = 1
while i ≤ n:
    count = 1
    while i + count ≤ n and input[i + count] = input[i]:
        count = count + 1
    output (count, input[i])
    i = i + count
```

**Decoding**: read each `(count, symbol)` pair; emit `symbol` exactly `count` times.

### Complexity

| Measure | Value |
|---------|-------|
| Encoding time | $O(n)$ |
| Decoding time | $O(n)$ |
| Space | No codebook or frequency table — self-describing format |

### Key Facts
- Simplest lossless compression scheme
- Effective when **expected run length is significantly greater than 2**
- Can **expand** data if every element is distinct (each run-1 symbol becomes a 2-element pair)
- No codebook or frequency table required — the format is self-describing
- Often used as one stage in a compression pipeline (not standalone)

---

## 🔬 Deep Dive
### Performance Characteristics

| Input type | Compression behaviour |
|---|---|
| Long homogeneous runs | Highly effective — e.g., 1000 white pixels → `(1000, white)` |
| Short mixed runs | Modest savings |
| Every element distinct | **Expansion** — each run of length 1 becomes a 2-element pair; output ≈ 2× input |

RLE works best when the **expected run length is significantly greater than 2**.

### Edge Cases and Pitfalls
- All-distinct input: RLE **doubles** the output size — a pathological worst case
- Single-element input: one (1, symbol) pair — trivial but correct
- Maximum run length: if count is stored as a fixed-width integer (e.g., 8 bits), runs longer than 255 must be split
- Binary data: runs of 0s and 1s — can alternate run length encoding (implied symbol, count only)
- Empty input: output is empty

### Limitations vs Alternatives

| Method | Advantage over RLE |
|---|---|
| Huffman coding | Better for non-run-structured text; exploits per-symbol frequency |
| LZW | Exploits longer repeated patterns, not just adjacent runs |
| DEFLATE (LZ77 + Huffman) | General-purpose; handles both repetition and frequency |

### Real-World Usage
**Fax Compression (ITU T.4)**: Black-and-white document pages consist mostly of white pixels with short black runs for text. Long white runs are common. The ITU T.4 standard (G3 fax) uses a variant of RLE tuned to typical document statistics — it codes runs using Huffman codes optimised for the expected distribution of run lengths rather than outputting a raw count. This combines RLE's structural advantage with Huffman's statistical advantage.

**Other uses**:
- TIFF images support RLE (PackBits)
- Some stages of JPEG/PNG preprocessing include run-length steps
- BMP image format uses RLE for 4-bit and 8-bit images

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Encode "AAABBBCCCCDDDDDD" using RLE. What is the compression ratio?
2. For what kind of input does RLE actually make the output larger than the input?

### Core Problems
1. **String Compression** (LeetCode 443): Implement in-place run-length encoding of a character array.
2. **Decode String** (LeetCode 394): Implement RLE decoding with nested brackets (e.g., "3[a2[c]]" → "accaccacc").
3. **RLE Iterator** (LeetCode 900): Implement an iterator that lazily decodes an RLE-encoded sequence.

### Challenge
**Compressed String Comparison**: Given two RLE-encoded strings, determine if they represent the same original string without fully decompressing either one. Analyse the time complexity of your solution.

---

*See also:* [[Huffman Coding]], [[LZW Compression]], [[Data Compression Overview]], [[Asymptotic Notation]], [[Arrays and Dynamic Arrays|Array]], [[CS Data Structures]]

## Supporting Chunks

### Supporting Chunks

- [[Compression - Run-length encoding encodes same-symbol runs as count-symbol pairs]]
- [[Compression - Run-length encoding is effective only when expected run length exceeds two symbols]]

## References

See [[CS Algorithms/Sources/Sources Index#Cormen 2013|Sources Index]], Chapter 9. See [[CS Algorithms/Sources/Sources Index#CP Algorithms - Online Reference|Sources Index]], RLE article. See [[Data Compression Overview]] for context among lossless compression methods. See [[Huffman Coding]] for the statistical approach.
