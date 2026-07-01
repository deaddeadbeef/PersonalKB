---
tags: [study, llm, transformer, training, decoder-only, implementation, lab]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
freshness: stable
tier-coverage: [core, deep-dive, practice]
---

# Tiny Decoder-Only Transformer Training Lab

> **One-line summary** Training a tiny decoder-only transformer makes the academic core tangible: tokens become logits, logits become cross-entropy loss, loss becomes gradients, and the trained model can autoregressively generate text.

Use this after [[LLM/Study/LLM Math and Tensor Shape Primer|LLM Math and Tensor Shape Primer]], [[LLM/Study/Attention Implementation Lab|Attention Implementation Lab]], [[LLM/Pre-2017 — Before Transformers/Language Model Fundamentals|Language Model Fundamentals]], and [[LLM/Pre-2017 — Before Transformers/Language Modeling Objectives|Language Modeling Objectives]]. The math primer proves the core objects and shapes; the attention lab proves the main tensor operation. This lab proves the whole causal language-model training loop.

Use it before treating [[LLM/Study/LLM Training Pipeline Map|LLM Training Pipeline Map]] as only a conceptual map. The point is not to train a useful assistant. The point is to see, in a small controlled setting, what pretraining optimizes and why local inference later uses the same logits, sampling, and autoregressive loop.

## Outcome

After this lab you should be able to:

- build a tiny decoder-only language model with token embeddings, positional embeddings, causal self-attention, MLP blocks, layer norm, and an output head
- create next-token training pairs from a small corpus
- compute cross-entropy loss from logits and target token IDs
- run teacher-forced training with AdamW and gradient clipping
- separate training loss from validation loss and identify overfitting
- generate text autoregressively from the trained model
- explain how this toy loop scales into pretraining, SFT, and local inference

## Mental Model

The causal LM loop has two modes:

| Mode | Input | Target | What changes |
| --- | --- | --- | --- |
| Training | Ground-truth prefix tokens | The next ground-truth token at every position | Model weights change via gradients. |
| Inference | Prompt tokens plus generated tokens so far | No ground-truth target | Model weights stay fixed; one sampled token is appended at a time. |

Teacher forcing means the model sees the true previous tokens during training, even if it would have generated a different token at inference time. This makes training parallel over positions but creates the familiar gap between low training loss and robust generation quality.

## Minimal Architecture

The model should be deliberately small:

| Component | Purpose | Shape intuition |
| --- | --- | --- |
| Token embedding | Convert token IDs into vectors | `[batch, time] -> [batch, time, d_model]` |
| Positional embedding | Tell the model where each token sits | Added to token embeddings. |
| Decoder block | Causal self-attention plus MLP | Preserves `[batch, time, d_model]`. |
| Causal mask | Prevent future-token leakage | Scores above diagonal are masked before softmax. |
| Final layer norm | Stabilize hidden states before logits | `[batch, time, d_model]`. |
| LM head | Map hidden vectors to vocabulary logits | `[batch, time, vocab_size]`. |

The simplest useful stack is 2 layers, 2-4 heads, context length 64-128, and a small character or byte-level vocabulary. Character-level tokenization is acceptable here because the lesson is the training loop, not tokenizer quality.

## Data Setup

Use a tiny public or synthetic corpus, not private notes.

| Step | Evidence |
| --- | --- |
| Choose text | Local file path, source note, or synthetic sample. |
| Build vocabulary | Character or byte vocabulary plus special tokens if used. |
| Encode text | `stoi` and `itos` mappings or tokenizer output. |
| Split train/validation | A fixed boundary, for example first 90 percent train, last 10 percent validation. |
| Create batches | Random start positions, context window, input `x`, target `y = next token`. |

For one sequence:

```text
tokens:  [t0, t1, t2, t3, t4]
input:   [t0, t1, t2, t3]
target:  [t1, t2, t3, t4]
```

The target is shifted by one position. This is the entire next-token objective in miniature.

## Minimal PyTorch Skeleton

