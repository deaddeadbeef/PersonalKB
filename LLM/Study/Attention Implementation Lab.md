---
tags: [study, llm, attention, implementation, lab]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [practice, deep-dive]
---

# Attention Implementation Lab

> **One-line summary** Implementing attention turns the transformer formula from a memorized expression into a concrete tensor program: project Q/K/V, compute scaled scores, apply masks, softmax, aggregate values, and verify every shape.

Use this after reading [[LLM/2017 — The Transformer/Attention Mechanism|Attention Mechanism]] and [[LLM/2017 — The Transformer/Transformer Architecture|Transformer Architecture]]. This lab is the capstone proof for "implement scaled dot-product attention and explain the tensor shapes" in [[LLM/Study/LLM Mastery Roadmap|LLM Mastery Roadmap]].

## Target Competence

After this lab you should be able to:

- implement scaled dot-product attention from Q, K, and V
- explain why the score tensor has shape `[batch, heads, query_len, key_len]`
- apply padding masks and causal masks before softmax
- reshape tensors for multi-head attention
- explain why MQA and GQA reduce KV-cache memory during inference
- write tests that catch shape, masking, and normalization bugs

## Core Formula

Scaled dot-product attention is:

```text
Attention(Q, K, V) = softmax((Q K^T) / sqrt(d_k)) V
```

The key source-backed anchors are [[LLM/_chunks/chunk-llm-001 Scaled Dot-Product Attention Formula|scaled dot-product attention]] and [[LLM/_chunks/chunk-llm-002 Multi-Head Attention Parallel Projections|multi-head attention projections]].

## Tensor Shapes

Use these symbols consistently:

| Symbol | Meaning |
| --- | --- |
| `B` | batch size |
| `Tq` | query sequence length |
| `Tk` | key/value sequence length |
| `D` | model width, also called `d_model` |
| `H` | number of query heads |
| `Dh` | per-head dimension, usually `D / H` |
| `G` | number of key/value head groups for GQA |

Single-head attention:

| Tensor | Shape | Meaning |
| --- | --- | --- |
| `Q` | `[B, Tq, Dh]` | What each query position is looking for |
| `K` | `[B, Tk, Dh]` | What each key position offers for matching |
| `V` | `[B, Tk, Dv]` | What information is aggregated |
| `scores` | `[B, Tq, Tk]` | Similarity between every query and key |
| `weights` | `[B, Tq, Tk]` | Softmax-normalized attention distribution |
| `output` | `[B, Tq, Dv]` | Weighted sum of value vectors |

Multi-head self-attention:

| Tensor | Shape | Meaning |
| --- | --- | --- |
| `X` | `[B, T, D]` | Input token representations |
| `Q, K, V` after projection | `[B, T, H, Dh]` | Per-head projections |
| `Q, K, V` after transpose | `[B, H, T, Dh]` | Head dimension moved before sequence for batched matmul |
| `scores` | `[B, H, T, T]` | Each head gets its own attention matrix |
| `head_output` | `[B, H, T, Dh]` | One output stream per head |
| `concat` | `[B, T, H * Dh]` | Heads concatenated back to model width |
| `output` | `[B, T, D]` | Final output projection |

The score tensor is quadratic in sequence length. This is why long-context attention is expensive and why [[LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants|efficient attention]] and [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse|KV-cache optimization]] matter for deployment.

## Minimal Scaled Dot-Product Attention

This is the smallest implementation worth understanding.

```python
import math
import torch


def scaled_dot_product_attention(q, k, v, mask=None):
    """q: [B, H, Tq, Dh], k/v: [B, H, Tk, Dh]."""
    d_k = q.size(-1)
    scores = q @ k.transpose(-2, -1)
    scores = scores / math.sqrt(d_k)

    if mask is not None:
        scores = scores.masked_fill(mask == 0, float("-inf"))

    weights = torch.softmax(scores, dim=-1)
    out = weights @ v
    return out, weights
```

What must be true:

- `k.transpose(-2, -1)` changes `[B, H, Tk, Dh]` into `[B, H, Dh, Tk]`.
- `q @ k^T` produces `[B, H, Tq, Tk]`.
- `softmax(..., dim=-1)` normalizes across keys, so every query position distributes probability over source positions.
- `weights @ v` produces `[B, H, Tq, Dh]`.

## Causal Mask

Decoder-only models must not attend to future tokens during training or generation.

```python
def causal_mask(seq_len, device=None):
    # Shape broadcasts to [B, H, T, T].
    return torch.tril(torch.ones(seq_len, seq_len, device=device)).view(1, 1, seq_len, seq_len)
```

Masking must happen before softmax. If future positions are masked after softmax, probability mass has already leaked into illegal positions.

## Multi-Head Self-Attention Skeleton

