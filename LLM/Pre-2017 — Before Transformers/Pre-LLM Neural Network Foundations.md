---
tags: [llm, history, neural-networks, foundations]
up: "[[Pre-2017 — Before Transformers Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---

# Pre-LLM Neural Network Foundations

> **One-line summary** Pre-LLM neural networks contributed the training machinery, representation idea, sequence-state problem, and first attention mechanisms that transformers later scaled into general-purpose language models.

Use this as the neural-network spine underneath [[Pre-Transformer Foundations]]. The older statistical era explained language with counts; the neural era asked a different question: can a differentiable model learn internal features, word meanings, sequence state, and alignment directly from data?

## Intuition

Pre-LLM neural networks were not yet large language models. They were mostly task-specific systems, feature extractors, or sequence models trained at far smaller scale. Their importance is that they introduced the reusable pieces that modern LLMs still depend on:

- **Backpropagation** made multi-layer representation learning trainable.
- **Distributed representations** replaced symbolic one-hot identity with dense vectors.
- **Recurrent state** made sequence history a learned object rather than a fixed n-gram window.
- **Gates** gave networks a controlled memory path, making LSTMs and GRUs usable on longer sequences than vanilla RNNs.
- **Encoder-decoder training** turned sequence transduction into one differentiable model.
- **Attention** removed the single-vector bottleneck by letting a decoder choose source positions dynamically.

The transformer did not discard this lineage. It kept learned embeddings, differentiable end-to-end training, softmax language modeling, and attention, then removed recurrence as the main sequence-processing bottleneck.

## Chronological Spine

| Era | Neural-network idea | Why it mattered for later LLMs |
|---|---|---|
| 1980s | Backpropagation for multi-layer networks | Made hidden representations learnable from error signals rather than hand-coded features. |
| 1990 | Simple recurrent networks | Treated time as a hidden state update problem, exposing the core long-dependency challenge. |
| 1997 | LSTM gating | Added explicit memory gates to reduce vanishing-gradient failure over long lags. |
| 1998 | Convolutional networks in document recognition | Showed end-to-end feature learning could replace hand-engineered pipelines in a real recognition system. |
| 2003 | Neural probabilistic language modeling | Joined word embeddings with next-word probability estimation to fight n-gram sparsity. |
| 2013-2014 | Word2Vec and GloVe | Made dense semantic word vectors cheap, reusable, and measurable through analogy/similarity tasks. |
| 2014 | GRU and RNN encoder-decoder | Simplified gated recurrence and encoded variable-length phrases into vectors for translation. |
| 2014 | Seq2seq LSTM | Made end-to-end sequence-to-sequence learning a general translation recipe. |
| 2014-2015 | Additive attention for neural MT | Let decoders softly align to source states, directly prefiguring transformer attention. |
| 2018 boundary | ELMo-style contextual word vectors | Showed bidirectional neural language models could produce context-dependent word features before BERT/GPT made transformers the default backbone. |

ELMo is included as a boundary case: it appears after the 2017 transformer paper, but it is still part of the recurrent pre-LLM lineage and clarifies the transition from static embeddings to contextual representations.

## Core Mechanics

### Backpropagation and Representation Learning

Backpropagation trains a network by propagating output error backward through layers and adjusting weights by gradient descent. Its LLM relevance is direct: modern pretraining is still a huge supervised-learning loop over token prediction losses, gradients, optimizers, and parameter updates. The scale changed; the learning mechanism stayed recognizable.

### Distributed Word Representations

One-hot word identities do not share statistical strength. Bengio et al.'s neural probabilistic language model learned word feature vectors jointly with a next-word probability model, addressing the n-gram curse of dimensionality by letting similar words support similar predictions. Word2Vec then made representation learning much cheaper through skip-gram/CBOW objectives and negative sampling; GloVe combined co-occurrence statistics with vector learning. Modern LLM token embeddings inherit the same principle, although their vectors become contextual after layers of attention.

### Recurrence, Gating, and the Sequence Bottleneck

RNNs update a hidden state one token at a time:

`h_t = f(W_h h_{t-1} + W_x x_t + b)`

This gives the model memory, but it creates two problems. First, information must pass through many sequential steps, which causes vanishing or exploding gradients. Second, training cannot fully parallelize across sequence positions. LSTMs and GRUs improved the memory problem with gates, but they did not remove the sequential compute bottleneck.

### Encoder-Decoder Models and Attention

Seq2seq models paired an encoder RNN with a decoder RNN. The first versions compressed the whole source sentence into one vector, which became a bottleneck for long inputs. Bahdanau attention changed the interface: the decoder could compute a weighted sum over encoder states at every output step. This made alignment differentiable and token-specific. Transformer self-attention generalizes the same idea inside a sequence: every token computes weighted access to other token states.

## What Carried Into LLMs

