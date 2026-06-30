---
tags: [llm, multimodal]
up: "[[2023 — Open Models and Agents Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Multimodal Tokenization and Fusion
> **One-line summary:** Multimodal systems must first turn images, audio, and video into tokens, then decide how those tokens interact with text.

---

## 🎯 Intuition

### Core Idea
Multimodal tokenization converts raw sensory signals—images, audio, video—into token sequences that transformers can process, while fusion strategies determine how and when these modality-specific tokens interact. These design choices fundamentally shape a model's capabilities, efficiency, and the tightness of its cross-modal reasoning.

### Analogy
Multimodal AI is AI that can see, hear, AND read — like upgrading from email to video call.

### Why It Matters
Tokenization and fusion are not implementation details—they are the core architectural decisions that determine what a multimodal model can and cannot do. The token tax problem is acute: a model with a 128K context window that spends 50K tokens on images has only 78K left for text reasoning. Compression techniques that reduce visual tokens without losing critical information directly expand the model's effective reasoning capacity. Similarly, the choice between early and late fusion determines whether a model can perform fine-grained cross-modal reasoning ("what does the text in the bottom-left of this image say?") or is limited to coarse-grained matching ("this image is about dogs").

---

## ⚙️ Core Mechanics

### How It Works
Image tokenization is the most mature non-text modality. The dominant approach uses a Vision Transformer (ViT) to split an image into non-overlapping patches (typically 14×14 or 16×16 pixels), linearly embed each patch, and process them through transformer layers to produce a sequence of continuous visual tokens. A 224×224 image with 14×14 patches yields 256 tokens; a 336×336 image yields 576. Self-supervised variants like DINO and DINOv2 produce patch features with strong spatial semantics without requiring text supervision. An alternative paradigm uses VQ-VAE (Vector Quantized Variational Autoencoder) to map image patches to discrete codebook entries, producing a sequence of integer tokens that can be directly embedded in a language model's vocabulary—this is the approach behind DALL-E's image tokenizer and is conceptually elegant because it unifies all modalities into discrete token sequences.

Audio tokenization follows a parallel evolution. The traditional approach converts raw waveforms to mel spectrograms—2D time-frequency representations that can be processed by ViT-like architectures. Neural audio codecs like Meta's EnCodec and Google's SoundStream take the discrete-token route: they compress audio into sequences of codes from learned codebooks at multiple quantization levels (e.g., 8 codebooks at 75 Hz), producing hierarchical discrete representations where the first codebook captures coarse structure and subsequent codebooks add detail. These discrete audio tokens can be interleaved with text tokens in a unified vocabulary, enabling models like AudioLM and MusicLM.

Fusion strategy—how and when modality tokens interact—is perhaps the most consequential architectural decision. Early fusion interleaves tokens from all modalities into a single sequence processed by one transformer (Gemini's approach): image tokens, text tokens, and audio tokens appear as a unified stream with modality-specific positional encodings. This allows deep cross-modal attention from the first layer but imposes a heavy token tax. Late fusion processes each modality through separate encoders and combines representations only at the final layers, preserving modality-specific processing but limiting cross-modal interaction. Cross-attention fusion (Flamingo's approach) inserts cross-attention layers into the LLM that attend to frozen visual features, offering a middle ground: the LLM's text processing is minimally disrupted while gaining access to visual information at selected layers.

