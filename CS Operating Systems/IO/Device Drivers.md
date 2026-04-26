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
# Device Drivers

## 🎯 Intuition
**The Core Idea:** A **device driver** is the OS kernel module that encapsulates how to communicate with one class of hardware device and translates generic I/O requests into the device's specific protocol.

**Analogy:** A driver is like a bilingual interpreter at a UN meeting — each device speaks its own protocol, but the OS speaks a generic I/O language.

**Why It Matters:** Drivers are a major source of kernel crashes, so the quality of this translation layer strongly affects OS stability.

## ⚙️ Core Mechanics
### What a Driver Does
A driver sits between the device-independent OS layer and the hardware interrupt handler.

### Driver Responsibilities
1. **Initialisation**: detect the device, configure it (set baud rate, DMA channel, IRQ), register with the kernel.
2. **Request handling**: receive generic block/character requests; issue device commands; wait for completion (blocking or DMA).
3. **Interrupt servicing**: handle the completion interrupt; wake waiting threads; report errors.
4. **Cleanup**: release resources on driver unload or device removal.

### Kernel Module Model (Linux)
Linux drivers are compiled as loadable kernel modules (`.ko` files). They expose a standard interface (`file_operations` structure with function pointers for `open`, `read`, `write`, `ioctl`, `release`). The kernel maps a device file (e.g., `/dev/sda`) to the correct driver via major and minor device numbers.

```c
static struct file_operations my_fops = {
    .read  = my_read,
    .write = my_write,
    .open  = my_open,
};
```

## 🔬 Deep Dive
### Driver vs Kernel
Drivers run in kernel mode with full hardware access — a bug crashes the kernel (kernel oops / panic). This is why driver quality matters enormously for OS stability. Tanenbaum argues microkernels (where drivers run as user processes) provide better fault isolation.

### Driver Categories

| Category | Examples |
|----------|---------|
| Block device | SATA/NVMe disk, SD card, loop device |
| Character device | Serial port, keyboard, /dev/null, /dev/random |
| Network device | Ethernet NIC, Wi-Fi adapter, loopback |
| USB | USB host controller + device class drivers |
| GPU | DRM/KMS display drivers; CUDA/ROCm compute paths |

### Why `file_operations` and Major/Minor Numbers Matter
- The `file_operations` structure gives the kernel a uniform way to call driver entry points such as `open`, `read`, and `write`.
- Major and minor device numbers let the kernel route a device file to the correct driver and identify particular devices or subdevices managed by that driver.
- This design keeps the user-visible interface generic even though the underlying hardware protocol is device-specific.

## 🏋️ Practice
### Warm-Up
1. Why do Linux drivers use a `file_operations` structure?
2. What is the difference between a block device driver and a character device driver?
3. Why is driver code especially dangerous compared with ordinary user-space code?

### Core Problems
1. Explain how major and minor device numbers help the kernel map `/dev/...` files to the correct driver.
2. A network card finishes transmitting a packet. Which driver responsibility is involved first, and what typically happens next?
3. Why does a driver need both request-handling logic and interrupt-servicing logic?

### Challenge
1. How does a microkernel improve driver fault isolation compared with a monolithic kernel?
2. Suppose a GPU driver has a bug in kernel mode. Explain the likely system-level consequence and why Tanenbaum uses this as an argument for microkernels.

## Supporting Chunks

- [[IO - Device drivers form the OS-to-hardware interface translating generic to device-specific commands]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 5.
