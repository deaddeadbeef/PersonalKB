---
id: chunk-csos-100
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 5 — I/O Systems Architecture"
topic: "io"
claim: "The interrupt handling model splits work into a top-half (runs in interrupt context with interrupts disabled, must be fast) and a bottom-half (deferred work with interrupts enabled) to prevent long handlers from causing unacceptable latency"
confidence: verified
supports:
  - "[[Interrupts and DMA]]"
  - "[[IO Software Layers]]"
tags:
  - csos
  - csos/io
  - chunk
up: "[[CS Operating Systems]]"
---
# IO — Interrupt handling splits into fast top-half and deferred bottom-half

## Context

When a device raises an interrupt, the CPU must respond quickly — but many interrupt-triggered tasks (e.g., processing a received network packet up the protocol stack) require substantial work. The split model solves this tension: the top-half runs with interrupts disabled, does the minimum necessary work (acknowledge hardware, copy data from device registers, schedule bottom-half), and returns. The bottom-half runs later with interrupts enabled. Linux implements bottom-halves via three mechanisms: softirqs (statically allocated, per-CPU, used for high-frequency events like networking), tasklets (dynamically allocated, built on softirqs), and workqueues (run in kernel thread context, can sleep).

## Why It Matters

This split is a fundamental design pattern for any system handling asynchronous events under latency constraints. Without it, a long network packet handler would block all other interrupts, causing missed timer ticks, dropped keystrokes, and degraded real-time responsiveness.

## QnA Seeds

- Q: Why must the top-half interrupt handler run with interrupts disabled?
- Q: What are the three Linux bottom-half mechanisms and when is each used?
- Q: What happens if an interrupt handler takes too long without the top/bottom-half split?