### Key Specifications
- **ViT patch tokenization**: Image → non-overlapping patches → linear projection → transformer layers → sequence of continuous tokens; 224px/14px patches = 256 tokens, 336px/14px = 576 tokens.
- **DINO/DINOv2 features**: Self-supervised ViT training via self-distillation; produces patch features with strong spatial and semantic properties without text supervision; useful for dense prediction tasks.
- **VQ-VAE discrete tokens**: Encoder maps image patches to nearest codebook vectors (typically 8,192–16,384 entries); produces integer token sequences that unify with text vocabulary; used in DALL-E, Parti.
- **Mel spectrogram tokenization**: Raw audio → 80-channel mel spectrogram (25ms windows, 10ms hop) → treat as 2D image and apply ViT or CNN encoder; continuous representations.
- **Neural codec discrete tokens (EnCodec)**: Audio → encoder → residual vector quantization across 8 codebooks at 75 Hz → discrete codes; hierarchical: codebook 1 = coarse, codebook 8 = fine detail; 1 second ≈ 600 tokens across codebooks.
- **Token tax**: Each image consumes 256–576 tokens of the context window; video multiplies this by frame count; a 10-image prompt can consume 5,760 tokens before any text; this is the fundamental efficiency bottleneck.
- **Token merging/compression**: Reduce visual token count by merging similar adjacent tokens (ToMe), using a perceiver/Q-Former to compress N visual tokens to M << N query tokens, or adaptive resolution that allocates fewer tokens to simple image regions.
- **Early fusion (interleaved)**: All modality tokens in one sequence; single transformer processes everything; maximum cross-modal interaction; used by Gemini, Chameleon.
- **Late fusion**: Separate encoders per modality; combine at final layers via concatenation, pooling, or learned combination; simpler training but limited cross-modal reasoning.
- **Cross-attention fusion (Flamingo-style)**: Insert gated cross-attention layers into the LLM at selected intervals; visual features are keys/values, text tokens are queries; LLM weights can remain frozen.

### Key Facts
- The field is converging toward discrete tokenization across all modalities, though the question is still open.
- Token budget is a first-class design constraint in multimodal systems.
- Fusion strategy determines how deeply modalities can reason together.
- Continuous vs. discrete representations create different tradeoffs in training, generation, and information loss.


| Aspect | Continuous Tokens | Discrete Tokens |
| --- | --- | --- |
| Representation | Dense float vectors | Integer codebook indices |
| Examples | ViT features, DINO, mel spectrograms | VQ-VAE, EnCodec, SoundStream |
| Integration with LLM | Requires projection/adapter layer | Can share vocabulary directly |
| Information loss | Minimal (no quantization) | Quantization bottleneck |
| Generation | Requires separate decoder | Unified autoregressive generation |
| Training simplicity | Needs modality-specific losses | Standard cross-entropy on all tokens |


| Aspect | Early Fusion | Late Fusion | Cross-Attention |
| --- | --- | --- | --- |
| Token interaction | From layer 1 | Final layers only | At selected layers |
| Cross-modal depth | Maximum | Minimal | Moderate |
| Token cost | Full tax on all tokens | Separate budgets | Compressed queries |
| Training | End-to-end, expensive | Modular, cheaper | Partially frozen, moderate |
| Examples | Gemini, Chameleon | Simple baselines | Flamingo, LLaVA |

---

## 🔬 Deep Dive

### Technical Details
The token tax is the central systems problem. Every image, spectrogram, or video frame competes with text for the same context budget unless the architecture compresses or separates modalities. That is why token merging, Q-Former-style compression, and adaptive resolution matter so much in real systems.

The field is also split between a unified-token view and a modular-adapter view. Discrete tokens make it elegant to train a single autoregressive model across modalities, but quantization can lose information. Continuous features preserve more detail, but they usually require adapter layers or specialized decoders.

### Limitations
Early fusion gives the richest cross-modal interaction but is expensive in tokens and compute. Late fusion is cheaper but weaker at fine-grained reasoning. Cross-attention is a useful compromise, but it still relies on the quality of the external encoder and the bottleneck between modalities.

### Impact
These choices directly determine whether a model can answer image-grounded questions, reason across speech and text, or scale to long multimodal contexts without wasting most of its budget on visual tokens.

---

## 🏋️ Practice

### Warm-Up
1. How many tokens does a 224×224 image produce with 14×14 ViT patches?
2. What is the token tax in multimodal models?
3. What is the main difference between early fusion and late fusion?

### Core Problems
1. Why might a model use a Q-Former or token merging stage before passing image tokens to an LLM?
2. What is the tradeoff between continuous and discrete multimodal tokens?
3. Why does early fusion usually support deeper cross-modal reasoning?

### Challenge
Design a multimodal assistant for screenshots plus spoken notes. Choose tokenization methods, a fusion strategy, and one compression technique to control context cost.

---

## Supporting Chunks

### Supporting Chunks
- No supporting chunk notes are attached yet.

## References
- [[LLM/Sources/Sources Index]]
