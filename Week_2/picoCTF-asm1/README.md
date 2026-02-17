## picoCTF — asm1

### Objective
Analyze a simple assembly function and determine the final value stored in a register.

---

### What I Did

1. Used `objdump -d` to disassemble the binary and view raw assembly.
2. Identified the function of interest and followed the instructions sequentially.
3. Tracked how registers (especially eax and ebx) were modified.
4. Simulated the arithmetic operations manually step by step.
5. Determined the final computed value required for the flag.

---

### How It Was Solved

The challenge required understanding how `mov`, `add`, and `sub` instructions manipulate register values. By carefully tracing register changes, I reconstructed the final output without executing the program blindly.

---

### What I Learned

- How data moves between registers using `mov`
- How arithmetic instructions modify CPU state
- How to read assembly line-by-line logically
- That assembly must be treated like a math equation executed sequentially
