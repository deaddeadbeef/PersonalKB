---
tags: [llm, era-hub]
up: "[[LLM]]"
---

# Pre-2017 — Before Transformers

The foundations of modern language AI — from counting words to learning representations. Every technique that powers today's frontier models traces back to ideas developed in this era: statistical language modeling, dense vector representations, recurrent sequence processing, and subword segmentation. Understanding these roots is essential for understanding why the transformer was such a breakthrough.

## The Statistical NLP Era

For decades, language modeling meant counting. N-gram models — bigrams, trigrams, and their smoothed variants (Kneser-Ney, modified Kneser-Ney) — estimated the probability of the next word by tallying co-occurrence frequencies in large corpora. These models powered machine translation (IBM Models, phrase-based MT), speech recognition, and spelling correction throughout the 1990s and 2000s. Their fundamental limitation was the curse of dimensionality: the number of possible n-grams grows exponentially with n, making it impossible to capture long-range dependencies. See [[Language Model Fundamentals]] for a comprehensive treatment.

## The Neural Network Lineage

Pre-LLM neural networks supplied the trainable machinery that later made transformers useful: backpropagation, hidden representations, learned word vectors, recurrent state, gating, encoder-decoder sequence modeling, and attention. This lineage matters because modern local LLM behavior still exposes these ingredients as embeddings, logits, loss, attention states, KV cache, and sampling controls. The transformer breakthrough was not a rejection of neural networks; it was a parallelizable reorganization of this lineage around self-attention. See [[Pre-LLM Neural Network Foundations]] for the academic spine and the bridge to local inference.

## Neural Word Representations

The key conceptual leap was learning continuous vector representations of words. Bengio et al. (2003) introduced the neural probabilistic language model, showing that words could be embedded in a dense vector space where similar words cluster together. This idea matured with Word2Vec (Mikolov et al. 2013), which demonstrated that simple shallow networks trained on skip-gram or CBOW objectives could produce embeddings encoding remarkable analogical relationships (e.g., king − man + woman ≈ queen). GloVe (Pennington et al. 2014) combined global co-occurrence statistics with local context windows. These static embeddings became the default input representation for virtually all NLP models. See [[Embeddings and Representation Geometry]] for the full story.

## Recurrent Architectures

Recurrent neural networks (RNNs), LSTMs (Hochreiter & Schmidhuber, 1997), and GRUs processed sequences token-by-token, maintaining a hidden state that in theory could capture arbitrary-length dependencies. In practice, vanilla RNNs suffered from vanishing/exploding gradients; LSTMs mitigated this with gating mechanisms. Seq2seq models (Sutskever et al. 2014) paired an encoder RNN with a decoder RNN, and the addition of Bahdanau attention (2015) allowed the decoder to selectively attend to encoder hidden states — a direct precursor to transformer attention. These architectures dominated machine translation, summarization, and language modeling until 2017. See [[Pre-LLM Neural Network Foundations]] for the academic lineage and [[Pre-Transformer Foundations]] for the broader recurrent-to-transformer bridge.

## Subword Tokenization

The vocabulary problem — how to handle rare words, morphological variants, and multilingual text — was solved by subword methods. Byte-Pair Encoding (BPE, Sennrich et al. 2016) iteratively merges the most frequent character pairs to build a vocabulary of subword units, balancing coverage with compactness. SentencePiece (Kudo & Richardson, 2018) later made this language-agnostic and reversible. WordPiece (used in BERT) and Unigram (used in T5) offered alternative segmentation strategies. Subword tokenization remains the universal preprocessing step for all modern LLMs. See [[Tokenization]].

## Evaluation Roots

Perplexity — the exponentiated average cross-entropy loss — became the standard intrinsic metric for language models, measuring how well a model predicts held-out text. Lower perplexity means better next-token prediction. While perplexity correlates with downstream task performance, the relationship is not always monotonic, and the field would later supplement it with task-specific benchmarks, human evaluation, and LLM-as-judge protocols. See [[Perplexity and Intrinsic Metrics]].

## Training Fundamentals

Stochastic gradient descent and its adaptive variants — Adam (Kingma & Ba, 2015), AdaGrad, RMSProp — provided the optimization backbone for neural NLP. Learning rate scheduling (warmup, cosine decay), gradient clipping, and weight initialization strategies were all established in this era. These training recipes would carry forward into the transformer era with remarkably little modification. See [[Optimizers and Training Stability]] and [[Language Modeling Objectives]] for pretraining objectives that connect to these foundations.

## What Was Missing

Despite this progress, pre-transformer NLP suffered from three critical limitations: (1) sequential processing made training slow and hard to parallelize, (2) long-range dependencies were difficult to capture even with LSTMs, and (3) there was no effective mechanism for transfer learning — each task required training from scratch. The transformer would address all three.

## Pages in This Era

- [[Language Model Fundamentals]]
- [[Embeddings and Representation Geometry]]
- [[Tokenization]]
- [[Pre-LLM Neural Network Foundations]]
- [[Pre-Transformer Foundations]]
- [[Perplexity and Intrinsic Metrics]]
- [[Language Modeling Objectives]]
- [[Optimizers and Training Stability]]

## Related Eras

→ Next: [[2017 — The Transformer Overview|2017 — The Transformer]]