This is intentionally compact. It is a study scaffold, not a production training script.

```python
import math
import torch
import torch.nn as nn
import torch.nn.functional as F


class CausalSelfAttention(nn.Module):
    def __init__(self, d_model, n_heads, context_len, dropout=0.0):
        super().__init__()
        assert d_model % n_heads == 0
        self.n_heads = n_heads
        self.head_dim = d_model // n_heads
        self.qkv = nn.Linear(d_model, 3 * d_model)
        self.proj = nn.Linear(d_model, d_model)
        self.dropout = nn.Dropout(dropout)
        mask = torch.tril(torch.ones(context_len, context_len))
        self.register_buffer("causal_mask", mask.view(1, 1, context_len, context_len))

    def forward(self, x):
        b, t, d = x.shape
        q, k, v = self.qkv(x).chunk(3, dim=-1)
        q = q.view(b, t, self.n_heads, self.head_dim).transpose(1, 2)
        k = k.view(b, t, self.n_heads, self.head_dim).transpose(1, 2)
        v = v.view(b, t, self.n_heads, self.head_dim).transpose(1, 2)

        scores = (q @ k.transpose(-2, -1)) / math.sqrt(self.head_dim)
        scores = scores.masked_fill(self.causal_mask[:, :, :t, :t] == 0, float("-inf"))
        weights = torch.softmax(scores, dim=-1)
        weights = self.dropout(weights)
        out = weights @ v
        out = out.transpose(1, 2).contiguous().view(b, t, d)
        return self.proj(out)


class DecoderBlock(nn.Module):
    def __init__(self, d_model, n_heads, context_len, dropout=0.0):
        super().__init__()
        self.ln1 = nn.LayerNorm(d_model)
        self.attn = CausalSelfAttention(d_model, n_heads, context_len, dropout)
        self.ln2 = nn.LayerNorm(d_model)
        self.mlp = nn.Sequential(
            nn.Linear(d_model, 4 * d_model),
            nn.GELU(),
            nn.Linear(4 * d_model, d_model),
            nn.Dropout(dropout),
        )

    def forward(self, x):
        x = x + self.attn(self.ln1(x))
        x = x + self.mlp(self.ln2(x))
        return x


class TinyDecoderLM(nn.Module):
    def __init__(self, vocab_size, context_len=128, d_model=128, n_heads=4, n_layers=2):
        super().__init__()
        self.context_len = context_len
        self.token_embed = nn.Embedding(vocab_size, d_model)
        self.pos_embed = nn.Embedding(context_len, d_model)
        self.blocks = nn.ModuleList(
            [DecoderBlock(d_model, n_heads, context_len) for _ in range(n_layers)]
        )
        self.ln = nn.LayerNorm(d_model)
        self.head = nn.Linear(d_model, vocab_size, bias=False)

    def forward(self, idx, targets=None):
        b, t = idx.shape
        pos = torch.arange(t, device=idx.device)
        x = self.token_embed(idx) + self.pos_embed(pos)
        for block in self.blocks:
            x = block(x)
        logits = self.head(self.ln(x))
        loss = None
        if targets is not None:
            loss = F.cross_entropy(logits.reshape(b * t, -1), targets.reshape(b * t))
        return logits, loss
```

## Training Loop

The loop should log enough evidence to distinguish learning from memorization.

```python
model = TinyDecoderLM(vocab_size=len(vocab)).to(device)
optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4, weight_decay=0.1)

for step in range(max_steps):
    xb, yb = get_batch("train")
    logits, loss = model(xb, yb)
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
    optimizer.step()

    if step % eval_interval == 0:
        train_loss = estimate_loss("train")
        val_loss = estimate_loss("val")
        print(step, train_loss, val_loss)
```

Key checks:

- `logits.shape == [batch, context_len, vocab_size]`
- `targets.shape == [batch, context_len]`
- loss decreases on train batches
- validation loss is measured on held-out text
- validation loss eventually stops improving if the tiny model overfits
- gradient clipping does not hide NaNs or broken loss

## Generation Loop