| Pre-LLM concept | Modern LLM descendant | Local inference relevance |
|---|---|---|
| Backpropagation and loss minimization | Pretraining, SFT, preference optimization, adapter training | Explains why quality changes require data/loss evidence, not just prompt hope. |
| Learned word vectors | Token embedding tables and hidden states | Explains tokenizer/model coupling and why embedding models power RAG. |
| Softmax next-word prediction | Causal LM logits over vocabulary | Explains logits, temperature, top-p/top-k, and decode controls. |
| Recurrent hidden state | Transformer KV cache during autoregressive decoding | Both preserve past context for next-token prediction, but KV cache stores attention keys/values rather than one compressed state. |
| Gating | LSTM/GRU memory gates; later GLU/SwiGLU feed-forward variants | Explains controlled information flow and why modern MLP blocks are not simple linear stacks. |
| Encoder-decoder translation | Transformer encoder-decoder, encoder-only, and decoder-only families | Explains why local model architecture affects chat, completion, embedding, and translation workloads. |
| Additive attention | Scaled dot-product self-attention and cross-attention | Explains why attention replaced recurrence and why KV-cache memory dominates long-context inference. |

## What Was Still Missing

- **No transformer-style parallel sequence processing.** RNN-family models still processed tokens serially.
- **No reliable long-context mechanism.** Gating helped, but hidden-state compression and gradient path length remained limiting.
- **No general foundation-model workflow.** Many systems were trained for one task or used pretrained features, but broad instruction-following assistants were not yet the operating target.
- **No mature local-serving stack.** There was no routine path from open model artifact to quantized local chat endpoint, benchmark row, safety proof, and deployment memo.
- **No clean separation of prefill and decode evidence.** Modern local inference analysis depends on transformer-specific phases, KV cache, batching, and token-level streaming behavior.

## Study Handles

If you can explain this note, you should be able to answer:

1. Why did learned embeddings solve a different problem from RNN recurrence?
2. Why did LSTM gates help but not make recurrence scale like transformers?
3. What exactly did attention fix in encoder-decoder translation?
4. Why is a transformer KV cache not just an RNN hidden state?
5. Which pre-LLM ideas are still visible when you run a local chat model and inspect tokens, logits, TTFT, decode speed, and memory?

## Practice

### Warm-Up

1. Draw the path from one-hot token to embedding vector to hidden representation.
2. Explain the vanishing-gradient problem without using equations.
3. Compare static embeddings, recurrent contextual state, and transformer contextual state.

### Core Problems

1. Given a local LLM response, identify which observed artifacts descend from pre-LLM neural-network ideas: tokenization, embeddings, logits, softmax sampling, hidden states, attention, and training loss.
2. Explain why a recurrent encoder-decoder needed attention for long translation inputs, then map that explanation to why transformers use self-attention over all token positions.

### Challenge

1. Defend this claim: transformers were not a break from neural networks; they were a parallelizable reorganization of existing neural-network ingredients around attention.

## See Also

- [[Pre-2017 — Before Transformers Overview]]
- [[Pre-Transformer Foundations]]
- [[Embeddings and Representation Geometry]]
- [[Language Model Fundamentals]]
- [[Optimizers and Training Stability]]
- [[Attention Mechanism]]
- [[Transformer Architecture]]
- [[LLM/Study/Local LLM End-to-End Mental Model]]
- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]]

## Evidence Status

This note is currently backed by external primary papers rather than vault-local `_chunks`. Future raw/chunk ingest can promote the cited papers into local source notes, but the academic claims above are intentionally tied to the paper links below.

## References

- Rumelhart, Hinton, and Williams, 1986, "Learning representations by back-propagating errors", Nature: https://www.nature.com/articles/323533a0
- Elman, 1990, "Finding Structure in Time", Cognitive Science: https://onlinelibrary.wiley.com/doi/abs/10.1207/s15516709cog1402_1
- Hochreiter and Schmidhuber, 1997, "Long Short-Term Memory", Neural Computation: https://direct.mit.edu/neco/article/9/8/1735/6109/Long-Short-Term-Memory
- LeCun, Bottou, Bengio, and Haffner, 1998, "Gradient-Based Learning Applied to Document Recognition", Proceedings of the IEEE: https://ieeexplore.ieee.org/document/726791
- Bengio, Ducharme, Vincent, and Jauvin, 2003, "A Neural Probabilistic Language Model", JMLR: https://www.jmlr.org/papers/v3/bengio03a.html
- Mikolov, Chen, Corrado, and Dean, 2013, "Efficient Estimation of Word Representations in Vector Space": https://arxiv.org/abs/1301.3781
- Pennington, Socher, and Manning, 2014, "GloVe: Global Vectors for Word Representation", ACL Anthology: https://aclanthology.org/D14-1162/
- Cho et al., 2014, "Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation": https://arxiv.org/abs/1406.1078
- Sutskever, Vinyals, and Le, 2014, "Sequence to Sequence Learning with Neural Networks": https://arxiv.org/abs/1409.3215
- Bahdanau, Cho, and Bengio, 2014, "Neural Machine Translation by Jointly Learning to Align and Translate": https://arxiv.org/abs/1409.0473
- Peters et al., 2018, "Deep Contextualized Word Representations", ACL Anthology: https://aclanthology.org/N18-1202/
