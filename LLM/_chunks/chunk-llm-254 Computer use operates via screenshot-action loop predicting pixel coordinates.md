---
tags: [llm, chunk]
id: chunk-llm-254
source: "[[raw-llm-068]]"
supports: ["[[Computer Use and GUI Agents]]"]
confidence: verified
up: "[[LLM]]"
---

# Computer Use Operates via Screenshot-Action Loop at Pixel Coordinates

## Context

Computer use agents extend LLM capabilities from text and code into the visual domain of graphical interfaces, interacting with any software the way a human would.

## Claim

Computer use agents operate in a screenshot-action loop where the model perceives screen state via screenshots and outputs mouse clicks at pixel coordinates and keyboard inputs to interact with any GUI.

## Why It Matters

This approach is universal — any software with a graphical interface becomes automatable without requiring an API, enabling interaction with legacy systems, web applications, and desktop software.

## QnA Seeds

- Q: How does the computer use loop work? → A: The model receives a screenshot, identifies UI elements, predicts coordinates for actions (click, type, scroll), executes them, then receives the next screenshot.
- Q: Why use pixel coordinates instead of DOM elements? → A: Pixel coordinates work across any GUI (desktop, web, mobile) without requiring access to internal application structure.