Generation reuses the same model, but no target tokens are supplied.

```python
@torch.no_grad()
def generate(model, idx, max_new_tokens, temperature=1.0, top_k=None):
    for _ in range(max_new_tokens):
        idx_cond = idx[:, -model.context_len:]
        logits, _ = model(idx_cond)
        logits = logits[:, -1, :] / temperature
        if top_k is not None:
            values, _ = torch.topk(logits, top_k)
            logits[logits < values[:, [-1]]] = -float("inf")
        probs = torch.softmax(logits, dim=-1)
        next_id = torch.multinomial(probs, num_samples=1)
        idx = torch.cat([idx, next_id], dim=1)
    return idx
```

This is the same high-level inference loop used by local model servers:

1. condition on the current context
2. compute next-token logits
3. apply sampling controls
4. select a token
5. append it
6. repeat until stop or max output tokens

## Debugging Table

| Symptom | Likely cause | First fix |
| --- | --- | --- |
| Loss is `nan` | Learning rate too high, mask bug, invalid logits, or numerical instability | Lower LR, inspect masks, check logits for `inf`/`nan`. |
| Loss does not move | Targets not shifted, optimizer not stepping, model too small, or data constant | Print `x/y` examples, check gradients, verify optimizer step. |
| Train loss falls but validation worsens | Overfitting or data leakage | Reduce steps/model size or improve validation split. |
| Model predicts future tokens during training | Causal mask bug | Test attention weights above diagonal are zero. |
| Generated text repeats | Tiny corpus, low diversity, low temperature, or overfitting | Adjust sampling, train on more text, compare train/val loss. |
| Generated text is random after training | Undertraining, bad token mapping, or too high temperature | Lower temperature and inspect reconstruction on train text. |
| Context longer than training window fails | Position embedding/context limit | Keep generation context within `context_len` or train longer context. |

## What To Explain After The Lab

Use this as an oral proof:

| Question | Passing answer |
| --- | --- |
| Why are targets shifted by one token? | The model predicts the next token at each position. |
| Why is causal masking needed during training? | Teacher forcing exposes the full sequence tensor; the mask prevents future-token leakage. |
| What is the cross-entropy loss comparing? | Vocabulary logits at each position against the true next token ID. |
| Why does validation loss matter? | It detects whether the model learned general sequence structure or only memorized train text. |
| Why does inference run sequentially? | Each new token depends on the previous generated token. |
| Why can training be parallel over sequence positions? | Teacher forcing provides all previous ground-truth tokens in one tensor while the mask enforces causality. |
| How does this connect to local hosting? | The served model is a larger trained version of the same logits-to-sampling generation loop. |

## Completion Gate

This lab is complete when you have:

- [ ] a tiny corpus and fixed train/validation split
- [ ] vocabulary/tokenization evidence
- [ ] input/target shift example
- [ ] attention mask test proving future positions are hidden
- [ ] model parameter count
- [ ] training and validation loss samples
- [ ] one generated sample at low temperature
- [ ] one generated sample at higher temperature or top-k
- [ ] one short explanation of overfitting or undertraining evidence
- [ ] one link from this lab to a later [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] row or an explicit note that this is a toy training-only proof

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Pre-2017 — Before Transformers/Language Model Fundamentals]]
- [[LLM/Pre-2017 — Before Transformers/Language Modeling Objectives]]
- [[LLM/Pre-2017 — Before Transformers/Perplexity and Intrinsic Metrics]]
- [[LLM/Pre-2017 — Before Transformers/Optimizers and Training Stability]]
- [[LLM/2017 — The Transformer/Attention Mechanism]]
- [[LLM/2017 — The Transformer/Transformer Architecture]]
- [[LLM/2018–2019 — Pretrained Language Models/Decoder-Only Models]]
- [[LLM/Study/Attention Implementation Lab]]
- [[LLM/Study/LLM Math and Tensor Shape Primer]]
- [[LLM/Study/LLM Training Pipeline Map]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/LLM Mastery Roadmap]]
