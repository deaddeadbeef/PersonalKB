---
tags: [llm, prompting]
up: "[[2020–2021 — The Scaling Era Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Few-Shot Prompting

> **Few-shot prompting teaches a model a task by showing a handful of examples in the prompt instead of updating its weights.**

## 🎯 Intuition
**The Core Idea:** A language model can infer a task pattern from a few in-prompt demonstrations and apply that pattern to a new input at inference time.

**Analogy:** It is like showing a chef three dishes and asking for a fourth in the same style.

**Why It Matters:** Few-shot prompting, popularized by GPT-3, showed that sufficiently large language models can adapt through context alone. It created a practical middle ground between zero-shot prompting and full fine-tuning, making rapid prototyping much easier. At the same time, its brittleness revealed how much performance can depend on example choice, ordering, and formatting.

---

## ⚙️ Core Mechanics
### How It Works
- Few-shot prompting, popularized by GPT-3 (Brown et al., 2020), enables language models to perform tasks by providing a small number of input-output examples directly in the prompt—no parameter updates required.
- The model observes the pattern in the examples and applies it to new inputs, demonstrating in-context learning capabilities that scale with model size.
- The technique relies on carefully chosen demonstrations that illustrate the task format, desired reasoning style, and output structure.
- Performance depends heavily on example selection, ordering, and formatting choices, making prompt engineering both powerful and brittle.
- Few-shot prompting bridges zero-shot (no examples) and full fine-tuning, offering a practical middle ground where task adaptation happens at inference time through context rather than through gradient descent.

### Key Specifications

| Comparison | Few-Shot Prompting | Alternative |
|------------|-------------------|-------------|
| **vs Zero-shot** | Provides demonstrations in context | Relies only on task instructions |
| **vs Fine-tuning** | No weight updates, inference-time only | Updates model parameters with gradients |
| **vs Retrieval-augmented** | Examples are static in prompt | Dynamically retrieves relevant examples |
| **vs Meta-learning** | No explicit training on task distribution | Trained explicitly to adapt quickly |
| **Random vs kNN selection** | Fast but suboptimal | Better performance, requires embedding computation |
| **Fixed vs dynamic ordering** | Same order for all inputs | Optimizes order per query |

### Key Facts
- **Example selection strategies**: random sampling, k-nearest neighbors by semantic similarity, diversity-based sampling, uncertainty-based selection.
- **Example ordering effects**: performance varies significantly based on demonstration order; recency bias and primacy effects.
- **Zero/one/few-shot curves**: performance typically improves from zero to few examples, plateaus around 5-10 demonstrations.
- **Format sensitivity**: whitespace, delimiters, label tokens, and template structure dramatically impact results.
- **Scaling behavior**: few-shot capabilities emerge strongly in models beyond ~10B parameters.

---

## 🔬 Deep Dive
### Technical Details
Few-shot prompting works because the model can use the prompt itself as a temporary adaptation interface. Instead of changing parameters through gradient descent, it conditions on a sequence of demonstrations and infers the latent task from them. The examples communicate the task format, desired reasoning style, and output structure all at once. This is why the technique is closely tied to in-context learning and why its effectiveness tends to improve with model scale.

Implementation details matter a great deal:
- Example selection can be random, semantic-similarity-based through k-nearest neighbors, diversity-based, or uncertainty-based.
- Example ordering can significantly change performance because models show both recency bias and primacy effects.
- Prompt formatting choices such as delimiters, whitespace, labels, and template structure can dramatically alter outcomes.
- Failure modes include misleading examples, injected biases, and prompts that encourage shortcut exploitation instead of genuine task understanding.

Few-shot prompting fundamentally changed how we interact with large language models by enabling task adaptation without expensive fine-tuning infrastructure. It demonstrated that sufficiently large models contain meta-learning capabilities that can be activated through context alone. This made LLMs practical for rapid prototyping and one-off tasks where collecting training data would be prohibitively expensive.

### Limitations and Criticisms
- Performance is brittle because example selection, order, and formatting can all change results substantially.
- A few bad demonstrations can mislead the model, inject bias, or trigger spurious shortcuts.
- Few-shot prompting often plateaus after a modest number of examples and may still underperform instruction tuning or fine-tuning.

### Impact and Legacy
Few-shot prompting was one of the defining ideas of the scaling era. It helped establish prompt engineering as a serious practice, provided early evidence of in-context meta-learning, and influenced later work on chain-of-thought prompting, example retrieval for ICL, prompt calibration, and instruction tuning.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why is few-shot prompting considered different from fine-tuning even though both adapt a model to a task?
2. Why can changing the order of demonstrations alter a model's output?
3. What does it mean to say that few-shot prompting adapts the model "through context"?

### Core Problems
1. Compare random example selection with k-nearest-neighbor selection for few-shot prompting. When might the extra embedding computation be worth it?
2. A prompt works well for sentiment classification with one delimiter format but fails when the formatting is slightly changed. How would you analyze this failure?

### Challenge
1. Design a few-shot prompting system for a high-stakes task and explain how you would choose, order, and validate demonstrations to minimize brittleness and bias.

---

*See also:* [[Language Model Fundamentals]] — few-shot ability emerges from language model pretraining; [[Decoder-Only Models]] — few-shot prompting works best with large decoder models; [[Chain-of-Thought Prompting]] — extending few-shot with explicit reasoning traces; [[Instruction Tuning]] — instruction-tuned models often outperform few-shot prompting; [[Function Calling]] — structured prompting evolved from few-shot patterns

## Supporting Chunks / References
- [[In-Context Learning Mechanisms]]
- [[Chain-of-Thought Prompting]]
- Example Selection for ICL
- Prompt Sensitivity and Calibration
- [[Scaling Laws|ICL Scaling Laws]]

→ [[LLM/Sources/Sources Index|LLM Sources Index]]
- Brown et al. (2020) - "Language Models are Few-Shot Learners" (GPT-3)
- Liu et al. (2021) - "What Makes Good In-Context Examples for GPT-3?"
- Lu et al. (2022) - "Fantastically Ordered Prompts"
- Min et al. (2022) - "Rethinking the Role of Demonstrations"

## References
- [[LLM/Sources/Sources Index|LLM Sources Index]]
