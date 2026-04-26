---
tags: [chunk, llm]
id: "chunk-llm-009"
source: "[[LLM/_raw/raw-llm-003 BERT Pre-training of Deep Bidirectional Transformers]]"
source_loc: "Section 3.1"
topic: "masked language modeling"
claim: "MLM masks 15% of tokens (80% [MASK], 10% random, 10% unchanged) and predicts them from bidirectional context"
confidence: "verified"
supports: ["[[LLM/Architecture Variants/Encoder-Only Models]]"]
up: "[[LLM/LLM]]"
---

# Masked Language Modeling Strategy

## Context

BERT's core pre-training objective is Masked Language Modeling (MLM): 15% of input tokens are selected for prediction, but not all are replaced with [MASK]. Of the selected tokens, 80% are replaced with [MASK], 10% are replaced with a random token, and 10% are left unchanged. The model must predict the original token at each selected position using bidirectional context from all surrounding tokens.

This mixed masking strategy addresses a practical concern: during fine-tuning and inference, the model never sees [MASK] tokens, creating a pre-training/fine-tuning mismatch. By sometimes keeping the original token or using a random replacement, the model learns to produce useful representations for all positions, not just masked ones. The 15% masking rate was chosen as a balance between having enough prediction signal per batch and maintaining enough context for accurate predictions.

## Why It Matters

MLM was a breakthrough because it enabled bidirectional pre-training — something impossible with standard autoregressive language modeling, which can only condition on left context. The specific 80/10/10 masking strategy became an important implementation detail that was widely adopted and studied, influencing subsequent pre-training objectives like replaced token detection in ELECTRA.

## QnA Seeds
- Q: Why doesn't BERT simply replace all selected tokens with [MASK]?
  A: If all selected tokens were masked, the model would only learn to produce good representations when it sees [MASK] tokens — but these never appear during fine-tuning or inference. The 10% random and 10% unchanged replacements force the model to maintain good representations at every position, since it can't know which tokens were selected for prediction.
- Q: Why was 15% chosen as the masking rate rather than a higher percentage?
  A: The masking rate balances two competing needs: higher masking provides more training signal per sequence (more predictions per forward pass), but too much masking removes too much context, making predictions unreliable. At 15%, the model sees enough context to make meaningful predictions while still getting sufficient gradient signal. Later work (SpanBERT) explored masking contiguous spans instead of random tokens.
