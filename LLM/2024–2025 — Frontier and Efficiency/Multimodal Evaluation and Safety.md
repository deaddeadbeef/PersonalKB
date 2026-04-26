---
tags: [llm, multimodal]
up: "[[2024–2025 — Frontier and Efficiency Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Multimodal Evaluation and Safety

> **One-line summary**: Multimodal evaluation asks whether a model truly reasons across images and text, while multimodal safety asks whether those same cross-modal abilities create new failure and attack surfaces.

---

## 🎯 Intuition

### Core Idea
Evaluating multimodal models means testing genuine cross-modal reasoning, not just text skills pasted onto image inputs. A strong model should answer questions about what is actually in an image, read text inside visuals, and reason about layout, charts, and documents without leaning on language-only shortcuts.

### Analogy
Multimodal evaluation is like **testing a translator on reading, listening, AND speaking**. It is not enough to be good at one channel; the system has to combine multiple channels correctly under pressure.

### Why It Matters
Safety concerns multiply once models can perceive and generate across modalities. Visual prompt injection, cross-modal hallucination, deepfakes, and biased visual descriptions create risks with no direct text-only equivalent. If the benchmarks are weak, models learn shortcuts instead of real grounding, and deployment decisions become much riskier.

---

## ⚙️ Core Mechanics

### How It Works
The evaluation landscape is anchored by benchmark families that test different slices of multimodal ability. VQAv2 targets general visual reasoning over natural images. GQA stresses compositional spatial and relational reasoning via scene graphs. TextVQA and OCR-VQA test whether the model can read text inside natural images. DocVQA shifts to invoices, forms, and reports, where layout matters as much as text. ChartQA adds chart parsing and numerical reasoning.

### Key Specs
- **VQAv2**: 1.1M questions on 200K COCO images; balanced pairs reduce language-only shortcuts; uses VQA accuracy with human-agreement normalization.
- **GQA**: 22M compositional questions generated from scene graphs; tests spatial, comparative, and logical reasoning; includes consistency and plausibility metrics.
- **TextVQA**: 45K questions that require OCR on signs, book covers, and screens.
- **DocVQA**: 50K questions on 12K document images; focuses on layout-aware extraction; uses **ANLS** (Average Normalized Levenshtein Similarity).
- **ChartQA**: tests chart and graph understanding through visual parsing plus numerical reasoning.
- **POPE** and **CHAIR** specifically measure cross-modal hallucination.

### Key Facts
- Cross-modal hallucination is the signature multimodal failure mode: models may invent objects, text, or spatial relations that are visually false.
- Even state-of-the-art systems still hallucinate objects in roughly **10–30%** of responses.
- Visual prompt injection can hide instructions inside images through overlaid text, tiny text, steganographic encoding, or adversarial patches.
- Multimodal safety also includes deepfake misuse, privacy leakage, bias in visual descriptions, and NSFW handling.


| Benchmark | Domain | Key Capability Tested | Metric |
| --- | --- | --- | --- |
| VQAv2 | Natural images | General visual reasoning | VQA accuracy |
| GQA | Scene graphs | Compositional reasoning | Accuracy, consistency |
| TextVQA | Text in images | OCR + reasoning | VQA accuracy |
| DocVQA | Documents | Layout-aware extraction | ANLS |
| ChartQA | Charts/graphs | Visual + numerical reasoning | Accuracy |
| POPE | Object probing | Hallucination detection | F1, accuracy |
| MMBench | Comprehensive | Multi-ability evaluation | Accuracy per skill |


| Safety Risk | Modality | Attack Vector | Mitigation |
| --- | --- | --- | --- |
| Visual prompt injection | Image | Embedded adversarial text | Instruction hierarchy, input filtering |
| Cross-modal hallucination | Image + text | Over-reliance on language priors | Grounding training, RLHF |
| Deepfake generation | Image/video | Model misuse for manipulation | Watermarking, detection models |
| Privacy extraction | Image | Facial recognition, location inference | Output filtering, consent policies |
| Description bias | Image + text | Stereotyped visual reasoning | Debiasing training data, evaluation |

---

## 🔬 Deep Dive

### Technical Details
Cross-modal hallucination is different from text-only hallucination because the ground truth is often visually verifiable. A model may say a cat is on the left when it is on the right, or invent text that does not appear in a document, because it over-trusts language priors instead of attending to visual evidence. POPE uses polling-style object probes, while CHAIR compares mentioned objects against image ground truth.

Visual prompt injection is a novel multimodal attack surface. If a model reads all text embedded in an image, it may obey hidden instructions that conflict with the user prompt, such as trying to reveal a system prompt or manipulate a GUI agent. This is especially dangerous when multimodal models are attached to browsers, UI agents, or automation systems.

### Limitations
- Most current benchmarks are still single-image benchmarks; multi-image and video evaluation are less mature.
- Many benchmarks can still be partially solved by language priors rather than true visual reasoning.
- Static benchmarks saturate as models improve, so harder tests must be developed continuously.
- Existing metrics often correlate poorly with human judgments of response quality.

### Impact
Text benchmarks like MMLU and HumanEval are comparatively standardized and trusted, but multimodal benchmarks remain newer and harder to interpret. That evaluation gap means weaker confidence in deployment readiness just as the safety surface becomes larger across image, audio, and video inputs.

---

## 🏋️ Practice

### Warm-Up
- What does it mean for a benchmark to test **cross-modal reasoning** rather than unimodal skill?
- Why is TextVQA harder than ordinary object recognition?

### Core Problems
- Explain the difference between **DocVQA** and **ChartQA** in one or two sentences.
- Why is cross-modal hallucination easier to verify than many text-only hallucinations?
- Name two defenses against visual prompt injection.

### Challenge
- Suppose a multimodal agent reads screenshots and takes actions. Explain why visual prompt injection becomes a security issue, not just an accuracy issue.
- Compare why benchmark saturation is a bigger problem for multimodal evaluation than it first appears.

## Supporting Chunks
*(To be populated as chunks are created)*

## References
- [[LLM/Sources/Sources Index]]
