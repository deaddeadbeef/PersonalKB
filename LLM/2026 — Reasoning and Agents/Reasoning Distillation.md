---
tags: [llm, reasoning-agents]
up: "[[2026 — Reasoning and Agents Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Reasoning Distillation

> **One-line summary** Training smaller models on the reasoning traces of larger models, enabling compact architectures to exhibit reasoning capabilities that were previously exclusive to frontier-scale systems.

## 🎯 Intuition

### Core Idea

Reasoning distillation teaches a smaller model not just the answer, but the path a stronger model took to get there. That means the student can learn reasoning behaviour that would otherwise seem reserved for much larger systems.

### Analogy

Reasoning distillation is like a student learning by studying the teacher's worked examples instead of only memorising final answers.

### Why It Matters

It makes advanced reasoning cheaper, faster, and more deployable. Once a frontier model learns how to "think," that capability can often be packaged into smaller models for real-world use.

---

## ⚙️ Core Mechanics

### How It Works

Classical knowledge distillation transfers a large model's output distribution to a smaller student model. Reasoning distillation extends this by training on the **reasoning process** itself.

The standard recipe is:

1. generate a dataset of **(problem, reasoning trace, answer)** triples from a teacher model
2. fine-tune the student model on those triples
3. train the student to reproduce similar reasoning patterns

DeepSeek's R1 distillation is the standout example. Starting from R1, DeepSeek produced models from **70B down to 1.5B** parameters. The **14B distilled model outperformed o1-mini on several benchmarks**, and the **7B distilled model outperformed Llama 3.1 70B on math reasoning**.

### Key Specs

- Representative compression path: **70B → 32B → 14B → 7B → 1.5B**
- Training target: **problem + reasoning trace + answer**
- Deployment effect: **10–100× cheaper inference** than the teacher

### Key Facts

- **DeepSeek R1 distillation**: 70B → 32B → 14B → 7B → 1.5B variants
- **14B distilled model** outperformed o1-mini on several benchmarks
- **7B distilled model** outperformed Llama 3.1 70B on math reasoning
- **Technique**: fine-tune on (problem, reasoning trace, answer) triples
- **o1-mini**: OpenAI's compact reasoning model (likely internal distillation)
- **Key insight**: reasoning transfers as a generation *style*, not just as knowledge
- **Cost reduction**: 10–100× cheaper inference than the teacher model

| Aspect | Knowledge Distillation | Reasoning Distillation |
|--------|----------------------|----------------------|
| What transfers | Output probabilities | Step-by-step reasoning |
| Training data | (input, soft label) | (input, reasoning trace, answer) |
| Student capability | Mimics teacher's answers | Mimics teacher's thinking |
| Effectiveness | Moderate compression | Surprisingly effective compression |
| Typical use | Model compression | Enabling reasoning in small models |

---

## 🔬 Deep Dive

### Technical Details

The surprising result is that reasoning appears to transfer as a learnable **style of generation**, not just as stored knowledge. OpenAI's o1-mini can be interpreted as a similar pattern internally: a smaller, faster reasoning model retaining much of o1's capability at lower cost and latency.

### Limitations

- Distilled reasoning may not preserve the full breadth of teacher capability
- Benchmark gains can vary by domain
- The student still depends on the teacher's generated traces and biases

### Impact

Reasoning distillation democratizes advanced reasoning by moving it from expensive frontier models into smaller deployments suitable for edge settings, real-time use, and cost-sensitive applications.

### Related Notes

- [[DeepSeek R1 and Open Reasoning]] — the primary source of distilled reasoning models
- [[Reasoning Models and Test-Time Compute]] — the capability being distilled
- [[Distillation and Model Compression]] — classical distillation techniques
- [[Scaling Laws|Scaling Laws and Chinchilla]] — how distillation interacts with scaling

---

## 🏋️ Practice

### Warm-Up

1. What is the difference between knowledge distillation and reasoning distillation?
2. Why are reasoning traces more informative than final answers alone?

### Core Problems

1. Explain why reasoning can transfer as a style rather than just as knowledge.
2. Describe the DeepSeek R1 distillation pipeline and why its 14B and 7B results were notable.
3. Compare the training data used in classical distillation versus reasoning distillation.

### Challenge

Defend or reject the claim that reasoning distillation matters more for deployment economics than for research progress.

---

## Supporting Chunks

- [[LLM/_chunks/chunk-llm-258 Reasoning distillation trains small models on teacher reasoning traces|chunk-llm-258 Reasoning distillation trains small models on chain-of-thought traces transferring how to think not just what to know]]
- [[LLM/_chunks/chunk-llm-259 DeepSeek 7B distilled model outperforms Llama 3.1 70B on math reasoning|chunk-llm-259 DeepSeek distilled 32B model outperforms 70B base models demonstrating reasoning compresses efficiently]]

## References

→ [[Sources Index]]
