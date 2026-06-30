---
tags: [llm, era-hub]
up: "[[LLM]]"
confidence: plausible
---
# 2017 — The Transformer

One paper changes everything. "Attention Is All You Need" (Vaswani et al., June 2017) replaces recurrence with parallelizable self-attention, enabling the scaling revolution that followed. The transformer architecture is the foundation of every modern large language model — GPT, BERT, LLaMA, PaLM, and their successors all descend directly from this design.

## The Translation Bottleneck

By 2016, neural machine translation based on encoder-decoder RNNs with attention (Bahdanau et al. 2015) had surpassed phrase-based statistical MT. But RNNs processed tokens sequentially, creating a training speed bottleneck that limited model scale. Attention over encoder states helped the decoder focus on relevant source positions, but the encoder itself still processed the input left-to-right. Researchers at Google Brain and Google Research asked: what if attention alone could replace the entire recurrent computation?

## The Paper

"Attention Is All You Need" was published by Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, and Polosukhin. It introduced the transformer: a model built entirely from attention layers and feed-forward networks, with no recurrence or convolution. Trained on WMT 2014 English-to-German and English-to-French translation, it achieved state-of-the-art BLEU scores while training significantly faster than existing RNN-based models. See [[Transformer Architecture]] for the full architectural walkthrough.

## Self-Attention and Multi-Head Attention

The core innovation is scaled dot-product attention: given queries Q, keys K, and values V, compute Attention(Q, K, V) = softmax(QK^T / $\sqrt{d_k}$)V. This allows every position to attend to every other position in a single operation — $O(n²·d)$ complexity but fully parallelizable, unlike the $O(n)$ sequential steps of RNNs. Multi-head attention runs h parallel attention functions with different learned projections, allowing the model to jointly attend to information from different representation subspaces. See [[Attention Mechanism]] for a deep dive into the mechanics.

## The Full Architecture

The original transformer uses an encoder-decoder structure with N=6 identical layers in each stack. Each encoder layer contains multi-head self-attention and a position-wise FFN, each wrapped with residual connections and layer normalization. The decoder adds masked (causal) self-attention and cross-attention to encoder outputs. The FFN uses a two-layer MLP with ReLU activation and a hidden dimension of 4× the model dimension (d_model = 512, d_ff = 2048 in the base model). See [[Encoder-Decoder Models]] for how this design was later adapted and split.

## Positional Encoding

Because self-attention is permutation-invariant — it has no inherent notion of token order — position information must be injected explicitly. The original paper used fixed sinusoidal positional encodings with different frequencies for each dimension: PE(pos, 2i) = sin(pos / 10000^(2i/d_model)). This approach theoretically allows generalization to unseen sequence lengths. Later work introduced learned positional embeddings, relative position encodings (Shaw et al. 2018), and rotary position embeddings (RoPE, Su et al. 2021). See [[Positional Encoding]].

## Why It Won

Three properties made the transformer dominant: (1) **parallelism** — self-attention processes all positions simultaneously, enabling efficient GPU/TPU utilization; (2) **expressiveness** — direct connections between all token pairs capture long-range dependencies without information bottlenecks; (3) **scalability** — performance improves predictably with more parameters, data, and compute, a property that would be formalized as scaling laws in 2020. The architecture's modular design also proved remarkably adaptable to tasks beyond translation.

## Immediate Impact

Within months, the transformer was adopted across NLP. It replaced RNNs in language modeling (Transformer-XL, Dai et al. 2019), machine translation (becoming the standard at Google Translate), and text generation. More importantly, it enabled the pretrain-then-fine-tune paradigm: by 2018, both BERT and GPT-1 would use transformer variants as the backbone for large-scale pretraining. The architectural split into encoder-only (BERT) and decoder-only (GPT) paths — explored in the next era — was a direct consequence of the transformer's modular design. See [[Transformer Breakthrough and Scaling Era]] for the broader historical context.

## Pages in This Era

- [[Transformer Architecture]]
- [[Attention Mechanism]]
- [[Positional Encoding]]
- [[Encoder-Decoder Models]]
- [[Transformer Breakthrough and Scaling Era]]

## Related Eras

← Previous: [[Pre-2017 — Before Transformers Overview|Pre-2017 — Before Transformers]]
→ Next: [[2018–2019 — Pretrained Language Models Overview|2018–2019 — Pretrained Language Models]]

## References
- [[LLM/Sources/Sources Index|LLM Sources Index]]
