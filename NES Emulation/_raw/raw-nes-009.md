---
tags: [raw, nes-emulation, achievement]
source: "OxideNES main.rs achievement system"
---

# Raw NES 009 — Achievement System Architecture

OxideNES includes a RetroAchievements-inspired achievement system that defines achievements based on memory conditions. Achievements are defined in JSON files alongside ROMs and evaluated each frame by the emulator.

## Achievement Definition Format

Each achievement is a JSON object with fields:
- id: Unique identifier string
- 	itle: Display name
- description: How to unlock
- conditions: Array of condition groups (AND logic within group, OR between groups)
- icon: Optional emoji or icon path for display

Each condition specifies: ddress (CPU memory location to monitor), comparison (eq, neq, gt, lt, gte, lte), alue (target value), and optional 	ype (current value, previous value, delta). This allows conditions like "HP at  equals 0" (player died) or "level counter at  increased by 1" (level completed).

## Evaluation Engine

The achievement evaluator runs once per frame after the CPU executes. It reads the specified memory addresses through the bus (same path as CPU reads, ensuring mapper-correct values). Conditions are evaluated as boolean expressions: all conditions in a group must be true (AND), and any group being true triggers the achievement (OR of ANDs). This is equivalent to disjunctive normal form (DNF), which can express any boolean function.

## State Tracking

Achievements track three value types per condition: current value (this frame), previous value (last frame), and delta (current minus previous). Delta conditions enable detecting changes: "score increased" rather than "score equals X". The evaluator maintains a per-achievement state machine: inactive → active (conditions being met) → triggered (all conditions met, achievement awarded). Once triggered, achievements don't re-fire.

## Persistence

Triggered achievements are saved to a JSON file in the config directory (~/.nes-emulator/achievements/<rom-crc32>.json). On ROM load, previously triggered achievements are loaded and excluded from evaluation. This provides cross-session persistence. Save states do NOT affect achievement state — reloading a save state cannot re-trigger an already-earned achievement.

## Display

When an achievement triggers, a notification overlay appears on-screen: a toast message showing the title and description that fades out over 3 seconds. The notification is rendered as a semi-transparent rectangle with text, composited on top of the CRT pipeline output. Active achievement progress (e.g., "3/5 items collected") is not currently displayed — only the trigger notification.

## Anti-Cheat Considerations

The achievement system doesn't implement anti-cheat measures like hashing game state or disabling achievements when Lua scripts are active. This is a known limitation. For community-verified achievements, integration with the official RetroAchievements service could be added in the future, which includes server-side validation.