```python
class MultiHeadSelfAttention(torch.nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        assert d_model % num_heads == 0
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads

        self.q_proj = torch.nn.Linear(d_model, d_model)
        self.k_proj = torch.nn.Linear(d_model, d_model)
        self.v_proj = torch.nn.Linear(d_model, d_model)
        self.o_proj = torch.nn.Linear(d_model, d_model)

    def split_heads(self, x):
        b, t, d = x.shape
        x = x.view(b, t, self.num_heads, self.head_dim)
        return x.transpose(1, 2)

    def merge_heads(self, x):
        b, h, t, dh = x.shape
        x = x.transpose(1, 2).contiguous()
        return x.view(b, t, h * dh)

    def forward(self, x, mask=None):
        q = self.split_heads(self.q_proj(x))
        k = self.split_heads(self.k_proj(x))
        v = self.split_heads(self.v_proj(x))
        out, weights = scaled_dot_product_attention(q, k, v, mask)
        out = self.merge_heads(out)
        return self.o_proj(out), weights
```

The important implementation detail is not the class structure. It is the reshape discipline: projection creates `[B, T, D]`, splitting heads creates `[B, H, T, Dh]`, attention runs per head, and merging returns `[B, T, D]`.

## Tests To Run

Use tiny tensors so you can inspect failures.

| Test | What it catches |
| --- | --- |
| Output shape is `[B, H, Tq, Dh]` for raw attention | Wrong matmul axes |
| Weights shape is `[B, H, Tq, Tk]` | Wrong transpose or missing head axis |
| `weights.sum(dim=-1)` is all ones | Softmax along wrong dimension |
| Causal mask gives zero probability to future keys | Mask applied after softmax or wrong mask shape |
| Identical Q/K rows produce symmetric scores before masking | Projection or transpose bug |
| Single-token sequence returns the value vector | Softmax or matmul bug |

Minimal check:

```python
B, H, T, Dh = 2, 4, 5, 8
q = torch.randn(B, H, T, Dh)
k = torch.randn(B, H, T, Dh)
v = torch.randn(B, H, T, Dh)
mask = causal_mask(T, q.device)

out, weights = scaled_dot_product_attention(q, k, v, mask)

assert out.shape == (B, H, T, Dh)
assert weights.shape == (B, H, T, T)
assert torch.allclose(weights.sum(dim=-1), torch.ones(B, H, T), atol=1e-5)
assert torch.all(weights.masked_select(mask == 0) == 0)
```

## Debugging Checklist

| Symptom | Likely bug |
| --- | --- |
| Output has shape `[B, T, H, Dh]` unexpectedly | Forgot to transpose heads before or after attention |
| Weights do not sum to 1 | Softmax applied over the wrong dimension |
| Future tokens affect decoder output | Causal mask missing, inverted, or applied after softmax |
| NaNs appear with fully masked rows | A query has no legal keys after masking |
| Training is unstable | Missing `1 / sqrt(d_k)` scaling or bad initialization |
| Inference memory is unexpectedly high | Full MHA KV cache where MQA/GQA would reduce KV heads |

## Extension: MQA And GQA

Standard MHA gives each query head its own K and V. [[LLM/_chunks/chunk-llm-213 Multi-Query Attention Shared KV Heads|MQA]] shares one K/V set across all query heads. GQA shares K/V across groups of query heads.

| Variant | Query heads | Key/value heads | KV-cache implication |
| --- | --- | --- | --- |
| MHA | `H` | `H` | Highest KV memory |
| MQA | `H` | `1` | Lowest KV memory, less KV diversity |
| GQA | `H` | `G`, where `1 < G < H` | Middle ground |

This is the implementation-level reason attention design affects local inference. During generation, previous K/V tensors are cached. Fewer KV heads mean fewer cached tensors per token, which lowers memory pressure and bandwidth use. See [[LLM/_chunks/chunk-llm-216 MQA Foundational KV Optimization|MQA as a KV optimization]] and [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]].

## Completion Gate

This lab is complete when you can:

- write scaled dot-product attention without looking at the formula
- explain every tensor shape from `X` to `scores` to merged output
- show why softmax runs over keys
- build and apply a causal mask before softmax
- explain why attention is `O(T^2)` in sequence length
- explain how MQA/GQA change the KV-cache footprint
- connect the implementation to one local inference bottleneck in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]]

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/2017 — The Transformer/Attention Mechanism]]
- [[LLM/2017 — The Transformer/Transformer Architecture]]
- [[LLM/Study/LLM Architecture Cheatsheet]]
- [[LLM/Study/LLM Mastery Roadmap]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/_chunks/chunk-llm-001 Scaled Dot-Product Attention Formula]]
- [[LLM/_chunks/chunk-llm-002 Multi-Head Attention Parallel Projections]]
- [[LLM/_chunks/chunk-llm-213 Multi-Query Attention Shared KV Heads]]
- [[LLM/_chunks/chunk-llm-216 MQA Foundational KV Optimization]]
