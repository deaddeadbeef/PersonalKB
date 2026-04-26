---
tags: [chunk, llm]
id: "chunk-llm-109"
source: "[[LLM/_raw/raw-llm-028 Whisper Robust Speech Recognition]]"
source_loc: "What Is This, Key Takeaways 1-2"
topic: "Whisper encoder-decoder on 680K hours"
claim: "Whisper achieves robust speech recognition by training an encoder-decoder transformer on 680K hours of weakly supervised multilingual audio."
confidence: "verified"
supports: ["[[LLM/Multimodal/Speech-Language Models]]"]
up: "[[LLM/LLM]]"
---

# Whisper Trains on 680K Hours of Weakly Supervised Audio

## Context
Whisper is an encoder-decoder Transformer model trained on approximately 680,000 hours of weakly supervised multilingual audio data collected from the internet. "Weakly supervised" means the audio-transcript pairs are not human-verified — they come from sources like YouTube subtitles, podcast transcripts, and web audio with associated text. This is orders of magnitude more data than prior supervised ASR datasets (LibriSpeech has ~960 hours).

The encoder processes log-mel spectrogram features from 30-second audio segments, and the decoder generates text tokens autoregressively. The model uses a multitask format where special tokens indicate the task (transcription, translation), language, and whether timestamps should be included. This unified architecture handles all speech tasks in a single model without task-specific heads or modules.

## Why It Matters
Whisper proved that the "scale weakly labeled data" paradigm that succeeded for text (GPT) and images (CLIP) also works for speech. By training on 680K hours of diverse, imperfect data instead of small curated datasets, Whisper achieved unprecedented robustness across accents, noise conditions, and domains — making production-quality speech recognition accessible through a single open-source model.

## QnA Seeds
- Q: How much training data does Whisper use and what makes it "weakly supervised"?
  A: 680,000 hours of multilingual audio from the internet, where transcripts come from sources like YouTube subtitles rather than human verification — orders of magnitude more than curated datasets like LibriSpeech (~960 hours).
- Q: What is Whisper's model architecture?
  A: An encoder-decoder Transformer where the encoder processes log-mel spectrograms from 30-second audio segments and the decoder generates text tokens autoregressively using special tokens for task, language, and timestamp control.
