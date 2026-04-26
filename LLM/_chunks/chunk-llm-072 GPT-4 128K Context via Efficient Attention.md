---
tags: [chunk, llm]
id: "chunk-llm-072"
source: "[[LLM/_raw/raw-llm-018 GPT-4 Technical Report]]"
source_loc: "Key Takeaways"
topic: "GPT-4 Turbo long context"
claim: "GPT-4's 128K context window (Turbo variant) was enabled by efficient attention techniques and position encoding advances."
confidence: "verified"
supports: ["[[LLM/Architecture Variants/Efficient Attention and Long-Context Variants]]"]
up: "[[LLM/LLM]]"
---

# GPT-4 128K Context via Efficient Attention

## Context
The original GPT-4 launched with an 8K context window, with a 32K variant available shortly after. GPT-4 Turbo later expanded this to 128K tokens — roughly 300 pages of text. While OpenAI disclosed no details about how this was achieved, the expansion was almost certainly enabled by a combination of FlashAttention (reducing memory from O(n²) to O(n)), efficient position encoding (likely RoPE with scaling techniques), and potentially sliding window or sparse attention patterns for very long contexts.

A 128K context window transformed the model's practical utility: entire codebases, legal documents, research papers, or book-length texts could be processed in a single prompt. However, context window size alone doesn't guarantee effective use of all context — studies showed that GPT-4 Turbo's performance degraded for information placed in the middle of very long contexts (the "lost in the middle" phenomenon), suggesting that having a large window is necessary but not sufficient for reliable long-context reasoning.

## Why It Matters
GPT-4 Turbo's 128K context established the expectation that frontier models should support very long contexts. It kicked off a context-length arms race: Claude expanded to 100K then 200K, Gemini to 1M, and open models like Llama 3 to 128K. The practical ability to process long documents in a single pass opened entirely new use cases that were impossible with earlier 2K-4K context models.

## QnA Seeds
- Q: What techniques likely enabled GPT-4 Turbo's 128K context window?
  A: While OpenAI disclosed no details, FlashAttention (O(n) memory instead of O(n²)), efficient position encoding (likely RoPE with frequency scaling), and possibly sparse or sliding window attention patterns were almost certainly involved. These are the standard techniques used by all long-context models.
- Q: Does a 128K context window mean the model effectively uses all 128K tokens?
  A: Not perfectly. Studies revealed a "lost in the middle" phenomenon where GPT-4 Turbo's retrieval accuracy degraded for information placed in the middle of very long contexts, while information near the beginning and end was recalled well. Large context windows are necessary but not sufficient for reliable long-context reasoning.
