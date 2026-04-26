---
tags: [nes, wiki]
up: "[[Extended Features Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Achievement System

> **OxideNES evaluates RetroAchievements-compatible conditions against CPU RAM every frame to unlock achievements for a specific ROM.**

## 🎯 Intuition
**The Core Idea:** This is a frame-by-frame RAM inspector evaluating RetroAchievements-compatible conditions.
**Analogy:** A sports referee watching instant replay every frame.
**Why It Matters:** It adds replayability to classic games and stays compatible with the RetroAchievements ecosystem.

---

## ⚙️ Core Mechanics
### How It Works
OxideNES supports a local achievement system using a RetroAchievements-compatible condition syntax. Achievements are defined per-ROM and evaluated every frame against CPU RAM state.

Achievement JSON files stored at `~/.oxidenes/achievements/{rom_md5}.json`:

```json
{
    "game_title": "Super Mario Bros.",
    "achievements": [
        {
            "id": 1,
            "title": "First Steps",
            "description": "Complete World 1-1",
            "points": 10,
            "conditions": "0xH0075>0_S_0xH0760=1"
        }
    ]
}
```

Each frame, the engine:
1. Snapshots current CPU RAM
2. Evaluates all locked achievement conditions against current and previous RAM
3. Unlocks achievements whose conditions are newly satisfied
4. Displays notification popup with title and point value
5. Persists unlock state to disk

### Key Specifications

| Expression | Meaning |
|-----------|---------|
| `0xHADDR=VALUE` | Byte at address equals value |
| `0xHADDR>VALUE` | Byte greater than value |
| `0xHADDR<VALUE` | Byte less than value |
| `d0xHADDR!=0xH` | Value changed from previous frame (delta) |
| `_S_` | AND operator (all conditions must be true) |

### Key Facts
- Achievements are defined per-ROM.
- Definitions are stored at `~/.oxidenes/achievements/{rom_md5}.json`.
- Conditions are evaluated every frame against CPU RAM state.
- Evaluation uses both current RAM and previous-frame RAM.
- Unlock state is persisted to disk.

---

## 🔬 Deep Dive
### `achievements.rs`
The OxideNES implementation lives in `achievements.rs` (`482` lines).

### Core Engine
`AchievementEngine` loads definitions from JSON, evaluates conditions via the `evaluate_conditions()` parser, and manages persistent unlock state.

### ROM Identification
The implementation includes a minimal MD5 implementation for ROM identification.

### Reference Implementations
In OxideNES, `AchievementEngine` snapshots RAM every frame, compares current and previous values, parses condition strings such as `0xH0075>0_S_0xH0760=1`, unlocks newly satisfied achievements, displays a popup, and persists the result.

---

## 🏋️ Practice
### Warm-Up (5 min)
- Write a condition for `score > 100` at `0x07DD`.
- Explain what a delta condition checks.
- Trace one frame of evaluation from RAM snapshot to persisted unlock state.

### Core Problems
- Break down `0xH0075>0_S_0xH0760=1` into its subconditions and explain why `_S_` matters.
- Explain why the engine must keep both current-frame RAM and previous-frame RAM.

### Challenge
- Design a multi-condition achievement that only unlocks after a state change and a value threshold are both satisfied in the same evaluation pass.

---

*See also:* [[Input Recording and TAS]], [[Lua Scripting Engine]], [[Netplay — UDP Multiplayer]], [[Extended Features Overview]]

## References
→ [[Sources Index]]