---
tags: [llm, agents]
up: "[[2023 — Open Models and Agents Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---

# Function Calling
> **One-line summary:** Function calling lets an LLM request structured tool use instead of only generating free-form text.

---

## 🎯 Intuition

### Core Idea
Function calling is the mechanism by which LLMs invoke external tools through structured output. Instead of generating free-form text, the model outputs a JSON object specifying a function name and its arguments, which a runtime then executes and returns results to the model. This is the foundational primitive that turns a language model into an agent.

The key insight behind function calling is that LLMs can be trained—or prompted—to produce structured JSON conforming to a predefined schema rather than natural language.

### Analogy
Function calling is like a receptionist who takes your request and fills out the right form for the right department.

### Why It Matters
Function calling is the bridge between language understanding and real-world action. Without it, an LLM is limited to generating text. With it, the model can query databases, call APIs, manipulate files, run code, and interact with any system that exposes a programmatic interface. Every major agent framework—LangChain, AutoGen, CrewAI, OpenAI Assistants—is built on top of function calling as the core interaction primitive.

---

## ⚙️ Core Mechanics

### How It Works
OpenAI introduced this formally in June 2023 with their function calling API: you supply a list of tool definitions (each with a name, description, and JSON Schema for parameters), and the model decides when and how to call them. Anthropic's tool use follows a similar pattern, embedding tool definitions in the system prompt and receiving structured `tool_use` content blocks in the response.

The model does not execute anything itself. It produces a *declaration of intent*—"I want to call `get_weather` with `{"city": "London"}`"—and the orchestrating code is responsible for actual execution, error handling, and feeding results back. This separation of declaration from execution is crucial for safety and flexibility. The model reasons about *what* to do; the runtime decides *whether and how* to do it.

Parallel function calling extends this by allowing the model to request multiple tool invocations in a single turn. For example, when asked to compare weather in three cities, the model can emit three `get_weather` calls simultaneously rather than sequentially. This reduces latency and round-trips. OpenAI supports this natively; other providers handle it through batched tool-use blocks.

### Key Specifications
- **Tool definitions**: Each tool is described with a name, natural-language description, and a JSON Schema specifying required/optional parameters, types, and enums.
- **Model selection**: The model decides whether to call a tool (vs. respond directly), which tool to call, and what arguments to pass—all based on the conversation context and tool descriptions.
- **Execution loop**: User message → model response with tool call → runtime executes → result injected as tool message → model generates final response (or calls another tool).
- **Parallel calls**: Multiple independent tool invocations in a single model turn, reducing round-trips for independent operations.
- **Forced vs. auto**: APIs typically support `tool_choice: "auto"` (model decides), `tool_choice: "required"` (must call something), or `tool_choice: {"name": "specific_tool"}` (force a specific tool).
- **Training**: Models are fine-tuned on datasets of (prompt, tool_call, result, response) sequences to learn when and how to invoke tools reliably.
- **Error handling**: Common patterns include returning error messages as tool results so the model can retry with corrected arguments, and implementing retry limits to prevent infinite loops.
- **Schema validation**: Runtime should validate model-generated arguments against the JSON Schema before execution to catch hallucinated or malformed parameters.

### Key Facts
- OpenAI and Anthropic expose similar tool-use patterns with different response formats.
- The runtime—not the model—does the actual execution.
- Tool descriptions and schemas strongly influence agent reliability.
- Missing validation or poor error handling is a common source of silent failure.


| Aspect | OpenAI Function Calling | Anthropic Tool Use |
| --- | --- | --- |
| Definition location | `tools` parameter in API request | `tools` parameter in API request |
| Response format | `tool_calls` array in message | `tool_use` content blocks |
| Parallel calls | Native support | Supported via multiple content blocks |
| Forcing tool use | `tool_choice` parameter | `tool_choice` parameter |
| Streaming | Delta-based tool call streaming | Event-based streaming with `content_block_start` |

---

## 🔬 Deep Dive

### Technical Details
Function calling works because the model is constrained to emit structure rather than open-ended prose. That structure becomes a contract between model and runtime. Good tool schemas reduce ambiguity. Good orchestration loops keep the model grounded by feeding back tool results in a consistent format.

Clear tool design matters more than many people expect. The quality of function calling directly determines agent reliability. Poorly described tools lead to incorrect invocations. Missing error handling leads to silent failures. The design of your tool definitions—clear names, precise descriptions, constrained schemas—is arguably more important than the prompt itself when building agentic systems.

### Limitations
The model can still hallucinate arguments, pick the wrong tool, or create malformed requests. Parallel calls reduce latency but add orchestration complexity. Poorly scoped tool permissions can also create safety problems even when the schema itself looks correct.

### Impact
Function calling is what makes modern agents practical. It turns LLMs from text generators into systems that can interact with APIs, databases, and external software in a controlled loop.

---

## 🏋️ Practice

### Warm-Up
1. What is the difference between a tool call and actual tool execution?
2. Why is JSON Schema useful in function calling?
3. When are parallel function calls helpful?

### Core Problems
1. A model keeps calling the wrong tool. What should you improve first: the tool description, the schema, or the final prompt?
2. Why should runtime code validate arguments before execution?
3. Explain `tool_choice: "auto"` vs. forcing a specific tool.

### Challenge
Design a small tool interface for a weather assistant with two tools. Define the tool names, arguments, and one safety check your runtime must perform before execution.

---

## References
### Supporting Chunks
- Evidence chunks and raw source notes are reachable through [[LLM/LLM Corpus Index|LLM Corpus Index]] and [[LLM/Sources/Sources Index|LLM Sources Index]].

### See Also
- [[LLM/Prompting and In-Context Learning/Structured Output and Constrained Generation|Structured Output]] — function calls are a form of structured generation
- [[LLM/Prompting and In-Context Learning/Tool-Augmented Prompting|Tool-Augmented Prompting]] — prompting techniques for tool use

### References
- [[LLM/Sources/Sources Index]]
