---
tags: [cs-os, raw]
source_type: textbook_topic
source_title: "Power Management in OS"
authors: Tanenbaum, Bos; Intel ACPI Specification
year: 2018
---

# Power Management in OS

## Summary

Operating system power management controls hardware energy consumption through standardized interfaces, primarily defined by the ACPI (Advanced Configuration and Power Interface) specification. ACPI provides a firmware-level abstraction that the OS uses to discover and manage power states across all system components.

ACPI defines system-level sleep states (S0–S5): S0 (fully operational), S1 (CPU caches flushed, CPU stopped but powered), S2 (CPU powered off), S3 (suspend-to-RAM—only DRAM powered, resume in seconds), S4 (hibernate—state saved to disk, all hardware off, resume in tens of seconds), and S5 (soft-off—mechanically powered off via software). Processor-level states include C-states and P-states. **C-states** control idle power: C0 (active execution), C1 (halt—clock stopped, ~10 μs wake), C2 (stop-clock, ~100 μs wake), C3 (sleep—caches may be flushed, ~1 ms wake), with deeper states saving more power but requiring longer wake-up latency. **P-states** (performance states) control active power by adjusting CPU voltage and frequency together—DVFS (Dynamic Voltage and Frequency Scaling). Lower P-states reduce voltage and frequency proportionally, saving power approximately cubically with voltage reduction (P ∝ V²f).

Linux implements CPU frequency scaling through the **cpufreq** subsystem with pluggable **governors**. The `performance` governor locks the CPU at maximum frequency. The `powersave` governor locks at minimum. The `ondemand` governor increases frequency to maximum when load is detected and decreases when idle. The `schedutil` governor (default since kernel 4.7 on many systems) integrates directly with the scheduler, using per-CPU utilization tracking to set frequency proportionally, achieving faster response than periodic sampling.

The **tickless kernel** (CONFIG_NO_HZ) eliminates periodic timer interrupts on idle CPUs, allowing them to remain in deep C-states longer. Without tickless support, the traditional 250 Hz or 1000 Hz tick would wake CPUs hundreds of times per second even when idle. The **race-to-idle** strategy maximizes throughput at full frequency to complete work quickly, then enters deep sleep—often more energy-efficient than running at a lower frequency for longer.

Mobile operating systems extend power management further. Android's wakelocks (now replaced by `WakeLockSentinel` and runtime power management APIs) prevent the system from sleeping while background tasks complete. iOS uses aggressive app suspension and coalesced timer firings to minimize wake-ups.

## Key Claims

- ACPI provides a standardized firmware interface for OS power management, defining system sleep states (S0–S5), processor idle states (C-states), and performance states (P-states) for dynamic voltage/frequency scaling
- C-states trade wake-up latency for power savings: deeper states (C3+) save more power but require millisecond-scale transition times, making state selection a latency-sensitive optimization
- Dynamic Voltage and Frequency Scaling (DVFS) exploits the cubic relationship between voltage and dynamic power (P ∝ V²f) to achieve significant energy savings at reduced performance levels
- The tickless kernel eliminates periodic timer interrupts on idle CPUs, allowing sustained deep C-state residency and reducing idle power consumption by up to 20–30% on server workloads
- Race-to-idle (completing work at maximum frequency then entering deep sleep) is often more energy-efficient than running slowly because leakage power dominates at low utilization

## Atomic Facts

1. ACPI S3 (suspend-to-RAM) preserves system state in DRAM while powering off nearly all components, consuming approximately 1–5 watts and resuming in 1–3 seconds
2. CPU C-state transitions are managed by the `intel_idle` or `acpi_idle` driver on Linux, which selects states based on expected idle duration using the menu or TEO (Timer Events Oriented) governor
3. P-state transitions on modern Intel processors are managed by Hardware P-states (HWP/Speed Shift), where the CPU autonomously adjusts frequency based on workload within OS-specified bounds
4. The Linux `schedutil` governor reads the scheduler's per-CPU `util_avg` metric to set frequency proportionally: frequency = max_freq × (util / max_util)
5. CONFIG_NO_HZ_FULL extends tickless operation to busy CPUs, eliminating timer ticks entirely for real-time or latency-sensitive workloads at the cost of increased scheduling overhead
6. Android's Doze mode (introduced in Android 6.0) batches background network access, syncs, and alarms into infrequent maintenance windows when the device is stationary and screen-off

## Significance

Power management is a critical OS function that directly impacts battery life, data center energy costs, and thermal management. The OS sits at the intersection of hardware power states and application demands, making power-aware scheduling and idle management essential responsibilities. Understanding power management is increasingly important as energy efficiency becomes a primary design constraint in mobile, IoT, and large-scale cloud computing, where electricity costs can dominate total cost of ownership.

## Chunks Extracted

*Pending*
