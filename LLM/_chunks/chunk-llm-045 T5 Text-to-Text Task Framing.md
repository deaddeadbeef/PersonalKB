---
tags: [chunk, llm]
id: "chunk-llm-045"
source: "[[LLM/_raw/raw-llm-012 T5 Unified Text-to-Text Transformer]]"
source_loc: "Key Takeaways 1"
topic: "T5 text-to-text framing"
claim: "T5 frames every NLP task as text-to-text: input text → output text, using task-specific prefixes."
confidence: "verified"
supports: ["[[LLM/Architecture Variants/Encoder-Decoder Models]]"]
up: "[[LLM/LLM]]"
---

# T5 Text-to-Text Task Framing

## Context
T5 introduced a unified paradigm where every NLP task is cast as converting an input text string to an output text string. Classification tasks produce a class label as text ("positive", "entailment"), translation prepends "translate English to German:", summarization uses "summarize:", and question answering concatenates the question with the context. The key mechanism is a task-specific prefix that instructs the model on what operation to perform.

This framing is deceptively powerful: by representing all tasks in the same format, T5 can use the same model architecture, loss function (cross-entropy on output tokens), and training procedure for every task. The only thing that changes between tasks is the prefix string and the training data. This eliminated the need for task-specific output heads or architectures that plagued earlier transfer learning approaches.

## Why It Matters
The text-to-text paradigm was a conceptual precursor to the prompt-based approach that dominates modern LLMs. It demonstrated that a single model with a single output format could handle the full range of NLP tasks, foreshadowing the generality of instruction-tuned models like ChatGPT that also convert natural language instructions into text responses.

## QnA Seeds
- Q: How does T5's text-to-text framing handle classification tasks?
  A: Classification tasks are converted to text generation: the input includes a task prefix (e.g., "classify sentiment:") followed by the text, and the model generates the class label as a text string (e.g., "positive"). The same cross-entropy loss over output tokens is used for all tasks.
- Q: What advantage does the text-to-text paradigm have over task-specific output heads?
  A: It allows one architecture, one loss function, and one training procedure for all tasks. There's no need to design or swap output layers for different tasks — the model simply generates different text strings, making multi-task training and transfer straightforward.
