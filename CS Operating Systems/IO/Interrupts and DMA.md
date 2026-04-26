---
tags:
  - csos
  - csos/io
confidence: verified
up: "[[IO Overview]]"
tier-coverage:
  - intuition
  - core
  - deep-dive
  - practice
---
# Interrupts and DMA

## 🎯 Intuition
**The Core Idea:** Interrupts let the CPU do useful work instead of polling devices, and DMA lets the CPU skip bulk data copying by handing the transfer to a dedicated controller.

**Analogy:** Interrupts are like a doorbell — you do not stand at the door waiting. DMA is like a delivery person who puts packages in your house while you keep working.

**Why It Matters:** Without interrupts and DMA, the CPU would waste huge amounts of time babysitting devices instead of executing processes and kernel work.

## ⚙️ Core Mechanics
### Interrupts
An **interrupt** is an asynchronous hardware signal that tells the CPU to stop what it is doing and handle a device event. Without interrupts, the CPU would have to busy-wait (poll) — wasting cycles checking whether a device is ready.

### Interrupt Vector Table
A fixed table in memory (or pointed to by IDTR on x86) maps each interrupt request number (IRQ) to the address of its handler routine. The table is set up by the OS at boot.

### Interrupt Lifecycle
```
Device signals IRQ line
    → CPU completes current instruction
    → CPU pushes flags + CS:IP (or PC + CPSR) to stack
    → CPU loads handler address from interrupt vector
    → Handler runs (saves registers, services device, sends EOI, restores)
    → CPU resumes interrupted code
```

### DMA — Direct Memory Access
**DMA** offloads large data movements (disk reads, network receive, GPU upload) from the CPU to a dedicated **DMA controller**. The CPU programs the DMA with:
- Source address
- Destination address
- Transfer count
- Transfer direction

The DMA controller then takes the memory bus and moves data autonomously, interrupting the CPU only once when the entire block is complete. A large disk read that would take thousands of CPU-cycle loops with programmed I/O takes a single interrupt with DMA.

## 🔬 Deep Dive
### Interrupt Priority and Masking
Hardware interrupt controllers (e.g., Intel 8259 PIC or APIC) assign priorities. The CPU can **mask** (disable) interrupts during critical sections to avoid re-entrant handler problems; interrupts are re-enabled when safe.

### PIC vs APIC
- The **8259 PIC** is the classic programmable interrupt controller used on older x86 systems.
- The **APIC** family supports more advanced interrupt routing and priority handling in modern systems.
- In both cases, the interrupt controller helps map device requests into the CPU's interrupt delivery mechanism.

### Bus Arbitration
The DMA controller must negotiate bus access with the CPU. Two modes:
- **Cycle stealing**: DMA takes one bus cycle at a time; CPU slows slightly.
- **Burst mode**: DMA holds the bus for the entire transfer; CPU stalls.

### Why These Trade-Offs Matter
- If interrupts are not masked during a critical section, a handler may run at an unsafe moment and create re-entrant state corruption.
- DMA is most valuable for large transfers because setup cost is paid once, then the block moves without CPU copy loops.
- Burst mode maximises DMA throughput but can stall the CPU because the DMA controller monopolises the memory bus for the duration of the transfer.

## 🏋️ Practice
### Warm-Up
1. What problem do interrupts solve compared with busy-wait polling?
2. What does the interrupt vector table map?
3. Which four values does the CPU program into a DMA controller before a transfer?

### Core Problems
1. What can go wrong if interrupts are not masked during a critical section?
2. Calculate the CPU savings of DMA versus programmed I/O for transferring 4 KB when programmed I/O requires 1 byte per CPU cycle of active copying.
3. Walk through the interrupt lifecycle from IRQ assertion to returning to interrupted code.

### Challenge
1. Why does burst mode DMA stall the CPU, while cycle stealing only slows it slightly?
2. Compare PIC and APIC at a high level. Why do modern systems prefer APIC-style interrupt handling?
3. A high-speed network card delivers large packets frequently. Explain why interrupts alone are not enough and why DMA is essential.

## Supporting Chunks

- [[IO - Interrupts allow devices to signal the CPU asynchronously without busy-waiting]]
- [[IO - DMA offloads bulk data transfers from the CPU to a dedicated controller]]

## See Also

- [[System Calls]] — the trap mechanism (syscall instruction) is architecturally similar to hardware interrupts
- [[CPU Scheduling]] — timer interrupts drive preemptive scheduling
- [[Disk Scheduling Algorithms]] — DMA completions trigger interrupts that feed the disk I/O scheduler
- [[Hypervisors]] — hypervisors must intercept and virtualise guest interrupt delivery

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 5.
